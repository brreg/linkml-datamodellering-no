#!/usr/bin/env bash
# Validerer eit LinkML-skjema med alle importar resolve (flatten + validate).
# Nyttig for domenemodeller med relative importar (t.d. FINT, AP-NO).
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
VALIDATOR_DIR="${VALIDATOR_DIR:-$(dirname "$0")}"
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
# Desse kan overstyrasst utanfrå (t.d. for å bruke eit spesifikt image)
LINKML_IMAGE="${LINKML_IMAGE:-ghcr.io/brreg/linkml-local:latest}"
MCP_IMAGE="${MCP_IMAGE:-mcp-linkml-validator}"

TMPFILE=$(mktemp /tmp/flat-XXXXXX.yaml)
trap 'rm -f "$TMPFILE"' EXIT

# Steg 1: Flat ut alle importar til eitt komplett skjema
echo "→ Flattar ut $SCHEMA ..." >&2
podman run --rm \
  -v "$REPO_ROOT:/work" \
  -w /work \
  -e PYTHONWARNINGS=ignore \
  "$LINKML_IMAGE" \
  gen-linkml --mergeimports --format yaml "$SCHEMA" \
  > "$TMPFILE" 2>/dev/null

# Steg 1b: gen-linkml --mergeimports strip tree_root — les det tilbake frå original-skjemaet.
python3 - "$REPO_ROOT/$SCHEMA" "$TMPFILE" << 'PYEOF'
import yaml, sys

orig_path, flat_path = sys.argv[1], sys.argv[2]
with open(orig_path) as f:
    orig = yaml.safe_load(f)
tree_root_classes = {
    name for name, cls in (orig.get("classes") or {}).items()
    if isinstance(cls, dict) and cls.get("tree_root")
}
if not tree_root_classes:
    sys.exit(0)
with open(flat_path) as f:
    flat = yaml.safe_load(f)
for name in tree_root_classes:
    if name in (flat.get("classes") or {}) and isinstance(flat["classes"][name], dict):
        flat["classes"][name]["tree_root"] = True
with open(flat_path, "w") as f:
    yaml.dump(flat, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
PYEOF

# Steg 2: Send flattened schema til MCP-serveren og print resultatet.
# Policyar vert montert inn frå repoet slik at endringar tek effekt utan rebuild.
echo "→ Validerer (policy: $POLICY) ..." >&2
python3 -c "
import json, sys, os, yaml
flat_path, policy, example_path = sys.argv[1], sys.argv[2], sys.argv[3]
schema = open(flat_path).read()
args = {'schemaText': schema, 'policy': policy}
if os.path.isfile(example_path):
    flat = yaml.safe_load(schema)
    has_tree_root = any(
        isinstance(cls, dict) and cls.get('tree_root')
        for cls in (flat.get('classes') or {}).values()
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
" "$TMPFILE" "$POLICY" "$EXAMPLE" | podman run -i --rm \
  -v "$VALIDATOR_DIR/server.py:/app/server.py:ro" \
  -v "$VALIDATOR_DIR/policies:/app/policies:ro" \
  "$MCP_IMAGE" | python3 -c "
import json, sys
for line in sys.stdin:
    r = json.loads(line)
    if r.get('id') == 2:
        print(r['result']['content'][0]['text'])
"
