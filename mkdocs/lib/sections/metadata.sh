#!/usr/bin/env bash
# Generer modellmetadata-tabell (seksjon 7 i index.md)
set -euo pipefail

generate_metadata() {
    local gendoc_index="$1"

    [ ! -f "$gendoc_index" ] && return 0

    echo "---"
    echo ""
    # Ekstraher frå "## Modellmetadata" til neste "## "-seksjon (ikkje inkludert)
    # Legg til {#metadata}-anker i overskrifta
    awk '/^## Modellmetadata( \{#metadata\})?$/{ p=1; print "## Modellmetadata {#metadata}"; next } p{ if(/^## / && !/^## Modellmetadata( \{#metadata\})?$/){ exit } print }' "$gendoc_index"
}
