#!/usr/bin/env bash
# Generer artefaktabell (seksjon 16 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/formatters.sh"

# NOTE: ARTIFACT_ORDER er definert globalt i publish.sh og tilgjengeleg her via parent scope

generate_artifacts_table() {
    local out="$1"
    local schema="$2"
    local domain="${3:-${CURRENT_DOMAIN:-}}"

    local has_artifact=false
    local artifact_rows=""

    # Første rad: Modellmanifest ihht Modelldcat-ap-no
    local manifest_yaml="$out/${schema}-manifest.yaml"
    if [ -f "$manifest_yaml" ]; then
        has_artifact=true
        artifact_rows+="| Modellmanifest ihht Modelldcat-ap-no | [${schema}-manifest.yaml](${schema}-manifest.yaml) |"$'\n'
    fi

    for suffix in $ARTIFACT_ORDER; do
        local f="$out/${schema}-${suffix}"
        if [ -f "$f" ]; then
            has_artifact=true
            artifact_rows+="| $(artifact_label "$suffix") | [${schema}-${suffix}](${schema}-${suffix}) |"$'\n'
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

    # Java-klassar (ligg i java/-underkatalog, éin fil per klasse/enum)
    if [ -d "$out/java" ]; then
        local java_links="" java_file
        for java_file in "$out/java"/*.java; do
            [ -f "$java_file" ] || continue
            local base
            base=$(basename "$java_file")
            [ -n "$java_links" ] && java_links+=" · "
            java_links+="[${base}](java/${base})"
        done
        if [ -n "$java_links" ]; then
            has_artifact=true
            artifact_rows+="| Java-klassar | ${java_links} |"$'\n'
        fi
    fi


    if $has_artifact; then
        # Tel antal rader (antal linjeskift i artifact_rows)
        local artifact_count
        artifact_count=$(echo -n "$artifact_rows" | grep -c '^' || echo 0)

        echo ""
        echo "---"
        echo ""
        echo "## Genererte artefakter ($artifact_count) {#generated-artifacts}"
        echo ""
        echo "> Denne seksjonen listar maskinlesbare artefakt som er genererte frå skjemaet. Artefakta blir brukte til validering, integrasjon, dokumentasjon og kodegenerering."
        echo ""
        echo "| Artefakt | Fil |"
        echo "|----------|-----|"
        printf '%s' "$artifact_rows"
        if [ -n "$domain" ]; then
            # Delmodell-skjema ligg fysisk i FORELDRE-skjemaet sin katalog —
            # sjå tilsvarande kommentar i datamodell.sh.
            local source_dir="${PARENT_MODEL:-$schema}"
            echo ""
            echo "*Full byggekonfigurasjon: [build.yaml](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/$domain/$source_dir/build.yaml)*"
        fi
    fi
}
