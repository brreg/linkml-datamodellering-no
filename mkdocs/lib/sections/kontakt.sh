#!/usr/bin/env bash
# Generer kontaktinformasjon-seksjon (seksjon 19 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

source "$REPO_ROOT/mkdocs/lib/utils/imported_schemas.sh"

generate_contact_info() {
    local domain="$1"
    local schema="$2"

    echo ""
    echo "---"
    echo ""
    echo "## Kontakt"
    echo ""
    echo "> Her finn du informasjon om forvaltningsansvarleg, kontaktpunkt og kanal for feilrapportering eller forslag til forbetringar."
    echo ""

    # CODEOWNERS.md-matchinga (catalog_slug, deretter path_patterns) er
    # alt gjort éin gong for alle skjema i publish.sh Steg 1.5
    # (collect-schema-metadata.py) — slå opp resultatet i staden for å
    # gjere eit eige `podman run`-kall med same matching-logikk per
    # skjema. Sjå specs/backlog/reduser-podman-kall-docs-publish.md.
    local line name="" org_uri="" contact_uri=""
    if line=$(lookup_schema_metadata_line "$domain/$schema"); then
        local _key _policy _url _label _version _title _desc _ec _ev _qp _rest
        IFS=$'\x1f' read -r _key _policy _url _label _version _title _desc _ec _ev _qp name org_uri contact_uri _rest <<< "$line"
    fi

    if [ -n "$name" ]; then
        echo "**Forvaltningsansvarleg:** [$name]($org_uri)"
        echo ""
        if [ -n "$contact_uri" ]; then
            echo "**Kontakt:** [$name - Kontakt]($contact_uri)"
            echo ""
        fi
        echo "**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)"
    else
        # Fallback — ingen match funne
        echo "**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)"
    fi
    echo ""
}
