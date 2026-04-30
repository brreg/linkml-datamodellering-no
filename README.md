# linkml-w3c-no-profiles

Modellerer norske W3C-applikasjonsprofiler og tilknytte domenemodeller i [LinkML-format](https://linkml.io/).

## Krav

- [Podman](https://podman.io/) — alle kommandoar køyrer via container-image, ingen lokal installasjon nødvendig

## Kommandoar

### Skjema og testar

| Kommando | Beskriving |
|---|---|
| `make test` | Lint alle skjema og valider alle eksempelfiler |
| `make validate` | Valider skjema mot LinkML-metaskjemaet |
| `make gen-jsonld` | Generer JSON-LD kontekst (`*-context.jsonld`) |
| `make gen-shacl` | Generer SHACL shapes (`*-shapes.ttl`) |
| `make gen-python` | Generer Python-dataklassar (`*-model.py`) |
| `make gen-jsonschema` | Generer JSON Schema (`*-schema.json`) |
| `make gen-owl` | Generer OWL/Turtle-ontologi (`*-ontology.ttl`) |
| `make gen-rdf` | Generer RDF/Turtle-graf av skjemaet |
| `make docs` | Generer HTML-dokumentasjon til `generated/` |
| `make clean` | Slett `generated/` |

### MCP-validator

| Kommando | Beskriving |
|---|---|
| `make mcp-build` | Bygg container-bilete for MCP-serveren |
| `make mcp-test` | Køyr unit-testar for MCP-serveren |
| `make mcp-smoke` | Røyk-test MCP-serveren med eksempel-JSON-RPC-meldingar |
| `make mcp-run` | Start MCP-serveren interaktivt (stdin/stdout) |

### Eksempel: validering via MCP-serveren

MCP-serveren les JSON-RPC-meldingar frå stdin og skriv responsar til stdout. Kvar melding er éi linje.

```bash
make mcp-build   # éin gong
make mcp-smoke   # røyk-test med tests/test-mcp-linkml-validator.json
```

For å validere eit eige sjølvstendig skjema (utan relative importer), pipe meldingane direkte:

```bash
python3 -c "
import json
schema = '''
id: https://example.org/mitt-skjema
name: mitt-skjema
prefixes:
  linkml: https://w3id.org/linkml/
  ex: https://example.org/
default_prefix: ex
imports:
  - linkml:types
classes:
  Datasett:
    class_uri: ex:Datasett
    attributes:
      tittel:
        range: string
'''
msgs = [
    {'jsonrpc':'2.0','id':1,'method':'initialize','params':{}},
    {'jsonrpc':'2.0','id':2,'method':'tools/call','params':{
        'name':'validate_linkml_schema',
        'arguments':{'schemaText': schema}
    }},
]
print('\n'.join(json.dumps(m) for m in msgs))
" | podman run -i --rm mcp-linkml-validator
```

Valideringsresultatet kjem i `result.content[0].text` for melding 2:

```json
{
  "valid": true,
  "errorCount": 0,
  "warningCount": 2,
  "issues": [
    {
      "severity": "warning",
      "code": "missing_recommended_metadata",
      "target": "schema:mitt-skjema",
      "message": "Manglar anbefalt metadata: description"
    },
    {
      "severity": "warning",
      "code": "missing_recommended_metadata",
      "target": "class:Datasett",
      "message": "Manglar anbefalt metadata: description"
    }
  ]
}
```

> **Merk:** Skjema med relative importer (t.d. `../../common/`) kan ikkje resolverast frå MCP-serveren sin tempkatalog. Bruk `make test` / `linkml lint` direkte for slike skjema.

Policy-baserte tilleggsreglar (`required`/`recommended`-felt, påkravde fellesklassar) konfigurerast i `src/mcp-linkml-validator/policy.yaml`.

### Lint enkeltskjema direkte

```bash
podman run --rm -v "$(pwd):/work" -w /work -e PYTHONWARNINGS=ignore \
  docker.io/linkml/linkml:latest \
  linkml lint --ignore-warnings src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
```

## Katalogstruktur

```
src/
├── linkml/
│   ├── ap-no/                      # Norske W3C-applikasjonsprofiler
│   │   ├── common/                 # Felles slot-definisjonar (delt av alle AP-NO)
│   │   ├── dcat-ap-no/             # Datakatalogar og datasett
│   │   ├── dqv-ap-no/              # Datakvalitet
│   │   ├── cpsv-ap-no/             # Offentlege tenester
│   │   ├── skos-ap-no/             # Begrepssamlingar
│   │   └── xkos-ap-no/             # Utvidet klassifikasjon
│   ├── ngr/
│   │   └── ngr-adresse/            # Adressemodell (Matrikkelen)
│   ├── fint/                       # FINT-domenemodeller
│   │   ├── fint-common/            # Felles typar og abstrakte klassar
│   │   ├── fint-administrasjon/    # Lønn, arbeidsforhold, organisasjon
│   │   ├── fint-arkiv/             # Sak, journal, dokument
│   │   ├── fint-okonomi/           # Økonomi og rekneskap
│   │   ├── fint-personvern/        # Personvernmeldingar
│   │   ├── fint-ressurs/           # Ressursar
│   │   └── fint-utdanning/         # Utdanning og skole
│   └── fair/
│       └── fair-metadata/          # FAIR-metadataoverbygning (F/A/I/R-prinsippa)
├── mcp-linkml-validator/           # MCP-server for LinkML-validering
│   ├── server.py                   # JSON-RPC MCP-server
│   ├── policy.yaml                 # Konfigurerbare valideringsreglar
│   ├── Dockerfile
│   └── requirements.txt
└── templates/
    └── docgen/                     # Jinja2-malar for HTML-dokumentasjon

examples/
├── ap-no/                          # Eksempeldata for AP-NO-profilene
├── ngr/                            # Eksempeldata for NGR-domenemodellane
└── fair/                           # Eksempeldata for FAIR-metadata

tests/
├── fixtures/                       # Testfixturer med Container/tree_root for AP-NO og FAIR
├── test_schemas.sh                 # Lint og valider alle skjema og eksempel
├── test_mcp_server.py              # Unit-testar for MCP-validator (pytest)
└── test-mcp-linkml-validator.json  # Eksempel-JSON-RPC-meldingar for røyk-test

generated/                          # Genererte artefakter (ikkje innsjekka i git)
```

## Arkitekturprinsipp

### AP-NO-profiler

Skjema under `src/linkml/ap-no/` definerer klasser og slot-ar utan `Container`/`tree_root`. Dei er meint å importerast av domenemodeller og er ikkje sjølvstendige. Felles slot-ar som går att i fleire profiler ligg i `common/`.

Testfixturer (`tests/fixtures/`) legg til ein `Container`-klasse med `tree_root: true` for kvar profil, slik at eksempeldata kan validerast isolert.

### NGR- og FINT-domenemodeller

Skjema under `src/linkml/ngr/` og `src/linkml/fint/` er sjølvstendige og har eigen `tree_root`-klasse. FINT-modellane importerer `fint-common` for felles abstrakte klassar og typar (`Aktoer`, `Enhet`, `Begrep`, `Identifikator` m.fl.).

### FAIR-metadata

`src/linkml/fair/fair-metadata/` modellerer gapet mellom AP-NO-profilene og [FAIR-prinsippa](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable). Skjemaet er eit bibliotek utan `tree_root`; testfixturen (`tests/fixtures/fair-metadata-fixture.yaml`) legg til `Container` for validering.

### MCP-validator

`src/mcp-linkml-validator/` er ein [MCP-server](https://modelcontextprotocol.io/) som eksponerer LinkML-validering som eit verktøy (`validate_linkml_schema`). Serveren køyrer standard LinkML-linting og policy-baserte tilleggsreglar konfigurerbare via `policy.yaml`. Bygg og køyr med `make mcp-build` og `make mcp-run`.
