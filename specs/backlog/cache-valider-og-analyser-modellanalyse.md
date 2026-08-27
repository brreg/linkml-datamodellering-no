# Plan: Kjeldebasert caching i valider-og-analyser og modellanalyse-tvers-domene

**Kortnavn:** `cache-valider-og-analyser-modellanalyse`
**Dato:** 2026-08-27

---

## Bakgrunn

`.github/workflows/generate.yml` sin `generate`-jobb (matrise per domene) cachar
alt genererte artefakt under `generated/${{ matrix.domain }}/` med
`actions/cache@v6`, nøkla på ein hash av kjeldeskjemaa (`src/linkml/<domain>/**`)
pluss ein eksplisitt, grep-verifisert liste over "infra"-filer (Dockerfile,
scripts, templates, relevante `make/*.mk`) — sjå kommentaren over
`Cache genererte artefakter`-steget i `generate.yml` (linje 416-438). Alle
etterfølgjande steg er gata med `if: steps.cache-generated.outputs.cache-hit
!= 'true'`.

Dei to andre jobbane i same workflow — `valider-og-analyser` (matrise per
domene) og `modellanalyse-tvers-domene` (éin jobb) — har **ingen** caching i
dag. Dette var eit **medvite, dokumentert vedtak** (ikkje ei forgløymt
oppgåve) — sjå `specs/done/splitt-validering-modellanalyse-eigen-jobb.md`:

> **Caching:** ikkje cache den nye jobben. Sidan modellanalyse-delen alt er
> batcha ned til ~19 s og valideringa til ~16 s (til saman ~35 s), er
> cache-kompleksiteten ... ikkje verdt det.

Køyretidene i siste `generate`-workflow-køyring (2026-08-26, run 32967383776)
stadfestar at estimatet framleis stemmer — `valider-og-analyser` tek 25-47 s
per domene, `modellanalyse-tvers-domene` ~39 s. Brukar har likevel bekrefta
(2026-08-26) at caching skal innførast no, og at det tidlegare vedtaket
dermed vert reversert.

### Kjent avgrensing i mønsteret som vert kopiert (avklart med brukar)

`generate`-jobben sin cache-nøkkel er scopa til `src/linkml/<domain>/**` —
**ikkje** transitivt til domene skjemaet importerer. Fleire domene importerer
på tvers av domenegrensa (verifisert med grep av `imports:`-felt):

- `samt/samt-bu` → `ap-no/dqv-ap-no`
- `modellkatalog/{brreg,digdir,kartverket,ksdigital,novari,skatteetaten}-modellkatalog` → `ap-no/modelldcat-ap-no`
- `referanse/referansemodell` → `ap-no/dcat-ap-no`
- `begrepskatalog/brreg-begrepskatalog` → `ap-no/skos-ap-no`

Dette gapet er kjent frå før (`specs/done/generate-workflow-per-schema.md` §
"Cache-nøklar og importavhengigheiter" kalla det "problemet som gjenstår",
og valde medvite ein enklare strategi i første omgang). Brukar har bekrefta
(2026-08-26) at dei to nye cachane skal ha **same avgrensing** som
`generate`-jobben (domene-scopa hash, ingen transitiv import-oppløysing) —
altså **same kjende avvik vert arva**, ikkje introdusert på nytt. Merk at
`modellanalyse-tvers-domene` **ikkje** har dette problemet i det heile, sidan
`--scope all` uansett les heile `src/linkml/**`.

### Kallgraf verifisert (grep) for infra-delen av cache-nøklane

**`valider-og-analyser`** (steg "Valider alle skjema" + "Køyr modellanalyse
per skjema"):
- `src/assets/scripts/makefile/run-validation.sh` → kallar
  `src/mcp-linkml-validator/flatten-and-validate.bash` direkte via `bash`
  (ingen `make`-kall i kallgrafen — verifisert med grep, difor er
  `make/40-validation.mk` **ikkje** relevant her, i motsetnad til i
  `generate`-jobben der han dekkjer eit anna, meir grunnleggjande
  `make validate`-steg, jf. kommentaren i `generate.yml` linje 428-432)
- `flatten-and-validate.bash` monterer `server.py` og heile
  `policies/`-katalogen inn i `mcp-linkml-validator`-kontaineren
  (`-v .../server.py:/app/server.py:ro`, `-v .../policies:/app/policies:ro`)
- `src/assets/scripts/utils/validation_log.py` (delt loggstruktur, BUG-12,
  importert av det embedde Python-steget i `run-validation.sh`)
- `make analyse-similar-domene-batch` / `make analyse-lokal-modellanalyse-domene`
  → `make/91-modell-analyse.mk`, som brukar `$(PYTHON_RUN)`/`$(LINKML_RUN)`
  frå `make/01-containers.mk`, og `print_header`/`LOGLVL` frå
  `make/00-settings.mk`
- Tre statisk pulla images: `linkml-local` (`Dockerfile.linkml`),
  `python-pytest` (`Dockerfile.python`), `mcp-linkml-validator`
  (`Dockerfile.mcp-linkml`)
- `make/80-images.mk` — same grunngjeving som i `generate`-jobben:
  `.github/actions/pull-images` fell tilbake til `make <target>` ved GHCR-feil

**`modellanalyse-tvers-domene`** (steg "Køyr modellanalyse på tvers av
domene"):
- `make analyse-similar-alle-domene-batch` → same `make/91-modell-analyse.mk`
  + `make/00-settings.mk` + `make/01-containers.mk`
- Eitt pulla image: `python-pytest` (`Dockerfile.python`)
- `make/80-images.mk` (same fallback-grunngjeving)

## Tiltak

1. **Cache i `valider-og-analyser`** — legg til eit `actions/cache@v6`-steg
   rett etter `download-artifact@v8 (source)`, før "Oppgrader crun":
   ```yaml
   - name: Cache validering og modellanalyse (${{ matrix.domain }})
     id: cache-valider
     uses: actions/cache@v6
     with:
       path: generated/${{ matrix.domain }}/
       key: v1-valider-og-analyser-${{ matrix.domain }}-${{ hashFiles(format('src/linkml/{0}/**', matrix.domain)) }}-infra-${{ hashFiles('src/assets/scripts/makefile/run-validation.sh', 'src/assets/scripts/makefile/find-similar-names.py', 'src/assets/scripts/makefile/find-unused-local-definitions.py', 'src/assets/scripts/utils/validation_log.py', 'src/mcp-linkml-validator/flatten-and-validate.bash', 'src/mcp-linkml-validator/server.py', 'src/mcp-linkml-validator/policies/**', 'src/assets/containers/Dockerfile.linkml', 'src/assets/containers/Dockerfile.mcp-linkml', 'src/assets/containers/Dockerfile.python', 'make/00-settings.mk', 'make/01-containers.mk', 'make/80-images.mk', 'make/91-modell-analyse.mk', 'Makefile') }}
   ```
   Legg kommentar over `key:` som forklarer kallgraf-grunngjevinga frå
   Bakgrunn-seksjonen (same stil som `generate.yml` linje 421-437), inkl.
   den kjende domene-scopa import-avgrensinga.
   Gat desse fire eksisterande steg med
   `if: steps.cache-valider.outputs.cache-hit != 'true'`:
   "Oppgrader crun", "Logg inn på GHCR", "Last images inn i podman frå
   GHCR", "Valider alle skjema for ...", "Kopier valideringsloggar til
   generated/", "Køyr modellanalyse per skjema for ...". Sisste steg
   (`upload-artifact`) vert **ikkje** gata — skal alltid laste opp anten
   friskt generert eller cache-gjenoppretta innhald.

2. **Cache i `modellanalyse-tvers-domene`** — same mønster, éin jobb (ikkje
   matrise):
   ```yaml
   - name: Cache modellanalyse på tvers av domene
     id: cache-modellanalyse-tvers
     uses: actions/cache@v6
     with:
       path: generated/modell-analyse-tvers-domene/
       key: v1-modellanalyse-tvers-domene-${{ hashFiles('src/linkml/**') }}-infra-${{ hashFiles('src/assets/scripts/makefile/find-similar-names.py', 'src/assets/containers/Dockerfile.python', 'make/00-settings.mk', 'make/01-containers.mk', 'make/80-images.mk', 'make/91-modell-analyse.mk', 'Makefile') }}
   ```
   Gat "Oppgrader crun", "Logg inn på GHCR", "Last python-pytest frå GHCR",
   "Køyr modellanalyse på tvers av domene" med
   `if: steps.cache-modellanalyse-tvers.outputs.cache-hit != 'true'`.
   `upload-artifact` vert **ikkje** gata.

3. **Oppdater eksisterande forklarande kommentarar** som no vert utdaterte:
   - Kommentaren i `valider-og-analyser` (linje ~195-197: "Ikkje cacha (jf.
     modellanalyse-tvers-domene-jobben) — 35 s er billeg nok ...") må
     fjernast/erstattast, sidan han no direkte motseier koden.
   - Same for eventuell tilsvarande grunngjeving i
     `modellanalyse-tvers-domene`-jobben sin kommentar.
   - Legg til ei kort tilvising til denne specen (etter flytting til
     `specs/done/`) som forklarer kvifor vedtaket i
     `specs/done/splitt-validering-modellanalyse-eigen-jobb.md` vart
     reversert.

4. **Verifiser kallgrafen på nytt før merge** — grep-verifiser infra-lista i
   tiltak 1 og 2 mot faktisk kode (same metode som vart brukt i denne
   planlegginga), sidan feil/manglande filer i `infra`-hashen gir stille
   feil (stale cache-hit som ikkje fangar ei reell åtferdsendring) — jf.
   prinsippet "Ingen stille feil". Spesielt: dobbeltsjekk at
   `run-validation.sh` og dei to `analyse-*`-måla framleis ikkje har fått
   nye avhengigheiter (t.d. nye `make`-kall) sidan denne planen vart skriven.

5. **Test lokalt / i CI**
   - Køyr `podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/generate.yml`
     etter kvar endring (obligatorisk etter CI-workflow-endring, jf.
     CLAUDE.md).
   - Push og verifiser i Actions-loggen: (a) fyrste køyring etter endringa
     har `cache-hit: false` og køyrer alle steg normalt for begge jobbane,
     (b) ei påfølgjande køyring **utan** endring i kjelde/infra-filene gir
     `cache-hit: true` og hoppar over dei gata stega, (c) ei køyring med
     **berre** ei endring i eitt domene sitt skjema gir cache-miss **berre**
     for det domenet i `valider-og-analyser`-matrisa, ikkje for dei andre.
   - Stadfest at `publish`-jobben framleis får korrekt innhald frå
     `generated-<domain>-checks`- og
     `generated-modell-analyse-tvers-domene`-artefakta uavhengig av om dei
     kom frå cache eller frisk køyring.

6. **Avslutning** — når alle tiltak er verifiserte: legg til `## Utført`,

## Status (2026-08-27)

Tiltak 1, 2 og 3 er implementerte i `.github/workflows/generate.yml`.

Under tiltak 4 (grep-verifisering) vart eit reelt hòl i infra-lista funne og
retta før commit: `find-unused-local-definitions.py` (brukt av
`analyse-lokal-modellanalyse-domene`, køyrd via `LINKML_RUN`) importerer i
tillegg `src/assets/scripts/utils/linkml_relative_import_patch.py`, som
mangla i det opphavlege utkastet i denne specen. Lagt til i
`valider-og-analyser`-jobben sin cache-nøkkel.

**Attstår (krev handling frå brukar, ikkje LLM):**
- Tiltak 5, fyrste kulepunkt: `actionlint` mot `generate.yml`. Podman er
  ikkje tilgjengeleg i shell-miljøet LLM opererer i her — brukar må køyre
  denne sjølv:
  ```bash
  podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/generate.yml
  ```
- Tiltak 5, resten (push + verifiser cache-hit/-miss-åtferd i Actions-loggen
  for begge jobbane, stadfest `publish` framleis får korrekt innhald) — krev
  faktisk push, som LLM aldri utfører (jf. CLAUDE.md).

Specen vert flytta til `specs/done/` når brukar har stadfesta at
`actionlint` er reint og at CI-åtferda er verifisert som venta.
   flytt specen til `specs/done/`.
