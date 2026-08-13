#!/usr/bin/env bash
# Genererer den kategoriserte target-lista for `make help`. Les kvart
# target sin `## `-hjelpetekst frå filene gitt som argument (Makefile sin
# $(MAKEFILE_LIST)) og listar dei opp gruppert etter kategori — første
# kategori-mønster som matchar eit targetnamn vinn (target vist i éin
# kategori, aldri fleire, sjølv om namnet matchar fleire mønster — t.d.
# build-docker-mcp-validator matchar både "build-docker-" og "mcp-", men
# hamnar berre under "Container images" sidan det mønsteret kjem først).
# Delt ut for å unngå å gjenta same grep|sed|awk-pipeline sju gonger inline
# i Makefile (éin gong per kategori) — sjå specs/done/forenkle-make-laget.md.
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
    "Vedlikehald|(update-|new-|remove-|check-)"
)

# Merk: ingen -h til grep — når fleire filer er gitt, prefikser grep kvar
# linje med "filnamn:", og det etterfølgjande sed-steget nyttar nettopp
# dette (fjernar alt til og med FØRSTE kolon = filnamnet) for å få fram
# sjølve "target: ## skildring"-linja. Med -h forsvinn filnamn-prefikset,
# og sed ville i staden fjerne target-namnet.
#
# Andre sed-steget strippar eventuelle Makefile-prerequisitar mellom
# target-kolon og "## " (t.d. "gource-preview: build-docker-gource ## ..."
# → "gource-preview: ## ...") slik at namnekolonna i output berre viser
# target-namnet, ikkje prerequisitar.
mapfile -t lines < <(
    grep -E '^[a-zA-Z_-]+:.*?## .*$' "${files[@]}" \
        | sed 's/^[^:]*://' \
        | sed -E 's/^([a-zA-Z_-]+):[^#]*## /\1: ## /'
)

declare -A shown=()
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
    for line in "${lines[@]}"; do
        target="${line%%:*}"
        [ -n "${shown[$target]+x}" ] && continue
        if [[ "$target" =~ $pattern ]]; then
            printf "  %s%-32s%s %s\n" "$CLR_STEP" "${target}:" "$CLR_RST" "${line#*## }"
            shown[$target]=1
        fi
    done
done
