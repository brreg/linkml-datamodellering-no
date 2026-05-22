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

# Køyr ein enkelt test og skriv parseable RESULT-markørar til stdout
_run_one() {
    local tname="$1"; shift
    echo "========================================"
    echo "TEST: $tname  ($(date '+%H:%M:%S'))"
    echo "========================================"
    if "$@" 2>&1; then
        echo "##RESULT:OK:$tname"
    else
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
    local tmplog
    tmplog=$(mktemp /tmp/test_make_schema_XXXXXX.log)

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
        _run_one "convert-rdf ($name)"     test_convert_rdf    "$schema" "$outdir/$name-eksempel.ttl" \
                                                               "examples/$domain/$name-eksempel.yaml" "$domain"
        _run_one "linkml-lint ($name)"     test_linkml_lint    "$schema"
        _run_one "linkml-validate ($name)" test_linkml_validate "$schema" \
                                                               "examples/$domain/$name-eksempel.yaml" "$domain" "$name"
        _run_one "gen-proto ($name)"              test_gen_proto             "$schema" "$outdir/$name-schema.proto"
        _run_one "gen-plantuml ($name)"           test_gen_plantuml          "$schema" "$outdir/diagrams/$name.puml" "$outdir/diagrams/$name.svg"
        _run_one "mcp-validate-instance ($name)"  test_mcp_validate_instance "$schema" \
                                                               "examples/$domain/$name-eksempel.yaml" "$domain" "$name"
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
                printf "Test %-50s ... ${CLR_OK}OK${CLR_RST}\n" "${line#"##RESULT:OK:"}"
                pass=$((pass + 1))
            elif [[ "$line" == "##RESULT:FAIL:"* ]]; then
                local tname="${line#"##RESULT:FAIL:"}"
                printf "Test %-50s ... ${CLR_ERR}FEIL${CLR_RST}\n" "$tname"
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
    make validate SCHEMAS="$1" || return 1
}

test_gen_jsonld() {
    local schema="$1" outfile="$2"
    make gen-jsonld SCHEMAS="$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_json_valid "$outfile" || return 1
    assert_json_has_key "$outfile" "@context" || return 1
}

test_gen_python() {
    local schema="$1" outfile="$2"
    make gen-python SCHEMAS="$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    python3 -m py_compile "$outfile" || { echo "Syntaksfeil i $outfile"; return 1; }
}

test_gen_jsonschema() {
    local schema="$1" outfile="$2"
    make gen-jsonschema SCHEMAS="$schema" || return 1
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
    # Hoppar over for fint og samt — same som GEN_RDF_SKIP_* i Makefile
    if [[ "$domain" == "fint" || "$domain" == "samt" ]]; then
        echo "Hoppar over gen-rdf for $domain (GEN_RDF_SKIP)"
        return 0
    fi
    make gen-rdf SCHEMAS="$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_gen_erdiagram() {
    local schema="$1" outfile="$2"
    make gen-erdiagram SCHEMAS="$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    grep -q '```mermaid' "$outfile" || { echo "Manglar mermaid-blokk i $outfile"; return 1; }
    grep -q 'erDiagram'  "$outfile" || { echo "Manglar erDiagram i $outfile"; return 1; }
}

test_gen_docs() {
    local schema="$1" docsdir="$2"
    make gen-docs SCHEMAS="$schema" || return 1
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
    make gen-shacl SCHEMAS="$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_gen_owl() {
    local schema="$1" outfile="$2"
    make gen-owl SCHEMAS="$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_linkml_lint() {
    local schema="$1"
    podman run --rm \
        -v "$REPO_ROOT:/work" \
        -w /work \
        -e PYTHONWARNINGS=ignore \
        "$LINKML_IMAGE" \
        linkml lint --ignore-warnings "$schema" || return 1
}

test_linkml_validate() {
    local schema="$1" example="$2" domain="$3" name="$4"
    if [ ! -f "$example" ]; then
        echo "Ingen eksempelfil: $example (hoppar over)"
        return 0
    fi
    local validate_schema
    if [[ "$domain" == "ap-no" || "$domain" == "fair" ]]; then
        validate_schema="tests/fixtures/$name-fixture.yaml"
        if [ ! -f "$validate_schema" ]; then
            echo "Ingen fixture: $validate_schema (hoppar over)"
            return 0
        fi
    else
        validate_schema="$schema"
    fi
    podman run --rm \
        -v "$REPO_ROOT:/work" \
        -w /work \
        -e PYTHONWARNINGS=ignore \
        "$LINKML_IMAGE" \
        linkml validate --schema "$validate_schema" "$example" || return 1
}

test_convert_rdf() {
    local schema="$1" outfile="$2" example="$3" domain="$4"
    # ap-no og fair har ikkje tree_root — linkml-convert kan ikkje bestemme målklasse
    if [[ "$domain" == "ap-no" || "$domain" == "fair" ]]; then
        echo "Hoppar over convert-rdf for $domain (ingen tree_root)"
        return 0
    fi
    # Desse skjemaa har id-only stub-klasser i inlined_as_list container-slots.
    # linkml-convert har ein bug der {id: curie}-dicts med berre id-feltet
    # vert feilaktig prosessert (JsonObj vert sendt som id-verdi).
    # linkml validate krev objekt-forma; linkml-convert krev streng-forma.
    # Referanse: linkml-runtime yamlutils.py _normalize_inlined / _normalize_inlined_as_list.
    local name
    name=$(schema_name "$schema")
    if [[ "$name" == "ngr-adresse" || "$name" == "ngr-eiendom" || "$name" == "ngr-virksomhet" ]]; then
        echo "Hoppar over convert-rdf for $name (linkml-runtime bug med id-only inlined_as_list)"
        return 0
    fi
    if [ ! -f "$example" ]; then
        echo "Ingen eksempelfil: $example (hoppar over)"
        return 0
    fi
    mkdir -p "$(dirname "$outfile")"
    podman run --rm \
        -v "$REPO_ROOT:/work" \
        -w /work \
        -e PYTHONWARNINGS=ignore \
        "$LINKML_IMAGE" \
        linkml-convert \
            --schema "$schema" \
            --output-format ttl \
            --no-validate \
            --output "$outfile" \
            "$example" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_gen_proto() {
    local schema="$1" outfile="$2"
    make gen-proto SCHEMAS="$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    grep -qE 'syntax\s*=\s*"proto3"' "$outfile" || { echo "Manglar proto3-syntaksdeklarasjon i $outfile"; return 1; }
}

test_gen_plantuml() {
    local schema="$1" pumlfile="$2" svgfile="$3"
    make gen-plantuml SCHEMAS="$schema" || return 1
    assert_file_nonempty "$pumlfile" || return 1
    assert_file_nonempty "$svgfile" || return 1
    grep -q '@startuml' "$pumlfile" || { echo "Manglar @startuml i $pumlfile"; return 1; }
    grep -q '<svg' "$svgfile" || { echo "Manglar <svg> i $svgfile"; return 1; }
}

test_mcp_validate_instance() {
    local schema="$1" example="$2" domain="$3" name="$4"
    if [[ "$domain" == "ap-no" || "$domain" == "fair" ]]; then
        echo "Hoppar over mcp-validate-instance for $domain (ingen tree_root)"
        return 0
    fi
    if [ ! -f "$example" ]; then
        echo "Ingen eksempelfil: $example (hoppar over)"
        return 0
    fi
    local validate_schema="$schema"
    [ -f "tests/fixtures/$name-fixture.yaml" ] && validate_schema="tests/fixtures/$name-fixture.yaml"
    local tmpflat
    tmpflat=$(mktemp /tmp/mcp_flat_XXXXXX.yaml)
    podman run --rm \
        -v "$REPO_ROOT:/work" \
        -w /work \
        -e PYTHONWARNINGS=ignore \
        "$LINKML_IMAGE" \
        gen-linkml --mergeimports --format yaml "$validate_schema" \
        > "$tmpflat" 2>/dev/null || { echo "gen-linkml feila for $validate_schema"; rm -f "$tmpflat"; return 1; }
    python3 - "$REPO_ROOT" "$tmpflat" "$example" << 'PYEOF'
import json, sys, subprocess
repo_root, schema_path, instance_path = sys.argv[1], sys.argv[2], sys.argv[3]
schema_text = open(schema_path).read()
instance_text = open(instance_path).read()
msgs = [
    {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {
        "name": "validate_linkml_instance",
        "arguments": {"schemaText": schema_text, "instanceText": instance_text},
    }},
]
proc = subprocess.run(
    ["podman", "run", "-i", "--rm",
     "-v", f"{repo_root}/src/mcp-linkml-validator/server.py:/app/server.py:ro",
     "-v", f"{repo_root}/src/mcp-linkml-validator/policies:/app/policies:ro",
     "mcp-linkml-validator"],
    input="\n".join(json.dumps(m) for m in msgs),
    capture_output=True, text=True,
)
for line in proc.stdout.splitlines():
    try:
        r = json.loads(line)
    except json.JSONDecodeError:
        continue
    if r.get("id") == 2:
        d = json.loads(r["result"]["content"][0]["text"])
        errors = [i for i in d.get("issues", []) if i["severity"] == "error"]
        if errors:
            for e in errors:
                print(f"[ERROR] {e['target']}: {e['message']}")
            sys.exit(1)
        sys.exit(0)
sys.exit(1)
PYEOF
    local rc=$?
    rm -f "$tmpflat"
    return $rc
}

# ---------------------------------------------------------------------------
# Start ein bakgrunnsprosess per skjema; testar per skjema køyrer sekvensielt
# ---------------------------------------------------------------------------
for schema in "${SCHEMAS[@]}"; do
    run_schema_tests "$schema"
done

wait_for_tests
