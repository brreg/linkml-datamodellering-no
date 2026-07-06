#!/usr/bin/env bash
# Kopier genererte artefakter til mkdocs/docs/
set -euo pipefail

copy_schema_artifacts() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$3"
    local out="$4"

    mkdir -p "$out/klasser"

    # Kopier artefaktfiler (berre filer, ikkje docs/-underkatalog)
    find "$schema_dir" -maxdepth 1 -type f -exec cp {} "$out/" \;

    # Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet)
    # Søk etter <schema>-schema.yaml i src/linkml/<domain>/*/
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    # Kopier CHANGELOG.md dersom den finst
    if [ -n "$src_dir" ] && [ -f "$src_dir/CHANGELOG.md" ]; then
        cp "$src_dir/CHANGELOG.md" "$out/CHANGELOG.md"
    fi

    # Kopier PlantUML-diagramfiler til diagrams/-underkatalog
    if [ -d "$schema_dir/diagrams" ]; then
        mkdir -p "$out/diagrams"
        find "$schema_dir/diagrams" -type f -exec cp {} "$out/diagrams/" \;
    fi

    # Kopier gen-doc markdown-filer til klasser/-underkatalog
    if [ -d "$schema_dir/docs" ]; then
        find "$schema_dir/docs" -name "*.md" -exec cp {} "$out/klasser/" \;
        # Rename alle .md-filer til lowercase (via .tmp for case-insensitive filsystem)
        for f in "$out/klasser/"*.md; do
            [ -f "$f" ] || continue
            local base=$(basename "$f")
            local lower=$(echo "$base" | tr '[:upper:]' '[:lower:]')
            if [ "$base" != "$lower" ]; then
                mv "$f" "$out/klasser/${lower}.tmp"
                mv "$out/klasser/${lower}.tmp" "$out/klasser/$lower"
            fi
        done
        # Oppdater alle interne .md-lenkjer til lowercase
        find "$out/klasser" -maxdepth 1 -name "*.md" \
            -exec sed -i 's/](\([^)]*\.md\))/](\L\1)/g' {} \;
    fi
}
