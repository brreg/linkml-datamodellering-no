#!/usr/bin/env bash
# Generer Kom i gang-seksjon (seksjon 5 i index.md)
set -euo pipefail

generate_quickstart() {
    local domain="$1"
    local schema="$2"
    local quickstart_file="$REPO_ROOT/src/linkml/$domain/quickstart.md"

    # Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet)
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    local example_file=""
    [ -n "$src_dir" ] && example_file="$src_dir/examples/${schema}-eksempel.yaml"

    if [ -f "$quickstart_file" ]; then
        # Les og inject quickstart.md med variabel-substitusjon
        sed "s/{{SCHEMA}}/$schema/g; s/{{SCHEMA_UNDERSCORE}}/${schema//-/_}/g" "$quickstart_file"
        echo ""
        echo ""
    elif [ "$domain" = "ap-no" ]; then
        # Fallback: AP-NO Quickstart (hardkoda)
        echo "## Kom i gang"
        echo ""
        echo "### Importer i LinkML-skjema"
        echo ""
        echo "\`\`\`yaml"
        echo "imports:"
        echo "  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/$schema/$schema-schema"
        echo "\`\`\`"
        echo ""
        echo "### Python-bruk"
        echo ""
        echo "\`\`\`bash"
        echo "pip install linkml-runtime pyyaml"
        echo "\`\`\`"
        echo ""
        echo "\`\`\`python"
        echo "from linkml_runtime.loaders import yaml_loader"
        echo "from ${schema//-/_}_model import Katalog"
        echo ""
        echo "katalog = yaml_loader.load('eksempel.yaml', target_class=Katalog)"
        echo "print(katalog.tittel)"
        echo "\`\`\`"
        echo ""
        echo "### Valider data mot SHACL"
        echo ""
        echo "\`\`\`bash"
        echo "pyshacl --shacl $schema-shapes.ttl --data-format turtle mine-data.ttl"
        echo "\`\`\`"
        echo ""
        echo ""
    elif [ -f "$example_file" ]; then
        # Fallback: Domenemodell Quickstart (hardkoda)
        echo "## Kom i gang"
        echo ""
        echo "### Valider eiga datafil"
        echo ""
        echo "\`\`\`bash"
        echo "linkml-validate -s $schema-schema.yaml mine-data.yaml"
        echo "\`\`\`"
        echo ""
        echo ""
    fi
}
