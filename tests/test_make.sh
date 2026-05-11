#!/usr/bin/env bash
# Integrasjonstester for make-targets. Køyr mot reelle skjema.
# Krev at localhost/linkml-local:latest er bygd (make linkml-build-docker).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

LINKML_IMAGE="localhost/linkml-local:latest"
GEN_DIR="generated"
LOGDIR="tests/testlogs"
LOG="$LOGDIR/test_make_$(date '+%Y%m%d_%H%M%S').log"
mkdir -p "$LOGDIR"
PASS=0
FAIL=0

NGR_ADRESSE="src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml"
FINT_PERSONVERN="src/linkml/fint/fint-personvern/fint-personvern-schema.yaml"

CLR_OK=$(printf '\033[0;32m')
CLR_ERR=$(printf '\033[0;31m')
CLR_RST=$(printf '\033[0m')

# Initiér loggfil
echo "test_make.sh — $(date)" > "$LOG"
echo "LINKML_IMAGE: $LINKML_IMAGE" >> "$LOG"

# ---------------------------------------------------------------------------
# Cleanup: slett berre katalogar som testane sjølve oppretta.
# track_test_dir() registrerer ein katalog FØR testen køyrer — berre om han
# ikkje finst frå før, slik at pre-eksisterande generert innhald ikkje vert
# sletta etter testkøyringa.
# ---------------------------------------------------------------------------
declare -a TEST_DIRS=()

track_test_dir() {
    [ -d "$1" ] || TEST_DIRS+=("$1")
}

cleanup() {
    for dir in "${TEST_DIRS[@]+"${TEST_DIRS[@]}"}"; do
        rm -rf "$dir"
    done
}
trap cleanup EXIT

# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------
run_test() {
    local name="$1"; shift
    echo -n "Test $name ... "
    {
        echo ""
        echo "========================================"
        echo "TEST: $name  ($(date '+%H:%M:%S'))"
        echo "========================================"
    } >> "$LOG"
    if "$@" >> "$LOG" 2>&1; then
        echo "${CLR_OK}OK${CLR_RST}"
        echo "RESULT: OK" >> "$LOG"
        PASS=$((PASS + 1))
    else
        echo "${CLR_ERR}FEIL${CLR_RST}"
        echo "RESULT: FEIL" >> "$LOG"
        tail -20 "$LOG" >&2
        FAIL=$((FAIL + 1))
    fi
}

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
# gen-jsonld
# ---------------------------------------------------------------------------
test_gen_jsonld() {
    local outfile="$GEN_DIR/ngr/ngr-adresse/ngr-adresse-context.jsonld"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    make gen-jsonld SCHEMAS="$NGR_ADRESSE" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_json_valid "$outfile" || return 1
    assert_json_has_key "$outfile" "@context" || return 1
}

# ---------------------------------------------------------------------------
# gen-python
# ---------------------------------------------------------------------------
test_gen_python() {
    local outfile="$GEN_DIR/ngr/ngr-adresse/ngr-adresse-model.py"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    make gen-python SCHEMAS="$NGR_ADRESSE" || return 1
    assert_file_nonempty "$outfile" || return 1
    python3 -m py_compile "$outfile" || { echo "Syntaksfeil i $outfile"; return 1; }
}

# ---------------------------------------------------------------------------
# gen-jsonschema
# ---------------------------------------------------------------------------
test_gen_jsonschema() {
    local outfile="$GEN_DIR/ngr/ngr-adresse/ngr-adresse-schema.json"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    make gen-jsonschema SCHEMAS="$NGR_ADRESSE" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_json_valid "$outfile" || return 1
    python3 -c "
import json
d = json.load(open('$outfile'))
assert '\$defs' in d or 'properties' in d, '\$defs og properties manglar i $outfile'
" || return 1
}

# ---------------------------------------------------------------------------
# gen-rdf
# ---------------------------------------------------------------------------
test_gen_rdf() {
    local outfile="$GEN_DIR/ngr/ngr-adresse/ngr-adresse-schema.ttl"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    make gen-rdf SCHEMAS="$NGR_ADRESSE" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

# ---------------------------------------------------------------------------
# gen-erdiagram
# ---------------------------------------------------------------------------
test_gen_erdiagram() {
    local outfile="$GEN_DIR/ngr/ngr-adresse/ngr-adresse-erdiagram.md"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    make gen-erdiagram SCHEMAS="$NGR_ADRESSE" || return 1
    assert_file_nonempty "$outfile" || return 1
    grep -q '```mermaid' "$outfile" || { echo "Manglar mermaid-blokk i $outfile"; return 1; }
    grep -q 'erDiagram'  "$outfile" || { echo "Manglar erDiagram i $outfile"; return 1; }
}

# ---------------------------------------------------------------------------
# gen-docs
# ---------------------------------------------------------------------------
test_gen_docs() {
    local docsdir="$GEN_DIR/ngr/ngr-adresse/docs"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    make gen-docs SCHEMAS="$NGR_ADRESSE" || return 1
    [ -d "$docsdir" ] || { echo "Katalog manglar: $docsdir"; return 1; }
    local mdcount
    mdcount=$(find "$docsdir" -name "*.md" | wc -l)
    [ "$mdcount" -gt 0 ] || { echo "Ingen .md-filer i $docsdir"; return 1; }
    while IFS= read -r f; do
        [ -s "$f" ]         || { echo "Tom fil: $f"; return 1; }
        grep -q '^#' "$f"   || { echo "Manglar #-overskrift: $f"; return 1; }
    done < <(find "$docsdir" -name "*.md")
}

# ---------------------------------------------------------------------------
# convert-rdf
# ---------------------------------------------------------------------------
test_convert_rdf() {
    local example="examples/ngr/ngr-adresse-eksempel.yaml"
    local outfile="$GEN_DIR/ngr/ngr-adresse/ngr-adresse-eksempel.ttl"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    mkdir -p "$GEN_DIR/ngr/ngr-adresse"
    podman run --rm \
        -v "$REPO_ROOT:/work" \
        -w /work \
        -e PYTHONWARNINGS=ignore \
        "$LINKML_IMAGE" \
        linkml-convert \
            --schema "$NGR_ADRESSE" \
            --output-format ttl \
            --no-validate \
            --output "$outfile" \
            "$example" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

# ---------------------------------------------------------------------------
# gen-shacl
# ---------------------------------------------------------------------------
test_gen_shacl() {
    local outfile="$GEN_DIR/ngr/ngr-adresse/ngr-adresse-shapes.ttl"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    make gen-shacl SCHEMAS="$NGR_ADRESSE" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_gen_shacl_fint() {
    local outfile="$GEN_DIR/fint/fint-personvern/fint-personvern-shapes.ttl"
    track_test_dir "$GEN_DIR/fint/fint-personvern"
    make gen-shacl SCHEMAS="$FINT_PERSONVERN" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

# ---------------------------------------------------------------------------
# gen-owl
# ---------------------------------------------------------------------------
test_gen_owl() {
    local outfile="$GEN_DIR/ngr/ngr-adresse/ngr-adresse-ontology.ttl"
    track_test_dir "$GEN_DIR/ngr/ngr-adresse"
    make gen-owl SCHEMAS="$NGR_ADRESSE" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

test_gen_owl_fint() {
    local outfile="$GEN_DIR/fint/fint-personvern/fint-personvern-ontology.ttl"
    track_test_dir "$GEN_DIR/fint/fint-personvern"
    make gen-owl SCHEMAS="$FINT_PERSONVERN" || return 1
    assert_file_nonempty "$outfile" || return 1
    assert_rdf_valid "$outfile" || return 1
}

# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------
test_validate() {
    make validate SCHEMAS="$NGR_ADRESSE" || return 1
}

# ---------------------------------------------------------------------------
run_test "validate (ngr-adresse)"      test_validate
run_test "gen-jsonld (ngr-adresse)"    test_gen_jsonld
run_test "gen-python (ngr-adresse)"     test_gen_python
run_test "gen-jsonschema (ngr-adresse)" test_gen_jsonschema
run_test "gen-rdf (ngr-adresse)"        test_gen_rdf
run_test "gen-erdiagram (ngr-adresse)" test_gen_erdiagram
run_test "gen-docs (ngr-adresse)"      test_gen_docs
run_test "convert-rdf (ngr-adresse)"   test_convert_rdf
run_test "gen-shacl (ngr-adresse)"     test_gen_shacl
run_test "gen-shacl (fint-personvern)" test_gen_shacl_fint
run_test "gen-owl (ngr-adresse)"       test_gen_owl
run_test "gen-owl (fint-personvern)"   test_gen_owl_fint

# ---------------------------------------------------------------------------
echo ""
echo "Resultat: $PASS OK, $FAIL feil"
echo "Sjå $LOG for detaljar"
[ "$FAIL" -eq 0 ]
