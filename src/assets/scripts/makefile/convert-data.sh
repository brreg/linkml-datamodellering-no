#!/usr/bin/env bash
# Finn datafiler (src/linkml/**/data/*/*.yaml) som skal konverterast til
# RDF/Turtle med linkml-convert, filtrert mot `publish_external: true` i
# build.yaml. Analogt til convert-examples.sh, men for data-katalogar i
# staden for eksempelfiler.
#
# Skriv éi tab-separert linje per datafil som skal konverterast:
#   <skjema-sti>\t<datafil-sti>\t<output-ttl-sti>
# Køyrer discovery/filtrering FØR noko vert skrive til stdout, slik at éi
# log_debug-deloverskrift kan skrivast først — same mønster som
# convert-examples.sh.
#
# Bruk: convert-data.sh [domene]
# Miljøvariablar som må vere sette: SCHEMA_DIR, GEN_DIR, LOG_FUNCTIONS
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

: "${SCHEMA_DIR:?miljøvariabelen SCHEMA_DIR må vere sett}"
: "${GEN_DIR:?miljøvariabelen GEN_DIR må vere sett}"

eval "$LOG_FUNCTIONS"

domain_filter="${1:-}"
search_dir="$SCHEMA_DIR"
[ -n "$domain_filter" ] && search_dir="$SCHEMA_DIR/$domain_filter"

enabled=()
enabled_names=()
for datadir in $(find "$search_dir" -mindepth 4 -maxdepth 4 -type d -path '*/data/*' 2>/dev/null | sort); do
    domain=$(echo "$datadir" | awk -F/ '{print $3}')
    model=$(echo "$datadir" | awk -F/ '{print $4}')
    catalog=$(basename "$datadir")
    manifest="$datadir/build.yaml"
    [ -f "$manifest" ] || continue
    publish_external=$(grep '^publish_external:' "$manifest" | awk '{print $2}')
    [ "$publish_external" = "true" ] || continue
    datafile="$datadir/$catalog.yaml"
    [ -f "$datafile" ] || continue
    schema="$SCHEMA_DIR/$domain/$model/$model-schema.yaml"
    mkdir -p "$GEN_DIR/$domain/$catalog"
    out="$GEN_DIR/$domain/$catalog/$catalog.ttl"
    enabled+=("$(printf '%s\t%s\t%s' "$schema" "$datafile" "$out")")
    enabled_names+=("$catalog")
done

if [ "${#enabled_names[@]}" -gt 0 ]; then
    names=$(printf '%s, ' "${enabled_names[@]}")
    names=${names%, }
    names="${CLR_OK}${names}${CLR_RST}"
else
    names="(ingen)"
fi
log_debug "linkml-convert (publish_external: true) — køyrer: ${names}"

for entry in "${enabled[@]}"; do
    printf '%s\n' "$entry"
done
