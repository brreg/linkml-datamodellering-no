#!/usr/bin/env bash
# Generer versjonslog-seksjon (seksjon 18 i index.md)
set -euo pipefail

generate_changelog() {
    local domain="$1"
    local schema="$2"
    local changelog_src="$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"

    [ ! -f "$changelog_src" ] && return 0

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
