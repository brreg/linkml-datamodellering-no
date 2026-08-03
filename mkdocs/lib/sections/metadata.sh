#!/usr/bin/env bash
# Generer modellmetadata-tabell (seksjon 7 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

generate_metadata() {
    local gendoc_index="$1"

    [ ! -f "$gendoc_index" ] && return 0

    echo "---"
    echo ""
    # Ekstraher frå "## Modellmetadata" til neste "##" eller "###"-seksjon (ikkje inkludert)
    # Legg til {#metadata}-anker i overskrifta
    awk '/^## Modellmetadata( \{#metadata\})?$/{ p=1; print "## Modellmetadata {#metadata}"; next } p{ if(/^###? / && !/^## Modellmetadata( \{#metadata\})?$/){ exit } print }' "$gendoc_index"
}
