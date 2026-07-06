#!/usr/bin/env bash
# Generer avhengigheitstre (seksjon 9 i index.md)
set -euo pipefail

generate_dependencies() {
    local domain="$1"
    local schema="$2"

    # Finn schema-fil (handter både ${schema}-schema.yaml og ${schema}-*-schema.yaml)
    local schema_path="$REPO_ROOT/src/linkml/$domain/$schema/${schema}-schema.yaml"
    if [ ! -f "$schema_path" ]; then
        # Fallback: finn *-schema.yaml i katalogen (t.d. common/common-ap-no-schema.yaml)
        schema_path=$(find "$REPO_ROOT/src/linkml/$domain/$schema" -maxdepth 1 -name "*-schema.yaml" | head -1)
    fi

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
        echo "---"
        echo ""
        echo "## Avhengigheiter"
        echo ""
        echo "### Imports"
        echo ""
        echo "Dette skjemaet importerer følgjande skjema (direkte og transitivt):"
        echo ""
        echo "\`\`\`"
        # Kall Python-script for å bygge hierarkisk tre
        # Send normaliserte direkte importar som tredje argument
        python3 "$REPO_ROOT/src/assets/scripts/parse-dependency-tree.py" "$schema" "$imports" "$direct_imports_normalized"
        echo "\`\`\`"
        echo ""
        echo "!!! note \"Leseretning\""
        echo "    Diagrammet ovanfor viser avhengigheiter **frå høgre til venstre**. Dette skjemaet"
        echo "    importerer dei skjemaa som står lengst til høgre, som igjen automatisk inkluderer"
        echo "    alle sine avhengigheiter lengre til venstre i treet."
        echo ""
        echo "*Sjå [Importhierarki](../../importhierarki.md) for fullstendig importkjede.*"
        echo ""
        echo ""
    fi
}
