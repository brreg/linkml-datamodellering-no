#!/usr/bin/env bash
# Generer "Om denne modellen"-seksjon (tidlegare seksjon 4 i index.md)
# Inneheld: offisiell referanse (dersom den finst) + description.md (dersom den finst)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/metadata_parsers.sh"

generate_description() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet via det pre-berekna oppslaget frå
    # Steg 1.5 — sjå specs/backlog/batch-docs-publish-generering.md
    local schema_file
    schema_file=$(lookup_schema_path "${schema}-schema") || schema_file=""
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    local description_file=""
    [ -n "$src_dir" ] && [ -f "$src_dir/description.md" ] && description_file="$src_dir/description.md"

    # Hent offisiell referanse
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/build.yaml"
    local external_spec=$(get_external_spec_url "$manifest")
    local external_label=""
    if [ -n "$external_spec" ]; then
        external_label=$(get_external_spec_label "$manifest")
        [ -z "$external_label" ] && external_label="$schema"  # Fallback til skjemanavn
    fi

    # Vis seksjonen dersom vi har referanse ELLER description.md
    [ -z "$external_spec" ] && [ -z "$description_file" ] && return 0

    echo "## Om denne modellen"
    echo ""

    # Vis standard ingress
    echo "> Denne sida dokumenterer LinkML-modellen $schema, inkludert klassar, eigenskapar, datatypar, valideringsresultat og genererte artefakter. Informasjonen er generert automatisk frå skjemaet og tilhøyrande byggeproses."
    echo ""

    # Vis offisiell referanse etter ingress (dersom den finst)
    if [ -n "$external_spec" ]; then
        echo "**Offisiell referanse:** [$external_label]($external_spec)"
        echo ""
    fi

    # Vis description.md-innhald (dersom det finst)
    if [ -n "$description_file" ]; then
        cat "$description_file"
        echo ""
    fi

    echo ""
    echo "---"
    echo ""
}
