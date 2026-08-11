#!/usr/bin/env bash
# Generer avhengigheitstre (seksjon 9 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

# Source imported_schemas utility
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/imported_schemas.sh"

# Hjelpefunksjon: Bygg lenkjeliste til importerte modeller
build_imported_models_links() {
    local domain="$1"
    local schema="$2"

    # Bruk memoisert resultat frå generate_schema_index() i staden for å
    # kalle get_imported_schemas() på nytt (sjå
    # specs/backlog/batch-docs-publish-generering.md)
    local imported_schemas="${IMPORTED_SCHEMAS_CACHE:-}"
    [ -z "$imported_schemas" ] && return 0

    # Bygg lenkjeliste
    local links=""
    local linkml_types_link=""

    # Spesialbehandling for linkml:types (GitHub-lenke, først i lista)
    if echo "$imported_schemas" | grep -q "^linkml:types$"; then
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

        # Slå opp domene for importert skjema via føre-berekna oppslag
        # (publish.sh Steg 1.5) i staden for whole-tree find
        local imported_domain
        imported_domain=$(lookup_schema_domain "$imported") || continue

        # Bygg relativ lenke til #datamodell-ankeret
        local link
        if [ "$imported_domain" = "$domain" ]; then
            link="../${imported_clean}/#datamodell"
        else
            link="../../${imported_domain}/${imported_clean}/#datamodell"
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
        echo "*Importerte modeller: $final_links*"
    fi
}

generate_dependencies() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet via det pre-berekna oppslaget frå
    # Steg 1.5 — sjå specs/backlog/batch-docs-publish-generering.md
    local schema_file
    schema_file=$(lookup_schema_path "${schema}-schema") || schema_file=""
    local schema_path=""
    [ -n "$schema_file" ] && schema_path="$schema_file"

    # Parse direkte importar frå dette skjemaet
    local imports=""
    local direct_imports_normalized=""
    if [ -f "$schema_path" ]; then
        # Behald -schema-suffiks (ikkje strip det)
        imports=$(sed -n '/^imports:/,/^[a-z_]/p' "$schema_path" | grep -E "^[ ]*- " | sed 's/^[ ]*- //' | sed 's|^\.\./\.\./||' | sed 's|^\.\./||')
        # Normaliser til skjemanamn (basename) for direkte-import-matching
        direct_imports_normalized=$(echo "$imports" | tr ' ' '\n' | xargs -I {} basename {} | tr '\n' ' ')
    fi

    # Output (hierarkisk tre med transitive avhengigheiter)
    if [ -n "$imports" ]; then
        # Bygg dependency tree og tel antal imports
        local dep_tree
        dep_tree=$(python3 "$REPO_ROOT/mkdocs/lib/scripts/parse-dependency-tree.py" "$schema" "$imports" "$direct_imports_normalized")
        local import_count
        import_count=$(echo "$dep_tree" | grep -c '^' || echo 0)

        echo "---"
        echo ""
        echo "## Avhengigheiter ($import_count) {#avhengigheiter}"
        echo ""
        echo "> Denne modellen importerer og gjenbruker komponentar frå andre skjema. "
        echo "> Importerte klassar og eigenskapar kan vere synlege i diagram, valideringsrapportar og andre analysar sjølv om dei ikkje blir lista som lokale element i denne modellen."
        echo ""
        echo "Dette skjemaet importerer følgjande skjema (direkte og transitivt):"
        echo ""
        echo "\`\`\`"
        echo "$dep_tree"
        echo "\`\`\`"
        echo ""
        echo "*Sjå [Importhierarki](../../arkitektur/importhierarki.md) for oversikt over heile repoet sitt importhierarki.*"
        build_imported_models_links "$domain" "$schema"
        echo ""
        echo ""
    fi
}
