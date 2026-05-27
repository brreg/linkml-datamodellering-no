#!/usr/bin/env bash
# Genererer config.mk frå alle manifest.yaml-filer (skjema-manifest) i src/linkml/.
set -euo pipefail

echo "# Generert av src/assets/scripts/gen-config.sh — ikkje rediger manuelt"
echo "# Regenerer med: make config.mk"
echo ""

get_field() {
    grep -E "^  ${1}:" "${2}" | awk '{print $2}' || true
}

get_quoted_field() {
    grep -E "^  ${1}:" "${2}" | sed 's/.*: *"\(.*\)".*/\1/' || true
}

find src/linkml -mindepth 3 -maxdepth 3 -name 'manifest.yaml' \
    | grep -v '/common/' \
    | sort \
    | while IFS= read -r yaml; do
    domain=$(echo "$yaml" | cut -d/ -f3)
    model=$(echo "$yaml"  | cut -d/ -f4)
    key="${domain//-/_}_${model//-/_}"

    rdf=$(get_field "rdf" "$yaml")
    example_rdf=$(get_field "example_rdf" "$yaml")
    shacl_flags=$(get_quoted_field "shacl_flags" "$yaml")
    owl_flags=$(get_quoted_field "owl_flags" "$yaml")

    if [ "${rdf:-true}"         = "false" ]; then echo "GEN_RDF_SKIP_${key} := true"; fi
    if [ "${example_rdf:-true}" = "false" ]; then echo "EXAMPLE_RDF_SKIP_${key} := true"; fi
    if [ -n "${shacl_flags:-}" ]; then echo "SHACL_FLAGS_${key} := ${shacl_flags}"; fi
    if [ -n "${owl_flags:-}" ];   then echo "OWL_FLAGS_${key} := ${owl_flags}"; fi
done
