# Implementasjonsplan: `mcp-json2linkml`

MCP-server som tek eit JSON Schema som input og genererer eit første utkast til ein LinkML-modell, basert på konfigurerbare profiler og CLAUDE.md-modelleringsprinsippa.

Følgjer same mønster som `src/mcp-linkml-validator/`: eitt Python-script per server, profiler som YAML-filer, stdin/stdout JSON-RPC 2.0, og podman-container for køyring.

## Filstruktur (sluttmål)

```
src/mcp-json2linkml/
  server.py              ← JSON-RPC 2.0-server, handterar 2 verktøy
  converter.py           ← convert(json_schema, profile) → LinkML YAML str
  validator.py           ← validate_generated(linkml_yaml) → dict
  profiles/
    ap-no.yaml           ← initiell profil (CLAUDE.md-prinsippa)
  requirements.txt
  Dockerfile

tests/
  test-mcp-json2linkml.json    ← smoke test-meldingar
  test_mcp_json2linkml.py      ← unit-testar (ingen podman)
```

---

## Del 1 — Profil (`profiles/ap-no.yaml`)

**Lever:** `src/mcp-json2linkml/profiles/ap-no.yaml`

**Avheng av:** ingenting

**Ferdig når:** fila finst og er gyldig YAML med alle nøklane nedanfor.

Profilen er kontrakten resten av koden byggjer på. Alle andre delar les verdiar herifrå — skriv denne fyrst.

```yaml
version: 1
description: >
  AP-NO-profil for JSON Schema → LinkML-konvertering.
  Implementerer prinsippa i CLAUDE.md for norsk offentleg sektor.

naming:
  class_uri_prefix: "ex"
  slot_uri_prefix: "ex"

standard_prefixes:
  linkml: "https://w3id.org/linkml/"
  dct:    "http://purl.org/dc/terms/"
  dcat:   "http://www.w3.org/ns/dcat#"
  foaf:   "http://xmlns.com/foaf/0.1/"
  skos:   "http://www.w3.org/2004/02/skos/core#"
  xsd:    "http://www.w3.org/2001/XMLSchema#"
  rdf:    "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  rdfs:   "http://www.w3.org/2000/01/rdf-schema#"

schema_defaults:
  default_range: string
  imports:
    - linkml:types

generation:
  add_id_slot: true
  add_container_class: true
  container_class_name: "Containerklasse"
  container_slot_suffix: "er"        # suffiks for fleirtal i container-slots
  add_see_also_stub: true
  see_also_base_uri: "https://data.norge.no/concepts/"

subsets:
  required_maps_to: "Obligatorisk"
  non_required_default: "Anbefalt"

type_mapping:
  string:  string
  integer: integer
  number:  float
  boolean: boolean

format_mapping:
  uri:       uriorcurie
  date:      date
  date-time: datetime
  time:      time
```

---

## Del 2 — Konverteringslogikk (`converter.py`) + testar

**Lever:** `src/mcp-json2linkml/converter.py` og `tests/test_mcp_json2linkml.py` (klassen `TestConversion`)

**Avheng av:** Del 1 (profil-YAML)

**Ferdig når:** alle testar i `TestConversion` er grøne og `SchemaView` kan laste output utan parse-feil.

### Offentleg API

```python
def convert(
    json_schema: dict,
    profile: dict,
    schema_id: str,
    schema_name: str,
    schema_title: str = "",
) -> tuple[str, list[str]]:
    """Returnerer (linkml_yaml_str, warnings)."""
```

### Klassifisering av JSON Schema-noder

| JSON Schema-konstruksjon | Handtering |
|---|---|
| `type: object` med `properties` | → LinkML-klasse + globale slots |
| `$defs` / `definitions` | → separate klasser |
| `$ref: "#/$defs/Foo"` | → `range: Foo` |
| `type: array` med `items` | → `multivalued: true` + behandling av `items` |
| `type: string/integer/number/boolean` | → range frå `type_mapping` |
| `format: uri/date/date-time` | → range frå `format_mapping` (overrider type) |
| `type: null` | → ignorert |
| `anyOf: [{type: X}, {type: null}]` | → nullable-mønster: bruk type X |

### Algoritme (steg-for-steg)

1. Bygg `prefixes:` frå `profile["standard_prefixes"]` + `ex:` avleidd frå `schemaId`
2. Bygg skjema-topp (`id`, `name`, `title`, `description`, `default_prefix`, `imports`)
3. Registrer subsets `Obligatorisk`, `Anbefalt`, `Valgfri` alltid
4. Traverser `$defs` / `definitions` + rot-`properties`, samle `(klassenamn → {properties, required_set})`
5. For kvar klasse:
   - `class_uri: ex:<KlasseNamn>` (stub)
   - `see_also: ["https://data.norge.no/concepts/TODO"]` om profil seier det
   - `slots: [id, ...]` om `add_id_slot: true`
   - `slot_usage` med `required: true` + `in_subset: [Obligatorisk]` for required-felt
   - `slot_usage` med `in_subset: [Anbefalt]` for øvrige felt
6. Legg til global `id`-slot med `identifier: true` og `range: uriorcurie`
7. Legg til global slot per eigeskap med `slot_uri: ex:<slotnamn>` (stub)
8. Legg til containerklasse (`tree_root: true`) med ein multivalued/inlined slot per klasse
9. Serialiser med `yaml.dump(..., sort_keys=False)`

### Kanttilfelle konverteraren må handtere

| Tilfelle | Handtering |
|---|---|
| JSON Schema utan `$defs` | Éin klasse med namn frå `schema_name` |
| Slot-namns-kollisjon (same namn, ulik type) | Åtvaring i `warnings`, bruk første type |
| Sirkulære `$ref` | `visited`-set under traversering, åtvaring om syklus |
| `$ref` utanfor same fil | Åtvaring, ikkje exception |
| `anyOf` med fleire ikkje-null-typar | Åtvaring, fallback `range: string` |
| `allOf` | Ikkje støtta v1, åtvaring |
| `additionalProperties` | Ignorert v1, åtvaring |
| Tom `properties`-dict | Klasse utan slots (gyldig) |

### Testar (`TestConversion`)

- Enkelt objekt med required/non-required properties → korrekt `slot_usage`
- `$ref` til `$defs`-definisjon → `range:` vert sett til klassnamnet
- `type: array` → `multivalued: true`
- `format: uri` → `range: uriorcurie`
- `format: date` → `range: date`
- Containerklasse vert generert med `tree_root: true`
- `id`-slot vert generert med `identifier: true`
- Slot-namns-kollisjon → åtvaring, ikkje exception
- `anyOf` med `null` → nullable-mønster
- JSON Schema utan `$defs` → éin klasse

---

## Del 3 — Valideringslogikk (`validator.py`) + testar

**Lever:** `src/mcp-json2linkml/validator.py` og testar i `tests/test_mcp_json2linkml.py` (klassen `TestValidation`)

**Avheng av:** Del 2 (converter produserer gyldig YAML)

**Ferdig når:** `validate_generated()` returnerer strukturert resultat for både gyldig og ugyldig input.

### Offentleg API

```python
def validate_generated(linkml_yaml: str) -> dict:
    """Returnerer {"lint_issues": [...], "dummy_validation": {...}}"""
```

### Steg A — Lint

Last skjemaet med `SchemaView` (parse-feil fangast og rapporterast). Køyr `linkml.linter.linter.Linter` — same mønster som eksisterande `mcp-linkml-validator`.

### Steg B — Dummy-datasett-validering

1. Finn containerklassen (`tree_root: true` i SchemaView)
2. Finn obligatoriske slots per klasse (`required: true` i `slot_usage`)
3. Bygg minimalt YAML-dokument med éin instans per klasse og placeholder-verdiar:

| Range | Placeholder |
|---|---|
| `uriorcurie` | `"ex:dummy-1"` |
| `string` | `"dummy"` |
| `integer` | `0` |
| `float` | `0.0` |
| `date` | `"2024-01-01"` |
| `datetime` | `"2024-01-01T00:00:00"` |
| `boolean` | `false` |

4. Køyr `linkml_runtime`-validering mot skjemaet og returner resultat

### Testar (`TestValidation`)

- Gyldig YAML frå converter → ingen lint-feil, dummy-validering passerer
- Syntaktisk ugyldig YAML → lint_issues inneheld parse-feil
- Skjema utan containerklasse → dummy_validation returnerer advarsel, krasjar ikkje

---

## Del 4 — MCP-server (`server.py`) + protokolltestar

**Lever:** `src/mcp-json2linkml/server.py` og testar i `tests/test_mcp_json2linkml.py` (klassane `TestMCPProtocol` og `TestListProfiles`)

**Avheng av:** Del 2 og Del 3

**Ferdig når:** alle protokolltestar er grøne og serveren svarar korrekt på alle JSON-RPC-metodar.

### Verktøy 1: `generate_linkml_from_json_schema`

Input-parametrar:

| Parameter | Type | Påkravd | Default |
|---|---|---|---|
| `jsonSchema` | string | ja | — |
| `schemaId` | string | ja | — |
| `schemaName` | string | ja | — |
| `schemaTitle` | string | nei | `""` |
| `profile` | string | nei | `"ap-no"` |
| `validate` | boolean | nei | `true` |

Output i `content[0].text`:

```json
{
  "linkmlSchema": "...",
  "warnings": [...],
  "lintIssues": [...],
  "dummyValidation": {...}
}
```

### Verktøy 2: `list_profiles`

Ingen parametrar. Returnerer liste av `{"name": "...", "description": "..."}` for alle YAML-filer i `profiles/`.

### Testar (`TestMCPProtocol`, `TestListProfiles`)

- `initialize` → korrekt `serverInfo` og `capabilities`
- `tools/list` → begge verktøy er lista
- `list_profiles` → returnerer minst `ap-no`
- `generate_linkml_from_json_schema` med gyldig input → `linkmlSchema` er gyldig YAML
- `generate_linkml_from_json_schema` med `validate: false` → `lintIssues` er tom liste
- Ukjent verktøy → `error.code: -32602`
- Ugyldig JSON → `error.code: -32700`

---

## Del 5 — Container og Makefile-integrasjon

**Lever:** `Dockerfile`, `requirements.txt`, og nye Makefile-targets

**Avheng av:** Del 4 (server.py er ferdig)

**Ferdig når:** `make json2linkml-build` og `make json2linkml-smoke` går gjennom utan feil.

### `requirements.txt`

```
linkml
linkml-runtime
pyyaml
```

### `Dockerfile`

Identisk med eksisterande `mcp-linkml-validator/Dockerfile`, med `converter.py` og `validator.py` lagt til som ekstra placeholder-filer:

```dockerfile
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential git \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN touch server.py converter.py validator.py
RUN useradd -m mcp
USER mcp
CMD ["python", "server.py"]
```

### Makefile-tillegg

```makefile
JSON2LINKML_DIR   := src/mcp-json2linkml
JSON2LINKML_IMAGE := mcp-json2linkml
JSON2LINKML_RUN   := podman run -i --rm \
  -v "$(CURDIR)/$(JSON2LINKML_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(JSON2LINKML_DIR)/converter.py:/app/converter.py:ro" \
  -v "$(CURDIR)/$(JSON2LINKML_DIR)/validator.py:/app/validator.py:ro" \
  -v "$(CURDIR)/$(JSON2LINKML_DIR)/profiles:/app/profiles:ro"

json2linkml-build:
	podman build -t $(JSON2LINKML_IMAGE) $(JSON2LINKML_DIR)

json2linkml-run:
	$(JSON2LINKML_RUN) $(JSON2LINKML_IMAGE)

json2linkml-smoke: json2linkml-build
	cat tests/test-mcp-json2linkml.json | $(JSON2LINKML_RUN) $(JSON2LINKML_IMAGE)

# Bruk: make json2linkml-generate SCHEMA=<sti> [PROFILE=ap-no]
json2linkml-generate:
	@test -n "$(SCHEMA)" || (echo "Bruk: make json2linkml-generate SCHEMA=<sti> [PROFILE=ap-no]"; exit 1)
	@python3 -c " \
import json, sys; \
schema = open('$(SCHEMA)').read(); \
profile = '$(or $(PROFILE),ap-no)'; \
msgs = [ \
  {'jsonrpc':'2.0','id':1,'method':'initialize','params':{}}, \
  {'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'generate_linkml_from_json_schema','arguments':{'jsonSchema':schema,'schemaId':'https://example.org/generated','schemaName':'generated','profile':profile}}}, \
]; \
print('\n'.join(json.dumps(m) for m in msgs)) \
" | $(JSON2LINKML_RUN) $(JSON2LINKML_IMAGE) \
  | python3 -c " \
import json,sys; \
[print(json.loads(r['result']['content'][0]['text'])['linkmlSchema']) \
 for r in map(json.loads,sys.stdin) if r.get('id')==2] \
"
```

### Smoke test (`tests/test-mcp-json2linkml.json`)

```json
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
{"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}
{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_profiles", "arguments": {}}}
{"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "generate_linkml_from_json_schema", "arguments": {"jsonSchema": "{\"type\": \"object\", \"properties\": {\"namn\": {\"type\": \"string\"}, \"dato\": {\"type\": \"string\", \"format\": \"date\"}}, \"required\": [\"namn\"]}", "schemaId": "https://example.org/test", "schemaName": "test", "validate": true}}}
```
