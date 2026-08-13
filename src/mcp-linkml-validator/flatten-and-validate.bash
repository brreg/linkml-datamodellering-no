#!/usr/bin/env bash
# Validerer eit LinkML-skjema mot mcp-linkml-validator. Namnet er historisk —
# skriptet flatar ikkje lenger ut importar sjølv: heile repoet vert montert
# inn i validator-kontainaren, og SchemaView løyser relative importar
# naturleg mot filsystemet. Sjå specs/backlog/effektiviser-mcp-linkml-
# validator-koyretid.md (Tiltak 2) for grunngjevinga — den tidlegare
# `gen-linkml --mergeimports`-utflatinga var reint dobbeltarbeid av det
# SchemaView allereie gjer internt, berre via ein ekstra podman-kontainar.
#
# Bruk: bash src/mcp-linkml-validator/flatten-and-validate.bash <sti-til-skjema> [policy] [instans]
# Eks:  bash src/mcp-linkml-validator/flatten-and-validate.bash \
#           src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml gold
# Eks med eksplisitt datafil:
#   bash src/mcp-linkml-validator/flatten-and-validate.bash \
#       src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml felles-begrepskatalog \
#       data/begrep/brreg-begrep.yaml

set -euo pipefail

SCHEMA="${1:?Bruk: $0 <sti-til-skjema> [policy] [instans]}"
POLICY="${2:-bronze}"
EXPLICIT_INSTANCE="${3:-}"
# REPO_ROOT og VALIDATOR_DIR kan setjast utanfrå (t.d. i reusable workflows).
REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
VALIDATOR_DIR="${VALIDATOR_DIR:-$(cd "$(dirname "$0")" && pwd)}"
NAME=$(basename "$(dirname "$SCHEMA")")
DOMAIN=$(basename "$(dirname "$(dirname "$SCHEMA")")")
# Ny eksempelplassering: src/linkml/<domene>/<modell>/examples/<modell>-eksempel.yaml
EXAMPLE="${REPO_ROOT}/src/linkml/${DOMAIN}/${NAME}/examples/${NAME}-eksempel.yaml"
# Fallback til gammal plassering for bakoverkompatibilitet
if [ ! -f "$EXAMPLE" ]; then
    EXAMPLE="${REPO_ROOT}/examples/${DOMAIN}/${NAME}-eksempel.yaml"
fi
if [ -n "$EXPLICIT_INSTANCE" ]; then
    EXAMPLE="${REPO_ROOT}/${EXPLICIT_INSTANCE}"
fi
# Kan overstyrast utanfrå (t.d. for å bruke eit spesifikt image)
MCP_IMAGE="${MCP_IMAGE:-mcp-linkml-validator}"

# Send skjemastien direkte til MCP-serveren (schemaPath, ikkje schemaText) —
# heile repoet vert montert read-only på /repo slik at SchemaView kan løyse
# relative importar. Policyar vert monterte inn frå repoet slik at endringar
# tek effekt utan rebuild.
python3 -c "
import json, sys, os, yaml
schema_rel, container_schema_path, policy, example_path = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
args = {'schemaPath': container_schema_path, 'policy': policy}
if os.path.isfile(example_path):
    schema = yaml.safe_load(open(schema_rel).read())
    has_tree_root = any(
        isinstance(cls, dict) and cls.get('tree_root')
        for cls in (schema.get('classes') or {}).values()
    )
    if has_tree_root:
        args['instanceText'] = open(example_path).read()
msgs = [
    {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {}},
    {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/call', 'params': {
        'name': 'validate_linkml_schema',
        'arguments': args,
    }},
]
print('\n'.join(json.dumps(m) for m in msgs))
" "$REPO_ROOT/$SCHEMA" "/repo/$SCHEMA" "$POLICY" "$EXAMPLE" | podman run -i --rm \
  -v "$REPO_ROOT:/repo:ro" \
  -v "$VALIDATOR_DIR/server.py:/app/server.py:ro" \
  -v "$VALIDATOR_DIR/policies:/app/policies:ro" \
  "$MCP_IMAGE" | python3 -c "
import json, sys
for line in sys.stdin:
    r = json.loads(line)
    if r.get('id') != 2:
        continue
    if 'error' in r:
        print(f\"MCP-feil: {r['error'].get('message', r['error'])}\", file=sys.stderr)
        sys.exit(1)
    print(r['result']['content'][0]['text'])
"
