#!/usr/bin/env bash
# Parsing av manifest, validation-policy, versjon osv.
set -euo pipefail

source "$REPO_ROOT/mkdocs/lib/utils/imported_schemas.sh"

# Slå opp domain/schema-nøkkel frå ein manifest-sti på forma
# src/linkml/<domain>/<schema>/build.yaml — konvensjonen alle kallarar av
# denne fila alt konstruerer manifest-stien etter.
_manifest_schema_key() {
    local manifest="$1"
    local schema domain
    schema=$(basename "$(dirname "$manifest")")
    domain=$(basename "$(dirname "$(dirname "$manifest")")")
    printf '%s/%s' "$domain" "$schema"
}

# Les validation_policy/external_spec_url/external_spec_label for eit
# skjema frå det pre-berekna SCHEMA_METADATA_SERIALIZED-registeret (bygd i
# publish.sh Steg 1.5 via collect-schema-metadata.py — EIN containerprosess
# for alle skjema, i staden for at get_validation_policy/
# get_external_spec_url/get_external_spec_label kvar gjorde sitt eige
# `podman run`-kall mot same fil. Sjå
# specs/backlog/reduser-podman-kall-docs-publish.md (tidlegare batcha til
# éin python3-prosess PER skjema av batch-docs-publish-generering.md — no
# batcha på nytt til éin prosess for ALLE skjema).
load_manifest_cache() {
    local manifest="$1"
    export MANIFEST_CACHE_PATH="$manifest"
    export MANIFEST_CACHE_POLICY="bronze"
    export MANIFEST_CACHE_EXTERNAL_SPEC_URL=""
    export MANIFEST_CACHE_EXTERNAL_SPEC_LABEL=""
    [ ! -f "$manifest" ] && return

    local line
    if ! line=$(lookup_schema_metadata_line "$(_manifest_schema_key "$manifest")"); then
        echo "ÅTVARING: fann ingen pre-berekna metadata for $manifest — bruker default-verdiar" >&2
        return
    fi
    local _key policy url label _rest
    IFS=$'\x1f' read -r _key policy url label _rest <<< "$line"
    MANIFEST_CACHE_POLICY="${policy:-bronze}"
    MANIFEST_CACHE_EXTERNAL_SPEC_URL="$url"
    MANIFEST_CACHE_EXTERNAL_SPEC_LABEL="$label"
}

get_validation_policy() {
    local manifest="$1"
    if [ "${MANIFEST_CACHE_PATH:-}" = "$manifest" ]; then
        echo "$MANIFEST_CACHE_POLICY"
        return
    fi
    [ ! -f "$manifest" ] && echo "bronze" && return
    local line
    if line=$(lookup_schema_metadata_line "$(_manifest_schema_key "$manifest")"); then
        local _key policy _rest
        IFS=$'\x1f' read -r _key policy _rest <<< "$line"
        echo "${policy:-bronze}"
    else
        echo "ÅTVARING: fann ingen pre-berekna metadata for $manifest — bruker bronze" >&2
        echo "bronze"
    fi
}

get_latest_validation_version() {
    local validation_dir="$1"
    [ ! -d "$validation_dir" ] && return
    ls -v "$validation_dir" 2>/dev/null | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | tail -n1
}

get_external_spec_url() {
    local manifest="$1"
    if [ "${MANIFEST_CACHE_PATH:-}" = "$manifest" ]; then
        echo "$MANIFEST_CACHE_EXTERNAL_SPEC_URL"
        return
    fi
    [ ! -f "$manifest" ] && return
    local line
    line=$(lookup_schema_metadata_line "$(_manifest_schema_key "$manifest")") || return
    local _key _policy url _rest
    IFS=$'\x1f' read -r _key _policy url _rest <<< "$line"
    echo "$url"
}

get_external_spec_label() {
    local manifest="$1"
    if [ "${MANIFEST_CACHE_PATH:-}" = "$manifest" ]; then
        echo "$MANIFEST_CACHE_EXTERNAL_SPEC_LABEL"
        return
    fi
    [ ! -f "$manifest" ] && return
    local line
    line=$(lookup_schema_metadata_line "$(_manifest_schema_key "$manifest")") || return
    local _key _policy _url label _rest
    IFS=$'\x1f' read -r _key _policy _url label _rest <<< "$line"
    echo "$label"
}

get_validation_json_path() {
    local domain="$1"
    local schema="$2"
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/build.yaml"
    local policy=$(get_validation_policy "$manifest")

    # Bruk alltid generated/.../validation/ som kjelde — validate.yml kopierer
    # dit, og generate.yml kopierer dit frå src/linkml/
    local gen_validation_dir="$REPO_ROOT/generated/${domain}/${schema}/validation"

    local latest_version=$(get_latest_validation_version "$gen_validation_dir")
    [ -z "$latest_version" ] && return
    echo "$gen_validation_dir/$latest_version/${policy}.json"
}

# generate.yml sitt «Køyr modellanalyse per skjema»-steg skriv
# similar-classes-domain-report.md / similar-slots-domain-report.md hit —
# sjå specs/done/modellanalyse-per-skjema-index-md.md. I motsetnad til
# valideringsloggar er desse ikkje versjonslåste/committa (dei avheng av
# resten av domenet sitt innhald, ikkje berre dette skjemaet), så det finst
# berre éin, alltid-fersk katalog per skjema — ingen versjons-underkatalog.
get_model_analyse_dir() {
    local domain="$1"
    local schema="$2"
    local dir="$REPO_ROOT/generated/${domain}/${schema}/model-analyse"
    [ -d "$dir" ] || return
    echo "$dir"
}
