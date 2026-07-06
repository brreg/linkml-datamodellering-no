#!/usr/bin/env bash
# Generer eksempeldatafil-seksjon (seksjon 6 i index.md)
set -euo pipefail

generate_example() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet)
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    local example_file=""
    [ -n "$src_dir" ] && example_file="$src_dir/examples/${schema}-eksempel.yaml"

    [ ! -f "$example_file" ] && return 0

    # Rekonstruer relative sti frå src/linkml/ for GitHub-lenke
    local relative_path="${src_dir#$REPO_ROOT/src/linkml/}"

    echo "---"
    echo ""
    echo "## Eksempeldatafil"
    echo ""
    echo "### YAML"
    echo ""
    echo "\`\`\`yaml"
    # Ekstraher første 20 liner (eller til første tom linje etter header)
    head -20 "$example_file" | awk '
        NR == 1 && /^#/ { in_header = 1 }
        in_header && /^$/ { in_header = 0; next }
        !in_header { print }
        NR > 20 { exit }
    '
    echo "\`\`\`"
    echo ""
    echo "[📄 Full eksempelfil (YAML)](https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/$relative_path/examples/$schema-eksempel.yaml)"
    echo ""
    echo "*Detaljerte eksempel per klasse finst på kvar klasseside, t.d. [Classes](#classes).*"
    echo ""
    echo ""
}
