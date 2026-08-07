#!/usr/bin/env bash
# Delt orkestrering for parallell artefaktgenerering — brukt av "_parallel"-
# makroane i make/10-generator-macros.mk som har etterhandsaming/eksterne
# verktøy (gen-doc, gen-erdiagram, gen-plantuml, gen-xsd, gen-openapi,
# gen-asyncapi). Dei reint linkml-baserte generatorane (merge, jsonld-
# context, shacl, python, json-schema, owl, rdf, proto) batchar i staden N
# skjema inn i éin kontainar via batch-generate.py — sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md (Tiltak 1).
# Filtrerer skjemalista mot eit valfritt build.yaml-flagg FØR xargs-parallelliseringa startar,
# skriv éi deloverskrift (log_debug) + éi samla skip-debug-linje, og køyrer
# sjølve genererings-kommandoen (gitt via miljøvariabelen GEN_CMD) per
# skjema — kvar fullført køyring loggar si eiga log_info-linje med
# køyretid, så deloverskrifta held seg til LOGLVL=DEBUG for å unngå at
# batchar med berre eitt skjema logger to nesten identiske INFO-linjer.
#
# Sjå specs/done/delt-script-parallell-generering.md for grunngjeving —
# erstattar dei to tidlegare, nesten identiske make-makroane
# run_parallel_with_timer og run_gen_with_check_parallel, som dupliserte
# denne scaffoldinga som sterkt nøsta bash-i-bash-i-xargs-i-make.
#
# Bruk:
#   GEN_CMD='...' run-parallel-gen.sh --generator <namn> [--flag <flagg>] \
#       [--check-suffix <suffiks>] [--out-suffix <suffiks>] \
#       [--extra-flags-field <build.yaml-feltnamn>] -- <skjema...>
#
# --extra-flags-field: valfritt. Om sett, les kvart skjema sitt eige
#   build.yaml-felt (t.d. "shacl_flags" eller "owl_flags", forma som
#   `  <felt>: "--nokre --flagg"` under generators:) og gjer verdien
#   tilgjengeleg som shell-variabelen $extra_flags for GEN_CMD. Tom/manglande
#   verdi gjev tom $extra_flags. Les direkte frå build.yaml (ikkje via
#   config.mk/Make-variablar) sidan GEN_CMD vert evaluert i ein xargs-
#   subshell utan tilgang til Make sin variabeltilstand.
#
# Miljøvariablar som må vere sette (eksportert frå make/00-settings.mk):
#   GEN_CMD, GEN_DIR, PARALLEL, LOG_FUNCTIONS, CLR_STEP, CLR_RST
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

generator=""
flag=""
check_suffix=""
out_suffix=""
extra_flags_field=""

while [ $# -gt 0 ]; do
    case "$1" in
        --generator) generator="$2"; shift 2 ;;
        --flag) flag="$2"; shift 2 ;;
        --check-suffix) check_suffix="$2"; shift 2 ;;
        --out-suffix) out_suffix="$2"; shift 2 ;;
        --extra-flags-field) extra_flags_field="$2"; shift 2 ;;
        --) shift; break ;;
        *) echo "run-parallel-gen.sh: ukjent flagg: $1" >&2; exit 1 ;;
    esac
done

: "${generator:?--generator er obligatorisk}"
: "${GEN_CMD:?miljøvariabelen GEN_CMD må vere sett}"
: "${GEN_DIR:?miljøvariabelen GEN_DIR må vere sett}"
: "${PARALLEL:?miljøvariabelen PARALLEL må vere sett}"

eval "$LOG_FUNCTIONS"

enabled=()
skipped=()
for s in "$@"; do
    d=$(echo "$s" | cut -d/ -f3)
    n=$(basename "$s" -schema.yaml | sed 's/-schema$//')
    if [ -z "$flag" ]; then
        enabled+=("$s")
    else
        manifest=$(dirname "$s")/build.yaml
        if [ -f "$manifest" ] && grep -q "^  $flag: true" "$manifest"; then
            enabled+=("$s")
        else
            skipped+=("$d/$n")
        fi
    fi
done

if [ "${#enabled[@]}" -gt 0 ]; then
    names=$(for s in "${enabled[@]}"; do d=$(echo "$s" | cut -d/ -f3); n=$(basename "$s" -schema.yaml | sed 's/-schema$//'); echo "$d/$n"; done | paste -sd, -)
else
    names="(ingen skjema aktivert)"
fi
if [ -n "$flag" ]; then
    log_debug "${generator} (${flag}: true) for schemas: ${names}"
else
    log_debug "${generator} for schemas: ${names}"
fi

if [ "${#skipped[@]}" -gt 0 ]; then
    skipped_list=$(printf '%s, ' "${skipped[@]}")
    skipped_list=${skipped_list%, }
    log_debug "  hoppar over (${flag}: false): ${skipped_list}"
fi

[ "${#enabled[@]}" -eq 0 ] && exit 0

export GEN_CMD GEN_DIR LOG_FUNCTIONS CLR_STEP CLR_RST generator check_suffix out_suffix extra_flags_field

printf '%s\n' "${enabled[@]}" | xargs -P "$PARALLEL" -I {} bash -c '
    set -euo pipefail
    eval "$LOG_FUNCTIONS"
    s="{}"
    name=$(basename "$s" -schema.yaml | sed "s/-schema\$//")
    domain=$(echo "$s" | cut -d/ -f3)
    trap "log_error \"::error file=$s::${generator} feila for $domain/$name (linje \$LINENO) — kommando: \$BASH_COMMAND\"; exit 1" ERR
    outdir="$GEN_DIR/$domain/$name"
    mkdir -p "$outdir"
    if [ -n "$check_suffix" ]; then
        input="$outdir/$name-$check_suffix"
        if [ ! -f "$input" ]; then
            log_error "ÅTVARING: $input finst ikkje — hoppar over $generator for $name"
            exit 0
        fi
    fi
    if [ -n "$out_suffix" ]; then
        out="$outdir/$name-$out_suffix"
    fi
    extra_flags=""
    if [ -n "$extra_flags_field" ]; then
        manifest=$(dirname "$s")/build.yaml
        if [ -f "$manifest" ]; then
            extra_flags=$(sed -n "s/^  ${extra_flags_field}: *\"\\(.*\\)\"/\\1/p" "$manifest" | head -1)
        fi
    fi
    t0=$(date +%s%3N)
    eval "$GEN_CMD"
    rc=$?
    t1=$(date +%s%3N)
    elapsed_ms=$((t1 - t0))
    log_info "$(printf "${CLR_STEP}→ %s  %s/%s${CLR_RST} (%d.%ds)" "$generator" "$domain" "$name" $((elapsed_ms / 1000)) $((elapsed_ms % 1000 / 100)))"
    exit "$rc"
'
