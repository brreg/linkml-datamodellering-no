# Kommandoar

Alle kommandoar køyrer via containerar — ingen lokal Python-installasjon trengst.

## Oppsett og føresetnadar

| Kommando | Beskriving | Output |
|---|---|---|
| `make check-prereqs` | Sjekkar at Git, Podman, GNU make, user namespace og ledig diskplass er korrekt konfigurert | Skriv OK/FEIL per føresetnad til stdout; avsluttar med kode 1 ved feil |

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
make gen-docs SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml LOGLVL=DEBUG

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
Dette er noko anna enn **parallellisering** (`PARALLEL=N`, sjå § "Generering
av artefakter"): parallellisering styrer kor mange skjema som køyrer
**samstundes** (fleire prosessar), medan batching styrer kor mange
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
| `make new-modell NAME=<modell> DOMAIN=<domain>` | Opprettar katalogstruktur og boilerplate for ein ny LinkML-domenemodell.  | `src/linkml/<domain>/<modell>/<modell>-schema.yaml`<br>`src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml` |
| `make new-modellkatalog NAME=<alias>` | Opprettar katalogstruktur og boilerplate for ein ny organisasjonskatalog (modellkatalog + datakatalog). `<alias>` må vere registrert i `CODEOWNERS.md`-frontmatter med `catalog_slug`. | `src/linkml/modellkatalog/<catalog_slug>/` |
| `make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>` | Opprettar katalogstruktur for ei ny begrepssamling. Oppretter `begrep/`-mappe og `build.yaml` med aggregation-metadata. Døme: `make new-begrepssamling DOMAIN=oreg NAME=begrepssamling-foretaksregisteret` | `src/linkml/<domain>/<begrepssamling-namn>/` |
| `make new-begrepskatalog NAME=<katalognavn>` | **Legacy**, ikkje ein alias for `make new-begrepssamling` — eige script, eigen monolittisk `BegrepContainer`-skjemastruktur. Bruk `make new-begrepssamling` for nye begrepssamlingar; dette targetet held fram fordi `brreg-begrepskatalog` alt nyttar formatet. | `src/linkml/begrepskatalog/<katalognavn>/` |

## Validering

| Kommando | Beskriving | Output | Batching |
|---|---|---|---|
| `make lint` | Linter alle skjema i repoet. | OK/FEIL per skjema til stdout; avsluttar med kode 1 ved feil | Batcha — `batch-lint.py`, éin delt `Linter`/`TerminalFormatter`-sesjon for alle skjema |
| `make lint SCHEMA=<sti>` | Linter eit enkelt skjema raskt utan å køyre generatorar. Nyttig for hurtigsjekk under utvikling. | OK/FEIL til stdout; avsluttar med kode 1 ved feil | Batcha (same mekanisme, N=1) |
| `make validate-instance SCHEMA=<sti> INSTANCE=<sti>` | Validerer ei datafil mot eit skjema utan lint og generatorar. Raskaste enkeltsjekk av datainnhald. | OK/FEIL til stdout; avsluttar med kode 1 ved feil | Ikkje batcha — eitt skjema/éin instans om gongen |
| `make roundtrip SCHEMA=<sti>` | Køyrer berre roundtrip-testane (JSON og TTL) for eitt skjema. Raskare enn full testsuite — nyttig etter skjema-endringar som kan påverke serialisering. | Testrapport for `roundtrip-json` og `roundtrip-ttl` til stdout; avsluttar med kode 1 ved feil | Batcha — `tests/test_make.sh` sitt Fase A/B-mønster (`batch-convert.py`), Kategori D |
| `make roundtrip` | Køyrer roundtrip-testar for alle skjema i repoet. | Testrapport til stdout; avsluttar med kode 1 ved feil | Batcha (same, for heile skjemalista) |
| `make roundtrip-json-schema SCHEMA=<sti>` | Køyrer roundtrip-test spesifikt for JSON Schema-generering. Verifiserer at YAML → JSON Schema → YAML gjev same resultat. | Testrapport til stdout; avsluttar med kode 1 ved feil | Ikkje batcha — eiga testveg (MCP-modell-utkast-rundtur), utanfor Kategori A-D |
| `make test SCHEMA=<sti>` | Køyrer full testsuite (lint + validering + alle generatorar) for eitt skjema. | Samla testrapport til stdout; avsluttar med kode 1 ved feil | Batcha — Fase A/B-mønster (alle 17 teststeg, Kategori A-D), sjølv med eitt skjema |
| `make test` | Linter alle skjema og validerer alle eksempelfiler i heile repoet. | Samla testrapport til stdout; avsluttar med kode 1 ved feil | Batcha (same, for heile skjemalista testen dekkjer) |
| `make validate` | Validerer alle skjema mot LinkML-metaskjemaet (strukturvalidering, ikkje policy). | Validerings-resultat per skjema til stdout | Batcha — `batch-generate.py --generator merge`, éin kontainar mergar imports for alle skjema |
| `make mcp-linkml-valider-modell SCHEMA=<sti>` | Policy-validering mot `validation_policy` frå build.yaml. POLICY kan overstyres med `POLICY=<bronze\|silver\|gold\|felles-datakatalog\|felles-begrepskatalog>`. | Pass/fail per policy-regel til stdout | Ikkje batcha — tek berre eitt skjema; underliggande `batch-flatten-and-validate.py` støttar batching (brukt av `validate-bronze`/`validate-data`), men eksponerast ikkje her |
| `make validate-capture` | Generer valideringsresultat for alle skjema og lagre til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`. | JSON-filer med valideringsresultat | Ikkje batcha — parallellisert (`--parallel`, ThreadPool), men éin kontainar per skjema |
| `make validate-capture SCHEMA=<sti>` | Generer valideringsresultat for eitt skjema og lagre til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`. | JSON-fil med valideringsresultat | Ikkje batcha |
| `make validate-bronze DOMAIN=<domain>` | Validerer alle skjema i eit domene mot bronze-policy (basis skjemakvalitet). Brukt i CI per domene. | Pass/fail per skjema til stdout; avsluttar med kode 1 ved feil | Batcha — `batch-flatten-and-validate.py --policy bronze`, éin kontainar for alle skjema i domenet |
| `make validate-data DOMAIN=<domain>` | Validerer alle datafiler i `data/`-katalogar i eit domene mot deira `validation_policy` frå build.yaml. Brukt i CI per domene. | Pass/fail per datafil til stdout | Batcha — same script med `--jobs-tsv`, heterogene (skjema, policy, datafil)-triplar i éin kontainar |
| `make validate-examples DOMAIN=<domain>` | Validerer alle eksempelfiler i eit domene mot tilhøyrande skjema. Brukt i CI per domene. | Pass/fail per eksempelfil til stdout; avsluttar med kode 1 ved feil | Batcha — `batch-linkml-validate.py --jobs-tsv <fil>`, éin kontainar for alle eksempelfiler i domenet (TSV bygd frå discovery-logikk med fixture-støtte) |
| `make log-mcp-validate SCHEMA=<sti>` | Policy-validering med full JSON-logg. Nyttig for debugging av policy-reglar. | JSON-logg til stdout | Ikkje batcha |
| `make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>` | Instansvalidering med full JSON-logg. Nyttig for debugging av valideringsfeil. | JSON-logg til stdout | Ikkje batcha |


## Generering av artefakter

### Per domene (anbefalt)

Kvar `domain-*` target køyrer følgjande steg for alle skjema i domenet:

1. **Validering**: `merge-imports` mergar imports og validerer skjemaet (output vert kasta)
2. **Artefaktgenerering** (parallelt): JSON-LD context, SHACL, Python, JSON Schema, OWL, RDF, PlantUML, docs
3. **Eksempelkonvertering**: Konverterer `*-eksempel.yaml` til RDF/Turtle via `gen-linkml-convert` (dersom `example_rdf: true`)
4. **Modellmanifest** (parallelt): Genererer Informasjonsmodell-instans ihht ModelDCAT-AP-NO til `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`

**Parallellisering**: Alle `domain-*` targets støttar `PARALLEL` parameter (default: 8 jobbar).

- `make domain-ap-no` — køyrer med 8 parallelle jobbar (default)
- `make domain-ap-no PARALLEL=16` — køyrer med 16 parallelle jobbar
- `make domain-ap-no PARALLEL=1` — køyrer sekvensielt (debugging)

Parallell køyring viser timer per jobb: `→ gen-jsonld-context ap-no/dcat-ap-no (5.1s)`

**Batching:** `domain-*` er sjølv **ikkje** ei batch-operasjon — han er ein
fase-parallell *orkestrator* (`run-domain-pipeline.sh`) som kallar kvart av
steg 1-4 over som eit eige, rekursivt `$(MAKE) <target> DOMAIN=<domain>`-kall.
Batchinga skjer eitt nivå ned, i **kvart einskild** steg (alle fire er
batcha på tvers av skjema i domenet — sjå "Batching"-kolonna i tabellen
under § "Enkeltartefakter" for mekanismen per generator, inkludert
`gen-linkml-convert` som er steg 3 sin batcha eksempelkonverterings-
mekanisme). `domain-*` batchar altså ikkje på tvers av **domene** —
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
- **`make gen-<format> DOMAIN=<domain>`** — generer for alle skjema i **eitt domene**
- **`make gen-<format> SCHEMA=<sti>`** — generer for **eitt** spesifikt skjema

| Kommando | Beskriving | Output | Batching |
|---|---|---|---|
| <a id="gen-jsonld-context"></a>`make gen-jsonld-context [DOMAIN=...] [SCHEMA=...]` | JSON-LD kontekst | `generated/<domain>/<modell>/<modell>-context.jsonld` | Batcha — `batch-generate.py --generator jsonld-context`, éin kontainar |
| <a id="gen-shacl"></a>`make gen-shacl [DOMAIN=...] [SCHEMA=...]` | SHACL shapes | `generated/<domain>/<modell>/<modell>-shapes.ttl` | Batcha — `batch-generate.py --generator shacl` |
| <a id="gen-python"></a>`make gen-python [DOMAIN=...] [SCHEMA=...]` | Python-dataklassar | `generated/<domain>/<modell>/<modell>-model.py` | Batcha — `batch-generate.py --generator python` |
| <a id="gen-jsonschema"></a>`make gen-jsonschema [DOMAIN=...] [SCHEMA=...]` | JSON Schema | `generated/<domain>/<modell>/<modell>-schema.json` | Batcha — `batch-generate.py --generator json-schema` |
| <a id="gen-owl"></a>`make gen-owl [DOMAIN=...] [SCHEMA=...]` | OWL/Turtle-ontologi | `generated/<domain>/<modell>/<modell>-ontology.ttl` | Batcha — `batch-generate.py --generator owl` |
| <a id="gen-rdf"></a>`make gen-rdf [DOMAIN=...] [SCHEMA=...]` | RDF/Turtle-graf av skjemaet | `generated/<domain>/<modell>/<modell>-schema.ttl` | Batcha — `batch-generate.py --generator rdf` |
| <a id="gen-erdiagram"></a>`make gen-erdiagram [DOMAIN=...] [SCHEMA=...]` | Mermaid ER-diagram | `generated/<domain>/<modell>/<modell>-erdiagram.md` | Delvis batcha — Fase A (linkml-generering) og Fase B (Python-filter) batcha, Fase A.5 (awk-filtrering) køyrer per skjema direkte på host, ikkje kontainerisert |
| <a id="gen-docs"></a>`make gen-docs [DOMAIN=...] [SCHEMA=...]` | HTML-klassereferanse og Mermaid ER-diagram | `generated/<domain>/<modell>/docs/` | Batcha — to fasar (`batch-generate-instances.py --generator docgen-examples` + `batch-generate.py --generator doc`) |
| <a id="gen-proto"></a>`make gen-proto [DOMAIN=...] [SCHEMA=...]` | Protocol Buffers-skjema | `generated/<domain>/<modell>/<modell>-schema.proto` | Batcha — `batch-generate.py --generator proto` |
| <a id="gen-graphql"></a>`make gen-graphql [DOMAIN=...] [SCHEMA=...]` | GraphQL-skjema (SDL, berre skjema med `graphql: true` i build.yaml) | `generated/<domain>/<modell>/<modell>-schema.graphql` | Batcha — `batch-generate.py --generator graphql` |
| <a id="gen-plantuml"></a>`make gen-plantuml [DOMAIN=...] [SCHEMA=...]` | PlantUML-diagram og SVG | `generated/<domain>/<modell>/diagrams/<modell>.svg` | Batcha — tre fasar (rå .puml-generering, Python-filter, SVG-rendering for **alle** skjema samla i éin PlantUML-kontainar) |
| <a id="gen-xsd"></a>`make gen-xsd [DOMAIN=...] [SCHEMA=...]` | XSD-skjema via Avrotize (berre skjema med `xsd: true` i build.yaml) | `generated/<domain>/<modell>/<modell>-schema.xsd` | Batcha — `batch-gen-xsd.sh` køyrer `avrotize j2a`/`a2x`/`fix-xsd-dates.py` sekvensielt for alle skjema inni éin kontainar (amortiserer kontainar-oppstart) |
| <a id="gen-asyncapi"></a>`make gen-asyncapi [DOMAIN=...] [SCHEMA=...]` | AsyncAPI 3.0-spec (berre skjema med `asyncapi: true` i build.yaml) | `generated/<domain>/<modell>/<modell>-asyncapi.yaml` | Batcha — generering batcha via `batch-generate-instances.py`, validering batcha via `batch-asyncapi-validate.sh` i éin Node.js-kontainar (amortiserer kontainar-oppstart) |
| <a id="gen-openapi"></a>`make gen-openapi [DOMAIN=...] [SCHEMA=...]` | OpenAPI 3.1-spec (berre skjema med `openapi: true` i build.yaml) | `generated/<domain>/<modell>/<modell>-openapi.yaml` | Batcha — generering og validering saman i éin kontainar |
| <a id="gen-config"></a>`make gen-config [DOMAIN=...] [SCHEMA=...]` | Generatorkonfigurasjon frå build.yaml | `generated/<domain>/<modell>/config.yaml` | Ikkje aktuelt — eitt samla script over alle `build.yaml`, ikkje eit per-skjema-kontainarkall |
| <a id="gen-dqv-measurements"></a>`make gen-dqv-measurements [DOMAIN=...] [SCHEMA=...]` | DQV-kvalitetsmålingar for datakatalogdata | `generated/<domain>/<modell>/dqv-measurements.ttl` | Ikkje aktuelt — same grunn |
| <a id="gen-modelldcat-elements"></a>`make gen-modelldcat-elements [DOMAIN=...] [SCHEMA=...]` | ModelDCAT-element for modellkatalogdata | `generated/<domain>/<modell>/modelldcat-elements.ttl` | Ikkje aktuelt — same grunn |
| <a id="gen-linkml-convert"></a>`make gen-linkml-convert DOMAIN=<domain>` | Konverter eksempel-YAML til RDF/Turtle for eitt domene — dette er steg 3 ("Eksempelkonvertering") i `domain-*`-pipelinen, sjeldan kalla frittståande. **Ikkje** same implementasjon som `convert-rdf` under, sjølv om resultatet er likt. | `generated/<domain>/<modell>/<modell>-eksempel.ttl` | Batcha — `batch-generate-instances.py --generator convert --jobs-tsv <fil>`, éin kontainar for alle skjema i domenet |
| <a id="convert-rdf"></a>`make convert-rdf` | Konverter alle eksempel-YAML til RDF/Turtle, repo-vidt (ikkje domenegata). Frittståande, brukarvendt kommando — brukar same batch-mekanisme som `gen-linkml-convert` over. | `generated/<domain>/<modell>/<modell>-eksempel.ttl` | Batcha — `batch-generate-instances.py --generator convert --jobs-tsv <fil>`, éin kontainar for alle filer (TSV bygd via `convert-examples.sh`) |
| <a id="convert-data"></a>`make convert-data` | Konverter produksjonsdatafiler i `data/`-underkatalogar til RDF/Turtle (berre `publish_external: true`) | `generated/<domain>/<katalog>/<katalog>.ttl` | Batcha — same mekanisme som `convert-rdf` (TSV bygd via `convert-data.sh`) |
| <a id="clean"></a>`make clean` | Slett `generated/` | — | Ikkje aktuelt |

Nye skjema under `src/linkml/<domain>/<modell>/` vert oppdaga automatisk — ingen Makefile-endringar nødvendig.

### Vedlikehald

| Kommando | Beskriving | Output | Batching |
|---|---|---|---|
| <a id="gen-informasjonsmodell-instance"></a>`make gen-informasjonsmodell-instance SCHEMA=<sti>` | Genererer ModelDCAT-metadata-fil (`metadata/modelldcat.yaml`) for eit enkelt skjema. Samlar data frå 6 kjelder: schema.yaml (toppnivå + annotations), build.yaml, CODEOWNERS.md, lokale klasser, genererte artefakter, er_profil_av. Genererer inline Kontaktopplysning og Standard-instansar. | `src/linkml/<domain>/<modell>/metadata/modelldcat.yaml` | Batcha — `batch-generate-instances.py --generator informasjonsmodell`, reint Python, éin kontainar (gevinsten realiserast fullt ut når kalla for fleire skjema, t.d. via `domain-*`/`DOMAIN=`) |
| <a id="validate-informasjonsmodell-instance"></a>`make validate-informasjonsmodell-instance SCHEMA=<sti>` | Validerer generert ModelDCAT-metadata mot modelldcat-katalog-schema.yaml med full LinkML-validering. Sjekkar YAML-struktur, obligatoriske felt, LangString-format og inline-instansar. Køyrer i LinkML-container for korrekt schema-oppløysing. **Convenience-target** (ikkje eit `$(MAKE)`-kall til `validate-instance` — sjå [§ Wrapper-target](#wrapper-target)): gjenbruker same underliggande valideringslogikk, men via eige script som auto-detekterer `metadata/modelldcat.yaml` og schema-sti. | Pass/fail til stdout; avsluttar med kode 1 ved feil | Ikkje batcha — eitt skjema om gongen |
| <a id="gen-begrepskatalog-instance"></a>`make gen-begrepskatalog-instance` | Samlar alle begrep frå begrepssamlingar og genererer begrepskatalog per organisasjon. Finn alle begrepssamlingar med `aggregation.organization`-metadata, samle begrep-YAML-filer frå `begrep/*.yaml`, og generer aggregert begrepskatalog under `begrepskatalog/<org>-begrepskatalog/data/`. Køyrast automatisk av CI før generatorfasen. | `src/linkml/begrepskatalog/<org>-begrepskatalog/data/<org>-begrepskatalog/<org>-begrepskatalog.yaml` | Ikkje aktuelt — eitt samla script over alle begrepssamlingar, ikkje eit per-skjema-kontainarmønster |
| <a id="gen-modellkatalog-instance"></a>`make gen-modellkatalog-instance` | Genererer per-org modellkatalogar frå alle `metadata/modelldcat.yaml`-filer. Grupper Informasjonsmodell-instansar etter utgiver (frå CODEOWNERS.md) og genererer éi katalogfil per organisasjon for publisering til Felles datakatalog. Konverterer standard URI-ar (`https://data.norge.no/...`) til org-spesifikke URI-ar (`https://<org-domene>/modellkatalogar/<catalog_slug>/...`). **Erstatter:** `make update-modellkatalog` (deprecated). | `src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml` | Ikkje aktuelt — same grunn |
| <a id="validate-modellkatalog-instance"></a>`make validate-modellkatalog-instance ORG=<org-slug>` | Validerer generert modellkatalog-datafil mot org-spesifikt schema. Eksempel: `ORG=digdir-modellkatalog`. Validerer `src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml` mot `src/linkml/modellkatalog/<org>/<org>-schema.yaml`. **Convenience-target** (ikkje eit `$(MAKE)`-kall til `validate-instance` — sjå [§ Wrapper-target](#wrapper-target)): køyrer same underliggande `linkml validate`-kommando direkte, med schema- og instans-stiar auto-konstruerte frå `ORG=`. | Pass/fail til stdout; avsluttar med kode 1 ved feil | Ikkje batcha |

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
| `make mcp-linkml-modell-utkast SCHEMA=<sti> FORMAT=json-schema PROFILE=default` | Same som over med eksplisitt format og profil. | `<same katalog>/<modell>-schema.yaml` |
| `make mcp-linkml-modell-utkast-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## LinkML-begrep utkast (mcp-linkml-begrep-utkast)

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-mcp-begrep-utkast` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-begrep-utkast:latest` |
| `make mcp-linkml-begrep-utkast-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-begrep-utkast-list-profiles` | Listar alle tilgjengelege organisasjonsprofiler som kan brukast ved oppretting av begrep. | JSON-liste over profil-ID-ar til stdout |
| `make mcp-linkml-begrep-utkast INPUT=<sti>` | Genererer eit YAML-utkast til begrep frå ei JSON-fil med argument til `opprett_begrep`. | YAML-blokker til stdout |
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
og IRI-ar som ikkje resolverer. Feilar aldri (ikkje ein valideringspolicy);
brukt av den vekentlege `.github/workflows/modell-analyse.yml`. Namne-
samanlikninga brukar berre klasser/slots definerte lokalt i kvart skjema
(ikkje namn arva via `imports`), og fuzzy string-likskap
(`difflib.SequenceMatcher`) — juster terskel med `SIMILARITY_THRESHOLD`.

| Kommando | Beskriving | Output |
|---|---|---|
| `make analyse-similar-classes-domain [SIMILARITY_THRESHOLD=0.8]` | Finn klasser med liknande namn innanfor same domene. | Markdown-tabell til stdout |
| `make analyse-similar-classes-all [SIMILARITY_THRESHOLD=0.8]` | Finn klasser med liknande namn på tvers av alle domene. | Markdown-tabell til stdout |
| `make analyse-similar-slots-domain [SIMILARITY_THRESHOLD=0.8]` | Finn slots med liknande namn innanfor same domene. | Markdown-tabell til stdout |
| `make analyse-similar-slots-all [SIMILARITY_THRESHOLD=0.8]` | Finn slots med liknande namn på tvers av alle domene. | Markdown-tabell til stdout |
| `make analyse-iri-resolution` | Testar HTTP-resolusjon for `id`/`default_prefix`/`prefixes`-IRI-ar i alle skjema, og innhaldsforhandling (`Accept: text/turtle`, `Accept-Language: nb`/`en`) for IRI-ar repoet sjølv eig (`id`/`default_prefix`). Krev nettverkstilgang. | Markdown-tabellar til stdout |

## Påskeegg: Gource-visualisering

Krev `make build-docker-gource` éin gong (eller etter endringar i Dockerfile). Output-filer hamnar i `tmp/`.

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-gource` | Byggjer container-image med Gource og ffmpeg. | Image `localhost/gource-local:latest` |
| `make gource-preview` | Genererer ein 30fps-preview-video av heile git-historikken (rask, lågare kvalitet). | `tmp/gource-preview.mp4` |
| `make gource-video` | Genererer ein 60fps fullkvalitetsvideo av heile git-historikken. | `tmp/gource.mp4` |

