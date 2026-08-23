#!/usr/bin/env bash
# Generer modellanalyse-seksjon (seksjon 18 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/metadata_parsers.sh"

generate_modell_analyse() {
    local domain="$1"
    local schema="$2"
    local analyse_dir=$(get_model_analyse_dir "$domain" "$schema")

    echo ""
    echo "---"
    echo ""

    if [ -n "$analyse_dir" ]; then
        python3 "$REPO_ROOT/mkdocs/lib/scripts/generate-modellanalyse-md.py" "$analyse_dir" "$domain" "$schema"
    else
        echo "## Modellanalyse"
        echo ""
        echo "> Modellanalysen samanliknar dette skjemaet sine lokalt definerte klasse- og slotnamn mot andre skjema i same domene, og flaggar par med høg namnelikskap som eit mogleg duplikat- eller konsolideringssignal."
        echo ""
        echo "*Modellanalyse ikkje tilgjengeleg — krev at generate-workflowen har køyrt.*"
    fi
}
