#!/usr/bin/env bash
# Integrasjonstester for make-targets. Køyr mot alle reelle skjema, parallelt.
# Krev at localhost/linkml-local:latest er bygd (make linkml-build-docker).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

LINKML_IMAGE="localhost/linkml-local:latest"
MCP_IMAGE="mcp-linkml-validator"
GEN_DIR="generated"
SCHEMA_DIR="src/linkml"
LOGDIR="tests/testlogs"
LOG="$LOGDIR/test_make_$(date '+%Y%m%d_%H%M%S').log"
mkdir -p "$LOGDIR"
mkdir -p "$REPO_ROOT/tmp"

CLR_OK=$(printf '\033[0;32m')
CLR_ERR=$(printf '\033[0;31m')
CLR_RST=$(printf '\033[0m')

# ---------------------------------------------------------------------------
# Skjemaoppdaging — same logikk som Makefile SCHEMAS-variabelen
# Valfritt første argument avgrensar til eitt skjema: bash test_make.sh <sti>
# ---------------------------------------------------------------------------
SCHEMA_FILTER="${1:-}"

if [ -n "$SCHEMA_FILTER" ]; then
    SCHEMA_FILTER="${SCHEMA_FILTER#./}"
    if [ ! -f "$SCHEMA_FILTER" ]; then
        echo "Feil: skjema ikkje funne: $SCHEMA_FILTER" >&2
        exit 1
    fi
    SCHEMAS=("$SCHEMA_FILTER")
else
    mapfile -t SCHEMAS < <(
        find "$SCHEMA_DIR" -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
            | grep -v common | sort
    )
fi

schema_domain() { echo "$1" | cut -d/ -f3; }
schema_name()   { echo "$1" | cut -d/ -f4; }
schema_outdir() { echo "$GEN_DIR/$(schema_domain "$1")/$(schema_name "$1")"; }

# ap-no og fair har ikkje tree_root — påverkar linkml-convert (treng fixture-
# schema for å bestemme målklasse) og gen-rdf frå eksempelfiler.
lacks_tree_root() { [[ "$1" == "ap-no" || "$1" == "fair" ]]; }

# Avgjer om eit skjema treng mcp-validate-instance-validering, og i så fall
# kva skjema- og instansfil som skal brukast. Delt mellom Fase A (bygging av
# batcha jobbliste) og test_mcp_validate_instance (skip-meldingar), slik at
# begge stadene er garantert samde om kva som vert hoppa over — unngår at
# skip-logikken driv frå kvarandre over tid.
# Skriv "<skjema-å-validere-mot> <instansfil>" til stdout og returnerer 0
# dersom skjemaet skal validerast; returnerer 1 (ingen output) elles.
mcp_instance_job() {
    local schema="$1" domain="$2" name="$3"
    lacks_tree_root "$domain" && return 1
    local example="src/linkml/$domain/$name/examples/$name-eksempel.yaml"
    [ -f "$example" ] || return 1
    local validate_schema="$schema"
    [ -f "tests/fixtures/$name-fixture.yaml" ] && validate_schema="tests/fixtures/$name-fixture.yaml"
    echo "$validate_schema $example"
}

# Delte "treng dette skjemaet steg X"-avgjerder for Kategori D (convert-rdf,
# roundtrip-json, roundtrip-ttl, linkml-validate) — same grunngjeving som
# mcp_instance_job() over: delt mellom Fase A (jobbliste) og Fase B
# (skip-meldingar) for å garantere samsvar.

convert_rdf_job() {
    local schema="$1" domain="$2" name="$3" example="$4"
    lacks_tree_root "$domain" && return 1
    local build_yaml="$(dirname "$schema")/build.yaml"
    if [ -f "$build_yaml" ] && grep -q "^  example_rdf: false" "$build_yaml"; then
        return 1
    fi
    # BUG-2: rdflib_loader feiler på inlined_as_list + identifier: true
    # Sjå bugs/inlined-as-list-rdflib-roundtrip.md
    case "$name" in
        ngr-adresse|ngr-eiendom|ngr-virksomhet) return 1 ;;
    esac
    [ -f "$example" ] || return 1
    return 0
}

roundtrip_json_job() {
    local schema="$1" domain="$2" name="$3" example="$4"
    lacks_tree_root "$domain" && return 1
    [ -f "$example" ] || return 1
    return 0
}

roundtrip_ttl_job() {
    local schema="$1" domain="$2" name="$3" example="$4"
    lacks_tree_root "$domain" && return 1
    # BUG-2: rdflib_loader feiler på inlined_as_list + identifier: true
    case "$name" in
        ngr-adresse|ngr-eiendom|ngr-virksomhet) return 1 ;;
    esac
    # BUG-1: rdflib_loader rekonstruerer ikkje LangString-verdiar frå TTL
    # Sjå bugs/langstring-rdflib-roundtrip.md
    case "$name" in
        brreg-begrepskatalog|brreg-modellkatalog|digdir-modellkatalog| \
        novari-modellkatalog|ksdigital-modellkatalog|skatteetaten-modellkatalog| \
        kartverket-modellkatalog) return 1 ;;
    esac
    [ -f "$example" ] || return 1
    return 0
}

# Avgjer om eit skjema treng linkml-validate, og i så fall kva skjema det
# skal validerast MOT (kan vere ein test-fixture, for skjema som manglar
# tree_root — ulikt mcp_instance_job() vert desse IKKJE hoppa over, berre
# validerte mot fixture i staden). Skriv skjemaet-å-validere-mot til stdout.
# Attribueringsnøkkelen (brukt av phase_a_check) er alltid det ORIGINALE
# skjemaet ($schema), aldri fixture-stien.
linkml_validate_job() {
    local schema="$1" domain="$2" name="$3" example="$4"
    [ -f "$example" ] || return 1
    local validate_schema="$schema"
    if lacks_tree_root "$domain"; then
        validate_schema="tests/fixtures/$name-fixture.yaml"
        [ -f "$validate_schema" ] || return 1
    fi
    echo "$validate_schema"
}

echo "test_make.sh — $(date)" > "$LOG"
echo "LINKML_IMAGE: $LINKML_IMAGE" >> "$LOG"
printf "Skjema (%d):\n" "${#SCHEMAS[@]}" >> "$LOG"
printf "  %s\n" "${SCHEMAS[@]}" >> "$LOG"

# ---------------------------------------------------------------------------
# Cleanup: slett berre katalogar som testane sjølve oppretta.
# Pre-registrer FØR testane startar.
# ---------------------------------------------------------------------------
declare -a TEST_DIRS=()
for schema in "${SCHEMAS[@]}"; do
    outdir=$(schema_outdir "$schema")
    [ -d "$outdir" ] || TEST_DIRS+=("$outdir")
done

cleanup() {
    for dir in "${TEST_DIRS[@]+"${TEST_DIRS[@]}"}"; do
        rm -rf "$dir"
    done
    rm -rf "$REPO_ROOT/tmp"
}
trap cleanup EXIT

# ---------------------------------------------------------------------------
# Parallell test-infrastruktur
# Skjema køyrer i parallell; testar per skjema køyrer sekvensielt.
# Dette avgrenser samtidige Podman-kontainerr til ~N-skjema og unngår
# Podman-database-lock ved for høg grad av parallelisme.
# ---------------------------------------------------------------------------
declare -a SCHEMA_PIDS=()
declare -a SCHEMA_LOGS=()

# Køyr ein enkelt test og skriv parseable RESULT-markørar til stdout.
# Set TEST_FILTER=<prefiks> for å køyre berre testar med namn som startar med prefikset.
_run_one() {
    local tname="$1"; shift
    if [[ -n "${TEST_FILTER:-}" && "$tname" != ${TEST_FILTER}* ]]; then
        return 0
    fi
    printf "  %-52s ..." "$tname" >&3
    echo "========================================"
    echo "TEST: $tname  ($(date '+%H:%M:%S'))"
    echo "========================================"
    if "$@" 2>&1; then
        printf " ${CLR_OK}OK${CLR_RST}\n" >&3
        echo "##RESULT:OK:$tname"
    else
        printf " ${CLR_ERR}FEIL${CLR_RST}\n" >&3
        echo "##RESULT:FAIL:$tname"
    fi
}

# Køyr alle testar for eit skjema sekvensielt (i ein bakgrunnsprosess)
run_schema_tests() {
    local schema="$1"
    local domain name outdir
    domain=$(schema_domain "$schema")
    name=$(schema_name "$schema")
    outdir=$(schema_outdir "$schema")
    local example="src/linkml/$domain/$name/examples/$name-eksempel.yaml"
    local tmplog
    tmplog=$(mktemp /tmp/test_make_schema_XXXXXX.log)

    echo "→ Startar testar for $name ..." >&3

    {
        _run_one "validate ($name)"        test_validate       "$schema"
        _run_one "gen-jsonld ($name)"      test_gen_jsonld     "$schema" "$outdir/$name-context.jsonld"
        _run_one "gen-python ($name)"      test_gen_python     "$schema" "$outdir/$name-model.py"
        _run_one "gen-jsonschema ($name)"  test_gen_jsonschema "$schema" "$outdir/$name-schema.json"
        _run_one "gen-rdf ($name)"         test_gen_rdf        "$schema" "$outdir/$name-schema.ttl" "$domain"
        _run_one "gen-erdiagram ($name)"   test_gen_erdiagram  "$schema" "$outdir/$name-erdiagram.md"
        _run_one "gen-docs ($name)"        test_gen_docs       "$schema" "$outdir/docs"
        _run_one "gen-shacl ($name)"       test_gen_shacl      "$schema" "$outdir/$name-shapes.ttl"
        _run_one "gen-owl ($name)"         test_gen_owl        "$schema" "$outdir/$name-ontology.ttl"
        _run_one "convert-rdf ($name)"     test_convert_rdf    "$schema" "$outdir/$name-eksempel.ttl" "$example" "$domain"
        _run_one "linkml-lint ($name)"     test_linkml_lint    "$schema"
        _run_one "linkml-validate ($name)" test_linkml_validate "$schema" "$domain" "$name"
        _run_one "gen-proto ($name)"              test_gen_proto             "$schema" "$outdir/$name-schema.proto"
        _run_one "gen-plantuml ($name)"           test_gen_plantuml          "$schema" "$outdir/diagrams/$name.puml" "$outdir/diagrams/$name.svg"
        _run_one "mcp-validate-instance ($name)"  test_mcp_validate_instance "$schema" "$domain" "$name"
        _run_one "roundtrip-json ($name)"  test_roundtrip_json "$schema" "$example" "$domain" "$name"
        _run_one "roundtrip-ttl ($name)"   test_roundtrip_ttl  "$schema" "$example" "$domain" "$name"
    } >> "$tmplog" 2>&1 &

    SCHEMA_PIDS+=($!)
    SCHEMA_LOGS+=("$tmplog")
}

wait_for_tests() {
    local pass=0 fail=0
    for i in "${!SCHEMA_PIDS[@]}"; do
        local pid="${SCHEMA_PIDS[$i]}"
        local tmplog="${SCHEMA_LOGS[$i]}"
        wait "$pid" || true  # always process log, uavhengig av exit-kode
        while IFS= read -r line; do
            if [[ "$line" == "##RESULT:OK:"* ]]; then
                pass=$((pass + 1))
            elif [[ "$line" == "##RESULT:FAIL:"* ]]; then
                local tname="${line#"##RESULT:FAIL:"}"
                fail=$((fail + 1))
                echo "--- output frå $tname ---" >&2
                grep -A 25 "TEST: $tname " "$tmplog" | tail -25 >&2 || true
            fi
        done < "$tmplog"
        sed 's/\x1b\[[0-9;]*m//g' "$tmplog" >> "$LOG"
        rm -f "$tmplog"
    done
    echo ""
    echo "Resultat: $pass OK, $fail feil"
    echo "Sjå $LOG for detaljar"
    [ "$fail" -eq 0 ]
}

# ---------------------------------------------------------------------------
# Fase A: batch-generer for ALLE skjema som skal testast, éin gong per
# generator (i staden for éin gong per skjema × generator). Gjenbruker den
# same batch-generate.py/batch-generate-instances.py-infrastrukturen som
# `make generate`/`make docs-publish` alt brukar i produksjon — amortiserer
# linkml/linkml_runtime sin importskatt (~8 s) over heile skjemalista i
# staden for å betale han på nytt for kvart einaste skjema × steg. Sjå
# specs/backlog/batch-validate-lint-test-per-skjema.md, Tiltak 3 Kategori
# A+B.
#
# Kategori C (linkml-lint, mcp-validate-instance) ER batcha her — sjå
# run_phase_a_lint()/run_phase_a_mcp_instance() lenger nede, som brukar
# batch-lint.py/batch-validate-instances.py i staden for
# batch-generate.py-makroane over.
#
# Kategori D (convert-rdf, roundtrip-json/roundtrip-ttl, linkml-validate)
# ER OGSÅ batcha her — sjå run_phase_a_convert_rdf()/
# run_phase_a_roundtrip_json()/run_phase_a_roundtrip_ttl()/
# run_phase_a_linkml_validate() lenger nede, som brukar batch-convert.py
# (linkml-convert-kall) og batch-linkml-validate.py (linkml.validator
# .validate()-API direkte).
# ---------------------------------------------------------------------------
declare -A PHASE_A_LOG

# Køyr eitt batcha make-mål for heile skjemalista.
# $1=nøkkel (brukt av phase_a_check)  $2=make-target  $3=testnamn-prefiks
# (for å respektere TEST_FILTER — same filtreringsregel som _run_one)
run_phase_a_step() {
    local key="$1" target="$2" prefix="$3"
    if [[ -n "${TEST_FILTER:-}" ]] \
        && [[ "$prefix" != "$TEST_FILTER"* ]] \
        && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
        return 0
    fi
    local logfile
    logfile=$(mktemp "$LOGDIR/phase_a_${key}_XXXXXX.log")
    echo "→ Fase A: $target (${#SCHEMAS[@]} skjema) ..." >&3
    make "$target" SCHEMAS="${SCHEMAS[*]}" > "$logfile" 2>&1 || true
    PHASE_A_LOG[$key]="$logfile"
    {
        echo "========================================"
        echo "FASE A: $target  ($(date '+%H:%M:%S'))"
        echo "========================================"
        cat "$logfile"
    } >> "$LOG"
}

# Kategori C, steg 1: linkml-lint, batcha via batch-lint.py --ignore-
# warnings (delt Linter/TerminalFormatter-sesjon for heile skjemalista).
# Direkte podman-kall (ikkje via `make lint`) — speglar at testen alltid
# har kalla `linkml lint` direkte med --ignore-warnings, ikkje via
# Makefile-målet (som manglar dette flagget og har strengare standard-
# semantikk, jf. Tiltak 2).
run_phase_a_lint() {
    local prefix="linkml-lint"
    if [[ -n "${TEST_FILTER:-}" ]] \
        && [[ "$prefix" != "$TEST_FILTER"* ]] \
        && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
        return 0
    fi
    local logfile
    logfile=$(mktemp "$LOGDIR/phase_a_lint_XXXXXX.log")
    echo "→ Fase A: linkml-lint --ignore-warnings (${#SCHEMAS[@]} skjema) ..." >&3
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        python3 src/assets/scripts/makefile/batch-lint.py \
            --config src/assets/containers/.linkmllint.yaml --ignore-warnings -- "${SCHEMAS[@]}" \
        > "$logfile" 2>&1 || true
    PHASE_A_LOG[lint]="$logfile"
    {
        echo "========================================"
        echo "FASE A: linkml-lint --ignore-warnings  ($(date '+%H:%M:%S'))"
        echo "========================================"
        cat "$logfile"
    } >> "$LOG"
}

# Kategori C, steg 2: mcp-validate-instance, batcha via
# batch-validate-instances.py (JSON-RPC-stdin-mekanismen frå
# batch-flatten-and-validate.py, mot validate_linkml_instance-verktøyet).
# Bruker schemaPath (lagt til i server.py saman med dette) i staden for den
# gamle gen-linkml --mergeimports+schemaText-flyten — fjernar eit heilt
# kontainarkall per skjema i tillegg til å batche sjølve MCP-kallet.
declare -A PHASE_A_MCP_INDEX  # schema -> jobb-indeks (berre sett for skjema som faktisk vart validerte)
PHASE_A_MCP_OUTDIR=""

run_phase_a_mcp_instance() {
    local prefix="mcp-validate-instance"
    if [[ -n "${TEST_FILTER:-}" ]] \
        && [[ "$prefix" != "$TEST_FILTER"* ]] \
        && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
        return 0
    fi
    local jobs=()
    local idx=0
    for schema in "${SCHEMAS[@]}"; do
        local domain name job
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        job=$(mcp_instance_job "$schema" "$domain" "$name") || continue
        local validate_schema example
        read -r validate_schema example <<< "$job"
        jobs+=("${validate_schema}=${example}")
        PHASE_A_MCP_INDEX["$schema"]="$idx"
        idx=$((idx + 1))
    done
    if [ "${#jobs[@]}" -eq 0 ]; then
        return 0
    fi
    local outdir
    outdir=$(mktemp -d "$LOGDIR/phase_a_mcp_XXXXXX")
    PHASE_A_MCP_OUTDIR="$outdir"
    echo "→ Fase A: mcp-validate-instance (${#jobs[@]} skjema) ..." >&3
    {
        echo "========================================"
        echo "FASE A: mcp-validate-instance  ($(date '+%H:%M:%S'))"
        echo "========================================"
        REPO_ROOT="$REPO_ROOT" VALIDATOR_DIR="$REPO_ROOT/src/mcp-linkml-validator" MCP_IMAGE="$MCP_IMAGE" \
            python3 src/mcp-linkml-validator/batch-validate-instances.py \
                --output-dir "$outdir" "${jobs[@]}" 2>&1 || true
    } >> "$LOG"
}

# Kategori D: convert-rdf, roundtrip-json, roundtrip-ttl (alle batcha via
# batch-convert.py, sjå den fila sin toppkommentar for grunngjeving) og
# linkml-validate (batcha via batch-linkml-validate.py). Same
# jobbliste/TSV-mønster som batch-flatten-and-validate.py etablerte for
# heterogene jobbar.
_run_phase_a_convert_batch() {
    local key="$1" jobs_tsv="$2" label="$3"
    local logfile
    logfile=$(mktemp "$LOGDIR/phase_a_${key}_XXXXXX.log")
    echo "→ Fase A: $label ($(wc -l < "$jobs_tsv") jobb(ar)) ..." >&3
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        python3 src/assets/scripts/makefile/batch-convert.py --jobs-tsv "/work/$jobs_tsv" \
        > "$logfile" 2>&1 || true
    PHASE_A_LOG[$key]="$logfile"
    rm -f "$jobs_tsv"
    {
        echo "========================================"
        echo "FASE A: $label  ($(date '+%H:%M:%S'))"
        echo "========================================"
        cat "$logfile"
    } >> "$LOG"
}

run_phase_a_convert_rdf() {
    local prefix="convert-rdf"
    if [[ -n "${TEST_FILTER:-}" ]] \
        && [[ "$prefix" != "$TEST_FILTER"* ]] \
        && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
        return 0
    fi
    local jobs_tsv
    jobs_tsv=$(mktemp "$LOGDIR/phase_a_convert_rdf_jobs_XXXXXX.tsv")
    local has_jobs=0
    for schema in "${SCHEMAS[@]}"; do
        local domain name example outdir
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        example="src/linkml/$domain/$name/examples/$name-eksempel.yaml"
        outdir=$(schema_outdir "$schema")
        convert_rdf_job "$schema" "$domain" "$name" "$example" || continue
        printf '%s\t%s\t%s\t%s\n' "$schema" "$example" "ttl" "$outdir/$name-eksempel.ttl" >> "$jobs_tsv"
        has_jobs=1
    done
    if [ "$has_jobs" -eq 0 ]; then
        rm -f "$jobs_tsv"
        return 0
    fi
    _run_phase_a_convert_batch convert_rdf "$jobs_tsv" "convert-rdf"
}

run_phase_a_roundtrip_json() {
    local prefix="roundtrip-json"
    if [[ -n "${TEST_FILTER:-}" ]] \
        && [[ "$prefix" != "$TEST_FILTER"* ]] \
        && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
        return 0
    fi
    local jobs_tsv
    jobs_tsv=$(mktemp "$LOGDIR/phase_a_roundtrip_json_jobs_XXXXXX.tsv")
    local has_jobs=0
    for schema in "${SCHEMAS[@]}"; do
        local domain name example rtdir
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        example="src/linkml/$domain/$name/examples/$name-eksempel.yaml"
        roundtrip_json_job "$schema" "$domain" "$name" "$example" || continue
        rtdir="tmp/roundtrip-json/$name"
        printf '%s\t%s\t%s\t%s\n' "$schema" "$example" "json" "$rtdir/a.json" >> "$jobs_tsv"
        printf '%s\t%s\t%s\t%s\n' "$schema" "$rtdir/a.json" "yaml" "$rtdir/b.yaml" >> "$jobs_tsv"
        printf '%s\t%s\t%s\t%s\n' "$schema" "$rtdir/b.yaml" "json" "$rtdir/c.json" >> "$jobs_tsv"
        has_jobs=1
    done
    if [ "$has_jobs" -eq 0 ]; then
        rm -f "$jobs_tsv"
        return 0
    fi
    _run_phase_a_convert_batch roundtrip_json "$jobs_tsv" "roundtrip-json"
}

run_phase_a_roundtrip_ttl() {
    local prefix="roundtrip-ttl"
    if [[ -n "${TEST_FILTER:-}" ]] \
        && [[ "$prefix" != "$TEST_FILTER"* ]] \
        && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
        return 0
    fi
    local jobs_tsv
    jobs_tsv=$(mktemp "$LOGDIR/phase_a_roundtrip_ttl_jobs_XXXXXX.tsv")
    local has_jobs=0
    for schema in "${SCHEMAS[@]}"; do
        local domain name example rtdir
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        example="src/linkml/$domain/$name/examples/$name-eksempel.yaml"
        roundtrip_ttl_job "$schema" "$domain" "$name" "$example" || continue
        rtdir="tmp/roundtrip-ttl/$name"
        printf '%s\t%s\t%s\t%s\n' "$schema" "$example" "json" "$rtdir/a.json" >> "$jobs_tsv"
        printf '%s\t%s\t%s\t%s\n' "$schema" "$example" "ttl" "$rtdir/b.ttl" >> "$jobs_tsv"
        printf '%s\t%s\t%s\t%s\n' "$schema" "$rtdir/b.ttl" "yaml" "$rtdir/c.yaml" >> "$jobs_tsv"
        printf '%s\t%s\t%s\t%s\n' "$schema" "$rtdir/c.yaml" "json" "$rtdir/d.json" >> "$jobs_tsv"
        has_jobs=1
    done
    if [ "$has_jobs" -eq 0 ]; then
        rm -f "$jobs_tsv"
        return 0
    fi
    _run_phase_a_convert_batch roundtrip_ttl "$jobs_tsv" "roundtrip-ttl"
}

run_phase_a_linkml_validate() {
    local prefix="linkml-validate"
    if [[ -n "${TEST_FILTER:-}" ]] \
        && [[ "$prefix" != "$TEST_FILTER"* ]] \
        && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
        return 0
    fi
    local jobs_tsv
    jobs_tsv=$(mktemp "$LOGDIR/phase_a_linkml_validate_jobs_XXXXXX.tsv")
    local has_jobs=0
    for schema in "${SCHEMAS[@]}"; do
        local domain name example validate_schema
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        example="src/linkml/$domain/$name/examples/$name-eksempel.yaml"
        validate_schema=$(linkml_validate_job "$schema" "$domain" "$name" "$example") || continue
        printf '%s\t%s\t%s\n' "$schema" "$validate_schema" "$example" >> "$jobs_tsv"
        has_jobs=1
    done
    if [ "$has_jobs" -eq 0 ]; then
        rm -f "$jobs_tsv"
        return 0
    fi
    local logfile
    logfile=$(mktemp "$LOGDIR/phase_a_linkml_validate_XXXXXX.log")
    echo "→ Fase A: linkml-validate ($(wc -l < "$jobs_tsv") skjema) ..." >&3
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        python3 src/assets/scripts/makefile/batch-linkml-validate.py --jobs-tsv "/work/$jobs_tsv" \
        > "$logfile" 2>&1 || true
    PHASE_A_LOG[linkml_validate]="$logfile"
    rm -f "$jobs_tsv"
    {
        echo "========================================"
        echo "FASE A: linkml-validate  ($(date '+%H:%M:%S'))"
        echo "========================================"
        cat "$logfile"
    } >> "$LOG"
}

run_phase_a() {
    run_phase_a_step validate   validate           "validate"
    run_phase_a_step jsonld     gen-jsonld-context  "gen-jsonld"
    run_phase_a_step python     gen-python          "gen-python"
    run_phase_a_step jsonschema gen-jsonschema      "gen-jsonschema"
    run_phase_a_step rdf        gen-rdf             "gen-rdf"
    run_phase_a_step erdiagram  gen-erdiagram       "gen-erdiagram"
    run_phase_a_step docs       gen-docs            "gen-docs"
    run_phase_a_step shacl      gen-shacl           "gen-shacl"
    run_phase_a_step owl        gen-owl             "gen-owl"
    run_phase_a_step proto      gen-proto           "gen-proto"
    run_phase_a_step plantuml   gen-plantuml        "gen-plantuml"
    run_phase_a_lint
    run_phase_a_mcp_instance
    run_phase_a_convert_rdf
    run_phase_a_roundtrip_json
    run_phase_a_roundtrip_ttl
    run_phase_a_linkml_validate
}

# Sjekk om eit gitt skjema feila i Fase A-batchen for ein gjeven generator.
# batch-generate.py/batch-generate-instances.py/batch-lint.py (i
# --ignore-warnings-modus) skriv ::error file=<schema>:: for per-skjema-
# isolerte feil (sjå spec, Tiltak 1/2) — grep denne markøren i staden for å
# stole på heile batchen sin exit-kode, sidan éitt skjema sin feil elles
# ville sjå ut som at ALLE skjema i batchen feila.
phase_a_check() {
    local key="$1" schema="$2"
    local logfile="${PHASE_A_LOG[$key]:-}"
    [ -n "$logfile" ] || return 0  # Fase A køyrde ikkje (TEST_FILTER) — _run_one hoppar uansett over kallaren
    local err
    err=$(grep "::error file=$schema::" "$logfile" 2>/dev/null || true)
    if [ -n "$err" ]; then
        echo "$err"
        return 1
    fi
    return 0
}

# Sjekk resultatet av mcp-validate-instance-batchen for eit gitt skjema.
# Ulikt phase_a_check() (som grep-ar ein loggtekst) les denne resultat-
# JSON-fila batch-validate-instances.py skreiv for dette skjemaet sin jobb.
phase_a_mcp_check() {
    local schema="$1"
    local idx="${PHASE_A_MCP_INDEX[$schema]:-}"
    [ -n "$idx" ] || return 0  # ikkje ein del av batchen — kallaren har alt avgjort å hoppe over
    local resultfile="$PHASE_A_MCP_OUTDIR/$idx.json"
    if [ ! -f "$resultfile" ]; then
        echo "Manglar resultatfil for $schema: $resultfile"
        return 1
    fi
    python3 -c "
import json, sys
d = json.load(open('$resultfile'))
errors = [i for i in d.get('issues', []) if i['severity'] == 'error']
if errors:
    for e in errors:
        print(f\"[ERROR] {e['target']}: {e['message']}\")
    sys.exit(1)
sys.exit(0)
"
}

# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------
assert_file_nonempty() {
    [ -f "$1" ] || { echo "Fil manglar: $1"; return 1; }
    [ -s "$1" ] || { echo "Fil er tom: $1"; return 1; }
}

assert_json_valid() {
    python3 -m json.tool "$1" > /dev/null || { echo "Ugyldig JSON: $1"; return 1; }
}

assert_json_has_key() {
    python3 -c "import json; d=json.load(open('$1')); assert '$2' in d, '$2 manglar i $1'" \
        || return 1
}

assert_rdf_valid() {
    local f="$1"
    podman run --rm \
        -v "$REPO_ROOT:/work" \
        -w /work \
        -e PYTHONWARNINGS=ignore \
        "$LINKML_IMAGE" \
        python3 -c "
import rdflib
g = rdflib.Graph()
g.parse('/work/$f')
assert len(g) > 0, 'Graf er tom: $f'
print('tripler:', len(g))
"
}

# ---------------------------------------------------------------------------
# Testfunksjonar — generiske, tar schema og outfile som argument
# ---------------------------------------------------------------------------
test_validate() {
    phase_a_check validate "$1" || return 1
}

test_gen_jsonld() {
    local schema="$1" outfile="$2"
    phase_a_check jsonld "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_json_valid "$outfile" || return 1
    assert_json_has_key "$outfile" "@context" || return 1
}

test_gen_python() {
    local schema="$1" outfile="$2"
    phase_a_check python "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    python3 -m py_compile "$outfile" || { echo "Syntaksfeil i $outfile"; return 1; }
}

test_gen_jsonschema() {
    local schema="$1" outfile="$2"
    phase_a_check jsonschema "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_json_valid "$outfile" || return 1
    python3 -c "
import json
d = json.load(open('$outfile'))
assert '\$defs' in d or 'properties' in d, '\$defs og properties manglar i $outfile'
" || return 1
}

test_gen_rdf() {
    local schema="$1" outfile="$2" domain="$3"
    phase_a_check rdf "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_gen_erdiagram() {
    local schema="$1" outfile="$2"
    phase_a_check erdiagram "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    grep -q '```mermaid' "$outfile" || { echo "Manglar mermaid-blokk i $outfile"; return 1; }
    grep -q 'erDiagram'  "$outfile" || { echo "Manglar erDiagram i $outfile"; return 1; }
}

test_gen_docs() {
    local schema="$1" docsdir="$2"
    phase_a_check docs "$schema" || return 1
    [ -d "$docsdir" ] || { echo "Katalog manglar: $docsdir"; return 1; }
    local mdcount
    mdcount=$(find "$docsdir" -name "*.md" | wc -l)
    [ "$mdcount" -gt 0 ] || { echo "Ingen .md-filer i $docsdir"; return 1; }
    while IFS= read -r f; do
        [ -s "$f" ]       || { echo "Tom fil: $f"; return 1; }
        grep -q '^#' "$f" || { echo "Manglar #-overskrift: $f"; return 1; }
    done < <(find "$docsdir" -name "*.md")
}

test_gen_shacl() {
    local schema="$1" outfile="$2"
    phase_a_check shacl "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_gen_owl() {
    local schema="$1" outfile="$2"
    phase_a_check owl "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_linkml_lint() {
    phase_a_check lint "$1" || return 1
}

test_linkml_validate() {
    local schema="$1" domain="$2" name="$3"
    local example="src/linkml/$domain/$name/examples/$name-eksempel.yaml"
    local validate_schema
    if ! validate_schema=$(linkml_validate_job "$schema" "$domain" "$name" "$example"); then
        if [ ! -f "$example" ]; then
            echo "Ingen eksempelfil: $example (hoppar over)"
        else
            echo "Ingen fixture: tests/fixtures/$name-fixture.yaml (hoppar over)"
        fi
        return 0
    fi
    phase_a_check linkml_validate "$schema" || return 1
}

test_roundtrip_json() {
    local schema="$1" example="$2" domain="$3" name="$4"

    if ! roundtrip_json_job "$schema" "$domain" "$name" "$example"; then
        if lacks_tree_root "$domain"; then
            echo "Hoppar over roundtrip-json for $domain (ingen tree_root)"
        else
            echo "Ingen eksempelfil: $example (hoppar over)"
        fi
        return 0
    fi
    phase_a_check roundtrip_json "$schema" || return 1

    local rtdir="tmp/roundtrip-json/$name"
    python3 - "$rtdir/a.json" "$rtdir/c.json" << 'PYEOF'
import json, sys
a = json.load(open(sys.argv[1]))
b = json.load(open(sys.argv[2]))
if a != b:
    import pprint
    print("ROUNDTRIP-AVVIK (yaml→json→yaml→json):")
    print("Forventa:", pprint.pformat(a)[:500])
    print("Fekk:    ", pprint.pformat(b)[:500])
    sys.exit(1)
print("Roundtrip OK")
PYEOF
}

test_roundtrip_ttl() {
    local schema="$1" example="$2" domain="$3" name="$4"

    if ! roundtrip_ttl_job "$schema" "$domain" "$name" "$example"; then
        if lacks_tree_root "$domain"; then
            echo "Hoppar over roundtrip-ttl for $domain (ingen tree_root)"
        elif [[ "$name" == "ngr-adresse" || "$name" == "ngr-eiendom" || "$name" == "ngr-virksomhet" ]]; then
            echo "Hoppar over roundtrip-ttl for $name (BUG-2: linkml-runtime inlined_as_list-bug)"
        elif [[ "$name" == "brreg-begrepskatalog" || "$name" == "brreg-modellkatalog" || \
                "$name" == "digdir-modellkatalog" || "$name" == "novari-modellkatalog" || \
                "$name" == "ksdigital-modellkatalog" || "$name" == "skatteetaten-modellkatalog" || \
                "$name" == "kartverket-modellkatalog" ]]; then
            echo "Hoppar over roundtrip-ttl for $name (BUG-1: linkml-runtime LangString-bug)"
        else
            echo "Ingen eksempelfil: $example (hoppar over)"
        fi
        return 0
    fi
    phase_a_check roundtrip_ttl "$schema" || return 1

    local rtdir="tmp/roundtrip-ttl/$name"
    python3 - "$rtdir/a.json" "$rtdir/d.json" << 'PYEOF'
import json, sys
def sort_lists(obj):
    if isinstance(obj, dict):
        return {k: sort_lists(v) for k, v in obj.items()}
    if isinstance(obj, list):
        items = [sort_lists(i) for i in obj]
        if items and isinstance(items[0], dict) and 'id' in items[0]:
            items = sorted(items, key=lambda x: str(x.get('id', '')))
        return items
    return obj
a = sort_lists(json.load(open(sys.argv[1])))
b = sort_lists(json.load(open(sys.argv[2])))
if a != b:
    import pprint
    print("ROUNDTRIP-AVVIK (yaml→ttl→yaml→json):")
    print("Forventa:", pprint.pformat(a)[:500])
    print("Fekk:    ", pprint.pformat(b)[:500])
    sys.exit(1)
print("Roundtrip OK")
PYEOF
}

test_convert_rdf() {
    local schema="$1" outfile="$2" example="$3" domain="$4"
    local name
    name=$(schema_name "$schema")
    if ! convert_rdf_job "$schema" "$domain" "$name" "$example"; then
        local build_yaml="$(dirname "$schema")/build.yaml"
        if lacks_tree_root "$domain"; then
            echo "Hoppar over convert-rdf for $domain (ingen tree_root)"
        elif [ -f "$build_yaml" ] && grep -q "^  example_rdf: false" "$build_yaml"; then
            echo "Hoppar over convert-rdf for $name (example_rdf: false)"
        elif [[ "$name" == "ngr-adresse" || "$name" == "ngr-eiendom" || "$name" == "ngr-virksomhet" ]]; then
            echo "Hoppar over convert-rdf for $name (BUG-2: linkml-runtime inlined_as_list-bug)"
        else
            echo "Ingen eksempelfil: $example (hoppar over)"
        fi
        return 0
    fi
    phase_a_check convert_rdf "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_gen_proto() {
    local schema="$1" outfile="$2"
    phase_a_check proto "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    grep -qE 'syntax\s*=\s*"proto3"' "$outfile" || { echo "Manglar proto3-syntaksdeklarasjon i $outfile"; return 1; }
}

test_gen_plantuml() {
    local schema="$1" pumlfile="$2" svgfile="$3"
    phase_a_check plantuml "$schema" || return 1
    assert_file_nonempty "$pumlfile" || return 1
    assert_file_nonempty "$svgfile" || return 1
    grep -q '@startuml' "$pumlfile" || { echo "Manglar @startuml i $pumlfile"; return 1; }
    grep -q '<svg' "$svgfile" || { echo "Manglar <svg> i $svgfile"; return 1; }
}

test_mcp_validate_instance() {
    local schema="$1" domain="$2" name="$3"
    local job
    if ! job=$(mcp_instance_job "$schema" "$domain" "$name"); then
        if lacks_tree_root "$domain"; then
            echo "Hoppar over mcp-validate-instance for $domain (ingen tree_root)"
        else
            echo "Ingen eksempelfil: src/linkml/$domain/$name/examples/$name-eksempel.yaml (hoppar over)"
        fi
        return 0
    fi
    phase_a_mcp_check "$schema" || return 1
}

test_roundtrip_json_schema() {
    local json_schema="$1"
    local basename_ns=$(basename "$json_schema" .json)
    basename_ns="${basename_ns%.schema}"

    # Steg 1: JSON Schema → LinkML
    local tmp_linkml
    tmp_linkml=$(mktemp "$REPO_ROOT/tmp/rt_linkml_XXXXXX.yaml")

    python3 -c "
import json
content = open('$json_schema').read()
msgs = [
  {'jsonrpc':'2.0','id':1,'method':'initialize','params':{}},
  {'jsonrpc':'2.0','id':2,'method':'tools/call','params':{
    'name':'generate_linkml',
    'arguments':{
      'inputFormat':'json-schema',
      'inputContent':content,
      'schemaId':'https://example.org/roundtrip-test',
      'schemaName':'roundtrip_test',
      'profile':'bronze'
    }
  }}
]
print('\n'.join(json.dumps(m) for m in msgs))
" | podman run -i --rm \
        -v "$REPO_ROOT/src/mcp-linkml-modell-utkast/server.py:/app/server.py:ro" \
        -v "$REPO_ROOT/src/mcp-linkml-modell-utkast/converter.py:/app/converter.py:ro" \
        -v "$REPO_ROOT/src/mcp-linkml-modell-utkast/validator.py:/app/validator.py:ro" \
        -v "$REPO_ROOT/src/mcp-linkml-modell-utkast/profiles:/app/profiles:ro" \
        mcp-linkml-modell-utkast \
    | python3 -c "
import json, sys
for line in sys.stdin:
    try:
        r = json.loads(line)
    except json.JSONDecodeError:
        continue
    if r.get('id') == 2:
        result = json.loads(r['result']['content'][0]['text'])
        with open('$tmp_linkml', 'w') as f:
            f.write(result['linkmlSchema'])
        sys.exit(0)
sys.exit(1)
" || { echo "JSON Schema → LinkML feila"; rm -f "$tmp_linkml"; return 1; }

    # Steg 2: LinkML → JSON Schema
    local tmp_json_schema
    tmp_json_schema=$(mktemp "$REPO_ROOT/tmp/rt_jsonschema_XXXXXX.json")

    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        gen-json-schema "tmp/$(basename "$tmp_linkml")" \
        > "$tmp_json_schema" \
        || { echo "LinkML → JSON Schema feila"; rm -f "$tmp_linkml" "$tmp_json_schema"; return 1; }

    # Steg 3: Semantisk samanlikning (ekskluder containerklassen)
    python3 - "$json_schema" "$tmp_json_schema" << 'PYEOF'
import json, sys

def extract_semantic_definitions(schema):
    """
    Hent ut semantiske definisjonar frå JSON Schema.
    Ekskluderer containerklassen (tree_root) som berre er for serialisering.
    Returnerer både klasser (type=object) og typar (type=string/number/etc).
    """
    defs = schema.get('$defs', schema.get('definitions', {}))

    # Identifiser containerklassen: har berre properties med type=array av objekt
    container_class = None
    for class_name, class_def in defs.items():
        props = class_def.get('properties', {})
        if not props:
            continue

        # Sjekk om alle properties er arrays av objekt-referansar
        all_array_refs = True
        for prop_name, prop_def in props.items():
            if prop_def.get('type') != 'array':
                all_array_refs = False
                break
            items = prop_def.get('items', {})
            if '$ref' not in items:
                all_array_refs = False
                break

        if all_array_refs and len(props) > 3:  # Containerklasse har typisk mange properties
            container_class = class_name
            break

    # Returner alle definisjonar utanom containerklassen
    semantic_defs = {k: v for k, v in defs.items() if k != container_class}
    return semantic_defs

def is_type_definition(definition):
    """Sjekk om ein definisjon er ein type (ikkje ein klasse)"""
    typ = definition.get('type')
    # Typar har type=string/number/integer/boolean utan properties
    return typ in ('string', 'number', 'integer', 'boolean') and 'properties' not in definition

def extract_types_and_classes(defs):
    """Splitt definisjonar i typar og klasser"""
    types = {k: v for k, v in defs.items() if is_type_definition(v)}
    classes = {k: v for k, v in defs.items() if not is_type_definition(v)}
    return types, classes

def normalize_class(class_def):
    """Normaliser ein klassedefinisjon for samanlikning"""
    if not isinstance(class_def, dict):
        return class_def

    normalized = {}
    for key, value in class_def.items():
        # Hopp over metadata
        if key in ['title', 'description', '$id', 'id']:
            continue

        if isinstance(value, dict):
            normalized[key] = normalize_class(value)
        elif isinstance(value, list):
            # Sorter lister for rekkefølgje-uavhengig samanlikning
            normalized[key] = sorted(value) if all(isinstance(x, str) for x in value) else value
        else:
            normalized[key] = value

    return normalized

def normalize_type(type_val):
    """Normaliser type-verdi for samanlikning (handter array med null)"""
    if isinstance(type_val, list):
        # Fjern 'null' frå type-array for samanlikning
        non_null = [t for t in type_val if t != 'null']
        return non_null[0] if len(non_null) == 1 else non_null
    return type_val

def compare_property(orig_prop, gen_prop, prop_name):
    """Samanlikn ein enkelt property mellom to klassedefinisjonar"""
    # Hopp over samanlikning av properties med oneOf/anyOf/allOf — desse er ikkje fullt støtta
    if 'oneOf' in orig_prop or 'anyOf' in orig_prop or 'allOf' in orig_prop:
        return None

    orig_type = normalize_type(orig_prop.get('type'))
    gen_type = normalize_type(gen_prop.get('type'))

    # Type-samanlikning
    # Aksepter at $ref kan bli inline-type (t.d. $ref → type=string med pattern)
    if orig_type != gen_type:
        # Aksepter null i anyOf som ekvivalent til ikkje-required
        if 'anyOf' in gen_prop:
            pass  # Ignorer for no
        elif '$ref' in orig_prop and gen_type:
            # Original hadde $ref (til ein type), generert har inline type
            pass  # Dette er OK — typen vart inlined
        elif orig_type and '$ref' in gen_prop:
            # Original hadde inline type, generert har $ref
            pass  # Dette er OK
        elif orig_type is None and '$ref' in orig_prop:
            # Original har berre $ref, ingen type
            pass  # OK
        elif gen_type is None and '$ref' in gen_prop:
            # Generert har berre $ref, ingen type
            pass  # OK
        else:
            return f"Ulik type for '{prop_name}': {orig_type} vs {gen_type}"

    # $ref-samanlikning (berre når begge har $ref)
    if '$ref' in orig_prop and '$ref' in gen_prop:
        orig_ref = orig_prop['$ref'].split('/')[-1]
        gen_ref = gen_prop['$ref'].split('/')[-1]
        if orig_ref != gen_ref:
            return f"Ulik $ref for '{prop_name}': {orig_ref} vs {gen_ref}"

    # Pattern-samanlikning
    if 'pattern' in orig_prop and 'pattern' in gen_prop:
        if orig_prop['pattern'] != gen_prop['pattern']:
            return f"Ulik pattern for '{prop_name}'"

    # Enum-samanlikning
    if 'enum' in orig_prop and 'enum' in gen_prop:
        if set(orig_prop['enum']) != set(gen_prop['enum']):
            return f"Ulike enum-verdiar for '{prop_name}'"

    return None

def compare_type_definition(orig_type, gen_type, type_name):
    """Samanlikn ein typedefinisjon mellom original og generert"""
    orig_base_type = orig_type.get('type')
    gen_base_type = gen_type.get('type')

    if orig_base_type != gen_base_type:
        return f"Type '{type_name}': ulik basetype {orig_base_type} vs {gen_base_type}"

    # Pattern-samanlikning
    if 'pattern' in orig_type and 'pattern' in gen_type:
        if orig_type['pattern'] != gen_type['pattern']:
            return f"Type '{type_name}': ulik pattern"

    # Enum-samanlikning
    if 'enum' in orig_type and 'enum' in gen_type:
        if set(orig_type['enum']) != set(gen_type['enum']):
            return f"Type '{type_name}': ulike enum-verdiar"

    # Format-samanlikning
    if 'format' in orig_type and 'format' in gen_type:
        if orig_type['format'] != gen_type['format']:
            return f"Type '{type_name}': ulik format"

    return None

def schemas_equivalent(original, generated):
    """
    Sjekk om to JSON Schema er semantisk ekvivalente.
    Ekskluderer containerklassen og fokuserer på semantiske definisjonar.
    """
    orig_defs = extract_semantic_definitions(original)
    gen_defs = extract_semantic_definitions(generated)

    # Splitt i typar og klasser
    orig_types, orig_classes = extract_types_and_classes(orig_defs)
    gen_types, gen_classes = extract_types_and_classes(gen_defs)

    # ===== Samanlikn typar =====
    orig_type_names = set(orig_types.keys())
    gen_type_names = set(gen_types.keys())

    missing_types = orig_type_names - gen_type_names

    # VIKTIG: LinkML-typar vert ikkje eksporterte tilbake til JSON Schema av gen-json-schema
    # Om ein type manglar i generert, men finst som inline-constraint, tel vi det som OK
    if missing_types:
        # Pragmatisk: godta at typar kan vere inlined
        print(f"  Info: Typar ikkje eksporterte til $defs (OK, kan vere inlined): {missing_types}")

    # Ekstra typar er OK
    if gen_type_names - orig_type_names:
        print(f"  Info: Ekstra typar (OK): {gen_type_names - orig_type_names}")

    # Samanlikn felles typar
    for type_name in orig_type_names & gen_type_names:
        error = compare_type_definition(orig_types[type_name], gen_types[type_name], type_name)
        if error:
            return False, error

    # ===== Samanlikn klasser =====
    orig_class_names = set(orig_classes.keys())
    gen_class_names = set(gen_classes.keys())

    # Bygg ein mapping frå normaliserte namn (utan _\d+) til faktiske namn
    # gen-json-schema kan normalisere Foo_2 → Foo2
    import re as _re
    def normalize_class_name(name):
        return _re.sub(r'_(\d+)$', r'\1', name)

    gen_class_map = {normalize_class_name(name): name for name in gen_class_names}

    missing_classes = orig_class_names - gen_class_names

    # Filtrer ut klasser med allOf/anyOf/oneOf — desse er ikkje fullt støtta i konverteringa
    unsupported_classes = set()
    normalized_missing = set()

    for class_name in missing_classes:
        class_def = orig_classes[class_name]
        if 'allOf' in class_def or 'anyOf' in class_def or 'oneOf' in class_def:
            unsupported_classes.add(class_name)
        else:
            # Sjekk om klassen finst med normalisert namn (t.d. Foo_2 → Foo2)
            normalized = normalize_class_name(class_name)
            if normalized in gen_class_map:
                # OK — finst med normalisert namn
                print(f"  Info: Klasse '{class_name}' finst som '{gen_class_map[normalized]}' (normalisert)")
            else:
                normalized_missing.add(class_name)

    if unsupported_classes:
        print(f"  Info: Klasser med allOf/anyOf/oneOf (ikkje fullt støtta, hoppar over): {unsupported_classes}")

    if normalized_missing:
        return False, f"Manglar klasser: {normalized_missing}"

    # Ekstra klasser er OK (LinkML kan generere hjelpeklasser)
    if gen_class_names - orig_class_names:
        print(f"  Info: Ekstra klasser (OK): {gen_class_names - orig_class_names}")

    # Samanlikn kvar felles klasse (ekskluder allOf/anyOf/oneOf-klasser)
    for class_name in orig_class_names:
        # Hopp over klasser som vart filtrerte ut (allOf/anyOf/oneOf eller normaliserte)
        if class_name in unsupported_classes:
            continue

        # Finn den genererte klassen (kan vere normalisert, t.d. Foo_2 → Foo2)
        normalized = normalize_class_name(class_name)
        gen_class_name = gen_class_map.get(normalized) or class_name

        if gen_class_name not in gen_classes:
            continue

        orig_class = orig_classes[class_name]
        gen_class = gen_classes[gen_class_name]

        # Samanlikn properties
        orig_props = orig_class.get('properties', {})
        gen_props = gen_class.get('properties', {})

        orig_prop_names = set(orig_props.keys())
        gen_prop_names = set(gen_props.keys())

        # Normaliser property-namn (bindestrek → underscore, same som _sanitize_slot_name)
        def normalize_prop_name(name):
            return name.replace('-', '_')

        gen_prop_map = {normalize_prop_name(name): name for name in gen_prop_names}

        missing_props = set()
        normalized_props = set()

        for prop_name in orig_prop_names:
            normalized = normalize_prop_name(prop_name)
            if prop_name not in gen_prop_names and normalized not in gen_prop_map:
                missing_props.add(prop_name)
            elif prop_name != normalized and normalized in gen_prop_map:
                # Property finst med normalisert namn
                normalized_props.add(prop_name)

        if normalized_props:
            normalized_str = ', '.join(f"'{p}' → '{normalize_prop_name(p)}'" for p in normalized_props)
            print(f"  Info: Klasse '{class_name}': properties normaliserte ({normalized_str})")

        if missing_props:
            return False, f"Klasse '{class_name}': manglar properties {missing_props}"

        extra_props = gen_prop_names - orig_prop_names - set(normalize_prop_name(p) for p in orig_prop_names)
        if extra_props:
            print(f"  Info: Klasse '{class_name}': ekstra properties (OK): {extra_props}")

        # Samanlikn felles properties i detalj
        for prop_name in orig_prop_names:
            # Finn den genererte property (kan vere normalisert)
            normalized = normalize_prop_name(prop_name)
            gen_prop_name = gen_prop_map.get(normalized) or prop_name

            if gen_prop_name not in gen_props:
                continue  # Allereie handtert i missing_props-sjekken

            error = compare_property(orig_props[prop_name], gen_props[gen_prop_name], prop_name)
            if error:
                return False, f"Klasse '{class_name}': {error}"

        # Samanlikn required-felt (normaliser property-namn)
        orig_req = set(orig_class.get('required', []))
        gen_req = set(gen_class.get('required', []))

        # Normaliser orig_req for samanlikning
        orig_req_normalized = {normalize_prop_name(p) for p in orig_req}

        missing_req = orig_req_normalized - gen_req
        # Fjern 'id' frå ekstra required (LinkML legg til dette)
        extra_req = (gen_req - orig_req_normalized) - {'id'}

        if missing_req:
            # Finn originale namn (før normalisering)
            missing_orig = {p for p in orig_req if normalize_prop_name(p) in missing_req}
            return False, f"Klasse '{class_name}': manglar required-felt {missing_orig}"
        if extra_req:
            print(f"  Info: Klasse '{class_name}': ekstra required-felt (OK): {extra_req}")

    return True, None

try:
    original = json.load(open(sys.argv[1]))
    generated = json.load(open(sys.argv[2]))

    equivalent, diff = schemas_equivalent(original, generated)

    if equivalent:
        print("JSON Schema roundtrip OK (semantiske klasser bevarte)")
        sys.exit(0)
    else:
        print(f"JSON Schema roundtrip AVVIK:\n{diff}")
        sys.exit(1)
except Exception as e:
    import traceback
    print(f"Samanlikning feila: {e}")
    traceback.print_exc()
    sys.exit(1)
PYEOF
    local rc=$?
    rm -f "$tmp_linkml" "$tmp_json_schema"
    return $rc
}

# ---------------------------------------------------------------------------
# JSON Schema roundtrip-testar (køyrer separat frå skjema-testar)
# ---------------------------------------------------------------------------
run_json_schema_tests() {
    if [[ "${TEST_FILTER:-}" != "roundtrip-json-schema" ]]; then
        return 0
    fi

    local json_schema_filter="${1:-}"
    local json_schemas=()

    if [ -n "$json_schema_filter" ]; then
        if [ ! -f "$json_schema_filter" ]; then
            echo "Feil: JSON Schema ikkje funne: $json_schema_filter" >&2
            exit 1
        fi
        json_schemas=("$json_schema_filter")
    else
        # Finn alle JSON Schema i src/tmp/
        mapfile -t json_schemas < <(find src/tmp -name "*.json" -o -name "*.schema.json" | sort)
    fi

    if [ "${#json_schemas[@]}" -eq 0 ]; then
        echo "Ingen JSON Schema funne i src/tmp/" >&2
        return 0
    fi

    echo "JSON Schema roundtrip-testar (${#json_schemas[@]} filer):" >&3

    for json_schema in "${json_schemas[@]}"; do
        local basename_js=$(basename "$json_schema")
        local tmplog
        tmplog=$(mktemp /tmp/test_make_jsonschema_XXXXXX.log)

        {
            _run_one "roundtrip-json-schema ($basename_js)" test_roundtrip_json_schema "$json_schema"
        } >> "$tmplog" 2>&1 &

        SCHEMA_PIDS+=($!)
        SCHEMA_LOGS+=("$tmplog")
    done
}

# ---------------------------------------------------------------------------
# Start ein bakgrunnsprosess per skjema; testar per skjema køyrer sekvensielt
# ---------------------------------------------------------------------------
exec 3>&1

# Køyr JSON Schema roundtrip-testar (dersom TEST_FILTER=roundtrip-json-schema)
run_json_schema_tests "$SCHEMA_FILTER"

# Køyr vanlige skjema-testar (dersom TEST_FILTER != roundtrip-json-schema)
if [[ "${TEST_FILTER:-}" != "roundtrip-json-schema" ]]; then
    run_phase_a
    for schema in "${SCHEMAS[@]}"; do
        run_schema_tests "$schema"
    done
fi

wait_for_tests
