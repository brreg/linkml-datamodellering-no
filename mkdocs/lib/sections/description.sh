#!/usr/bin/env bash
# Generer description.md-seksjon (seksjon 4 i index.md)
set -euo pipefail

generate_description() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet)
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    local description_file=""
    [ -n "$src_dir" ] && [ -f "$src_dir/description.md" ] && description_file="$src_dir/description.md"

    [ -z "$description_file" ] && return 0

    echo "## Om denne modellen"
    echo ""
    cat "$description_file"
    echo ""
    echo ""
    echo "---"
    echo ""
}
