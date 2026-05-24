#!/usr/bin/env bash
# Kopier genererte artefakter til mkdocs/docs/ og generer index-sider og mkdocs.yml.
# Køyr etter make <domain> eller make validate.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GEN="$REPO_ROOT/generated"
DOCS="$REPO_ROOT/mkdocs/docs"
MKDOCS_YML="$REPO_ROOT/mkdocs/mkdocs.yml"

SEP="************************************************************"
CLR_SEP=$(printf '\033[1;33m')
CLR_HDR=$(printf '\033[1;37m')
CLR_STEP=$(printf '\033[0;36m')
CLR_OK=$(printf '\033[0;32m')
CLR_ERR=$(printf '\033[0;31m')
CLR_RST=$(printf '\033[0m')

log_step() {
    echo "${CLR_SEP}${SEP}${CLR_RST}"
    echo "${CLR_HDR}$*${CLR_RST}"
    echo "${CLR_SEP}${SEP}${CLR_RST}"
}

# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------

domain_label() {
    case "$1" in
        ap-no)   echo "AP-NO – Applikasjonsprofiler" ;;
        begrep)  echo "Begrep – Begrepskatalogmodellar" ;;
        ngr)     echo "NGR – Nasjonale Grunndata" ;;
        fint)    echo "FINT – Fylkeskommunale integrasjonar" ;;
        samt)    echo "SAMT – Kommunale integrasjonar" ;;
        fair)    echo "FAIR – Metadataoverbygning" ;;
        oreg)    echo "OREG – Offentlege registre" ;;
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
        schema.proto)   echo "Protobuf-skjema" ;;
        erdiagram.md)   echo "ER-diagram (Mermaid)" ;;
        eksempel.ttl)   echo "Eksempeldata (Turtle)" ;;
        *)              echo "$1" ;;
    esac
}

# Rekkjefølgje på artefakter i tabellen
ARTIFACT_ORDER="shapes.ttl context.jsonld schema.json ontology.ttl schema.ttl model.py schema.proto erdiagram.md eksempel.ttl"

# ---------------------------------------------------------------------------
# Per-skjema prosessering (køyrer parallelt)
# ---------------------------------------------------------------------------
process_schema() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$GEN/$domain/$schema"
    local out="$DOCS/$domain/$schema"
    local t0
    t0=$(date +%s%3N)

    mkdir -p "$out/klasser"

    # Kopier artefaktfiler (berre filer, ikkje docs/-underkatalog)
    find "$schema_dir" -maxdepth 1 -type f -exec cp {} "$out/" \;

    # Kopier PlantUML-diagramfiler til diagrams/-underkatalog
    if [ -d "$schema_dir/diagrams" ]; then
        mkdir -p "$out/diagrams"
        find "$schema_dir/diagrams" -type f -exec cp {} "$out/diagrams/" \;
    fi

    # Kopier gen-doc markdown-filer til klasser/-underkatalog
    if [ -d "$schema_dir/docs" ]; then
        find "$schema_dir/docs" -name "*.md" -exec cp {} "$out/klasser/" \;
        # Rename alle .md-filer til lowercase (via .tmp for case-insensitive filsystem)
        for f in "$out/klasser/"*.md; do
            [ -f "$f" ] || continue
            base=$(basename "$f")
            lower=$(echo "$base" | tr '[:upper:]' '[:lower:]')
            if [ "$base" != "$lower" ]; then
                mv "$f" "$out/klasser/${lower}.tmp"
                mv "$out/klasser/${lower}.tmp" "$out/klasser/$lower"
            fi
        done
        # Oppdater alle interne .md-lenkjer til lowercase
        find "$out/klasser" -maxdepth 1 -name "*.md" \
            -exec sed -i 's/](\([^)]*\.md\))/](\L\1)/g' {} \;
    fi

    # ----------------------------------------------------------------
    # Generer schema/index.md
    # ----------------------------------------------------------------
    {
        echo "# $schema"
        echo ""

        # Embed oversiktsdiagram frå gen-erdiagram
        erdiagram_file="$out/${schema}-erdiagram.md"
        if [ -f "$erdiagram_file" ]; then
            awk 'NR==1 && /^# / { next } 1' "$erdiagram_file"
        fi

        # Inline klasseliste frå gen-doc direkte i index.md
        klasse_src=""
        [ -f "$out/klasser/index.md" ] && klasse_src="$out/klasser/index.md"
        [ -z "$klasse_src" ] && [ -f "$out/klasser/${schema}.md" ] && klasse_src="$out/klasser/${schema}.md"

        if [ -n "$klasse_src" ]; then
            echo ""
            awk 'NR==1 && /^# / { next } 1' "$klasse_src" \
                | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g'
        fi

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

        # PlantUML-diagram (ligg i diagrams/-underkatalog)
        puml_svg="$out/diagrams/${schema}.svg"
        puml_src="$out/diagrams/${schema}.puml"
        if [ -f "$puml_svg" ] || [ -f "$puml_src" ]; then
            has_artifact=true
            puml_links=""
            [ -f "$puml_svg" ] && puml_links="[${schema}.svg](diagrams/${schema}.svg)"
            if [ -f "$puml_src" ]; then
                [ -n "$puml_links" ] && puml_links+=" · "
                puml_links+="[${schema}.puml](diagrams/${schema}.puml)"
            fi
            artifact_rows+="| PlantUML-diagram | ${puml_links} |"$'\n'
        fi

        if $has_artifact; then
            echo ""
            echo ""
            echo "## Generated artifacts"
            echo ""
            echo "| Artefakt | Fil |"
            echo "|----------|-----|"
            printf '%s' "$artifact_rows"
        fi
    } > "$out/index.md"

    local elapsed_ms=$(( $(date +%s%3N) - t0 ))
    printf "${CLR_STEP}  → %s/%s${CLR_RST} (%d.%ds)\n" \
        "$domain" "$schema" \
        $((elapsed_ms / 1000)) \
        $((elapsed_ms % 1000 / 100))
}

# ---------------------------------------------------------------------------
# Steg 1: Rens tidlegare genererte domene-katalogar frå docs/
# ---------------------------------------------------------------------------
log_step "Steg 1: Rens tidlegare genererte domene-katalogar frå docs/"

if [ ! -d "$GEN" ] || [ -z "$(ls -A "$GEN" 2>/dev/null)" ]; then
    echo "Ingen genererte artefakter funne i $GEN. Køyr make <domain> fyrst." >&2
    exit 1
fi

for domain_dir in "$GEN"/*/; do
    [ -d "$domain_dir" ] || continue
    domain=$(basename "$domain_dir")
    find "${DOCS}/${domain}" -mindepth 1 -depth -delete 2>/dev/null || true
    rmdir "${DOCS}/${domain}" 2>/dev/null || true
done

# ---------------------------------------------------------------------------
# Steg 2: Generer innhald per domene og skjema (parallelt)
# ---------------------------------------------------------------------------
log_step "Steg 2: Generer innhald per domene og skjema (parallelt)"

declare -a ALL_DOMAINS=()
declare -A DOMAIN_SCHEMA_LIST=()

# Samle domene/skjema-struktur sekvensielt (rask); hopp over tomme domene-katalogar
for domain_dir in $(find "$GEN" -mindepth 1 -maxdepth 1 -type d | sort); do
    domain=$(basename "$domain_dir")
    schemas=()
    for schema_dir in $(find "$domain_dir" -mindepth 1 -maxdepth 1 -type d | sort); do
        schemas+=("$(basename "$schema_dir")")
    done
    [ "${#schemas[@]}" -eq 0 ] && continue
    ALL_DOMAINS+=("$domain")
    DOMAIN_SCHEMA_LIST[$domain]="${schemas[*]:-}"
done

# Start alle skjemajobbar parallelt
declare -a PIDS=()
declare -a KEYS=()
for domain in "${ALL_DOMAINS[@]}"; do
    for schema in ${DOMAIN_SCHEMA_LIST[$domain]:-}; do
        process_schema "$domain" "$schema" &
        PIDS+=($!)
        KEYS+=("$domain/$schema")
    done
done

# Vent på alle jobbar og rapporter feil
failed=0
for i in "${!PIDS[@]}"; do
    if ! wait "${PIDS[$i]}"; then
        echo "${CLR_ERR}FEIL: ${KEYS[$i]}${CLR_RST}" >&2
        failed=$((failed + 1))
    fi
done
[ "$failed" -gt 0 ] && exit 1

# Generer domain/index.md sekvensielt (avheng av at alle skjema er ferdige)
for domain in "${ALL_DOMAINS[@]}"; do
    {
        echo "# $(domain_label "$domain")"
        echo ""
        echo "| Modell | Tilgjengelege artefakter |"
        echo "|--------|--------------------------|"

        for schema in ${DOMAIN_SCHEMA_LIST[$domain]:-}; do
            artifacts=""
            for suffix in $ARTIFACT_ORDER; do
                if [ -f "$GEN/$domain/$schema/${schema}-${suffix}" ]; then
                    [ -n "$artifacts" ] && artifacts+=" · "
                    artifacts+="$(artifact_label "$suffix")"
                fi
            done
            if [ -f "$GEN/$domain/$schema/diagrams/${schema}.svg" ] || [ -f "$GEN/$domain/$schema/diagrams/${schema}.puml" ]; then
                [ -n "$artifacts" ] && artifacts+=" · "
                artifacts+="PlantUML-diagram"
            fi
            echo "| [${schema}](${schema}/index.md) | ${artifacts:-–} |"
        done
    } > "$DOCS/$domain/index.md"
done

# ---------------------------------------------------------------------------
# Steg 3: Generer index.md frå README.md
# ---------------------------------------------------------------------------
log_step "Steg 3: Generer index.md frå README.md"

sed \
  -e '/Sjå.*CLAUDE\.md.*COMMANDS\.md/d' \
  -e 's/\[\([^]]*\)\](src\/[^)]*)/\1/g' \
  "$REPO_ROOT/README.md" > "$DOCS/index.md"

# ---------------------------------------------------------------------------
# Steg 4: Generer mkdocs.yml
# ---------------------------------------------------------------------------
log_step "Steg 4: Generer mkdocs.yml"

{
cat << 'STATIC'
site_name:  Norske W3C-profiler og offentlige domenemodeller i LinkML-format
site_description: Norske W3C-applikasjonsprofiler og offentlige domenemodeller i LinkML-format
site_url: https://brreg.github.io/linkml-datamodellering-no
docs_dir: docs

theme:
  name: material
  language: nb
  features:
    - navigation.indexes
    - navigation.top
    - content.code.copy
    - navigation.instant
  palette:
    - scheme: default
      primary: indigo
      accent: indigo

plugins:
  - search
  - build-cache

extra_css:
  - stylesheets/aktivt-menypunkt.css

extra_javascript:
  - javascripts/nav-active-fix.js

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
      - Ny begrepskatalog: ny-begrepsmodell.md
      - Generatorkonfigurasjon: generate-config.md
STATIC

    for domain in "${ALL_DOMAINS[@]}"; do
        label=$(domain_label "$domain")
        echo "  - '${label}':"
        echo "      - ${domain}/index.md"

        schemas_str="${DOMAIN_SCHEMA_LIST[$domain]:-}"
        for schema in $schemas_str; do
            echo "      - '${schema}': ${domain}/${schema}/index.md"
        done
    done
} > "$MKDOCS_YML"

echo ""
echo "${CLR_OK}Publisert ${#ALL_DOMAINS[@]} domene(r) til mkdocs/docs/${CLR_RST}"
echo "${CLR_OK}Oppdatert mkdocs/mkdocs.yml${CLR_RST}"
