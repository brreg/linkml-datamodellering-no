#!/usr/bin/env bash
# Opprettar filstruktur og boilerplate for ei ny begrepssamling.
# Bruk: bash src/assets/scripts/new-begrepssamling.sh <domain> <begrepssamling-namn>
set -euo pipefail

DOMAIN="${1:-}"
NAME="${2:-}"

if [[ -z "$DOMAIN" ]]; then
    echo "Feil: DOMAIN er påkravd." >&2
    echo "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>" >&2
    echo "Døme: make new-begrepssamling DOMAIN=oreg NAME=begrepssamling-foretaksregisteret" >&2
    exit 1
fi

if [[ -z "$NAME" ]]; then
    echo "Feil: NAME er påkravd." >&2
    echo "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>" >&2
    echo "Døme: make new-begrepssamling DOMAIN=oreg NAME=begrepssamling-foretaksregisteret" >&2
    exit 1
fi

# Valider at NAME startar med "begrepssamling-"
if [[ ! "$NAME" =~ ^begrepssamling- ]]; then
    echo "Feil: NAME må starte med 'begrepssamling-'" >&2
    echo "Døme: begrepssamling-foretaksregisteret" >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
SCHEMA_DIR="$REPO_ROOT/src/linkml/$DOMAIN/$NAME"
BEGREP_DIR="$SCHEMA_DIR/begrep"
MANIFEST_FILE="$SCHEMA_DIR/build.yaml"

if [[ -d "$SCHEMA_DIR" ]]; then
    echo "Feil: katalogen $SCHEMA_DIR finst allereie." >&2
    exit 1
fi

mkdir -p "$BEGREP_DIR"

cat > "$MANIFEST_FILE" << 'EOF'
publish_external: false
validation_policy: bronze

# Metadata for aggregering til begrepskatalog
# aggregation-metadata vert auto-detektert frå CODEOWNERS.md basert på path-matching
# (kan overstyrast ved å legge til eksplisitt aggregation-blokk her)

generators:
  jsonld_context: false
  shacl: false
  python: false
  json_schema: false
  owl: false
  rdf: false
  protobuf: false
  erdiagram: false
  docs: false
  plantuml: false
  example_rdf: false
EOF

cat > "$BEGREP_DIR/.gitkeep" << 'EOF'
# Denne mappa inneheld éin YAML-fil per begrep.
# Bruk mcp-linkml-begrep-utkast til å generere begrepsfiler:
#   make mcp-begrep-run
# Eller skriv manuelt i formatet:
#   id: https://begrep.org.no/<slug>
#   anbefalt_term: [...]
#   har_definisjon: [...]
#   identifikator_literal: "..."
#   kontaktpunkt_vcard: [...]
#   utgjevar: https://data.norge.no/organizations/<orgnr>
#   fagomrade: [...]
EOF

echo ""
echo "Oppretta:"
echo "  $MANIFEST_FILE"
echo "  $BEGREP_DIR/"
echo ""
echo "Neste steg:"
echo "  1. Skriv begrep til begrep/<begrep-slug>.yaml (manuelt eller med mcp-linkml-begrep-utkast):"
echo "     make mcp-begrep-run"
echo "     Bruk verktøyet 'skriv_begrep_fil' med domain=$DOMAIN og begrepssamling=$NAME"
echo "  2. Køyr gen-begrepskatalog-instance for å aggregere til begrepskatalog:"
echo "     make gen-begrepskatalog-instance"
echo "  3. Valider begrepskatalogen:"
echo "     make mcp-validate SCHEMA=src/linkml/begrepskatalog/<katalog>/<katalog>-schema.yaml POLICY=felles-begrepskatalog"
