#!/usr/bin/env bash
# Hent flat liste av alle importerte skjema (direkte og transitivt)
set -euo pipefail

get_imported_schemas() {
    local domain="$1"
    local schema="$2"

    # Finn schema-fil
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    [ -z "$schema_file" ] && return 0

    # Parse direkte importar
    local imports
    imports=$(sed -n '/^imports:/,/^[a-z_]/p' "$schema_file" | grep -E "^[ ]*- " | sed 's/^[ ]*- //' | sed 's|^\.\./\.\./||' | sed 's|^\.\./||')
    [ -z "$imports" ] && return 0

    # Kall parse-dependency-tree.py med --format flat
    python3 "$REPO_ROOT/src/assets/scripts/parse-dependency-tree.py" --format flat "$schema" "$imports"
}
