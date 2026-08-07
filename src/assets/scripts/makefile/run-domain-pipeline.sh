#!/usr/bin/env bash
# Orkestrerer domain_target sin genereringspipeline med fase-medviten
# parallellisering mellom uavhengige batch-grupper — sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md,
# «Parallellisering etter batching».
#
# Kvart steg er eit rekursivt $(MAKE) <target> DOMAIN=<domene>-kall til eit
# alt eksisterande, sjølvstendig verifisert gen-*-target (batch-generate.py/
# batch-generate-instances.py/run-parallel-gen.sh gjer sjølve genererings-
# arbeidet, uendra) — dette scriptet reimplementerer ingen podman- eller
# genereringslogikk, berre fase-rekkjefølgje, samstundes-oppstart og
# feilsamling (PID-array + wait, same mønster som
# parallelliser-domene-validering.md).
#
# Fase 1 (samstundes): alle grupper utan innbyrdes avhengigheit, inkl.
#   gen-jsonschema sjølv (fase 2 ventar spesifikt på henne, ikkje på resten
#   av fase 1).
# Fase 2 (samstundes, ventar på gen-jsonschema): gen-xsd/gen-openapi/
#   gen-asyncapi les alle <name>-schema.json.
# Fase 3 (ventar på ALT frå fase 1+2): gen-informasjonsmodell-instance sin
#   discover_artifacts() skannar heile generated/<domain>/<name>/ for
#   finnes_i_format-lista, og må difor køyre sist.
#
# Bruk: run-domain-pipeline.sh <domene>
# Miljøvariablar som må vere sette: MAKE, GEN_DIR, LOG_FUNCTIONS
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

: "${MAKE:?miljøvariabelen MAKE må vere sett}"
: "${GEN_DIR:?miljøvariabelen GEN_DIR må vere sett}"

domain="$1"

eval "$LOG_FUNCTIONS"

declare -A PIDS
FAILED=0

run_bg() {
    local key="$1"; shift
    ( "$@" ) &
    PIDS[$key]=$!
}

wait_job() {
    local key="$1"
    if ! wait "${PIDS[$key]}"; then
        log_error "::error::domain-${domain}/${key} feila"
        FAILED=$((FAILED + 1))
    fi
    unset "PIDS[$key]"
}

# --- Fase 1 — uavhengige grupper, inkl. gen-jsonschema ---------------------
run_bg merge          "$MAKE" gen-linkml-merge DOMAIN="$domain"
run_bg jsonld-context "$MAKE" gen-jsonld-context DOMAIN="$domain"
run_bg shacl          "$MAKE" gen-shacl DOMAIN="$domain"
run_bg python         "$MAKE" gen-python DOMAIN="$domain"
run_bg json-schema    "$MAKE" gen-jsonschema DOMAIN="$domain"
run_bg owl            "$MAKE" gen-owl DOMAIN="$domain"
run_bg rdf            "$MAKE" gen-rdf DOMAIN="$domain"
run_bg proto          "$MAKE" gen-proto DOMAIN="$domain"
run_bg linkml-convert "$MAKE" gen-linkml-convert DOMAIN="$domain"
run_bg docs           "$MAKE" gen-docs DOMAIN="$domain"
run_bg plantuml       "$MAKE" gen-plantuml DOMAIN="$domain"

# Fase 2 avheng berre av gen-jsonschema (ikkje resten av fase 1) — vent på
# nøyaktig den eine jobben, la dei andre halde fram i bakgrunnen.
wait_job json-schema

# --- Fase 2 — treng gen-jsonschema sitt output ------------------------------
run_bg xsd      "$MAKE" gen-xsd DOMAIN="$domain"
run_bg openapi  "$MAKE" gen-openapi DOMAIN="$domain"
run_bg asyncapi "$MAKE" gen-asyncapi DOMAIN="$domain"

# Vent på resten av fase 1 + heile fase 2.
for key in "${!PIDS[@]}"; do
    wait_job "$key"
done

if [ "$FAILED" -gt 0 ]; then
    log_error "::error::domain-${domain}: $FAILED gruppe(r) feila — stoppar før gen-informasjonsmodell-instance"
    exit 1
fi

# --- Fase 3 — treng ALT (finnes_i_format-lista skannar heile generated/) ---
"$MAKE" gen-informasjonsmodell-instance DOMAIN="$domain"
