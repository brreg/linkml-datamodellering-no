#!/usr/bin/env bash
# Generer versjonslog-seksjon (seksjon 18 i index.md)
set -euo pipefail

generate_changelog() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet)
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    local changelog_src=""
    [ -n "$src_dir" ] && [ -f "$src_dir/CHANGELOG.md" ] && changelog_src="$src_dir/CHANGELOG.md"

    [ -z "$changelog_src" ] && return 0

    echo ""
    echo "---"
    echo ""
    echo "## Versjonslog"
    echo ""
    # Fjern hovudoverskrift "# Changelog" og auk nivået på alle andre overskrifter med éin #
    tail -n +1 "$changelog_src" | awk '
        NR==1 && /^# Changelog/ { next }
        /^##/ { print "#" $0; next }
        { print }
    '
    echo ""
}
