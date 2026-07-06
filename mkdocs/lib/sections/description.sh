#!/usr/bin/env bash
# Generer description.md-seksjon (seksjon 4 i index.md)
set -euo pipefail

generate_description() {
    local domain="$1"
    local schema="$2"
    local description_file="$REPO_ROOT/src/linkml/$domain/$schema/description.md"

    [ ! -f "$description_file" ] && return 0

    cat "$description_file"
    echo ""
    echo ""
}
