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

# --no-print-directory: utan dette skrur GNU Make automatisk på
# "Entering/Leaving directory"-meldingar for sub-make-kall som oppdagar dei
# køyrer under ein annan make (MAKELEVEL > 0) — rein støy her, sidan kvart
# steg alt har si eiga print_header-deloverskrift (sjå
# specs/done/gjenopprett-debug-logging-fjern-make-directory-stoy.md).

# --- Fase 1 — uavhengige grupper, inkl. gen-jsonschema ---------------------
run_bg merge          "$MAKE" --no-print-directory gen-linkml-merge DOMAIN="$domain"
run_bg jsonld-context "$MAKE" --no-print-directory gen-jsonld-context DOMAIN="$domain"
run_bg shacl          "$MAKE" --no-print-directory gen-shacl DOMAIN="$domain"
run_bg python         "$MAKE" --no-print-directory gen-python DOMAIN="$domain"
run_bg json-schema    "$MAKE" --no-print-directory gen-jsonschema DOMAIN="$domain"
run_bg owl            "$MAKE" --no-print-directory gen-owl DOMAIN="$domain"
run_bg rdf            "$MAKE" --no-print-directory gen-rdf DOMAIN="$domain"
run_bg proto          "$MAKE" --no-print-directory gen-proto DOMAIN="$domain"
run_bg linkml-convert "$MAKE" --no-print-directory gen-linkml-convert DOMAIN="$domain"
run_bg docs           "$MAKE" --no-print-directory gen-docs DOMAIN="$domain"
run_bg plantuml       "$MAKE" --no-print-directory gen-plantuml DOMAIN="$domain"

# Fase 2 avheng berre av gen-jsonschema (ikkje resten av fase 1) — vent på
# nøyaktig den eine jobben, la dei andre halde fram i bakgrunnen.
wait_job json-schema

# --- Fase 2 — treng gen-jsonschema sitt output ------------------------------
run_bg xsd      "$MAKE" --no-print-directory gen-xsd DOMAIN="$domain"
run_bg openapi  "$MAKE" --no-print-directory gen-openapi DOMAIN="$domain"
run_bg asyncapi "$MAKE" --no-print-directory gen-asyncapi DOMAIN="$domain"

# Vent på resten av fase 1 + heile fase 2.
for key in "${!PIDS[@]}"; do
    wait_job "$key"
done

if [ "$FAILED" -gt 0 ]; then
    log_error "::error::domain-${domain}: $FAILED gruppe(r) feila — stoppar før gen-informasjonsmodell-instance"
    exit 1
fi

# --- Fase 3 — treng ALT (finnes_i_format-lista skannar heile generated/) ---
"$MAKE" --no-print-directory gen-informasjonsmodell-instance DOMAIN="$domain"
