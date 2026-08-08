#!/usr/bin/env bash
# Hent flat liste av alle importerte skjema (direkte og transitivt)
set -euo pipefail

# Slå opp domenet eit skjemanamn (t.d. "dcat-ap-no-schema") høyrer til, via
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

# Slå opp full filsti for eit skjemanamn via same føre-berekna oppslag.
# Nødvendig i tillegg til lookup_schema_domain(), sidan delmodell-skjema
# (t.d. dqv-core-schema.yaml) ligg i foreldreskjemaet sin katalog — stien
# kan difor IKKJE rekonstruerast frå domene+namn åleine.
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

get_imported_schemas() {
    local domain="$1"
    local schema="$2"

    # Finn schema-fil
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    [ -z "$schema_file" ] && return 0

    # Parse direkte importar
    local imports
    imports=$(sed -n '/^imports:/,/^[a-z_]/p' "$schema_file" | grep -E "^[ ]*- " | sed 's/^[ ]*- //' | sed 's|^\.\./\.\./||' | sed 's|^\.\./||')
    [ -z "$imports" ] && return 0

    # Kall parse-dependency-tree.py med --format flat
    python3 "$REPO_ROOT/mkdocs/lib/scripts/parse-dependency-tree.py" --format flat "$schema" "$imports"
}
