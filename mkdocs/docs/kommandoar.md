# Kommandoar

Alle kommandoar køyrer via containerar — ingen lokal Python-installasjon trengst.

## Oppsett og føresetnadar

| Kommando | Beskriving | Output |
|---|---|---|
| `make check-prereqs` | Sjekkar at Podman, GNU make, user namespace og ledig diskplass er korrekt konfigurert | Skriv OK/FEIL per føresetnad til stdout; avsluttar med kode 1 ved feil |

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
| `make new-model NAME=<modell> DOMAIN=<domain>` | Opprettar katalogstruktur og boilerplate for ein ny LinkML-domenemodell.  | `src/linkml/<domain>/<modell>/<modell>-schema.yaml`<br>`src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml` |
| `make new-modellkatalog NAME=<alias>` | Opprettar katalogstruktur og boilerplate for ein ny organisasjonskatalog (modellkatalog + datakatalog). `<alias>` må vere registrert i `CODEOWNERS.md`-frontmatter med `catalog_slug`. | `src/linkml/modellkatalog/<catalog_slug>/` |
| `make new-begrepskatalog NAME=<katalognavn>` | Opprettar katalogstruktur og boilerplate for ein ny begrepskatalog. | `src/linkml/begrepskatalog/<katalognavn>/` |

## Validering

| Kommando | Beskriving | Output |
|---|---|---|
| `make lint` | Linter alle skjema i repoet. | OK/FEIL per skjema til stdout; avsluttar med kode 1 ved feil |
| `make lint SCHEMA=<sti>` | Linter eit enkelt skjema raskt utan å køyre generatorar. Nyttig for hurtigsjekk under utvikling. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `make validate-instance SCHEMA=<sti> INSTANCE=<sti>` | Validerer ei datafil mot eit skjema utan lint og generatorar. Raskaste enkeltsjekk av datainnhald. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `make roundtrip SCHEMA=<sti>` | Køyrer berre roundtrip-testane (JSON og TTL) for eitt skjema. Raskare enn full testsuite — nyttig etter skjema-endringar som kan påverke serialisering. | Testrapport for `roundtrip-json` og `roundtrip-ttl` til stdout; avsluttar med kode 1 ved feil |
| `make roundtrip` | Køyrer roundtrip-testar for alle skjema i repoet. | Testrapport til stdout; avsluttar med kode 1 ved feil |
| `make roundtrip-json-schema SCHEMA=<sti>` | Køyrer roundtrip-test spesifikt for JSON Schema-generering. Verifiserer at YAML → JSON Schema → YAML gjev same resultat. | Testrapport til stdout; avsluttar med kode 1 ved feil |
| `make test SCHEMA=<sti>` | Køyrer full testsuite (lint + validering + alle generatorar) for eitt skjema. | Samla testrapport til stdout; avsluttar med kode 1 ved feil |
| `make test` | Linter alle skjema og validerer alle eksempelfiler i heile repoet. | Samla testrapport til stdout; avsluttar med kode 1 ved feil |
| `make validate` | Validerer alle skjema mot LinkML-metaskjemaet (strukturvalidering, ikkje policy). | Validerings-resultat per skjema til stdout |
| `make mcp-linkml-validate SCHEMA=<sti>` | Policy-validering mot `validation_policy` frå manifest.yaml. POLICY kan overstyres med `POLICY=<bronze\|silver\|gold\|felles-datakatalog\|felles-begrepskatalog>`. | Pass/fail per policy-regel til stdout |
| `make validate-capture` | Generer valideringsresultat for alle skjema og lagre til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`. | JSON-filer med valideringsresultat |
| `make validate-capture SCHEMA=<sti>` | Generer valideringsresultat for eitt skjema og lagre til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`. | JSON-fil med valideringsresultat |
| `make validate-bronze DOMAIN=<domain>` | Validerer alle skjema i eit domene mot bronze-policy (basis skjemakvalitet). Brukt i CI per domene. | Pass/fail per skjema til stdout; avsluttar med kode 1 ved feil |
| `make validate-data DOMAIN=<domain>` | Validerer alle datafiler i `data/`-katalogar i eit domene mot deira `validation_policy` frå manifest.yaml. Brukt i CI per domene. | Pass/fail per datafil til stdout |
| `make validate-examples DOMAIN=<domain>` | Validerer alle eksempelfiler i eit domene mot tilhøyrande skjema. Brukt i CI per domene. | Pass/fail per eksempelfil til stdout; avsluttar med kode 1 ved feil |
| `make log-mcp-validate SCHEMA=<sti>` | Policy-validering med full JSON-logg. Nyttig for debugging av policy-reglar. | JSON-logg til stdout |
| `make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>` | Instansvalidering med full JSON-logg. Nyttig for debugging av valideringsfeil. | JSON-logg til stdout |

### Validerings-Policyar

| Policy | Beskriving |
|---|---|
| `bronze` | Obligatoriske metadata (`id`, `name`), anbefalt `description`, alle klasser har identifikator og begrepsreferanse |
| `silver` | Bronze + skjemaet importerer DCAT-AP-NO og DQV-AP-NO |
| `gold` | Silver + FAIR-sjekkar F1-R1.3 (class_uri, lisens, proveniens m.m.) |

`mcp-validate` flattar automatisk ut relative importar med LinkML sitt `gen-linkml --mergeimports` før validering, slik at domenemodeller med fleire schema-lag fungerer utan tilpassing.

### Publiserings-Policyar

Brukt for skjema der `publish_external: true` i `manifest.yaml`. Sjekkar at skjemaet
er i samsvar med krava til ei bestemt ekstern katalog. Arvær `bronze`-laget.

| Policy | Beskriving |
|---|---|
| `felles-datakatalog` | Bronze + import av ModelDCAT-AP-NO, containerklasse med `Modellkatalog` og `Informasjonsmodell`, obligatoriske felt for desse klassane (tittel, beskrivelse, identifikator, utgjevar, kontaktpunkt) |
| `felles-begrepskatalog` | Bronze + import av SKOS-AP-NO-Begrep, containerklasse med `Begrep`, obligatoriske felt for `Begrep` (anbefalt term, definisjon, identifikator, utgjevar, kontaktpunkt) og `Samling` |

## Generering av artefakter

### Per domene (anbefalt)

Kvar `domain-*` target køyrer følgjande steg for alle skjema i domenet:
1. **Validering**: `merge-imports` mergar imports og validerer skjemaet (output vert kasta)
2. **Artefaktgenerering** (parallelt): JSON-LD context, SHACL, Python, JSON Schema, OWL, RDF, PlantUML, docs
3. **Eksempelkonvertering**: Konverterer `*-eksempel.yaml` til RDF/Turtle (dersom `example_rdf: true`)
4. **Modellmanifest** (parallelt): Genererer Informasjonsmodell-instans ihht ModelDCAT-AP-NO til `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`

**Parallellisering**: Alle `domain-*` targets støttar `PARALLEL` parameter (default: 8 jobbar).
- `make domain-ap-no` — køyrer med 8 parallelle jobbar (default)
- `make domain-ap-no PARALLEL=16` — køyrer med 16 parallelle jobbar
- `make domain-ap-no PARALLEL=1` — køyrer sekvensielt (debugging)

Parallell køyring viser timer per jobb: `→ gen-jsonld-context ap-no/dcat-ap-no (5.1s)`

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

| Kommando | Beskriving | Output |
|---|---|---|
| <a id="gen-jsonld-context"></a>`make gen-jsonld-context [DOMAIN=...] [SCHEMA=...]` | JSON-LD kontekst | `generated/<domain>/<modell>/<modell>-context.jsonld` |
| <a id="gen-shacl"></a>`make gen-shacl [DOMAIN=...] [SCHEMA=...]` | SHACL shapes | `generated/<domain>/<modell>/<modell>-shapes.ttl` |
| <a id="gen-python"></a>`make gen-python [DOMAIN=...] [SCHEMA=...]` | Python-dataklassar | `generated/<domain>/<modell>/<modell>-model.py` |
| <a id="gen-jsonschema"></a>`make gen-jsonschema [DOMAIN=...] [SCHEMA=...]` | JSON Schema | `generated/<domain>/<modell>/<modell>-schema.json` |
| <a id="gen-owl"></a>`make gen-owl [DOMAIN=...] [SCHEMA=...]` | OWL/Turtle-ontologi | `generated/<domain>/<modell>/<modell>-ontology.ttl` |
| <a id="gen-rdf"></a>`make gen-rdf [DOMAIN=...] [SCHEMA=...]` | RDF/Turtle-graf av skjemaet | `generated/<domain>/<modell>/<modell>-schema.ttl` |
| <a id="gen-erdiagram"></a>`make gen-erdiagram [DOMAIN=...] [SCHEMA=...]` | Mermaid ER-diagram | `generated/<domain>/<modell>/<modell>-erdiagram.md` |
| <a id="gen-docs"></a>`make gen-docs [DOMAIN=...] [SCHEMA=...]` | HTML-klassereferanse og Mermaid ER-diagram | `generated/<domain>/<modell>/docs/` |
| <a id="gen-proto"></a>`make gen-proto [DOMAIN=...] [SCHEMA=...]` | Protocol Buffers-skjema | `generated/<domain>/<modell>/<modell>-schema.proto` |
| <a id="gen-plantuml"></a>`make gen-plantuml [DOMAIN=...] [SCHEMA=...]` | PlantUML-diagram og SVG | `generated/<domain>/<modell>/diagrams/<modell>.svg` |
| <a id="gen-xsd"></a>`make gen-xsd [DOMAIN=...] [SCHEMA=...]` | XSD-skjema via Avrotize (berre skjema med `xsd: true` i manifest) | `generated/<domain>/<modell>/<modell>-schema.xsd` |
| <a id="gen-asyncapi"></a>`make gen-asyncapi [DOMAIN=...] [SCHEMA=...]` | AsyncAPI 3.0-spec (berre skjema med `asyncapi: true` i manifest) | `generated/<domain>/<modell>/<modell>-asyncapi.yaml` |
| <a id="gen-openapi"></a>`make gen-openapi [DOMAIN=...] [SCHEMA=...]` | OpenAPI 3.1-spec (berre skjema med `openapi: true` i manifest) | `generated/<domain>/<modell>/<modell>-openapi.yaml` |
| <a id="gen-config"></a>`make gen-config [DOMAIN=...] [SCHEMA=...]` | Generatorkonfigurasjon frå manifest.yaml | `generated/<domain>/<modell>/config.yaml` |
| <a id="gen-dqv-measurements"></a>`make gen-dqv-measurements [DOMAIN=...] [SCHEMA=...]` | DQV-kvalitetsmålingar for datakatalogdata | `generated/<domain>/<modell>/dqv-measurements.ttl` |
| <a id="gen-modelldcat-elements"></a>`make gen-modelldcat-elements [DOMAIN=...] [SCHEMA=...]` | ModelDCAT-element for modellkatalogdata | `generated/<domain>/<modell>/modelldcat-elements.ttl` |
| <a id="convert-rdf"></a>`make convert-rdf` | Konverter alle eksempel-YAML til RDF/Turtle | `generated/<domain>/<modell>/<modell>-eksempel.ttl` |
| <a id="convert-data"></a>`make convert-data` | Konverter produksjonsdatafiler i `data/`-underkatalogar til RDF/Turtle (berre `publish_external: true`) | `generated/<domain>/<katalog>/<katalog>.ttl` |
| <a id="clean"></a>`make clean` | Slett `generated/` | — |

Nye skjema under `src/linkml/<domain>/<modell>/` vert oppdaga automatisk — ingen Makefile-endringar nødvendig.

### Vedlikehald

| Kommando | Beskriving | Output |
|---|---|---|
| <a id="gen-informasjonsmodell-instance"></a>`make gen-informasjonsmodell-instance SCHEMA=<sti>` | Genererer ModelDCAT-metadata-fil (`metadata/modelldcat.yaml`) for eit enkelt skjema. Samlar data frå 6 kjelder: schema.yaml (toppnivå + annotations), build.yaml, CODEOWNERS.md, lokale klasser, genererte artefaktar, er_profil_av. Genererer inline Kontaktopplysning og Standard-instansar. | `src/linkml/<domain>/<modell>/metadata/modelldcat.yaml` |
| <a id="validate-informasjonsmodell-instance"></a>`make validate-informasjonsmodell-instance SCHEMA=<sti>` | Validerer generert ModelDCAT-metadata mot modelldcat-katalog-schema.yaml med full LinkML-validering. Sjekkar YAML-struktur, obligatoriske felt, LangString-format og inline-instansar. Køyrer i LinkML-container for korrekt schema-oppløysing. **Convenience wrapper** for `make validate-instance` som auto-detekterer `metadata/modelldcat.yaml` og schema-sti. | Pass/fail til stdout; avsluttar med kode 1 ved feil |
| <a id="gen-modellkatalog-instance"></a>`make gen-modellkatalog-instance` | Genererer per-org modellkatalogar frå alle `metadata/modelldcat.yaml`-filer. Grupper Informasjonsmodell-instansar etter utgiver (frå CODEOWNERS.md) og genererer éi katalogfil per organisasjon for publisering til Felles datakatalog. Konverterer standard URI-ar (`https://data.norge.no/...`) til org-spesifikke URI-ar (`https://<org-domene>/modellkatalogar/<catalog_slug>/...`). **Erstatter:** `make update-modellkatalog` (deprecated). | `src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml` |
| <a id="validate-modellkatalog-instance"></a>`make validate-modellkatalog-instance ORG=<org-slug>` | Validerer generert modellkatalog-datafil mot org-spesifikt schema. Eksempel: `ORG=digdir-modellkatalog`. Validerer `src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml` mot `src/linkml/modellkatalog/<org>/<org>-schema.yaml`. **Convenience wrapper** for `make validate-instance` som auto-konstruerer schema- og instans-stiar. | Pass/fail til stdout; avsluttar med kode 1 ved feil |

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
| `make mcp-linkml-validate-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-validate-test` | Køyrer alle policy-testar for validator MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-validate-run` | Startar validator MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## Påskeegg: Gource-visualisering

Krev `make build-docker-gource` éin gong (eller etter endringar i Dockerfile). Output-filer hamnar i `tmp/`.

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-gource` | Byggjer container-image med Gource og ffmpeg. | Image `localhost/gource-local:latest` |
| `make gource-preview` | Genererer ein 30fps-preview-video av heile git-historikken (rask, lågare kvalitet). | `tmp/gource-preview.mp4` |
| `make gource-video` | Genererer ein 60fps fullkvalitetsvideo av heile git-historikken. | `tmp/gource.mp4` |

