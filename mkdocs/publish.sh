#!/usr/bin/env bash
# Kopier genererte artefaktar til mkdocs/docs/ og generer index-sider og mkdocs.yml.
# Køyr etter make <domain> eller make validate.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GEN="$REPO_ROOT/generated"
DOCS="$REPO_ROOT/mkdocs/docs"
MKDOCS_YML="$REPO_ROOT/mkdocs/mkdocs.yml"

# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------

domain_label() {
    case "$1" in
        ap-no) echo "AP-NO – Applikasjonsprofiler" ;;
        ngr)   echo "NGR – Nasjonale Grunndata" ;;
        fint)  echo "FINT – Fylkeskommunale integrasjonar" ;;
        fair)  echo "FAIR – Metadataoverbygning" ;;
        oreg)  echo "OREG – Offentlege registre" ;;
        *)     echo "$1" | awk '{print toupper($0)}' ;;
    esac
}

artifact_label() {
    case "$1" in
        shapes.ttl)     echo "SHACL shapes" ;;
        ontology.ttl)   echo "OWL ontologi" ;;
        schema.ttl)     echo "RDF/Turtle skjema" ;;
        context.jsonld) echo "JSON-LD kontekst" ;;
        schema.json)    echo "JSON Schema" ;;
        model.py)       echo "Python-klasser" ;;
        eksempel.ttl)   echo "Eksempeldata (Turtle)" ;;
        *)              echo "$1" ;;
    esac
}

# Rekkjefølgje på artefaktar i tabellen
ARTIFACT_ORDER="shapes.ttl context.jsonld schema.json ontology.ttl schema.ttl model.py eksempel.ttl"

# ---------------------------------------------------------------------------
# Steg 1: Rens tidlegare genererte domene-katalogar frå docs/
# ---------------------------------------------------------------------------
if [ ! -d "$GEN" ] || [ -z "$(ls -A "$GEN" 2>/dev/null)" ]; then
    echo "Ingen genererte artefaktar funne i $GEN. Køyr make <domain> fyrst." >&2
    exit 1
fi

for domain_dir in "$GEN"/*/; do
    [ -d "$domain_dir" ] || continue
    domain=$(basename "$domain_dir")
    rm -rf "${DOCS:?}/${domain}"
done

# ---------------------------------------------------------------------------
# Steg 2: Generer innhald per domene og skjema
# ---------------------------------------------------------------------------

# Saml domene-info for seinare nav-generering
declare -a ALL_DOMAINS=()
declare -A DOMAIN_SCHEMA_LIST=()

for domain_dir in $(find "$GEN" -mindepth 1 -maxdepth 1 -type d | sort); do
    domain=$(basename "$domain_dir")
    ALL_DOMAINS+=("$domain")
    schemas=()

    for schema_dir in $(find "$domain_dir" -mindepth 1 -maxdepth 1 -type d | sort); do
        schema=$(basename "$schema_dir")
        schemas+=("$schema")
        out="$DOCS/$domain/$schema"
        mkdir -p "$out/klasser"

        # Kopier artefaktfiler (berre filer, ikkje docs/-underkatalog)
        find "$schema_dir" -maxdepth 1 -type f -exec cp {} "$out/" \;

        # Kopier gen-doc markdown-filer til klasser/-underkatalog
        if [ -d "$schema_dir/docs" ]; then
            find "$schema_dir/docs" -name "*.md" -exec cp {} "$out/klasser/" \;
        fi

        # ----------------------------------------------------------------
        # Generer schema/index.md
        # ----------------------------------------------------------------
        {
            echo "# $schema"
            echo ""

            # Artefaktabell
            has_artifact=false
            artifact_rows=""
            for suffix in $ARTIFACT_ORDER; do
                f="$out/${schema}-${suffix}"
                if [ -f "$f" ]; then
                    has_artifact=true
                    artifact_rows+="| $(artifact_label "$suffix") | [${schema}-${suffix}](${schema}-${suffix}) |"$'\n'
                fi
            done

            if $has_artifact; then
                echo "## Artefaktar"
                echo ""
                echo "| Artefakt | Fil |"
                echo "|----------|-----|"
                printf '%s' "$artifact_rows"
            fi

            # Lenke til klasse-referansen om gen-doc vart køyrt.
            # index.md har full klasseliste; <schema>.md er berre ei minimal skjemaoversikt.
            klasse_doc=""
            [ -f "$out/klasser/index.md" ] && klasse_doc="klasser/index.md"
            [ -z "$klasse_doc" ] && [ -f "$out/klasser/${schema}.md" ] && klasse_doc="klasser/${schema}.md"
            if [ -n "$klasse_doc" ]; then
                echo ""
                echo "## Klassereferanse"
                echo ""
                echo "Sjå [klasser og eigenskapar](${klasse_doc}) for full dokumentasjon av alle klasser, eigenskapar og typar i dette skjemaet."
            fi
        } > "$out/index.md"

        echo "  $domain/$schema"
    done

    DOMAIN_SCHEMA_LIST[$domain]="${schemas[*]:-}"

    # ----------------------------------------------------------------
    # Generer domain/index.md
    # ----------------------------------------------------------------
    {
        echo "# $(domain_label "$domain")"
        echo ""
        echo "| Modell | Tilgjengelege artefaktar |"
        echo "|--------|--------------------------|"

        for schema in "${schemas[@]}"; do
            artifacts=""
            for suffix in $ARTIFACT_ORDER; do
                if [ -f "$GEN/$domain/$schema/${schema}-${suffix}" ]; then
                    [ -n "$artifacts" ] && artifacts+=" · "
                    artifacts+="$(artifact_label "$suffix")"
                fi
            done
            echo "| [${schema}](${schema}/index.md) | ${artifacts:-–} |"
        done
    } > "$DOCS/$domain/index.md"
done

# ---------------------------------------------------------------------------
# Steg 3: Generer mkdocs.yml
# ---------------------------------------------------------------------------
{
cat << 'STATIC'
site_name: LinkML W3C-profiler
site_description: Norske W3C-applikasjonsprofiler og domenemodeller i LinkML-format
site_url: https://example.org/linkml-w3c-no-profiles
docs_dir: docs

theme:
  name: material
  language: nb
  features:
    - navigation.indexes
    - navigation.top
    - content.code.copy
  palette:
    - scheme: default
      primary: indigo
      accent: indigo

markdown_extensions:
  - admonition
  - tables
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format

# gen-doc genererer interne lenkjer som ikkje alltid har tilsvarende .md-filer
# (t.d. lowercase-alias for PascalCase-klassefiler på case-insensitive filsystem).
# Desse åtvaringane er ikkje kritiske og vert undertrykka her.
validation:
  links:
    not_found: ignore
  nav:
    omitted_files: ignore

nav:
  - Heim: index.md
  - Rettleiingar:
      - Ny domenemodell: ny-domenemodell.md
STATIC

    for domain in "${ALL_DOMAINS[@]}"; do
        label=$(domain_label "$domain")
        echo "  - '${label}':"
        echo "      - ${domain}/index.md"

        schemas_str="${DOMAIN_SCHEMA_LIST[$domain]:-}"
        for schema in $schemas_str; do
            klasse_nav=""
            [ -f "$DOCS/$domain/$schema/klasser/index.md" ] && klasse_nav="${domain}/${schema}/klasser/index.md"
            [ -z "$klasse_nav" ] && [ -f "$DOCS/$domain/$schema/klasser/${schema}.md" ] && klasse_nav="${domain}/${schema}/klasser/${schema}.md"

            if [ -n "$klasse_nav" ]; then
                echo "      - '${schema}':"
                echo "          - Oversikt: ${domain}/${schema}/index.md"
                echo "          - Klasser: ${klasse_nav}"
            else
                echo "      - '${schema}': ${domain}/${schema}/index.md"
            fi
        done
    done
} > "$MKDOCS_YML"

echo ""
echo "Publisert ${#ALL_DOMAINS[@]} domene(r) til mkdocs/docs/"
echo "Oppdatert mkdocs/mkdocs.yml"
