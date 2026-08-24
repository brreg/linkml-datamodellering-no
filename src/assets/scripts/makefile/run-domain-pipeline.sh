#!/usr/bin/env bash
# Orkestrerer domain_target sin genereringspipeline med fase-medviten
# parallellisering mellom uavhengige batch-grupper — sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md,
# «Parallellisering etter batching».
#
# Kvart steg er eit rekursivt $(MAKE) <target> DOMAIN=<domene>-kall til eit
# alt eksisterande, sjølvstendig verifisert gen-*-target (batch-generate.py/
# batch-generate-instances.py gjer sjølve genereringsarbeidet, uendra) —
# dette scriptet reimplementerer ingen podman- eller genereringslogikk,
# berre fase-rekkjefølgje, samstundes-oppstart og feilsamling (PID-array +
# wait, same mønster som parallelliser-domene-validering.md).
#
# Fase 1 (samstundes): alle grupper utan innbyrdes avhengigheit, inkl.
#   gen-jsonschema sjølv (fase 2 ventar spesifikt på henne, ikkje på resten
#   av fase 1). Inkluderer gen-graphql og gen-java (reint LinkML-generert,
#   ingen JSON Schema-avhengigheit, same gruppe som gen-proto).
# Fase 2 (samstundes, ventar på gen-jsonschema): gen-xsd/gen-openapi/
#   gen-asyncapi les alle <name>-schema.json.
# Fase 3 (ventar på ALT frå fase 1+2): gen-informasjonsmodell-instance sin
#   discover_artifacts() skannar heile generated/<domain>/<name>/ for
#   finnes_i_format-lista, og må difor køyre sist.
#
# Til slutt vert ei oppsummering skriven (print_pipeline_summary()), analogt
# print_phase_a_summary() i tests/test_make.sh — sjå
# specs/done/oppsummering-run-domain-pipeline.md. Dei tre fasane er IKKJE
# likeverdige (Fase 1 er uavhengig, Fase 2 ventar på json-schema, Fase 3
# ventar på ALT), så oppsummeringa viser dei som tre eksplisitt åtskilde
# grupper med kvar si forklårande overskrift, ikkje éi flat liste.
#
# Bruk: run-domain-pipeline.sh <domene>
# Miljøvariablar som må vere sette: MAKE, GEN_DIR, LOG_FUNCTIONS
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

: "${MAKE:?miljøvariabelen MAKE må vere sett}"
: "${GEN_DIR:?miljøvariabelen GEN_DIR må vere sett}"

domain="$1"
PIPELINE_T0=$(date +%s%3N)

eval "$LOG_FUNCTIONS"

declare -A PIDS
declare -A ELAPSED_MS OK_FLAG ELAPSED_FILES
declare -a STEP_ORDER_PHASE1=() STEP_ORDER_PHASE2=()
FAILED=0

# MERK: elapsed-tida vert målt INNI subskalet sjølv (skriven til ei
# eiga, fast fil), IKKJE utrekna i wait_job() ut frå "no" der. Grunngjeving:
# wait_job() vert kalla FOR KVAR NØKKEL i eit usortert associative-array-
# loop (sjå "for key in "${!PIDS[@]}""-løkka under) — dersom EITT tidleg
# steg i den løkka faktisk må BLOKKERE ei stund (endå ikkje ferdig), får
# ALLE steg som kjem etter i løkka (sjølv om DEI vart ferdige for lengst)
# "no" i wait_job() rekna som SITT sluttidspunkt — dette gav i praksis
# feilaktig oppblåste tider (mange steg synte ~25s uavhengig av reell
# køyretid, verifisert empirisk). Å måle elapsed FØR/ETTER "$@" INNI
# subskalet unngår heilt denne ordenavhengige feilkjelda.
run_bg() {
    local phase="$1" key="$2"; shift 2
    if [ "$phase" = "1" ]; then
        STEP_ORDER_PHASE1+=("$key")
    else
        STEP_ORDER_PHASE2+=("$key")
    fi
    local elapsedfile
    elapsedfile=$(mktemp "${TMPDIR:-/tmp}/domain-pipeline-elapsed-XXXXXX")
    ELAPSED_FILES[$key]="$elapsedfile"
    (
        t0=$(date +%s%3N)
        # if/then/else (ikkje "$@" || rc=$?") slik at linja ETTER alltid
        # køyrer sjølv om "$@" feilar — set -euo pipefail er aktivt (arva
        # av subskalet), og eit ikkje-null steg midt i eit vanleg kommando-
        # kall ville elles avslutta subskalet FØR elapsed vart skriven.
        if "$@"; then rc=0; else rc=$?; fi
        echo "$(( $(date +%s%3N) - t0 ))" > "$elapsedfile"
        exit "$rc"
    ) &
    PIDS[$key]=$!
}

wait_job() {
    local key="$1"
    local rc=0
    wait "${PIDS[$key]}" || rc=$?
    ELAPSED_MS[$key]=$(cat "${ELAPSED_FILES[$key]}" 2>/dev/null || echo 0)
    rm -f "${ELAPSED_FILES[$key]}"
    if [ "$rc" -ne 0 ]; then
        log_error "::error::domain-${domain}/${key} feila"
        FAILED=$((FAILED + 1))
        OK_FLAG[$key]=0
    else
        OK_FLAG[$key]=1
    fi
    unset "PIDS[$key]"
}

# Skriv éi oppsummeringslinje for eitt steg — kolonnejustert navn/tidsbruk/
# status, same visuelle mønster (breidder, fargar) som print_phase_a_summary()
# i tests/test_make.sh.
print_step_line() {
    local key="$1"
    local prefix="→ $key"
    local timing="($(fmt_elapsed_ms "${ELAPSED_MS[$key]}"))"
    if [ "${OK_FLAG[$key]}" -eq 1 ]; then
        printf '%-30s %-11s %sOK%s\n' "$prefix" "$timing" "$CLR_OK" "$CLR_RST"
    else
        printf '%-30s %-11s %sFEIL%s\n' "$prefix" "$timing" "$CLR_ERR" "$CLR_RST"
    fi
}

print_pipeline_summary() {
    echo ""
    echo "=== domain-${domain} — oppsummering ==="
    echo ""
    echo "Parallelle batcha kall (Fase 1 — uavhengige steg, køyrer samstundes, ingen ventar på noko):"
    local key
    for key in "${STEP_ORDER_PHASE1[@]}"; do
        print_step_line "$key"
    done

    if [ "${#STEP_ORDER_PHASE2[@]}" -gt 0 ]; then
        echo ""
        echo "Rekkjefølgde batcha kall (Fase 2 — ventar på gen-jsonschema frå Fase 1, køyrer så samstundes seg imellom):"
        for key in "${STEP_ORDER_PHASE2[@]}"; do
            print_step_line "$key"
        done
    fi

    if [ -n "${INFOMODELL_OK_FLAG:-}" ]; then
        echo ""
        echo "Synkrone kall (Fase 3 — ventar på ALT frå Fase 1+2, køyrer heilt åleine sist):"
        local prefix="→ informasjonsmodell-instance"
        local timing="($(fmt_elapsed_ms "$INFOMODELL_ELAPSED_MS"))"
        if [ "$INFOMODELL_OK_FLAG" -eq 1 ]; then
            printf '%-30s %-11s %sOK%s\n' "$prefix" "$timing" "$CLR_OK" "$CLR_RST"
        else
            printf '%-30s %-11s %sFEIL%s\n' "$prefix" "$timing" "$CLR_ERR" "$CLR_RST"
        fi
    fi

    local total_steps=$(( ${#STEP_ORDER_PHASE1[@]} + ${#STEP_ORDER_PHASE2[@]} ))
    if [ -n "${INFOMODELL_OK_FLAG:-}" ]; then
        total_steps=$((total_steps + 1))
    fi
    echo ""
    echo "Resultat: domain-${domain}: $((total_steps - FAILED)) OK, $FAILED feil"
    echo "Total tidsbruk: $(fmt_elapsed_ms $(( $(date +%s%3N) - PIPELINE_T0 )))"
}

# --no-print-directory: utan dette skrur GNU Make automatisk på
# "Entering/Leaving directory"-meldingar for sub-make-kall som oppdagar dei
# køyrer under ein annan make (MAKELEVEL > 0) — rein støy her, sidan kvart
# steg alt har si eiga print_header-deloverskrift (sjå
# specs/done/gjenopprett-debug-logging-fjern-make-directory-stoy.md).

# --- Fase 1 — uavhengige grupper, inkl. gen-jsonschema ---------------------
run_bg 1 merge          "$MAKE" --no-print-directory validate DOMAIN="$domain"
run_bg 1 jsonld-context "$MAKE" --no-print-directory gen-jsonld-context DOMAIN="$domain"
run_bg 1 shacl          "$MAKE" --no-print-directory gen-shacl DOMAIN="$domain"
run_bg 1 python         "$MAKE" --no-print-directory gen-python DOMAIN="$domain"
run_bg 1 json-schema    "$MAKE" --no-print-directory gen-jsonschema DOMAIN="$domain"
run_bg 1 owl            "$MAKE" --no-print-directory gen-owl DOMAIN="$domain"
run_bg 1 rdf            "$MAKE" --no-print-directory gen-rdf DOMAIN="$domain"
run_bg 1 proto          "$MAKE" --no-print-directory gen-proto DOMAIN="$domain"
run_bg 1 graphql        "$MAKE" --no-print-directory gen-graphql DOMAIN="$domain"
run_bg 1 java           "$MAKE" --no-print-directory gen-java DOMAIN="$domain"
run_bg 1 convert-instance-rdf "$MAKE" --no-print-directory convert-instance-rdf DOMAIN="$domain"
run_bg 1 docs           "$MAKE" --no-print-directory gen-schema-docs DOMAIN="$domain"
run_bg 1 plantuml       "$MAKE" --no-print-directory gen-plantuml DOMAIN="$domain"

# Fase 2 avheng berre av gen-jsonschema (ikkje resten av fase 1) — vent på
# nøyaktig den eine jobben, la dei andre halde fram i bakgrunnen.
wait_job json-schema

# --- Fase 2 — treng gen-jsonschema sitt output ------------------------------
run_bg 2 xsd      "$MAKE" --no-print-directory gen-xsd DOMAIN="$domain"
run_bg 2 openapi  "$MAKE" --no-print-directory gen-openapi DOMAIN="$domain"
run_bg 2 asyncapi "$MAKE" --no-print-directory gen-asyncapi DOMAIN="$domain"

# Vent på resten av fase 1 + heile fase 2.
for key in "${!PIDS[@]}"; do
    wait_job "$key"
done

if [ "$FAILED" -gt 0 ]; then
    print_pipeline_summary
    log_error "::error::domain-${domain}: $FAILED gruppe(r) feila — stoppar før gen-informasjonsmodell-instance"
    exit 1
fi

# --- Fase 3 — treng ALT (finnes_i_format-lista skannar heile generated/) ---
INFOMODELL_T0=$(date +%s%3N)
rc=0
"$MAKE" --no-print-directory gen-informasjonsmodell-instance DOMAIN="$domain" || rc=$?
INFOMODELL_ELAPSED_MS=$(( $(date +%s%3N) - INFOMODELL_T0 ))
if [ "$rc" -ne 0 ]; then
    log_error "::error::domain-${domain}/informasjonsmodell-instance feila"
    FAILED=$((FAILED + 1))
    INFOMODELL_OK_FLAG=0
else
    INFOMODELL_OK_FLAG=1
fi

print_pipeline_summary

[ "$FAILED" -eq 0 ]
