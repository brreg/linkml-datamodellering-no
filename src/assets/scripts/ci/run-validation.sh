#!/usr/bin/env bash
# Wrapper-script for validering av LinkML-skjema med logging til co-location-struktur.
#
# Bruk:
#   run-validation.sh --schema <path> --policy <policy>
#   run-validation.sh --manifest <path>
#   run-validation.sh --schema <path> --policy <policy> --instance <path>
#
# Eksempel:
#   run-validation.sh --schema src/linkml/samt/samt-bu/samt-bu-schema.yaml --policy silver
#   run-validation.sh --manifest src/linkml/samt/samt-bu/build.yaml

set -euo pipefail

# Standardverdiar
SCHEMA=""
POLICY=""
MANIFEST=""
INSTANCE=""

# Parse argument
while [[ $# -gt 0 ]]; do
  case $1 in
    --schema)
      SCHEMA="$2"
      shift 2
      ;;
    --policy)
      POLICY="$2"
      shift 2
      ;;
    --manifest)
      MANIFEST="$2"
      shift 2
      ;;
    --instance)
      INSTANCE="$2"
      shift 2
      ;;
    *)
      echo "Feil: Ukjent argument: $1" >&2
      echo "Bruk: $0 --schema <path> --policy <policy>" >&2
      echo "      $0 --manifest <path>" >&2
      exit 1
      ;;
  esac
done

# Manifest-modus: les policy og schema frå build.yaml
if [ -n "$MANIFEST" ]; then
  if [ ! -f "$MANIFEST" ]; then
    echo "Feil: build.yaml finst ikkje: $MANIFEST" >&2
    exit 1
  fi

  # Les validation_policy frå build.yaml (bruk Python i staden for yq)
  POLICY=$(python3 -c "import yaml; print(yaml.safe_load(open('$MANIFEST')).get('validation_policy', ''))" 2>/dev/null || echo "")

  # Valider at policy er sett
  if [ -z "$POLICY" ] || [ "$POLICY" = "None" ]; then
    echo "Feil: $MANIFEST manglar validation_policy-felt" >&2
    exit 1
  fi

  # Finn schema-sti frå manifest (same katalog som build.yaml)
  schema_dir=$(dirname "$MANIFEST")
  SCHEMA=$(find "$schema_dir" -maxdepth 1 -name "*-schema.yaml" | head -n1)

  if [ -z "$SCHEMA" ]; then
    echo "Feil: Fann ingen *-schema.yaml i $schema_dir" >&2
    exit 1
  fi
fi

# Valider at required argument er sette
if [ -z "$SCHEMA" ]; then
  echo "Feil: --schema eller --manifest må oppgjevast" >&2
  exit 1
fi

if [ -z "$POLICY" ]; then
  echo "Feil: --policy må oppgjevast (eller vere sett i build.yaml)" >&2
  exit 1
fi

if [ ! -f "$SCHEMA" ]; then
  echo "Feil: Schema-fil finst ikkje: $SCHEMA" >&2
  exit 1
fi

# Les version frå schema YAML (bruk Python i staden for yq)
VERSION=$(python3 -c "import yaml; v = yaml.safe_load(open('$SCHEMA')).get('version', ''); print(v if v else '')" 2>/dev/null || echo "")

if [ -z "$VERSION" ] || [ "$VERSION" = "null" ]; then
  echo "Feil: $SCHEMA manglar version:-felt" >&2
  exit 1
fi

# Finn domain og modell frå schema-sti
# Eksempel: src/linkml/samt/samt-bu/samt-bu-schema.yaml → samt, samt-bu
schema_dir=$(dirname "$SCHEMA")
model=$(basename "$schema_dir")
domain=$(basename "$(dirname "$schema_dir")")

# Rekn ut loggsti (co-location)
log_path="$schema_dir/validation/$VERSION/$POLICY.json"

echo "→ Validerer $domain/$model (v$VERSION) med policy: $POLICY" >&2

# Køyr validering
# REPO_ROOT for å finne validate-and-log.py og MCP-image
REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
VALIDATOR_SCRIPT="$REPO_ROOT/src/mcp-linkml-validator/validate-and-log.py"
MCP_IMAGE="${MCP_IMAGE:-mcp-linkml-validator}"

# Lag logg-katalog
mkdir -p "$(dirname "$log_path")"

# Bygg podman run-kommando
podman_args=(
  run --rm
  -v "$REPO_ROOT:/work"
  -w /work
  "$MCP_IMAGE"
  python3 /work/src/mcp-linkml-validator/validate-and-log.py
  --schema "/work/$SCHEMA"
  --policy "$POLICY"
  --log-file "/work/$log_path"
)

# Legg til --instance dersom spesifisert
if [ -n "$INSTANCE" ]; then
  if [ ! -f "$INSTANCE" ]; then
    echo "Feil: Instans-fil finst ikkje: $INSTANCE" >&2
    exit 1
  fi
  podman_args+=(--instance "/work/$INSTANCE")
fi

# Køyr validering
if podman "${podman_args[@]}"; then
  echo "✓ Validering vellykka: $log_path" >&2
  exit 0
else
  echo "✗ Validering feila: sjå $log_path for detaljar" >&2
  exit 1
fi
