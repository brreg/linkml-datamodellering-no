#!/usr/bin/env bash
# Generer hovudoverskrift (seksjon 1 i index.md)
set -euo pipefail

generate_header() {
    local schema="$1"
    echo "# $schema"
    echo ""
}
