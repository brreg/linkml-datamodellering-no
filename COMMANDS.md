# Kommandoar

Alle kommandoar køyrer via containerar — ingen lokal Python-installasjon trengst.

## Oppsett og føresetnadar

| Kommando | Beskriving |
|---|---|
| `make check-prereqs` | Sjekk at Podman, GNU make, user namespace og diskplass er korrekt konfigurert |

## Container-image-bygging

Berre nødvendig ved første bruk eller etter endringar i Dockerfile.

| Kommando | Image | Bruk |
|---|---|---|
| `make linkml-build-docker` | `linkml-local` | Artefaktgenerering og validering |
| `make docs-build-docker` | `mkdocs-local` | Dokumentasjonsportal |
| `make python-build-docker` | `python-pytest` | Python-testar |
| `make mcp-mod-build` | `mcp-linkml-modell-utkast` | Modell-utkast MCP-server |
| `make mcp-val-build` | `mcp-linkml-validator` | Validator MCP-server |

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
| `make fair` | Valider + generer alle artefakter for FAIR-metadata | `generated/fair/` |
| `make fint` | Valider + generer alle artefakter for FINT-modellane | `generated/fint/` |
| `make ngr` | Valider + generer alle artefakter for NGR-modellane | `generated/ngr/` |
| `make oreg` | Valider + generer alle artefakter for OREG-registera | `generated/oreg/` |
| `make samt` | Valider + generer alle artefakter for SAMT-modellane | `generated/samt/` |

### Enkeltartefakter (alle skjema)

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

`make publish` køyrer `mkdocs/publish.sh` som kopier artefakter og dokumentasjon frå `generated/` til `mkdocs/docs/`, genererer `index.md` per skjema og domene, og oppdaterer navigasjonsstrukturen i `mkdocs.yml`. Nye domene og skjema dukkar opp automatisk neste gong `publish` vert køyrt.

## mcp-linkml-modell-utkast

| Kommando | Beskriving | Output |
|---|---|---|
| `make mcp-generate SCHEMA=<sti>` | Generer LinkML-utkast frå JSON Schema-fil | `<same katalog>/<skjema>-schema.yaml` |
| `make mcp-generate SCHEMA=<sti> FORMAT=json-schema PROFILE=default` | Same med eksplisitt format og profil | `<same katalog>/<skjema>-schema.yaml` |
| `make mcp-mod-build` | Bygg container-image | — |
| `make mcp-mod-smoke` | Røyktest med eksempel-meldingar | — |
| `make mcp-mod-test` | Køyr alle unit-testar | — |
| `make mcp-mod-run` | Start server interaktivt (stdin/stdout) | — |

## LinkML-validator mcp-server (mcp-linkml-validator)

| Kommando | Beskriving |
|---|---|
| `make mcp-validate SCHEMA=<sti> POLICY=bronze` | Validerer LinkML skjema mot bronze policyen |
| `make mcp-val-build` | Bygg container-image |
| `make mcp-val-smoke` | Røyktest med eksempel-meldingar |
| `make mcp-val-test` | Køyr policy-testar |
| `make mcp-val-run` | Start server interaktivt (stdin/stdout) |


