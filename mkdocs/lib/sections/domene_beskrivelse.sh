#!/usr/bin/env bash
# Generer domene-skildring for domenet sin index.md (før modell-tabellen)
# Inneheld: src/linkml/<domain>/description.md (dersom den finst)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

generate_domain_description() {
    local domain="$1"

    local description_file="$REPO_ROOT/src/linkml/$domain/description.md"
    [ -f "$description_file" ] || return 0

    cat "$description_file"
    echo ""
}
