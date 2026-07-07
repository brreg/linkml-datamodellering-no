#!/usr/bin/env bash
# Generer delmodell-info (boksar for delmodell og liste for hovudmodell)
set -euo pipefail

# Generer "Delmodell av"-boks for delmodellar
generate_submodel_box() {
    local parent="${PARENT_MODEL:-}"

    [ -z "$parent" ] && return 0

    # Hent title frå hovudmodellen sitt skjema
    # Søk i alle mogelege plassar der hovudmodellen kan ligge:
    # 1. Same katalog som delmodellen (dqv-core og dqv-ap-no i same dqv-ap-no/)
    # 2. Separat katalog med same namn som hovudmodellen
    local parent_schema=""

    # Forsøk 1: søk alle *-schema.yaml-filer i domenet og finn den som heiter <parent>-schema.yaml
    parent_schema=$(find "$REPO_ROOT/src/linkml/${CURRENT_DOMAIN}" -name "${parent}-schema.yaml" -type f | head -1)

    # Forsøk 2: om ikkje funnen, søk i separat katalog (fallback)
    if [ -z "$parent_schema" ]; then
        local parent_dir="$REPO_ROOT/src/linkml/${CURRENT_DOMAIN}/${parent}"
        for candidate in "${parent_dir}"/*-schema.yaml; do
            [ -f "$candidate" ] && parent_schema="$candidate" && break
        done
    fi

    if [ -z "$parent_schema" ]; then
        echo "!!! info \"Delmodell\""
        echo "    Denne modellen er ein delmodell av **${parent}**."
        echo ""
        return 0
    fi

    local parent_title=$(python3 -c "import yaml; d=yaml.safe_load(open('$parent_schema')); print(d.get('title', d.get('name', '$parent')))" 2>/dev/null || echo "$parent")

    echo "!!! info \"Delmodell\""
    echo "    Denne modellen er ein delmodell av [${parent_title}](../${parent}/)."
    echo ""
}

# Generer "Delmodellar"-seksjon for hovudmodellar
generate_submodels_section() {
    local submodels="${SUBMODELS:-}"

    [ -z "$submodels" ] && return 0

    echo "---"
    echo ""
    echo "## Delmodellar"
    echo ""
    echo "Denne modellen er delt i fleire delmodellar:"
    echo ""

    for sub in $submodels; do
        # Hent title og description frå delmodell-skjemaet
        # Søk først i same katalog som hovudmodellen, deretter i underkatalogar
        local sub_schema=""
        sub_schema=$(find "$REPO_ROOT/src/linkml/${CURRENT_DOMAIN}" -name "${sub}-schema.yaml" -type f | head -1)

        if [ -z "$sub_schema" ] || [ ! -f "$sub_schema" ]; then
            echo "- **${sub}**"
            continue
        fi

        local sub_title=$(python3 -c "import yaml; d=yaml.safe_load(open('$sub_schema')); print(d.get('title', d.get('name', '$sub')))" 2>/dev/null || echo "$sub")
        local sub_desc=$(python3 -c "import yaml; d=yaml.safe_load(open('$sub_schema')); desc=d.get('description', ''); print(desc.split('.')[0] if desc else '')" 2>/dev/null || echo "")

        if [ -n "$sub_desc" ]; then
            # Fjern linjeskift og forkorta til første setning
            sub_desc=$(echo "$sub_desc" | tr '\n' ' ' | sed 's/\..*$//' | sed 's/^[[:space:]]*//')
            echo "- [${sub_title}](../${sub}/): ${sub_desc}"
        else
            echo "- [${sub_title}](../${sub}/)"
        fi
    done
    echo ""
}
