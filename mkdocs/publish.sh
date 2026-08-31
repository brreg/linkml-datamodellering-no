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
source "$LIB_DIR/utils/python_container.sh"
source "$LIB_DIR/utils/imported_schemas.sh"
source "$LIB_DIR/copy_artifacts.sh"
source "$LIB_DIR/generate_index.sh"
source "$LIB_DIR/utils/formatters.sh"
source "$LIB_DIR/utils/metadata_parsers.sh"

# Rekkjefølgje på artefakter i tabellen (brukt både i artifacts.sh og domain/index.md-generering)
ARTIFACT_ORDER="shapes.ttl context.jsonld schema.json schema.xsd openapi.yaml asyncapi.yaml ontology.ttl schema.ttl model.py schema.proto schema.graphql erdiagram.md eksempel.ttl"

# ---------------------------------------------------------------------------
# Hjelpefunksjonar (legacy — flytta til lib/)
# ---------------------------------------------------------------------------

# DEPRECATED: domain_label() og artifact_label() er flytta til lib/utils/formatters.sh
# DEPRECATED: ARTIFACT_ORDER er flytta til lib/sections/artifacts.sh

# ---------------------------------------------------------------------------
# Generer valideringsregler.md frå policies/README.md
# ---------------------------------------------------------------------------
generate_validation_docs() {
    local policies_readme="$REPO_ROOT/src/mcp-linkml-validator/policies/README.md"
    local output="$DOCS/arkitektur/valideringsregler.md"
    local github_base="https://github.com/brreg/linkml-datamodellering-no/blob/main"

    # Ingen eigen før/etter-logging her — kalt via timed_run(), som alt
    # loggar navn+tid ved suksess og navn+tid+kommando ved feil. Sjå
    # specs/backlog/flytt-steg3-til-steg1-med-timing.md.
    log_debug "→ Genererer $output frå $policies_readme"

    {
        cat <<'EOF'
# Valideringsreglar

!!! note "Beskrivelse"

     Valideringsreglar består av policyer som du kan velge å etterleve og maskinelt validere etterlevelsen av. Alle må som minimum etterleve bronze policyen.
     
     Denne sida er generert automatisk frå validator-dokumentasjonen i `src/mcp-linkml-validator/policies/`. Sjå [GitHub-repoet](https://github.com/brreg/linkml-datamodellering-no/tree/main/src/mcp-linkml-validator) for siste versjon.

---

EOF
        cat "$policies_readme" | \
            sed -E "s|\]\(([^)]+\.yaml)\)|]($github_base/src/mcp-linkml-validator/policies/\1)|g" | \
            sed -E "s|specs/done/([^)]+)|$github_base/specs/done/\1|g" | \
            sed -E "s|\.\./\.\./\.\./([A-Z][A-Za-z-]*\.md)|$github_base/\1|g"
    } > "$output"
}

# ---------------------------------------------------------------------------
# Generer modellanalyse/-sider frå dei tre --scope all-rapportane
# (similar-classes/-slots/-types-all), køyrde éin gong per generate.yml-
# køyring (sjå .github/workflows/generate.yml, steget "Køyr modellanalyse
# på tvers av domene"). Gjer at kvart skjema sin per-objekttype-fotnote
# under ## Modellanalyse (generate-modellanalyse-md.py) kan lenke til ei
# ekte, stabil side i staden for GitHub Actions-workflowen — sjå
# specs/backlog/modellanalyse-ubrukte-lokale-definisjonar.md.
# ---------------------------------------------------------------------------
generate_cross_domain_modellanalyse_docs() {
    local src_dir="$GEN/modell-analyse-tvers-domene"
    local out_dir="$DOCS/modellanalyse"
    mkdir -p "$out_dir"

    local -A files=(
        [similar-classes-all-report.md]="liknande-klassenavn-alle-domene.md"
        [similar-slots-all-report.md]="liknande-slotnavn-alle-domene.md"
        [similar-types-all-report.md]="liknande-typenavn-alle-domene.md"
    )

    local src_name dest
    for src_name in "${!files[@]}"; do
        dest="$out_dir/${files[$src_name]}"
        if [ -f "$src_dir/$src_name" ]; then
            cp "$src_dir/$src_name" "$dest"
        else
            log_info "${CLR_WARN}ÅTVARING: $src_dir/$src_name finst ikkje — hoppar over${CLR_RST}"
            printf '%s\n' "# Analyse ikkje tilgjengeleg" "" \
                "Rapporten vart ikkje generert i denne bygginga." > "$dest"
        fi
    done

    cat > "$out_dir/index.md" <<'EOF'
# Modellanalyse på tvers av domene

Desse sidene viser navnelikskaps-analysar køyrde på tvers av **alle**
domene i repoet — til skilnad frå dei domene-scopa analysane som ligg
under kvar enkelt modell sin `## Modellanalyse`-seksjon.

- [Liknande klassenavn](liknande-klassenavn-alle-domene.md)
- [Liknande slotnavn](liknande-slotnavn-alle-domene.md)
- [Liknande typenavn](liknande-typenavn-alle-domene.md)
EOF
}

# ---------------------------------------------------------------------------
# Generer index.md frå README.md (+ footer med byggetidspunkt)
# ---------------------------------------------------------------------------
write_index_from_readme() {
    cp "$REPO_ROOT/README.md" "$DOCS/index.md"

    cat >> "$DOCS/index.md" <<EOF

---

_Portalen vart sist bygd: ${BUILD_TIMESTAMP}_
EOF
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
    t0=$(now_ms)

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

    local elapsed_ms=$(( $(now_ms) - t0 ))
    log_info "$(printf "${CLR_STEP}  → %s/%s${CLR_RST} (%s)" \
        "$domain" "$schema" \
        "$(fmt_elapsed_ms "$elapsed_ms")")"
}

# ---------------------------------------------------------------------------
# Steg 1: Rens tidlegare genererte domene-katalogar frå docs/
# ---------------------------------------------------------------------------
log_step "Steg 1: Rens tidlegare genererte domene-katalogar frå docs/"
t1=$(now_ms)

if [ ! -d "$GEN" ] || [ -z "$(ls -A "$GEN" 2>/dev/null)" ]; then
    log_error "Ingen genererte artefakter funne i $GEN. Køyr make <domain> fyrst."
    exit 1
fi

clean_previous_docs() {
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
        log_debug "→ Slettar $DOCS/$domain"
        find "${DOCS}/${domain}" -mindepth 1 -depth -delete 2>/dev/null || true
        rmdir "${DOCS}/${domain}" 2>/dev/null || true
    done

    # Slett mkdocs/docs/$domain/ for domene som ikkje lenger finst i generated/
    for docs_domain_dir in "$DOCS"/*/; do
        [ -d "$docs_domain_dir" ] || continue
        domain=$(basename "$docs_domain_dir")
        case "$domain" in
            stylesheets|javascripts|kom-i-gang|arkitektur|publisering|automasjon|modellanalyse) continue ;;
        esac
        if [ ! -d "$GEN/$domain" ]; then
            log_info "Ryddar forsvunne domene: $domain"
            rm -rf "$docs_domain_dir"
        fi
    done
}

timed_run "Rens tidlegare genererte domene-katalogar" clean_previous_docs

# Generer byggetidspunkt (ISO 8601 UTC), nødvendig for footer-en
# write_index_from_readme() skriv rett under
BUILD_TIMESTAMP=$(TZ="Europe/Oslo" date +"%Y-%m-%d %H:%M %Z")

# README-tabellgenerering, README→index.md og valideringsregler.md avheng
# ikkje av noko frå Steg 2 (statiske kjeldefiler, arkitektur/ er kvitelista
# i Steg 1 sin opprydding) — flytta hit for å unngå unødig venting etter
# det tunge parallelle skjema-arbeidet. Kvart kall tidtakast og loggast
# individuelt via timed_run() (frå LOG_FUNCTIONS, make/00-settings.mk) i
# staden for eit samla steg-tal. Inngår i Steg 1 sin samla tidtaking —
# "✓ Steg 1 ferdig" loggast fyrst etter Steg 1.4/1.5 lenger ned, slik at
# ho står som siste linje av Steg 1 rett før Steg 2-banneret. Sjå
# specs/done/flytt-steg3-til-steg1-med-timing.md og
# specs/done/flytt-readme-tabellar-inn-i-publish-sh.md.
#
# README-tabellgenereringa må køyrast FØR write_index_from_readme, sidan
# index.md vert kopiert direkte frå README.md — elles kopierer
# write_index_from_readme ein utdatert versjon av tabellane.
timed_run "Oppdater README.md-tabellar" bash "$REPO_ROOT/src/assets/scripts/makefile/generate-readme-tables.sh" "$REPO_ROOT/README.md"
timed_run "Generer index.md frå README.md" write_index_from_readme
timed_run "Generer valideringsregler.md" generate_validation_docs
timed_run "Generer modellanalyse-tvers-domene-sider" generate_cross_domain_modellanalyse_docs

# ---------------------------------------------------------------------------
# Steg 1.4: Finn domene/skjema-struktur frå generated/
# ---------------------------------------------------------------------------
# Flytta hit frå (tidlegare) Steg 2 — denne enumereringa avheng berre av
# $GEN, ikkje av noko bygd i Steg 1.5, og Steg 1.5 treng no
# ALL_DOMAINS/DOMAIN_SCHEMA_LIST for å byggje input til det samla
# metadata-kallet. Sjå specs/backlog/reduser-podman-kall-docs-publish.md.
#
# Tidteke som eige delsteg (manuell t/elapsed, ikkje timed_run) sidan
# ALL_DOMAINS/DOMAIN_SCHEMA_LIST/DOMAIN_EXISTS må vere synlege i
# hovudshell-scope etter blokka — ei `declare -a`/`declare -A` inni ein
# bash-funksjon utan `-g` ville gjort desse lokale og usynlege for Steg
# 1.5/2/3. Sjå specs/done/tidtaking-steg1-4-1-5-docs-publish.md.
t1_4=$(now_ms)
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

elapsed1_4_ms=$(( $(now_ms) - t1_4 ))
log_info "$(printf "${CLR_STEP}→ Steg 1.4: Finn domene/skjema-struktur${CLR_RST} (%s)" \
    "$(fmt_elapsed_ms "$elapsed1_4_ms")")"

# ---------------------------------------------------------------------------
# Steg 1.5: Bygg delmodell-/metadata-oppslag
# ---------------------------------------------------------------------------
# Same grunngjeving som Steg 1.4 for manuell t/elapsed i staden for
# timed_run: SCHEMA_PARENT_MODEL/SCHEMA_SUBMODELS m.fl. må vere synlege i
# hovudshell-scope for Steg 2/3.
t1_5=$(now_ms)

# Bruk assosiative arrays som må eksporterast manuelt til subshells
declare -A SCHEMA_PARENT_MODEL_TMP=()
declare -A SCHEMA_SUBMODELS_TMP=()

# Globalt oppslag skjemanavn → domene og → filsti, bygd éin gong for heile
# repoet. Erstattar gjentekne whole-tree `find "$REPO_ROOT/src/linkml" -name
# "<navn>-schema.yaml"`-kall i classes.sh/avhengigheiter.sh (kvart slikt
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

# Samla metadata-innhenting: EIN containerprosess (collect-schema-metadata.py)
# for ALLE skjema, i staden for opptil ~211 separate `podman run`-kall (éin
# per submodels-oppslag/skjema-felt) — kvart `podman run`-kall har ~2,7s
# eigen container-oppstartskostnad, målt direkte. Sjå
# specs/backlog/reduser-podman-kall-docs-publish.md for profilering og
# grunngjeving.
#
# Input (stdin, éi linje per skjema i DOMAIN_SCHEMA_LIST): felt skilde med
# \x1f — domain, schema, schema_file (container-sti, tom viss ikkje funnen),
# manifest_path (container-sti, tom viss build.yaml ikkje finst).
SCHEMA_METADATA_INPUT=""
for domain in "${ALL_DOMAINS[@]}"; do
    for schema in ${DOMAIN_SCHEMA_LIST[$domain]:-}; do
        schema_file_path=$(lookup_schema_path "${schema}-schema") || schema_file_path=""
        schema_file_container=""
        [ -n "$schema_file_path" ] && schema_file_container=$(to_container_path "$schema_file_path")

        manifest_path="$REPO_ROOT/src/linkml/${domain}/${schema}/build.yaml"
        manifest_container=""
        [ -f "$manifest_path" ] && manifest_container=$(to_container_path "$manifest_path")

        SCHEMA_METADATA_INPUT+="${domain}$(printf '\x1f')${schema}$(printf '\x1f')${schema_file_container}$(printf '\x1f')${manifest_container}"$'\n'
    done
done

COLLECT_OUTPUT=$(printf '%s' "$SCHEMA_METADATA_INPUT" | run_python_container /work/mkdocs/lib/scripts/collect-schema-metadata.py)

# Splitt output i dei tre seksjonane scriptet skriv (### SUBMODELS /
# ### SCHEMAS / ### ORGS), kvar linje felt-skilt med \x1f.
SUBMODELS_SECTION=""
SCHEMAS_SECTION=""
ORGS_SECTION=""
collect_mode=""
while IFS= read -r collect_line; do
    case "$collect_line" in
        "### SUBMODELS") collect_mode="submodels"; continue ;;
        "### SCHEMAS") collect_mode="schemas"; continue ;;
        "### ORGS") collect_mode="orgs"; continue ;;
    esac
    case "$collect_mode" in
        submodels) SUBMODELS_SECTION+="$collect_line"$'\n' ;;
        schemas) SCHEMAS_SECTION+="$collect_line"$'\n' ;;
        orgs) ORGS_SECTION+="$collect_line"$'\n' ;;
    esac
done <<< "$COLLECT_OUTPUT"

# Bygg SCHEMA_SUBMODELS_TMP/SCHEMA_PARENT_MODEL_TMP frå SUBMODELS-seksjonen
# (same semantikk som den tidlegare 41-kalls-sekvensielle løkka)
while IFS=$'\x1f' read -r schema_key submodels_csv; do
    [ -z "$schema_key" ] && continue
    SCHEMA_SUBMODELS_TMP["$schema_key"]="$submodels_csv"
    IFS=',' read -ra sub_array <<< "$submodels_csv"
    for sub in "${sub_array[@]}"; do
        SCHEMA_PARENT_MODEL_TMP["$sub"]="$schema_key"
    done
done <<< "$SUBMODELS_SECTION"

# Eksporter per-skjema metadata og CODEOWNERS-org-registeret til subshells
# — konsumert via lookup_schema_metadata_line()/lookup_org_name() i
# mkdocs/lib/utils/imported_schemas.sh
export SCHEMA_METADATA_SERIALIZED="$SCHEMAS_SECTION"
export ORG_URI_TO_NAME_SERIALIZED="$ORGS_SECTION"

# Serialiser delmodell-map til miljøvariablar for eksport til subshells
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

elapsed1_5_ms=$(( $(now_ms) - t1_5 ))
log_info "$(printf "${CLR_STEP}→ Steg 1.5: Bygg delmodell-/metadata-oppslag${CLR_RST} (%s)" \
    "$(fmt_elapsed_ms "$elapsed1_5_ms")")"

elapsed1_ms=$(( $(now_ms) - t1 ))
log_info "$(printf "${CLR_OK}✓ Steg 1 ferdig${CLR_RST} (%s)" \
    "$(fmt_elapsed_ms "$elapsed1_ms")")"

# ---------------------------------------------------------------------------
# Steg 2: Generer innhald per domene og skjema (parallelt)
# ---------------------------------------------------------------------------
log_step "Steg 2: Generer innhald per domene og skjema (parallelt)"
t2=$(now_ms)

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

log_info "${CLR_OK}Publisert ${#ALL_DOMAINS[@]} domene(r) til mkdocs/docs/${CLR_RST}"

elapsed2_ms=$(( $(now_ms) - t2 ))
log_info "$(printf "${CLR_OK}✓ Steg 2 ferdig${CLR_RST} (%s)" \
    "$(fmt_elapsed_ms "$elapsed2_ms")")"

# ---------------------------------------------------------------------------
# Steg 3: Generer mkdocs.yml
# ---------------------------------------------------------------------------
log_step "Steg 3: Generer mkdocs.yml"
t4=$(now_ms)

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
    # - navigation.instant  # mellombels av: test om dette er årsaka til at
    #   TOC-aktiv-klasse-fiksen (toc-active-click-fix.js) ikkje verkar —
    #   sjå specs/backlog/toc-aktivt-element-ved-klikk.md
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

extra_javascript:
  - javascripts/toc-active-click-fix.js # Umiddelbar aktiv-markering av TOC-lenkje ved klikk

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

# gen-doc genererer systematiske fragment-lenkjer utan filnavn (t.d.
# ../../ap-no/dcat-ap-no/#classes i staden for .../index.md#classes) som
# mkdocs ikkje kjenner att som interne lenkjer. Denne åtvaringa er ikkje
# kritisk og vert undertrykka her. Merk: dette dekkjer ikkje mermaid
# click-hrefs (klikkbare lenkjer i klassediagram) — mkdocs sin
# lenkje-validator ser berre rendra <a href>-element, ikkje rå tekst inni
# fenced code-blokker, sjå specs/backlog/mermaid-klikkbare-lenker-404.md.
validation:
  links:
    not_found: warn
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
          - Standardetterleving: arkitektur/standardetterleving.md
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
      - Modellanalyse:
          - modellanalyse/index.md
          - Liknande klassenavn (alle domene): modellanalyse/liknande-klassenavn-alle-domene.md
          - Liknande slotnavn (alle domene): modellanalyse/liknande-slotnavn-alle-domene.md
          - Liknande typenavn (alle domene): modellanalyse/liknande-typenavn-alle-domene.md
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

log_info "${CLR_OK}Oppdatert mkdocs/mkdocs.yml${CLR_RST}"

elapsed4_ms=$(( $(now_ms) - t4 ))
log_info "$(printf "${CLR_OK}✓ Steg 3 ferdig${CLR_RST} (%s)" \
    "$(fmt_elapsed_ms "$elapsed4_ms")")"
