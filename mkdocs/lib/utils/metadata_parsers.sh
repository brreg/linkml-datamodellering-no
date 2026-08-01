#!/usr/bin/env bash
# Parsing av manifest, validation-policy, versjon osv.
set -euo pipefail

get_validation_policy() {
    local manifest="$1"
    [ ! -f "$manifest" ] && echo "bronze" && return
    python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('validation_policy', 'bronze'))" 2>/dev/null || echo "bronze"
}

get_latest_validation_version() {
    local validation_dir="$1"
    [ ! -d "$validation_dir" ] && return
    ls -v "$validation_dir" 2>/dev/null | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | tail -n1
}

get_external_spec_url() {
    local manifest="$1"
    [ ! -f "$manifest" ] && return
    python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('external_spec_url', ''))" 2>/dev/null || echo ""
}

get_external_spec_label() {
    local manifest="$1"
    [ ! -f "$manifest" ] && return
    python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('external_spec_label', ''))" 2>/dev/null || echo ""
}

get_validation_json_path() {
    local domain="$1"
    local schema="$2"
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/build.yaml"
    local policy=$(get_validation_policy "$manifest")

    # Prioriter generated/ (nyare, frå generate-workflow) over src/ (eldre, frå validate-workflow)
    local generated_validation_dir="$REPO_ROOT/generated/${domain}/${schema}/validation"
    local src_validation_dir="$REPO_ROOT/src/linkml/${domain}/${schema}/validation"

    local latest_version=$(get_latest_validation_version "$generated_validation_dir")
    if [ -n "$latest_version" ] && [ -f "$generated_validation_dir/$latest_version/${policy}.json" ]; then
        echo "$generated_validation_dir/$latest_version/${policy}.json"
        return
    fi

    latest_version=$(get_latest_validation_version "$src_validation_dir")
    [ -z "$latest_version" ] && return
    echo "$src_validation_dir/$latest_version/${policy}.json"
}
