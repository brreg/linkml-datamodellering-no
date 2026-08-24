#!/usr/bin/env bash
# Hent flat liste av alle importerte skjema (direkte og transitivt)
set -euo pipefail

# Slå opp domenet eit skjemanavn (t.d. "dcat-ap-no-schema") høyrer til, via
# det føre-berekna oppslaget frå publish.sh Steg 1.5
# (SCHEMA_NAME_TO_DOMAIN_SERIALIZED). Erstattar whole-tree `find`-kall som
# tidlegare fanst duplisert i både classes.sh og avhengigheiter.sh — sjå
# specs/backlog/batch-docs-publish-generering.md.
lookup_schema_domain() {
    local schema_name="$1"
    local entry key val
    for entry in $SCHEMA_NAME_TO_DOMAIN_SERIALIZED; do
        key="${entry%%=*}"
        val="${entry#*=}"
        if [ "$key" = "$schema_name" ]; then
            echo "$val"
            return 0
        fi
    done
    return 1
}

# Slå opp full filsti for eit skjemanavn via same føre-berekna oppslag.
# Nødvendig i tillegg til lookup_schema_domain(), sidan delmodell-skjema
# (t.d. dqv-core-schema.yaml) ligg i foreldreskjemaet sin katalog — stien
# kan difor IKKJE rekonstruerast frå domene+navn åleine.
lookup_schema_path() {
    local schema_name="$1"
    local entry key val
    for entry in $SCHEMA_NAME_TO_PATH_SERIALIZED; do
        key="${entry%%=*}"
        val="${entry#*=}"
        if [ "$key" = "$schema_name" ]; then
            echo "$val"
            return 0
        fi
    done
    return 1
}

# Slå opp den samla metadata-lina (policy, versjon, tittel, quickstart,
# CODEOWNERS-oppslag osv.) for eit domain/schema-par frå det pre-berekna
# SCHEMA_METADATA_SERIALIZED-registeret (bygd i publish.sh Steg 1.5 via
# collect-schema-metadata.py — EIN containerprosess for alle skjema, i
# staden for opptil 5 separate `podman run`-kall per skjema. Sjå
# specs/backlog/reduser-podman-kall-docs-publish.md).
# Feltrekkjefølgje (skilt med \x1f): domain/schema, policy,
# external_spec_url, external_spec_label, version, title, description,
# example_class, example_var, quickstart_policy, codeowners_name,
# codeowners_org_uri, codeowners_contact_uri.
lookup_schema_metadata_line() {
    local key="$1"
    local line
    while IFS= read -r line; do
        case "$line" in
            "$key"$'\x1f'*) printf '%s\n' "$line"; return 0 ;;
        esac
    done <<< "$SCHEMA_METADATA_SERIALIZED"
    return 1
}

# Slå opp organisasjonsnavn for ein org_uri frå det pre-berekna
# ORG_URI_TO_NAME_SERIALIZED-registeret (CODEOWNERS.md, parsa éin gong i
# same container-kall som over).
lookup_org_name() {
    local org_uri="$1"
    local uri name
    while IFS=$'\x1f' read -r uri name; do
        [ "$uri" = "$org_uri" ] && printf '%s\n' "$name" && return 0
    done <<< "$ORG_URI_TO_NAME_SERIALIZED"
    return 1
}

get_imported_schemas() {
    local domain="$1"
    local schema="$2"

    # Finn schema-fil via det pre-berekna oppslaget (Steg 1.5) i staden
    # for eit eige find-kall — sjå specs/backlog/batch-docs-publish-generering.md
    local schema_file
    schema_file=$(lookup_schema_path "${schema}-schema") || return 0
    [ -z "$schema_file" ] && return 0

    # Parse direkte importar
    local imports
    imports=$(sed -n '/^imports:/,/^[a-z_]/p' "$schema_file" | grep -E "^[ ]*- " | sed 's/^[ ]*- //' | sed 's|^\.\./\.\./||' | sed 's|^\.\./||')
    [ -z "$imports" ] && return 0

    # Kall parse-dependency-tree.py med --format flat
    python3 "$REPO_ROOT/mkdocs/lib/scripts/parse-dependency-tree.py" --format flat "$schema" "$imports"
}
