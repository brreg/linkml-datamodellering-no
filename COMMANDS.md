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

## Ny modell/begrepskatalog/modellkatalog

| Kommando | Beskriving | Output |
|---|---|---|
| `make new-model NAME=<modell> DOMAIN=<domain>` | Opprettar katalogstruktur og boilerplate for ein ny LinkML-domenemodell.  | `src/linkml/<domain>/<modell>/<modell>-schema.yaml`<br>`src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml` |
| `make new-org-catalog ORG=<alias>` | Opprettar katalogstruktur og boilerplate for ein ny organisasjonskatalog (modellkatalog + datakatalog). `<alias>` må vere registrert i `CODEOWNERS.md`-frontmatter med `catalog_slug`. | `src/linkml/modellkatalog/<catalog_slug>/` |
| `make new-begrepskatalog NAME=<katalognavn>` | Opprettar katalogstruktur og boilerplate for ein ny begrepskatalog. | `src/linkml/begrepskatalog/<katalognavn>/` |

## Validering

| Kommando | Beskriving | Output |
|---|---|---|
| `make lint` | Linter alle skjema i repoet. | OK/FEIL per skjema til stdout; avsluttar med kode 1 ved feil |
| `make lint SCHEMA=<sti>` | Linter eit enkelt skjema raskt utan å køyre generatorar. Nyttig for hurtigsjekk under utvikling. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `make validate-instance SCHEMA=<sti> INSTANCE=<sti>` | Validerer ei datafil mot eit skjema utan lint og generatorar. Raskaste enkeltsjekk av datainnhald. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `make roundtrip SCHEMA=<sti>` | Køyrer berre roundtrip-testane (JSON og TTL) for eitt skjema. Raskare enn full testsuite — nyttig etter skjema-endringar som kan påverke serialisering. | Testrapport for `roundtrip-json` og `roundtrip-ttl` til stdout; avsluttar med kode 1 ved feil |
| `make roundtrip` | Køyrer roundtrip-testar for alle skjema i repoet. | Testrapport til stdout; avsluttar med kode 1 ved feil |
| `make test SCHEMA=<sti>` | Køyrer full testsuite (lint + validering + alle generatorar) for eitt skjema. | Samla testrapport til stdout; avsluttar med kode 1 ved feil |
| `make test` | Linter alle skjema og validerer alle eksempelfiler i heile repoet. | Samla testrapport til stdout; avsluttar med kode 1 ved feil |
| `make validate` | Validerer alle skjema mot LinkML-metaskjemaet (strukturvalidering, ikkje policy). | Validerings-resultat per skjema til stdout |
| `make mcp-validate SCHEMA=<sti>` | Policy-validering mot `validation_policy` frå manifest.yaml. POLICY kan overstyres med `POLICY=<bronze\|silver\|gold\|felles-datakatalog\|felles-begrepskatalog>`. | Pass/fail per policy-regel til stdout |
| `make validate-capture` | Generer valideringsresultat for alle skjema og lagre til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`. | JSON-filer med valideringsresultat |
| `make validate-capture SCHEMA=<sti>` | Generer valideringsresultat for eitt skjema og lagre til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`. | JSON-fil med valideringsresultat |
| `make validate-bronze DOMAIN=<domain>` | Validerer alle skjema i eit domene mot bronze-policy (basis skjemakvalitet). Brukt i CI per domene. | Pass/fail per skjema til stdout; avsluttar med kode 1 ved feil |
| `make validate-data DOMAIN=<domain>` | Validerer alle datafiler i `data/`-katalogar i eit domene mot deira `validation_policy` frå manifest.yaml. Brukt i CI per domene. | Pass/fail per datafil til stdout |
| `make validate-examples DOMAIN=<domain>` | Validerer alle eksempelfiler i eit domene mot tilhøyrande skjema. Brukt i CI per domene. | Pass/fail per eksempelfil til stdout; avsluttar med kode 1 ved feil |
| `make check-published-uris` | Verifiserer at alle URI-ar i `published-uris.lock`-filer finst i tilhøyrande datafil. Køyr etter endringar i datafiler med `publish_external: true`. | OK/FEIL til stdout; avsluttar med kode 1 ved manglande URI |

### Validerings-Policyar

| Policy | Beskriving |
|---|---|
| `bronze` | Obligatoriske metadata (`id`, `name`), anbefalt `description`, alle klasser har identifikator og begrepsreferanse |
| `silver` | Bronze + skjemaet importerer DCAT-AP-NO og DQV-AP-NO |
| `gold` | Silver + FAIR-sjekkar F1-R1.3 (class_uri, lisens, proveniens m.m.) |

`mcp-validate` flattar automatisk ut relative importar med `gen-linkml --mergeimports` før validering, slik at domenemodeller med fleire schema-lag fungerer utan tilpassing.

### Publiserings-Policyar

Brukt for skjema der `publish_external: true` i `manifest.yaml`. Sjekkar at skjemaet
er i samsvar med krava til ei bestemt ekstern katalog. Arvær `bronze`-laget.

| Policy | Beskriving |
|---|---|
| `felles-datakatalog` | Bronze + import av ModelDCAT-AP-NO, containerklasse med `Modellkatalog` og `Informasjonsmodell`, obligatoriske felt for desse klassane (tittel, beskrivelse, identifikator, utgjevar, kontaktpunkt) |
| `felles-begrepskatalog` | Bronze + import av SKOS-AP-NO-Begrep, containerklasse med `Begrep`, obligatoriske felt for `Begrep` (anbefalt term, definisjon, identifikator, utgjevar, kontaktpunkt) og `Samling` |

## Generering av artefakter

### Per domene (anbefalt)

| Kommando | Beskriving | Output |
|---|---|---|
| `make domain-ap-no` | Valider + generer alle artefakter for alle AP-NO-profiler | `generated/ap-no/` |
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
| `make gen-jsonld [DOMAIN=...] [SCHEMA=...]` | JSON-LD kontekst | `generated/<domain>/<modell>/<modell>-context.jsonld` |
| `make gen-shacl [DOMAIN=...] [SCHEMA=...]` | SHACL shapes | `generated/<domain>/<modell>/<modell>-shapes.ttl` |
| `make gen-python [DOMAIN=...] [SCHEMA=...]` | Python-dataklassar | `generated/<domain>/<modell>/<modell>-model.py` |
| `make gen-jsonschema [DOMAIN=...] [SCHEMA=...]` | JSON Schema | `generated/<domain>/<modell>/<modell>-schema.json` |
| `make gen-owl [DOMAIN=...] [SCHEMA=...]` | OWL/Turtle-ontologi | `generated/<domain>/<modell>/<modell>-ontology.ttl` |
| `make gen-rdf [DOMAIN=...] [SCHEMA=...]` | RDF/Turtle-graf av skjemaet | `generated/<domain>/<modell>/<modell>-schema.ttl` |
| `make gen-erdiagram [DOMAIN=...] [SCHEMA=...]` | Mermaid ER-diagram | `generated/<domain>/<modell>/<modell>-erdiagram.md` |
| `make gen-docs [DOMAIN=...] [SCHEMA=...]` | HTML-klassereferanse og Mermaid ER-diagram | `generated/<domain>/<modell>/docs/` |
| `make gen-proto [DOMAIN=...] [SCHEMA=...]` | Protocol Buffers-skjema | `generated/<domain>/<modell>/<modell>-schema.proto` |
| `make gen-plantuml [DOMAIN=...] [SCHEMA=...]` | PlantUML-diagram og SVG | `generated/<domain>/<modell>/diagrams/<modell>.svg` |
| `make gen-xsd [DOMAIN=...] [SCHEMA=...]` | XSD-skjema via Avrotize (berre skjema med `xsd: true` i manifest) | `generated/<domain>/<modell>/<modell>-schema.xsd` |
| `make gen-asyncapi [DOMAIN=...] [SCHEMA=...]` | AsyncAPI 3.0-spec (berre skjema med `asyncapi: true` i manifest) | `generated/<domain>/<modell>/<modell>-asyncapi.yaml` |
| `make gen-openapi [DOMAIN=...] [SCHEMA=...]` | OpenAPI 3.1-spec (berre skjema med `openapi: true` i manifest) | `generated/<domain>/<modell>/<modell>-openapi.yaml` |
| `make convert-rdf` | Konverter alle eksempel-YAML til RDF/Turtle | `generated/<domain>/<modell>/<modell>-eksempel.ttl` |
| `make convert-data` | Konverter produksjonsdatafiler i `data/`-underkatalogar til RDF/Turtle (berre `publish_external: true`) | `generated/<domain>/<katalog>/<katalog>.ttl` |
| `make clean` | Slett `generated/` | — |

Nye skjema under `src/linkml/<domain>/<modell>/` vert oppdaga automatisk — ingen Makefile-endringar nødvendig.

### Vedlikehald

| Kommando | Beskriving | Output |
|---|---|---|
| `make update-modellkatalog` | Oppdaterer `Informasjonsmodell`-innslag i modellkatalogen frå `annotations.*` i alle skjema. Køyr etter at eit skjema legg til eller endrar annotasjonar (`utgiver`, `endringsdato` o.a.). | `src/linkml/modellkatalog/brreg-modellkatalog/data/` |

## Dokumentasjonsportal

| Kommando | Beskriving | Output |
|---|---|---|
| `make publish` | Kopier `generated/` → `mkdocs/docs/` og regenerer `mkdocs.yml` | `mkdocs/docs/` |
| `make docs-serve` | Start lokal dev-server med live reload. Leser `mkdocs/docs/` | `http://localhost:8000` |
| `make docs-build` | Bygg statisk HTML-site (CI-pipeline for produksjon) | `mkdocs/site/` |

`make publish` køyrer `mkdocs/publish.sh` som kopier artefakter og dokumentasjon frå `generated/` til `mkdocs/docs/`, genererer `index.md` per skjema og domene, og oppdaterer navigasjonsstrukturen i `mkdocs.yml`. Nye domene og skjema dukkar opp automatisk neste gong `publish` vert køyrt.

## LinkML-modell utkast (mcp-linkml-modell-utkast)

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-mcp-modell-utkast` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-modell-utkast:latest` |
| `make mcp-modell-utkast-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-modell-utkast-test` | Køyrer alle unit-testar for MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-linkml-modell-utkast SCHEMA=<sti>` | Genererer eit LinkML-skjemautkast frå ei JSON Schema-fil ved hjelp av MCP-serveren. | `<same katalog>/<modell>-schema.yaml` |
| `make mcp-linkml-modell-utkast SCHEMA=<sti> FORMAT=json-schema PROFILE=default` | Same som over med eksplisitt format og profil. | `<same katalog>/<modell>-schema.yaml` |
| `make mcp-modell-utkast-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## LinkML-begrep utkast (mcp-linkml-begrep-utkast)

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-mcp-begrep-utkast` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-begrep-utkast:latest` |
| `make mcp-begrep-utkast-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-begrep-utkast-list-profiles` | Listar alle tilgjengelege organisasjonsprofiler som kan brukast ved oppretting av begrep. | JSON-liste over profil-ID-ar til stdout |
| `make mcp-linkml-begrep-utkast INPUT=<sti>` | Genererer eit YAML-utkast til begrep frå ei JSON-fil med argument til `opprett_begrep`. | YAML-blokker til stdout |
| `make mcp-begrep-utkast-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## LinkML-validator (mcp-linkml-validator)

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-mcp-validator` | Byggjer container-image for validator MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-validator:latest` |
| `make mcp-validator-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-validator-test` | Køyrer alle policy-testar for validator MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-validator-run` | Startar validator MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## Påskeegg: Gource-visualisering

Krev `make build-docker-gource` éin gong (eller etter endringar i Dockerfile). Output-filer hamnar i `tmp/`.

| Kommando | Beskriving | Output |
|---|---|---|
| `make build-docker-gource` | Byggjer container-image med Gource og ffmpeg. | Image `localhost/gource-local:latest` |
| `make gource-preview` | Genererer ein 30fps-preview-video av heile git-historikken (rask, lågare kvalitet). | `tmp/gource-preview.mp4` |
| `make gource-video` | Genererer ein 60fps fullkvalitetsvideo av heile git-historikken. | `tmp/gource.mp4` |

