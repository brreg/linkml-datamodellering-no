#!/usr/bin/env bash
# Orkestrer generering av index.md per skjema
set -euo pipefail

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

    # Sjekk om dette er ein delmodell
    local is_submodel=false
    [ -n "${PARENT_MODEL:-}" ] && is_submodel=true

    {
        generate_header "$schema"
        generate_badges "$domain" "$schema" "$gendoc_index"

        # Hopp over external_reference og description for delmodellar
        if ! $is_submodel; then
            generate_external_reference "$domain" "$schema"
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
}
