#!/usr/bin/env bash
# Generer versjonslog-seksjon (seksjon 18 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

source "$REPO_ROOT/mkdocs/lib/utils/imported_schemas.sh"

generate_changelog() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet via det pre-berekna oppslaget frå
    # Steg 1.5 — sjå specs/backlog/batch-docs-publish-generering.md
    local schema_file
    schema_file=$(lookup_schema_path "${schema}-schema") || schema_file=""
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
    echo "> Versjonsloggen viser endringar mellom publiserte versjonar av modellen. Innhaldet blir generert frå prosjektets release-historikk."
    echo ""
    # Fjern hovudoverskrift "# Changelog" og auk nivået på alle andre overskrifter med éin #
    tail -n +1 "$changelog_src" | awk '
        NR==1 && /^# Changelog/ { next }
        /^##/ { print "#" $0; next }
        { print }
    '
    echo ""
}
