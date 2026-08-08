#!/usr/bin/env bash
# Orkestrer generering av index.md per skjema
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

# Source alle seksjonsgenererande funksjonar
SECTIONS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/sections" && pwd)"
for section_file in "$SECTIONS_DIR"/*.sh; do
    source "$section_file"
done

generate_schema_index() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$3"
    local out="$4"

    local gendoc_index="$schema_dir/docs/index.md"

    # Finn klasse-kjelde (index.md eller ${schema}.md)
    local klasse_src=""
    [ -f "$out/klasser/index.md" ] && klasse_src="$out/klasser/index.md"
    [ -z "$klasse_src" ] && [ -f "$out/klasser/${schema}.md" ] && klasse_src="$out/klasser/${schema}.md"

    # Sett miljøvariablar for seksjonsfunksjonar
    export CURRENT_DOMAIN="$domain"
    export CURRENT_SCHEMA="$schema"

    # Berekn importerte skjema éin gong (i staden for på nytt i kvar av dei
    # 5 Classes/Slots/Enumerations/Types/Subsets-seksjonane + éin gong til i
    # avhengigheiter-seksjonen — kvart kall spawnar python3 + gjer find).
    # Sjå specs/backlog/batch-docs-publish-generering.md.
    export IMPORTED_SCHEMAS_CACHE
    IMPORTED_SCHEMAS_CACHE=$(get_imported_schemas "$domain" "$schema")

    # Berekn build.yaml-felt (validation_policy, external_spec_url/label)
    # éin gong — same fil vert elles lest av opptil 5 separate python3-kall
    # spreidd over badges.sh/om_denne_modellen.sh/valideringsresultat.sh.
    load_manifest_cache "$REPO_ROOT/src/linkml/${domain}/${schema}/build.yaml"

    # Sjekk om dette er ein delmodell
    local is_submodel=false
    [ -n "${PARENT_MODEL:-}" ] && is_submodel=true

    {
        generate_header "$schema"
        generate_badges "$domain" "$schema" "$gendoc_index"

        # Hopp over description (som no også inneheld external_reference) for delmodellar
        if ! $is_submodel; then
            generate_description "$domain" "$schema"
        fi

        generate_quickstart "$domain" "$schema"
        generate_example "$domain" "$schema"
        generate_metadata "$gendoc_index"
        generate_submodel_box
        generate_dependencies "$domain" "$schema"
        generate_submodels_section
        generate_er_diagram "$schema" "$out"
        generate_datamodell "$domain" "$schema"
        generate_classes_section "$klasse_src"
        generate_artifacts_table "$out" "$schema"
        generate_validation_results "$domain" "$schema"
        generate_changelog "$domain" "$schema"
        generate_contact_info "$domain" "$schema"
    } > "$out/index.md"

    # Rydd opp miljøvariablar
    unset CURRENT_DOMAIN
    unset CURRENT_SCHEMA
    unset IMPORTED_SCHEMAS_CACHE
    unset MANIFEST_CACHE_PATH MANIFEST_CACHE_POLICY MANIFEST_CACHE_EXTERNAL_SPEC_URL MANIFEST_CACHE_EXTERNAL_SPEC_LABEL
}
