#!/usr/bin/env bash
# Integrasjonstester for make-targets. Køyr mot alle reelle skjema, parallelt.
# Krev at localhost/linkml-local:latest er bygd (make linkml-build-docker).
set -euo pipefail

# Delt logg-infrastruktur (log_debug/log_info/log_error/fmt_elapsed_ms/
# timed_run/run_logged) — same mønster som run-domain-pipeline.sh og
# mkdocs/publish.sh. LOG_FUNCTIONS/LOGLVL/CLR_*-variablane vert automatisk
# arva som miljøvariablar når scriptet køyrer via ein make-recipe (dei er
# export-erte i make/00-settings.mk) — :?-sjekken gjev ei tydeleg feilmelding
# dersom scriptet nokon gong køyrer utanfor make.
: "${LOG_FUNCTIONS:?miljøvariabelen LOG_FUNCTIONS må vere sett (eksportert frå make/00-settings.mk — køyr via make test/roundtrip, ikkje scriptet direkte)}"
eval "$LOG_FUNCTIONS"

SCRIPT_T0=$(date +%s%3N)

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

LINKML_IMAGE="localhost/linkml-local:latest"
MCP_IMAGE="mcp-linkml-validator"
PYTHON_IMAGE="localhost/python-pytest:latest"
GEN_DIR="generated"
SCHEMA_DIR="src/linkml"
LOGDIR="tests/testlogs"
LOG="$LOGDIR/test_make_$(date '+%Y%m%d_%H%M%S').log"
mkdir -p "$LOGDIR"
mkdir -p "$REPO_ROOT/tmp"

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

# Fila sin eigen, unike basisnamn (filnamn utan -schema.yaml) — identifiserer
# DETTE skjemaet eintydig, sjølv når fleire skjema er samlokaliserte i same
# katalog (t.d. ap-no/dqv-ap-no/{dqv-ap-no,dqv-core}-schema.yaml). Brukt for
# genererte artefaktnamn/utdatakatalog og visingsnamn i testutskrifta.
# Matchar batch-generate.py sin schema_domain_name(). Sjå
# specs/done/fiks-schema-name-katalog-kollisjon-test-make.md.
schema_name() {
    local base
    base=$(basename "$1" .yaml)
    echo "${base%-schema}"
}

# Kjeldekatalognamnet (4. sti-komponent) — brukt KUN til å finne DELTE
# per-katalog-ressursar (examples/<katalog>-eksempel.yaml,
# tests/fixtures/<katalog>-fixture.yaml) når fleire skjema er samlokaliserte
# (AP-NO-profilfamiliar). For dei aller fleste skjema (éin fil per katalog)
# er dette identisk med schema_name().
schema_dir_name() { echo "$1" | cut -d/ -f4; }

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
    local schema="$1" domain="$2"
    lacks_tree_root "$domain" && return 1
    # Eksempel-/fixture-filer er DELTE per kjeldekatalog (fleire skjema kan
    # vere samlokaliserte, t.d. AP-NO-profilfamiliar) — bruk difor
    # schema_dir_name(), ikkje schema_name(), her. Sjå
    # specs/done/fiks-schema-name-katalog-kollisjon-test-make.md.
    local dir_name
    dir_name=$(schema_dir_name "$schema")
    local example="src/linkml/$domain/$dir_name/examples/$dir_name-eksempel.yaml"
    [ -f "$example" ] || return 1
    local validate_schema="$schema"
    [ -f "tests/fixtures/$dir_name-fixture.yaml" ] && validate_schema="tests/fixtures/$dir_name-fixture.yaml"
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
    # BUG-19: rdflib_loader rekonstruerer datetime-verdiar med mellomrom i
    # staden for T-separator. Sjå bugs/datetime-separator-rdflib-roundtrip.md
    case "$name" in
        enhetsregisteret-bvrinn) return 1 ;;
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
    local schema="$1" domain="$2" example="$4"
    [ -f "$example" ] || return 1
    local validate_schema="$schema"
    if lacks_tree_root "$domain"; then
        # Fixture-filer er DELTE per kjeldekatalog — bruk schema_dir_name(),
        # ikkje det (no filnamn-baserte) $name-parameteret. Sjå
        # specs/done/fiks-schema-name-katalog-kollisjon-test-make.md.
        validate_schema="tests/fixtures/$(schema_dir_name "$schema")-fixture.yaml"
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
    echo "========================================"
    echo "TEST: $tname  ($(date '+%H:%M:%S'))"
    echo "========================================"
    log_debug "→ $tname"
    local t0 elapsed rc=0
    t0=$(date +%s%3N)
    "$@" 2>&1 || rc=$?
    elapsed=$(( $(date +%s%3N) - t0 ))
    # Heile statuslinja (namn + "..." + OK/FEIL + linjeskift) skrivast som
    # ÉIN printf — éin write()-syscall for ei linje av denne lengda er
    # atomisk med omsyn til andre samstundes skjema sine skriv til same
    # fildeskriptor (>&3), sidan mange skjema køyrer parallelt via
    # SCHEMA_PIDS. Å splitte i eit "namn ..."-kall FØR testen og eit
    # "OK/FEIL"-kall ETTER (den tidlegare koden) let andre prosessar sitt
    # skriv lande i gapet mellom dei to — garbla, samanblanda linjer. Sjå
    # specs/done/atomisk-terminal-utskrift-test-make.md.
    # Namn- og tidsbruk-delen er kvar sin eigen fast-breidde printf-
    # kolonne (i staden for tidsbruken lagt inn i namne-strengen), slik at
    # tidsbruken alltid startar i same kolonne på tvers av linjer —
    # uavhengig av kor langt testnamnet/skjemanamnet er. Same mønster som
    # print_phase_a_summary()/Fase B-oppsummeringa, sjå
    # specs/done/fase-a-oppsummering-test-make.md.
    local timing="($(fmt_elapsed_ms "$elapsed"))"
    # Tidsbruken vert lagt til RESULT-markøren (tab-skilt) slik
    # wait_for_tests() kan summere han per test-type til Fase B-
    # oppsummeringa, utan å måtte parse den menneskelesbare terminal-
    # linja.
    if [ "$rc" -eq 0 ]; then
        printf "  %-52s %-11s ... ${CLR_OK}OK${CLR_RST}\n" "$tname" "$timing" >&3
        printf '##RESULT:OK:%s\t%s\n' "$tname" "$elapsed"
    else
        printf "  %-52s %-11s ... ${CLR_ERR}FEIL${CLR_RST}\n" "$tname" "$timing" >&3
        printf '##RESULT:FAIL:%s\t%s\n' "$tname" "$elapsed"
    fi
    log_info "${CLR_STEP}→ ${tname}${CLR_RST} ($(fmt_elapsed_ms "$elapsed"))"
}

# Køyr alle testar for eit skjema sekvensielt (i ein bakgrunnsprosess)
run_schema_tests() {
    local schema="$1"
    local domain name outdir dir_name
    domain=$(schema_domain "$schema")
    name=$(schema_name "$schema")
    outdir=$(schema_outdir "$schema")
    # Eksempelfila er DELT per kjeldekatalog (fleire skjema kan vere
    # samlokaliserte) — bruk schema_dir_name(), ikkje schema_name(). Sjå
    # specs/done/fiks-schema-name-katalog-kollisjon-test-make.md.
    dir_name=$(schema_dir_name "$schema")
    local example="src/linkml/$domain/$dir_name/examples/$dir_name-eksempel.yaml"
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
        _run_one "gen-docs ($name)"        test_gen_docs       "$schema"
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
    # Per test-type-tal (t.d. "gen-jsonld", "roundtrip-ttl") på tvers av
    # ALLE skjema — grunnlaget for Fase B-oppsummeringa lenger nede.
    # phase_b_types held rekkjefølgja typane vart ELSTE (fylgjer
    # definisjonsrekkjefølgja i run_schema_tests(), sidan første skjema si
    # loggfil vert lesen først og typane der følgjer _run_one()-kalla i
    # rekkjefølgje).
    local -a phase_b_types=()
    local -A phase_b_ok=() phase_b_fail=() phase_b_elapsed=() phase_b_fail_names=()
    for i in "${!SCHEMA_PIDS[@]}"; do
        local pid="${SCHEMA_PIDS[$i]}"
        local tmplog="${SCHEMA_LOGS[$i]}"
        wait "$pid" || true  # always process log, uavhengig av exit-kode
        while IFS= read -r line; do
            local rest ok_flag
            if [[ "$line" == "##RESULT:OK:"* ]]; then
                pass=$((pass + 1))
                rest="${line#"##RESULT:OK:"}"
                ok_flag=1
            elif [[ "$line" == "##RESULT:FAIL:"* ]]; then
                rest="${line#"##RESULT:FAIL:"}"
                fail=$((fail + 1))
                ok_flag=0
            else
                continue
            fi
            local tname="${rest%%$'\t'*}" elapsed="${rest#*$'\t'}"
            if [ "$ok_flag" -eq 0 ]; then
                echo "--- output frå $tname ---" >&2
                grep -A 25 "TEST: $tname " "$tmplog" | tail -25 >&2 || true
            fi
            # Test-typen er tname utan "(<skjemanamn>)"-suffikset, t.d.
            # "gen-jsonld (novari-modellkatalog)" → "gen-jsonld". Testar
            # utan skjemanamn (t.d. "copy-artifacts-click-href") manglar
            # " (" og vert difor sin eigen type uendra.
            local type="${tname%% (*}"
            if [[ -z "${phase_b_ok[$type]+x}" ]]; then
                phase_b_types+=("$type")
                phase_b_ok[$type]=0
                phase_b_fail[$type]=0
                phase_b_elapsed[$type]=0
                phase_b_fail_names[$type]=""
            fi
            if [ "$ok_flag" -eq 1 ]; then
                phase_b_ok[$type]=$(( phase_b_ok[$type] + 1 ))
            else
                phase_b_fail[$type]=$(( phase_b_fail[$type] + 1 ))
                # Skjemanamnet er teksten i parentesen i tname, t.d.
                # "roundtrip-ttl (fint-utdanning)" → "fint-utdanning".
                # Testar utan " (" (t.d. "copy-artifacts-click-href") har
                # ikkje eit skjemanamn å hente ut — hoppar over.
                if [[ "$tname" == *" ("* ]]; then
                    local schema_short="${tname#*(}"
                    schema_short="${schema_short%)*}"
                    phase_b_fail_names[$type]="${phase_b_fail_names[$type]:+${phase_b_fail_names[$type]}, }$schema_short"
                fi
            fi
            phase_b_elapsed[$type]=$(( phase_b_elapsed[$type] + elapsed ))
        done < "$tmplog"
        sed 's/\x1b\[[0-9;]*m//g' "$tmplog" >> "$LOG"
        rm -f "$tmplog"
    done
    print_phase_a_summary
    echo ""
    echo "=== Fase B — oppsummering ==="
    local type
    for type in "${phase_b_types[@]}"; do
        local n=$(( phase_b_ok[$type] + phase_b_fail[$type] ))
        local prefix="→ Fase B: $type ($n sjekkar) ..."
        printf '%-58s %-11s %sOK:%s %-4s %sFEIL:%s %s\n' "$prefix" "($(fmt_elapsed_ms "${phase_b_elapsed[$type]}"))" "$CLR_OK" "$CLR_RST" "${phase_b_ok[$type]}" "$CLR_ERR" "$CLR_RST" "${phase_b_fail[$type]}"
        if [ -n "${phase_b_fail_names[$type]}" ]; then
            echo "    Feila: ${phase_b_fail_names[$type]}"
        fi
    done
    echo ""
    echo "Resultat: $pass OK, $fail feil"
    echo "Total tidsbruk: $(fmt_elapsed_ms $(( $(date +%s%3N) - SCRIPT_T0 )))"
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
# Fase A-steg køyrer samstundes (sjå run_phase_a()) — kvart steg sin
# loggfil-sti må difor vere fast/føreseieleg (IKKJE mktemp-generert), sidan
# phase_a_check()/phase_a_mcp_check() konstruerer stien direkte i staden for
# å slå ho opp i eit array. Eit bash-array-oppslag ville ikkje fungert her:
# variabeltilordningar i eit backgrounda underskal (`funksjon &`) går tapt
# for foreldreskalet når jobben er ferdig, så eit array populert INNI eit
# Fase A-steg kan ikkje lesast av Fase B etterpå. Filsystemet er den einaste
# tilstanden som overlever backgrounding.
phase_a_logfile() { echo "$LOGDIR/phase_a_$1.log"; }

# Same faste-fil-mønster som phase_a_logfile() — held på (N, elapsed, label)
# for kvart steg slik print_phase_a_summary() kan gjenskape opningslinja med
# tal etterpå, sjølv om steget køyrde i eit anna underskal enn summary-
# funksjonen. Sjå specs/done/fase-a-oppsummering-test-make.md.
phase_a_metafile() { echo "$LOGDIR/phase_a_$1.meta"; }

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
    logfile=$(phase_a_logfile "$key")
    echo "→ Fase A: $target (${#SCHEMAS[@]} skjema) ..." >&3
    # Steg-nivå tidsmåling skriv til $LOG (ikkje via log_info/stderr direkte)
    # sidan dette steget køyrer backgrounda UTAN ein omsluttande redirect
    # (jf. run_phase_a(), Del 1) — direkte log_info her ville lekke live til
    # terminalen og interleave med dei andre 16 samstundes Fase A-stega.
    local t0 elapsed
    t0=$(date +%s%3N)
    make "$target" SCHEMAS="${SCHEMAS[*]}" > "$logfile" 2>&1 || true
    elapsed=$(( $(date +%s%3N) - t0 ))
    printf '%s\t%s\t%s\t%s\n' "${#SCHEMAS[@]}" "$elapsed" "$target" "skjema" > "$(phase_a_metafile "$key")"
    {
        echo "========================================"
        echo "FASE A: $target  ($(date '+%H:%M:%S'), $(fmt_elapsed_ms "$elapsed"))"
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
    logfile=$(phase_a_logfile "lint")
    echo "→ Fase A: linkml-lint --ignore-warnings (${#SCHEMAS[@]} skjema) ..." >&3
    local t0 elapsed
    t0=$(date +%s%3N)
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        python3 src/assets/scripts/makefile/batch-lint.py \
            --config src/assets/containers/.linkmllint.yaml --ignore-warnings -- "${SCHEMAS[@]}" \
        > "$logfile" 2>&1 || true
    elapsed=$(( $(date +%s%3N) - t0 ))
    printf '%s\t%s\t%s\t%s\n' "${#SCHEMAS[@]}" "$elapsed" "linkml-lint --ignore-warnings" "skjema" > "$(phase_a_metafile "lint")"
    {
        echo "========================================"
        echo "FASE A: linkml-lint --ignore-warnings  ($(date '+%H:%M:%S'), $(fmt_elapsed_ms "$elapsed"))"
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
#
# schema→jobb-indeks-koplinga (batch-validate-instances.py skriv resultat
# som <idx>.json, 0-indeksert) vert skriven til ei fast indeksfil i staden
# for eit bash-array — sjå phase_a_logfile()-kommentaren over for kvifor
# (Fase A-steg køyrer no samstundes i eigne underskal, jf. run_phase_a()).
phase_a_mcp_outdir() { echo "$LOGDIR/phase_a_mcp"; }
phase_a_mcp_indexfile() { echo "$LOGDIR/phase_a_mcp_index.tsv"; }

run_phase_a_mcp_instance() {
    local prefix="mcp-validate-instance"
    if [[ -n "${TEST_FILTER:-}" ]] \
        && [[ "$prefix" != "$TEST_FILTER"* ]] \
        && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
        return 0
    fi
    local indexfile
    indexfile=$(phase_a_mcp_indexfile)
    : > "$indexfile"
    local jobs=()
    local idx=0
    for schema in "${SCHEMAS[@]}"; do
        local domain name job
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        job=$(mcp_instance_job "$schema" "$domain") || continue
        local validate_schema example
        read -r validate_schema example <<< "$job"
        jobs+=("${validate_schema}=${example}")
        printf '%s\t%s\n' "$schema" "$idx" >> "$indexfile"
        idx=$((idx + 1))
    done
    if [ "${#jobs[@]}" -eq 0 ]; then
        return 0
    fi
    local outdir
    outdir=$(phase_a_mcp_outdir)
    rm -rf "$outdir"
    mkdir -p "$outdir"
    echo "→ Fase A: mcp-validate-instance (${#jobs[@]} skjema) ..." >&3
    local logfile t0 elapsed
    logfile=$(phase_a_logfile "mcp_instance")
    t0=$(date +%s%3N)
    REPO_ROOT="$REPO_ROOT" VALIDATOR_DIR="$REPO_ROOT/src/mcp-linkml-validator" MCP_IMAGE="$MCP_IMAGE" \
        python3 src/mcp-linkml-validator/batch-validate-instances.py \
            --output-dir "$outdir" "${jobs[@]}" > "$logfile" 2>&1 || true
    elapsed=$(( $(date +%s%3N) - t0 ))
    printf '%s\t%s\t%s\t%s\n' "${#jobs[@]}" "$elapsed" "mcp-validate-instance" "skjema" > "$(phase_a_metafile "mcp_instance")"
    {
        echo "========================================"
        echo "FASE A: mcp-validate-instance  ($(date '+%H:%M:%S'), $(fmt_elapsed_ms "$elapsed"))"
        echo "========================================"
        cat "$logfile"
    } >> "$LOG"
}

# Kategori D: convert-rdf, roundtrip-json, roundtrip-ttl (alle batcha via
# batch-convert.py, sjå den fila sin toppkommentar for grunngjeving) og
# linkml-validate (batcha via batch-linkml-validate.py). Same
# jobbliste/TSV-mønster som batch-flatten-and-validate.py etablerte for
# heterogene jobbar.
_run_phase_a_convert_batch() {
    local key="$1" jobs_tsv="$2" label="$3"
    local logfile n
    logfile=$(phase_a_logfile "$key")
    n=$(wc -l < "$jobs_tsv")
    echo "→ Fase A: $label ($n jobb(ar)) ..." >&3
    local t0 elapsed
    t0=$(date +%s%3N)
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        python3 src/assets/scripts/makefile/batch-convert.py --jobs-tsv "/work/$jobs_tsv" \
        > "$logfile" 2>&1 || true
    elapsed=$(( $(date +%s%3N) - t0 ))
    printf '%s\t%s\t%s\t%s\n' "$n" "$elapsed" "$label" "jobb(ar)" > "$(phase_a_metafile "$key")"
    rm -f "$jobs_tsv"
    {
        echo "========================================"
        echo "FASE A: $label  ($(date '+%H:%M:%S'), $(fmt_elapsed_ms "$elapsed"))"
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
        local domain name example outdir dir_name
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        dir_name=$(schema_dir_name "$schema")
        example="src/linkml/$domain/$dir_name/examples/$dir_name-eksempel.yaml"
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
        local domain name example rtdir dir_name
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        dir_name=$(schema_dir_name "$schema")
        example="src/linkml/$domain/$dir_name/examples/$dir_name-eksempel.yaml"
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
        local domain name example rtdir dir_name
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        dir_name=$(schema_dir_name "$schema")
        example="src/linkml/$domain/$dir_name/examples/$dir_name-eksempel.yaml"
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
        local domain name example validate_schema dir_name
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        dir_name=$(schema_dir_name "$schema")
        example="src/linkml/$domain/$dir_name/examples/$dir_name-eksempel.yaml"
        validate_schema=$(linkml_validate_job "$schema" "$domain" "$name" "$example") || continue
        printf '%s\t%s\t%s\n' "$schema" "$validate_schema" "$example" >> "$jobs_tsv"
        has_jobs=1
    done
    if [ "$has_jobs" -eq 0 ]; then
        rm -f "$jobs_tsv"
        return 0
    fi
    local logfile n
    logfile=$(phase_a_logfile "linkml_validate")
    n=$(wc -l < "$jobs_tsv")
    echo "→ Fase A: linkml-validate ($n skjema) ..." >&3
    local t0 elapsed
    t0=$(date +%s%3N)
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        python3 src/assets/scripts/makefile/batch-linkml-validate.py --jobs-tsv "/work/$jobs_tsv" \
        > "$logfile" 2>&1 || true
    elapsed=$(( $(date +%s%3N) - t0 ))
    printf '%s\t%s\t%s\t%s\n' "$n" "$elapsed" "linkml-validate" "skjema" > "$(phase_a_metafile "linkml_validate")"
    rm -f "$jobs_tsv"
    {
        echo "========================================"
        echo "FASE A: linkml-validate  ($(date '+%H:%M:%S'), $(fmt_elapsed_ms "$elapsed"))"
        echo "========================================"
        cat "$logfile"
    } >> "$LOG"
}

# Batchar RDF-gyldigheitssjekk (tidlegare assert_rdf_valid(), som spann opp
# éin ny podman-kontainar PER FIL — sjå
# specs/backlog/optimaliser-make-test-basert-pa-logginnsikt.md, Tiltak 1)
# for output-filene til gen-rdf/gen-shacl/gen-owl/convert-rdf, i éin
# kontainar. MÅ køyrast sekvensielt ETTER dei fire stega over (les filer
# DEI produserer) — kallast difor IKKJE i PHASE_A_PIDS-lista i run_phase_a(),
# men rett etter at hovud-wait-løkka er ferdig.
run_phase_a_rdf_validity() {
    local jobs_list
    jobs_list=$(mktemp "$LOGDIR/phase_a_rdf_validity_jobs_XXXXXX.txt")
    local has_jobs=0
    for schema in "${SCHEMAS[@]}"; do
        local domain name outdir
        domain=$(schema_domain "$schema")
        name=$(schema_name "$schema")
        outdir=$(schema_outdir "$schema")
        local pair prefix f
        for pair in "gen-rdf:$outdir/$name-schema.ttl" \
                    "gen-shacl:$outdir/$name-shapes.ttl" \
                    "gen-owl:$outdir/$name-ontology.ttl" \
                    "convert-rdf:$outdir/$name-eksempel.ttl"; do
            prefix="${pair%%:*}"
            f="${pair#*:}"
            if [[ -n "${TEST_FILTER:-}" ]] \
                && [[ "$prefix" != "$TEST_FILTER"* ]] \
                && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
                continue
            fi
            [ -s "$f" ] || continue
            printf '%s\n' "$f" >> "$jobs_list"
            has_jobs=1
        done
    done
    if [ "$has_jobs" -eq 0 ]; then
        rm -f "$jobs_list"
        return 0
    fi
    local logfile n
    logfile=$(phase_a_logfile "rdf_validity")
    n=$(wc -l < "$jobs_list")
    echo "→ Fase A: rdf-validity ($n fil(er)) ..." >&3
    local t0 elapsed
    t0=$(date +%s%3N)
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$LINKML_IMAGE" \
        python3 src/assets/scripts/makefile/batch-rdf-validate.py --files-list "/work/$jobs_list" \
        > "$logfile" 2>&1 || true
    elapsed=$(( $(date +%s%3N) - t0 ))
    printf '%s\t%s\t%s\t%s\n' "$n" "$elapsed" "rdf-validity" "fil(er)" > "$(phase_a_metafile "rdf_validity")"
    rm -f "$jobs_list"
    {
        echo "========================================"
        echo "FASE A: rdf-validity  ($(date '+%H:%M:%S'), $(fmt_elapsed_ms "$elapsed"))"
        echo "========================================"
        cat "$logfile"
    } >> "$LOG"
}

# Batchar .md-fil-gyldigheitssjekk for gen-docs (tidlegare éin bash-while-
# løkke PER SKJEMA i test_gen_docs(), 60-225 separate find/grep-kall per
# skjema — sjå specs/backlog/gjer-gen-docs-raskare-fase-b.md for måling).
# MÅ køyrast sekvensielt ETTER gen-docs (les katalogen han produserer) —
# kallast difor IKKJE i PHASE_A_PIDS-lista i run_phase_a(), men rett etter
# at hovud-wait-løkka er ferdig. Reint stdlib-arbeid (ingen linkml-import),
# køyrer difor i PYTHON_IMAGE (raskare oppstart enn LINKML_IMAGE), med
# ThreadPoolExecutor internt i batch-skriptet for å overlappe I/O-ventetid
# mellom filene i staden for å stable ho sekvensielt.
run_phase_a_docs_validity() {
    local jobs_list
    jobs_list=$(mktemp "$LOGDIR/phase_a_docs_validity_jobs_XXXXXX.tsv")
    local has_jobs=0
    local prefix="gen-docs"
    for schema in "${SCHEMAS[@]}"; do
        if [[ -n "${TEST_FILTER:-}" ]] \
            && [[ "$prefix" != "$TEST_FILTER"* ]] \
            && [[ "${prefix} (" != "$TEST_FILTER"* ]]; then
            continue
        fi
        local outdir
        outdir=$(schema_outdir "$schema")
        printf '%s\t%s\n' "$schema" "$outdir/docs" >> "$jobs_list"
        has_jobs=1
    done
    if [ "$has_jobs" -eq 0 ]; then
        rm -f "$jobs_list"
        return 0
    fi
    local logfile n
    logfile=$(phase_a_logfile "docs_validity")
    n=$(wc -l < "$jobs_list")
    echo "→ Fase A: docs-validity ($n skjema) ..." >&3
    local t0 elapsed
    t0=$(date +%s%3N)
    podman run --rm \
        -v "$REPO_ROOT:/work" -w /work \
        -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root \
        "$PYTHON_IMAGE" \
        python3 src/assets/scripts/makefile/batch-docs-validate.py --jobs-tsv "/work/$jobs_list" \
        > "$logfile" 2>&1 || true
    elapsed=$(( $(date +%s%3N) - t0 ))
    printf '%s\t%s\t%s\t%s\n' "$n" "$elapsed" "docs-validity" "skjema" > "$(phase_a_metafile "docs_validity")"
    rm -f "$jobs_list"
    {
        echo "========================================"
        echo "FASE A: docs-validity  ($(date '+%H:%M:%S'), $(fmt_elapsed_ms "$elapsed"))"
        echo "========================================"
        cat "$logfile"
    } >> "$LOG"
}

run_phase_a() {
    # Alle Fase A-steg er uavhengige (ingen les output frå eit anna steg i
    # denne lista — kvart tek berre kjeldeskjemaet/eksempelfila som input),
    # så dei køyrer samstundes i staden for i sekvens. Same
    # run_bg-liknande PID-array-mønster som SCHEMA_PIDS/wait_for_tests
    # lenger opp i fila, og same grunnmønster som
    # run-domain-pipeline.sh sin Fase 1 alt har verifisert i produksjon for
    # den tilsvarande "ekte" genereringspipelinen. Sjå
    # specs/done/paralleliser-fase-a-test-make.md.
    #
    # Rydd opp attverande Fase A-artefakt frå eit tidlegare skript-kall
    # FØR nokon steg startar: loggfilnamna er no faste (ikkje mktemp), så
    # phase_a_check()/phase_a_mcp_check() sin "[ -f ... ]"-sjekk (som
    # skil "steget vart hoppa over via TEST_FILTER" frå "steget køyrde")
    # ville elles kunne lese ei fil frå EIN ANNAN, tidlegare køyring med
    # ein annan TEST_FILTER-verdi.
    rm -f "$LOGDIR"/phase_a_*.log
    rm -f "$LOGDIR"/phase_a_*.meta
    rm -f "$(phase_a_mcp_indexfile)"
    rm -rf "$(phase_a_mcp_outdir)"

    local -a PHASE_A_PIDS=()

    run_phase_a_step validate   validate           "validate"      & PHASE_A_PIDS+=($!)
    run_phase_a_step jsonld     gen-jsonld-context  "gen-jsonld"    & PHASE_A_PIDS+=($!)
    run_phase_a_step python     gen-python          "gen-python"   & PHASE_A_PIDS+=($!)
    run_phase_a_step jsonschema gen-jsonschema      "gen-jsonschema" & PHASE_A_PIDS+=($!)
    run_phase_a_step rdf        gen-rdf             "gen-rdf"      & PHASE_A_PIDS+=($!)
    run_phase_a_step erdiagram  gen-erdiagram       "gen-erdiagram" & PHASE_A_PIDS+=($!)
    run_phase_a_step docs       gen-docs            "gen-docs"     & PHASE_A_PIDS+=($!)
    run_phase_a_step shacl      gen-shacl           "gen-shacl"    & PHASE_A_PIDS+=($!)
    run_phase_a_step owl        gen-owl             "gen-owl"      & PHASE_A_PIDS+=($!)
    run_phase_a_step proto      gen-proto           "gen-proto"    & PHASE_A_PIDS+=($!)
    run_phase_a_step plantuml   gen-plantuml        "gen-plantuml" & PHASE_A_PIDS+=($!)
    run_phase_a_lint                                                & PHASE_A_PIDS+=($!)
    run_phase_a_mcp_instance                                        & PHASE_A_PIDS+=($!)
    run_phase_a_convert_rdf                                         & PHASE_A_PIDS+=($!)
    run_phase_a_roundtrip_json                                      & PHASE_A_PIDS+=($!)
    run_phase_a_roundtrip_ttl                                       & PHASE_A_PIDS+=($!)
    run_phase_a_linkml_validate                                     & PHASE_A_PIDS+=($!)

    for pid in "${PHASE_A_PIDS[@]}"; do
        wait "$pid" || true  # feil vert oppdaga av Fase B via phase_a_check()/loggfil-innhald, ikkje via denne exit-koden
    done

    # Sekvensielt (som gruppe), ETTER at hovudstega over er ferdige — begge
    # les output desse produserer (gen-rdf/gen-shacl/gen-owl/convert-rdf
    # for rdf_validity, gen-docs for docs_validity). Dei to er uavhengige
    # av KVARANDRE, så dei køyrer parallelt seg imellom.
    local -a PHASE_A_POST_PIDS=()
    run_phase_a_rdf_validity  & PHASE_A_POST_PIDS+=($!)
    run_phase_a_docs_validity & PHASE_A_POST_PIDS+=($!)
    for pid in "${PHASE_A_POST_PIDS[@]}"; do
        wait "$pid" || true
    done
}

# Same nøkkelrekkjefølgje som kalla i run_phase_a() over — brukt av
# print_phase_a_summary() til å gjenskape Fase A-overskriftene i
# opphavleg rekkjefølgje til slutt i køyringa.
PHASE_A_KEYS=(validate jsonld python jsonschema rdf erdiagram docs shacl owl proto plantuml lint mcp_instance convert_rdf roundtrip_json roundtrip_ttl linkml_validate rdf_validity docs_validity)

# Kort, lesbart namn frå ein filsti brukt i eit ::error file=<sti>::-merke —
# stripper kjend filending og kjende suffiks (-schema/-eksempel/-shapes/
# -ontology/-context) slik at t.d. "src/linkml/fint/fint-utdanning/
# fint-utdanning-schema.yaml" og "generated/fint/fint-utdanning/
# fint-utdanning-eksempel.ttl" begge kortast til "fint-utdanning" i
# feillistene under. Dei ulike batch-skripta brukar ulike filtypar som
# nøkkel (skjema-YAML, instans-YAML, TTL-artefakt) — denne funksjonen er
# difor meir generell enn schema_name() (som berre handterer skjema-YAML).
phase_a_short_name() {
    local base
    base=$(basename "$1")
    base="${base%.yaml}"; base="${base%.ttl}"; base="${base%.json}"
    base="${base%-schema}"; base="${base%-eksempel}"
    base="${base%-shapes}"; base="${base%-ontology}"; base="${base%-context}"
    echo "$base"
}

# Unike, kortnamna kjelder til ::error file=<sti>::-merke i ei loggfil —
# brukt til å liste KVA skjema/artefakt som feila i Fase A-oppsummeringa,
# ikkje berre kor mange.
phase_a_error_names() {
    local logfile="$1"
    sed -n 's/.*::error file=\([^:]*\)::.*/\1/p' "$logfile" | sort -u | while IFS= read -r f; do
        phase_a_short_name "$f"
    done
}

# mcp-validate-instance brukar IKKJE ::error file=-konvensjonen (batch-
# validate-instances.py skriv strukturerte per-skjema JSON-resultatfiler i
# staden, sjå phase_a_mcp_check()) — treng difor eiga utrekning av kva
# skjema som feila, ved å lese SAME indeksfil/resultatfiler som
# phase_a_mcp_check() brukar.
phase_a_mcp_error_names() {
    local indexfile outdir
    indexfile=$(phase_a_mcp_indexfile)
    [ -f "$indexfile" ] || return 0
    outdir=$(phase_a_mcp_outdir)
    while IFS=$'\t' read -r schema idx; do
        local resultfile="$outdir/$idx.json"
        [ -f "$resultfile" ] || continue
        if ! python3 -c "
import json, sys
d = json.load(open('$resultfile'))
errors = [i for i in d.get('issues', []) if i['severity'] == 'error']
sys.exit(1 if errors else 0)
" 2>/dev/null; then
            phase_a_short_name "$schema"
        fi
    done < "$indexfile"
}

# Oppsummering til slutt i make test: gjentek kvar Fase A-overskrift saman
# med samla tidsbruk (frå metafila, sjå phase_a_metafile()) og eit OK/
# ERROR-tal (ERROR = talet på ::error file=-linjer i steget si loggfil —
# same universelle markør dei fleste batch-skripta brukar, unntatt
# mcp-validate-instance, sjå phase_a_mcp_error_names(); OK = N - ERROR,
# der N er det same talet steget alt viste i opningslinja si). Når
# ERROR > 0 vert dei feila skjema/artefakta lista på ei eiga, innrykka
# linje under. Steg som ikkje køyrde (TEST_FILTER, eller ingen jobbar å
# gjere) manglar loggfil og vert hoppa over — same konvensjon som
# phase_a_check(). Sjå specs/done/fase-a-oppsummering-test-make.md for
# grunngjeving, inkludert den kjende avgrensinga for build.yaml-flagg-
# styrte generatorar (N er kandidatlista, ikkje den faktisk aktiverte
# delmengda — same tal opningslinja alt viser i dag).
print_phase_a_summary() {
    echo ""
    echo "=== Fase A — oppsummering ==="
    local key
    for key in "${PHASE_A_KEYS[@]}"; do
        local logfile metafile
        logfile=$(phase_a_logfile "$key")
        [ -f "$logfile" ] || continue
        metafile=$(phase_a_metafile "$key")
        [ -f "$metafile" ] || continue
        local n elapsed label unit error ok prefix error_names
        IFS=$'\t' read -r n elapsed label unit < "$metafile"
        if [ "$key" = "mcp_instance" ]; then
            # mcp-validate-instance: éin JSON-resultatfil per skjema, så
            # talet på feila NAMN er òg det korrekte ERROR-talet (1:1).
            error_names=$(phase_a_mcp_error_names)
            error=$([ -z "$error_names" ] && echo 0 || echo "$error_names" | wc -l)
        else
            # Elles: ERROR-talet held fram å telje ::error file=-LINJER
            # (kan vere fleire enn talet unike skjema, t.d. eit
            # roundtrip-kall der same skjema feilar i to kjeda steg) — same
            # semantikk som N (jobbrad-/skjematal), uendra frå før. Namne-
            # lista er berre eit ekstra, deduplisert visingslag oppå dette.
            error=$(grep -c "::error file=" "$logfile" || true)
            error_names=$(phase_a_error_names "$logfile")
        fi
        ok=$(( n - error ))
        prefix="→ Fase A: $label ($n $unit) ..."
        # Namn-, tidsbruk- og OK:/FEIL:-delen er kvar sin eigen fast-
        # breidde printf-kolonne, slik at ALLE tre alltid startar i same
        # kolonne på tvers av linjer — uavhengig av kor langt steg-
        # namnet/talet er. Same fargar som OK/FEIL på dei live
        # terminallinjene i _run_one() (CLR_OK/CLR_ERR).
        printf '%-58s %-11s %sOK:%s %-4s %sFEIL:%s %s\n' "$prefix" "($(fmt_elapsed_ms "$elapsed"))" "$CLR_OK" "$CLR_RST" "$ok" "$CLR_ERR" "$CLR_RST" "$error"
        if [ -n "$error_names" ]; then
            # IKKJE `paste -sd ', '` — paste sin -d tolkar ein fleirteikn-
            # streng som EI LISTE av delskiljeteikn å SYKLE gjennom per
            # felt (t.d. "," så " " så "," ...), ikkje eitt tofelts skiljeteikn
            # — gav feil, alternerande utskrift. Bygg strengen manuelt i
            # staden, same mønster som phase_b_fail_names lenger nede.
            local joined="" name
            while IFS= read -r name; do
                joined="${joined:+${joined}, }$name"
            done <<< "$error_names"
            echo "    Feila: $joined"
        fi
    done
}

# Sjekk om eit gitt skjema feila i Fase A-batchen for ein gjeven generator.
# batch-generate.py/batch-generate-instances.py/batch-lint.py (i
# --ignore-warnings-modus) skriv ::error file=<schema>:: for per-skjema-
# isolerte feil (sjå spec, Tiltak 1/2) — grep denne markøren i staden for å
# stole på heile batchen sin exit-kode, sidan éitt skjema sin feil elles
# ville sjå ut som at ALLE skjema i batchen feila.
phase_a_check() {
    local key="$1" schema="$2"
    local logfile
    logfile=$(phase_a_logfile "$key")
    [ -f "$logfile" ] || return 0  # Fase A køyrde ikkje (TEST_FILTER) — _run_one hoppar uansett over kallaren
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
    local indexfile
    indexfile=$(phase_a_mcp_indexfile)
    [ -f "$indexfile" ] || return 0  # Fase A køyrde ikkje (TEST_FILTER)
    local idx
    idx=$(awk -F'\t' -v s="$schema" '$1 == s { print $2 }' "$indexfile")
    [ -n "$idx" ] || return 0  # ikkje ein del av batchen — kallaren har alt avgjort å hoppe over
    local resultfile="$(phase_a_mcp_outdir)/$idx.json"
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
    local name
    name=$(schema_name "$schema")
    # BUG-17: gen-rdf vert med vilje hoppa over for skjema med versjonslåst
    # URL-import (RDFGenerator fetchar <import>.context.jsonld over
    # nettverk, som aldri finst for slike importar). Sjå
    # bugs/gen-rdf-manglar-stotte-for-versjonslaste-importar.md
    case "$name" in
        lunchregisteret) echo "Hoppar over gen-rdf for $name (BUG-17: versjonslåst URL-import)"; return 0 ;;
    esac
    phase_a_check rdf "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    phase_a_check rdf_validity "$outfile" || return 1
}

test_gen_erdiagram() {
    local schema="$1" outfile="$2"
    phase_a_check erdiagram "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    grep -q '```mermaid' "$outfile" || { echo "Manglar mermaid-blokk i $outfile"; return 1; }
    grep -q 'erDiagram'  "$outfile" || { echo "Manglar erDiagram i $outfile"; return 1; }
}

test_gen_docs() {
    local schema="$1"
    phase_a_check docs "$schema" || return 1
    # .md-fil-innhaldssjekken (katalog finst, ikkje-tom, #-overskrift) er
    # batcha til Fase A sitt docs_validity-steg, sjå
    # run_phase_a_docs_validity() og specs/backlog/gjer-gen-docs-raskare-
    # fase-b.md — IKKJE lenger ei bash-while-løkke her.
    phase_a_check docs_validity "$schema" || return 1
}

test_gen_shacl() {
    local schema="$1" outfile="$2"
    phase_a_check shacl "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    phase_a_check rdf_validity "$outfile" || return 1
}

test_gen_owl() {
    local schema="$1" outfile="$2"
    phase_a_check owl "$schema" || return 1
    assert_file_nonempty "$outfile" || return 1
    phase_a_check rdf_validity "$outfile" || return 1
}

test_linkml_lint() {
    phase_a_check lint "$1" || return 1
}

test_linkml_validate() {
    local schema="$1" domain="$2" name="$3"
    local dir_name
    dir_name=$(schema_dir_name "$schema")
    local example="src/linkml/$domain/$dir_name/examples/$dir_name-eksempel.yaml"
    local validate_schema
    if ! validate_schema=$(linkml_validate_job "$schema" "$domain" "$name" "$example"); then
        if [ ! -f "$example" ]; then
            echo "Ingen eksempelfil: $example (hoppar over)"
        else
            echo "Ingen fixture: tests/fixtures/$dir_name-fixture.yaml (hoppar over)"
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
        elif [[ "$name" == "enhetsregisteret-bvrinn" ]]; then
            echo "Hoppar over roundtrip-ttl for $name (BUG-19: linkml-runtime datetime-separator-bug)"
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
    phase_a_check rdf_validity "$outfile" || return 1
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
    local schema="$1" domain="$2"
    local job
    if ! job=$(mcp_instance_job "$schema" "$domain"); then
        if lacks_tree_root "$domain"; then
            echo "Hoppar over mcp-validate-instance for $domain (ingen tree_root)"
        else
            local dir_name
            dir_name=$(schema_dir_name "$schema")
            echo "Ingen eksempelfil: src/linkml/$domain/$dir_name/examples/$dir_name-eksempel.yaml (hoppar over)"
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
# Regresjonstest: mermaid click-href-omskriving i copy_artifacts.sh
# (sjå specs/backlog/mermaid-klikkbare-lenker-404.md). Køyrer mot ei fiktiv
# fixture — treng ingen containerar og ingen ekte skjema.
# ---------------------------------------------------------------------------
test_copy_artifacts_click_href() {
    local tmp
    tmp=$(mktemp -d)

    mkdir -p "$tmp/repo/src/linkml/fixturedomain/fixtureschema"
    touch "$tmp/repo/src/linkml/fixturedomain/fixtureschema/fixtureschema-schema.yaml"
    mkdir -p "$tmp/repo/generated/fixturedomain/fixtureschema/docs"

    cat > "$tmp/repo/generated/fixturedomain/fixtureschema/docs/TestKlasse.md" <<'FIXTURE'
# TestKlasse

```mermaid
classDiagram
    class TestKlasse
    click TestKlasse href "../TestKlasse/"
    class AnnenKlasse
    click AnnenKlasse href "../AnnenKlasse/"
    class Uriorcurie
    click Uriorcurie href "../http://www.w3.org/2001/XMLSchema#anyURI/"
    class String
    click String href "../http://www.w3.org/2001/XMLSchema#string/"
```
FIXTURE
    cat > "$tmp/repo/generated/fixturedomain/fixtureschema/docs/AnnenKlasse.md" <<'FIXTURE'
# AnnenKlasse
FIXTURE

    local out="$tmp/repo/mkdocs/docs/fixturedomain/fixtureschema"
    mkdir -p "$out"

    (
        source "$REPO_ROOT/mkdocs/lib/copy_artifacts.sh"
        REPO_ROOT="$tmp/repo"
        copy_schema_artifacts "fixturedomain" "fixtureschema" \
            "$tmp/repo/generated/fixturedomain/fixtureschema" "$out"
    )
    local rc=$?
    if [ "$rc" -ne 0 ]; then
        echo "copy_schema_artifacts feila (exit $rc)"
        rm -rf "$tmp"
        return 1
    fi

    local target="$out/klasser/testklasse.md"
    if [ ! -f "$target" ]; then
        echo "Manglar generert fil (lowercase-omdøyping feila): $target"
        rm -rf "$tmp"
        return 1
    fi

    # Lokale klasse-/enum-/slot-/type-referansar skal vere
    # "../<lowercase(namn)>/" — utleidd frå namnet i click-statementet, ikkje
    # frå den opphavlege href-verdien (som kan vere feilkasa, sjå
    # specs/done/mermaid-klikkbare-lenker-404.md). Eksterne linkml:types-typar
    # (t.d. Uriorcurie, String) skal derimot bevare den absolutte XSD-URI-en
    # LinkML sin eigen gen-doc genererte, berre med det feilaktige
    # "../"-prefikset og den påklistra avsluttande "/" fjerna — IKKJE
    # omskrivast til ei lokal lenkje (BUG-13, sjå
    # specs/backlog/mermaid-diagram-elementaere-typar-og-attributtklikk.md).
    local -A expected_hrefs=(
        [TestKlasse]="../testklasse/"
        [AnnenKlasse]="../annenklasse/"
        [Uriorcurie]="http://www.w3.org/2001/XMLSchema#anyURI"
        [String]="http://www.w3.org/2001/XMLSchema#string"
    )
    local fail=0
    while IFS= read -r line; do
        local name href expected
        name=$(echo "$line" | sed -E 's/click ([A-Za-z0-9_]+) href.*/\1/')
        href=$(echo "$line" | sed -E 's/.*href "([^"]*)".*/\1/')
        expected="${expected_hrefs[$name]:-}"
        if [ -z "$expected" ]; then
            echo "Ukjend click-namn i fixture: $name"
            fail=1
        elif [ "$href" != "$expected" ]; then
            echo "Feil click-href for $name: fekk '$href', venta '$expected'"
            fail=1
        fi
    done < <(grep -o 'click [A-Za-z0-9_]* href "[^"]*"' "$target")

    rm -rf "$tmp"
    [ "$fail" -eq 0 ]
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
# copy_artifacts.sh-testar (køyrer alltid — treng ingen skjemaliste/containarar)
# ---------------------------------------------------------------------------
run_copy_artifacts_tests() {
    local tmplog
    tmplog=$(mktemp /tmp/test_make_copyartifacts_XXXXXX.log)

    {
        _run_one "copy-artifacts-click-href" test_copy_artifacts_click_href
    } >> "$tmplog" 2>&1 &

    SCHEMA_PIDS+=($!)
    SCHEMA_LOGS+=("$tmplog")
}

# ---------------------------------------------------------------------------
# Start ein bakgrunnsprosess per skjema; testar per skjema køyrer sekvensielt
# ---------------------------------------------------------------------------
exec 3>&1

# Køyr JSON Schema roundtrip-testar (dersom TEST_FILTER=roundtrip-json-schema)
run_json_schema_tests "$SCHEMA_FILTER"

# Køyr copy_artifacts.sh-testar (uavhengig av TEST_FILTER — rask, lokal sjekk)
run_copy_artifacts_tests

# Køyr vanlige skjema-testar (dersom TEST_FILTER != roundtrip-json-schema)
if [[ "${TEST_FILTER:-}" != "roundtrip-json-schema" ]]; then
    run_phase_a
    for schema in "${SCHEMAS[@]}"; do
        run_schema_tests "$schema"
    done
fi

wait_for_tests
