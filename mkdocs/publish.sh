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
# Source lib-filer (refactored modulær struktur)
# ---------------------------------------------------------------------------
LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/lib" && pwd)"
source "$LIB_DIR/copy_artifacts.sh"
source "$LIB_DIR/generate_index.sh"
source "$LIB_DIR/utils/formatters.sh"
source "$LIB_DIR/utils/metadata_parsers.sh"

# Rekkjefølgje på artefakter i tabellen (brukt både i artifacts.sh og domain/index.md-generering)
ARTIFACT_ORDER="shapes.ttl context.jsonld schema.json schema.xsd openapi.yaml asyncapi.yaml ontology.ttl schema.ttl model.py schema.proto erdiagram.md eksempel.ttl"

# ---------------------------------------------------------------------------
# Hjelpefunksjonar (legacy — flytta til lib/)
# ---------------------------------------------------------------------------

# DEPRECATED: get_contact_info() er flytta til lib/sections/contact.sh
# Behald stub for bakoverkompatibilitet med eksisterande kode
get_contact_info() {
    schema_path="$1"

    # Les CODEOWNERS.md for å finne eigar-org basert på path pattern
    codeowners_file="$REPO_ROOT/CODEOWNERS.md"
    if [ ! -f "$codeowners_file" ]; then
        echo "**Support:** [GitHub Issues](https://github.com/brreg/linkml-datamodellering-no/issues)"
        return
    fi

    # Ekstraher YAML-frontmatter frå CODEOWNERS.md
    # Parse YAML og match path mot path_patterns for kvar org
    org_data=$(python3 - "$schema_path" "$codeowners_file" <<'PYEOF'
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
        name=$(echo "$org_data" | grep '^name:' | sed 's/^name: //')
        org_uri=$(echo "$org_data" | grep '^org_uri:' | sed 's/^org_uri: //')
        contact_uri=$(echo "$org_data" | grep '^contact_uri:' | sed 's/^contact_uri: //')

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
}

# DEPRECATED: domain_label() og artifact_label() er flytta til lib/utils/formatters.sh
# DEPRECATED: ARTIFACT_ORDER er flytta til lib/sections/artifacts.sh

# ---------------------------------------------------------------------------
# Generer valideringsregler.md frå policies/README.md
# ---------------------------------------------------------------------------
generate_validation_docs() {
    local policies_readme="$REPO_ROOT/src/mcp-linkml-validator/policies/README.md"
    local output="$DOCS/valideringsregler.md"
    local github_base="https://github.com/brreg/linkml-datamodellering-no/blob/main"

    echo "${CLR_STEP}→ Genererer valideringsregler.md frå policies/README.md${CLR_RST}"

    {
        cat <<'EOF'
# Valideringsregler

!!! note "Beskrivelse"

     Denne sida er generert automatisk frå validator-dokumentasjonen i `src/mcp-linkml-validator/policies/`. Sjå [GitHub-repoet](https://github.com/brreg/linkml-datamodellering-no/tree/main/src/mcp-linkml-validator) for siste versjon.

---

EOF
        cat "$policies_readme" | \
            sed -E "s|\]\(([^)]+\.yaml)\)|]($github_base/src/mcp-linkml-validator/policies/\1)|g" | \
            sed -E "s|specs/done/([^)]+)|$github_base/specs/done/\1|g"
    } > "$output"

    echo "${CLR_OK}✓ Genererte $output${CLR_RST}"
}

# DEPRECATED: build_dependency_graph() er flytta til lib/sections/dependencies.sh

# ---------------------------------------------------------------------------
# Per-skjema prosessering (køyrer parallelt) — REFACTORED
# ---------------------------------------------------------------------------
process_schema() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$GEN/$domain/$schema"
    local out="$DOCS/$domain/$schema"
    local t0
    t0=$(date +%s%3N)

    # Steg 2a: Kopier artefakter
    copy_schema_artifacts "$domain" "$schema" "$schema_dir" "$out"

    # Steg 2b: Deserialisér delmodell-map frå miljøvariablar og generer index.md
    local parent_model=""
    local submodels=""

    for entry in $SCHEMA_PARENT_MODEL_SERIALIZED; do
        key="${entry%%=*}"
        val="${entry#*=}"
        [ "$key" = "$schema" ] && parent_model="$val" && break
    done

    for entry in $SCHEMA_SUBMODELS_SERIALIZED; do
        key="${entry%%=*}"
        val="${entry#*=}"
        if [ "$key" = "$schema" ]; then
            # val er komma-separert — konverter til mellomrom-separert for SUBMODELS
            submodels="${val//,/ }"
            break
        fi
    done

    export PARENT_MODEL="$parent_model"
    export SUBMODELS="$submodels"
    generate_schema_index "$domain" "$schema" "$schema_dir" "$out"
    unset PARENT_MODEL SUBMODELS

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
    # Hopp over tomme domene-katalogar (ingen skjema-underkatalogar)
    schema_count=$(find "$domain_dir" -mindepth 1 -maxdepth 1 -type d | wc -l)
    [ "$schema_count" -eq 0 ] && continue
    domain=$(basename "$domain_dir")
    # Åtvar om domenet finst i generated/ men ikkje i src/linkml/ (stale artefakter)
    if [ ! -d "$REPO_ROOT/src/linkml/$domain" ]; then
        echo "${CLR_ERR}ÅTVARING: $domain finst i generated/ men ikkje i src/linkml/ — stale artefakter frå omdøypt domene?${CLR_RST}" >&2
    fi
    find "${DOCS}/${domain}" -mindepth 1 -depth -delete 2>/dev/null || true
    rmdir "${DOCS}/${domain}" 2>/dev/null || true
done

# Slett mkdocs/docs/$domain/ for domene som ikkje lenger finst i generated/
for docs_domain_dir in "$DOCS"/*/; do
    [ -d "$docs_domain_dir" ] || continue
    domain=$(basename "$docs_domain_dir")
    case "$domain" in
        stylesheets|javascripts) continue ;;
    esac
    if [ ! -d "$GEN/$domain" ]; then
        echo "Ryddar forsvunne domene: $domain"
        rm -rf "$docs_domain_dir"
    fi
done

# ---------------------------------------------------------------------------
# Steg 1.5: Bygg delmodell-map frå manifest-filer
# ---------------------------------------------------------------------------
# Bruk assosiative arrays som må eksporterast manuelt til subshells
declare -A SCHEMA_PARENT_MODEL_TMP=()
declare -A SCHEMA_SUBMODELS_TMP=()

for manifest_file in $(find "$REPO_ROOT/src/linkml" -name build.yaml); do
    # Ekstraher domene og katalog frå manifest-stien
    # manifest_file = /path/src/linkml/<domain>/<schema>/build.yaml
    schema_dir=$(dirname "$manifest_file")
    schema=$(basename "$schema_dir")
    domain=$(basename "$(dirname "$schema_dir")")

    # Les submodels-lista frå manifest (bruk komma som skiljetegn for å unngå konflikt med mellomrom i serialisering)
    submodels=$(python3 -c "import yaml, sys; d=yaml.safe_load(open('$manifest_file')); print(','.join(d.get('submodels', [])))" 2>/dev/null || echo "")

    if [ -n "$submodels" ]; then
        SCHEMA_SUBMODELS_TMP["$schema"]="$submodels"

        # Bygg parent-map for kvar delmodell (submodels er komma-separert)
        IFS=',' read -ra sub_array <<< "$submodels"
        for sub in "${sub_array[@]}"; do
            SCHEMA_PARENT_MODEL_TMP["$sub"]="$schema"
        done
    fi
done

# Serialiser map til miljøvariablar for eksport til subshells
export SCHEMA_PARENT_MODEL_SERIALIZED=""
for key in "${!SCHEMA_PARENT_MODEL_TMP[@]}"; do
    SCHEMA_PARENT_MODEL_SERIALIZED+="$key=${SCHEMA_PARENT_MODEL_TMP[$key]} "
done

export SCHEMA_SUBMODELS_SERIALIZED=""
for key in "${!SCHEMA_SUBMODELS_TMP[@]}"; do
    SCHEMA_SUBMODELS_SERIALIZED+="$key=${SCHEMA_SUBMODELS_TMP[$key]} "
done

# Bygg lokale map for bruk i hovudshell (nav-generering)
declare -A SCHEMA_PARENT_MODEL=()
declare -A SCHEMA_SUBMODELS=()
for entry in $SCHEMA_PARENT_MODEL_SERIALIZED; do
    key="${entry%%=*}"
    val="${entry#*=}"
    SCHEMA_PARENT_MODEL["$key"]="$val"
done
for entry in $SCHEMA_SUBMODELS_SERIALIZED; do
    key="${entry%%=*}"
    val="${entry#*=}"
    # Behald komma-separering i SCHEMA_SUBMODELS-map
    SCHEMA_SUBMODELS["$key"]="$val"
done

# ---------------------------------------------------------------------------
# Steg 2: Generer innhald per domene og skjema (parallelt)
# ---------------------------------------------------------------------------
log_step "Steg 2: Generer innhald per domene og skjema (parallelt)"

declare -a ALL_DOMAINS=()
declare -A DOMAIN_SCHEMA_LIST=()

# Samle domene/skjema-struktur sekvensielt (rask); hopp over tomme domene-katalogar og dublett-schema-katalogar
for domain_dir in $(find "$GEN" -mindepth 1 -maxdepth 1 -type d | sort); do
    domain=$(basename "$domain_dir")
    schemas=()
    for schema_dir in $(find "$domain_dir" -mindepth 1 -maxdepth 1 -type d | sort); do
        schema=$(basename "$schema_dir")

        # Hopp over *-schema-katalogar dersom tilsvarande katalog utan -schema finst
        # (indikerer dublett: både data og schema generert frå same kjeldekatalog)
        if [[ "$schema" == *-schema ]]; then
            base_schema="${schema%-schema}"
            if [ -d "$domain_dir/$base_schema" ]; then
                continue
            fi
        fi

        schemas+=("$schema")
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
    # Sjekk om noko skjema i domenet har eit publisert URI-register
    domain_has_published=false
    for schema in ${DOMAIN_SCHEMA_LIST[$domain]:-}; do
        [ -f "$REPO_ROOT/src/linkml/$domain/$schema/published-uris.lock" ] && domain_has_published=true && break
    done

    {
        echo "# $(domain_label "$domain")"
        echo ""
        if $domain_has_published; then
            echo "| Modell | Tilgjengelege artefakter | Publisert til |"
            echo "|--------|--------------------------|---------------|"
        else
            echo "| Modell | Tilgjengelege artefakter |"
            echo "|--------|--------------------------|"
        fi

        for schema in ${DOMAIN_SCHEMA_LIST[$domain]:-}; do
            artifacts=""
            for suffix in $ARTIFACT_ORDER; do
                if [ -f "$GEN/$domain/$schema/${schema}-${suffix}" ]; then
                    [ -n "$artifacts" ] && artifacts+=" · "
                    artifacts+="$(artifact_label "$suffix")"
                fi
            done
            if [ -f "$GEN/$domain/$schema/diagrams/${schema}-filtered.svg" ] || [ -f "$GEN/$domain/$schema/diagrams/${schema}-filtered.puml" ] || \
               [ -f "$GEN/$domain/$schema/diagrams/${schema}.svg" ] || [ -f "$GEN/$domain/$schema/diagrams/${schema}.puml" ]; then
                [ -n "$artifacts" ] && artifacts+=" · "
                artifacts+="PlantUML-diagram"
            fi
            if $domain_has_published; then
                published_col=""
                [ -f "$REPO_ROOT/src/linkml/$domain/$schema/published-uris.lock" ] && \
                    published_col="[Felles Begrepskatalog](https://data.norge.no/concepts)"
                echo "| [${schema}](${schema}/index.md) | ${artifacts:--} | ${published_col} |"
            else
                echo "| [${schema}](${schema}/index.md) | ${artifacts:--} |"
            fi
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
# Steg 3: Generer valideringsregler.md
# ---------------------------------------------------------------------------
log_step "Steg 3: Generer valideringsregler.md"
generate_validation_docs

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
copyright: >
  Repoet er lisensiert under <a href="https://github.com/brreg/linkml-datamodellering-no/blob/main/LICENSE">MIT-lisens</a>.
  Dei enkelte modellane har egne lisensar — sjå <code>license:</code>-feltet i det einskilde skjemaet.

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
  - stylesheets/responsivt-design.css

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
  - Rettleiingar:
      - index.md
      - Bli modelleigar: ny-org.md
      - Ny domenemodell: ny-domenemodell.md
      - Ny begrepskatalog: ny-begrepsmodell.md
      - Modellmanifest: manifest-config.md
      - Importhierarki: importhierarki.md
      - Valideringsreglar: valideringsregler.md
      - AP-NO arkitektur og avvik: ap-no-arkitektur.md
      - Bruk frå eksternt repo: ekstern-bruk.md
      - Publiser til Felles Begrepskatalog: publisering-begrep.md
      - Publiser til Felles Datakatalog: publisering-modell.md
      - Publiseringsflyt: arkitektur-oversikt.md
      - Struktur for modell-dokumentasjon: index-md-struktur.md
      - Monitorering av automasjon: monitorering.md
      - Om: om.md
STATIC

    for domain in "${ALL_DOMAINS[@]}"; do
        label=$(domain_label "$domain")
        echo "  - '${label}':"
        echo "      - ${domain}/index.md"

        schemas_str="${DOMAIN_SCHEMA_LIST[$domain]:-}"
        for schema in $schemas_str; do
            # Hopp over delmodellar — dei vert lagt til under hovudmodellen
            [ -n "${SCHEMA_PARENT_MODEL[$schema]:-}" ] && continue

            echo "      - '${schema}': ${domain}/${schema}/index.md"

            # Legg til delmodellar innrykka under hovudmodell (submodels er komma-separert)
            submodels="${SCHEMA_SUBMODELS[$schema]:-}"
            if [ -n "$submodels" ]; then
                IFS=',' read -ra sub_array <<< "$submodels"
                for sub in "${sub_array[@]}"; do
                    echo "      - '${sub}': ${domain}/${sub}/index.md"
                done
            fi
        done
    done
} > "$MKDOCS_YML"

echo ""
echo "${CLR_OK}Publisert ${#ALL_DOMAINS[@]} domene(r) til mkdocs/docs/${CLR_RST}"
echo "${CLR_OK}Oppdatert mkdocs/mkdocs.yml${CLR_RST}"
