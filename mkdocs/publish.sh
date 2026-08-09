#!/usr/bin/env bash
# Kopier genererte artefakter til mkdocs/docs/ og generer index-sider og mkdocs.yml.
# Køyr etter make <domain> eller make validate.
set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

: "${LOG_FUNCTIONS:?miljøvariabelen LOG_FUNCTIONS må vere sett (eksportert frå make/00-settings.mk)}"
eval "$LOG_FUNCTIONS"

export REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GEN="$REPO_ROOT/generated"
DOCS="$REPO_ROOT/mkdocs/docs"
MKDOCS_YML="$REPO_ROOT/mkdocs/mkdocs.yml"

# log_step — banner/deloverskrift, alltid synleg (uavhengig av LOGLVL),
# same kontrakt som print_header i make/03-output.mk. SEP/CLR_*-variablane
# er arva frå miljøet (eksportert av make/00-settings.mk), ikkje
# redeklarerte lokalt.
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
    local output="$DOCS/arkitektur/valideringsregler.md"
    local github_base="https://github.com/brreg/linkml-datamodellering-no/blob/main"

    log_info "${CLR_STEP}→ Genererer valideringsregler.md frå policies/README.md${CLR_RST}"

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

    log_info "${CLR_OK}✓ Genererte $output${CLR_RST}"
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
    log_info "$(printf "${CLR_STEP}  → %s/%s${CLR_RST} (%d.%ds)" \
        "$domain" "$schema" \
        $((elapsed_ms / 1000)) \
        $((elapsed_ms % 1000 / 100)))"
}

# ---------------------------------------------------------------------------
# Steg 1: Rens tidlegare genererte domene-katalogar frå docs/
# ---------------------------------------------------------------------------
log_step "Steg 1: Rens tidlegare genererte domene-katalogar frå docs/"
t1=$(date +%s%3N)

if [ ! -d "$GEN" ] || [ -z "$(ls -A "$GEN" 2>/dev/null)" ]; then
    log_error "Ingen genererte artefakter funne i $GEN. Køyr make <domain> fyrst."
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
        log_info "${CLR_WARN}ÅTVARING: $domain finst i generated/ men ikkje i src/linkml/ — stale artefakter frå omdøypt domene?${CLR_RST}"
    fi
    find "${DOCS}/${domain}" -mindepth 1 -depth -delete 2>/dev/null || true
    rmdir "${DOCS}/${domain}" 2>/dev/null || true
done

# Slett mkdocs/docs/$domain/ for domene som ikkje lenger finst i generated/
for docs_domain_dir in "$DOCS"/*/; do
    [ -d "$docs_domain_dir" ] || continue
    domain=$(basename "$docs_domain_dir")
    case "$domain" in
        stylesheets|javascripts|kom-i-gang|arkitektur|publisering|automasjon) continue ;;
    esac
    if [ ! -d "$GEN/$domain" ]; then
        log_info "Ryddar forsvunne domene: $domain"
        rm -rf "$docs_domain_dir"
    fi
done

elapsed1_ms=$(( $(date +%s%3N) - t1 ))
log_info "$(printf "${CLR_OK}✓ Steg 1 ferdig${CLR_RST} (%d.%ds)" \
    $((elapsed1_ms / 1000)) \
    $((elapsed1_ms % 1000 / 100)))"

# Generer byggetidspunkt (ISO 8601 UTC)
BUILD_TIMESTAMP=$(TZ="Europe/Oslo" date +"%Y-%m-%d %H:%M %Z")

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
    if ! submodels=$(python3 -c "import yaml, sys; d=yaml.safe_load(open('$manifest_file')); print(','.join(d.get('submodels', [])))" 2>&1); then
        echo "ÅTVARING: kunne ikkje lese submodels frå $manifest_file — hoppar over ($submodels)" >&2
        submodels=""
    fi

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

# Globalt oppslag skjemanamn → domene og → filsti, bygd éin gong for heile
# repoet. Erstattar gjentekne whole-tree `find "$REPO_ROOT/src/linkml" -name
# "<namn>-schema.yaml"`-kall i classes.sh/avhengigheiter.sh (kvart slikt
# find-kall er dyrt på NTFS-monterte /mnt/c-filsystem under WSL2 — sjå
# specs/backlog/batch-docs-publish-generering.md for profilering).
# Filstien vert lagra direkte (ikkje rekonstruert frå katalogkonvensjonen)
# fordi delmodell-skjema (t.d. dqv-core-schema.yaml) ligg i FORELDREskjemaet
# sin katalog (dqv-ap-no/), ikkje i ein katalog oppkalla etter seg sjølv.
declare -A SCHEMA_NAME_TO_DOMAIN_TMP=()
declare -A SCHEMA_NAME_TO_PATH_TMP=()
for schema_yaml in $(find "$REPO_ROOT/src/linkml" -name '*-schema.yaml'); do
    schema_name=$(basename "$schema_yaml" .yaml)
    domain=$(basename "$(dirname "$(dirname "$schema_yaml")")")
    SCHEMA_NAME_TO_DOMAIN_TMP["$schema_name"]="$domain"
    SCHEMA_NAME_TO_PATH_TMP["$schema_name"]="$schema_yaml"
done

export SCHEMA_NAME_TO_DOMAIN_SERIALIZED=""
for key in "${!SCHEMA_NAME_TO_DOMAIN_TMP[@]}"; do
    SCHEMA_NAME_TO_DOMAIN_SERIALIZED+="$key=${SCHEMA_NAME_TO_DOMAIN_TMP[$key]} "
done

export SCHEMA_NAME_TO_PATH_SERIALIZED=""
for key in "${!SCHEMA_NAME_TO_PATH_TMP[@]}"; do
    SCHEMA_NAME_TO_PATH_SERIALIZED+="$key=${SCHEMA_NAME_TO_PATH_TMP[$key]} "
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
t2=$(date +%s%3N)

declare -a ALL_DOMAINS=()
declare -A DOMAIN_SCHEMA_LIST=()

# Hardkoda rekkefølgje på domene i nav-menyen
DOMAIN_ORDER=("referanse" "ap-no" "fair" "ngr" "oreg" "fint" "samt" "begrepskatalog" "modellkatalog")

# Samle domene/skjema-struktur frå generated/ — bygg opp DOMAIN_SCHEMA_LIST for alle domene
declare -A DOMAIN_EXISTS=()
for domain_dir in $(find "$GEN" -mindepth 1 -maxdepth 1 -type d); do
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
    DOMAIN_EXISTS[$domain]=1
    DOMAIN_SCHEMA_LIST[$domain]="${schemas[*]:-}"
done

# Bygg ALL_DOMAINS i hardkoda rekkefølgje, deretter alfabetisk for resten
for domain in "${DOMAIN_ORDER[@]}"; do
    if [ "${DOMAIN_EXISTS[$domain]:-0}" = "1" ]; then
        ALL_DOMAINS+=("$domain")
        unset DOMAIN_EXISTS[$domain]
    fi
done

# Legg til resterande domene (ikkje i DOMAIN_ORDER) i alfabetisk rekkefølgje
for domain in $(printf '%s\n' "${!DOMAIN_EXISTS[@]}" | sort); do
    ALL_DOMAINS+=("$domain")
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
failed_jobs=()
for i in "${!PIDS[@]}"; do
    if ! wait "${PIDS[$i]}"; then
        domain_schema="${KEYS[$i]}"
        domain="${domain_schema%/*}"
        schema="${domain_schema#*/}"

        log_error "$domain/$schema (Domain: $domain, Schema: $schema, Output: $DOCS/$domain/$schema/)"

        failed_jobs+=("$domain/$schema")
    fi
done

if [ ${#failed_jobs[@]} -gt 0 ]; then
    failed_list=$(printf '  - %s\n' "${failed_jobs[@]}")
    log_error "OPPSUMMERING: ${#failed_jobs[@]} skjema feila:
${failed_list}"
    exit 1
fi

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
        generate_domain_description "$domain"
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

elapsed2_ms=$(( $(date +%s%3N) - t2 ))
log_info "$(printf "${CLR_OK}✓ Steg 2 ferdig${CLR_RST} (%d.%ds)" \
    $((elapsed2_ms / 1000)) \
    $((elapsed2_ms % 1000 / 100)))"

# ---------------------------------------------------------------------------
# Steg 3: Generer index.md frå README.md
# ---------------------------------------------------------------------------
log_step "Steg 3: Generer index.md frå README.md"
t3=$(date +%s%3N)

cp "$REPO_ROOT/README.md" "$DOCS/index.md"

# Legg til footer med byggetidspunkt
cat >> "$DOCS/index.md" <<EOF

---

_Portalen vart sist bygd: ${BUILD_TIMESTAMP}_
EOF

# ---------------------------------------------------------------------------
# Steg 3: Generer valideringsregler.md
# ---------------------------------------------------------------------------
log_step "Steg 3: Generer valideringsregler.md"
generate_validation_docs

elapsed3_ms=$(( $(date +%s%3N) - t3 ))
log_info "$(printf "${CLR_OK}✓ Steg 3 ferdig${CLR_RST} (%d.%ds)" \
    $((elapsed3_ms / 1000)) \
    $((elapsed3_ms % 1000 / 100)))"

# ---------------------------------------------------------------------------
# Steg 4: Generer mkdocs.yml
# ---------------------------------------------------------------------------
log_step "Steg 4: Generer mkdocs.yml"
t4=$(date +%s%3N)

{
cat << 'STATIC'
site_name:  Norske W3C-profiler og offentlige domenemodellar i LinkML-format
site_description: Norske W3C-applikasjonsprofilar og offentlige domenemodellar i LinkML-format
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
    - toc.follow
  palette:
    - scheme: default
      primary: indigo
      accent: indigo

plugins:
  - search

extra_css:
  - stylesheets/brreg-theme.css              # Brønnøysund designsystem-tema (NPM-pakke, kombinert)
  - stylesheets/brreg-material-overrides.css # Material-overrides
  - stylesheets/responsivt-design.css

markdown_extensions:
  - admonition
  - tables
  - attr_list
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
# (t.d. lowercase-alias for PascalCase-klassefiler på case-insensitive filsystem),
# og systematiske fragment-lenkjer utan filnamn (t.d. ../../ap-no/dcat-ap-no/#classes
# i staden for .../index.md#classes) som mkdocs ikkje kjenner att som interne lenkjer.
# Desse åtvaringane er ikkje kritiske og vert undertrykka her.
validation:
  links:
    not_found: ignore
    unrecognized_links: ignore
  nav:
    omitted_files: ignore

nav:
  - Rettleiingar:
      - index.md
      - Kom i gang:
          - kom-i-gang/index.md
          - Bli modelleigar: kom-i-gang/ny-org.md
          - Ny domenemodell: kom-i-gang/ny-domenemodell.md
          - Ny begrepskatalog: kom-i-gang/ny-begrepsmodell.md
          - Byggmanifest: kom-i-gang/build-config.md
          - Kommandooversikt: kom-i-gang/kommandoar.md
      - Arkitektur:
          - arkitektur/index.md
          - Arkitekturoversikt: arkitektur/arkitektur-oversikt.md
          - Importhierarki: arkitektur/importhierarki.md
          - Valideringsreglar: arkitektur/valideringsregler.md
          - AP-NO arkitektur og avvik: arkitektur/ap-no-arkitektur.md
          - Bruk frå eksternt repo: arkitektur/ekstern-bruk.md
      - Publisering:
          - publisering/index.md
          - Publiseringsflyt: publisering/publisering-oversikt.md
          - Publiser til Felles Begrepskatalog: publisering/publisering-begrep.md
          - Publiser til Felles Datakatalog: publisering/publisering-modell.md
      - Automasjon:
          - automasjon/index.md
          - Artefaktgenerering — kjelder og pipeline: automasjon/artefakt-generering.md
          - Generering av modell-dokumentasjon: automasjon/index-md-struktur.md
          - Generering av modellmanifest: automasjon/modellmanifest-generering.md
          - README-tabellgenerering: automasjon/readme-tabellgenerering.md
          - Monitorering av automasjon: automasjon/monitorering.md
      - Om dette repoet: om.md
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

elapsed4_ms=$(( $(date +%s%3N) - t4 ))
log_info "$(printf "${CLR_OK}✓ Steg 4 ferdig${CLR_RST} (%d.%ds)" \
    $((elapsed4_ms / 1000)) \
    $((elapsed4_ms % 1000 / 100)))"

log_info "${CLR_OK}Publisert ${#ALL_DOMAINS[@]} domene(r) til mkdocs/docs/${CLR_RST}"
log_info "${CLR_OK}Oppdatert mkdocs/mkdocs.yml${CLR_RST}"
