# Kommandoar

Alle kommandoar køyrer via containerar — ingen lokal Python-installasjon trengst.

## Ny modell

| Kommando | Beskriving | Output |
|---|---|---|
| `make new-model NAME=<namn> DOMAIN=<domene>` | Opprett filstruktur og boilerplate for ny modell | `src/linkml/<domene>/<namn>/<namn>-schema.yaml`<br>`examples/<domene>/<namn>-eksempel.yaml` |

Skjemaet passerer `POLICY=bronze` utan manuell redigering.

## Validering

| Kommando | Beskriving |
|---|---|
| `./tests/lint_schema.bash <skjema>` | Linter skjema (rask enkeltsjekk) |
| `./tests/validate_schema.bash <skjema> <eksempel>` | Valider eksempelfil mot skjema (rask enkeltsjekk, utan lint og generatorar) |
| `make test SCHEMA=<sti>` | Køyr full testsuite (lint + validering + alle generatorar) for eitt skjema |
| `make mcp-validate SCHEMA=<sti> POLICY=bronze` | Policy-validering, bronze-nivå |
| `make mcp-validate SCHEMA=<sti> POLICY=silver` | Policy-validering, silver-nivå |
| `make mcp-validate SCHEMA=<sti> POLICY=gold` | Policy-validering, gold-nivå |
| `make test` | Lint alle skjema og valider alle eksempelfiler |
| `make validate` | Valider alle skjema mot LinkML-metaskjemaet |

### Policyar

| Policy | Beskriving |
|---|---|
| `bronze` | Obligatoriske metadata (`id`, `name`), anbefalt `description`, alle klasser har identifikator og begrepsreferanse |
| `silver` | Bronze + skjemaet importerer DCAT-AP-NO og DQV-AP-NO |
| `gold` | Silver + FAIR-sjekkar F1–R1.3 (class_uri, lisens, proveniens m.m.) |

`mcp-validate` flattar automatisk ut relative importar med `gen-linkml --mergeimports` før validering, slik at domenemodeller med fleire schema-lag fungerer utan tilpassing.

## Generering av artefaktar

### Per domene (anbefalt)

| Kommando | Beskriving | Output |
|---|---|---|
| `make ap-no` | Valider + generer alle artefaktar for alle AP-NO-profiler | `generated/ap-no/` |
| `make fair` | Valider + generer alle artefaktar for FAIR-metadata | `generated/fair/` |
| `make fint` | Valider + generer alle artefaktar for FINT-modellane | `generated/fint/` |
| `make ngr` | Valider + generer alle artefaktar for NGR-modellane | `generated/ngr/` |
| `make oreg` | Valider + generer alle artefaktar for OREG-registera | `generated/oreg/` |
| `make samt` | Valider + generer alle artefaktar for SAMT-modellane | `generated/samt/` |

### Enkeltartefaktar (alle skjema)

| Kommando | Beskriving | Output |
|---|---|---|
| `make gen-jsonld` | JSON-LD kontekst | `generated/<domene>/<skjema>/<skjema>-context.jsonld` |
| `make gen-shacl` | SHACL shapes | `generated/<domene>/<skjema>/<skjema>-shapes.ttl` |
| `make gen-python` | Python-dataklassar | `generated/<domene>/<skjema>/<skjema>-model.py` |
| `make gen-jsonschema` | JSON Schema | `generated/<domene>/<skjema>/<skjema>-schema.json` |
| `make gen-owl` | OWL/Turtle-ontologi | `generated/<domene>/<skjema>/<skjema>-ontology.ttl` |
| `make gen-rdf` | RDF/Turtle-graf av skjemaet | `generated/<domene>/<skjema>/<skjema>-schema.ttl` |
| `make gen-erdiagram` | Mermaid ER-diagram | `generated/<domene>/<skjema>/<skjema>-erdiagram.md` |
| `make gen-docs` | HTML-klassereferanse | `generated/<domene>/<skjema>/docs/` |
| `make convert-rdf` | Konverter alle eksempel-YAML til RDF/Turtle | `generated/<domene>/<skjema>/<skjema>-eksempel.ttl` |
| `make clean` | Slett `generated/` | — |

Nye skjema under `src/linkml/<domene>/<namn>/` vert oppdaga automatisk — ingen Makefile-endringar nødvendig.

## Dokumentasjonsportal

| Kommando | Beskriving | Output |
|---|---|---|
| `make publish` | Kopier `generated/` → `mkdocs/docs/` og regenerer `mkdocs.yml` | `mkdocs/docs/` |
| `make docs-serve` | Start lokal dev-server med live reload | `http://localhost:8000` |
| `make docs-build` | Bygg statisk HTML-site (produksjon) | `mkdocs/site/` |
| `make docs-build-fast` | Same som `docs-build`, men hoppar over uendra sider | `mkdocs/site/` |

`make publish` køyrer `mkdocs/publish.sh` som kopier artefaktar og dokumentasjon frå `generated/` til `mkdocs/docs/`, genererer `index.md` per skjema og domene, og oppdaterer navigasjonsstrukturen i `mkdocs.yml`. Nye domene og skjema dukkar opp automatisk neste gong `publish` vert køyrt.

## LinkML-generator mcp-server (mcp-linkml-generator)

| Kommando | Beskriving | Output |
|---|---|---|
| `make linkml-gen-generate SCHEMA=<sti>` | Generer LinkML-utkast frå JSON Schema-fil | `<same katalog>/<skjema>-schema.yaml` |
| `make linkml-gen-generate SCHEMA=<sti> FORMAT=json-schema PROFILE=default` | Same med eksplisitt format og profil | `<same katalog>/<skjema>-schema.yaml` |
| `make linkml-gen-build` | Bygg container-image | — |
| `make linkml-gen-smoke` | Røyktest med eksempel-meldingar | — |
| `make linkml-gen-test-converter` | Køyr alle unit-testar (44 testar) | — |
| `make linkml-gen-run` | Start server interaktivt (stdin/stdout) | — |

## LinkML-validator mcp-server (mcp-linkml-validator)

| Kommando | Beskriving |
|---|---|
| `make mcp-build` | Bygg container-image |
| `make mcp-smoke` | Røyktest med eksempel-meldingar |
| `make mcp-test-policies` | Køyr policy-testar |
| `make mcp-run` | Start server interaktivt (stdin/stdout) |

## Container-image-bygging

Berre nødvendig ved første bruk eller etter endringar i Dockerfile.

| Kommando | Image | Bruk |
|---|---|---|
| `make linkml-build-docker` | `linkml-local` | Artefaktgenerering og validering |
| `make docs-build-docker` | `mkdocs-local` | Dokumentasjonsportal |
| `make python-build-docker` | `python-pytest` | Python-testar |
| `make linkml-gen-build` | `mcp-linkml-generator` | LinkML-generator MCP-server |
| `make mcp-build` | `mcp-linkml-validator` | Validator MCP-server |

