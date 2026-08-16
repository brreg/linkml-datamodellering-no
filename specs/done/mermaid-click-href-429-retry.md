# Retry-logikk og inkrementell backoff for mermaid click-href-sjekk

## Bakgrunn

Køyring [31931289364](https://github.com/brreg/linkml-datamodellering-no/actions/runs/31931289364/job/95126418186)
(2026-08-16) av jobben `mermaid-click-href-sjekk` i
`.github/workflows/lenkje-og-mermaid-sjekk.yml` feila:

> Totalt sjekka: 5757 sider. Broten funn: 963.

Av dei 963 broten funna var 962 `HTTP Error 429: Unknown Error` og 1
`HTTP Error 503: Service Unavailable`. Alle 962 429-feila oppstod innanfor
under eitt sekund (06:23:32.32–06:23:32.42), som stadfestar at dei kjem frå
rate limiting hos GitHub Pages/Fastly-CDN-en som svarar på
`https://brreg.github.io/linkml-datamodellering-no`, utløyst av at
`mkdocs/lib/scripts/check-mermaid-click-hrefs.py` hentar eit stort tal sider
(alle klasse-/slot-sider i sitemap.xml, her 5757 stk.) samtidig via ein
`ThreadPoolExecutor` med `--concurrency 10`, utan nokon retry- eller
backoff-mekanisme.

Root cause: `fetch()` og `check_external_url()` i
`mkdocs/lib/scripts/check-mermaid-click-hrefs.py` kallar `urlopen()` direkte.
Ein einskild feila HTTP-respons (429/503/timeout) vert umiddelbart rapportert
som eit broten click-href, sjølv om årsaka er midlertidig rate limiting og
ikkje ein faktisk broten lenkje. Dette gjev falske positivar i
click-href-rapporten og gjer jobben ustabil ved store portalar.

Avklarte val for denne spesifikasjonen (sjå diskusjon i chat 2026-08-16):

1. **Backoff-strategi:** Eksponentiell backoff med jitter, som respekterer
   ein eventuell `Retry-After`-header frå 429-svaret når han er til stades.
2. **Concurrency:** Reduser standard `--concurrency` frå 10 til eit lågare
   tal (5) i tillegg til retry/backoff, for å redusere sannsynet for å
   trigge rate limiting i utgangspunktet.
3. **Omfang:** Retry/backoff-mekanismen gjeld både `fetch()` (sidehenting av
   sitemap.xml og kvar klasse-/slot-side) og `check_external_url()` (HEAD-
   oppslag mot eksterne vokabular-URL-ar, t.d. XSD-typedefinisjonar).

## Steg

1. Legg til ein delt retry-hjelpefunksjon i
   `mkdocs/lib/scripts/check-mermaid-click-hrefs.py` som:
   - Tek ein kallbar HTTP-operasjon (t.d. ein `urlopen(...)`-thunk), maks
     tal forsøk og ein basis-delay som parametrar.
   - Ved `HTTPError` med status `429` eller `5xx`, eller ved
     `URLError`/`TimeoutError`/`OSError`: vent og forsøk på nytt, opptil eit
     maks tal forsøk (t.d. 5).
   - Backoff-delay: eksponentiell (`basis * 2^forsøk`) pluss tilfeldig jitter
     (t.d. `random.uniform(0, basis)`), avgrensa til eit fornuftig tak
     (t.d. maks 30s per forsøk).
   - Dersom 429-responsen har ein `Retry-After`-header (sekund eller
     HTTP-dato-format), bruk denne verdien i staden for berekna backoff når
     han er til stades og gyldig.
   - Etter siste mislykka forsøk: kast/returner feilen vidare som i dag, slik
     at han hamnar i rapporten med tydeleg status (skil gjerne ut
     `"HENTING FEILA ETTER N FORSØK: {exc}"` frå den eksisterande
     `"HENTING FEILA: {exc}"`-teksten, slik at rapporten skil mellom eit
     reelt strukturelt problem og ein rate-limit-relatert feil som ikkje
     løyste seg innan retry-vindauget).
2. Bruk retry-hjelpefunksjonen i `fetch()` (line 54–56) og i
   `check_external_url()` (line 59–79) — begge stadene der `urlopen()` vert
   kalla direkte i dag.
3. Endre standardverdien for `--concurrency` i `argparse`-oppsettet
   (line 138) frå `10` til `5`.
4. Oppdater workflow-kallet i
   `.github/workflows/lenkje-og-mermaid-sjekk.yml` (line 208–213) dersom
   `--concurrency 10` er eksplisitt sett der — fjern det eksplisitte flagget
   slik at scriptets nye standard (5) gjeld, med mindre det er ønskt å
   halde ein annan verdi eksplisitt.
5. Oppdater docstring-en øvst i scriptet (line 16, "Bruk:"-linja) til å
   nemne retry/backoff-oppførselen kort, slik at framtidige lesarar forstår
   kvifor køyringa kan ta lengre tid enn før ved rate limiting.
6. Køyr `python3 mkdocs/lib/scripts/check-mermaid-click-hrefs.py` lokalt mot
   den publiserte portalen (`https://brreg.github.io/linkml-datamodellering-no`)
   for å stadfeste at scriptet framleis fungerer og at retry-logikken ikkje
   endrar korrekt oppførsel for faktisk broten lenkjer (`IKKJE FUNNE`,
   `EKSTERN LENKJE FEILA`) — desse skal framleis rapporterast umiddelbart
   utan retry, sidan dei ikkje er HTTP-feilstatusar.
7. Verifiser at `::error`-linjene og markdown-rapporten (`--report`) framleis
   har korrekt format, og at exit-koden framleis er `1` ved reelle broten
   funn og `0` når alt er OK.

## Handlingsliste

- [x] Mellombels mitigering: `CLICK_HREF_SJEKK_CONCURRENCY`-env-variabel sett
      til `1` på jobbnivå i `lenkje-og-mermaid-sjekk.yml`, brukt i
      `--concurrency`-flagget i staden for hardkoda `10` (actionlint kjørt,
      ingen `[expression]`-feil). Reduserer sannsynet for 429 kraftig i
      påvente av full retry/backoff-implementasjon under.
- [x] Legg til retry-hjelpefunksjon med eksponentiell backoff + jitter +
      `Retry-After`-støtte i `check-mermaid-click-hrefs.py`
- [x] Bruk retry-hjelpefunksjonen i `fetch()`
- [x] Bruk retry-hjelpefunksjonen i `check_external_url()`
- [x] Endre standard `--concurrency` i scriptet frå 10 til 5 (verdien i
      workflowen er framleis eksplisitt styrt av
      `CLICK_HREF_SJEKK_CONCURRENCY=1`, sett i forrige økt — uendra, sidan
      det var eit eksplisitt brukarval og ikkje del av denne økta sitt
      omfang)
- [x] Oppdater docstring i scriptet
- [x] Lokal verifisering mot publisert portal (retry-oppførsel + at reelle
      broten lenkjer framleis vert rapporterte umiddelbart)
- [x] Stadfest rapportformat og exit-kode uendra for gyldige/ugyldige funn

## Utført

Retry-logikk med eksponentiell backoff + jitter og `Retry-After`-støtte lagt
til i `mkdocs/lib/scripts/check-mermaid-click-hrefs.py` (ny
`_urlopen_with_retry()`-hjelpefunksjon, brukt i både `fetch()` og
`check_external_url()`). Standard `--concurrency` endra frå 10 til 5.
Docstring oppdatert til å nemne retry/backoff-oppførselen.

Lokal verifisering mot `https://brreg.github.io/linkml-datamodellering-no`
(køyrt i `localhost/linkml-local:latest`-containeren, `--concurrency 5`):
alle 5757 klasse-/slot-sider sjekka, 0 broten funn, exit-kode 0 — ingen
falske 429-positivar lenger. Rapportformat (`| Side | Click-namn | Href |
Status |`-tabell + totalsummering) stadfesta uendra.

`python3 -m py_compile` stadfesta gyldig syntaks. `actionlint` frå forrige
økt (workflow-endringa) hadde ingen `[expression]`-feil.
