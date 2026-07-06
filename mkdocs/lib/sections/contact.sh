#!/usr/bin/env bash
# Generer kontaktinformasjon-seksjon (seksjon 19 i index.md)
set -euo pipefail

generate_contact_info() {
    local domain="$1"
    local schema="$2"
    local schema_path="src/linkml/${domain}/${schema}"

    echo ""
    echo "---"
    echo ""
    echo "## Kontakt"
    echo ""

    # Les CODEOWNERS.md for å finne eigar-org basert på path pattern
    local codeowners_file="$REPO_ROOT/CODEOWNERS.md"
    if [ ! -f "$codeowners_file" ]; then
        echo "**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)"
        echo ""
        return
    fi

    # Ekstraher YAML-frontmatter frå CODEOWNERS.md
    # Parse YAML og match path mot path_patterns for kvar org
    local org_data=$(python3 - "$schema_path" "$codeowners_file" <<'PYEOF'
import sys
import re
import yaml

schema_path = sys.argv[1]
codeowners_file = sys.argv[2]

with open(codeowners_file, "r") as f:
    content = f.read()

# Ekstraher YAML-frontmatter (mellom første ``` og neste ```)
match = re.search(r'^```yaml\n(.*?)\n```', content, re.MULTILINE | re.DOTALL)
if not match:
    sys.exit(1)

yaml_content = match.group(1)
data = yaml.safe_load(yaml_content)

# Match schema_path mot path_patterns for kvar org
for org in data.get('organizations', []):
    for pattern in org.get('path_patterns', []):
        # Konverter glob-pattern til regex (enkel variant — berre ** og *)
        # Bruk placeholder for å unngå at * i .* vert erstatta
        regex_pattern = pattern.replace('**', '__DOUBLESTAR__').replace('*', '[^/]*').replace('__DOUBLESTAR__', '.*')
        # Gjer /** valfri for å matche både "path" og "path/noko"
        regex_pattern = re.sub(r'/\.\*$', r'(/.*)?', regex_pattern)
        if re.search(regex_pattern, schema_path):
            # Fann match — print org-data som YAML
            print(f"name: {org['name']}")
            print(f"org_uri: {org['org_uri']}")
            print(f"contact_uri: {org.get('contact_uri', '')}")
            sys.exit(0)

# Ingen match funne
sys.exit(1)
PYEOF
)

    if [ $? -eq 0 ] && [ -n "$org_data" ]; then
        # Ekstraher felt frå org_data
        local name=$(echo "$org_data" | grep '^name:' | sed 's/^name: //')
        local org_uri=$(echo "$org_data" | grep '^org_uri:' | sed 's/^org_uri: //')
        local contact_uri=$(echo "$org_data" | grep '^contact_uri:' | sed 's/^contact_uri: //')

        echo "**Forvaltningsansvarleg:** [$name]($org_uri)"
        echo ""
        if [ -n "$contact_uri" ]; then
            echo "**Kontakt:** [$name - Kontakt]($contact_uri)"
            echo ""
        fi
        echo "**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)"
    else
        # Fallback — ingen match funne
        echo "**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)"
    fi
    echo ""
}
