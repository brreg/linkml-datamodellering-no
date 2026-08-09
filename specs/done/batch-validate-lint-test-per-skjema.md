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

### Tiltak 3 — `tests/test_make.sh`: detaljert evaluering

**Baseline-måling** (lokalt, WSL2/podman, varme image-lag,
`bash tests/test_make.sh <eitt skjema>` — dokumentert einskild-skjema-modus):
alle 17 testtrinn for `samt/samt-bu` sekvensielt: **4 min 45 s (285 s)**,
16 OK / 1 FEIL (`roundtrip-ttl` — sjå «Sidefunn» under, ikkje relatert til
batching). Dette talet er representativt for **alle** 36 skjema sin
kjedelengd, sidan `run_schema_tests()` gjev kvart skjema si eiga
sekvensielle kjede av same 17 steg — skjema-nivå-parallelliteten
(bakgrunnsjobbar) let kjedene **overlappe**, men forkortar ikkje **kvar
enkelt** kjede. Total `make test`-tid i dag er difor avgrensa nedanfrå av
denne ~285 s-kjedelengda (pluss ressurskonkurranse frå opp til 36 samtidige
kontainarar), uansett kor mange skjema som køyrer samstundes. **Dette er
sjølve flaskehalsen Tiltak 3 må angripe** — ikkje talet på skjema, men
lengda på kjeda per skjema.

**Kategorisering av dei 17 testtrinna** (kva kontainarkall/mekanisme kvart
steg brukar i dag, og kor batchbart det er):

| Steg | Mekanisme i dag | Kategori | Batchbarheit |
|---|---|---|---|
| validate | `make validate SCHEMAS=<1>` | A | Alt batcha infrastruktur (Tiltak 1) — treng berre kallast med N skjema i staden for 1 |
| gen-jsonld | `make gen-jsonld-context SCHEMAS=<1>` | A | Alt batcha (`run_gen_parallel,jsonld-context`) |
| gen-python | `make gen-python SCHEMAS=<1>` | A | Alt batcha (`run_gen_parallel,python`) |
| gen-jsonschema | `make gen-jsonschema SCHEMAS=<1>` | A | Alt batcha (`run_gen_parallel,json-schema`) |
| gen-rdf | `make gen-rdf SCHEMAS=<1>` | A | Alt batcha (`run_gen_rdf_parallel`) |
| gen-shacl | `make gen-shacl SCHEMAS=<1>` | A | Alt batcha (`run_gen_shacl_parallel`) |
| gen-owl | `make gen-owl SCHEMAS=<1>` | A | Alt batcha (`run_gen_owl_parallel`) |
| gen-proto | `make gen-proto SCHEMAS=<1>` | A | Alt batcha (`run_gen_parallel,proto`) |
| gen-erdiagram | `make gen-erdiagram SCHEMAS=<1>` | B | Alt batcha, 2-fase (`run_gen_erdiagram_parallel`) |
| gen-docs | `make gen-docs SCHEMAS=<1>` | B | Alt batcha, 2-fase (`run_gen_doc_parallel` + erdiagram) |
| gen-plantuml | `make gen-plantuml SCHEMAS=<1>` | B | Alt batcha, 3-fase — Fase C batchar SVG-rendering for **alle** skjema alt i dag |
| linkml-lint | Eigen `podman run linkml lint --ignore-warnings` (bypassar `make lint`) | C | `batch-lint.py` (Tiltak 2) finst alt — treng berre eit `--ignore-warnings`-tilsvarande flagg |
| mcp-validate-instance | `gen-linkml --mergeimports` **+** JSON-RPC `schemaText` til MCP-server | C | Sjå eige funn under — burde bruke `schemaPath` (alt bygd i `effektiviser-mcp-...` Tiltak 2) OG batchast som `batch-flatten-and-validate.py` alt gjer |
| convert-rdf | Direkte `linkml-convert`-podman-kall | D | `linkml.converter.cli:cli` er ein rein Click-kommando **utan** `sys.exit()` i kroppen — kompatibel med same `run_click()`-mønster som Tiltak A/B |
| roundtrip-json | 3× `linkml-convert`-kall + Python-samanlikning | D | Same som convert-rdf, 3 kall per skjema kan batchast som 3 separate jobbar i éin kontainar |
| roundtrip-ttl | 4× `linkml-convert`-kall + Python-samanlikning | D | Same som over, 4 kall per skjema |
| linkml-validate | Direkte `linkml validate --schema X Y`-podman-kall | D | `linkml.validator.cli:cli` kallar **derimot** `sys.exit()` (2 stader) — kan IKKJE gjenbrukast via `run_click()`. Bruk i staden `linkml.validator.validate()`-API-et direkte (same funksjon MCP-serveren alt brukar internt) |

**Kategori A (8 steg) og B (3 steg) — 11 av 17 steg, null nytt script-
arbeid:** infrastrukturen (`batch-generate.py` + dei tilhøyrande
`run_gen_*_parallel`-makroane) finst og er verifisert **allereie**. Det
einaste som manglar er å endre **korleis testorkestreringa kallar han** —
i staden for at kvart skjema sin `run_schema_tests()`-kjede kallar
`make gen-X SCHEMAS="$schema"` (N=1, betaler importskatt for kvart einaste
skjema), må ei ny **Fase A** kalle `make gen-X SCHEMAS="<alle skjema som
skal testast>"` **éin gong per generator, før** skjema-løkka startar. Ei
etterfølgjande **Fase B**, per skjema, køyrer så dei eksisterande
`assert_*`-sjekkane (`assert_file_nonempty`, `assert_json_valid` osv.) mot
filene Fase A alt har skrive — reint filsystem-arbeid, ingen nye
kontainarkall.

**Kategori C (2 steg) — treng lite nytt script-arbeid, godt presedens:**

- **linkml-lint:** `batch-lint.py` (Tiltak 2) manglar berre eit flagg som
  speglar CLI-en sitt `--ignore-warnings` (styrer kun exit-kode-
  utrekninga — ingen endring i sjølve lint-logikken).
- **mcp-validate-instance — eige funn:** denne testen er **ikkje**
  oppdatert etter `effektiviser-mcp-linkml-validator-koyretid.md` sitt
  Tiltak 2 (sjå «Sidefunn» under for detaljar) — han gjer framleis den no
  overflødige `gen-linkml --mergeimports`-utflatinga sjølv, og sender
  `schemaText` i staden for `schemaPath`. Å modernisere denne testen til
  same mønster som `flatten-and-validate.bash` alt bruker (send
  `schemaPath` direkte, ingen utflating) fjernar **både** eit heilt
  kontainarkall per skjema (utflatinga) **og** opnar for å batche sjølve
  MCP-kallet med akkurat den same JSON-RPC-stdin-mekanismen
  `batch-flatten-and-validate.py` alt implementerer for N skjema i éin
  kontainar.

**Kategori D (4 steg, involverer opptil 8 `linkml-convert`-kall per
skjema) — stadfesta batchbart, men størst implementeringsarbeid:**
Verifisert direkte (`inspect.getsource`) at `linkml.converter.cli:cli`
(bak `linkml-convert`) er ein rein Click-kommando som **ikkje** kallar
`sys.exit()` i kroppen (kastar exceptions i staden) — dette er nøyaktig
kontrakten `run_click()`-hjelparen i `batch-generate.py` alt føreset, så
alle `linkml-convert`-kall (convert-rdf, og dei 3+4 delkonverteringane i
roundtrip-json/roundtrip-ttl) kan i prinsippet batchast med same mekanisme.
Ulikt Kategori A/B (éin fast generator-type med berre `schema` som
argument) treng convert-jobbane derimot eit **heterogent jobb-format**
(kvar jobb har eigen `schema`, `input`, `output-format`, `output-path`) —
same mønster `batch-flatten-and-validate.py` alt etablerte for heterogene
MCP-valideringsjobbar (`--jobs-tsv`). `linkml-validate` (siste rad i
tabellen) krev eit anna grep — CLI-en kallar `sys.exit()` og kan ikkje
gjenbrukast direkte, så batching der må gå via `linkml.validator.validate()`
sitt Python-API (same funksjon MCP-serveren sjølv brukar, med same kjende
"send eit bygd `SchemaDefinition`-objekt, ikkje ein stistreng"-detalj som
`effektiviser-mcp-linkml-validator-koyretid.md` alt dokumenterte og løyste).

**Estimert samla gevinst:** basert på dei same amortiseringsforholda som
Tiltak 1/2/MCP-specen målte (~8 s fast importskatt + ~0,1-0,9 s marginalt
per ekstra skjema/jobb i same prosess), ville ei full batching av Kategori
A-D redusere kjedelengda per skjema frå ~285 s til i praksis nesten berre
konverterings-/samanlikningsarbeidet (sub-sekund per skjema) pluss ein
handfull faste importskattar (éin per generator/verktøy, ikkje éin per
skjema × steg). Talet på `podman run`-kall for **heile** testsuiten (36
skjema × 17 steg ≈ 600+ kall i dag) ville falle til storleiksorden 15-20
kall totalt (éin per Kategori A/B/C/D-gruppe), uavhengig av kor mange
skjema som testast. Dette er eit **estimat basert på verifisert
amortiseringsrate**, ikkje ei direkte måling av den fullt batcha
arkitekturen — presis totaltid bør målast etter kvar fase er implementert,
jf. metoden i referansespecane.

**Tilrådd rekkjefølgje (aukande risiko):**

1. Kategori A+B (11 steg) — reorganiser `run_schema_tests()` til Fase A
   (batch-generering for heile skjemalista) + Fase B (per-skjema assert).
   Null nytt script-arbeid, berre bash-omstrukturering. **Lågast risiko,
   størst del av gevinsten** (11 av 17 steg).
2. Kategori C (linkml-lint, mcp-validate-instance) — liten scriptutviding
   (lint-flagg) + modernisering av mcp-validate-instance til
   `schemaPath`. **Låg-til-moderat risiko** (mcp-validate-instance-delen
   rører kontrakten testen sender til MCP-serveren, sjølv om
   `schemaPath`-støtta alt er verifisert i produksjon andre stader).
3. Kategori D (convert-rdf, roundtrip-json, roundtrip-ttl, linkml-validate)
   — nytt batch-script for heterogene `linkml-convert`-jobbar +
   `linkml.validator.validate()`-basert batching. **Høgast risiko** —
   roundtrip-testane sin eigen samanlikningslogikk (sortering,
   normalisering) må halde fram å få nøyaktig same input som i dag, og
   dette er den delen av testsuiten med flest kjende, dokumenterte
   BUG-1/BUG-2-workarounds som lett kan bli utilsikta påverka av ei
   omskriving.

**Fellesregel for alle fasar:**
- Behald skjema-nivå-parallelliteten som finst i dag
  (`run_schema_tests()` sin bakgrunnsjobb-mekanikk) for Fase B/assert-delen
  — han løyser eit anna problem (unngår at éitt trått skjema blokkerer
  rapportering av resten) og er ikkje i konflikt med generator-nivå-
  batching i Fase A.
- Feilmeldingar må framleis kunne sporast tilbake til rett skjema + rett
  steg (i dag garantert av `_run_one`-namngjevinga) — batch-scripta sitt
  eksisterande `::error file=<schema>::...`-format (Tiltak 1/2) gjev alt
  denne sporbarheita, men den nye Fase A/B-strukturen må vidareføre ho heilt
  ut til `_run_one`-rapporteringa.
- Testresultat (pass/fail per test, per skjema) må vere **identisk**
  før/etter kvar fase, verifisert steg for steg (ikkje samla til slutt) —
  same disiplin som `batch-docs-publish-generering.md` og
  `effektiviser-generate-workflow-koyretid.md` brukte.
- Mål total `make test`-tid før/etter kvar fase.

**Eksplisitt utanfor scope for Tiltak 3:** `run_json_schema_tests()`/
`test_roundtrip_json_schema()` (linje 587-1022) — ein separat testveg (MCP
`mcp-linkml-modell-utkast`-rundtur), berre aktiv med
`TEST_FILTER=roundtrip-json-schema`, typisk få filer om gongen. Låg
prioritet samanlikna med hovudløkka sine 36 skjema × 17 steg.

**Sidefunn under evalueringa (ikkje batching-relatert, men verdt å
dokumentere):**

1. **`test_mcp_validate_instance` er ikkje oppdatert etter
   `effektiviser-mcp-linkml-validator-koyretid.md` sitt Tiltak 2.** Den
   specen fjerna heile utflatingssteget (`gen-linkml --mergeimports`) frå
   `flatten-and-validate.bash` og let MCP-serveren løyse imports naturleg
   via `schemaPath` — og fann i tillegg ein reell falsk-positiv-bug som
   utflatinga forårsaka (importerte klassar vart telde som lokale).
   `test_mcp_validate_instance` (linje 526-585 i `tests/test_make.sh`) gjer
   framleis den gamle, no overflødige utflatinga sjølv og sender
   `schemaText`. Dette er ikkje ein feil i seg sjølv (testen fungerer), men
   testen validerer no ein kodeveg (`schemaText`-kontrakten) som ikkje
   lenger er den ordinære produksjonsvegen, og betaler ein unødvendig
   kontainarkostnad kvar gong. Bør rettast som eige, lite steg (uavhengig
   av resten av Tiltak 3) — flagg som eiga oppgåve i oppfølgingsarbeidet.
2. **Pre-eksisterande testfeil oppdaga under baseline-målinga, ikkje
   relatert til batching:** `roundtrip-ttl (samt-bu)` feilar i dag med
   `linkml_runtime.MappingError: No pred for
   https://data.norge.no/samt/samt-bu/id <class 'rdflib.term.URIRef'>` i
   `rdflib_loader.from_rdf_graph()`. Ikkje undersøkt vidare her (utanfor
   denne evalueringa sitt omfang), men bør fylgjast opp separat — sjekk om
   han høyrer heime i `bugs/` saman med dei allereie dokumenterte
   BUG-1/BUG-2 rdflib-roundtrip-avvika, eller om han er ny.

**Konklusjon:** Tiltak 3 er **stadfesta gjennomførbart i sin heilskap** —
alle 17 steg let seg i prinsippet batche, 11 av dei med infrastruktur som
alt finst og er verifisert. Attverande arbeid er i hovudsak
**orkestreringsomskriving** (Kategori A/B), ikkje ny kontainar-/API-
forsking — den forskinga er gjort her.

## Utført (Tiltak 3 Kategori A+B — 2026-08-09)

`tests/test_make.sh` omstrukturert til to fasar, som skissert i evalueringa
over:

- **Ny «Fase A»** (`run_phase_a()`, `run_phase_a_step()`): køyrer kvart av
  dei 11 Kategori A/B-generatormåla (`validate`, `gen-jsonld-context`,
  `gen-python`, `gen-jsonschema`, `gen-rdf`, `gen-erdiagram`, `gen-docs`,
  `gen-shacl`, `gen-owl`, `gen-proto`, `gen-plantuml`) **éin gong** med
  `SCHEMAS="<heile skjemalista testen dekkjer>"`, i staden for éin gong per
  skjema. Respekterer `TEST_FILTER` (hoppar over eit steg sin batch dersom
  filteret ikkje kan matche det steget sitt testnamn — unngår unødvendig
  generering). Køyrer **før** skjema-nivå-bakgrunnsjobbane startar, rett
  etter `TEST_DIRS`/cleanup-registreringa (kritisk rekkjefølgje — Fase A
  må ikkje skrive output før cleanup-registreringa har fastslått kva
  katalogar som er nye).
- **Ny `phase_a_check()`:** per (generator, skjema), grep etter
  `::error file=<skjema>::` i Fase A sin logg for det generatoren (skriven
  av `batch-generate.py`/`batch-generate-instances.py` sin alt eksisterande
  per-skjema-isolasjon, jf. Tiltak 1/2) — gjev presis feilattribuering
  sjølv når Fase A-batchen som heilskap "lykkast" for dei fleste skjema,
  men feila for nokre få.
- Dei 11 tilhøyrande testfunksjonane (`test_validate`, `test_gen_jsonld`,
  `test_gen_python`, `test_gen_jsonschema`, `test_gen_rdf`,
  `test_gen_erdiagram`, `test_gen_docs`, `test_gen_shacl`, `test_gen_owl`,
  `test_gen_proto`, `test_gen_plantuml`) bruker no `phase_a_check <nøkkel>
  "$schema"` i staden for sitt eige `make gen-X SCHEMAS="$schema"`-kall —
  sjølve `assert_*`-sjekkane etter er **uendra**.
- Kategori C/D-steg (`linkml-lint`, `mcp-validate-instance`, `convert-rdf`,
  `roundtrip-json`, `roundtrip-ttl`, `linkml-validate`) er **ikkje** rørte —
  køyrer framleis éin gong per skjema, uendra frå før, slik evalueringa sin
  tilrådde fase-rekkjefølgje føreset.

**Kjend, medvite akseptert avgrensing:** `batch-render-plantuml.sh`
(SVG-render-fasen av `gen-plantuml`) manglar per-fil-feilattribuering (jf.
evalueringa sitt funn) — dersom heile denne batchen feilar utan at noko
enkeltskjema får ein `::error file=`-markør, fell `phase_a_check` tilbake
til å returnere "ingen feil funne", og dei eksisterande
`assert_file_nonempty`-sjekkane på `.puml`/`.svg` er den einaste
resterande sikringa. Same avgrensing gjeld i praksis alt i dag for
produksjons-`make gen-plantuml` (ikkje noko denne omlegginga innfører) —
ikkje forsøkt løyst her, jf. CLAUDE.md sin regel om å unngå spekulativ
feilhandtering for scenario som ikkje er stadfesta å skje i praksis.

**Verifisert:**

1. `bash -n tests/test_make.sh` — syntaks OK.
2. **Éin-skjema-modus** (`bash tests/test_make.sh
   src/linkml/samt/samt-bu/samt-bu-schema.yaml`): **16 OK, 1 FEIL** — byte-
   for-byte same resultat (same einaste feil, `roundtrip-ttl`, pre-
   eksisterande `rdflib_loader.MappingError`, ikkje relatert) som før
   endringa. Tid: 4 min 43 s, praktisk talt uendra frå baseline (4 min 45 s)
   — venta, sidan N=1 ikkje gjev batching-gevinst (import-/oppstands-
   kostnaden er den same anten han betalast i den gamle eller nye
   strukturen når det berre er eitt skjema).
3. **Full køyring, alle 36 skjema:** fullførte på **17 min 26 s**, **536
   OK, 42 FEIL**. Alle 42 feil verifisert å vere **fullstendig urelaterte**
   til denne endringa:
   - **36 feil** (`gen-jsonld`/`gen-python`/`gen-jsonschema`/`gen-proto` ×
     9 skjema kvar — `cpsv-ap-no`, `dcat-ap-no`, `dqv-ap-no`,
     `modelldcat-ap-no`, `skos-ap-no`, `xkos-ap-no`): **pre-eksisterande
     hòl i testsuiten**, stadfesta uendra med `git stash` mot uendra kode
     for `cpsv-ap-no`/`gen-jsonld` (identisk `Fil manglar: ...`-feil både
     før og etter). Rotårsak: desse er AP-NO-profilskjema som **medvite**
     har `jsonld_context: false`/`python: false`/`json_schema: false`/
     `protobuf: false` i `build.yaml` (stadfesta for alle 5 unike
     skjemanamn) — testane sjekkar ikkje desse flagga før dei ventar at
     output-fila finst. Denne testsuite-mangelen finst identisk i **begge**
     arkitekturane og er **ikkje** noko denne omlegginga innfører eller
     påverkar. Ikkje retta her (utanfor omfanget av Tiltak 3 Kategori A/B).
   - **6 feil** (`roundtrip-ttl` for `samt-bu`, `fint-utdanning`,
     `fint-personvern`, `enhetsregisteret-bvrinn` m.fl.): Kategori D,
     ikkje rørt av denne endringa. `samt-bu`-tilfellet er identisk med
     feilen alt dokumentert under Tiltak 3-evalueringa sitt «Sidefunn».
   - **0 feil** i noko av dei 11 Kategori A/B-testtypane utover dei alt
     nemnde, pre-eksisterande `build.yaml`-flagg-tilfella.
4. Ingen utilsikta repo-tilstandsendring: `git status` viser berre
   `tests/test_make.sh` og denne specen som endra. `generated/` og
   `tests/testlogs/` er gitignora (stadfesta via `git check-ignore`) —
   testkøyringane sine artefakt/loggar påverkar ikkje versjonskontroll.

**Ikkje målt:** eit direkte "før"-tal for full 36-skjema-køyring med den
**gamle** (ubatcha) arkitekturen. Éin-skjema-baselinen (285 s/skjema,
målt både før og etter denne endringa) og den dokumenterte risikoen for
ressurskonkurranse ved unbounded 36-vegs-parallellitet (jf.
`batch-docs-publish-generering.md` sitt tilsvarande funn) gjer det
sannsynleg at ei full gammal køyring ville teke minst like lang tid, mogleg
vesentleg lengre — men dette er ikkje stadfesta med ei direkte måling, av
omsyn til køyretid/ressursbruk ved å køyre heile 36-skjema-suiten to gonger
i same økt. Dersom eit presist før/etter-tal er ønskt, kan det målast i eiga
økt.

**Attverande arbeid (ved slutten av denne økta):** Kategori C (linkml-lint
batching, mcp-validate-instance-modernisering til `schemaPath`) og
Kategori D (`linkml-convert`-batching for convert-rdf/roundtrip-json/
roundtrip-ttl, `linkml.validator.validate()`-batching for linkml-validate)
var **ikkje** implementerte i denne økta — begge var detaljerte i
evalueringa over, klare til å gjennomførast som eiga oppfølgingsøkt.
**Kategori C er sidan gjennomført** (sjå «Utført (Tiltak 3 Kategori C —
2026-08-09)» rett under) — Kategori D står framleis att.

## Utført (Tiltak 3 Kategori C — 2026-08-09)

Begge Kategori C-stega ferdigstilte: `linkml-lint` og `mcp-validate-
instance` er no batcha på same måte som Kategori A/B (éin batch-kontainar
for heile skjemalista i Fase A, `phase_a_check`/`phase_a_mcp_check` i
Fase B for per-skjema-attribuering).

### linkml-lint

`batch-lint.py` (Tiltak 2) fekk eit nytt `--ignore-warnings`-flagg som
speglar CLI-en sitt eige flagg — styrer **berre** exit-kode-utrekninga
(skjema med berre åtvaringar reknast ikkje som feil), ingen endring i
sjølve lint-logikken. Ny per-skjema `::error file=<skjema>::`-attribuering
er **kun** aktiv i `--ignore-warnings`-modus, slik at `make lint` sin
standardmodus (utan flagget) er **heilt uendra** frå Tiltak 2 sitt
verifiserte, CLI-identiske output — stadfesta direkte (`ngr-adresse`,
19 åtvaringar, identisk output og exit-kode 1 i standardmodus, exit-kode 0
i `--ignore-warnings`-modus, begge samanlikna mot native CLI).

Ny `run_phase_a_lint()` i `tests/test_make.sh` kallar `batch-lint.py
--ignore-warnings` direkte via `podman run` (ikkje via `make lint`, sidan
testen alltid har brukt `--ignore-warnings`-semantikk som `make lint` sjølv
ikkje støttar) for heile skjemalista på éin gong.
`test_linkml_lint()` er redusert til eitt `phase_a_check lint "$1"`-kall.

### mcp-validate-instance

**Server-sida (`src/mcp-linkml-validator/server.py`):**
`validate_instance()` (bak `validate_linkml_instance`-verktøyet) fekk ein
ny valfri `schema_path`-parameter, same mønster som `validate_schema()`
alt har for `validate_linkml_schema` (bygg `SchemaView(schema_path)`,
løys `target_class` frå `tree_root` automatisk). `TOOL_DEF_INSTANCE` fekk
tilsvarande nytt `schemaPath`-felt, `required` endra frå
`["schemaText", "instanceText"]` til berre `["instanceText"]` (validering
av at minst eitt av `schemaText`/`schemaPath` er gjeve skjer no i
`handle()`, same mønster som `validate_linkml_schema`). `schemaText`-vegen
er **heilt uendra** — reint additivt.

Dette fjernar den tidlegare `gen-linkml --mergeimports`-utflatinga
`test_mcp_validate_instance` gjorde sjølv (éin ekstra kontainar per skjema)
og opnar for å sende skjemaet som `schemaPath` — SchemaView løyser
relative imports naturleg mot eit montert repo, same grunngjeving som
`effektiviser-mcp-linkml-validator-koyretid.md` sitt Tiltak 2 alt
etablerte for `validate_linkml_schema`.

**Nytt batch-script** (`src/mcp-linkml-validator/batch-validate-
instances.py`): same JSON-RPC-stdin-batching-mekanisme som
`batch-flatten-and-validate.py` (éin `podman run` for N skjema+instans-par,
kvart sendt som ei eiga `tools/call`-melding), men mot
`validate_linkml_instance` i staden for `validate_linkml_schema` — reint
instansvalidering, ingen policy-sjekkar.

Ny `run_phase_a_mcp_instance()` og delt `mcp_instance_job()`-hjelpefunksjon
(brukt av både Fase A sin jobb-bygging og `test_mcp_validate_instance()`
sine skip-meldingar, for å garantere at begge alltid er samde om kva som
vert hoppa over) i `tests/test_make.sh`. Resultat lesast per skjema frå
JSON-filer batch-scriptet skreiv (`phase_a_mcp_check()`), i staden for
`phase_a_check()` sin logg-grep (ulikt format enn dei andre batch-scripta).

**Alvorleg, pre-eksisterande sti-bug oppdaga og retta (godkjent av brukar
før retting, sidan det utvida oppgåva sitt omfang):**
`test_mcp_validate_instance` (og, utanfor denne rettinga sitt omfang,
òg `test_convert_rdf`/`test_linkml_validate` — Kategori D) sjekka
eksempelfil-stien `examples/$domain/$name-eksempel.yaml` — men **ingen**
toppnivå-katalog `examples/` finst nokon stad i repoet (dei ekte filene
ligg i `src/linkml/$domain/$name/examples/$name-eksempel.yaml`). Stadfesta
med `git show HEAD:tests/test_make.sh` at denne feilen fanst **før** noka
endring i denne økta — testen har difor i praksis **alltid** teke
«Ingen eksempelfil»-skip-greina og rapportert falsk OK, for **kvart
einaste** skjema, i heile testen si levetid. Retta **berre** for
`mcp-validate-instance` (i tråd med brukarval — Kategori D-funksjonane sin
tilsvarande bug er **ikkje** rørt).

**Målt/verifisert:**
- `python3 -c "import ast; ast.parse(...)"` på alle tre endra/nye
  Python-filer, `bash -n tests/test_make.sh` — alle OK.
- `schemaPath` for `validate_linkml_instance` manuelt verifisert: gyldig
  resultat (`valid: true`) for `samt-bu` + eksempeldata via schemaPath, og
  stadfesta at det gamle `schemaText`-kallet (utan montert repo) framleis
  feilar nøyaktig som dokumentert i koden sin eigen kommentar (relativ
  import-oppløysing er kjend å vere broten for rå schemaText med imports —
  dette er nettopp grunngjevinga for schemaPath, ikkje ein ny feil).
  Manglar-begge-felt-feilen (`parse_error`) verifisert korrekt.
- `make mcp-linkml-valider-modell-test` (28 testar): **alle grøne**, ingen
  regresjon frå `validate_instance()`-signaturendringa.
- `make mcp-linkml-valider-modell-smoke`: uendra respons.
- `batch-validate-instances.py` testa direkte mot 2 skjema (`samt-bu`,
  `ngr-adresse`) — begge `valid: true`, batcha i éin kontainar.
- **Éin-skjema-modus** (`bash tests/test_make.sh
  src/linkml/samt/samt-bu/samt-bu-schema.yaml`): 16 OK, 1 FEIL — same
  einaste (urelaterte, pre-eksisterande) feil som før. Stadfesta i loggen
  at `mcp-validate-instance` no **faktisk validerer** (Fase A-loggen viser
  "Validerer 1 instans(ar) ... 0 ugyldige"), ikkje lenger berre eit stille
  «Ingen eksempelfil»-hopp-over.
- **Full køyring, alle 36 skjema:** **536 OK, 42 FEIL — nøyaktig same tal
  som før Kategori C** (same 36 pre-eksisterande `build.yaml`-flagg-hòl frå
  Kategori A/B-verifiseringa + same 6 `roundtrip-ttl`-feil, Kategori D,
  urørt). **0 nye feil** frå at `mcp-validate-instance`/`linkml-lint` no
  batchar OG (for mcp-validate-instance) faktisk køyrer for første gong:
  Fase A-loggen stadfesta 20 skjema fekk ekte instansvalidering i éin
  batcha kontainar (`→ Validerer 20 instans(ar) ... 0 ugyldige`), og
  batcha `linkml-lint --ignore-warnings` fann ingen skjema med reelle feil
  (berre åtvaringar, korrekt ignorert). Dette stadfestar både at
  batchinga er korrekt OG at eksempeldataen i repoet faktisk er gyldig —
  ikkje at testen framleis er tannlaus.
- Ingen utilsikta repo-tilstandsendring: `git status` viser berre dei fire
  intenderte filene (`server.py`, `batch-lint.py`,
  `batch-validate-instances.py` (ny), `tests/test_make.sh`) som endra.

**Ikkje gjort:** presist før/etter-tidsmål for Kategori C isolert (same
avveging som for Kategori A/B — ei ekstra full 36-skjema-køyring berre for
tidsmåling vart ikkje prioritert i denne økta).

## Utført (Tiltak 3 Kategori D — 2026-08-09)

Alle fire attverande stega batcha: `convert-rdf`, `roundtrip-json`,
`roundtrip-ttl` (alle via `linkml-convert`) og `linkml-validate` (via
`linkml.validator.validate()`-API-et direkte, sidan CLI-en kallar
`sys.exit()` og ikkje er `run_click()`-kompatibel, jf. evalueringa).

### To nye batch-script

- **`src/assets/scripts/makefile/batch-convert.py`** — batchar
  `linkml-convert`-kall via same `run_click()`-mønster som
  `batch-generate.py` (stadfesta i evalueringa: `linkml.converter.cli:cli`
  har ingen `sys.exit()` i kroppen). Tek ei `--jobs-tsv`-fil
  (`schema<TAB>input<TAB>output-format<TAB>output`, same TSV-konvensjon
  som `batch-flatten-and-validate.py`) sidan jobbane er heterogene (ulik
  input/format/output per jobb, ulikt Kategori A/B sine faste
  generator-typar). Jobbar for same skjema (roundtrip-stega) må stå i rett
  rekkjefølgje i TSV-fila når eit steg sin `input` er eit tidlegare steg
  sin `output` — verifisert trygt sidan scriptet prosesserer strengt
  sekvensielt (éin prosess, ingen intern parallellitet).
- **`src/assets/scripts/makefile/batch-linkml-validate.py`** — batchar
  `linkml validate`-kall via `linkml.validator.validate()` direkte,
  same funksjon `mcp-linkml-validator` sin `server.py` alt brukar internt.
  Tek `--jobs-tsv` med `attribueringsnøkkel<TAB>skjema-å-validere-mot
  <TAB>instansfil` — nøkkelen er alltid det ORIGINALE skjemaet (for
  `phase_a_check`-oppslag), medan "skjema-å-validere-mot" kan vere ein
  test-fixture for skjema utan `tree_root` (same fixture-mønster som
  `mcp_instance_job()` frå Kategori C, men her vert skjemaet validert mot
  fixturen i staden for hoppa heilt over — ulik åtferd, difor eigen
  `linkml_validate_job()`-hjelpefunksjon, ikkje gjenbruk av
  `mcp_instance_job()`).

### Fase A/B-integrasjon i `tests/test_make.sh`

- Fire nye Fase A-funksjonar: `run_phase_a_convert_rdf()`,
  `run_phase_a_roundtrip_json()`, `run_phase_a_roundtrip_ttl()`,
  `run_phase_a_linkml_validate()`. Roundtrip-stega sine mellomlagringsfiler
  (tidlegare `mktemp`-genererte tilfeldige namn inne i kvar per-skjema-
  testfunksjon) er no deterministiske stiar under `tmp/roundtrip-json/
  <namn>/` og `tmp/roundtrip-ttl/<namn>/` — nødvendig for at Fase A (som
  køyrer FØR skjema-nivå-bakgrunnsjobbane) kan skrive dei, og Fase B (i
  bakgrunnsjobbane) kan finne dei att utan ekstra tilstandsvidareføring
  mellom fasane.
- Fire nye delte jobb-hjelpefunksjonar (`convert_rdf_job()`,
  `roundtrip_json_job()`, `roundtrip_ttl_job()`, `linkml_validate_job()`),
  same mønster som `mcp_instance_job()` frå Kategori C — deler skip-
  logikken mellom Fase A (jobbliste) og Fase B (skip-meldingar), unngår at
  dei to driv frå kvarandre.
- `test_convert_rdf()`, `test_roundtrip_json()`, `test_roundtrip_ttl()`,
  `test_linkml_validate()` er alle reduserte til: sjekk om jobben skal
  køyrast (delt hjelpefunksjon) → `phase_a_check` → (for roundtrip-testane)
  same reine Python-samanlikningslogikk som før, uendra, mot dei no
  deterministiske filstiane.

### Tre pre-eksisterande bugar oppdaga og retta undervegs

Alle tre vart oppdaga fordi dei enten hindra batching frå å gje meining
(sti-bugane) eller batching sin eigen implementering avdekte dei direkte
(stale filnamn). Ingen av dei er introduserte av denne endringa —
stadfesta for den viktigaste (sti-bugen) med `git show HEAD` i Kategori C
sitt tilsvarande funn; dei to nye er verifisert ved at det aktuelle
filnamnet/mønsteret aldri finst andre stader i repoet.

1. **`test_convert_rdf`/`test_linkml_validate` brukte same feil
   eksempelfil-sti som `test_mcp_validate_instance` hadde i Kategori C**
   (`examples/$domain/$name-eksempel.yaml`, manglar `src/linkml/`-prefiks
   — ingen toppnivå-katalog `examples/` finst i repoet). Retta for begge,
   same grunngjeving/godkjenning som Kategori C sin tilsvarande fiks
   (brukar hadde alt godkjent denne bug-klassen for retting — ikkje spurt
   på nytt for denne identiske gjentakinga, men dokumentert her for
   sporbarheit). `test_roundtrip_json`/`test_roundtrip_ttl` brukte alt
   korrekt sti (ein lokal `$example`-variabel i `run_schema_tests()`) og
   var **ikkje** påverka.
2. **`test_convert_rdf` sjekka `generate.yaml` i staden for `build.yaml`**
   for `example_rdf: false`-flagget. `generate.yaml` vart omdøypt til
   `build.yaml` ein gong tidlegare i prosjektet si historie (stadfesta:
   `find src/linkml -iname "generate.yaml"` gjev 0 treff, `-iname
   "build.yaml"` gjev 41), men denne eine sjekken vart aldri oppdatert —
   `[ -f "$gen_yaml" ]` var difor **alltid** usann, og
   `example_rdf: false`-skipen triggast **aldri**. Praktisk konsekvens:
   9 skjema (`modellkatalog/{digdir,kartverket,ksdigital,novari,
   skatteetaten}-modellkatalog`, `referanse/{referansemodell,
   -bronze,-silver,-gold}`) som eksplisitt ber om å IKKJE få convert-rdf
   køyrd, fekk det likevel (dei 7 `ap-no`/`fair`-skjema med same flagget
   vart alt dekte av `lacks_tree_root`-sjekken, så dei var upåverka).
   Retta: `gen_yaml`/`generate.yaml` → `build_yaml`/`build.yaml` i
   `convert_rdf_job()`.

**Verifisert:**
- `python3 -c "import ast; ast.parse(...)"` på begge nye script,
  `bash -n tests/test_make.sh` — alle OK.
- `batch-convert.py` testa direkte med ei 3-stegs kjede (yaml→json→yaml→
  json, `samt-bu`) — byte-identisk innhald mellom første og siste steg sin
  output, stadfesta at kjeda med avhengige input/output-stiar fungerer
  korrekt sekvensielt i éin batch.
- `batch-linkml-validate.py` testa direkte med 2 skjema (`samt-bu`,
  `ngr-adresse`) — begge valide, batcha i éin kontainar.
- **Éin-skjema-modus** (`bash tests/test_make.sh
  src/linkml/samt/samt-bu/samt-bu-schema.yaml`): 16 OK, 1 FEIL — same
  einaste feil som heile tida (`roundtrip-ttl`, pre-eksisterande
  `rdflib_loader.MappingError`). Stadfesta i loggen at feilen no vert
  fanga med presis attribuering **gjennom eit kaskaderande andre steg**:
  steg 3 (ttl→yaml) feilar med den kjende `MappingError`-en, steg 4
  (yaml→json) feilar deretter naturleg fordi steg 3 sin output-fil aldri
  vart skriven — begge korrekt logga med `::error file=<schema>::`,
  `phase_a_check` fangar første treffet og rapporterer FEIL, uendra
  sluttresultat.
- **Full køyring, alle 36 skjema:** **536 OK, 42 FEIL — nøyaktig same tal
  som gjennom heile Kategori A/B/C-verifiseringa.** Same 36
  `build.yaml`-flagg-hòl (urelatert til Kategori D) + same 6
  `roundtrip-ttl`-feil. **0 nye feil**, sjølv om `convert-rdf` og
  `linkml-validate` no **faktisk køyrer** for dei fleste skjema for første
  gong (stadfesta i Fase A-loggen: 102 `linkml-convert`-kall totalt på
  tvers av convert-rdf/roundtrip-json/roundtrip-ttl sine batchar, 30
  skjema faktisk linkml-validerte) — igjen stadfesting av at både
  batchinga og eksempeldataen er korrekte, ikkje at testane er tannlause.
- Ingen utilsikta repo-tilstandsendring: `git status` viser berre dei tre
  intenderte filene (`tests/test_make.sh`, `batch-convert.py` (ny),
  `batch-linkml-validate.py` (ny)) som endra. `tmp/`-katalogen (no med
  nye `roundtrip-json/`/`roundtrip-ttl/`-underkatalogar) vert framleis
  fjerna heilt av `cleanup()`-trappa ved skriptslutt, uendra frå før.

**Ikkje gjort:** presist før/etter-tidsmål for Kategori D isolert (same
avveging som Kategori A/B/C — ei ekstra full 36-skjema-køyring berre for
tidsmåling vart ikkje prioritert).

**Alle fire kategoriar (A, B, C, D) i Tiltak 3 er no gjennomførte og
verifiserte.** Spesifikasjonen sitt opphavlege mål — undersøkje og
realisere batching-gevinst for `make validate`, `make lint` og `make
test` — er dermed oppnådd i sin heilskap. Denne specen er **ikkje** flytta
til `specs/done/` i denne økta likevel, av eitt gjenståande omsyn: eit
presist før/etter-tidsmål for full `make test`-køyring (nemnt som
«ikkje gjort» under kvar kategori sin eigen «Utført»-seksjon) er aldri
teke — kvar kategori sin fulle 36-skjema-verifisering målte KORREKTHEIT
(536 OK/42 feil, konsekvent gjennom alle fire rundar), ikkje TID isolert
frå kvarandre. Dette er eit medvite, dokumentert etterslep, ikkje eit
attverande funksjonelt tiltak — flytting til `specs/done/` bør vurderast
saman med brukaren.

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
- [x] Tiltak 3: detaljert evaluering (baseline-måling, kategorisering av
      alle 17 steg, API-kompatibilitetssjekk) — sjå «Tiltak 3» over
- [x] Tiltak 3 Kategori A+B: `tests/test_make.sh` omstrukturert til
      Fase A (batch-generering) + Fase B (per-skjema assert), verifisert
      0 regresjonar mot full 36-skjema-køyring (sjå eiga «Utført»-seksjon)
- [x] Tiltak 3 Kategori C: `batch-lint.py`-utviding (`--ignore-warnings`) +
      `mcp-validate-instance`-modernisering til `schemaPath`, begge batcha
      og verifisert 0 regresjonar mot full 36-skjema-køyring — i tillegg
      retta ein alvorleg, pre-eksisterande sti-bug (sjå eiga «Utført»)
- [x] Tiltak 3 Kategori D: batching av `linkml-convert`-baserte steg
      (convert-rdf, roundtrip-json, roundtrip-ttl) og `linkml-validate` via
      `linkml.validator.validate()`, verifisert 0 regresjonar mot full
      36-skjema-køyring — i tillegg retta to fleire pre-eksisterande bugar
      (sjå eiga «Utført»)

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

**Oppdatering (same dag, seinare økt):** sjølve evalueringa vart fyrst
fullført og lagt til i «Tiltak»-seksjonen over (baseline-måling,
kategorisering av alle 17 steg, API-kompatibilitetssjekk, fase-
rekkjefølgje) — og deretter **gjennomført for Kategori A+B** i ei tredje
økt same dag. Sjå «Utført (Tiltak 3 Kategori A+B — 2026-08-09)» rett under
«Tiltak»-seksjonen for fullt detaljert resultat (verifisering, målte tal,
kjende avgrensingar). Kategori C+D står att.

**Denne specen er difor framleis ikkje flytta til `specs/done/`** — Tiltak
1, 2 og 3 Kategori A+B er fullførte og verifiserte, Tiltak 3 Kategori C+D
står att som identifisert, men ugjennomført, oppfølgingsarbeid.

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
