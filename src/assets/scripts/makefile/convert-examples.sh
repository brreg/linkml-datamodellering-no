#!/usr/bin/env bash
# Finn eksempelfiler (src/linkml/**/examples/*-eksempel.yaml) som skal
# konverterast til RDF/Turtle med linkml-convert, filtrert mot
# `example_rdf: false` i build.yaml. Delt av `make convert-rdf` (Makefile,
# alle domene) og domain_target (make/20-domain-targets.mk, filtrert til
# eitt domene via $1) — sjå specs/done/forenkle-make-laget.md.
#
# Skriv éi tab-separert linje per eksempelfil som skal konverterast:
#   <skjema-sti>\t<eksempel-sti>\t<output-ttl-sti>
# Hoppa-over-eksempel vert samla til éi log_debug-linje (synleg berre på
# LOGLVL=DEBUG), same skip-mønster som run-parallel-gen.sh. Sjølve
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

skipped=()
for example in $(find "$search_dir" -path '*/examples/*-eksempel.yaml' 2>/dev/null | sort); do
    [ -f "$example" ] || continue
    name=$(basename "$example" .yaml)
    profil=$(echo "$name" | sed 's/-eksempel$//')
    domain=$(echo "$example" | awk -F/ '{print $3}')
    manifest="$SCHEMA_DIR/$domain/$profil/build.yaml"
    if [ -f "$manifest" ] && grep -q "^  example_rdf: false" "$manifest"; then
        skipped+=("$domain/$profil")
        continue
    fi
    mkdir -p "$GEN_DIR/$domain/$profil"
    if [ -f "tests/fixtures/$profil-fixture.yaml" ]; then
        schema="tests/fixtures/$profil-fixture.yaml"
    else
        schema="$SCHEMA_DIR/$domain/$profil/$profil-schema.yaml"
    fi
    out="$GEN_DIR/$domain/$profil/$name.ttl"
    printf '%s\t%s\t%s\n' "$schema" "$example" "$out"
done

if [ "${#skipped[@]}" -gt 0 ]; then
    skipped_list=$(printf '%s, ' "${skipped[@]}")
    skipped_list=${skipped_list%, }
    log_debug "  hoppar over linkml-convert (example_rdf: false): ${skipped_list}"
fi
