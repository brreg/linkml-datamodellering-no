#!/usr/bin/env bash
# Opprettar katalogstruktur for ein ny organisasjon sin modellkatalog.
# Krev at organisasjonen er registrert i CODEOWNERS.md-frontmatter.
# Bruk: bash src/assets/scripts/new-modellkatalog.sh <alias>
set -euo pipefail

ALIAS="${1:-}"

if [[ -z "$ALIAS" ]]; then
    echo "Feil: NAME-alias er påkravd." >&2
    echo "Bruk: make new-modellkatalog NAME=<alias>" >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
CODEOWNERS="$REPO_ROOT/CODEOWNERS.md"

if [[ ! -f "$CODEOWNERS" ]]; then
    echo "Feil: Fann ikkje CODEOWNERS.md i repo-rota." >&2
    exit 1
fi

# Les org-metadata frå CODEOWNERS.md-frontmatter
ORG_META=$(python3 - "$ALIAS" "$CODEOWNERS" << 'PYEOF'
import shlex
import sys, yaml

alias = sys.argv[1]
path  = sys.argv[2]

with open(path, encoding="utf-8") as f:
    content = f.read()

if not content.startswith("---"):
    print("FEIL: Ingen YAML-frontmatter i CODEOWNERS.md", file=sys.stderr)
    sys.exit(1)

parts = content.split("---", 2)
data = yaml.safe_load(parts[1]) or {}
orgs = {o["alias"]: o for o in data.get("organizations", [])}

if alias not in orgs:
    print(f"FEIL: Alias '{alias}' ikkje funne i CODEOWNERS.md. Legg til org i frontmatter fyrst.", file=sys.stderr)
    sys.exit(1)

org = orgs[alias]
for k in ("name", "org_uri", "catalog_slug", "catalog_title", "contact_uri"):
    val = org.get(k, "TODO")
    print(f"{k}={shlex.quote(str(val))}")
PYEOF
)

# Eksporter variablar frå Python-output
eval "$ORG_META"
# shellcheck disable=SC2154
CATALOG_DIR="$REPO_ROOT/src/linkml/modellkatalog/$catalog_slug"

if [[ -d "$CATALOG_DIR" ]]; then
    echo "Feil: Katalogen $CATALOG_DIR finst allereie." >&2
    exit 1
fi

TEMPLATE_DIR="$REPO_ROOT/src/linkml/modellkatalog/brreg-modellkatalog"
if [[ ! -d "$TEMPLATE_DIR" ]]; then
    echo "Feil: Malen $TEMPLATE_DIR finst ikkje." >&2
    exit 1
fi

echo "Oppretter katalog for $name ($ALIAS) ..."

mkdir -p "$CATALOG_DIR/examples"
mkdir -p "$CATALOG_DIR/data/$catalog_slug"

# --- Katalogskjema ---
SCHEMA_ID="https://data.norge.no/modellkatalog/$catalog_slug"
cat > "$CATALOG_DIR/$catalog_slug-schema.yaml" << YAML
id: $SCHEMA_ID
name: $catalog_slug
title: $catalog_title
description: >-
  Modellkatalog for $name sine informasjonsmodellar.
  Implementerer ModelDCAT-AP-NO direkte via import.
version: "1.0.0"

prefixes:
  linkml:       https://w3id.org/linkml/
  modelldcatno: https://data.norge.no/vocabulary/modelldcatno#
  dcat:         http://www.w3.org/ns/dcat#
  dct:          http://purl.org/dc/terms/

default_prefix: $SCHEMA_ID/
default_range: string

imports:
  - linkml:types
  - ../../ap-no/modelldcat-ap-no/modelldcat-ap-no-schema

classes:

  ModellkatalogContainer:
    tree_root: true
    attributes:
      modellkataloger:
        range: Modellkatalog
        multivalued: true
        inlined: true
        inlined_as_list: true
      informasjonsmodeller:
        range: Informasjonsmodell
        multivalued: true
        inlined: true
        inlined_as_list: true
      objekttyper:
        range: Objekttype
        multivalued: true
        inlined: true
        inlined_as_list: true
      kodelister:
        range: Kodeliste
        multivalued: true
        inlined: true
        inlined_as_list: true
      kodeelementer:
        range: Kodeelement
        multivalued: true
        inlined: true
        inlined_as_list: true
      enkeltyper:
        range: Enkeltype
        multivalued: true
        inlined: true
        inlined_as_list: true
      attributter:
        range: Attributt
        multivalued: true
        inlined: true
        inlined_as_list: true
      assosiasjoner:
        range: Assosiasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      aktoerer:
        range: Aktoer
        multivalued: true
        inlined: true
        inlined_as_list: true
      kontaktpunkt:
        range: Kontaktopplysning
        multivalued: true
        inlined: true
        inlined_as_list: true
YAML

# --- Manifest (skjema) ---
cat > "$CATALOG_DIR/build.yaml" << 'YAML'
publish_external: true

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
  example_rdf: false
  openapi: true
YAML

# --- Katalogdatafil ---
CATALOG_BASE_URI="https://data.norge.no/modellkatalog/$catalog_slug"
cat > "$CATALOG_DIR/data/$catalog_slug/$catalog_slug.yaml" << YAML
modellkataloger:
- id: $CATALOG_BASE_URI
  tittel:
  - $catalog_title
  beskrivelse:
  - "TODO: legg til skildring av katalogen"
  identifikator_literal: $CATALOG_BASE_URI
  utgiver: $org_uri
  kontaktpunkt:
  - $contact_uri
  har_del: []
  modell: []
  spraak:
  - http://publications.europa.eu/resource/authority/language/NOB
  lisens: http://publications.europa.eu/resource/authority/licence/CC_BY_4_0
informasjonsmodeller: []
aktoerer:
- id: $contact_uri
  navn_aktoer:
  - "TODO: namn på kontaktpunktet"
- id: $org_uri
  navn_aktoer:
  - $name
YAML

# --- Datafil-manifest ---
cat > "$CATALOG_DIR/data/$catalog_slug/build.yaml" << 'YAML'
publish_external: true
validation_policy: felles-datakatalog
YAML

# --- Eksempelfil ---
cat > "$CATALOG_DIR/examples/$catalog_slug-eksempel.yaml" << YAML
modellkataloger:
- id: $CATALOG_BASE_URI/eksempel
  tittel:
  - $catalog_title (eksempel)
  beskrivelse:
  - Eksempel på ein modellkatalogpost.
  identifikator_literal: $CATALOG_BASE_URI/eksempel
  utgiver: $org_uri
  kontaktpunkt:
  - $contact_uri
  har_del: []
  modell: []
  spraak:
  - http://publications.europa.eu/resource/authority/language/NOB
  lisens: http://publications.europa.eu/resource/authority/licence/CC_BY_4_0
informasjonsmodeller: []
aktoerer: []
YAML

echo ""
echo "Oppretta:"
echo "  $CATALOG_DIR/$catalog_slug-schema.yaml"
echo "  $CATALOG_DIR/build.yaml"
echo "  $CATALOG_DIR/data/$catalog_slug/$catalog_slug.yaml"
echo "  $CATALOG_DIR/data/$catalog_slug/build.yaml"
echo "  $CATALOG_DIR/examples/$catalog_slug-eksempel.yaml"
echo ""
echo "Neste steg:"
echo "  1. Fyll inn TODO-verdiar i datafila: $CATALOG_DIR/data/$catalog_slug/$catalog_slug.yaml"
echo "  2. Legg til annotations.utgiver: $org_uri i skjemaa din org eig"
echo "  3. make update-modellkatalog   # synkroniser katalogen med skjema-annotasjonar"
echo "  4. make mcp-validate SCHEMA=$CATALOG_DIR/$catalog_slug-schema.yaml POLICY=felles-datakatalog INSTANCE=$CATALOG_DIR/data/$catalog_slug/$catalog_slug.yaml"
