#!/usr/bin/env bash
# Generer artefaktabell (seksjon 16 i index.md)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/formatters.sh"

# NOTE: ARTIFACT_ORDER er definert globalt i publish.sh og tilgjengeleg her via parent scope

generate_artifacts_table() {
    local out="$1"
    local schema="$2"

    local has_artifact=false
    local artifact_rows=""

    # Første rad: Modellmanifest ihht Modelldcat-ap-no
    local manifest_yaml="$out/${schema}-manifest.yaml"
    if [ -f "$manifest_yaml" ]; then
        has_artifact=true
        artifact_rows+="| Modellmanifest ihht Modelldcat-ap-no | [\`${schema}-manifest.yaml\`](${schema}-manifest.yaml) |"$'\n'
    fi

    for suffix in $ARTIFACT_ORDER; do
        local f="$out/${schema}-${suffix}"
        if [ -f "$f" ]; then
            has_artifact=true
            artifact_rows+="| $(artifact_label "$suffix") | [\`${schema}-${suffix}\`](${schema}-${suffix}) |"$'\n'
        fi
    done

    # PlantUML-diagram (ligg i diagrams/-underkatalog)
    # Prioriter filtrert versjon (kun domenemodell) over full versjon
    local puml_svg_filtered="$out/diagrams/${schema}-filtered.svg"
    local puml_src_filtered="$out/diagrams/${schema}-filtered.puml"
    local puml_svg_full="$out/diagrams/${schema}.svg"
    local puml_src_full="$out/diagrams/${schema}.puml"

    if [ -f "$puml_svg_filtered" ] || [ -f "$puml_src_filtered" ] || [ -f "$puml_svg_full" ] || [ -f "$puml_src_full" ]; then
        has_artifact=true
        local puml_links=""
        # Vis filtrert versjon først (hovuddiagram)
        if [ -f "$puml_svg_filtered" ]; then
            puml_links="[${schema}-filtered.svg](diagrams/${schema}-filtered.svg)"
        elif [ -f "$puml_svg_full" ]; then
            puml_links="[${schema}.svg](diagrams/${schema}.svg)"
        fi
        # Legg til puml-kjeldekode
        if [ -f "$puml_src_filtered" ]; then
            [ -n "$puml_links" ] && puml_links+=" · "
            puml_links+="[${schema}-filtered.puml](diagrams/${schema}-filtered.puml)"
        fi
        if [ -f "$puml_src_full" ]; then
            [ -n "$puml_links" ] && puml_links+=" · "
            puml_links+="[${schema}.puml](diagrams/${schema}.puml) (full)"
        fi
        artifact_rows+="| PlantUML-diagram | ${puml_links} |"$'\n'
    fi


    if $has_artifact; then
        echo ""
        echo "---"
        echo ""
        echo "## Generated artifacts"
        echo ""
        echo "| Artefakt | Fil |"
        echo "|----------|-----|"
        printf '%s' "$artifact_rows"
    fi
}
