#!/usr/bin/env bash
# Opprettar filstruktur og boilerplate for ein ny LinkML-domenemodell.
# Bruk: bash src/assets/scripts/scaffolding/new-modell.sh <name> <domain> [json-schema-sti]
set -euo pipefail

NAME="${1:-}"
DOMAIN="${2:-}"
JSON_SCHEMA="${3:-}"

if [[ -z "$NAME" || -z "$DOMAIN" ]]; then
    echo "Feil: NAME og DOMAIN er påkravde." >&2
    echo "Bruk: make new-modell DOMAIN=<domene> NAME=<namn> [JSON_SCHEMA=<sti>]" >&2
    exit 1
fi

if [[ -n "$JSON_SCHEMA" && ! -f "$JSON_SCHEMA" ]]; then
    echo "Feil: JSON_SCHEMA-fila $JSON_SCHEMA finst ikkje." >&2
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

# Les gjeldande dcat-ap-no-versjon frå manifestet (sannkjelda release-please
# sjølv brukar) i staden for å hardkode tag-namnet — hardkoda versjonar går
# stalig ved kvart dcat-ap-no-release og må rettast manuelt i etterkant.
DCAT_AP_NO_VERSION=$(jq -r '."src/linkml/ap-no/dcat-ap-no"' "$REPO_ROOT/.github/release-please-manifest.json")
if [[ -z "$DCAT_AP_NO_VERSION" || "$DCAT_AP_NO_VERSION" == "null" ]]; then
    echo "Feil: fann ikkje dcat-ap-no-versjon i .github/release-please-manifest.json" >&2
    exit 1
fi

REQUEST_SCRIPT="$REPO_ROOT/src/assets/scripts/makefile/mcp-build-modell-utkast-request.py"
RESPONSE_SCRIPT="$REPO_ROOT/src/assets/scripts/makefile/mcp-extract-modell-utkast-response.py"

if [[ -n "$JSON_SCHEMA" ]]; then
    echo "Genererer skjema via mcp-linkml-modell-utkast frå JSON Schema ($JSON_SCHEMA)..."
    INPUT_FORMAT=json-schema
    INPUT_FILE_ARGS=(--input-file "$JSON_SCHEMA")
else
    echo "Genererer skjema via mcp-linkml-modell-utkast..."
    INPUT_FORMAT=empty
    INPUT_FILE_ARGS=()
fi

LINKML_YAML=$(python3 "$REQUEST_SCRIPT" \
    --input-format "$INPUT_FORMAT" \
    "${INPUT_FILE_ARGS[@]}" \
    --schema-id "$SCHEMA_ID" \
    --schema-name "$SCHEMA_NAME" \
    --schema-title "TODO: tittel for $NAME" \
    --policy silver \
    --no-validate \
  | podman run -i --rm \
      -v "$LINKML_GEN_DIR/server.py:/app/server.py:ro" \
      -v "$LINKML_GEN_DIR/converter.py:/app/converter.py:ro" \
      -v "$LINKML_GEN_DIR/validator.py:/app/validator.py:ro" \
      -v "$LINKML_GEN_DIR/profiles:/app/profiles:ro" \
      "$LINKML_GEN_IMAGE" \
  | python3 "$RESPONSE_SCRIPT")

if [[ -z "$LINKML_YAML" ]]; then
    echo "Feil: mcp-linkml-modell-utkast returnerte tomt svar." >&2
    exit 1
fi

mkdir -p "$SCHEMA_DIR"
mkdir -p "$EXAMPLES_DIR"

# Skriv LINKML_YAML til ei mellombels fil i staden for å interpolere han som
# eit Python-strenglitteral (sjå
# specs/done/fiks-syntaxwarning-json-schema-interpolasjon.md) — JSON-schema-
# genererte skjema kan innehalde regex-mønster med bakover-skråstrekar
# (t.d. \d, \.), og eit strenglitteral-interpolert innhald med slike teikn
# gir anten ei SyntaxWarning (ukjende escape som \d) eller, verre, stille
# feiltolking av gyldige Python-escape (\n, \t, \\ osv.) til faktiske
# spesialteikn. Filinnhald gjennom open().read() er ikkje underlagt
# strenglitteral-parsing i det heile.
RAW_SCHEMA_TMP=$(mktemp)
trap 'rm -f "$RAW_SCHEMA_TMP"' EXIT
printf '%s' "$LINKML_YAML" > "$RAW_SCHEMA_TMP"

# Transformer det genererte skjemaet (PascalCase klassenamn og containerklasse,
# versjonslåst common-ap-no-import i staden for lokal id-slot utan slot_uri —
# sjå specs/done/new-modell-genererer-gyldig-eksempel.md), skriv resultatet til
# $SCHEMA_FILE, og hent ut container-klassenamn/-slot for eksempelfila.
read CONTAINER_CLASS CONTAINER_SLOT < <(python3 -c "
import sys
import datetime
from pathlib import Path
import yaml

sys.path.insert(0, '$REPO_ROOT/src/assets/scripts')
from utils.codeowners import load_codeowners, find_owner_org

with open('$RAW_SCHEMA_TMP', encoding='utf-8') as f:
    raw = f.read()
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
    # Kun store forbokstav per del (ikkje p.capitalize(), som lower-caser
    # resten av kvar del) — elles vert alt PascalCase/camelCase namn utan
    # '_'/'-' å splitte på (vanleg for JSON-schema-avleidde klassenamn, t.d.
    # 'MeldingForEttersendingAvVedlegg') mangla til éin lowercase del når
    # denne funksjonen vert brukt idempotent på alt som alt er korrekt kasa.
    parts = name.replace('_', '-').split('-')
    return ''.join(p[:1].upper() + p[1:] for p in parts if p)

classes = schema.get('classes') or {}
container_name = None
stub_names = []
for cname, cdef in classes.items():
    if cdef.get('tree_root'):
        container_name = cname
    else:
        stub_names.append(cname)

# PascalCase-ar alle ikkje-container-klassar. For --input-format empty er dette
# éin generisk stub-klasse; for --input-format json-schema er klassane som regel
# alt PascalCase (MCP-konverteraren kasar dei frå JSON Schema-definisjonsnamna),
# så steget er idempotent der og gjer ingenting.
for stub_name in list(stub_names):
    new_stub_name = to_pascal_case(stub_name)
    if new_stub_name != stub_name:
        classes[new_stub_name] = classes.pop(stub_name)
        if container_name:
            for slot_def in (classes[container_name].get('attributes') or {}).values():
                if slot_def.get('range') == stub_name:
                    slot_def['range'] = new_stub_name

# PascalCase-ar containerklassen sitt namn (t.d. 'generatedContainer' eller
# 'Enhetsregisteret_bvrContainer' → 'EnhetsregisteretBvrContainer'), i tråd med
# <Domene>Container-konvensjonen i CLAUDE.md.
if container_name:
    new_container_name = to_pascal_case(container_name)
    if new_container_name != container_name:
        classes[new_container_name] = classes.pop(container_name)
        container_name = new_container_name

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
    '- https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v$DCAT_AP_NO_VERSION/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema'
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
    if '$INPUT_FORMAT' == 'json-schema':
        f.write('# TODO: Gjennomgå klassenamn, skildringar og slot_uri — desse er generert frå JSON Schema og kan trenge justering.\n')
        f.write('# TODO: Erstatt generated:-prefikset i class_uri/slot_uri med eit reelt vokabular.\n')
    else:
        f.write('# TODO: Gi stub-klassen eit meir meiningsfullt namn.\n')
        f.write('# TODO: Legg til slots og slot_usage for eigenskapane i modellen.\n')

print(container_name or '${SCHEMA_NAME}Container', container_slot or '${SCHEMA_NAME}er')
")

echo ""
echo "Genererer eksempeldata frå skjemaet..."
# Monterer src/assets/scripts/utils/ slik at validator.py kan bruke
# linkml_relative_import_patch (BUG-15/bugs/relativ-import-via-versjonslast-url.md)
# — utan den feilar SchemaView på det versjonslåste dcat-ap-no-importet.
EXAMPLE_DATA=$(podman run -i --rm \
      -v "$LINKML_GEN_DIR/server.py:/app/server.py:ro" \
      -v "$LINKML_GEN_DIR/converter.py:/app/converter.py:ro" \
      -v "$LINKML_GEN_DIR/validator.py:/app/validator.py:ro" \
      -v "$LINKML_GEN_DIR/profiles:/app/profiles:ro" \
      -v "$REPO_ROOT/src/assets/scripts/utils:/app/utils:ro" \
      -v "$SCHEMA_FILE:/app/schema.yaml:ro" \
      "$LINKML_GEN_IMAGE" \
      python3 /app/validator.py /app/schema.yaml "${SCHEMA_NAME}:eksempel") || EXAMPLE_DATA=""

if [[ -z "$EXAMPLE_DATA" ]]; then
    echo "ÅTVARING: automatisk eksempelgenerering feila — skriv minimal stub i staden." >&2
    cat > "$EXAMPLE_FILE" << EOF
# Eksempel for $NAME
# Tilpass instansane med reelle verdiar etter at skjemaet er ferdigstilt.
---
$CONTAINER_SLOT:
  - id: ${SCHEMA_NAME}:eksempel-1
EOF
else
    {
        echo "# Eksempel for $NAME"
        echo "# Genererte placeholder-verdiar (dummy, 0, 2024-01-01 osv.) må erstattast med"
        echo "# reelle verdiar før modellen er produksjonsklar."
        echo "---"
        echo "$EXAMPLE_DATA"
    } > "$EXAMPLE_FILE"
fi

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

# Les valideringspolicy attende frå build.yaml (i staden for å hardkode
# han på nytt her) — held «Neste steg»-eksempelet synkronisert dersom
# build.yaml-malen over nokon gong endrar validation_policy-verdien.
VALIDATION_POLICY=$(python3 -c "import yaml; print(yaml.safe_load(open('$MANIFEST_FILE')).get('validation_policy', 'bronze'))")

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

cd "$REPO_ROOT"

# Sjekk at skjemaet ikkje kolliderer med namn frå importerte skjema (t.d.
# eit lokalt slot med same namn som eit slot i common-ap-no/dcat-ap-no) —
# sjå specs/done/oreg-scaffold-generering-feiler.md for kva som skjer om
# dette ikkje vert fanga her: seks generatorsteg feilar seinare i CI med
# ei kryptisk "Conflicting URIs"-feilmelding.
echo ""
echo "Sjekkar for namnekollisjonar mot importerte skjema..."
make --no-print-directory check-import-duplicates SCHEMA="$SCHEMA_FILE_REL"

# Lint det genererte skjemaet
echo ""
echo "Linter det genererte skjemaet..."
make --no-print-directory lint SCHEMA="$SCHEMA_FILE_REL"

echo ""
echo "Neste steg:"
if [[ "$INPUT_FORMAT" == "json-schema" ]]; then
    echo "  1. Gjennomgå genererte klassenamn, skildringar og slot_uri (sjå TODO-kommentarar i skjemafila)"
else
    echo "  1. Gi stub-klassen eit meir meiningsfullt namn og legg til eigenskapar"
fi
echo "  2. Byt common-ap-no-importet til ein reell AP-NO-profil ved behov (sjå TODO-kommentar i skjemafila)"
echo "  3. Fyll ut description.md med formål og kontekst (eller slett ho)"
echo "  4. Rett opp placeholder-verdiane i $EXAMPLE_FILE med reelle verdiar"
echo "  5. Valider: make mcp-linkml-valider-modell SCHEMA=$SCHEMA_FILE_REL POLICY=$VALIDATION_POLICY"
