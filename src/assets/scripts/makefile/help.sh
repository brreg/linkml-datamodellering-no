#!/usr/bin/env bash
# Genererer den kategoriserte target-lista for `make help`. Les kvart
# target sin `## `-hjelpetekst frå filene gitt som argument (Makefile sin
# $(MAKEFILE_LIST)) og listar dei opp gruppert etter kategori — første
# kategori-mønster som matchar eit targetnamn vinn. Delt ut for å unngå å
# gjenta same grep|sed|awk-pipeline sju gonger inline i Makefile (éin gong
# per kategori) — sjå specs/done/forenkle-make-laget.md.
#
# Bruk: help.sh <fil1> [fil2 ...]
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

CLR_STEP=$'\033[0;36m'
CLR_RST=$'\033[0m'

[ $# -gt 0 ] || { echo "help.sh: krev minst éi fil som argument" >&2; exit 1; }
files=("$@")

# (overskrift|grep -E-mønster for targetnamn) — i visingsrekkefølgje
categories=(
    "Vanleg bruk|(test|roundtrip|clean|help)"
    "Generering (per domene eller skjema)|(gen-|domain-|convert-)"
    "Validering|(validate|lint)"
    "Dokumentasjon|docs-"
    "Container images|build-docker-"
    "MCP-serverar|mcp-"
    "Vedlikehald|(update-|new-|check-)"
)

first=true
for entry in "${categories[@]}"; do
    label="${entry%%|*}"
    pattern="${entry#*|}"
    if [ "$first" = true ]; then
        first=false
    else
        echo ""
    fi
    echo "${label}:"
    # Merk: ingen -h til grep — når fleire filer er gitt, prefikser grep
    # kvar linje med "filnamn:", og det etterfølgjande sed-steget nyttar
    # nettopp dette (fjernar alt til og med FØRSTE kolon = filnamnet) for å
    # få fram sjølve "target: ## skildring"-linja. Med -h forsvinn
    # filnamn-prefikset, og sed ville i staden fjerne target-namnet.
    grep -E '^[a-zA-Z_-]+:.*?## .*$' "${files[@]}" \
        | grep -E "$pattern" \
        | sed 's/^[^:]*://' \
        | awk -v step="$CLR_STEP" -v rst="$CLR_RST" 'BEGIN {FS = "## "}; {printf "  %s%-30s%s %s\n", step, $1, rst, $2}'
done
