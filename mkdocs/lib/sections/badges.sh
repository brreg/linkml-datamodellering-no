#!/usr/bin/env bash
# Generer badge-rad (seksjon 2 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../utils/metadata_parsers.sh"

generate_badges() {
    local domain="$1"
    local schema="$2"
    local gendoc_index="$3"

    [ ! -f "$gendoc_index" ] && return 0

    # Parse metadata frå gen-doc
    local version=$(grep "^| Versjon" "$gendoc_index" | sed 's/.*| \([^ ]*\) |/\1/' | head -1)
    local status=$(grep "^| Status" "$gendoc_index" | sed 's|.*status/\([^)]*\).*|\1|' | head -1)
    local license=$(grep "^| Lisens" "$gendoc_index" | sed 's|.*/nlod/no/\([0-9.]*\).*|\1|' | head -1)
    local endringsdato=$(grep "^| Endringsdato" "$gendoc_index" | sed 's/^| Endringsdato | \(.*\) |$/\1/' | head -1)
    local utgiver_uri=$(grep "^| Utgiver" "$gendoc_index" | sed -n 's/^| Utgiver | \[\(https:[^]]*\)\].*/\1/p' | head -1)

    # Slå opp organisasjonsnamn i CODEOWNERS.md ved å matche org_uri mot utgiver-URI-en
    local utgiver_navn=""
    if [ -n "$utgiver_uri" ] && [ -f "$REPO_ROOT/CODEOWNERS.md" ]; then
        utgiver_navn=$(python3 - "$utgiver_uri" "$REPO_ROOT/CODEOWNERS.md" <<'PYEOF' 2>/dev/null
import re
import sys

import yaml

utgiver_uri, codeowners_file = sys.argv[1], sys.argv[2]

with open(codeowners_file, "r") as f:
    content = f.read()

match = re.search(r'^```yaml\n(.*?)\n```', content, re.MULTILINE | re.DOTALL)
if match:
    data = yaml.safe_load(match.group(1))
    for org in data.get('organizations', []):
        if org.get('org_uri', '') == utgiver_uri:
            print(org['name'])
            break
PYEOF
) || utgiver_navn=""
    fi

    # Valideringsstatus
    local validation_json=$(get_validation_json_path "$domain" "$schema")
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/build.yaml"
    local policy=$(get_validation_policy "$manifest")
    local val_status="ukjent"
    local val_color="lightgrey"

    if [ -f "$validation_json" ]; then
        # Støtt både errorCount (ny camelCase) og error_count (gamal snake_case)
        local errors=$(python3 -c "import json; d=json.load(open('$validation_json')); r=d.get('result', {}); print(r.get('errorCount', r.get('error_count', 0)))" 2>/dev/null || echo "0")
        [ -z "$errors" ] && errors="0"
        if [ "$errors" -eq 0 ]; then
            val_status="✓_godkjent"
            val_color="green"
        else
            val_status="${errors}_feil"
            val_color="yellow"
        fi
    fi

    # Normaliser status-namn
    local status_label="$status"
    local status_color="blue"
    case "$status" in
        Completed) status_label="Ferdigstilt"; status_color="green" ;;
        UnderDevelopment) status_label="Under_utvikling"; status_color="orange" ;;
        Deprecated) status_label="Foreldet"; status_color="red" ;;
        Withdrawn) status_label="Trukket_tilbake"; status_color="red" ;;
    esac

    # URL-encode
    local val_status_encoded="${val_status// /_}"
    val_status_encoded="${val_status_encoded//✓/%E2%9C%93}"
    local policy_encoded="${policy//-/_}"

    # Output badges
    echo "[![Versjon](https://img.shields.io/badge/versjon-${version}-blue)]()"
    echo "[![Status](https://img.shields.io/badge/status-${status_label}-${status_color})]()"
    echo "[![Validering](https://img.shields.io/badge/${policy_encoded}-${val_status_encoded}-${val_color})]()"
    [ -n "$license" ] && echo "[![Lisens](https://img.shields.io/badge/NLOD-${license}-blue)]()"
    if [ -n "$utgiver_navn" ]; then
        local utgiver_encoded="${utgiver_navn// /_}"
        utgiver_encoded="${utgiver_encoded//-/--}"
        echo "[![Utgiver](https://img.shields.io/badge/utgiver-${utgiver_encoded}-blue)]()"
    fi
    local endringsdato_encoded="${endringsdato//-/--}"
    [ -n "$endringsdato" ] && echo "[![Endringsdato](https://img.shields.io/badge/endringsdato-${endringsdato_encoded}-blue)]()"
    echo ""
    echo ""
}
