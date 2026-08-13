#!/usr/bin/env bash
# Generer Kom i gang-seksjon (seksjon 5 i index.md)
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

source "$REPO_ROOT/mkdocs/lib/utils/imported_schemas.sh"

generate_quickstart() {
    local domain="$1"
    local schema="$2"

    # Versjon, auto-detektert eksempel-klasse/-variabel og
    # quickstart-policy hentast frå det pre-berekna
    # SCHEMA_METADATA_SERIALIZED-registeret (Steg 1.5) i staden for to
    # separate `podman run`-kall per skjema — sjå
    # specs/backlog/reduser-podman-kall-docs-publish.md.
    local version="" example_class="" example_var="" policy="bronze"
    local line
    if line=$(lookup_schema_metadata_line "$domain/$schema"); then
        local _key _policy _url _label _title _desc quickstart_policy _rest
        IFS=$'\x1f' read -r _key _policy _url _label version _title _desc example_class example_var quickstart_policy _rest <<< "$line"
        policy="$quickstart_policy"
    fi
    local version_tag="${version:+${schema}-v$version}"
    local version_path="${version_tag:-main}"

    # Fallback-verdiar dersom skjemaet ikkje finst i registeret
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
    echo "  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/$version_path/src/linkml/$domain/$schema/$schema-schema"
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
