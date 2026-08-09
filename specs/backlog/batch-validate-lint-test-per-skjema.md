# Batch make validate, make lint og make test på tvers av skjema

## Bakgrunn

Brukaren bad om å undersøkje om det er gevinst å hente ved å batche
`make`-kommandoar som utfører handlingar på fleire enn eitt skjema —
eksplisitt nemnt `make validate` og `make test`.

To tidlegare spesifikasjonar har alt løyst denne typen problem for andre
delar av repoet, og etablerer både metode og infrastruktur denne specen
byggjer vidare på:

- **`specs/done/effektiviser-generate-workflow-koyretid.md`** — batcha alle
  `gen-*`-mål (`gen-jsonld-context`, `gen-python`, `gen-jsonschema`,
  `gen-shacl`, `gen-owl`, `gen-rdf`, `gen-proto`, `gen-erdiagram`,
  `gen-plantuml`, `gen-docs`, `gen-asyncapi`, `gen-openapi`) via
  `src/assets/scripts/makefile/batch-generate.py` — N skjema i **éin**
  podman-kontainar/Python-prosess i staden for éin kontainar per skjema.
- **`specs/done/effektiviser-mcp-linkml-validator-koyretid.md`** — same
  mønster for policy-validering (`validate-bronze`, `validate-data`,
  `validate-examples`) via `batch-flatten-and-validate.py`.

Begge stadfestar same rotårsak: import av `linkml`/`linkml_runtime` (~5,4 s)
vert betalt på nytt for **kvar einaste** `podman run`, uavhengig av kor lite
arbeid sjølve kallet gjer. Podman sin eigen kontaineroppstart legg til
~2,6-2,7 s til. Batching amortiserer denne kostnaden over N skjema i staden
for å betale han N gonger.

**Denne specen dekkjer IKKJE dei to områda over på nytt** — dei er ferdige.
Han identifiserer kva som **står att**, som viser seg å vere akkurat dei to
kommandoane brukaren spurde om.

## Funn — to distinkte, ubatcha problem

### 1. `make validate` (`make/40-validation.mk` linje 22-25) — duplisert, ubatcha logikk ved sida av ein alt eksisterande batcha versjon

```make
validate: ## Valider alle skjema (merge-imports)
	$(call print_header,validate)
	@eval "$$LOG_FUNCTIONS"; \
	$(foreach s,$(SCHEMAS),log_info "..." && log_debug "..." && $(LINKML_RUN) gen-linkml $(s) > /dev/null;)
```

Dette er éin sekvensiell `podman run` per skjema. Samstundes finst det alt
ein ferdig, verifisert batcha makro for **nøyaktig same** operasjon
(`gen-linkml`/merge-imports), definert i `make/10-generator-macros.mk` og
brukt av `gen-linkml-merge`-målet (`make/11-generator-targets.mk` linje 29):

```make
define run_gen_linkml_parallel
@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate.py --generator merge -- $(1)
endef
```

`validate`-målet berre gjenoppfinn det same, ubatcha, ved sida av. Dette er
same type funn som CLAUDE.md sin DRY-regel elles fangar opp for
make-/Python-laget — to kjelder til same fakta/operasjon, éi av dei
utdatert.

**Målt** (lokalt, WSL2/podman, varme image-lag):

| Scenario | Tid |
|---|---|
| 1 skjema, plain `podman run gen-linkml` (dagens `validate`-arkitektur) | 9,0 s |
| 3 skjema, 3 separate `podman run gen-linkml`-kall (dagens arkitektur) | 25,7 s |
| 3 skjema, éin kontainar med `LinkmlGenerator`-API kalla 3x internt | **8,6 s** (import 8,0 s + 0,46/0,10/0,06 s arbeid) |

Ekstrapolert til alle 36 skjema: dagens arkitektur ≈ 36 × 9 s ≈ **324 s**
(5,4 min), batcha ≈ 8 s + 35 × ~0,2 s ≈ **~15 s** — ca. **95 % reduksjon**.

### 2. `make lint` (`make/40-validation.mk` linje 27-33) — ingen batcha ekvivalent finst

```make
lint: ## Køyr linkml lint [SCHEMA=<sti>]
	...
	$(foreach s,$(SCHEMAS),$(LINKML_RUN) linkml lint --config ... "$(s)" &&) true;
```

Same mønster, men her finst **ingen** batcha variant frå før — `lint` er
ikkje del av `batch-generate.py` sin `REGISTRY` (som dekkjer `merge`,
`jsonld-context`, `shacl`, `python`, `json-schema`, `owl`, `rdf`, `proto`,
`erdiagram`, `plantuml`, `doc`). `linkml.linter.linter.Linter` er eit anna
API enn generatorane i `REGISTRY` (tek eit `config: dict`, ikkje ein Click
CLI-kontekst), så han lét seg ikkje leggje inn i `run_click()`-mekanismen
uendra — treng eit eige, lite kall-mønster.

**Målt:** 3 skjema, éin kontainar med `Linter`-API kalla 3x internt (delt
config-lasting): **14,9 s** (import ~8 s delt + 5,5/0,4/0,3 s lint-arbeid —
det fyrste kallet sin lint-tid ser ut til å inkludere noko av `Linter`
sin eigen første-gongs oppsettskostnad). Éin skjema åleine i dag: 15,6 s.
Ekstrapolert: dagens arkitektur ≈ 36 × 15,6 s ≈ **562 s** (9,4 min), batcha
≈ **~20-25 s** — også her rundt 95 % reduksjon.

### 3. `tests/test_make.sh` (`make test`, `make roundtrip`) — kallar den batcha infrastrukturen med N=1, gong på gong

Dette er det største og mest interessante funnet: infrastrukturen frå
`effektiviser-generate-workflow-koyretid.md` finst og fungerer, men
`tests/test_make.sh` **nyttar han ikkje batcha**. Kvar `test_gen_*`-funksjon
kallar det batcha `gen-X`-målet med **eitt einaste skjema**:

```bash
test_gen_jsonld() {
    local schema="$1" outfile="$2"
    make gen-jsonld-context SCHEMAS="$schema" || return 1   # N=1 — betaler full importskatt
    ...
}
```

`run_schema_tests()` (linje 100-136) køyrer 17 slike testfunksjonar
**sekvensielt per skjema** (`validate`, `gen-jsonld`, `gen-python`,
`gen-jsonschema`, `gen-rdf`, `gen-erdiagram`, `gen-docs`, `gen-shacl`,
`gen-owl`, `convert-rdf`, `linkml-lint`, `linkml-validate`, `gen-proto`,
`gen-plantuml`, `mcp-validate-instance`, `roundtrip-json`, `roundtrip-ttl`),
kvar av dei minst éin `podman run`. Sjølve skjema-nivået **er** alt
parallellisert (skjema køyrer samstundes, medvite avgrensa — sjå
kommentaren linje 74-78 om å unngå Podman-database-lock ved for høg
samstundes kontainarbruk), men **per skjema** betalar likevel kvar av dei
~11-14 generator-/valideringssteg full import-/oppstartskostnad kvar for
seg — nøyaktig det biletet som var problemet **før**
`effektiviser-generate-workflow-koyretid.md`, berre no gøymt bak eit lag
skjema-parallellisering i staden for å vere synleg som éin flat, sekvensiell
løkke.

Med 36 skjema × ~11 generator-/lint-/valideringsstegar som kvar betaler
~8-15 s importskatt, uavhengig av kor mange skjema som faktisk køyrer
samstundes, er dette den klart største kjelda til total testtid i dag.

**Kvifor dette ikkje er identisk med Tiltak 1/2 over:** her er utfordringa
ikkje å *byggje* batching (han finst alt for generatorane), men å
*omstrukturere testorkestreringa* frå "per skjema: køyr alle generatorar" til
"per generator: køyr for alle skjema, assert deretter per skjema" — ei
retning på løkka som krev å skilje sjølve genereringssteget frå
assert-/samanlikningslogikken som i dag er vevd saman i kvar
`test_gen_*`-funksjon.

## Tiltak (prioritert etter gevinst/risiko-forhold)

### Tiltak 1 — `make validate`: bruk den alt eksisterande batcha makroen

**Gevinst:** ~95 % reduksjon (~324 s → ~15 s), **lågast mogleg risiko** —
gjenbruker kode som alt er verifisert og i produksjon via
`gen-linkml-merge`.

**Steg:**
1. Erstatt `validate`-målet sin `$(foreach ...)`-kropp i
   `make/40-validation.mk` med `$(call run_gen_linkml_parallel,$(SCHEMAS))`
   (eller `$(SCHEMA)` når sett — sjå handtering av valfri `SCHEMA=`-variabel
   i andre mål same fil, t.d. `lint`).
2. Verifiser at logg-/feilmeldingsformatet framleis er nyttig (batch-
   generate.py sin eigen logging, jf. mønsteret i `run_gen_*_parallel`-
   makroane) — juster `print_header`-kallet om nødvendig.
3. Test: `make validate` mot heile repoet og `make validate SCHEMAS=<eitt
   skjema>` — samanlikn exit-kode og at eit medviteøydelagt skjema
   framleis feilar synleg (fail-fast-eigenskapen må vere uendra).

### Tiltak 2 — `make lint`: ny batcha variant

**Gevinst:** ~95 % reduksjon (~562 s → ~20-25 s). **Låg-til-moderat
risiko** — nytt kall-mønster (ikkje Click-`run_click()`, men direkte
`Linter(config=...).lint(schema)`), men godt isolert og enkelt å
verifisere mot eksisterande CLI-output.

**Steg:**
1. Lag eit lite batch-script (t.d.
   `src/assets/scripts/makefile/batch-lint.py`, same katalog og
   loggmønster som `batch-generate.py`/`batch-flatten-and-validate.py`) som
   for ei liste skjema: lastar `.linkmllint.yaml` **éin gong**, konstruerer
   `Linter(config=...)` **éin gong**, og kallar `.lint(schema)` per skjema —
   skriv problem/exit-kode i same format som dagens `linkml lint`-CLI-output
   brukar (slik `lint`-målet sin feilhandtering ikkje treng endrast).
2. Oppdater `lint`-målet i `make/40-validation.mk` til å kalle det nye
   scriptet i staden for `$(foreach ...)`-løkka, både for
   `SCHEMA=<eitt skjema>` og alle-skjema-varianten.
3. Verifiser: samanlikn lint-output (problem-liste, exit-kode) skjema-for-
   skjema mot dagens CLI-baserte `make lint SCHEMA=<x>` for eit utval skjema
   (minst eitt med kjende lint-åtvaringar, eitt heilt reint).

### Tiltak 3 — `tests/test_make.sh`: omstrukturer til å bruke batcha generatorar på tvers av skjema

**Gevinst:** størst i absolutte tal (dette er i dag den klart lengste
kommandoen i repoet), men **høgast risiko og størst omfang** — rører
testinfrastrukturen sjølv, ikkje berre eitt make-mål.

**Føresetnad/avgrensing:** dette tiltaket bør **ikkje** startast før
Tiltak 1 (og helst òg 2) er gjennomførte og verifiserte, sidan
`test_validate`/`test_linkml_lint` sjølve kallar `make validate`/`make lint`
og automatisk arvar gevinsten frå Tiltak 1/2 utan eiga endring.

**Føreslått retning (krev vidare design før implementering — ikkje detaljert
her):**
1. Del testkøyringa i to fasar per skjema-batch: **Fase A** (generering) —
   kall kvart `gen-X`/`validate`/`lint`-mål **éin gong for heile
   skjemalista** (`SCHEMAS="$schema1 $schema2 ..."`), same mønster som
   `make generate` alt gjer via `batch-generate.py`. **Fase B** (assert) —
   for kvart skjema, køyr dei eksisterande `assert_*`-sjekkane
   (`assert_file_nonempty`, `assert_json_valid` osv.) mot filene Fase A alt
   har generert — ingen nye kontainarkall her, reint filsystem-arbeid.
2. `roundtrip-json`/`roundtrip-ttl`/`mcp-validate-instance` (linje 526-638+
   i `tests/test_make.sh`) gjer eige, meir samansett arbeid (last inn att,
   samanlikn) — vurder om desse kan batchast med same mønster, eller om dei
   bør haldast utanfor Fase A/B-oppdelinga i første omgang (lågare
   kompleksitet, seinare oppfølging).
3. Behald skjema-nivå-parallelliteten som finst i dag (`run_schema_tests`
   sin bakgrunnsjobb-mekanikk) — han løyser eit anna problem (unngår at éitt
   trått skjema blokkerer resten) og er ikkje i konflikt med
   generator-nivå-batching.
4. Verifiser grundig: testresultat (pass/fail per test, per skjema) må vere
   **identisk** før/etter, og feilmeldingar må framleis kunne sporast
   tilbake til rett skjema + rett steg (i dag garantert av
   `_run_one`-namngjevinga — må behaldast eller erstattast med tilsvarande
   presisjon i den nye strukturen).
5. Mål total `make test`-tid før/etter, jf. metoden i dei to referanse-
   specane (isolert profileringsrigg + reell full køyring).

**Merk:** dette er det einaste tiltaket i denne specen som ikkje er
"gjenbruk ei alt bygd og verifisert løysing" (Tiltak 1) eller "eit lite,
isolert nytt script følgje eit etablert mønster" (Tiltak 2) — det er ei
reell omstrukturering av eit 1000+ linjers testscript. Vurder å skrive
**ein eigen, meir detaljert oppfølgings-spec** for Tiltak 3 når Tiltak 1/2
er gjennomførte og den faktiske resterande testtida er kjend (kan vise seg
å vere "godt nok" allereie etter Tiltak 1/2 sin arva gevinst via
`test_validate`/`test_linkml_lint`).

## Handlingsliste

- [x] Tiltak 1: `make validate` bruker `run_gen_linkml_parallel`
- [x] Tiltak 1: verifisert uendra fail-fast-åtferd og feilmeldingsformat
- [x] Tiltak 2: `batch-lint.py` implementert og verifisert semantisk
      identisk problem-liste mot dagens CLI
- [x] Tiltak 2: `make lint` bruker det nye scriptet, både med og utan
      `SCHEMA=`
- [x] Målt total tid før/etter for både `make validate` og `make lint`
      (full køyring, alle 36 skjema)
- [x] Tiltak 3: vurdert om eigen oppfølgings-spec trengst etter at Tiltak
      1/2 sin arva gevinst i `make test` er målt — **konklusjon: ingen arva
      gevinst, Tiltak 3 står ved lag uendra** (sjå «Utført»)

## Utført (Tiltak 1 + 2 — 2026-08-09)

### Tiltak 1 — `make validate`

`make/40-validation.mk` sitt `validate`-mål bruker no
`$(call run_gen_linkml_parallel,$(SCHEMAS))` i staden for
`$(foreach ...)`-løkka med éin `podman run` per skjema.

**Målt (lokalt, WSL2/podman, varme image-lag):**

| Scenario | Før | Etter |
|---|---|---|
| Alle 36 skjema | ~324 s (estimert, aldri fullført-målt før) | **36,5 s** |

**Verifisert:**
- `make validate` (alle 36 skjema): exit-kode 0, alle skjema logga med
  `→ merge domain/name (tid)`.
- `make validate SCHEMAS="tmp/broken-schema/broken-schema.yaml ..."` med
  genuint ugyldig YAML: feilar med `::error file=...::merge feila for ...`
  og korrekt ikkje-null exit-kode (2) — same feiltype som direkte
  `podman run gen-linkml` gav før endringa.
- Ein skjematype (referanse til ikkje-eksisterande klasse i `range:`) gjev
  exit 0 både før og etter endringa — stadfesta at dette er eksisterande
  åtferd i `gen-linkml`/`LinkmlGenerator` (han valideringssjekkar ikkje
  klassereferansar), **ikkje** ein regresjon frå denne endringa.
- `bash -n`/Make-syntakssjekk (`make -n validate`) OK.

**Sidegevinst (ikkje søkt, men verifisert som forbetring):** den gamle
arkitekturen sin exit-kode reflekterte i praksis berre **siste** skjema i
lista (bash `;`-kjeding utan `set -e` gjev exit-kode frå siste kommando,
ikkje ei aggregering) — feil i eit tidleg skjema kunne difor "forsvinne"
dersom eit seinare skjema lykkast. `batch-generate.py` sitt
per-skjema-`try`/`except` (alt verifisert i `effektiviser-generate-
workflow-koyretid.md`) aggregerer korrekt: `failed`-teljar over alle skjema,
retur 1 dersom minst eitt feila. Dette er ei reell korrektheitsforbetring,
ikkje berre ei fartsforbetring.

### Tiltak 2 — `make lint`

Nytt script `src/assets/scripts/makefile/batch-lint.py`: lastar
`.linkmllint.yaml` éin gong, byggjer éin `Linter`-instans og éin
`TerminalFormatter`-sesjon delt over alle skjema (same klassar som
`linkml.linter.cli` sjølv brukar internt for katalog-input — CLI-en sin
eigen `main()`-funksjon kunne **ikkje** gjenbrukast direkte via
`run_click()`-mønsteret frå `batch-generate.py`, sidan han kallar
`sys.exit()` i funksjonskroppen, som ville drepe heile batchen ved første
skjema). `make/40-validation.mk` sitt `lint`-mål kallar no dette scriptet
for både `SCHEMA=<eitt skjema>` og alle-skjema-varianten.

**Målt (lokalt, WSL2/podman, varme image-lag):**

| Scenario | Før | Etter |
|---|---|---|
| Alle 36 skjema | (fullførte aldri i praksis — sjå bugfunn under) | **50,6 s** |

**Uventa, men viktig funn: `make lint` (utan `SCHEMA=`) linta i praksis
aldri meir enn det FØRSTE skjemaet i lista.** Den gamle
`$(foreach ...) && true`-løkka kjeda kvart skjema sitt CLI-kall med `&&`.
`linkml lint` returnerer exit-kode 1 for skjema med **berre åtvaringar**
(ikkje berre feil) — og nesten alle skjema i repoet har minst éi åtvaring.
Verifisert direkte (køyrde uendra kode via `git stash`): `make lint` stoppa
etter `ap-no/common-ap-no` (fyrste skjema i sortert rekkjefølgje) med
`Error 1`, og rapporterte aldri noko om dei attverande 35 skjema. Dette var
altså ein reell, tidlegare ukjend korrektheitsbug — ikkje berre eit
fartsproblem — og vart retta som ein direkte konsekvens av
batch-lint.py sin per-skjema-isolasjon (same mønster som Tiltak 1).
Full køyring etter fiksen: **376 problem i 32 av 36 skjema**, korrekt
rapportert i éin samla oppsummering.

**Verifisert:**
- Output for eit einskild skjema (`ngr-adresse`, 19 åtvaringar) er
  linje-for-linje identisk mot direkte `linkml lint --config ...`-CLI-kall,
  bortsett frå at CLI-en viser absolutt kontainarsti (`/work/...`) medan
  batch-scriptet viser repo-relativ sti (som alt kalla inn) — reint
  kosmetisk, ingen semantisk skilnad.
- Exit-kode-semantikk (0/1/2 for ingen problem/berre åtvaringar/feil)
  bevart i sjølve scriptet. På `make`-nivå returnerer `make lint` uendra
  alltid prosess-exit-kode 2 ved feil (GNU Make sin eigen konvensjon,
  uavhengig av recipe sin eigen exit-kode — stadfesta identisk før og etter
  endringa via `git stash`-samanlikning), så ingen synleg endring for
  kallarar som berre sjekkar `$$?` frå `make`.
- Ingen CI-workflow eller anna script kallar `make lint` direkte (kun
  dokumentasjon: `CLAUDE.md`, `CONTRIBUTING.md`, `COMMANDS.md`,
  `mkdocs/docs/`) — ingen skjulte kallarar å oppdatere.
- `python3 -c "import ast; ast.parse(...)"` og `make -n lint` OK.

### Tiltak 3 — reassessert, IKKJE gjennomført

Målte begge testfunksjonane sin faktiske arkitektur i
`tests/test_make.sh` for å avgjere om dei arvar gevinsten frå Tiltak 1/2
utan eiga endring, slik opphavleg hypotese i denne specen antok:

- `test_validate()` kallar `make validate SCHEMAS="$1"` — **eitt** skjema
  per kall.
- `test_linkml_lint()` kallar **ikkje** `make lint` i det heile — han gjer
  sitt eige, frittståande `podman run ... linkml lint --ignore-warnings
  "$schema"`-kall, heilt utanom Makefile-målet.

Målt N=1-tid for begge dei nye batcha måla: `make validate SCHEMAS=<1
skjema>` **11,8 s**, `make lint SCHEMA=<1 skjema>` **17,9 s** — praktisk
talt identisk med FØR Tiltak 1/2 (import-/oppstartskostnaden er framleis
uamortisert når batchen berre inneheld eitt skjema). **Konklusjon: Tiltak
1/2 gjev null arva gevinst for `make test`** — kvar av dei ~11-14
generator-/valideringsstega i `run_schema_tests()` betaler framleis full
importskatt for kvart einaste skjema, akkurat som før. Tiltak 3 (batch
generator-kall på tvers av heile skjemalista testen dekkjer, ikkje per
skjema) står difor ved lag som eit fullt ut naudsynt, ikkje valfritt,
oppfølgingsarbeid dersom `make test` sin totaltid skal ned.

Gjennomføring av Tiltak 3 er **ikkje** starta i denne økta (jf. spec sin
eigen føresetnad om at det krev vidare design). Tilrår ein eigen,
detaljert oppfølgings-spec når det er ønskt — same tilnærming som
`effektiviser-generate-workflow-koyretid.md` og `effektiviser-mcp-
linkml-validator-koyretid.md` brukte for tilsvarande omfang.

**Denne specen er difor ikkje flytta til `specs/done/`** — Tiltak 1 og 2 er
fullførte og verifiserte, Tiltak 3 står att som identifisert, men
ugjennomført, oppfølgingsarbeid.

## Relaterte filer

- `make/40-validation.mk` — `validate`, `lint`
- `make/10-generator-macros.mk` — `run_gen_linkml_parallel` (alt finst)
- `make/11-generator-targets.mk` — `gen-linkml-merge` (einaste noverande
  brukar av `run_gen_linkml_parallel`)
- `src/assets/scripts/makefile/batch-generate.py` — mønster for Tiltak 2
- `src/mcp-linkml-validator/batch-flatten-and-validate.py` — alternativt
  mønster for Tiltak 2 (JSON-RPC-stdin-batching, brukt for MCP-validator)
- `tests/test_make.sh` — Tiltak 3
- `specs/done/effektiviser-generate-workflow-koyretid.md` — presedens,
  metode og infrastruktur for Tiltak 1 (alt bygd) og Tiltak 2 (mønster)
- `specs/done/effektiviser-mcp-linkml-validator-koyretid.md` — presedens
  for kvantifisert profilering og "importskatt betalt éin gong"-prinsippet
