#!/usr/bin/env bash
# Generer modellmetadata-tabell (seksjon 7 i index.md)
set -euo pipefail

generate_metadata() {
    local gendoc_index="$1"

    [ ! -f "$gendoc_index" ] && return 0

    echo "---"
    echo ""
    # Ekstraher frå "## Metadata" til neste "## "-seksjon (ikkje inkludert)
    # Endre overskrift til "Modellmetadata" for klarheit
    awk '/^## Metadata$/{ p=1; print "## Modellmetadata"; next } p{ if(/^## / && !/^## Metadata$/){ exit } print }' "$gendoc_index"
}
