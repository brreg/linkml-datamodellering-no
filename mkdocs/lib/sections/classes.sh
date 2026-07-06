#!/usr/bin/env bash
# Generer klasseliste-seksjon (seksjon 11-15 i index.md: Classes, Slots, Enumerations, Types, Subsets)
set -euo pipefail

generate_classes_section() {
    local klasse_src="$1"

    [ -z "$klasse_src" ] || [ ! -f "$klasse_src" ] && return 0

    echo "---"
    echo ""
    # Ekstraher frå "## Classes" til slutten (hoppar over Metadata og Schema Diagram)
    awk '/^## Classes$/,0' "$klasse_src" \
        | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g'
}
