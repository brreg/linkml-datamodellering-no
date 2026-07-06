#!/usr/bin/env bash
# Generer ekstern referanse-boks (seksjon 3 i index.md)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/metadata_parsers.sh"

generate_external_reference() {
    local domain="$1"
    local schema="$2"
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/manifest.yaml"
    local external_spec=$(get_external_spec_url "$manifest")

    [ -z "$external_spec" ] && return 0

    echo "---"
    echo ""
    echo "!!! info \"Offisiell referanse\""
    echo "    📘 [$schema-spesifikasjonen]($external_spec) frå Digitaliseringsdirektoratet"
    echo ""
}
