#!/bin/sh
# Batch-generering av XSD-filer via avrotize (JSON Schema → Avro → XSD) +
# fix-xsd-dates.py, køyrer ALLE skjema inni ÉIN delt avrotize-kontainar i
# staden for éin kontainar per skjema × 3 verktøy.
#
# Bakgrunn: avrotize CLI-et tek berre éin fil om gongen (ingen multi-fil-
# støtte som PlantUML), og har ikkje eit dokumentert Python-API me kan
# importere direkte (same avgrensing som AsyncAPI CLI). Difor må me køyre
# kommandoane sekvensielt i ei intern løkke, men amortiserer framleis
# kontainar-**oppstarten** (~2,6-2,7 s per specs/done/effektiviser-generate-
# workflow-koyretid.md) over N skjema. fix-xsd-dates.py er reint Python og
# køyrer i same kontainar (entrypoint python3).
#
# Bruk: batch-gen-xsd.sh <schema1> <schema2> ...
#   Køyrer frå podman-kontekst med /work som CWD.
#   Skjema-stiar er relative til /work.
#
# Sjå specs/backlog/evaluer-batching-resterande-kommandoar.md, Tiltak 4.
set -eu

: "${GEN_DIR:=/work/generated}"

log_info() {
    echo "$*" >&2
}

log_error() {
    echo "[ERROR] $*" >&2
}

for schema in "$@"; do
    [ -f "$schema" ] || { log_error "Schema ikkje funne: $schema"; continue; }

    domain=$(echo "$schema" | cut -d/ -f3)
    name=$(basename "$schema" -schema.yaml | sed 's/-schema$//')

    # Sjekk build.yaml for xsd: true
    manifest=$(dirname "$schema")/build.yaml
    if [ ! -f "$manifest" ] || ! grep -q "^  xsd: true" "$manifest"; then
        continue
    fi

    jsonschema="$GEN_DIR/$domain/$name/$name-schema.json"
    if [ ! -f "$jsonschema" ]; then
        log_info "ÅTVARING: $jsonschema finst ikkje — hoppar over gen-xsd for $name"
        continue
    fi

    avsc="$GEN_DIR/$domain/$name/$name.avsc"
    xsd="$GEN_DIR/$domain/$name/$name-schema.xsd"
    namespace=$(grep '^id:' "$schema" | head -1 | awk '{print $2}')

    mkdir -p "$GEN_DIR/$domain/$name"

    t0=$(date +%s)

    # j2a: JSON Schema → Avro
    if ! avrotize j2a "$jsonschema" --out "$avsc" 2>&1; then
        log_error "::error file=$schema::avrotize j2a feila for $domain/$name"
        continue
    fi

    # a2x: Avro → XSD
    if ! avrotize a2x "$avsc" --namespace "$namespace" --out "$xsd" 2>&1; then
        log_error "::error file=$schema::avrotize a2x feila for $domain/$name"
        rm -f "$avsc"
        continue
    fi

    # fix-xsd-dates.py: Python-post-prosessering
    if ! python3 /work/src/assets/scripts/makefile/fix-xsd-dates.py "$xsd" "$jsonschema" 2>&1; then
        log_error "::error file=$schema::fix-xsd-dates.py feila for $domain/$name"
        rm -f "$avsc"
        continue
    fi

    rm -f "$avsc"

    t1=$(date +%s)
    elapsed_s=$((t1 - t0))
    log_info "$(printf '→ gen-xsd  %s/%s (%ds)' \
        "$domain" "$name" "$elapsed_s")"
done
