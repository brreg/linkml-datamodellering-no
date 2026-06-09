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
| `make linkml-build-docker` | Byggjer container-image for artefaktgenerering og validering. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/linkml-local:latest` |
| `make docs-build-docker` | Byggjer container-image for dokumentasjonsportalen. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/mkdocs-local:latest` |
| `make python-build-docker` | Byggjer container-image for Python-testar. Berre nødvendig ved første bruk eller etter endringar i Dockerfile. | Image `localhost/python-pytest:latest` |
| `make mcp-mod-build` | Byggjer container-image for modell-utkast MCP-server. | Image `localhost/mcp-linkml-modell-utkast:latest` |
| `make mcp-begrep-build` | Byggjer container-image for begrepsinstans-generator MCP-server. | Image `localhost/mcp-linkml-begrep-utkast:latest` |
| `make mcp-val-build` | Byggjer container-image for validator MCP-server. | Image `localhost/mcp-linkml-validator:latest` |

## Ny modell

| Kommando | Beskriving | Output |
|---|---|---|
| `make new-model NAME=<modell> DOMAIN=<domain>` | Opprettar katalogstruktur og boilerplate for ein ny LinkML-modell. Skjemaet passerer `POLICY=bronze` utan manuell redigering. | `src/linkml/<domain>/<modell>/<modell>-schema.yaml`<br>`src/linkml/<domain>/<modell>/examples/<modell>-eksempel.yaml` |

Skjemaet passerer `POLICY=bronze` utan manuell redigering.

## Validering

| Kommando | Beskriving | Output |
|---|---|---|
| `make lint` | Linter alle skjema i repoet. | OK/FEIL per skjema til stdout; avsluttar med kode 1 ved feil |
| `make lint SCHEMA=<sti>` | Linter eit enkelt skjema raskt utan å køyre generatorar. Nyttig for hurtigsjekk under utvikling. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `make validate-instance SCHEMA=<sti> INSTANCE=<sti>` | Validerer ei datafil mot eit skjema utan lint og generatorar. Raskaste enkeltsjekk av datainnhald. | OK/FEIL til stdout; avsluttar med kode 1 ved feil |
| `make test SCHEMA=<sti>` | Køyrer full testsuite (lint + validering + alle generatorar) for eitt skjema. | Samla testrapport til stdout; avsluttar med kode 1 ved feil |
| `make test` | Linter alle skjema og validerer alle eksempelfiler i heile repoet. | Samla testrapport til stdout; avsluttar med kode 1 ved feil |
| `make validate` | Validerer alle skjema mot LinkML-metaskjemaet (strukturvalidering, ikkje policy). | Validerings-resultat per skjema til stdout |
| `make mcp-validate SCHEMA=<sti> POLICY=bronze` | Policy-validering på bronze-nivå: obligatoriske metadata, identifikatorar og begrepsreferansar. | Pass/fail per policy-regel til stdout |
| `make mcp-validate SCHEMA=<sti> POLICY=silver` | Policy-validering på silver-nivå: bronze + krav om import av DCAT-AP-NO og DQV-AP-NO. | Pass/fail per policy-regel til stdout |
| `make mcp-validate SCHEMA=<sti> POLICY=gold` | Policy-validering på gold-nivå: silver + FAIR-sjekkar F1–R1.3 (class_uri, lisens, proveniens m.m.). | Pass/fail per policy-regel til stdout |

### Validerings-Policyar

| Policy | Beskriving |
|---|---|
| `bronze` | Obligatoriske metadata (`id`, `name`), anbefalt `description`, alle klasser har identifikator og begrepsreferanse |
| `silver` | Bronze + skjemaet importerer DCAT-AP-NO og DQV-AP-NO |
| `gold` | Silver + FAIR-sjekkar F1–R1.3 (class_uri, lisens, proveniens m.m.) |

`mcp-validate` flattar automatisk ut relative importar med `gen-linkml --mergeimports` før validering, slik at domenemodeller med fleire schema-lag fungerer utan tilpassing.

## Generering av artefakter

### Per domene (anbefalt)

| Kommando | Beskriving | Output |
|---|---|---|
| `make ap-no` | Valider + generer alle artefakter for alle AP-NO-profiler | `generated/ap-no/` |
| `make begrepskatalog` | Valider + generer alle artefakter for begrepskatalogmodellane | `generated/begrepskatalog/` |
| `make fair` | Valider + generer alle artefakter for FAIR-metadata | `generated/fair/` |
| `make fint` | Valider + generer alle artefakter for FINT-modellane | `generated/fint/` |
| `make modellkatalog` | Valider + generer alle artefakter for modellkatalogmodellane | `generated/modellkatalog/` |
| `make ngr` | Valider + generer alle artefakter for NGR-modellane | `generated/ngr/` |
| `make oreg` | Valider + generer alle artefakter for OREG-registera | `generated/oreg/` |
| `make samt` | Valider + generer alle artefakter for SAMT-modellane | `generated/samt/` |

### Enkeltartefakter (alle skjema)

| Kommando | Beskriving | Output |
|---|---|---|
| `make gen-jsonld` | JSON-LD kontekst | `generated/<domain>/<modell>/<modell>-context.jsonld` |
| `make gen-shacl` | SHACL shapes | `generated/<domain>/<modell>/<modell>-shapes.ttl` |
| `make gen-python` | Python-dataklassar | `generated/<domain>/<modell>/<modell>-model.py` |
| `make gen-jsonschema` | JSON Schema | `generated/<domain>/<modell>/<modell>-schema.json` |
| `make gen-owl` | OWL/Turtle-ontologi | `generated/<domain>/<modell>/<modell>-ontology.ttl` |
| `make gen-rdf` | RDF/Turtle-graf av skjemaet | `generated/<domain>/<modell>/<modell>-schema.ttl` |
| `make gen-erdiagram` | Mermaid ER-diagram | `generated/<domain>/<modell>/<modell>-erdiagram.md` |
| `make gen-docs` | HTML-klassereferanse | `generated/<domain>/<modell>/docs/` |
| `make convert-rdf` | Konverter alle eksempel-YAML til RDF/Turtle | `generated/<domain>/<modell>/<modell>-eksempel.ttl` |
| `make clean` | Slett `generated/` | — |

Nye skjema under `src/linkml/<domain>/<modell>/` vert oppdaga automatisk — ingen Makefile-endringar nødvendig.

## Dokumentasjonsportal

| Kommando | Beskriving | Output |
|---|---|---|
| `make publish` | Kopier `generated/` → `mkdocs/docs/` og regenerer `mkdocs.yml` | `mkdocs/docs/` |
| `make docs-serve` | Start lokal dev-server med live reload. Leser `mkdocs/docs/` | `http://localhost:8000` |
| `make docs-build` | Bygg statisk HTML-site (CI-pipeline for produksjon) | `mkdocs/site/` |
| `make docs-build-fast` | Same som `docs-build`, men hoppar over uendra sider | `mkdocs/site/` |

`make publish` køyrer `mkdocs/publish.sh` som kopier artefakter og dokumentasjon frå `generated/` til `mkdocs/docs/`, genererer `index.md` per skjema og domene, og oppdaterer navigasjonsstrukturen i `mkdocs.yml`. Nye domene og skjema dukkar opp automatisk neste gong `publish` vert køyrt.

## mcp-linkml-modell-utkast

| Kommando | Beskriving | Output |
|---|---|---|
| `make mcp-mod-build` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-modell-utkast:latest` |
| `make mcp-mod-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-mod-test` | Køyrer alle unit-testar for MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-generate SCHEMA=<sti>` | Genererer eit LinkML-skjemautkast frå ei JSON Schema-fil ved hjelp av MCP-serveren. | `<same katalog>/<modell>-schema.yaml` |
| `make mcp-generate SCHEMA=<sti> FORMAT=json-schema PROFILE=default` | Same som over med eksplisitt format og profil. | `<same katalog>/<modell>-schema.yaml` |
| `make mcp-mod-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## mcp-linkml-begrep-utkast

| Kommando | Beskriving | Output |
|---|---|---|
| `make mcp-begrep-build` | Byggjer container-image for MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-begrep-utkast:latest` |
| `make mcp-begrep-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-begrep-list-profiles` | Listar alle tilgjengelege organisasjonsprofiler som kan brukast ved oppretting av begrep. | JSON-liste over profil-ID-ar til stdout |
| `make mcp-begrep-run` | Startar MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |

## LinkML-validator mcp-server (mcp-linkml-validator)

| Kommando | Beskriving | Output |
|---|---|---|
| `make mcp-val-build` | Byggjer container-image for validator MCP-serveren (eingongsoperasjon). | Image `localhost/mcp-linkml-validator:latest` |
| `make mcp-val-smoke` | Køyrer røyktest med eksempel-meldingar for å verifisere at serveren svarar korrekt. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-val-test` | Køyrer alle policy-testar for validator MCP-serveren. | Testresultat til stdout; avsluttar med kode 1 ved feil |
| `make mcp-val-run` | Startar validator MCP-serveren interaktivt. Nyttig for manuell testing og feilsøking. | JSON-RPC på stdin/stdout |


