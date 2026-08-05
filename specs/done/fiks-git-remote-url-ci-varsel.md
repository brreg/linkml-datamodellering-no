# Fiks konsekvent git-remote-URL-åtvaring i CI

## Bakgrunn

`gen-informasjonsmodell-instance` (køyrer for kvart skjema via
`make domain-<domain>`) skriv konsekvent denne åtvaringa i CI:

```
⚠️  Kunne ikkje lese git remote-URL frå /work/.git/config (/work/.git/config finst ikkje) — brukar fallback-URL
```

**Rotårsak:** `get_github_raw_base_url()` i
`src/assets/scripts/makefile/generate-informasjonsmodell.py` les
`.git/config` inne i containeren, med kommentaren "repoet, inkl. .git/, er
alltid mounta". Det stemmer for lokal `make`-bruk (`.git/` er alltid del av
repo-rota som vert mounta via `$(CURDIR):/work`), men **ikkje** for
`generate`-jobben i CI: `checkout-source`-jobben i `.github/workflows/generate.yml`
lastar opp kjeldekoda som eit artifact med berre `src/`, `mkdocs/`,
`.github/`, `Makefile`, `make/`, `README.md`, `CODEOWNERS.md` (linje 69-81)
— aldri `.git/`. `generate`-jobben lastar dette artifactet, ikkje eit
`actions/checkout`-resultat, så `.git/` finst aldri der.

Resultat: åtvaringa fyrer deterministisk kvar gong (éin gong per skjema,
~30+ gonger per full generate-køyring) — reint støy, sidan
fallback-verdien (`brreg/linkml-datamodellering-no`) tilfeldigvis er
korrekt for dette repoet.

## Steg

1. Endre `get_github_raw_base_url()` til å prioritere miljøvariabelen
   `GITHUB_REPOSITORY` (sett automatisk av GitHub Actions i alle jobb-shell,
   format `owner/repo`) — direkte og korrekt i CI, krev ikkje `.git/` i det
   heile.
2. Behald dagens `.git/config`-lesing som fallback #2 (lokal utvikling, der
   `.git/` er mounta).
3. Behald hardkoda fallback (`brreg/linkml-datamodellering-no`) som siste
   utveg, med åtvaringa framleis skriven til stderr — men berre når
   **verken** `GITHUB_REPOSITORY` eller eit brukbart `.git/config` finst.
4. Legg til `-e GITHUB_REPOSITORY` på `PYTHON_RUN`-wrapparen i
   `make/01-containers.mk`, slik at miljøvariabelen (når sett av CI) vert
   vidareført inn i containeren. Trygt no-op lokalt der ho ikkje er sett.
5. Test lokalt: køyr scriptet både med og utan `GITHUB_REPOSITORY` sett, for
   å stadfeste at rett URL vert generert i begge tilfelle, og at åtvaringa
   berre kjem når begge kjeldene manglar.

## Handlingsliste

- [x] Endre `get_github_raw_base_url()` med `GITHUB_REPOSITORY`-prioritet
- [x] Legg til `-e GITHUB_REPOSITORY` på `PYTHON_RUN` i `01-containers.mk`
- [x] Lokal test: `GITHUB_REPOSITORY` sett → korrekt URL, ingen åtvaring
- [x] Lokal test: `GITHUB_REPOSITORY` usett, `.git/config` finst → korrekt URL (som før)
- [x] Lokal test: begge manglar → fallback-URL + åtvaring (som før)
- [x] Commit-melding

## Utført

`get_github_raw_base_url()` sjekkar no `GITHUB_REPOSITORY`-miljøvariabelen
først (sett automatisk av GitHub Actions), før `.git/config`-fallback og
hardkoda siste-utveg. `PYTHON_RUN` i `make/01-containers.mk` vidarefører
`GITHUB_REPOSITORY` frå host-shellet inn i containeren via `-e
GITHUB_REPOSITORY`.

Testa direkte mot `localhost/python-pytest:latest`-containeren i tre
scenario:
- `GITHUB_REPOSITORY` sett → korrekt URL, ingen åtvaring
- `GITHUB_REPOSITORY` usett, `.git/config` mounta → korrekt URL via
  `.git/config` (uendra frå før), ingen åtvaring
- Verken `GITHUB_REPOSITORY` eller `.git/` tilgjengeleg (simulert med
  isolert katalog utan `.git/`) → fallback-URL + åtvaring på stderr, som før

I CI vil `generate`-jobben (som aldri har `.git/` — sjå `checkout-source`
sitt artifact-innhald i `generate.yml`) no bruke `GITHUB_REPOSITORY` og
aldri vise åtvaringa. Lokal `make`-bruk er uendra (fell gjennom til
`.git/config` sidan `GITHUB_REPOSITORY` normalt ikkje er sett der).
