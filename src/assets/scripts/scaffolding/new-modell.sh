#!/usr/bin/env bash
# Opprettar filstruktur og boilerplate for ein ny LinkML-domenemodell.
# Bruk: bash src/assets/scripts/scaffolding/new-modell.sh <name> <domain>
set -euo pipefail

NAME="${1:-}"
DOMAIN="${2:-}"

if [[ -z "$NAME" || -z "$DOMAIN" ]]; then
    echo "Feil: NAME og DOMAIN er påkravde." >&2
    echo "Bruk: make new-modell NAME=<namn> DOMAIN=<domene>" >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
SCHEMA_DIR="$REPO_ROOT/src/linkml/$DOMAIN/$NAME"
EXAMPLES_DIR="$SCHEMA_DIR/examples"
SCHEMA_FILE="$SCHEMA_DIR/$NAME-schema.yaml"
SCHEMA_FILE_REL="src/linkml/$DOMAIN/$NAME/$NAME-schema.yaml"
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
            'schemaTitle': 'TODO: tittel for $NAME',
            'profile': 'silver',
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

# Transformer det genererte skjemaet (PascalCase stub-klassenamn, versjonslåst
# common-ap-no-import i staden for lokal id-slot utan slot_uri — sjå
# specs/done/new-modell-genererer-gyldig-eksempel.md), skriv resultatet til
# $SCHEMA_FILE, og hent ut container-klassenamn/-slot for eksempelfila.
read CONTAINER_CLASS CONTAINER_SLOT < <(python3 -c "
import sys
import datetime
from pathlib import Path
import yaml

sys.path.insert(0, '$REPO_ROOT/src/assets/scripts')
from utils.codeowners import load_codeowners, find_owner_org

raw = '''$LINKML_YAML'''
lines = raw.splitlines(keepends=True)
header_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    header_lines.append(line)
    i += 1
    if line.strip() == '':
        break
header = ''.join(header_lines)
body = ''.join(lines[i:])

schema = yaml.safe_load(body)

def to_pascal_case(name):
    parts = name.replace('_', '-').split('-')
    return ''.join(p.capitalize() for p in parts if p)

classes = schema.get('classes') or {}
container_name = None
stub_name = None
for cname, cdef in classes.items():
    if cdef.get('tree_root'):
        container_name = cname
    else:
        stub_name = cname

if stub_name:
    new_stub_name = to_pascal_case(stub_name)
    if new_stub_name != stub_name:
        classes[new_stub_name] = classes.pop(stub_name)
        if container_name:
            for slot_def in (classes[container_name].get('attributes') or {}).values():
                if slot_def.get('range') == stub_name:
                    slot_def['range'] = new_stub_name
        stub_name = new_stub_name

slots = schema.get('slots') or {}
slots.pop('id', None)
if slots:
    schema['slots'] = slots
else:
    schema.pop('slots', None)

# Post-prosesser silver-annotasjonane (statiske TODO-placeholder frå
# profiles/silver.yaml) til faktiske, dynamisk utleidde verdiar.
annotations = schema.get('annotations') or {}
if annotations:
    model_path = Path('src/linkml/$DOMAIN/$NAME')
    orgs = load_codeowners(Path('$REPO_ROOT'))
    owner_org = find_owner_org(model_path, orgs)
    if owner_org and owner_org.get('org_uri'):
        annotations['utgiver'] = owner_org['org_uri']
    else:
        print(f'ÅTVARING: fann ingen eigar-organisasjon for {model_path} i CODEOWNERS.md — behandlar annotations.utgiver som TODO', file=sys.stderr)
    today = datetime.date.today().isoformat()
    annotations['endringsdato'] = today
    annotations['utgivelsesdato'] = today
    schema['annotations'] = annotations

container_slot = None
if container_name:
    attrs = classes[container_name].get('attributes') or {}
    if attrs:
        container_slot = list(attrs.keys())[0]

body_out = yaml.dump(schema, allow_unicode=True, default_flow_style=False, sort_keys=False)
body_out = body_out.replace(
    '- linkml:types\n',
    '- linkml:types\n'
    '- https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.13.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema'
    '  # TODO: endre/legg til imports etter behov\n',
    1,
)
body_out = body_out.replace(
    'license: https://data.norge.no/nlod/no/2.0\n',
    'license: https://data.norge.no/nlod/no/2.0'
    '  # Andre gyldige lisensar: https://brreg.github.io/linkml-datamodellering-no/ap-no/common-ap-no/klasser/eulicence/\n',
    1,
)

with open('$SCHEMA_FILE', 'w') as f:
    f.write(header)
    f.write(body_out)
    f.write('# TODO: Gi stub-klassen eit meir meiningsfullt namn.\n')
    f.write('# TODO: Legg til slots og slot_usage for eigenskapane i modellen.\n')

print(container_name or '${SCHEMA_NAME}Container', container_slot or '${SCHEMA_NAME}er')
")

cat > "$EXAMPLE_FILE" << EOF
# Eksempel for $NAME
# Tilpass instansane med reelle verdiar etter at skjemaet er ferdigstilt.
---
$CONTAINER_SLOT:
  - id: $SCHEMA_ID/eksempel-1
EOF

MANIFEST_FILE="$SCHEMA_DIR/build.yaml"
cat > "$MANIFEST_FILE" << 'EOF'
publish_external: false
validation_policy: silver

generators:
  # Artefaktgeneratorer
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  example_rdf: true
  openapi: true
  graphql: true

  # Dokumentasjonsgeneratorer
  erdiagram: true
  docs: true
  plantuml: true
EOF

DESCRIPTION_FILE="$SCHEMA_DIR/description.md"
cat > "$DESCRIPTION_FILE" << EOF
<!-- Valfri skildring av $NAME. Vert vist i portalen mellom ER-diagrammet og klasselista. -->
<!-- Fyll ut eller slett denne fila. -->
EOF

echo ""
echo "Oppretta:"
echo "  $SCHEMA_FILE"
echo "  $EXAMPLE_FILE"
echo "  $MANIFEST_FILE"
echo "  $DESCRIPTION_FILE"

# Oppdater .github/valid-scopes.txt
echo ""
echo "Oppdaterer .github/valid-scopes.txt..."
cd "$REPO_ROOT"
make --no-print-directory update-valid-scopes

echo ""
echo "Neste steg:"
echo "  1. Gi stub-klassen eit meir meiningsfullt namn og legg til eigenskapar"
echo "  2. Byt common-ap-no-importet til ein reell AP-NO-profil ved behov (sjå TODO-kommentar i skjemafila)"
echo "  3. Fyll ut description.md med formål og kontekst (eller slett ho)"
echo "  4. Valider: make mcp-linkml-valider-modell SCHEMA=$SCHEMA_FILE_REL POLICY=bronze"
