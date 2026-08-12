#!/usr/bin/env bash
# Kopier genererte artefakter til mkdocs/docs/
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

source "$REPO_ROOT/mkdocs/lib/utils/imported_schemas.sh"

copy_schema_artifacts() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$3"
    local out="$4"

    mkdir -p "$out/klasser"

    # Kopier artefaktfiler (berre filer, ikkje docs/-underkatalog)
    # -exec ... + batchar alle filer inn i færre cp-prosessar (i staden for
    # éin cp-prosess per fil) — sjå specs/backlog/batch-docs-publish-generering.md
    find "$schema_dir" -maxdepth 1 -type f -exec cp -t "$out" {} +

    # Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet) via det
    # pre-berekna oppslaget frå Steg 1.5 i staden for eit eige find-kall —
    # sjå specs/backlog/batch-docs-publish-generering.md
    local schema_file
    schema_file=$(lookup_schema_path "${schema}-schema") || schema_file=""
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    # Kopier CHANGELOG.md dersom den finst
    if [ -n "$src_dir" ] && [ -f "$src_dir/CHANGELOG.md" ]; then
        cp "$src_dir/CHANGELOG.md" "$out/CHANGELOG.md"
    fi

    # Kopier metadata/<schema>-manifest.yaml dersom den finst
    if [ -n "$src_dir" ] && [ -f "$src_dir/metadata/${schema}-manifest.yaml" ]; then
        cp "$src_dir/metadata/${schema}-manifest.yaml" "$out/${schema}-manifest.yaml"
    fi

    # Kopier validation/-katalog dersom den finst i generated/ (populert frå CI eller lokal validering)
    # Merk: generated/ er autorativ kjelde her — publish.sh les frå generated/, ikkje src/
    if [ -d "$schema_dir/validation" ]; then
        mkdir -p "$out/validation"
        cp -r "$schema_dir/validation"/* "$out/validation/" 2>/dev/null || true
    fi

    # Kopier PlantUML-diagramfiler til diagrams/-underkatalog
    if [ -d "$schema_dir/diagrams" ]; then
        mkdir -p "$out/diagrams"
        find "$schema_dir/diagrams" -type f -exec cp -t "$out/diagrams" {} +
    fi

    # Kopier gen-doc markdown-filer til klasser/-underkatalog
    if [ -d "$schema_dir/docs" ]; then
        find "$schema_dir/docs" -name "*.md" -exec cp -t "$out/klasser" {} +
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
            -exec sed -i 's/](\([^)]*\.md\))/](\L\1)/g' {} +
        # Oppdater mermaid click-hrefs til lowercase — href vert bygd på nytt
        # frå namnet i click-statementet (ikkje frå den eksisterande
        # href-verdien, som for typar som Uriorcurie kan innehalde ein
        # innbaka XSD-URI i staden for typenamnet, sjå
        # specs/backlog/mermaid-klikkbare-lenker-404.md)
        find "$out/klasser" -maxdepth 1 -name "*.md" \
            -exec sed -i -E 's|click ([A-Za-z0-9_]+) href "[^"]*"|click \1 href "../\L\1\E/"|g' {} +
    fi
}
