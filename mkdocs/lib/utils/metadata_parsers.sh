#!/usr/bin/env bash
# Parsing av manifest, validation-policy, versjon osv.
set -euo pipefail

source "$REPO_ROOT/mkdocs/lib/utils/python_container.sh"

# Les validation_policy/external_spec_url/external_spec_label frå build.yaml
# i éin python3-prosess og cache dei i eksporterte variablar, i staden for
# at get_validation_policy/get_external_spec_url/get_external_spec_label
# kvar gjer sitt eige python3-kall mot same fil (opptil 5 kall per skjema
# før denne endringa — sjå specs/backlog/batch-docs-publish-generering.md).
load_manifest_cache() {
    local manifest="$1"
    export MANIFEST_CACHE_PATH="$manifest"
    if [ ! -f "$manifest" ]; then
        export MANIFEST_CACHE_POLICY="bronze"
        export MANIFEST_CACHE_EXTERNAL_SPEC_URL=""
        export MANIFEST_CACHE_EXTERNAL_SPEC_LABEL=""
        return
    fi
    # Merk: `key=verdi`-format (ikkje reine verdi-linjer) er nødvendig sidan
    # `$(...)`-kommandosubstitusjon strippar ALLE etterfølgjande linjeskift —
    # med reine verdi-linjer ville ein tom external_spec_label (vanlegast
    # tilfelle) kollapsa dei siste linjeskilja og brote opplesinga.
    local container_manifest
    container_manifest=$(to_container_path "$manifest")
    local result
    result=$(run_python_container -c "
import yaml
d = yaml.safe_load(open('$container_manifest')) or {}
print('policy=' + str(d.get('validation_policy', 'bronze')))
print('external_spec_url=' + str(d.get('external_spec_url', '')))
print('external_spec_label=' + str(d.get('external_spec_label', '')))
" 2>&1) || { echo "ÅTVARING: kunne ikkje lese $manifest — bruker default-verdiar ($result)" >&2; result=""; }

    export MANIFEST_CACHE_POLICY="bronze"
    export MANIFEST_CACHE_EXTERNAL_SPEC_URL=""
    export MANIFEST_CACHE_EXTERNAL_SPEC_LABEL=""
    local key val
    # Prosess-substitusjon (< <(...)) garanterer eit avsluttande linjeskift,
    # slik at siste felt ikkje vert forkasta av `read` ved EOF utan newline.
    while IFS='=' read -r key val; do
        case "$key" in
            policy) MANIFEST_CACHE_POLICY="$val" ;;
            external_spec_url) MANIFEST_CACHE_EXTERNAL_SPEC_URL="$val" ;;
            external_spec_label) MANIFEST_CACHE_EXTERNAL_SPEC_LABEL="$val" ;;
        esac
    done < <(printf '%s\n' "$result")
}

get_validation_policy() {
    local manifest="$1"
    if [ "${MANIFEST_CACHE_PATH:-}" = "$manifest" ]; then
        echo "$MANIFEST_CACHE_POLICY"
        return
    fi
    [ ! -f "$manifest" ] && echo "bronze" && return
    local container_manifest
    container_manifest=$(to_container_path "$manifest")
    local policy
    if policy=$(run_python_container -c "import yaml; print(yaml.safe_load(open('$container_manifest')).get('validation_policy', 'bronze'))" 2>&1); then
        echo "$policy"
    else
        echo "ÅTVARING: kunne ikkje lese validation_policy frå $manifest — bruker bronze ($policy)" >&2
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
    local container_manifest
    container_manifest=$(to_container_path "$manifest")
    run_python_container -c "import yaml; print(yaml.safe_load(open('$container_manifest')).get('external_spec_url', ''))" 2>/dev/null || echo ""
}

get_external_spec_label() {
    local manifest="$1"
    if [ "${MANIFEST_CACHE_PATH:-}" = "$manifest" ]; then
        echo "$MANIFEST_CACHE_EXTERNAL_SPEC_LABEL"
        return
    fi
    [ ! -f "$manifest" ] && return
    local container_manifest
    container_manifest=$(to_container_path "$manifest")
    run_python_container -c "import yaml; print(yaml.safe_load(open('$container_manifest')).get('external_spec_label', ''))" 2>/dev/null || echo ""
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
