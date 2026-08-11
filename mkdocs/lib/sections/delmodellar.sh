#!/usr/bin/env bash
# Generer delmodell-info (boksar for delmodell og liste for hovudmodell)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

source "$REPO_ROOT/mkdocs/lib/utils/imported_schemas.sh"

# Generer "Delmodell av"-boks for delmodellar
generate_submodel_box() {
    local parent="${PARENT_MODEL:-}"

    [ -z "$parent" ] && return 0

    # Title for hovudmodellen hentast frå det pre-berekna
    # SCHEMA_METADATA_SERIALIZED-registeret (Steg 1.5) i staden for eit
    # eige find+podman-kall — sjå
    # specs/backlog/reduser-podman-kall-docs-publish.md. "Ikkje i
    # registeret" (lookup feilar) tilsvarar "parent_schema ikkje funnen"
    # før — same rå-tekst-fallback (utan lenke).
    local line
    if ! line=$(lookup_schema_metadata_line "$CURRENT_DOMAIN/$parent"); then
        echo "!!! info \"Delmodell\""
        echo "    Denne modellen er ein delmodell av **${parent}**."
        echo ""
        return 0
    fi

    local _key _policy _url _label _version parent_title _desc _ec _ev _qp _rest
    IFS=$'\x1f' read -r _key _policy _url _label _version parent_title _desc _ec _ev _qp _rest <<< "$line"
    [ -z "$parent_title" ] && parent_title="$parent"

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
        # Title/description for kvar delmodell hentast frå det
        # pre-berekna SCHEMA_METADATA_SERIALIZED-registeret — sjå
        # specs/backlog/reduser-podman-kall-docs-publish.md.
        local line
        if ! line=$(lookup_schema_metadata_line "$CURRENT_DOMAIN/$sub"); then
            echo "- **${sub}**"
            continue
        fi

        local _key _policy _url _label _version sub_title sub_desc _ec _ev _qp _rest
        IFS=$'\x1f' read -r _key _policy _url _label _version sub_title sub_desc _ec _ev _qp _rest <<< "$line"
        [ -z "$sub_title" ] && sub_title="$sub"

        if [ -n "$sub_desc" ]; then
            # Fjern linjeskift og forkorta til første setning (description
            # er alt kutta ved fyrste '.' i collect-schema-metadata.py —
            # sed-en her er ein uskadeleg no-op, behalden for å matche
            # den pre-eksisterande, dobbelt-kutta åtferda byte-for-byte)
            sub_desc=$(echo "$sub_desc" | tr '\n' ' ' | sed 's/\..*$//' | sed 's/^[[:space:]]*//')
            echo "- [${sub_title}](../${sub}/): ${sub_desc}"
        else
            echo "- [${sub_title}](../${sub}/)"
        fi
    done
    echo ""
}
