#!/usr/bin/env bash
# Finn eksempelfiler (src/linkml/**/examples/*-eksempel.yaml) som skal
# konverterast til RDF/Turtle med linkml-convert, filtrert mot
# `example_rdf: false` i build.yaml. Delt av `make convert-rdf` (Makefile,
# alle domene) og domain_target (make/20-domain-targets.mk, filtrert til
# eitt domene via $1) — sjå specs/done/forenkle-make-laget.md.
#
# Skriv éi tab-separert linje per eksempelfil som skal konverterast:
#   <skjema-sti>\t<eksempel-sti>\t<output-ttl-sti>
# Køyrer discovery/filtrering FØR noko vert skrive til stdout, slik at éi
# log_debug-deloverskrift ("linkml-convert (example_rdf: true) — køyrer:
# …") kan skrivast først — same mønster og rekkjefølgje som
# run-parallel-gen.sh, synleg berre på LOGLVL=DEBUG. Sjølve
# linkml-convert-kallet gjer kallaren (ikkje dette scriptet), sidan det
# krev $(LINKML_RUN) sin podman-kontekst — den strengen inneheld sjølve
# anførselsteikn (frå WORK_MOUNT) som berre er trygge å la shellen tolke
# når dei kjem direkte frå ei Make-recipe-linje, ikkje via eit
# miljøvariabel-lag.
#
# Bruk: convert-examples.sh [domene]
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
for example in $(find "$search_dir" -path '*/examples/*-eksempel.yaml' 2>/dev/null | sort); do
    [ -f "$example" ] || continue
    name=$(basename "$example" .yaml)
    profil=$(echo "$name" | sed 's/-eksempel$//')
    domain=$(echo "$example" | awk -F/ '{print $3}')
    manifest="$SCHEMA_DIR/$domain/$profil/build.yaml"
    if [ -f "$manifest" ] && grep -q "^  example_rdf: false" "$manifest"; then
        continue
    fi
    mkdir -p "$GEN_DIR/$domain/$profil"
    if [ -f "tests/fixtures/$profil-fixture.yaml" ]; then
        schema="tests/fixtures/$profil-fixture.yaml"
    else
        schema="$SCHEMA_DIR/$domain/$profil/$profil-schema.yaml"
    fi
    out="$GEN_DIR/$domain/$profil/$name.ttl"
    enabled+=("$(printf '%s\t%s\t%s' "$schema" "$example" "$out")")
    enabled_names+=("$profil")
done

if [ "${#enabled_names[@]}" -gt 0 ]; then
    names=$(printf '%s, ' "${enabled_names[@]}")
    names=${names%, }
    names="${CLR_OK}${names}${CLR_RST}"
else
    names="(ingen)"
fi
log_debug "linkml-convert (example_rdf: true) — køyrer: ${names}"

for entry in "${enabled[@]}"; do
    printf '%s\n' "$entry"
done
