#!/usr/bin/env bash
# scripts/migrate-all-containers.sh
#
# Finn alle schema der containerklassen brukar globale slots i staden for attributes,
# og migrerer dei éin for éin. For kvart skjema køyrer scriptet:
#
#   1. scripts/migrate-container.py  — konverterer slots → inline attributes
#   2. gen-linkml                    — strukturvalidering av skjema
#   3. linkml validate               — instansvalidering mot eksempelfil (om ho finst)
#
# Bruk:
#   bash scripts/migrate-all-containers.sh

set -uo pipefail

# ---------------------------------------------------------------------------
# Oppsett
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$(cd "${SCRIPT_DIR}/.." && pwd)"

MIGRATE_PY="${SCRIPT_DIR}/migrate-container.py"
LINKML_IMAGE="localhost/linkml-local:latest"
LINKML_RUN="podman run --rm -v ${PWD}:/work -w /work -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root ${LINKML_IMAGE}"

# ---------------------------------------------------------------------------
# Fargar og log-funksjonar
# ---------------------------------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
DIM='\033[2m'
RESET='\033[0m'

SEP="══════════════════════════════════════════════════════════════"
THIN="──────────────────────────────────────────────────────────────"

log_sep()    { echo -e "\n${BOLD}${CYAN}${SEP}${RESET}"; }
log_thin()   { echo -e "${DIM}${THIN}${RESET}"; }
log_ok()     { echo -e "        ${GREEN}✓${RESET}  $*"; }
log_fail()   { echo -e "        ${RED}✗${RESET}  $*"; }
log_skip()   { echo -e "        ${YELLOW}⊘${RESET}  ${DIM}$*${RESET}"; }
log_detail() { echo -e "           ${DIM}$*${RESET}"; }
log_out()    { echo "$*" | sed 's/^/           /'; }

# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------

needs_migration() {
    # Returner 0 (sann) om skjemaet har tree_root med slots men ikkje attributes
    python3 - "$1" <<'PYEOF'
import sys, yaml
schema = yaml.safe_load(open(sys.argv[1]).read())
for cls in (schema.get("classes") or {}).values():
    if cls and cls.get("tree_root") and cls.get("slots") and not cls.get("attributes"):
        sys.exit(0)
sys.exit(1)
PYEOF
}

find_example() {
    # Returnerer stien til eksempelfila om ho finst, elles tom streng.
    # Mønster: examples/<domain>/<name>-eksempel.yaml
    # der <name> = basename(<schema> -schema.yaml)   (jf. Makefile)
    local schema="$1"
    local domain name example
    domain=$(echo "${schema}" | cut -d/ -f3)
    name=$(basename "${schema}" "-schema.yaml")
    example="examples/${domain}/${name}-eksempel.yaml"
    if [[ -f "${example}" ]]; then
        echo "${example}"
    fi
}

elapsed() {
    # Reknar ut sekund sidan $1 (epoch-sekund)
    echo $(( $(date +%s) - $1 ))
}

# ---------------------------------------------------------------------------
# Finn schema som treng migrering
# ---------------------------------------------------------------------------
echo -e "\n${BOLD}Container-slot-migrering${RESET}"
echo -e "${DIM}Skannar src/linkml/ etter schema der containerklassen brukar globale slots…${RESET}\n"

SCHEMAS_TO_MIGRATE=()
while IFS= read -r schema; do
    if needs_migration "${schema}"; then
        SCHEMAS_TO_MIGRATE+=("${schema}")
        echo -e "  ${YELLOW}→${RESET} ${schema}"
    fi
done < <(find src/linkml -name '*-schema*.yaml' | grep -v common | sort)

TOTAL=${#SCHEMAS_TO_MIGRATE[@]}
if [[ ${TOTAL} -eq 0 ]]; then
    echo -e "\n${GREEN}${BOLD}Alle schema er allereie migrerte.${RESET}"
    exit 0
fi

echo -e "\nFunne ${BOLD}${TOTAL}${RESET} schema som treng migrering.\n"

# ---------------------------------------------------------------------------
# Migrer og valider eitt og eitt
# ---------------------------------------------------------------------------
MIGRATED=0
LINT_OK=0; LINT_FAIL=0
VALIDATE_OK=0; VALIDATE_FAIL=0; VALIDATE_SKIP=0
FAILED_SCHEMAS=()

for schema in "${SCHEMAS_TO_MIGRATE[@]}"; do
    log_sep
    echo -e "${BOLD}  ${schema}${RESET}"
    log_thin

    SCHEMA_START=$(date +%s)

    # ── Steg 1: Migrering ────────────────────────────────────────────────
    echo -e "\n     ${BOLD}[1/3] Migrering${RESET}  ${DIM}migrate-container.py${RESET}"
    STEP_START=$(date +%s)

    if migrate_out=$(python3 "${MIGRATE_PY}" "${schema}" 2>&1); then
        SECS=$(elapsed "${STEP_START}")
        log_ok "Migrering fullført  ${DIM}(${SECS}s)${RESET}"
        # Skriv ut interessante linjer frå migrate-output (ikkje dei generiske)
        while IFS= read -r line; do
            [[ "${line}" == Skjema:* ]] && continue
            [[ "${line}" == Ferdig.* ]] && continue
            [[ -n "${line}" ]] && log_detail "${line}"
        done <<< "${migrate_out}"
        MIGRATED=$(( MIGRATED + 1 ))
    else
        log_fail "Migrering feila"
        log_out "${migrate_out}"
        FAILED_SCHEMAS+=("${schema} [migrering]")
        continue  # ikkje lint eit øydelagd skjema
    fi

    # ── Steg 2: Schema-lint (gen-linkml) ─────────────────────────────────
    echo -e "\n     ${BOLD}[2/3] Schema-lint${RESET}  ${DIM}gen-linkml${RESET}"
    STEP_START=$(date +%s)

    if lint_out=$(${LINKML_RUN} gen-linkml "${schema}" 2>&1); then
        SECS=$(elapsed "${STEP_START}")
        log_ok "Schema-lint OK  ${DIM}(${SECS}s)${RESET}"
        LINT_OK=$(( LINT_OK + 1 ))
    else
        SECS=$(elapsed "${STEP_START}")
        log_fail "Schema-lint feila  ${DIM}(${SECS}s)${RESET}"
        echo "${lint_out}" \
            | grep -E "^(ERROR|WARNING|error:|.*Error:)" \
            | head -15 \
            | while IFS= read -r line; do log_detail "${line}"; done
        LINT_FAIL=$(( LINT_FAIL + 1 ))
        FAILED_SCHEMAS+=("${schema} [lint]")
    fi

    # ── Steg 3: Instansvalidering ─────────────────────────────────────────
    echo -e "\n     ${BOLD}[3/3] Instansvalidering${RESET}  ${DIM}linkml validate${RESET}"
    STEP_START=$(date +%s)

    example=$(find_example "${schema}")
    if [[ -z "${example}" ]]; then
        log_skip "Ingen eksempelfil funne — hoppar over"
        VALIDATE_SKIP=$(( VALIDATE_SKIP + 1 ))
    else
        log_detail "Eksempel: ${example}"
        if validate_out=$(${LINKML_RUN} linkml validate --schema "${schema}" "${example}" 2>&1); then
            SECS=$(elapsed "${STEP_START}")
            if echo "${validate_out}" | grep -q "\[ERROR\]"; then
                log_fail "Instansvalidering feila  ${DIM}(${SECS}s)${RESET}"
                echo "${validate_out}" \
                    | grep "\[ERROR\]" \
                    | head -10 \
                    | while IFS= read -r line; do log_detail "${line}"; done
                VALIDATE_FAIL=$(( VALIDATE_FAIL + 1 ))
                FAILED_SCHEMAS+=("${schema} [validate]")
            else
                log_ok "Instansvalidering OK  ${DIM}(${SECS}s)${RESET}"
                VALIDATE_OK=$(( VALIDATE_OK + 1 ))
            fi
        else
            SECS=$(elapsed "${STEP_START}")
            log_fail "Instansvalidering feila (avvikande exit-kode)  ${DIM}(${SECS}s)${RESET}"
            echo "${validate_out}" | head -5 | while IFS= read -r line; do log_detail "${line}"; done
            VALIDATE_FAIL=$(( VALIDATE_FAIL + 1 ))
            FAILED_SCHEMAS+=("${schema} [validate]")
        fi
    fi

    SECS=$(elapsed "${SCHEMA_START}")
    echo -e "\n     ${DIM}Totalt for dette skjemaet: ${SECS}s${RESET}"
done

# ---------------------------------------------------------------------------
# Oppsummering
# ---------------------------------------------------------------------------
log_sep
echo -e "${BOLD}  OPPSUMMERING${RESET}"
log_thin
echo
printf "  %-28s %s\n" "Skjema funne:" "${TOTAL}"
printf "  %-28s %s\n" "Migrert:" "${MIGRATED} / ${TOTAL}"
echo
printf "  %-28s ${GREEN}%s${RESET}  feil: ${RED}%s${RESET}\n" \
    "Schema-lint (gen-linkml):" "${LINT_OK}" "${LINT_FAIL}"
printf "  %-28s ${GREEN}%s${RESET}  feil: ${RED}%s${RESET}  hoppa over: ${YELLOW}%s${RESET}\n" \
    "Instansvalidering:" "${VALIDATE_OK}" "${VALIDATE_FAIL}" "${VALIDATE_SKIP}"

TOTAL_FAILURES=$(( LINT_FAIL + VALIDATE_FAIL + MIGRATED - TOTAL + ${#SCHEMAS_TO_MIGRATE[@]} - MIGRATED ))
# Rekn ut faktisk antal feil
ACTUAL_FAILURES=$(( LINT_FAIL + VALIDATE_FAIL + (TOTAL - MIGRATED) ))

if [[ ${ACTUAL_FAILURES} -gt 0 ]]; then
    echo
    echo -e "  ${RED}${BOLD}Feil i følgjande skjema:${RESET}"
    for s in "${FAILED_SCHEMAS[@]}"; do
        echo -e "    ${RED}✗${RESET}  ${s}"
    done
    echo
    echo -e "${RED}${BOLD}  Migrering ikkje fullstendig — sjå feilmeldingar over.${RESET}"
    echo -e "${CYAN}${SEP}${RESET}\n"
    exit 1
else
    echo
    echo -e "  ${GREEN}${BOLD}Alle schema migrerte og validerte OK.${RESET}"
    echo -e "${CYAN}${SEP}${RESET}\n"
    exit 0
fi
