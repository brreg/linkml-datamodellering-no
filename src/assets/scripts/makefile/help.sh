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
# Kvart target vert vist på éi linje (sjå specs/done/make-help-argument-og-farge.md
# og specs/done/make-help-eitt-linje-format.md):
#   make <target> <argument-uttrykk> <skildring>
# der "make <target>" og argument-uttrykket er farga (kopierbar kall-syntaks),
# og skildringa dempa (hjelpetekst). Argument-uttrykket er ei avsluttande
# "(...)"- eller "[...]"-gruppe (eller
# fleire etter kvarandre) i `## `-skildringa som inneheld minst eitt "=" —
# konvensjonen er at parentes ("(NAME=<namn>)") markerer obligatoriske
# argument (farga grøn, CLR_OK), hakeparentes ("[SCHEMA=<sti>]") valfrie
# (farga gul, CLR_WARN). Kvar gruppe fargeleggjast for seg — ei gruppe med
# nøsta hakeparentes inni ein ytre parentes (t.d.
# "(SCHEMA=<sti> [POLICY=<...>])") vert farga grøn i sin heilskap, sidan
# ytre parentes er det avgjerande skiljet (gruppa vert ikkje token-parsa
# vidare). Ei avsluttande gruppe UTAN "=" (t.d. "(1080p, høg kvalitet)")
# er ei vanleg parentetisk merknad, ikkje eit argument, og vert verande i
# skildringa.
#
# Bruk: help.sh <fil1> [fil2 ...]
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

CLR_STEP=$'\033[0;36m'
CLR_OK=$'\033[0;32m'
CLR_WARN=$'\033[0;33m'
CLR_DBG=$'\033[2m'
CLR_RST=$'\033[0m'

[ $# -gt 0 ] || { echo "help.sh: krev minst éi fil som argument" >&2; exit 1; }
files=("$@")

# (overskrift|grep -E-mønster for targetnamn) — i visingsrekkefølgje, som
# også følgjer brukar-arbeidsflyten (opprett → valider → generer →
# publiser → analyser), med infrastruktur-/verktøykategoriane sist.
# Vanleg bruk-mønsteret er ankra (^...$, eksakt targetnamn) — dei andre
# mønstera er umarkerte prefiks/substring-mønster. Ankringa er nødvendig
# fordi "test" elles ville matche som substring i mcp-linkml-*-test og
# stole dei frå MCP-serverar (sjå specs/done/help-gruppering-vanleg-bruk-vedlikehald.md).
# Container images må stå før MCP-serverar — build-docker-mcp-*-target
# matchar begge mønstera, og fyrste treff vinn (sjå fil-toppkommentaren).
categories=(
    "Vanleg bruk|^(help|test|roundtrip|roundtrip-json-schema|clean|check-prereqs)\$"
    "Opprett og fjern modellar|(new-|remove-modell|gen-valid-scopes)"
    "Validering|(validate|lint|check-published-uris|check-import-duplicates)"
    "Generering (per domene eller skjema)|(gen-|domain-|convert-)"
    "Dokumentasjonsportal|docs-"
    "Modell-analyse|analyse-"
    "Container images|build-docker-"
    "MCP-serverar|mcp-"
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

# Halden i ein variabel (ikkje inline i [[ =~ ]]) sidan bash sin eigen
# parser elles kan feiltolke dei ubalanserte/blanda parentesane og
# hakeparentesane i mønsteret som shell-syntaks.
arg_group_re='^(.*[^[:space:]])[[:space:]]+(\[[^]]*=[^]]*\]|\([^)]*=[^)]*\))$'

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
            desc="${line#*## }"

            # Skil ut avsluttande argument-gruppe(r) frå skildringa — kan
            # vere fleire etter kvarandre, t.d. "(NAME=<n>) [CONFIRM=1]".
            # Krev "=" i gruppa for å ikkje ta med vanlege parentetiske
            # merknadar (sjå fil-toppkommentaren).
            argexpr=""
            while [[ "$desc" =~ $arg_group_re ]]; do
                group="${BASH_REMATCH[2]}"
                if [[ "$group" == \(* ]]; then
                    group="${CLR_OK}${group}${CLR_RST}"
                else
                    group="${CLR_WARN}${group}${CLR_RST}"
                fi
                if [ -n "$argexpr" ]; then
                    argexpr="$group $argexpr"
                else
                    argexpr="$group"
                fi
                desc="${BASH_REMATCH[1]}"
            done

            if [ -n "$argexpr" ]; then
                printf "  %smake %s%s %s %s%s%s\n" \
                    "$CLR_STEP" "$target" "$CLR_RST" "$argexpr" "$CLR_DBG" "$desc" "$CLR_RST"
            else
                printf "  %smake %s%s %s%s%s\n" \
                    "$CLR_STEP" "$target" "$CLR_RST" "$CLR_DBG" "$desc" "$CLR_RST"
            fi
            shown[$target]=1
        fi
    done
done
