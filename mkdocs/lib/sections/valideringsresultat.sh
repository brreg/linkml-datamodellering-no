#!/usr/bin/env bash
# Generer valideringsresultat-seksjon (seksjon 17 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

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
        python3 "$REPO_ROOT/mkdocs/lib/scripts/generate-validation-md.py" "$validation_json" "$domain" "$schema"
    else
        echo "## Valideringsresultat"
        echo ""
        echo "> Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte."
        echo ""
        echo "*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*"
    fi
}
