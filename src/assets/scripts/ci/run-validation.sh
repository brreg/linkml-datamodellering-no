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
  # Bruk namnekonvensjonen (<modell>-schema.yaml = katalognamnet, sjå
  # CONVENTIONS.md) i staden for `find | head -n1` — katalogar med fleire
  # *-schema.yaml-filer (t.d. modelldcat-ap-no, dqv-ap-no) ga elles eit
  # vilkårleg val som ikkje samsvarte med kva generate.yml sitt kopisteg
  # forventar.
  schema_dir=$(dirname "$MANIFEST")
  schema_name=$(basename "$schema_dir")
  SCHEMA="$schema_dir/${schema_name}-schema.yaml"

  if [ ! -f "$SCHEMA" ]; then
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
# Eksempel:
#   src/linkml/samt/samt-bu/samt-bu-schema.yaml → domain=samt, model=samt-bu
#   src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml → domain=ngr, model=ngr-adresse
schema_dir=$(dirname "$SCHEMA")
model=$(basename "$schema_dir")

# Sjekk om schema_dir har tre nivå (linkml/<domain>/<modell>) eller to (linkml/<modell>)
parent_dir=$(dirname "$schema_dir")
parent_name=$(basename "$parent_dir")

if [ "$parent_name" = "linkml" ]; then
  # To-nivå-struktur: linkml/<modell> (skal ikkje skje lenger, men handter det)
  echo "Åtvaring: Schema ligg direkte under linkml/ utan domenenivå: $SCHEMA" >&2
  domain="$model"  # Bruk modellnamn som domain (fallback)
else
  # Tre-nivå-struktur: linkml/<domain>/<modell>
  domain="$parent_name"
fi

# Rekn ut loggsti (co-location)
log_path="$schema_dir/validation/$VERSION/$POLICY.json"

echo "→ Validerer $domain/$model (v$VERSION) med policy: $POLICY" >&2

# Køyr validering
# REPO_ROOT peikar til repo-root (scriptet ligg i src/assets/scripts/ci/, så gå 4 nivå opp)
REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "$0")/../../../.." && pwd)}"
FLATTEN_VALIDATE_SCRIPT="$REPO_ROOT/src/mcp-linkml-validator/flatten-and-validate.bash"

# Lag logg-katalog
mkdir -p "$(dirname "$log_path")"

# Køyr validering via flatten-and-validate.bash (handterer importar korrekt)
# Fang berre stdout (JSON-resultatet), lat stderr (logge-meldingar) gå til terminal
result_json=$(bash "$FLATTEN_VALIDATE_SCRIPT" "$SCHEMA" "$POLICY" "$INSTANCE")
exit_code=$?

# Bygg logg-objekt med metadata
python3 - "$SCHEMA" "$VERSION" "$POLICY" "$result_json" "$log_path" << 'PYEOF'
import json, sys, yaml
from datetime import datetime, timezone
from pathlib import Path

schema_path, version, policy, result_json, log_file = sys.argv[1:6]

# Parse result frå flatten-and-validate (kan vere JSON eller feilmelding)
try:
    result = json.loads(result_json)
except json.JSONDecodeError as e:
    print(f"[ERROR] Klarte ikkje parse resultat som JSON ({e}) — brukar rå tekst som feilmelding", file=sys.stderr)
    result = {"valid": False, "errorCount": 1, "warningCount": 0, "issues": [{"severity": "error", "message": result_json}]}

# Ekstraher metadata frå schema-sti
path_parts = Path(schema_path).parts
if len(path_parts) >= 4 and path_parts[0] == "src" and path_parts[1] == "linkml":
    domain = path_parts[2]
    schema_name = path_parts[3]
else:
    domain = ""
    schema_name = Path(schema_path).stem

log_data = {
    "schema": schema_name,
    "domain": domain,
    "version": version,
    "validation_policy": policy,
    "result": result,
}

Path(log_file).parent.mkdir(parents=True, exist_ok=True)
with open(log_file, "w", encoding="utf-8") as f:
    json.dump(log_data, f, indent=2, ensure_ascii=False, sort_keys=True)
PYEOF

if [ $exit_code -eq 0 ]; then
  echo "✓ Validering vellykka: $log_path" >&2
  exit 0
else
  echo "✗ Validering feila: sjå $log_path for detaljar" >&2
  exit 1
fi
