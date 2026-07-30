#!/usr/bin/env bash
# Generer avhengigheitstre (seksjon 9 i index.md)
set -euo pipefail

generate_dependencies() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet)
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local schema_path=""
    [ -n "$schema_file" ] && schema_path="$schema_file"

    # Parse direkte importar frå dette skjemaet
    local imports=""
    local direct_imports_normalized=""
    if [ -f "$schema_path" ]; then
        # Behald -schema-suffiks (ikkje strip det)
        imports=$(sed -n '/^imports:/,/^[a-z_]/p' "$schema_path" | grep -E "^[ ]*- " | sed 's/^[ ]*- //' | sed 's|^\.\./\.\./||' | sed 's|^\.\./||')
        # Normaliser til skjemanamn (basename) for direkte-import-matching
        direct_imports_normalized=$(echo "$imports" | tr ' ' '\n' | xargs -I {} basename {} | tr '\n' ' ')
    fi

    # Output (hierarkisk tre med transitive avhengigheiter)
    if [ -n "$imports" ]; then
        # Bygg dependency tree og tel antal imports
        local dep_tree
        dep_tree=$(python3 "$REPO_ROOT/mkdocs/lib/scripts/parse-dependency-tree.py" "$schema" "$imports" "$direct_imports_normalized")
        local import_count
        import_count=$(echo "$dep_tree" | grep -c '^' || echo 0)

        echo "---"
        echo ""
        echo "## Avhengigheiter ($import_count) {#avhengigheiter}"
        echo ""
        echo "### Imports"
        echo ""
        echo "Dette skjemaet importerer følgjande skjema (direkte og transitivt):"
        echo ""
        echo "\`\`\`"
        echo "$dep_tree"
        echo "\`\`\`"
        echo ""
        echo "!!! note \"Leseretning\""
        echo "    Diagrammet ovanfor viser avhengigheiter **frå høgre til venstre**. Dette skjemaet"
        echo "    importerer dei skjemaa som står lengst til høgre, som igjen automatisk inkluderer"
        echo "    alle sine avhengigheiter lengre til venstre i treet."
        echo ""
        echo "*Sjå [Importhierarki](../../importhierarki.md) for oversikt over heile repoet sitt importhierarki.*"
        echo ""
        echo ""
    fi
}
