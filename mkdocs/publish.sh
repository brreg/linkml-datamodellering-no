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
        ap-no)   echo "AP-NO - Applikasjonsprofiler" ;;
        begrepskatalog) echo "Begrepskatalog - Begrepskatalogmodellar" ;;
        modellkatalog)   echo "Modellkatalog - Informasjonsmodellar" ;;
        ngr)     echo "NGR - Nasjonale Grunndata" ;;
        fint)    echo "FINT - Fylkeskommunale integrasjonar" ;;
        samt)    echo "SAMT - Kommunale integrasjonar" ;;
        fair)    echo "FAIR - Metadataoverbygning" ;;
        oreg)    echo "OREG - Offentlege registre" ;;
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
        schema.xsd)     echo "XML Schema (XSD)" ;;
        openapi.yaml)   echo "OpenAPI 3.1" ;;
        asyncapi.yaml)  echo "AsyncAPI 3.0" ;;
        model.py)       echo "Python-klasser" ;;
        schema.proto)   echo "Protobuf-skjema" ;;
        erdiagram.md)   echo "ER-diagram (Mermaid)" ;;
        eksempel.ttl)   echo "Eksempeldata (Turtle)" ;;
        *)              echo "$1" ;;
    esac
}

# Rekkjefølgje på artefakter i tabellen
ARTIFACT_ORDER="shapes.ttl context.jsonld schema.json schema.xsd openapi.yaml asyncapi.yaml ontology.ttl schema.ttl model.py schema.proto erdiagram.md eksempel.ttl"

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

    # Kopier CHANGELOG.md dersom den finst
    changelog_src="$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"
    if [ -f "$changelog_src" ]; then
        cp "$changelog_src" "$out/CHANGELOG.md"
    fi

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

        # Metadata-tabell frå gen-doc (ekstrahert frå docs/index.md)
        gendoc_index="$schema_dir/docs/index.md"
        if [ -f "$gendoc_index" ]; then
            # Ekstraher frå "## Metadata" til neste "## "-seksjon (ikkje inkludert)
            awk '/^## Metadata$/{ p=1 } p{ if(/^## / && !/^## Metadata$/){ exit } print }' "$gendoc_index"
        fi

        # Publiseringsinfo: boks dersom skjema har eit publisert URI-register
        lock_file="$REPO_ROOT/src/linkml/$domain/$schema/published-uris.lock"
        if [ -f "$lock_file" ]; then
            ttl_url="https://brreg.github.io/linkml-datamodellering-no/$domain/$schema/$schema.ttl"
            echo ""
            echo "!!! info \"Publisert til Felles Begrepskatalog\""
            echo "    Denne katalogen er publisert til [data.norge.no/concepts](https://data.norge.no/concepts)"
            echo "    via høstingsendepunkt. Turtle-fila er tilgjengeleg på:"
            echo ""
            echo "    \`${ttl_url}\`"
            echo ""
            echo "    Sjå [Publiser til Felles Begrepskatalog](../../publisering-begrep.md) for rettleiing"
            echo "    om arbeidsflyt, URI-stabilitet og oppsett for nye katalogar."
            echo ""
        fi

        # Embed PlantUML-diagram (filtrert versjon — kun lokale klasser)
        plantuml_svg="diagrams/${schema}-filtered.svg"
        plantuml_full="diagrams/${schema}.svg"

        # Prioriter filtrert versjon
        if [ -f "$out/$plantuml_svg" ]; then
            echo ""
            echo "## ER-diagram"
            echo ""
            echo "[![ER-diagram]($plantuml_svg)]($plantuml_svg){:target=\"_blank\"}"
            echo ""
            echo "*Diagrammet viser kun lokale klasser. Klikk for å zoome. [Vis fullstendig diagram med importerte klasser]($plantuml_full).*"
        elif [ -f "$out/$plantuml_full" ]; then
            echo ""
            echo "## ER-diagram"
            echo ""
            echo "[![ER-diagram]($plantuml_full)]($plantuml_full){:target=\"_blank\"}"
            echo ""
            echo "*Klikk for å zoome.*"
        fi

        # Inline klasseliste frå gen-doc direkte i index.md
        klasse_src=""
        [ -f "$out/klasser/index.md" ] && klasse_src="$out/klasser/index.md"
        [ -z "$klasse_src" ] && [ -f "$out/klasser/${schema}.md" ] && klasse_src="$out/klasser/${schema}.md"

        if [ -n "$klasse_src" ]; then
            echo ""
            # Ekstraher frå "## Classes" til slutten (hoppar over Metadata og Schema Diagram)
            awk '/^## Classes$/,0' "$klasse_src" \
                | sed 's/](\([^)]*\.md\))/](klasser\/\1)/g'
        fi

        # Artefaktabell (før valideringsresultat)
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
        # Prioriter filtrert versjon (kun domenemodell) over full versjon
        puml_svg_filtered="$out/diagrams/${schema}-filtered.svg"
        puml_src_filtered="$out/diagrams/${schema}-filtered.puml"
        puml_svg_full="$out/diagrams/${schema}.svg"
        puml_src_full="$out/diagrams/${schema}.puml"

        if [ -f "$puml_svg_filtered" ] || [ -f "$puml_src_filtered" ] || [ -f "$puml_svg_full" ] || [ -f "$puml_src_full" ]; then
            has_artifact=true
            puml_links=""
            # Vis filtrert versjon først (hovuddiagram)
            if [ -f "$puml_svg_filtered" ]; then
                puml_links="[${schema}-filtered.svg](diagrams/${schema}-filtered.svg)"
            elif [ -f "$puml_svg_full" ]; then
                puml_links="[${schema}.svg](diagrams/${schema}.svg)"
            fi
            # Legg til puml-kjeldekode
            if [ -f "$puml_src_filtered" ]; then
                [ -n "$puml_links" ] && puml_links+=" · "
                puml_links+="[${schema}-filtered.puml](diagrams/${schema}-filtered.puml)"
            fi
            if [ -f "$puml_src_full" ]; then
                [ -n "$puml_links" ] && puml_links+=" · "
                puml_links+="[${schema}.puml](diagrams/${schema}.puml) (full)"
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

        # Valideringsresultat frå siste versjon (co-location-struktur)
        local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/manifest.yaml"
        local policy="bronze"
        if [ -f "$manifest" ]; then
            # Les validation_policy frå manifest.yaml (bruk Python i staden for yq)
            policy=$(python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('validation_policy', 'bronze'))" 2>/dev/null || echo "bronze")
        fi

        # Finn siste versjon programmatisk (semver-sortering)
        local validation_dir="$REPO_ROOT/src/linkml/${domain}/${schema}/validation"
        local latest_version=""
        if [ -d "$validation_dir" ]; then
            # Sorter versjonar semantisk (semver: 1.10.0 > 1.2.0)
            latest_version=$(ls -v "$validation_dir" 2>/dev/null | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | tail -n1)
        fi

        # Finn validation-logg for siste versjon og denne policyen
        local validation_json=""
        if [ -n "$latest_version" ]; then
            validation_json="$validation_dir/$latest_version/${policy}.json"
        fi

        if [ -f "$validation_json" ]; then
            python3 "$REPO_ROOT/src/assets/scripts/generate-validation-md.py" "$validation_json"
        else
            echo ""
            echo "## Valideringsresultat"
            echo ""
            echo "*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*"
        fi

        # Versjonslog (CHANGELOG.md som rein Markdown)
        changelog_src="$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"
        if [ -f "$changelog_src" ]; then
            echo ""
            echo "## Versjonslog"
            echo ""
            # Fjern hovudoverskrift "# Changelog" frå CHANGELOG.md dersom den finst
            tail -n +1 "$changelog_src" | awk 'NR==1 && /^# Changelog/ { next } 1'
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
      - Om: om.md
      - Bruk frå eksternt repo: ekstern-bruk.md
      - Bli modelleigar: ny-org.md
      - Ny domenemodell: ny-domenemodell.md
      - Ny begrepskatalog: ny-begrepsmodell.md
      - Modellmanifest: manifest-config.md
      - Valideringsregler: valideringsregler.md
      - Arkitekturoversikt publisering: arkitektur-oversikt.md
      - Publiser til Felles Begrepskatalog: publisering-begrep.md
      - Publiser til Felles Datakatalog: publisering-modell.md
      - AP-NO arkitektur og avvik: ap-no-arkitektur.md
      - Monitorering av automasjon: monitorering.md
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
