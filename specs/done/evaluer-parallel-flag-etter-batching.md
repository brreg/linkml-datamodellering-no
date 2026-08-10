# Evaluer om PARALLEL-flagget framleis trengst etter batching

**Kortnamn:** `evaluer-parallel-flag-etter-batching`
**Dato:** 2026-08-10
**Revidert:** 2026-08-10 (same dag — brukaren bad om ei oppfølgingsevaluering
av om `validate-capture` sjølv kan batchast, sjå «Oppfølging» under. Dette
snur konklusjonen for funn 1 og Tiltak 3: `PARALLEL` er ikkje lenger
uunngåeleg, det er berre **ikkje enno batcha**.)

## Bakgrunn

Etter at alle batchbare `make`-kommandoar er batcha (sjå
`specs/done/evaluer-batching-resterande-kommandoar.md`, Tiltak 1-5, og dei
tidlegare `paralleliser-domain-targets-fase1/2`-spesifikasjonane), stilte
brukaren spørsmål om `PARALLEL`-flagget (`make/00-settings.mk:34`,
`PARALLEL ?= 16`) framleis har ein reell funksjon. Undersøkinga er gjort
ved å grepe heile repoet for faktiske (ikkje kommentar-) bruk av
`PARALLEL` og `run-parallel-gen.sh`, ikkje ved å gjette.

## Funn

### 1. `validate-capture` — PARALLEL er framleis reelt i bruk **i dag**, men berre fordi ho ikkje er batcha enno

`make/40-validation.mk` linje 223-229: `validate-capture PARALLEL=<n>` sender
`--parallel $(PARALLEL)` til `run-schema-validation.py`, som (linje 121-133)
spawnar **N separate podman-prosessar via `xargs -P`** — éin kontainar per
skjema, ikkje éin batcha kontainar. Kommentaren rett over `validate-capture`
i `make/40-validation.mk` forklarer at ei **tidlegare** DRY-vurdering
(`make-kommando-inkonsistens-audit.md`) medvite utsette konsolidering av
dette scriptet — men grunngjevinga der gjaldt **namnekonsistens/overlapp**
mot `log-mcp-validate`/`run-validation.sh` (CI-kritisk infrastruktur), ikkje
spørsmålet om sjølve valideringssteget kan batchast. Sjå «Oppfølging» under
for kvifor batching av **berre** valideringssteget (utan å røre
CI-kritiske script) faktisk er lågrisiko og bør gjerast.

### 2. `domain_target` sin `print_header` — vestigial referanse, ikkje lenger reell

`make/20-domain-targets.mk` linje 61:
```make
$$(call print_header,domain-$(1),$$(if $$(filter-out 1,$$(PARALLEL)),(PARALLEL=$$(PARALLEL))))
```
Denne linja viser `(PARALLEL=N)` i headeren når `PARALLEL != 1`. Men sjølve
pipeline-orkestreringa (`run-domain-pipeline.sh`) **les ikkje `$PARALLEL` i
det heile** — fase 1- og fase 2-gruppene startast alltid samstundes via
bakgrunnsjobbar (`run_bg`/`wait`, sjå linje 60-85 i scriptet), uavhengig av
kva `PARALLEL` er sett til. Før batchinga kontrollerte `PARALLEL` faktisk
kor mange `xargs -P`-prosessar `run-parallel-gen.sh` brukte inni
domain-pipelinen; etter at heile pipelinen vart lagt om til
fase-parallellisering via rekursive `$(MAKE)`-kall
(`3874ffa6 perf(make): fase-parallelliser uavhengige batch-grupper innanfor domain_target`),
mista denne koplinga funksjon, men header-teksten vart ikkje fjerna eller
oppdatert. I dag er ho **misvisande**: å setje `PARALLEL=1` endrar ikkje
åtferda til `domain-*`-targeta lenger, sjølv om headeren antyder at han
gjer det.

### 3. `run-parallel-gen.sh` — daud kode

`grep -rn "run-parallel-gen\.sh"` over heile repoet gjev **berre**
kommentar-referansar (i `10-generator-macros.mk`, `00-settings.mk`,
`batch-render-plantuml.sh`, `convert-examples.sh`,
`run-domain-pipeline.sh`) og scriptet sin eigen interne feilmeldingstekst
(`run-parallel-gen.sh: ukjent flagg: $1`). **Ingen** Makefile-oppskrift
eller anna script kallar scriptet lenger. Dette var det siste
`xargs -P $PARALLEL`-baserte "N separate kontainarar"-mønsteret att i
generator-laget; `gen-xsd` (Tiltak 4) og `gen-asyncapi` sin valideringsfase
(Tiltak 5) — dei to siste brukarane — vart begge batcha til éin delt
kontainar i `evaluer-batching-resterande-kommandoar.md`. Scriptet er no
ubrukt.

## Oppfølging: kan `validate-capture` sjølv batchast?

Brukaren bad om ei evaluering av om `run-schema-validation.py` sitt
`xargs -P`-mønster (funn 1) kan erstattast med same
«éin-delt-kontainar»-batching som resten av valideringslaget alt brukar.
Kartlegginga er gjort ved å lese `run-schema-validation.py`,
`flatten-and-validate.bash`, `batch-flatten-and-validate.py`,
`save-validation-log.py` og bruksstaden i `validate-bronze`
(`make/40-validation.mk` linje 40-70) direkte.

**Kva `run-schema-validation.py` faktisk gjer i dag:** for kvart releasja
skjema (`find_released_packages()` mot `release-please-config.json`) kallar
`process_schema()` → `run_validation()` → `subprocess.run(["bash",
"flatten-and-validate.bash", schema, policy])`. Det scriptet gjer **éin
`podman run -i --rm mcp-linkml-validator`** per kall — send JSON-RPC
`initialize` + `validate_linkml_schema` over stdin, les svaret frå stdout.
`--parallel N` gjer berre at N slike prosessar (kvar sin eigen
`flatten-and-validate.bash` → eigen podman-kontainar) køyrer samstundes via
`xargs -P` — presis det same monster-CLI-per-eining-mønsteret som `gen-xsd`
og `gen-asyncapi` sin valideringsfase hadde **før** Tiltak 4/5 i
`evaluer-batching-resterande-kommandoar.md`.

**Kva som alt finst og er verifisert i produksjon:**
`batch-flatten-and-validate.py` (same katalog som `flatten-and-validate.bash`)
er **nøyaktig** batch-erstatninga for dette mønsteret — brukt i dag av
`validate-bronze`/`validate-data` (`make/40-validation.mk` linje 40-118).
Han tek imot ei jobbliste (`--jobs-tsv`: `schema<TAB>policy<TAB>instance`
per linje, tom instance-kolonne = auto-oppdaga — nøyaktig det
`run-schema-validation.py` treng), løyser eksempelfil og
`tree_root`-deteksjon internt (same konvensjon som
`flatten-and-validate.bash`), og sender **alle** valideringskalla som éin
samla JSON-RPC-batch til **éin** `podman run mcp-linkml-validator`-kontainar
(`run_mcp_batch()`, linje 110-134). Resultatet vert skrive som éin JSON-fil
per jobb (`<index>.json`) i ein `--output-dir`, med **identisk innhald**
til det eit enkelt `flatten-and-validate.bash`-kall ville produsert (jf.
docstring-kommentaren i scriptet).

**Output-formatet matchar òg utan tilpassing:** `run-schema-validation.py`
sin eigen `save_report()` skriv til
`src/linkml/<domain>/<model>/validation/<version>/<policy>.json` med eit
handrulla JSON-skjema. Det finst alt eit **delt** produksjonsscript som gjer
nøyaktig dette — `save-validation-log.py` (brukt av `validate-bronze` linje
60-63) — som skriv til **same stad** (`src/linkml/<domain>/<model>/
validation/<version>/<type>.json`) via det delte
`utils/validation_log.py`-modulet (`build_validation_log_entry`/
`write_validation_log`). `run-schema-validation.py` sin `save_report()` er
altså ein **duplikat** implementasjon av noko som alt finst delt og
verifisert — batching av `validate-capture` løyser difor to ting samstundes:
eliminerer `xargs -P`-mønsteret OG eit DRY-avvik.

**Éin reell skilnad å handtere:** `run-schema-validation.py` sin
`get_policy()` les `validation_policy` frå `build.yaml` med eit eige regex
(`re.search(r"^validation_policy:\s*(\S+)", ...)`), medan det alt finst eit
delt, meir robust script for nøyaktig dette —
`detect-validation-policy.py` (brukt av `mcp-linkml-valider-modell`), som
brukar ordentleg YAML-parsing (`yaml.safe_load`) i staden for regex.
Sidefunn, ikkje ein hindring for batching, men bør konsoliderast i same
steg (same type sidefunn som `run_convert`/`batch-convert.py`-observasjonen
i `evaluer-batching-resterande-kommandoar.md`).

**Risikovurdering:** LÅG. Same mønster som Tiltak 1/2 i
`evaluer-batching-resterande-kommandoar.md` — gjenbruk av alt verifisert
produksjonskode (`batch-flatten-and-validate.py` + `save-validation-log.py`,
begge brukt av `validate-bronze`/`validate-data` i CI/lokalt kvar dag), ikkje
noko nytt skrive frå botnen av. `validate-capture` sjølv er **ikkje**
CI-kritisk (same kommentar som i dag stadfestar dette), så det er òg mindre
risikofylt å endre enn `run-validation.sh`/`log-mcp-validate`, som vart
medvite spart i den tidlegare namnekonsistens-vurderinga.

**Konsekvens for PARALLEL-flagget:** Dersom `validate-capture` batchast,
forsvinn den **siste** reelle brukstaden for `PARALLEL` — flagget kan då
fjernast heilt (variabel, eksport og alle referansar), ikkje berre ryddast
opp kosmetisk slik opphavleg Tiltak 3 føreslo.

## Konklusjon

`PARALLEL`-flagget har **ingen brukstad som ikkje kan batchast**. Alle tre
funn peikar no same veg — mot fjerning, ikkje vidarehald:

| Stad | Status | Tiltak |
|---|---|---|
| `validate-capture` (`run-schema-validation.py --parallel`) | Batchbar — gjenbruk `batch-flatten-and-validate.py` + `save-validation-log.py`, alt verifisert i `validate-bronze`/`validate-data` | Batch, fjern `--parallel`/`xargs`-mønsteret |
| `domain_target` sin `print_header` (`20-domain-targets.mk:61`) | Vestigial — viser feilaktig at PARALLEL styrer fase-parallellisering | Fjern `PARALLEL`-referansen frå header-teksten |
| `run-parallel-gen.sh` | Daud kode, ingen kallarar att | Slett scriptet |
| `PARALLEL ?= 16` sjølv (`00-settings.mk`) | Ingen attverande brukstad etter dei tre tiltaka over | Fjern variabelen, eksporten og `[PARALLEL=8]`-hjelpeteksten i `validate-capture` |

## Tiltak

1. **Batch `validate-capture`**: byt `run-schema-validation.py` sin
   per-skjema `subprocess.run(["bash", "flatten-and-validate.bash", ...])`
   (kalla frå `process_schema()`) med å byggje ei jobs-TSV
   (`schema<TAB>policy<TAB>` — tom instance-kolonne, same auto-oppdaging som
   i dag) frå dei releasja pakkane, og kalle
   `batch-flatten-and-validate.py --jobs-tsv <fil> --output-dir <dir>` éin
   gong for **alle** skjema. Les kvart `<index>.json`-resultat og send det
   vidare til `save-validation-log.py --schema <sti> --type <policy>
   --result <json>` (same kall-mønster som `validate-bronze` alt gjer,
   `make/40-validation.mk` linje 60-63) i staden for eigen `save_report()`.
   Fjern `process_schemas_parallel()`, `--parallel`-argumentet og
   `xargs -P`-koden heilt.
2. Bytt `get_policy()` sin eigne regex til å kalle
   `detect-validation-policy.py` (eller importere same logikk), slik at
   policy-deteksjon er éin kjelde med `mcp-linkml-valider-modell`.
3. Fjern `[PARALLEL=8]`-hjelpeteksten og `PARALLEL`-referansen frå
   `validate-capture` sin `print_header`-linje (`make/40-validation.mk`
   linje 223-224), sidan flagget ikkje lenger tek imot noko verdi.
4. Fjern `$$(if $$(filter-out 1,$$(PARALLEL)),(PARALLEL=$$(PARALLEL)))`-
   uttrykket frå `print_header`-kallet i `domain_target`
   (`make/20-domain-targets.mk:61`), sidan `PARALLEL` ikkje påverkar
   domain-pipelinen si åtferd (og no heller ikkje `validate-capture`).
5. Fjern `PARALLEL ?= 16` og `export PARALLEL` frå `make/00-settings.mk` —
   ingen attverande brukstad etter Tiltak 1 og 4.
6. Slett `src/assets/scripts/makefile/run-parallel-gen.sh` — stadfest på
   nytt (rett før sletting) at ingen nye kallarar er lagt til sidan denne
   evalueringa, deretter fjern kommentar-referansane til scriptet i
   `10-generator-macros.mk`, `00-settings.mk`, `batch-render-plantuml.sh`,
   `convert-examples.sh` og `run-domain-pipeline.sh` (dei er historiske
   forklaringar, ikkje lenger korrekte).
7. Verifiser: `make validate-capture` (alle releasja skjema) og
   `make validate-capture SCHEMA=<sti>` (enkeltskjema-stien er uendra, går
   framleis via `process_schema()`/direkte kall) gjev byte-identisk
   `validation/<version>/<policy>.json`-output mot før batching, for minst
   eitt skjema med kjend valideringsfeil og eitt utan. Verifiser òg
   `make domain-samt` etter fjerning av `PARALLEL`.

## Handlingsliste

- [x] Avklar med brukar om Tiltak 1-7 skal implementerast
- [x] Tiltak 1: batch `validate-capture` via `batch-flatten-and-validate.py` + `save-validation-log.py`
- [x] Tiltak 2: konsolider policy-deteksjon til delt `utils.schema_meta.detect_policy`
- [x] Tiltak 3: fjern PARALLEL-hjelpetekst frå validate-capture sin header
- [x] Tiltak 4: fjern vestigial PARALLEL-referanse frå domain_target header
- [x] Tiltak 5: fjern PARALLEL-variabelen og eksporten frå 00-settings.mk
- [x] Tiltak 6: slett run-parallel-gen.sh og kommentar-referansane til han
- [x] Tiltak 7: verifiser (delvis — sjå «Utført», podman utilgjengeleg i denne økta)

## Relaterte filer

- `make/00-settings.mk` — `PARALLEL ?= 16`, eksport — kandidat for sletting
- `make/20-domain-targets.mk` — `domain_target`, vestigial header-referanse
- `make/40-validation.mk` — `validate-capture`, `validate-bronze` (mønster å gjenbruke)
- `src/assets/scripts/makefile/run-schema-validation.py` — skal batchast, `xargs -P`-koden fjernast
- `src/mcp-linkml-validator/batch-flatten-and-validate.py` — gjenbrukbar batch-mekanisme, alt verifisert av validate-bronze/validate-data
- `src/assets/scripts/makefile/save-validation-log.py` — gjenbrukbar delt lagringslogikk
- `src/assets/scripts/makefile/detect-validation-policy.py` — delt policy-deteksjon (YAML), erstatning for run-schema-validation.py sin regex
- `src/assets/scripts/utils/validation_log.py` — delt loggformat (`build_validation_log_entry`/`write_validation_log`)
- `src/assets/scripts/makefile/run-domain-pipeline.sh` — fase-parallellisering, les ikkje PARALLEL
- `src/assets/scripts/makefile/run-parallel-gen.sh` — daud kode, kandidat for sletting
- `specs/done/evaluer-batching-resterande-kommandoar.md` — Tiltak 1/2 (same gjenbruksmønster), Tiltak 4/5 (siste brukarane av run-parallel-gen.sh vart batcha)
- `specs/done/fjern-parallel1-openapi-asyncapi-spesialkode.md` — tidlegare relatert opprydding

## Utført

### Tiltak 1+2 — `run-schema-validation.py` skriven om til batcha validering med delt policy-deteksjon

**`src/assets/scripts/utils/schema_meta.py`:** ny `detect_policy(schema_path) -> str`
— les `validation_policy` frå `build.yaml` via delt `utils.yaml_io.load_yaml`
(ordentleg YAML-parsing, ikkje regex). Fallback til `"bronze"` ved manglande
fil/felt/parsefeil, med `log`-linje til stderr ved parsefeil (ingen stille
feil).

**`src/assets/scripts/makefile/detect-validation-policy.py`:** forenkla til
tynn CLI-wrapper rundt `detect_policy()` — same åtferd, éin kjelde.

**`src/assets/scripts/makefile/run-schema-validation.py`:** fullstendig
omskriving:
- `get_policy()` (regex) fjerna, brukar no delt `detect_policy()`.
- `save_report()` (handrulla JSON-format) fjerna, brukar no delte
  `utils.validation_log.build_validation_log_entry`/`write_validation_log`
  — same format og skrivestad som `save-validation-log.py` alt brukar for
  `validate-bronze`/`validate-data` (`src/linkml/<domain>/<model>/
  validation/<version>/<policy>.json`).
- `process_schemas_parallel()` (`xargs -P` mot N separate
  `flatten-and-validate.bash`-kall) fjerna heilt, saman med
  `--parallel`-argumentet.
- Ny `process_schemas_batch()`: byggjer jobs-TSV (`schema<TAB>policy<TAB>`)
  for alle releasja skjema, kallar
  `batch-flatten-and-validate.py --jobs-tsv <fil> --output-dir <dir>
  --repo-root <REPO_ROOT>` **éin gong** for heile lista (same mekanisme som
  `validate-bronze`/`validate-data`), les eitt `<index>.json`-resultat per
  skjema, lagrar via `save_result()`.
- `process_schema()` (enkeltskjema, `--schema`-flagget) står att uendra i
  struktur — kallar framleis `flatten-and-validate.bash` direkte (N=1, inga
  kontainar-amortisering å hente), men lagrar no via same delte
  `save_result()`-funksjon som batch-stien, i staden for eigen
  `save_report()`.
- Resultat-parsing brukar no `errorCount`/`warningCount` (camelCase) direkte
  frå MCP-serveren sitt svar, i staden for å telje `issues` sjølv (den
  gamle koden dupliserte teljing MCP-serveren alt gjer, jf.
  `server.py` linje 891-893/993-995).

### Tiltak 3 — fjern PARALLEL-hjelpetekst frå validate-capture

**`make/40-validation.mk`:** `validate-capture` sin `##`-hjelpetekst og
`print_header`-kall oppdatert (`[PARALLEL=8]` fjerna, `"(alle skjema,
batcha)"` i staden for `"($(PARALLEL) workers)"`). Recipe forenkla til å
kalle `run-schema-validation.py` utan `--parallel`.

### Tiltak 4 — fjern vestigial PARALLEL-referanse frå domain_target header

**`make/20-domain-targets.mk`:** `print_header`-kallet i `domain_target`
forenkla til `$$(call print_header,domain-$(1))` — `PARALLEL` styrte
ingenting i `run-domain-pipeline.sh` (stadfesta i Funn 2), så referansen var
rein misvising.

### Tiltak 5 — fjern PARALLEL-variabelen frå 00-settings.mk

**`make/00-settings.mk`:** `PARALLEL ?= 16` og `export PARALLEL` fjerna.
Kommentaren over eksport-blokka (som nemnde `run-parallel-gen.sh`) og
`fmt_elapsed_ms`-kommentaren (same referanse) oppdaterte til å ikkje nemne
det sletta scriptet.

### Tiltak 6 — slett run-parallel-gen.sh og kommentar-referansane

**Sletta:** `src/assets/scripts/makefile/run-parallel-gen.sh`.

**Kommentaroppdateringar** (alle var reine tekst-referansar, ingen
funksjonelle kall att, stadfesta med grep før sletting):
- `make/10-generator-macros.mk`: fjerna stale toppblokk-avsnitt som
  feilaktig hevda gen-xsd/asyncapi-validering framleis var ubatcha (dei var
  alt batcha i `evaluer-batching-resterande-kommandoar.md`), og fjerna
  «Ingen run-parallel-gen.sh-fase att»-setninga ved `run_gen_doc_parallel`.
- `src/assets/scripts/makefile/batch-render-plantuml.sh`: retta referanse
  til korrekt Fase A-mekanisme (`batch-generate.py`, ikkje
  `run-parallel-gen.sh`).
- `src/assets/scripts/makefile/convert-examples.sh`: fjerna samanlikninga
  mot det sletta scriptet.
- `src/assets/scripts/makefile/run-domain-pipeline.sh`: fjerna referansen i
  opningskommentaren.
- `src/assets/scripts/makefile/batch-generate-instances.py`: fjerna
  referansen i `filter_enabled()` sin docstring.

### Tiltak 7 — verifisering (delvis — podman utilgjengeleg i denne økta)

**Verifisert utan podman (statisk/funksjonsnivå):**
- `python3 -c "import ast; ast.parse(...)"` — alle tre endra Python-filer
  (`run-schema-validation.py`, `utils/schema_meta.py`,
  `detect-validation-policy.py`) er syntaktisk gyldige.
- `make -n domain-samt` / `make -n validate-capture` — Makefile-recipa
  parserer korrekt, ingen udefinerte variabel-feil etter fjerning av
  `PARALLEL`.
- **Faktisk køyring av `make domain-samt`**: header viser no korrekt
  `make domain-samt` utan PARALLEL-tekst, fase-parallelliseringa i
  `run-domain-pipeline.sh` startar framleis `gen-docs`/`gen-rdf`/
  `gen-jsonschema`/`gen-linkml-merge`/`gen-shacl` samstundes som før — feilar
  først ved sjølve podman-kallet (sandkasse-avgrensing, sjå under), ikkje
  noko stad før det.
- **Direkte funksjonskall** (utan podman) mot det omskrivne
  `run-schema-validation.py`: testa `detect_policy()`, `get_domain_model()`,
  `get_version()` mot `samt-bu` (policy `silver`) og `fair-metadata` (policy
  `gold`) — korrekte verdiar. Testa `process_schemas_batch(..., dry_run=True)`
  og `process_schema(..., dry_run=True)` — begge skriv korrekte
  `[dry-run] ville skrive src/linkml/<domain>/<model>/validation/<version>/
  <policy>.json`-stiar, i tråd med det delte formatet.
- **Jobs-TSV-kompatibilitet**: bygde ei TSV med `process_schemas_batch()`
  sitt format (`schema<TAB>policy<TAB>`) og lasta ho inn direkte med
  `batch-flatten-and-validate.py` sin eigen `load_jobs()`/
  `resolve_example_path()`/`schema_has_tree_root()` — stadfesta korrekt
  parsing og korrekt eksempelfil-/tree_root-deteksjon for begge
  testskjemaa (`fair-metadata` utan `tree_root`, `samt-bu` med).
- `grep` stadfesta null attverande referansar til `run-parallel-gen.sh` eller
  `PARALLEL` i heile repoet (utanom denne specen sjølv).

**Ikkje verifisert (krev podman, utilgjengeleg i denne økta):** sjølve
`podman run mcp-linkml-validator`-kallet i `batch-flatten-and-validate.py`
og `flatten-and-validate.bash`, og dermed heile
`make validate-capture`/`make domain-samt`-kjeda ende-til-ende. Podman
feila konsekvent i denne sandkassa
(`chmod /run/user/1000/libpod: read-only file system`) — ei kjend,
førehandseksisterande avgrensing (jf. `specs/done/sandbox-wsl2-losning.md`),
ikkje ein konsekvens av desse endringane. **Brukaren bør køyre
`make validate-capture` (både utan `SCHEMA=` og med `SCHEMA=<sti>` for eitt
kjent-ugyldig og eitt kjent-gyldig skjema) og `make domain-samt` sjølv,
utanfor denne sandkassa, for å stadfeste at output er identisk med før
batchinga.**
