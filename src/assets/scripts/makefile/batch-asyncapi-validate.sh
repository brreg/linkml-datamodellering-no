#!/bin/sh
# Batch-validering av AsyncAPI YAML-filer via `asyncapi-validate`, køyrer
# ALLE skjema inni ÉIN delt asyncapi-kontainar i staden for éin kontainar
# per skjema.
#
# Bakgrunn: AsyncAPI CLI-et tek berre éin fil om gongen (ingen multi-fil-
# støtte), same avgrensing som avrotize. Difor må me køyre kommandoane
# sekvensielt i ei intern løkke, men amortiserer framleis kontainar-
# **oppstarten** (~2,6-2,7 s) over N skjema.
#
# Bruk: batch-asyncapi-validate.sh <schema1> <schema2> ...
#   Køyrer frå podman-kontekst med /work som CWD.
#   Skjema-stiar er relative til /work.
#
# Brukar `asyncapi-validate` frå asyncapi-cli-minimal image (296 MB),
# ikkje `asyncapi validate` frå asyncapi-cli-local (4.3 GB).
#
# Sjå specs/backlog/evaluer-batching-resterande-kommandoar.md, Tiltak 5.
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

    # Sjekk build.yaml for asyncapi: true
    manifest=$(dirname "$schema")/build.yaml
    if [ ! -f "$manifest" ] || ! grep -q "^  asyncapi: true" "$manifest"; then
        continue
    fi

    asyncapi_yaml="$GEN_DIR/$domain/$name/$name-asyncapi.yaml"
    if [ ! -f "$asyncapi_yaml" ]; then
        log_info "ÅTVARING: $asyncapi_yaml finst ikkje — hoppar over asyncapi-validate for $name"
        continue
    fi

    t0=$(date +%s)

    # asyncapi-validate (CLI i asyncapi-cli-minimal image)
    if ! asyncapi-validate "$asyncapi_yaml" 2>&1; then
        log_error "::error file=$schema::asyncapi-validate feila for $domain/$name"
        continue
    fi

    t1=$(date +%s)
    elapsed_s=$((t1 - t0))
    log_info "$(printf '→ asyncapi-validate  %s/%s (%ds)' \
        "$domain" "$name" "$elapsed_s")"
done
