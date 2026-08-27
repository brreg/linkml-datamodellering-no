# Kommandoar

Alle kommandoar køyrer via containerar — ingen lokal Python-installasjon trengst.

## Oppsett og føresetnadar

| Kommando | Beskriving | Output |
|---|---|---|
| `make check-prereqs` | Sjekkar at Git, jq, Podman, GNU make, user namespace og ledig diskplass er korrekt konfigurert | Skriv OK/FEIL per føresetnad til stdout; avsluttar med kode 1 ved feil |

`check-prereqs`-targetet er berre eit tynt wrapper-lag rundt
`src/assets/scripts/makefile/check-prereqs.bash`, som ikkje sjølv krev
`make` eller `podman` for å køyrast. På ein heilt ny maskin utan desse
installerte, køyr scriptet direkte i staden: `bash
src/assets/scripts/makefile/check-prereqs.bash`.

## Logging

Alle `make`-kommandoar støttar `LOGLVL`-variabelen for å styre detaljnivå:

| Nivå | Beskriving | Bruksområde |
|---|---|---|
| `DEBUG` | Viser alle script- og funksjonskall med kommandolinjer + timing | Feilsøking, debugging av parallelle køyringar |
| `INFO` (default) | Viser status-meldingar, framgang og summarar | Normal bruk |
| `ERROR` | Viser berre feil og kritiske åtvaringar | Stille køyring, CI-jobbfeil |

**Eksempel:**

```bash
# Debugging — vis alle kommandolinjer med timing
make gen-schema-docs SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml LOGLVL=DEBUG

# Normal bruk — vis berre status-meldingar
make domain-ngr LOGLVL=INFO

# Stille køyring — vis berre feil
make domain-ngr LOGLVL=ERROR
```

**GitHub Actions:** CI-workflows køyrer med `LOGLVL=DEBUG` som standard for full feilsøkingsinfo i loggar.

### Ingen stille feil — `run_logged`

Generator-makroar i `make/*.mk` skal **aldri** redirigere ein kommando sitt
output til `/dev/null` (`> /dev/null 2>&1`) — det kastar vekk den faktiske
feilteksten dersom kommandoen feilar. Bruk i staden `run_logged` frå
`LOG_FUNCTIONS` (`make/00-settings.mk`):

```bash
run_logged "<label>" <kommando> [args...]
```

`run_logged` fangar stdout+stderr frå kommandoen. Ved suksess går fanga
output til `log_debug` (stille på `INFO`/`ERROR`, akkurat som i dag). Ved
feil skriv han kommandolinja, exit code og den faktiske output-teksten via
`log_error` — synleg sjølv på `LOGLVL=ERROR`. Sjå `specs/done/ingen-stille-feil.md`
for bakgrunn og fleire eksempel på refaktorering.

For Python-script gjeld tilsvarande: bruk `error_handler.log_error()`
(`src/assets/scripts/utils/error_handler.py`) for uventa unntak, og skriv
alltid noko til `stderr` ved bevisste fallback-verdiar. Ein bar `except:`
eller `except Exception:` utan noka logging er ikkje tillate.

## Batching

Fleire kommandoar samlar N skjema inn i **éin** kontainarprosess i staden
for éin `podman run` per skjema — skildra per kommando i "Batching"-kolonna
i tabellane under §§ Validering, Generering av artefakter og Vedlikehald.
Dette er noko anna enn **parallellisering** (fase-parallellisering i
`run-domain-pipeline.sh`, sjå § "Generering av artefakter"): parallellisering
styrer kor mange skjema som køyrer **samstundes** (fleire prosessar), medan
batching styrer kor mange
**kontainarar** som startast i det heile, ved å behandle N skjema i éin
delt prosess. Gevinsten er størst for `linkml`-baserte kommandoar, der
import av `linkml`/`linkml_runtime` (~5-8 s) elles vert betalt på nytt for
kvart einaste skjema uavhengig av kor lite arbeid sjølve kallet gjer. Sjå
`specs/done/effektiviser-generate-workflow-koyretid.md`,
`specs/done/effektiviser-mcp-linkml-validator-koyretid.md` og
`specs/done/batch-validate-lint-test-per-skjema.md` for målingar, metode
og full grunngjeving.

## Wrapper-target

Nokre target gjer ikkje arbeidet sjølv, men **delegerer** til eit anna
target via eit rekursivt `$(MAKE) <target>`-kall i oppskrifta si. Dette
avsnittet gjer denne delegeringa eksplisitt, sidan ho ikkje er synleg i
`make help`-output.

### Reelle wrapper-target

| Target | Delegerer til | Kvifor |
|---|---|---|
| `make mcp-linkml-valider-modell` | `_mcp-valider-modell-with-header` (internt) | Detekterer POLICY frå build.yaml (eller bruker eksplisitt `POLICY=`), sender så vidare til det interne targetet som gjer sjølve valideringa |
| `make gource-preview` | `_gource-render` (internt) | Set `GOURCE_OUTFILE/EXTRA_FLAGS/FPS/FFMPEG_PRESET` for rask 720p-preview, kallar så delt render-oppskrift |
| `make gource-video` | `_gource-render` (internt) | Same mønster som over, men 1080p full kvalitet |
| `make mcp-linkml-modell-utkast` | `roundtrip-json-schema` (berre dersom `SCHEMA` er ei `.json`-fil) | Etter generering av eit JSON Schema-utkast køyrer targetet automatisk ein roundtrip-test som sjølvverifisering |

### "Bygg image berre viss det manglar"-vakt

Same `$(MAKE)`-delegeringsmønster, brukt for lat biletbygging
(`podman image exists ... || $(MAKE) build-docker-*`):

| Target | Byggjer (viss image manglar) |
|---|---|
| `_mcp-valider-modell-with-header` | `build-docker-mcp-validator` |
| `make validate-capture` | `build-docker-mcp-validator` |
| `make mcp-linkml-begrep-utkast-list-profiles` | `build-docker-mcp-begrep-utkast` |
| `make new-modell` | `build-docker-mcp-modell-utkast` |

**Merk — kontrasterande mønster:** `mcp-linkml-valider-modell-smoke`,
`mcp-linkml-valider-modell-test`, `mcp-linkml-modell-utkast-smoke`,
`mcp-linkml-modell-utkast-test`, `mcp-linkml-begrep-utkast-smoke`,
`gource-preview` og `gource-video` listar i staden `build-docker-*` som ein
vanleg Make-prerequisite (`target: build-docker-x`). Sidan
`build-docker-*`-target er `.PHONY`, tyder dette at biletet vert **bygd på
nytt kvar gong** desse targeta køyrer — til skilnad frå
`podman image exists`-vakten over, som berre byggjer ved behov. Dette er
altså to ulike, medvitne mønster med ulik åtferd, ikkje berre ein
stilskilnad.

### Konseptuelle wrapparar (ikkje `$(MAKE)`-kall)

`validate-informasjonsmodell-instance` og `validate-modellkatalog-instance`
(sjå tabellen under "Vedlikehald" nedanfor) vert omtala som "convenience
wrapper" for `make validate-instance` — men dei kallar **ikkje**
`make validate-instance` via `$(MAKE)`. Dei gjenbruker same underliggande
`linkml validate`-logikk direkte, med SCHEMA/INSTANCE-stiar auto-utleia frå
høvesvis `SCHEMA=` og `ORG=`.

## Container-image-bygging

Berre nødvendig ved første bruk eller etter endringar i Dockerfile.

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-all` | Byggjer alle container-image i repoet (alle radene under, pluss `build-docker-gource`). | Alle image over |
| `make build-docker-linkml` | Byggjer container-image for artefaktgenerering og validering. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/linkml-local:latest` |
| `make build-docker-mkdocs` | Byggjer container-image for dokumentasjonsportalen. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/mkdocs-local:latest` |
| `make build-docker-python` | Byggjer container-image for Python-testar. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/python-pytest:latest` |
| `make build-docker-mcp-modell-utkast` | Byggjer container-image for modell-utkast MCP-server. | Image `localhost/mcp-linkml-modell-utkast:latest` |
| `make build-docker-mcp-begrep-utkast` | Byggjer container-image for begrepsinstans-generator MCP-server. | Image `localhost/mcp-linkml-begrep-utkast:latest` |
| `make build-docker-mcp-validator` | Byggjer container-image for validator MCP-server. | Image `localhost/mcp-linkml-validator:latest` |
| `make build-docker-avrotize` | Byggjer container-image for XSD-generering via Avrotize. Nødvendig for `make gen-xsd`. | Image `localhost/avrotize-local:latest` |
| `make build-docker-asyncapi` | Byggjer container-image for AsyncAPI CLI-validering. Nødvendig for `make gen-asyncapi`. | Image `localhost/asyncapi-cli-local:latest` |
| `make build-docker-plantuml` | Byggjer container-image for PlantUML-diagram. Nødvendig for `make gen-plantuml`. | Image `localhost/plantuml:latest` |

## Ny modell/begrepskatalog/modellkatalog

| Kommando | Beskriving | Output |
|---|---|---|
| `make new-modell DOMAIN=<domene> NAME=<modell> [JSON_SCHEMA=<sti>]` | Opprettar katalogstruktur og boilerplate for ein ny LinkML-domenemodell. Utan `JSON_SCHEMA` genererast eit tomt stub-skjema (`--input-format empty`). Med `JSON_SCHEMA=<sti til eksportert JSON Schema>` genererast skjemaet frå JSON Schema-innhaldet i staden (same konvertering som `make mcp-linkml-modell-utkast`, men resultatet landar direkte i den nye katalogstrukturen med full etterbehandling — id/navn/tittel, `annotations.utgiver`/dato, versjonslåst import). Eksempeldatafila vert i begge tilfelle fylt med eit rikt syntetisk datasett — alle slots (ikkje berre obligatoriske/identifikator), kryssreferansar mellom genererte instansar (fell tilbake til ein minimal éin-linjes stub dersom automatisk generering feilar). | `src/linkml/<domain>/<modell>/<modell>-schema.yaml`<br>`src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml` |
| `make gen-eksempeldata SCHEMA=<sti> [OUT=<sti>] [ID_PREFIX=<prefiks>] [OVERWRITE=1]` | Genererer eit rikt syntetisk eksempeldatasett frå eit **eksisterande** skjema — same generator som `new-modell` nyttar internt, men tilgjengeleg direkte for manuell bruk (t.d. under lokal modellering, uavhengig av scaffolding av ein heilt ny modell). Utan `OUT` skriv resultatet til stdout. Med `OUT=<sti>` skriv til fil — nektar å overskrive ei eksisterande fil med mindre `OVERWRITE=1` er sett. Sjå `specs/done/gen-eksempeldata-fra-skjema.md`. | Stdout, eller `<OUT>` |
| `make remove-modell DOMAIN=<domene> NAME=<modell> [CONFIRM=1]` | Fjernar ein domenemodell etter tryggleikssjekkar (submodels-/imports-referansar, `publish_external`). Utan `CONFIRM=1` køyrer kommandoen berre sjekkane (dry-run) og viser kva som ville blitt sletta. | Sletta `src/linkml/<domain>/<modell>/` (berre med `CONFIRM=1`) |
| `make new-modellkatalog ORG=<alias>` | Opprettar katalogstruktur og boilerplate for ein ny organisasjonskatalog (modellkatalog + datakatalog). `<alias>` må vere registrert i `CODEOWNERS.md`-frontmatter med `catalog_slug`. | `src/linkml/modellkatalog/<catalog_slug>/` |
| `make new-begrepssamling DOMAIN=<domene> NAME=<begrepssamling>` | Opprettar katalogstruktur for ei ny begrepssamling. Oppretter `begrep/`-mappe og `build.yaml` med aggregation-metadata. Døme: `make new-begrepssamling DOMAIN=oreg NAME=begrepssamling-foretaksregisteret` | `src/linkml/<domain>/<begrepssamling>/` |

## Validering

| Kommando | Beskriving | Output | Batching |
|---|---|---|---|
| `make lint` | Linter alle skjema i repoet. | OK/FEIL per skjema til stdout; avsluttar med kode 1 ved feil | Batcha — `batch-lint.py`, éin delt `Linter`/`TerminalFormatter`-sesjon for alle skjema |
| `make lint SCHEMA=<sti>` | Linter eit enkelt skjema raskt utan å køyre generatorar. Nyttig for hurtigsjekk under utvikling. | OK/FEIL til stdout; avsluttar med kode 1 ved feil | Batcha (same mekanisme, N=1) |
| `make validate-instance SCHEMA=<sti> INSTANCE=<sti>` | Validerer ei datafil mot eit skjema utan lint og generatorar. Raskaste enkeltsjekk av datainnhald. | OK/FEIL til stdout; avsluttar med kode 1 ved feil | Ikkje batcha — eitt skjema/éin instans om gongen |
| `make roundtrip SCHEMA=<sti>` | Køyrer berre roundtrip-testane (JSON og TTL) for eitt skjema. Raskare enn full testsuite — nyttig etter skjema-endringar som kan påverke serialisering. | Testrapport for `roundtrip-json` og `roundtrip-ttl` til stdout; avsluttar med kode 1 ved feil | Batcha — `tests/test_make.sh` sitt Fase A/B-mønster (`batch-convert.py`), Kategori D |
| `make roundtrip` | Køyrer roundtrip-testar for alle skjema i repoet. | Testrapport til stdout; avsluttar med kode 1 ved feil | Batcha (same, for heile skjemalista) |
| `make roundtrip-json-schema JSONSCHEMA=<sti>` | Køyrer roundtrip-test spesifikt for JSON Schema-generering. Verifiserer at YAML → JSON Schema → YAML gjev same resultat. | Testrapport til stdout; avsluttar med kode 1 ved feil | Ikkje batcha — eiga testveg (MCP-modell-utkast-rundtur), utanfor Kategori A-D |
| `make test SCHEMA=<sti>` | Køyrer full testsuite (lint + validering + alle generatorar) for eitt skjema. | Samla testrapport til stdout; avsluttar med kode 1 ved feil | Batcha — Fase A/B-mønster (alle 17 teststeg, Kategori A-D), sjølv med eitt skjema |
| `make test` | Linter alle skjema og validerer alle eksempelfiler i heile repoet. | Samla testrapport til stdout; avsluttar med kode 1 ved feil | Batcha (same, for heile skjemalista testen dekkjer) |
| `make validate [DOMAIN=<domene>\|SCHEMA=<sti>]` | Validerer alle skjema (eller avgrensa til eit domene/eitt skjema) mot LinkML-metaskjemaet (strukturvalidering, ikkje policy), **og** at ingen skjema har lokale slots/klasser/typar/enum som kolliderer med navn frå importerte skjema (sjå `check-import-duplicates` under). Ingen fil skriven (fail-fast validering). Same target brukast både frittståande og som Fase 1-steget i `domain-*`-pipelinen (steg 1, sjå § "Generering av artefakter"). | Validerings-resultat per skjema til stdout | Batcha — `batch-generate.py --generator merge` + `check-import-duplicates.py`, éin kontainar kvar, mergar imports for alle skjema |
| `make check-import-duplicates [DOMAIN=<domene>\|SCHEMA=<sti>]` | Sjekkar at ingen skjema (eller avgrensa til eit domene/eitt skjema) har eit lokalt topnivå-slot/klasse/type/enum/subset med same navn som eit element alt definert i importkjeda (`imports:`, transitivt). Fangar feilen `Conflicting URIs (<schema-a>, <schema-b>) for item: <navn>` — som elles først dukkar opp djupt inne i python/proto/graphql/jsonld-context/plantuml-generatorane — tidleg og med presis, handlingsretta feilmelding. Brukar `linkml.utils.schemaloader.SchemaLoader(mergeimports=True).resolve()` direkte, same mekanisme desse generatorane alt bruker internt. Køyrt automatisk av `make validate` (og dermed CI) og av `make new-modell`. Sjå `specs/done/oreg-scaffold-generering-feiler.md` og `specs/backlog/new-modell-dublettsjekk-mot-imports.md`. | Suksess: `✓ Ingen import-kollisjonar funne (N skjema sjekka)` til stdout, kode 0. Feil: `[ERROR] ::error file=<sti>::...` per kollisjon + `✖ N av M skjema har import-kollisjonar`-oppsummering til stderr, kode 1. | Batcha — `check-import-duplicates.py`, éin kontainar for alle skjema |
| `make mcp-linkml-valider-modell SCHEMA=<sti>` | Policy-validering mot `validation_policy` frå build.yaml. POLICY kan overstyres med `POLICY=<bronze\|silver\|gold\|felles-datakatalog\|felles-begrepskatalog>`. Delegerer til `run-validation.sh` (same skript som CI brukar), så resultatet vert **òg** skrive til `src/linkml/<domain>/<modell>/validation/<versjon>/<policy>.json` og kopiert til `generated/<domain>/<modell>/validation/<versjon>/<policy>.json` — sistnemnde gjer at ein lokal `make docs-build`/`docs-serve`/`docs-publish` viser valideringsresultatet umiddelbart, utan noko separat synkroniseringssteg. | Pass/fail per policy-regel til stdout + JSON-loggfil begge stader | Ikkje batcha — tek berre eitt skjema; underliggande `batch-flatten-and-validate.py` støttar batching (brukt av `validate-data`), men eksponerast ikkje her |
| `make validate-capture` | Generer valideringsresultat for alle skjema og lagre til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`. | JSON-filer med valideringsresultat | Ikkje batcha — parallellisert (`--parallel`, ThreadPool), men éin kontainar per skjema |
| `make validate-capture SCHEMA=<sti>` | Generer valideringsresultat for eitt skjema og lagre til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`. | JSON-fil med valideringsresultat | Ikkje batcha |
| `make validate-data DOMAIN=<domene>` | Validerer alle datafiler i `data/`-katalogar i eit domene mot deira `validation_policy` frå build.yaml. Brukt i CI per domene. | Pass/fail per datafil til stdout | Batcha — same script med `--jobs-tsv`, heterogene (skjema, policy, datafil)-triplar i éin kontainar |
| `make validate-examples DOMAIN=<domene>` | Validerer alle eksempelfiler i eit domene mot tilhøyrande skjema. Brukt i CI per domene. | Pass/fail per eksempelfil til stdout; avsluttar med kode 1 ved feil | Batcha — `batch-linkml-validate.py --jobs-tsv <fil>`, éin kontainar for alle eksempelfiler i domenet (TSV bygd frå discovery-logikk med fixture-støtte) |
| `make validate-policy-logg (BUILDYAML=<sti>\|SCHEMA=<sti> POLICY=<policy>)` | Policy-validering med full JSON-logg. To måtar å kalle på: `SCHEMA=`+`POLICY=` validerer eit gitt skjema mot ein eksplisitt valt policy (overstyrer det som står i `build.yaml` — nyttig for å teste mot ein strengare/anna policy). `BUILDYAML=<sti-til-build.yaml>` validerer i staden modellen slik han faktisk er konfigurert: skjema-sti og policy vert utleia automatisk frå `build.yaml` (same som CI brukar). Nyttig for debugging av policy-reglar. | JSON-logg til stdout | Ikkje batcha |
| `make validate-instance-logg SCHEMA=<sti> INSTANCE=<sti>` | Instansvalidering med full JSON-logg. Nyttig for debugging av valideringsfeil. | JSON-logg til stdout | Ikkje batcha |


## Generering av artefakter

### Per domene (anbefalt)

Kvar `domain-*` target køyrer følgjande steg for alle skjema i domenet:

1. **Validering**: `merge-imports` mergar imports og validerer skjemaet (output vert kasta)
2. **Artefaktgenerering** (parallelt): JSON-LD context, SHACL, Python, JSON Schema, OWL, RDF, PlantUML, docs
3. **Eksempelkonvertering**: Konverterer `*-eksempel.yaml` til RDF/Turtle via `convert-instance-rdf DOMAIN=<domene>` (dersom `example_rdf: true`)
4. **Modellmanifest** (parallelt): Genererer Informasjonsmodell-instans ihht ModelDCAT-AP-NO til `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`

**Parallellisering**: Steg 2 og 4 vert fase-parallelliserte automatisk av
`run-domain-pipeline.sh` — ingen brukarstyrt jobb-tal (`PARALLEL` er fjerna,
sjå `specs/done/evaluer-parallel-flag-etter-batching.md`).

Parallell køyring viser timer per jobb: `→ gen-jsonld-context ap-no/dcat-ap-no (5.1s)`

**Batching:** `domain-*` er sjølv **ikkje** ei batch-operasjon — han er ein
fase-parallell *orkestrator* (`run-domain-pipeline.sh`) som kallar kvart av
steg 1-4 over som eit eige, rekursivt `$(MAKE) <target> DOMAIN=<domene>`-kall.
Batchinga skjer eitt nivå ned, i **kvart einskild** steg (alle fire er
batcha på tvers av skjema i domenet — sjå "Batching"-kolonna i tabellen
under § "Enkeltartefakter" for mekanismen per generator, inkludert
`convert-instance-rdf DOMAIN=<domene>` som er steg 3 sin batcha
eksempelkonverterings-mekanisme). `domain-*` batchar altså ikkje på tvers av **domene** —
`make domain-ap-no` og `make domain-oreg` er framleis to separate
kommandokøyringar.

| Kommando | Beskriving | Output |
|---|---|---|
| `make domain-ap-no` | Valider + generer alle artefakter for alle AP-NO-profiler (parallelt) | `generated/ap-no/` |
| `make domain-begrepskatalog` | Valider + generer alle artefakter for begrepskatalogmodellane | `generated/begrepskatalog/` |
| `make domain-fair` | Valider + generer alle artefakter for FAIR-metadata | `generated/fair/` |
| `make domain-fint` | Valider + generer alle artefakter for FINT-modellane | `generated/fint/` |
| `make domain-modellkatalog` | Valider + generer alle artefakter for modellkatalogmodellane | `generated/modellkatalog/` |
| `make domain-ngr` | Valider + generer alle artefakter for NGR-modellane | `generated/ngr/` |
| `make domain-oreg` | Valider + generer alle artefakter for OREG-registera | `generated/oreg/` |
| `make domain-samt` | Valider + generer alle artefakter for SAMT-modellane | `generated/samt/` |

### Enkeltartefakter

Alle `gen-*` targets støttar tre bruksmåtar:

- **`make gen-<format>`** — generer for **alle** skjema
- **`make gen-<format> DOMAIN=<domene>`** — generer for alle skjema i **eitt domene**
- **`make gen-<format> SCHEMA=<sti>`** — generer for **eitt** spesifikt skjema

| Kommando | Beskriving | Output | Batching |
|---|---|---|---|
| <a id="gen-jsonld-context"></a>`make gen-jsonld-context [DOMAIN=...] [SCHEMA=...]` | JSON-LD kontekst | `generated/<domain>/<modell>/<modell>-context.jsonld` | Batcha — `batch-generate.py --generator jsonld-context`, éin kontainar |
| <a id="gen-shacl"></a>`make gen-shacl [DOMAIN=...] [SCHEMA=...]` | SHACL shapes | `generated/<domain>/<modell>/<modell>-shapes.ttl` | Batcha — `batch-generate.py --generator shacl` |
| <a id="gen-python"></a>`make gen-python [DOMAIN=...] [SCHEMA=...]` | Python-dataklasser | `generated/<domain>/<modell>/<modell>-model.py` | Batcha — `batch-generate.py --generator python` |
| <a id="gen-jsonschema"></a>`make gen-jsonschema [DOMAIN=...] [SCHEMA=...]` | JSON Schema | `generated/<domain>/<modell>/<modell>-schema.json` | Batcha — `batch-generate.py --generator json-schema` |
| <a id="gen-owl"></a>`make gen-owl [DOMAIN=...] [SCHEMA=...]` | OWL/Turtle-ontologi | `generated/<domain>/<modell>/<modell>-ontology.ttl` | Batcha — `batch-generate.py --generator owl` |
| <a id="gen-rdf"></a>`make gen-rdf [DOMAIN=...] [SCHEMA=...]` | RDF/Turtle-graf av skjemaet | `generated/<domain>/<modell>/<modell>-schema.ttl` | Batcha — `batch-generate.py --generator rdf` |
| <a id="gen-erdiagram-mermaid"></a>`make gen-erdiagram-mermaid [DOMAIN=...] [SCHEMA=...]` | Mermaid ER-diagram | `generated/<domain>/<modell>/<modell>-erdiagram.md` | Delvis batcha — Fase A (linkml-generering) og Fase B (Python-filter) batcha, Fase A.5 (awk-filtrering) køyrer per skjema direkte på host, ikkje kontainerisert |
| <a id="gen-schema-docs"></a>`make gen-schema-docs [DOMAIN=...] [SCHEMA=...]` | HTML-klassereferanse og Mermaid ER-diagram | `generated/<domain>/<modell>/docs/` | Batcha — to fasar (`batch-generate-instances.py --generator docgen-examples` + `batch-generate.py --generator doc`) |
| <a id="gen-proto"></a>`make gen-proto [DOMAIN=...] [SCHEMA=...]` | Protocol Buffers-skjema | `generated/<domain>/<modell>/<modell>-schema.proto` | Batcha — `batch-generate.py --generator proto` |
| <a id="gen-graphql"></a>`make gen-graphql [DOMAIN=...] [SCHEMA=...]` | GraphQL-skjema (SDL, berre skjema med `graphql: true` i build.yaml) | `generated/<domain>/<modell>/<modell>-schema.graphql` | Batcha — `batch-generate.py --generator graphql` |
| <a id="gen-java"></a>`make gen-java [DOMAIN=...] [SCHEMA=...]` | Java-klasser (Lombok `@Data`, berre skjema med `java: true` i build.yaml) | `generated/<domain>/<modell>/java/*.java` | Batcha — `batch-generate.py --generator java` |
| <a id="gen-plantuml"></a>`make gen-plantuml [DOMAIN=...] [SCHEMA=...]` | PlantUML-diagram og SVG | `generated/<domain>/<modell>/diagrams/<modell>.svg` | Batcha — tre fasar (rå .puml-generering, Python-filter, SVG-rendering for **alle** skjema samla i éin PlantUML-kontainar) |
| <a id="gen-xsd"></a>`make gen-xsd [DOMAIN=...] [SCHEMA=...]` | XSD-skjema via Avrotize (berre skjema med `xsd: true` i build.yaml) | `generated/<domain>/<modell>/<modell>-schema.xsd` | Batcha — `batch-gen-xsd.sh` køyrer `avrotize j2a`/`a2x`/`fix-xsd-dates.py` sekvensielt for alle skjema inni éin kontainar (amortiserer kontainar-oppstart). **Kjend støy:** `xsd: true` på eit skjema med to eller fleire `inlined_as_list`-containerattributt gir ei ufarleg, ikkje-deterministisk `WARNING: Unable to resolve circular dependency`-linje i DEBUG-loggen (BUG-9, sjå `bugs/avrotize-falsk-circular-dependency-warning.md`) — påverkar ikkje byggresultatet |
| <a id="gen-asyncapi"></a>`make gen-asyncapi [DOMAIN=...] [SCHEMA=...]` | AsyncAPI 3.0-spec (berre skjema med `asyncapi: true` i build.yaml) | `generated/<domain>/<modell>/<modell>-asyncapi.yaml` | Batcha — generering batcha via `batch-generate-instances.py`, validering batcha via `batch-asyncapi-validate.sh` i éin Node.js-kontainar (amortiserer kontainar-oppstart) |
| <a id="gen-openapi"></a>`make gen-openapi [DOMAIN=...] [SCHEMA=...]` | OpenAPI 3.1-spec (berre skjema med `openapi: true` i build.yaml) | `generated/<domain>/<modell>/<modell>-openapi.yaml` | Batcha — generering og validering saman i éin kontainar |
| <a id="gen-config"></a>`make gen-config` | Regenererer generatorkonfigurasjon frå alle `build.yaml`-filer. Ingen argument. | `config.mk` (repo-rot) | Ikkje aktuelt — eitt samla script over alle `build.yaml`, ikkje eit per-skjema-kontainarkall |
| <a id="gen-dqv-measurements"></a>`make gen-dqv-measurements` | Oppdaterer DQV-kvalitetsmålingar direkte i datamanifest-filene, for alle datafiler med `validation_policy` sett. Ingen argument. | `src/linkml/<domain>/<modell>/data/<katalog>/build.yaml` (oppdatert in-place) | Ikkje aktuelt — eitt samla script over alle datamanifest, ikkje eit per-skjema-kontainarkall |
| <a id="gen-modelldcat-elements"></a>`make gen-modelldcat-elements [ORG=<alias>] [DRYRUN=1]` | ModelDCAT-element for modellkatalogdata. `ORG=` avgrensar til éin organisasjon, `DRYRUN=1` viser endringar utan å skrive til disk. | `src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml` | Ikkje aktuelt — same grunn |
| <a id="convert-instance-rdf"></a>`make convert-instance-rdf [DOMAIN=<domene>]` | Konverter eksempel-YAML til RDF/Turtle — repo-vidt utan `DOMAIN=`, avgrensa til eitt domene med `DOMAIN=<domene>` (sistnemnde er steg 3, "Eksempelkonvertering", i `domain-*`-pipelinen, sjeldan kalla frittståande der). | `generated/<domain>/<modell>/<modell>-eksempel.ttl` | Batcha — `batch-generate-instances.py --generator convert --jobs-tsv <fil>`, éin kontainar for alle filer (TSV bygd via `convert-examples.sh`) |
| <a id="convert-data"></a>`make convert-data` | Konverter produksjonsdatafiler i `data/`-underkatalogar til RDF/Turtle (berre `publish_external: true`) | `generated/<domain>/<katalog>/<katalog>.ttl` | Batcha — same mekanisme som `convert-instance-rdf` (TSV bygd via `convert-data.sh`) |
| <a id="clean"></a>`make clean` | Slett `generated/` | — | Ikkje aktuelt |

Nye skjema under `src/linkml/<domain>/<modell>/` vert oppdaga automatisk — ingen Makefile-endringar nødvendig.

### Vedlikehald

| Kommando | Beskriving | Output | Batching |
|---|---|---|---|
| <a id="gen-informasjonsmodell-instance"></a>`make gen-informasjonsmodell-instance SCHEMA=<sti>` | Genererer ModelDCAT-metadata-fil (`metadata/modelldcat.yaml`) for eit enkelt skjema. Samlar data frå 6 kjelder: schema.yaml (toppnivå + annotations), build.yaml, CODEOWNERS.md, lokale klasser, genererte artefakter, er_profil_av. Genererer inline Kontaktopplysning og Standard-instansar. | `src/linkml/<domain>/<modell>/metadata/modelldcat.yaml` | Batcha — `batch-generate-instances.py --generator informasjonsmodell`, reint Python, éin kontainar (gevinsten realiserast fullt ut når kalla for fleire skjema, t.d. via `domain-*`/`DOMAIN=`) |
| <a id="validate-informasjonsmodell-instance"></a>`make validate-informasjonsmodell-instance SCHEMA=<sti>` | Validerer generert ModelDCAT-metadata mot modelldcat-katalog-schema.yaml med full LinkML-validering. Sjekkar YAML-struktur, obligatoriske felt, LangString-format og inline-instansar. Køyrer i LinkML-container for korrekt schema-oppløysing. **Convenience-target** (ikkje eit `$(MAKE)`-kall til `validate-instance` — sjå [§ Wrapper-target](#wrapper-target)): gjenbruker same underliggande valideringslogikk, men via eige script som auto-detekterer `metadata/modelldcat.yaml` og schema-sti. | Pass/fail til stdout; avsluttar med kode 1 ved feil | Ikkje batcha — eitt skjema om gongen |
| <a id="gen-begrepskatalog-instance"></a>`make gen-begrepskatalog-instance` | Samlar alle begrep frå begrepssamlingar og genererer begrepskatalog per organisasjon. Finn alle begrepssamlingar med `aggregation.organization`-metadata, samle begrep-YAML-filer frå `begrep/*.yaml`, og generer aggregert begrepskatalog under `begrepskatalog/<org>-begrepskatalog/data/`. Køyrast automatisk av CI før generatorfasen. | `src/linkml/begrepskatalog/<org>-begrepskatalog/data/<org>-begrepskatalog/<org>-begrepskatalog.yaml` | Ikkje aktuelt — eitt samla script over alle begrepssamlingar, ikkje eit per-skjema-kontainarmønster |
| <a id="gen-modellkatalog-instance"></a>`make gen-modellkatalog-instance` | Genererer per-org modellkatalogar frå alle `metadata/modelldcat.yaml`-filer. Grupper Informasjonsmodell-instansar etter utgiver (frå CODEOWNERS.md) og genererer éi katalogfil per organisasjon for publisering til Felles datakatalog. Konverterer standard URI-ar (`https://data.norge.no/...`) til org-spesifikke URI-ar (`https://<org-domene>/modellkatalogar/<catalog_slug>/...`). | `src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml` | Ikkje aktuelt — same grunn |
| <a id="validate-modellkatalog-instance"></a>`make validate-modellkatalog-instance ORG=<alias>` | Validerer generert modellkatalog-datafil mot org-spesifikt schema. Eksempel: `ORG=digdir`. `ORG=` er CODEOWNERS-aliasen (same form som `new-modellkatalog`/`gen-modelldcat-elements`), slått opp mot `catalog_slug` via `resolve-catalog-slug.sh`. Validerer `src/linkml/modellkatalog/<catalog_slug>/data/<catalog_slug>/<catalog_slug>.yaml` mot `src/linkml/modellkatalog/<catalog_slug>/<catalog_slug>-schema.yaml`. **Convenience-target** (ikkje eit `$(MAKE)`-kall til `validate-instance` — sjå [§ Wrapper-target](#wrapper-target)): køyrer same underliggande `linkml validate`-kommando direkte, med schema- og instans-stiar auto-konstruerte frå `ORG=`. | Pass/fail til stdout; avsluttar med kode 1 ved feil | Ikkje batcha |

## Dokumentasjonsportal

| Kommando | Beskriving | Output |
|---|---|---|
| `make docs-publish` | Kopier `generated/` → `mkdocs/docs/` og regenerer `mkdocs.yml` | `mkdocs/docs/` |
| `make docs-serve` | Start lokal dev-server med live reload. Leser `mkdocs/docs/` | `http://localhost:8000` |
| `make docs-build` | Bygg statisk HTML-site (CI-pipeline for produksjon) | `mkdocs/site/` |

`make docs-publish` køyrer `mkdocs/publish.sh` som kopier artefakter og dokumentasjon frå `generated/` til `mkdocs/docs/`, genererer `index.md` per skjema og domene, og oppdaterer navigasjonsstrukturen i `mkdocs.yml`. Nye domene og skjema dukkar opp automatisk neste gong `publish` vert køyrt.

## LinkML-modell utkast (mcp-linkml-modell-utkast)

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-mcp-modell-utkast` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-modell-utkast:latest` |
| `make mcp-linkml-modell-utkast-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-modell-utkast-test` | Køyrer alle unit-testar for MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-modell-utkast SCHEMA=<sti>` | Genererer eit LinkML-skjemautkast frå ei JSON Schema-fil ved hjelp av MCP-serveren. | `<same katalog>/<modell>-schema.yaml` |
| `make mcp-linkml-modell-utkast SCHEMA=<sti> FORMAT=json-schema POLICY=default` | Same som over med eksplisitt format og policy. | `<same katalog>/<modell>-schema.yaml` |
| `make mcp-linkml-modell-utkast-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## LinkML-begrep utkast (mcp-linkml-begrep-utkast)

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-mcp-begrep-utkast` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-begrep-utkast:latest` |
| `make mcp-linkml-begrep-utkast-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-begrep-utkast-list-profiles` | Listar alle tilgjengelege organisasjonsprofiler som kan brukast ved oppretting av begrep. | JSON-liste over profil-ID-ar til stdout |
| `make mcp-linkml-begrep-utkast INPUT=<sti-til-json>` | Genererer eit YAML-utkast til begrep frå ei JSON-fil med argument til `opprett_begrep`. | YAML-blokker til stdout |
| `make mcp-linkml-begrep-utkast-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## LinkML-validator (mcp-linkml-validator)

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-mcp-validator` | Byggjer container-image for validator MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-validator:latest` |
| `make mcp-linkml-valider-modell-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-valider-modell-test` | Køyrer alle policy-testar for validator MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-valider-modell-run` | Startar validator MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## Modell-analyse

Informative rapportar på tvers av alle skjema — finn moglege navnekollisjonar
og IRI-ar som ikkje let seg derefere. Feilar aldri (ikkje ein valideringspolicy);
brukt av den vekentlege `.github/workflows/modell-analyse.yml`. Navne-
samanlikninga brukar berre klasser/slots/typar (`types:`) definerte lokalt i
kvart skjema (ikkje navn arva via `imports`), og fuzzy string-likskap
(`difflib.SequenceMatcher`) — juster terskel med `SIMILARITY_THRESHOLD`.
Avgrens til eitt domene med `DOMAIN=<domene>` eller éin modell med
`NAME=<modell>` (kombiner med `DOMAIN=` for direkte oppslag, eller bruk
`NAME=` åleine for søk på tvers av domene).

`analyse-similar-classes-domain`/`analyse-similar-slots-domain`/
`analyse-similar-types-domain` køyrer i tillegg automatisk **per skjema** i
`.github/workflows/generate.yml` (steget «Køyr modellanalyse per skjema») —
resultatet er synleg som `## Modellanalyse`-seksjonen i kvar modell sin
dokumentasjonsside, rett etter `## Valideringsresultat`. Denne embedda
seksjonen er avgrensa til domene-scopa, offline sjekkar (ikkje cross-domain,
ikkje IRI-/nettverkssjekkar) — sjå
`specs/done/modellanalyse-per-skjema-index-md.md` for grunngjeving.

| Kommando | Beskriving | Output |
|---|---|---|
| `make analyse-similar-classes-domain [SIMILARITY_THRESHOLD=0.8]` | Finn klasser med liknande navn innanfor same domene. | Markdown-tabell til stdout |
| `make analyse-similar-classes-all [SIMILARITY_THRESHOLD=0.8]` | Finn klasser med liknande navn på tvers av alle domene. | Markdown-tabell til stdout |
| `make analyse-similar-slots-domain [SIMILARITY_THRESHOLD=0.8]` | Finn slots med liknande navn innanfor same domene. | Markdown-tabell til stdout |
| `make analyse-similar-slots-all [SIMILARITY_THRESHOLD=0.8]` | Finn slots med liknande navn på tvers av alle domene. | Markdown-tabell til stdout |
| `make analyse-similar-types-domain [SIMILARITY_THRESHOLD=0.8]` | Finn typar (`types:`) med liknande navn innanfor same domene. | Markdown-tabell til stdout |
| `make analyse-similar-types-all [SIMILARITY_THRESHOLD=0.8]` | Finn typar (`types:`) med liknande navn på tvers av alle domene. | Markdown-tabell til stdout |
| `make analyse-iri-dereferering` | Testar IRI-dereferering (IRI resolution) for `id`/`default_prefix`/`prefixes`-IRI-ar i alle skjema. Kjende, avgjorde ikkje-dereferbare mønster (`schema.fintlabs.no`, `data.norge.no/vocabulary/ngr-*`, `example.org`-plasshaldarar) er utelatne frå testen. Krev nettverkstilgang. | Markdown-tabell til stdout |
| `make analyse-innhaldsforhandling` | Testar innhaldsforhandling (Accept-header for format/språk) for IRI-ar repoet eig (`id`/`default_prefix`). Krev nettverkstilgang. | Markdown-tabell til stdout |
| `make analyse-sammendrag` | Les dei åtte `analyse-*`-rapportfilene og skriv ein konsolidert sammendrag-tabell med tal på funn/feil per sjekk-type. Krev at rapportfilene alt finst (generert av dei andre `analyse-*`-måla). | Markdown-tabell til stdout |

## Påskeegg: Gource-visualisering

Krev `make build-docker-gource` éin gong (eller etter endringar i Dockerfile). Output-filer havner i `tmp/`.

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-gource` | Byggjer container-image med Gource og ffmpeg. | Image `localhost/gource-local:latest` |
| `make gource-preview` | Genererer ein 30fps-preview-video av heile git-historikken (rask, lågare kvalitet). | `tmp/gource-preview.mp4` |
| `make gource-video` | Genererer ein 60fps fullkvalitetsvideo av heile git-historikken. | `tmp/gource.mp4` |

