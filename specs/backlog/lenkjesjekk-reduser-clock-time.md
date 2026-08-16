# Reduser klokketid for lenkjesjekk-jobben

## Bakgrunn

`lenkjesjekk`-jobben i `.github/workflows/lenkje-og-mermaid-sjekk.yml` er
den klart tyngste jobben i workflowen. Faktisk steg-for-steg-tidsbruk henta
frå to nylege køyringar via GitHub API (`gh api
repos/.../actions/jobs/<id>` → `.steps[].started_at/completed_at`):

**Køyring [31936115357](https://github.com/brreg/linkml-datamodellering-no/actions/runs/31936115357)
(2026-08-16 08:19–08:27, etter purl.org-throttling, før kategori 1–6-fiksane):**

| Steg | Tid | Del av total |
|---|---|---|
| Sjekk ut repo | 2s | <1 % |
| Slå saman genererte domene-artefakt | 4s | <1 % |
| Logg inn på GHCR | 5s | <1 % |
| Last mkdocs-local/python-pytest (parallelt) | 6s | 1 % |
| **Publiser og bygg dokumentasjonsportal** (docs-publish + docs-build) | **2m 28s (148s)** | **33 %** |
| Trekk inn lychee | 2s | <1 % |
| **Sjekk lenkjer i dokumentasjon** (sjølve lychee-køyringa) | **4m 42s (282s)** | **62 %** |
| Last opp lenkjesjekk-rapport | 1s | <1 % |
| **Total (lenkjesjekk-jobben åleine)** | **7m 34s (454s)** | 100 % |

To steg står for 95 % av lenkjesjekk-jobben si eiga klokketid. Alt anna i
sjølve jobben er støy. **Merk:** denne tabellen dekkjer berre
`lenkjesjekk`-jobben — han har `needs: [checkout-source, generate]`, så den
matriserte `generate`-jobben (sjå tiltak 3) sin eigen køyretid legg seg
**framfor** desse 454 sekunda i den totale pipeline-tida frå trigger til
lenkjesjekk er ferdig.

**Samanlikningsdata:** Køyring
[31931289364](https://github.com/brreg/linkml-datamodellering-no/actions/runs/31931289364)
(06:23–06:31, **før** purl.org-throttling, med 962 falske 429-funn) brukte
berre 3m 47s (227s) på lenkjesjekk-steget — altså **raskare** enn den
seinare, meir korrekte køyringa (282s). Dette stadfestar at
purl.org-throttlinga (opphavleg `concurrency = 2`, `request_interval = "1s"`
i `.github/lychee.toml`) har eit reelt, målbart klokketid-kostnad:
pålitelege lenkjer tek lengre tid enn upålitelege-men-raske lenkjer. Denne
kostnaden vart medviten akseptert i `specs/done/lenkjesjekk-purl-org-429.md`
(riktig prioritering av korrekt før rask) — sjå tiltak 4 for oppfølging.

**Lychee sin eigen `# Summary`-tabell** (frå siste lokale full-køyring i
`specs/done/lenkjesjekk-3817-feil-evaluering.md`) syner omfanget lychee-steget
faktisk handterer:

| Status | Tal |
|---|---|
| Total (alle lenkje-*referansar*, inkl. duplikat på tvers av filer) | ~94 000 |
| **Unique** (faktisk distinkte URL-ar, det som avgjer nettverkskostnaden) | ~10 000 |
| Successful | ~90 000 |
| Errors | ~3 300 |

Lychee dedupliserer nettverksoppslag internt i éin køyring (Unique ≈ 10 000
mot Total ≈ 94 000), så nettverkskostnaden er alt avgrensa til dei unike
URL-ane, ikkje kvar enkelt referanse. Dei ~3300 feila lenkjene går gjennom
`max_retries = 2` × `retry_wait_time = 5s` kvar (opptil 10s ekstra
ventetid per feila lenkje, avhengig av per-host-kø), noko som også bidreg
merkbart til dei 282 sekunda.

## Tiltak, prioritert etter venta gevinst/kompleksitet

### 1. [Utført] Cache lychee sitt eige HTTP-request-cache på tvers av køyringar

Lychee støttar eit persistert på-disk-cache (`.lycheecache`) via
`cache = true` + `max_cache_age` i config — no slått på:

```toml
cache = true
max_cache_age = "1d"
```

`actions/cache@v6` lagt til i `lenkjesjekk`-jobben (før «Trekk inn
lychee»), key `lychee-cache-${{ github.run_id }}` (alltid unik → alltid ny
cache lagra ved jobbslutt) med `restore-keys: lychee-cache-` (hentar siste
tilgjengelege cache uavhengig av eksakt nøkkel). `.lycheecache` lagt til
`.gitignore`. `actionlint` stadfesta ingen `[expression]`-feil.

**Ikkje målt i praksis enno** — krev to påfølgjande CI-køyringar
(`workflow_dispatch`) for å samanlikne kald- mot varm-cache-tid, sjå
"Steg" nedanfor.

### 2. [Utført] Cache mkdocs/docs + mkdocs/site-bygget

`actions/cache@v6` lagt til rundt `mkdocs/docs/` + `mkdocs/site/`,
cache-key hasha på `generated/**` + eksplisitt fil-liste (`mkdocs/publish.sh`,
`mkdocs/lib/**`, `README.md`, `src/mcp-linkml-validator/policies/README.md`,
`src/assets/scripts/makefile/generate-readme-tables.sh`, dei statiske
rettleiingskatalogane `kom-i-gang/arkitektur/publisering/automasjon/
stylesheets/javascripts`, `make/50-docs.mk`, `Makefile`) — same eksplisitte
mønster som `generate.yml` (unngår at eit breitt `**`-mønster invaliderer
cachen unødig, jf. `specs/done/docs-only-endring-cache-miss-alle-domene.md`).
`make docs-publish`/`make docs-build` er no betinga på cache-miss
(`if: steps.cache-docs.outputs.cache-hit != 'true'`); eit nytt steg «Hopp
over bygg (cache-treff)» skriv ei kort forklarande linje til
`$GITHUB_STEP_SUMMARY` på cache-treff, sidan «MkDocs
build-åtvaringar»-seksjonen elles ikkje ville vorte fylt.

**Viktig atterhald (uendra frå opphavleg vurdering):** `make docs-build` sin
eigen mkdocs-validering køyrer **ikkje** på cache-treff — akseptabelt sidan
uendra innhald pr. definisjon alt vart validert då cachen vart skriven,
men eit medvite, dokumentert tradeoff.

**Ikkje målt i praksis enno**, same grunngjeving som tiltak 1.

### 3. [Ny, ikkje implementert] Cache genererte artefakter i denne workflowen sin eigen `generate`-matrise

**Oppdaga under gjennomgang:** `lenkje-og-mermaid-sjekk.yml` har si **eiga**
`generate`-jobb (line 46–92, matrisert per domene, kallar
`./.github/actions/generate-domain` og lastar opp resultatet som
artefakt) — **heilt separat** frå den identisk namngjevne og
identisk formåla `generate`-jobben i `generate.yml`. I motsetnad til
`generate.yml` sin versjon (som cachar `generated/${{ matrix.domain }}/`,
line 153–169) har **denne** `generate`-jobben inga cache i det heile —
han regenererer alle artefakt for alle domene **kvar einaste køyring**,
sjølv når `src/linkml/<domain>/**` ikkje har endra seg sidan sist.

Sidan `lenkjesjekk` har `needs: [checkout-source, generate]`, tel denne
jobben si køyretid med i den totale ventetida frå trigger til lenkjesjekk
kan starte — dette tiltaket ligg **utanfor** dei 454 sekunda målt i
"Bakgrunn" over, men reduserer den reelle totale pipeline-tida.

- Legg til same `actions/cache@v6`-steg som `generate.yml` line 153–169,
  **med identisk cache-key-formel**
  (`v4-generated-${{ matrix.domain }}-${{ hashFiles(format('src/linkml/{0}/**', matrix.domain)) }}-infra-${{ hashFiles(...) }}`,
  same fil-liste som `generate.yml` sin infra-del), rett før «Generer alle
  artefakter for ${{ matrix.domain }}»-steget (line 83–86).
- Gjer sjølve genereringssteget betinga:
  `if: steps.cache-generated.outputs.cache-hit != 'true'`.
- **Verdifull bieffekt av identisk nøkkel:** sidan GitHub Actions-cache er
  delt på tvers av workflowar i same repo (ikkje per-workflow-isolert), vil
  denne jobben kunne **gjenbruke cache skriven av `generate.yml`** sjølv om
  `generate.yml` sist køyrde i ein heilt annan workflow-køyring (t.d. ved
  push til main tidlegare same dag/veke) — og omvendt. Dette er den einaste
  av dei føreslegne tiltaka som potensielt kan gje **null** ekstra
  genereringstid for uendra domene, heilt utan eiga oppvarming.
- Same steg for `actions/upload-artifact@v7` (line 88–92) held fram
  uendra — cache-treffet fyller `generated/${{ matrix.domain }}/` slik at
  opplastinga framleis har innhald å laste opp.

### 4. [Ny, ikkje implementert] Legg til matrisert `ensure-images`-jobb med registry-basert caching

**Oppdaga under vidare gjennomgang:** `generate.yml` har ein eigen,
matrisert `ensure-images`-jobb (line 75–122) som køyrer **før**
`generate`-jobben: éin matrise-celle per image i
`src/assets/containers/images.json`, som via `./.github/actions/ensure-image`
sjekkar om det innhaldshasha imaget alt finst i GHCR (`skopeo inspect`), og
berre byggjer + pushar dersom det manglar. Dette er ein registry-basert
cache — bygg skjer maksimalt éin gong per unikt innhald, uavhengig av kor
mange nedstraums-jobbar/matrise-celler som treng imaget.

`lenkje-og-mermaid-sjekk.yml` har **inga tilsvarande jobb**. I staden
pullar både `generate`- og `lenkjesjekk`-jobbane images direkte via
`./.github/actions/pull-images`, som **fell tilbake til eit fullt lokalt
`make <target>`-bygg i kvar einskild matrise-celle** dersom GHCR-pullen
feilar (t.d. eit image-tag som endå ikkje er bygd/pusha) — stadfesta i
`pull-images/action.yml`: `"⚠ GHCR-pull feila ... — byggjer lokalt"`. Utan
ein upstream `ensure-images`-jobb kan dette i verste fall bety at **alle
10 domene-cellene i `generate`-matrisa** byggjer det same manglande imaget
lokalt og parallelt — full duplisert byggjekostnad multiplisert med talet
på matrise-celler, i staden for éin gong.

- Legg til `images: ${{ steps.image-tags.outputs.images }}` i
  `checkout-source` sin `outputs:`-blokk (line 20–23) — `compute-image-tags`
  produserer alt dette internt (stadfesta identisk i `generate.yml` line
  51), det manglar berre i output-lista her.
- Legg til ein ny `ensure-images`-jobb, **kopiert verbatim** frå
  `generate.yml` line 75–122 (same matrise over
  `needs.checkout-source.outputs.images`, same `ensure-image`-composite-
  action-kall).
- Legg til `ensure-images` i `needs:`-lista til både `generate`- og
  `lenkjesjekk`-jobbane (dei pullar framleis sjølve via `pull-images`, men
  no garantert mot eit GHCR som alt har det dei treng — fallback-grena i
  `pull-images` bør då aldri triggast i normal drift).

### 5. [Utført] Stram inn purl.org-throttlinga

Verifisert empirisk mot heile repoet (tre iterasjonar):

| Innstilling | 429-funn |
|---|---|
| `concurrency = 2`, `request_interval = "1s"` (opphavleg) | 0 |
| `concurrency = 4`, `request_interval = "500ms"` | **9** (for aggressivt) |
| `concurrency = 3`, `request_interval = "800ms"` | **0** ✓ |

`.github/lychee.toml` er sett til `concurrency = 3`/`request_interval =
"800ms"` — ei reell innstramming frå opphavleg (2/1000ms) som framleis
held 0 429-funn. `actionlint` stadfesta ingen `[expression]`-feil.

### 6. Hald fram å redusere talet på broken/retried lenkjer

Reint korrekt talet på feila lenkjer (~3300 att, ned frå 3836) påverkar
klokketid direkte via `max_retries`/`retry_wait_time`-serialisering per
vert. Kvar kategori-fiks frå oppfølgingsarbeidet nemnt i "Merk"-seksjonen i
`specs/done/lenkjesjekk-3817-feil-evaluering.md` (t.d.
`data.norge.no/concepts`-UUID-ane, `cccevno`-namneromma) gjev både betre
rapportkvalitet **og** mindre klokketid, sidan færre lenkjer treng
retry-ventetid. Diminishing returns samanlikna med tiltak 1–5, men reelt.

### 7. Vurder matrise-parallellisering av sjølve lychee-køyringa (høgast kompleksitet)

`generate`-jobben er alt matrisert per domene
(`.github/workflows/generate.yml` line 125–133, og tilsvarande i denne
workflow-fila sin eigen `generate`-jobb, jf. tiltak 3). Ein tilsvarande
matrise for `lenkjesjekk` (t.d. éin lychee-instans per domene-katalog under
`mkdocs/docs/<domain>/**` + éin for resten av repoet) ville parallellisere
sjølve 282-sekundars lychee-steget på tvers av fleire runnarar, og kunne gje
den største **isolerte** forbetringa i dette eine steget. Kompleksitet:
- Krev å dele opp `**/*.md`-globet meiningsfullt utan å køyre same fil i
  fleire matrise-cellar.
- Mister noko av lychee sin **interne** dedupliseringsgevinst (same URL i to
  ulike matrise-cellar vert no sjekka to gonger, ein gong per celle, sidan
  cachen ikkje er delt på tvers av parallelle jobbar i same køyring —
  **med mindre** tiltak 1 sitt persisterte cache er implementert fyrst, som
  då også deler last mellom matrise-cellar via same `.lycheecache`).
- Krev å aggregere N delrapportar til éi samla oppsummering
  (`lenkjesjekk-report.md` + `$GITHUB_STEP_SUMMARY`) — meir CI-kompleksitet
  å vedlikehalde.

Tilrådd **berre** dersom tiltak 1–6 til saman ikkje gjev tilstrekkeleg
gevinst, sidan kompleksiteten er vesentleg høgare enn dei føregåande.

## Steg

1. ~~Implementer tiltak 1 (lychee-cache)~~ **[Utført]**
2. Mål effekt av tiltak 1: køyr workflowen (`workflow_dispatch`) to gonger
   på rad, samanlikn "Sjekk lenkjer i dokumentasjon"-tida for køyring 2
   (cache-treff) mot køyring 1 (cache-miss, kald cache). **Ikkje gjort enno
   — krev faktisk CI-køyring, ikkje mogleg å simulere lokalt sidan
   cache-mekanismen er GitHub Actions-spesifikk.**
3. ~~Implementer tiltak 2 (docs-publish/docs-build-cache)~~ **[Utført]**
4. Mål effekt av tiltak 2, tilsvarande steg 2, for "Publiser og bygg
   dokumentasjonsportal"-steget. **Ikkje gjort enno, same grunngjeving.**
5. Implementer tiltak 3 (cache `generate`-matrisa i denne workflowen):
   legg til `actions/cache@v6` med identisk key-formel som `generate.yml`,
   gjer genereringssteget betinga.
6. Mål effekt av tiltak 3 tilsvarande steg 2/4, for `generate`-jobben sin
   eigen køyretid (ikkje del av dei 454 sekunda i "Bakgrunn").
7. Implementer tiltak 4 (`ensure-images`-matrisejobb): legg til
   `images`-output i `checkout-source`, kopier `ensure-images`-jobben
   verbatim frå `generate.yml`, legg `ensure-images` til `needs:` for
   `generate` og `lenkjesjekk`.
8. Mål effekt av tiltak 4: vanskeleg å måle isolert i normal drift (sidan
   GHCR-images normalt alt finst frå ein tidlegare `generate.yml`-køyring),
   men stadfest at fallback-bygget i `pull-images` ikkje lenger triggast i
   ei normal nattleg køyring (sjekk loggen for "byggjer lokalt"-linjer —
   skal ikkje finnast når `ensure-images` har køyrt fyrst).
9. ~~Implementer tiltak 5 (stram inn purl.org-throttling)~~ **[Utført,
   verifisert lokalt: 0 429-funn med concurrency=3/800ms]**
10. `actionlint` etter kvar CI-endring (obligatorisk, jf. CLAUDE.md) —
    **gjort for tiltak 1, 2 og 5; må gjerast på nytt etter tiltak 3 og 4.**
11. Vurder tiltak 6/7 som eiga oppfølging basert på målt gevinst frå 1–5.

## Handlingsliste

- [x] Tiltak 1: lychee-cache (`cache`/`max_cache_age` + `actions/cache`)
- [ ] Mål og dokumenter effekt av tiltak 1 (krev CI-køyring)
- [x] Tiltak 2: cache mkdocs/docs + mkdocs/site, betinga bygg
- [ ] Mål og dokumenter effekt av tiltak 2 (krev CI-køyring)
- [ ] Tiltak 3: cache `generate`-matrisa i lenkje-og-mermaid-sjekk.yml
      (same nøkkel-formel som generate.yml)
- [ ] Mål og dokumenter effekt av tiltak 3 (krev CI-køyring)
- [ ] Tiltak 4: legg til `ensure-images`-matrisejobb (kopiert frå
      generate.yml) + `images`-output i checkout-source + `needs:`-oppdatering
- [ ] Stadfest at `pull-images` sin fallback-bygg ikkje triggast etter
      tiltak 4 (krev CI-køyring)
- [x] Tiltak 5: stram inn purl.org-throttling — verifisert 0 429-funn med
      `concurrency=3`/`request_interval=800ms`
- [x] `actionlint` for tiltak 1, 2, 5
- [ ] `actionlint` for tiltak 3 og 4
- [ ] Vurder tiltak 6/7 som oppfølging basert på målt gevinst
