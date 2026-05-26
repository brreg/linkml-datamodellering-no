#!/usr/bin/env bash
# Opprettar filstruktur og boilerplate for ein ny LinkML-domenemodell.
# Bruk: bash src/assets/scripts/new-model.sh <name> <domain>
set -euo pipefail

NAME="${1:-}"
DOMAIN="${2:-}"

if [[ -z "$NAME" || -z "$DOMAIN" ]]; then
    echo "Feil: NAME og DOMAIN er påkravde." >&2
    echo "Bruk: make new-model NAME=<namn> DOMAIN=<domene>" >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
SCHEMA_DIR="$REPO_ROOT/src/linkml/$DOMAIN/$NAME"
EXAMPLES_DIR="$REPO_ROOT/examples/$DOMAIN"
SCHEMA_FILE="$SCHEMA_DIR/$NAME-schema.yaml"
EXAMPLE_FILE="$EXAMPLES_DIR/$NAME-eksempel.yaml"

if [[ -d "$SCHEMA_DIR" ]]; then
    echo "Feil: katalogen $SCHEMA_DIR finst allereie." >&2
    exit 1
fi

LINKML_GEN_DIR="$REPO_ROOT/src/mcp-linkml-modell-utkast"
LINKML_GEN_IMAGE="mcp-linkml-modell-utkast"
SCHEMA_ID="https://data.norge.no/$DOMAIN/$NAME"
# LinkML name-felt: bindestrek er ikkje tillate, bruk understrek
SCHEMA_NAME="${NAME//-/_}"

echo "Genererer skjema via mcp-linkml-modell-utkast..."

LINKML_YAML=$(printf '%s\n%s\n' \
    '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' \
    "$(python3 -c "
import json
print(json.dumps({
    'jsonrpc': '2.0', 'id': 2, 'method': 'tools/call',
    'params': {
        'name': 'generate_linkml',
        'arguments': {
            'inputFormat': 'empty',
            'schemaId': '$SCHEMA_ID',
            'schemaName': '$SCHEMA_NAME',
            'validate': False,
        }
    }
}))
")" \
  | podman run -i --rm \
      -v "$LINKML_GEN_DIR/server.py:/app/server.py:ro" \
      -v "$LINKML_GEN_DIR/converter.py:/app/converter.py:ro" \
      -v "$LINKML_GEN_DIR/validator.py:/app/validator.py:ro" \
      -v "$LINKML_GEN_DIR/profiles:/app/profiles:ro" \
      "$LINKML_GEN_IMAGE" \
  | python3 -c "
import json, sys
for line in sys.stdin:
    try:
        obj = json.loads(line.strip())
        if obj.get('id') == 2:
            content = obj['result']['content'][0]['text']
            print(json.loads(content)['linkmlSchema'])
    except Exception:
        pass
")

if [[ -z "$LINKML_YAML" ]]; then
    echo "Feil: mcp-linkml-modell-utkast returnerte tomt svar." >&2
    exit 1
fi

mkdir -p "$SCHEMA_DIR"
mkdir -p "$EXAMPLES_DIR"

# Legg til kommentar om import og skriv skjema
{
    echo "$LINKML_YAML"
    echo "# TODO: Legg til domene-spesifikke imports etter 'linkml:types', t.d.:"
    echo "#   - ../../ap-no/dcat-ap-no/dcat-ap-no-schema"
    echo "# TODO: Gi stub-klassen eit meiningsfult norsk namn (PascalCase)."
    echo "# TODO: Legg til slots og slot_usage for eigenskapane i modellen."
} > "$SCHEMA_FILE"

# Ekstraher container-slot-namn frå det genererte YAML-et
CONTAINER_SLOT=$(python3 -c "
import yaml, sys
schema = yaml.safe_load('''$LINKML_YAML''')
attrs = schema.get('classes', {}).get('Containerklasse', {}).get('attributes', {})
print(list(attrs.keys())[0] if attrs else '${SCHEMA_NAME}er')
" 2>/dev/null || echo "${SCHEMA_NAME}er")

cat > "$EXAMPLE_FILE" << EOF
# Eksempel for $NAME
# Tilpass instansane med reelle verdiar etter at skjemaet er ferdigstilt.
---
Containerklasse:
  $CONTAINER_SLOT:
    - id: $SCHEMA_ID/eksempel-1
EOF

GENERATE_FILE="$SCHEMA_DIR/generate.yaml"
cat > "$GENERATE_FILE" << 'EOF'
generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
EOF

echo ""
echo "Oppretta:"
echo "  $SCHEMA_FILE"
echo "  $EXAMPLE_FILE"
echo "  $GENERATE_FILE"
echo ""
echo "Neste steg:"
echo "  1. Gi stub-klassen eit norsk namn og legg til eigenskapar"
echo "  2. Legg til domene-spesifikke imports (sjå kommentar i skjemafila)"
echo "  3. Valider: make mcp-validate SCHEMA=$SCHEMA_FILE POLICY=bronze"
