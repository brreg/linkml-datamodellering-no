#!/usr/bin/env bash
# Batchar PlantUML SVG-rendering for N skjema til ÉITT podman-kall, i staden
# for eitt kall (× full/filtrert) per skjema — sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md (Tiltak 2).
#
# PlantUML sitt CLI tek fleire .puml-filer i eitt kall (verifisert i specen
# sitt «Funn»-avsnitt: 38 % reduksjon for berre 2 filer, JVM-/kontainar-
# oppstarten amortiserer over alle filene i staden for å betalast per fil).
#
# Køyrer berre for skjema der Fase A (gen-plantuml + filter_plantuml.py,
# framleis via run-parallel-gen.sh, uendra) alt har skrive .puml-filer —
# sjekkar filnærvær direkte i staden for å duplisere build.yaml sin
# plantuml:true-sjekk her (éin kjelde for gatinga: om fila finst).
#
# Bruk: PLANTUML_IMAGE=<image> bash batch-render-plantuml.sh schema1.yaml schema2.yaml ...
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR
eval "$LOG_FUNCTIONS"

: "${GEN_DIR:?miljøvariabelen GEN_DIR må vere sett}"
: "${PLANTUML_IMAGE:?miljøvariabelen PLANTUML_IMAGE må vere sett}"

files=()
for s in "$@"; do
    domain=$(echo "$s" | cut -d/ -f3)
    name=$(basename "$s" -schema.yaml | sed 's/-schema$//')
    outdir="$GEN_DIR/$domain/$name/diagrams"
    [ -f "$outdir/$name.puml" ] && files+=("$outdir/$name.puml")
    [ -f "$outdir/$name-filtered.puml" ] && files+=("$outdir/$name-filtered.puml")
done

if [ "${#files[@]}" -eq 0 ]; then
    log_debug "gen-plantuml-svg: ingen .puml-filer å rendere"
    exit 0
fi

t0=$(date +%s%3N)
podman run --rm -v "$PWD:/work" -w /work "$PLANTUML_IMAGE" -tsvg "${files[@]}" > /dev/null
t1=$(date +%s%3N)
ms=$(( t1 - t0 ))
log_info "$(printf '%s→ gen-plantuml-svg  batch (%d fil(er))%s (%d.%ds)' "$CLR_STEP" "${#files[@]}" "$CLR_RST" $(( ms / 1000 )) $(( ms % 1000 / 100 )))"
