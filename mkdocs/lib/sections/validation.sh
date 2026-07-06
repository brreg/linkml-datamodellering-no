#!/usr/bin/env bash
# Generer valideringsresultat-seksjon (seksjon 17 i index.md)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/metadata_parsers.sh"

generate_validation_results() {
    local domain="$1"
    local schema="$2"
    local validation_json=$(get_validation_json_path "$domain" "$schema")

    echo ""
    echo "---"
    echo ""

    if [ -f "$validation_json" ]; then
        python3 "$REPO_ROOT/src/assets/scripts/generate-validation-md.py" "$validation_json"
    else
        echo "## Valideringsresultat"
        echo ""
        echo "*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*"
    fi
}
