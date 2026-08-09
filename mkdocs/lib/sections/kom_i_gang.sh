#!/usr/bin/env bash
# Generer Kom i gang-seksjon (seksjon 5 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

source "$REPO_ROOT/mkdocs/lib/utils/python_container.sh"

generate_quickstart() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet (kan vere ulik $schema-namnet)
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    # Les versjon frå skjemaet
    local version=""
    if [ -n "$schema_file" ]; then
        version=$(run_python_container -c "import yaml, sys; d=yaml.safe_load(open('$(to_container_path "$schema_file")')); print(d.get('version', ''))" 2>/dev/null || echo "")
    fi
    local version_tag="${version:+${schema}-v$version}"
    local version_path="${version_tag:-main}"

    # Auto-detekter EXAMPLE_CLASS, EXAMPLE_VAR og POLICY
    local example_class=""
    local example_var=""
    local policy="bronze"

    if [ -n "$schema_file" ]; then
        # Python-script for auto-deteksjon
        read -r example_class example_var policy < <(run_python_container - "$(to_container_path "$schema_file")" <<'PYEOF'
import yaml
import sys
import os
import re

schema_file = sys.argv[1]

# Les skjema
with open(schema_file) as f:
    schema = yaml.safe_load(f)

# Les build.yaml for validation_policy
build_file = os.path.join(os.path.dirname(schema_file), 'build.yaml')
policy = 'bronze'  # default
if os.path.exists(build_file):
    with open(build_file) as f:
        build_config = yaml.safe_load(f)
        if build_config:
            policy = build_config.get('validation_policy', 'bronze')

# Finn container-klassenamn
container_class = None
for cls_name, cls_def in schema.get('classes', {}).items():
    if isinstance(cls_def, dict) and cls_def.get('tree_root'):
        container_class = cls_name
        break

# Finn representativ klasse
example_class = None

# Prioritet 1: Obligatorisk subset
for cls_name, cls_def in schema.get('classes', {}).items():
    if not isinstance(cls_def, dict):
        continue
    if cls_name == container_class:
        continue
    if 'Obligatorisk' in cls_def.get('in_subset', []):
        example_class = cls_name
        break

# Prioritet 2: Anbefalt subset
if not example_class:
    for cls_name, cls_def in schema.get('classes', {}).items():
        if not isinstance(cls_def, dict):
            continue
        if cls_name == container_class:
            continue
        if 'Anbefalt' in cls_def.get('in_subset', []):
            example_class = cls_name
            break

# Prioritet 3: Første ikkje-container-klasse
if not example_class:
    for cls_name, cls_def in schema.get('classes', {}).items():
        if not isinstance(cls_def, dict):
            continue
        if cls_name == container_class:
            continue
        if not cls_def.get('abstract'):
            example_class = cls_name
            break

# Fallback til containerklassen
if not example_class:
    example_class = container_class or "Container"

# Generer variabelnamn (lowercase, konverter PascalCase til snake_case)
example_var = re.sub('([a-z0-9])([A-Z])', r'\1_\2', example_class).lower()

print(f"{example_class} {example_var} {policy}")
PYEOF
)
    fi

    # Fallback-verdiar dersom auto-deteksjon feiler
    example_class="${example_class:-Container}"
    example_var="${example_var:-container}"
    policy="${policy:-bronze}"

    # Generer standard struktur (dynamisk, same for alle modellar)
    echo "## Kom i gang"
    echo ""
    echo "> Her finn du døme på korleis du importerer, validerer og brukar modellen i eigne prosjekt."
    echo ""
    echo "### Importer i egne LinkML-skjema"
    echo ""
    echo "\`\`\`yaml"
    echo "imports:"
    echo "  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/$version_path/src/linkml/$domain/$schema/$schema-schema.yaml"
    echo "\`\`\`"
    echo ""
    echo "### Valider skjemaet mot $policy-policy"
    echo ""
    echo "\`\`\`bash"
    echo "make mcp-linkml-valider-modell SCHEMA=src/linkml/$domain/$schema/$schema-schema.yaml"
    echo "\`\`\`"
    echo ""
    echo "### Valider datafil mot LinkML-skjemaet"
    echo ""
    echo "\`\`\`bash"
    echo "make validate-instance SCHEMA=src/linkml/$domain/$schema/$schema-schema.yaml INSTANCE=mine-data.yaml"
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
    echo "from ${schema//-/_}_model import $example_class"
    echo ""
    echo "$example_var = yaml_loader.load('mine-data.yaml', target_class=$example_class)"
    echo "\`\`\`"
    echo ""
    echo ""
}
