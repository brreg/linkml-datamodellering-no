#!/usr/bin/env bash
# Generer hovudoverskrift (seksjon 1 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

generate_header() {
    local schema="$1"
    echo "# $schema"
    echo ""
}
