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
    local section="$3"  # classes, slots, enumerations, types
    local label="$4"    # "klasser", "slots", "enums", "typer"

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
    echo "## Classes"
    echo ""
    awk '/^## Classes$/,/^## [^C]/' "$klasse_src" | sed '1d;$d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g'
    build_import_links "$domain" "$schema" "classes" "klasser"
    echo ""
    echo ""

    # Ekstraher Slots-seksjonen
    if grep -q "^## Slots$" "$klasse_src"; then
        echo "## Slots"
        echo ""
        awk '/^## Slots$/,/^## [^S]/' "$klasse_src" | sed '1d;$d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g'
        build_import_links "$domain" "$schema" "slots" "slots"
        echo ""
        echo ""
    fi

    # Ekstraher Enumerations-seksjonen
    if grep -q "^## Enumerations$" "$klasse_src"; then
        echo "## Enumerations"
        echo ""
        awk '/^## Enumerations$/,/^## [^E]/' "$klasse_src" | sed '1d;$d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g'
        build_import_links "$domain" "$schema" "enumerations" "enums"
        echo ""
        echo ""
    fi

    # Ekstraher Types-seksjonen
    if grep -q "^## Types$" "$klasse_src"; then
        echo "## Types"
        echo ""
        awk '/^## Types$/,/^## [^T]/' "$klasse_src" | sed '1d;$d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g'
        build_import_links "$domain" "$schema" "types" "typer"
        echo ""
        echo ""
    fi

    # Ekstraher Subsets-seksjonen (utan import-lenkjer)
    if grep -q "^## Subsets$" "$klasse_src"; then
        echo "## Subsets"
        echo ""
        awk '/^## Subsets$/,0' "$klasse_src" | sed '1d' | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g'
    fi
}
