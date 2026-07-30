#!/usr/bin/env bash
# Generer klasseliste-seksjon (seksjon 11-15 i index.md: Classes, Slots, Enumerations, Types, Subsets)
set -euo pipefail

# Source imported_schemas utility
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/imported_schemas.sh"

# Hjelpefunksjon: Bygg lenkjeliste til importerte skjema
build_import_links() {
    local domain="$1"
    local schema="$2"
    local section="$3"  # classes, slots, enumerations, types, subsets
    local label="$4"    # "klasser", "slots", "enums", "typer", "subsets"

    # Hent importerte skjema
    local imported_schemas
    imported_schemas=$(get_imported_schemas "$domain" "$schema")
    [ -z "$imported_schemas" ] && return 0

    # Bygg lenkjeliste
    local links=""
    local linkml_types_link=""

    # Spesialbehandling for linkml:types (kun for Types-seksjonen, og først i lista)
    if [ "$section" = "types" ] && echo "$imported_schemas" | grep -q "^linkml:types$"; then
        local linkml_url="https://github.com/linkml/linkml-model/blob/main/linkml_model/model/schema/types.yaml"
        linkml_types_link="[linkml:types]($linkml_url)"
    fi

    # Map section til overskrift-format (Classes, Slots, Enumerations, Types, Subsets)
    local section_header
    case "$section" in
        classes) section_header="Classes" ;;
        slots) section_header="Slots" ;;
        enumerations) section_header="Enumerations" ;;
        types) section_header="Types" ;;
        subsets) section_header="Subsets" ;;
        *) section_header="" ;;
    esac

    while IFS= read -r imported; do
        [ -z "$imported" ] && continue

        # Hopp over linkml:types (handtert separat)
        if [ "$imported" = "linkml:types" ]; then
            continue
        fi

        # Parse domene/schema frå import-namn
        # imported kan vere t.d. "common-ap-no-schema", "dcat-ap-no-schema"
        # Fjern -schema-suffiks
        local imported_clean="${imported%-schema}"

        # Finn domene for importert skjema (søk i src/linkml/)
        local imported_file
        imported_file=$(find "$REPO_ROOT/src/linkml" -name "${imported_clean}-schema.yaml" -type f 2>/dev/null | head -1)
        [ -z "$imported_file" ] && continue

        # Trekk ut domene frå sti (src/linkml/<domain>/<dir>/<file>)
        # Bruk relative sti frå REPO_ROOT for å handtere både absolutte og relative stiar
        local rel_path="${imported_file#$REPO_ROOT/}"
        local imported_domain
        imported_domain=$(echo "$rel_path" | cut -d/ -f3)

        # Sjekk om den importerte modellen faktisk har lokale definisjoner i denne seksjonen
        local imported_index="$REPO_ROOT/generated/${imported_domain}/${imported_clean}/docs/index.md"
        if [ -f "$imported_index" ] && [ -n "$section_header" ]; then
            # Hent schema.id frå kjelde-YAML
            local schema_id
            schema_id=$(grep "^id:" "$imported_file" | head -1 | sed 's/^id: *//')

            # Ekstraher teljing frå header (t.d. "## Classes (17)" → 17)
            local count
            count=$(grep "^## ${section_header} (" "$imported_index" | sed -n 's/.*(\([0-9]*\)).*/\1/p')

            # Hopp over dersom teljing er 0
            if [ "$count" = "0" ]; then
                continue
            fi

            # For ikkje-null teljing: sjekk om det finst lokale definisjoner
            # Ekstraher seksjonen og sjekk "Defined in"-kolonna
            if [ -n "$count" ] && [ "$count" != "0" ]; then
                # Ekstraher tabellen for denne seksjonen (frå header til "---" eller EOF)
                local section_content
                section_content=$(grep -A 100 "^## ${section_header}" "$imported_index" | grep -B 100 -m 1 "^---" 2>/dev/null || grep -A 100 "^## ${section_header}" "$imported_index")

                # Sjekk om det finst minst ein rad der "Defined in" matcher schema.id
                # Tabellformat: | Name | Description | Defined in |
                local has_local
                has_local=$(echo "$section_content" | grep -F "[$schema_id]" || true)

                # Hopp over dersom ingen lokale definisjoner
                if [ -z "$has_local" ]; then
                    continue
                fi
            fi
        fi

        # Bygg relativ lenke
        local link
        if [ "$imported_domain" = "$domain" ]; then
            link="../${imported_clean}/#${section}"
        else
            link="../../${imported_domain}/${imported_clean}/#${section}"
        fi

        # Legg til lenke i lista
        if [ -z "$links" ]; then
            links="[$imported_clean]($link)"
        else
            links="$links, [$imported_clean]($link)"
        fi
    done <<< "$imported_schemas"

    # Sett saman linkml:types (først) og andre imports
    local final_links=""
    if [ -n "$linkml_types_link" ]; then
        final_links="$linkml_types_link"
        if [ -n "$links" ]; then
            final_links="$final_links, $links"
        fi
    else
        final_links="$links"
    fi

    # Output lenkjelinje
    if [ -n "$final_links" ]; then
        echo ""
        echo "*Importerte $label: $final_links*"
    fi
}

generate_classes_section() {
    local klasse_src="$1"

    [ -z "$klasse_src" ] || [ ! -f "$klasse_src" ] && return 0

    # Hent domain og schema frå kontekst (sett i generate_schema_index)
    local domain="${CURRENT_DOMAIN:-}"
    local schema="${CURRENT_SCHEMA:-}"

    echo "---"
    echo ""

    # Ekstraher Classes-seksjonen (frå "## Classes" til neste "##")
    # Beheld overskrifta med teljing frå gendoc og legg til stabilt anker {#classes}
    awk '/^## Classes/,/^## [^C]/' "$klasse_src" | sed '$d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g' | sed 's/^## Classes (\([0-9]*\))$/## Classes (\1) {#classes}/'
    build_import_links "$domain" "$schema" "classes" "klasser"
    echo ""
    echo ""

    # Ekstraher Slots-seksjonen
    if grep -q "^## Slots" "$klasse_src"; then
        awk '/^## Slots/,/^## [^S]/' "$klasse_src" | sed '$d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g' | sed 's/^## Slots (\([0-9]*\))$/## Slots (\1) {#slots}/'
        build_import_links "$domain" "$schema" "slots" "slots"
        echo ""
        echo ""
    fi

    # Ekstraher Enumerations-seksjonen
    if grep -q "^## Enumerations" "$klasse_src"; then
        awk '/^## Enumerations/,/^## [^E]/' "$klasse_src" | sed '$d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g' | sed 's/^## Enumerations (\([0-9]*\))$/## Enumerations (\1) {#enumerations}/'
        build_import_links "$domain" "$schema" "enumerations" "enums"
        echo ""
        echo ""
    fi

    # Ekstraher Types-seksjonen
    if grep -q "^## Types" "$klasse_src"; then
        awk '/^## Types/,/^## [^T]/' "$klasse_src" | sed '$d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g' | sed 's/^## Types (\([0-9]*\))$/## Types (\1) {#types}/'
        build_import_links "$domain" "$schema" "types" "typer"
        echo ""
        echo ""
    fi

    # Ekstraher Subsets-seksjonen (til slutt av fil, sidan Subsets er siste seksjon)
    if grep -q "^## Subsets" "$klasse_src"; then
        awk '/^## Subsets/,0' "$klasse_src" | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g' | sed 's/^## Subsets (\([0-9]*\))$/## Subsets (\1) {#subsets}/'
        build_import_links "$domain" "$schema" "subsets" "subsets"
    fi
}
