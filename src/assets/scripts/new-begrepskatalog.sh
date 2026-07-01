#!/usr/bin/env bash
# Opprettar filstruktur og boilerplate for ein ny LinkML-begrepskatalog.
# Bruk: bash src/assets/scripts/new-begrepskatalog.sh <name>
set -euo pipefail

NAME="${1:-}"

if [[ -z "$NAME" ]]; then
    echo "Feil: NAME er påkravd." >&2
    echo "Bruk: make new-begrepskatalog NAME=<katalognavn>" >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
SCHEMA_DIR="$REPO_ROOT/src/linkml/begrepskatalog/$NAME"
EXAMPLES_DIR="$SCHEMA_DIR/examples"
SCHEMA_FILE="$SCHEMA_DIR/$NAME-schema.yaml"
EXAMPLE_FILE="$EXAMPLES_DIR/$NAME-eksempel.yaml"
MANIFEST_FILE="$SCHEMA_DIR/manifest.yaml"
DESCRIPTION_FILE="$SCHEMA_DIR/description.md"

if [[ -d "$SCHEMA_DIR" ]]; then
    echo "Feil: katalogen $SCHEMA_DIR finst allereie." >&2
    exit 1
fi

# LinkML name-felt: bindestrek er ikkje tillate, bruk understrek
SCHEMA_NAME="${NAME//-/_}"
SCHEMA_ID="https://data.norge.no/begrepskatalog/$NAME"

mkdir -p "$SCHEMA_DIR"
mkdir -p "$EXAMPLES_DIR"

cat > "$SCHEMA_FILE" << EOF
id: $SCHEMA_ID
name: $SCHEMA_NAME
title: 'TODO: <Organisasjon> - Begrepskatalog'
description: 'TODO: beskriv katalogen'
version: "0.1.0"
license: https://data.norge.no/nlod/no/2.0

annotations:
  utgiver: 'TODO: https://data.norge.no/organizations/<orgnr>'
  status: http://purl.org/adms/status/UnderDevelopment

prefixes:
  linkml: https://w3id.org/linkml/

default_prefix: $SCHEMA_ID/
default_range: string

imports:
  - linkml:types
  - ../../ap-no/skos-ap-no/skos-ap-no-schema

classes:

  BegrepContainer:
    tree_root: true
    attributes:
      begrep:
        range: Begrep
        multivalued: true
        inlined: true
        inlined_as_list: true
      samlingar:
        range: Samling
        multivalued: true
        inlined: true
        inlined_as_list: true
      definisjoner:
        range: Definisjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      generiske_relasjonar:
        range: GeneriskRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      partitive_relasjonar:
        range: PartitivRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      assosiative_relasjonar:
        range: AssosiativRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      organisasjonar:
        range: Organisasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      kontaktpunkt:
        range: VCardKontakt
        multivalued: true
        inlined: true
        inlined_as_list: true
EOF

cat > "$MANIFEST_FILE" << 'EOF'
publish_external: false
data_policy: felles-begrepskatalog

generators:
  jsonld_context: true
  shacl: false
  python: false
  json_schema: true
  owl: false
  rdf: true
  protobuf: false
  erdiagram: true
  docs: true
  plantuml: false
  example_rdf: true
  openapi: true
EOF

cat > "$EXAMPLE_FILE" << EOF
# Eksempel for $NAME
# Generer YAML-blokker med: make mcp-begrep-run (sjå ny-begrepsmodell.md steg 4)
---
BegrepContainer:
  begrep: []
EOF

cat > "$DESCRIPTION_FILE" << EOF
<!-- Valfri skildring av $NAME. Vert vist i portalen mellom ER-diagrammet og klasselista. -->
<!-- Fyll ut eller slett denne fila. -->
EOF

echo ""
echo "Oppretta:"
echo "  $SCHEMA_FILE"
echo "  $EXAMPLE_FILE"
echo "  $MANIFEST_FILE"
echo "  $DESCRIPTION_FILE"
echo ""
echo "Neste steg:"
echo "  1. Fyll ut title, description, utgiver i $SCHEMA_FILE"
echo "  2. Generer YAML-instansar: sjå ny-begrepsmodell.md steg 4"
echo "  3. Valider: make mcp-validate SCHEMA=$SCHEMA_FILE POLICY=bronze"
