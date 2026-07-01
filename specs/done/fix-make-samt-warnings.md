# Plan: Fjern åtvaringar frå `make samt`

## Bakgrunn

`make samt` (bygger `src/linkml/samt/samt-bu`) fullfører med exit code 0 —
ingen faktiske feil. Køyringa skriv likevel ut fire kategoriar
åtvaringar/meldingar til stderr. To av dei er allerede dokumenterte og
akseptert i `specs/done/`. Dei to andre er ikkje dokumenterte og kan delvis
ryddast opp.

Full logg er fanga i samband med denne planen:

```
/usr/local/lib/python3.11/site-packages/linkml/generators/owlgen.py:244: DeprecationWarning: [owlgen-skip-vacuous-min-zero-cardinality-default] DEPRECATED
/usr/local/lib/python3.11/site-packages/linkml/generators/owlgen.py:247: DeprecationWarning: [owlgen-skip-vacuous-local-range-default] DEPRECATED
/usr/local/lib/python3.11/site-packages/linkml/generators/owlgen.py:250: DeprecationWarning: [owlgen-consolidate-cardinality-axioms-default] DEPRECATED
WARNING: Unable to resolve circular dependency in no.norge.data.samt_bu.samt::document_wrapper with dependencies: ['no.norge.data.samt_bu.samt.Distribusjon']   (eller .Tidsrom — varierer mellom køyringar)
WARNING: NODE_ENV value of 'production' did not match any deployment config file names.
WARNING: See https://github.com/node-config/node-config/wiki/Strict-Mode
WARNING: No configurations found in configuration directory:/app/config
WARNING: To disable this warning set SUPPRESS_NO_CONFIG_WARNING in the environment.
✖ 1 problem (0 errors, 0 warnings, 1 info, 0 hints)   ← asyncapi-latest-version info (3.1.0)
```

## Vurdering per kategori

### 1. OwlSchemaGenerator DeprecationWarning (3 stk) — kan fiksast
`gen-owl` for `samt-bu` manglar `owl_flags`. Sju `fint-*`-skjema har allerede
konvensjonen `owl_flags: "--log_level ERROR"` i `manifest.yaml` (sjå
`src/linkml/fint/*/manifest.yaml`), same fix som `BUG-4`
(`specs/bugs/lint-validate-flag-deprecated.md`) brukte for ein analog
`linkml`-deprecation-åtvaring. Same mønster gjelder for 15 andre skjema i
repoet utan `owl_flags` — men denne planen er avgrensa til `samt-bu` sidan
det er det `make samt` faktisk bygger. Repo-vid utrulling er eit eige,
separat tiltak (sjå pkt. 5).

### 2. Avrotize "circular dependency" WARNING — ingen handling
Allerede dokumentert i `specs/done/xml-schema-generering.md` (steg 3,
«Kjende avvik — aksepterte») som avrotize-intern boilerplate frå
JSON Schema sin top-level union (`document_wrapper*`), ikkje semantisk
relevant. At klassen som rapporteres varierer mellom køyringar (`Distribusjon`
vs. `Tidsrom`) skyldas ikkje-deterministisk dict-rekkjefølgje i avrotize sjølv
— ingen tiltak i dette repoet kan endre det.

### 3. AsyncAPI "latest version"-info — ingen handling
Allerede dokumentert i `specs/done/openapi-asyncapi-generering.md` (linje 145)
som eit akseptert lint-tips, exit code 0. `gen-asyncapi.py` skriv hardkoda
`"asyncapi": "3.0.0"` med vilje (sjå linje 56) — å oppgradere til 3.1.0 er ei
separat vurdering, ikkje ein feilretting, og er ikkje del av denne planen.

### 4. asyncapi-cli "NODE_ENV"/node-config-åtvaringar — kan fiksast
Ikkje tidlegare dokumentert. Dette er reint cli-verktøy-støy frå
`@asyncapi/cli` (`node-config`-biblioteket), uavhengig av skjemainnhald, og
oppstår for alle skjema som genererer AsyncAPI. Verktøyet sjølv foreslår
miljøvariabelen `SUPPRESS_NO_CONFIG_WARNING`.

## Prioritert handlingsliste

| # | Tiltak | Fil | Prioritet |
|---|---|---|---|
| 1 | ✓ Legg til `owl_flags` i `manifest.yaml` for `samt-bu` | `src/linkml/samt/samt-bu/manifest.yaml` | Høg |
| 2 | ✓ Køyr `make samt` på nytt og verifiser at OWL-deprecation-åtvaringane er borte og exit code framleis er 0 | — | Høg |
| 3 | ✓ Legg til `-e SUPPRESS_NO_CONFIG_WARNING=true` i `ASYNCAPI_RUN` og bruk variabelen i `gen-asyncapi`-valideringskallet | `Makefile` (linje 11, 175) | Medium |
| 4 | ✓ Køyr `make samt` på nytt og verifiser åtvaringsreduksjon | — | Medium |
| 5 | (Separat, eige tiltak — ikkje del av denne planen) Vurder å rulle ut `owl_flags`-fiksen til dei resterande 15 skjemaa utan flagget | alle `src/linkml/*/*/manifest.yaml` utan `owl_flags` | Lav |

Pkt. 2 og 3 i avrotize/asyncapi-kategoriane (sjå vurdering ovanfor) krev ingen
tiltak — dei er allerede dokumenterte og akseptert i `specs/done/`.

### Avvik frå opphavleg plan (utført 2026-06-21)

- **Pkt. 1:** `owl_flags: "--log_level ERROR"` (mønsteret kopiert frå `fint-*`)
  viste seg å **ikkje** suppresse `DeprecationWarning`-ane ved test — same
  åtvaringar dukka opp uendra på `fint-administrasjon` med dette flagget.
  `--log_level` styrer kun `linkml` sin eigen logger, ikkje Python sin
  `warnings`-modul som `owlgen.py` brukar via `deprecation_warning()`.
  Verifisert korrekt fiks: dei tre underliggande generator-flagga må setjast
  **eksplisitt** (anbefalt av åtvaringsteksten sjølv) for å silence varselet
  utan å endre genereringsoppførselen:
  `--no-skip-vacuous-local-range-axioms --no-skip-vacuous-min-zero-cardinality-axioms --no-consolidate-cardinality-axioms`.
  Det betyr at `fint-*`-skjemaa sitt `owl_flags: "--log_level ERROR"` **ikkje**
  faktisk løyser dette problemet for dei heller — eit separat, ikkje-relatert
  funn utanfor denne planen sitt omfang.
- **Pkt. 3:** Oppdaga under verifisering at `ASYNCAPI_RUN`-variabelen var
  definert i `Makefile` men **aldri brukt** — `run_gen_asyncapi`-makroen
  bygde sitt eige separate `podman run`-kall (linje 175, gammal). Retta opp
  ved å bruke `$(ASYNCAPI_RUN)` direkte der, slik at miljøvariabelen faktisk
  blir sendt med.
- **Pkt. 3/4 — delvis løyst:** `SUPPRESS_NO_CONFIG_WARNING=true` fjernar kun
  to av fire NODE_ENV/node-config-linjer («No configurations found» og «To
  disable this warning»). Dei to gjenstående («NODE_ENV value of 'production'
  did not match…» / «See …Strict-Mode») kjem frå at `asyncapi/cli`-imaget
  internt set `NODE_ENV=production` uavhengig av kva som sendes via `-e`
  ved `podman run` — verifisert ved å teste `-e NODE_ENV=test`, som ikkje
  endra meldinga. Ein fullstendig fiks krev å montere ein dummy
  `NODE_CONFIG_DIR` med ei `production.json`-fil — testa og bekrefta at det
  fungerer, men vurdert som disproporsjonal kompleksitet for rein kosmetisk
  CLI-støy frå eit upstream-bibliotek. Akseptert som gjenstående støy, på
  linje med korleis AsyncAPI-versjonstipset (pkt. 3 i vurderinga ovanfor) er
  akseptert i `specs/done/`.

## Avhengigheiter

- Ingen nye containerimage eller verktøy — begge fiksane er konfigurasjonsendringar
  (`manifest.yaml`-flagg og ein Makefile-miljøvariabel)
- Pkt. 3 påvirkar `ASYNCAPI_RUN`, som brukas av alle skjema med `asyncapi: true`
  i manifestet — verifiser at ingen andre skjema sin asyncapi-generering
  forventar `NODE_ENV`-åtvaringa (svært usannsynleg, men `make` (alle domene)
  bør køyrast etter endringa for å bekrefte)

## Utført

Utført 2026-06-21. Tiltak 1-4 er fullførte; tiltak 5 var aldri del av planen
sitt omfang (eksplisitt utsett til eige tiltak).

**Kva som vart gjort:**
- `src/linkml/samt/samt-bu/manifest.yaml`: `owl_flags` satt til
  `--no-skip-vacuous-local-range-axioms --no-skip-vacuous-min-zero-cardinality-axioms --no-consolidate-cardinality-axioms`
  — fjernar alle tre `OwlSchemaGenerator`-`DeprecationWarning`-ane frå `gen-owl`
  utan å endre OWL-outputen
- `Makefile`: `ASYNCAPI_RUN` (linje 11) utvida med `-e SUPPRESS_NO_CONFIG_WARNING=true`,
  og `run_gen_asyncapi`-makroen (linje ~175) endra til å bruke `$(ASYNCAPI_RUN)`
  i staden for eit duplikat, hardkoda `podman run`-kall — variabelen var
  tidlegare definert, men aldri brukt
- Verifisert med to nye køyringar av `make samt`: exit code 0 begge gongar,
  alle tre OWL-deprecation-linjene og to av fire NODE_ENV/node-config-linjer
  er borte

**Avvik frå opphavleg plan:**
- Opphavleg plan (tiltak 1) foreslo `owl_flags: "--log_level ERROR"` etter
  mønsteret frå `fint-*`-skjemaa. Testing viste at dette **ikkje** fungerer —
  `--log_level` styrer `linkml` sin eigen logger, ikkje Python sin
  `warnings`-modul som `owlgen.py` brukar. Korrekt fiks (eksplisitte
  generator-flagg, sjå ovanfor) vart brukt i staden. `fint-*`-skjemaa har
  framleis det ueffektive flagget — eit separat, urelatert funn utanfor
  denne planen sitt omfang.
- Under verifisering av tiltak 3 vart det oppdaga at `ASYNCAPI_RUN`-variabelen
  var ubrukt i `Makefile`. Dette er retta som ein del av tiltak 3, sjølv om
  det ikkje var eksplisitt i opphavleg plan.
- NODE_ENV/node-config-støyen er **delvis** løyst: to av fire linjer
  («No configurations found» / «To disable this warning») er borte.
  Dei to gjenstående («NODE_ENV value of 'production' did not match…» /
  «Strict-Mode»-lenkja) kjem frå at `asyncapi/cli`-imaget internt fastlåser
  `NODE_ENV=production` uavhengig av `-e`-flagg ved `podman run` (verifisert
  ved test). Ein fullstendig fiks (montert `NODE_CONFIG_DIR` med dummy
  `production.json`) er testa og fungerer, men vurdert som disproporsjonal
  kompleksitet for rein kosmetisk CLI-støy — akseptert som gjenstående,
  harmløs støy, exit code framleis 0.
