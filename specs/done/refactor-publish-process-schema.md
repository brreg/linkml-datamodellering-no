# Refactor: `publish.sh:process_schema()` — Splitt opp i logiske modular

## Bakgrunn

`publish.sh:process_schema()` er for lang og gjer for mykje (linjer 216-611, ~390 linjer).
Funksjonen genererer alle seksjonsbolkar i `index.md` for kvart skjema, med minst 19
ulike ansvarsområder (sjå `mkdocs/docs/index-md-struktur.md`).

Dette gjer funksjonen vanskeleg å:
- Teste isolert
- Vedlikehalde (lang heredoc med innbygd bash-logikk)
- Utvide (ny seksjon krev endring midt i heredoc)
- Forstå (blanding av filkopi, parsing, generering og formatering)

## Målsetjing

Splitt `process_schema()` i mindre, testbare funksjonar med klart avgrensa ansvar.
Kvar funksjon skal generere éin seksjon i `index.md`.

## Designprinsipp

### 1. Separer filkopi frå innhaldsgenerering

```bash
# Før: Alt i process_schema()
process_schema() {
    # Kopier filer (linjer 224-257)
    # Generer index.md (linjer 262-604)
}

# Etter: To separate steg
process_schema() {
    copy_schema_artifacts "$domain" "$schema" "$schema_dir" "$out"
    generate_schema_index "$domain" "$schema" "$schema_dir" "$out"
}
```

### 2. Ein funksjon per index.md-seksjon

Kvar seksjon i tabellen i `index-md-struktur.md` får sin eigen funksjon:

```bash
generate_schema_index() {
    {
        generate_header "$schema"
        generate_badges "$domain" "$schema" "$gendoc_index"
        generate_external_reference "$domain" "$schema"
        generate_description "$domain" "$schema"
        generate_quickstart "$domain" "$schema"
        generate_example "$domain" "$schema"
        generate_metadata "$gendoc_index"
        generate_publishing_info "$domain" "$schema"
        generate_dependencies "$domain" "$schema"
        generate_er_diagram "$schema" "$out"
        generate_classes_section "$klasse_src"
        generate_artifacts_table "$out" "$schema"
        generate_validation_results "$domain" "$schema"
        generate_changelog "$domain" "$schema"
        generate_contact_info "$domain" "$schema"
    } > "$out/index.md"
}
```

### 3. Pure functions der mogleg

Funksjonar skal returnere Markdown-tekst til stdout, ikkje skrive direkte til fil.
Dette gjer dei testbare og komponerbare:

```bash
generate_badges() {
    local domain="$1"
    local schema="$2"
    local gendoc_index="$3"

    # Parse metadata
    local version=$(grep "^| Versjon" "$gendoc_index" | ...)
    local status=$(grep "^| Status" "$gendoc_index" | ...)
    # ...

    # Output Markdown til stdout
    echo "[![Versjon](https://img.shields.io/badge/versjon-${version}-blue)]()"
    echo "[![Status](https://img.shields.io/badge/status-${status_label}-${status_color})]()"
    # ...
}
```

### 4. Valfrie seksjonar returnerer tom streng

Seksjonar som er valfrie (t.d. `description.md`, `external_spec_url`) skal returnere
tom streng dersom innhaldet ikkje finst:

```bash
generate_description() {
    local domain="$1"
    local schema="$2"
    local description_file="$REPO_ROOT/src/linkml/$domain/$schema/description.md"

    [ ! -f "$description_file" ] && return 0

    cat "$description_file"
    echo ""
    echo ""
}
```

### 5. Metadata-parsing som eigne hjelpefunksjonar

Parsing av manifest, validation-policy, versjon osv. skal skiljast ut:

```bash
get_validation_policy() {
    local manifest="$1"
    [ ! -f "$manifest" ] && echo "bronze" && return
    python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('validation_policy', 'bronze'))" 2>/dev/null || echo "bronze"
}

get_latest_validation_version() {
    local validation_dir="$1"
    [ ! -d "$validation_dir" ] && return
    ls -v "$validation_dir" 2>/dev/null | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | tail -n1
}

get_external_spec_url() {
    local manifest="$1"
    [ ! -f "$manifest" ] && return
    python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('external_spec_url', ''))" 2>/dev/null || echo ""
}
```

## Foreslått filstruktur etter refactoring

```
mkdocs/
  publish.sh                    ← Hovudscript (steg 1-4, orkestrering)
  lib/
    copy_artifacts.sh           ← Steg 2a: Kopier artefakter (linjer 224-257)
    generate_index.sh           ← Steg 2b: Orkestrering av index.md-generering
    sections/                   ← Éin fil per seksjon i index.md
      header.sh                 ← Seksjon 1: Hovudoverskrift
      badges.sh                 ← Seksjon 2: Badge-rad
      external_reference.sh     ← Seksjon 3: Offisiell referanse
      description.sh            ← Seksjon 4: description.md
      quickstart.sh             ← Seksjon 5: Kom i gang
      example.sh                ← Seksjon 6: Eksempeldatafil
      metadata.sh               ← Seksjon 7: Modellmetadata
      publishing_info.sh        ← Seksjon 8: Publiseringsinfo
      dependencies.sh           ← Seksjon 9: Avhengigheiter (flyttar build_dependency_graph)
      er_diagram.sh             ← Seksjon 10: ER-diagram
      classes.sh                ← Seksjon 11-15: Classes, Slots, Enums, Types, Subsets
      artifacts.sh              ← Seksjon 16: Generated artifacts
      validation.sh             ← Seksjon 17: Valideringsresultat
      changelog.sh              ← Seksjon 18: Versjonslog
      contact.sh                ← Seksjon 19: Kontakt
    utils/
      metadata_parsers.sh       ← Hjelpefunksjonar for parsing av manifest, versjon osv.
      formatters.sh             ← Hjelpefunksjonar for formatering (artifact_label, domain_label)
```

## Steg-for-steg refactoring

### Steg 1: Oppsett av lib/-katalogstruktur

```bash
mkdir -p mkdocs/lib/{sections,utils}
```

### Steg 2: Ekstraher hjelpefunksjonar først

Flytt `artifact_label()` og `domain_label()` til `lib/utils/formatters.sh`:

```bash
# mkdocs/lib/utils/formatters.sh
artifact_label() {
    case "$1" in
        shapes.ttl)     echo "SHACL shapes" ;;
        # ... (eksisterande logikk)
    esac
}

domain_label() {
    case "$1" in
        ap-no)   echo "AP-NO - Applikasjonsprofiler" ;;
        # ... (eksisterande logikk)
    esac
}
```

Opprett `lib/utils/metadata_parsers.sh`:

```bash
# mkdocs/lib/utils/metadata_parsers.sh

get_validation_policy() {
    local manifest="$1"
    [ ! -f "$manifest" ] && echo "bronze" && return
    python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('validation_policy', 'bronze'))" 2>/dev/null || echo "bronze"
}

get_latest_validation_version() {
    local validation_dir="$1"
    [ ! -d "$validation_dir" ] && return
    ls -v "$validation_dir" 2>/dev/null | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | tail -n1
}

get_external_spec_url() {
    local manifest="$1"
    [ ! -f "$manifest" ] && return
    python3 -c "import yaml; print(yaml.safe_load(open('$manifest')).get('external_spec_url', ''))" 2>/dev/null || echo ""
}

get_validation_json_path() {
    local domain="$1"
    local schema="$2"
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/manifest.yaml"
    local policy=$(get_validation_policy "$manifest")
    local validation_dir="$REPO_ROOT/src/linkml/${domain}/${schema}/validation"
    local latest_version=$(get_latest_validation_version "$validation_dir")

    [ -z "$latest_version" ] && return
    echo "$validation_dir/$latest_version/${policy}.json"
}
```

### Steg 3: Ekstraher seksjonsgenererande funksjonar

**Eksempel 1: `lib/sections/badges.sh`**

```bash
#!/usr/bin/env bash
# Generer badge-rad (seksjon 2 i index.md)
set -euo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/../utils/metadata_parsers.sh"

generate_badges() {
    local domain="$1"
    local schema="$2"
    local gendoc_index="$3"

    [ ! -f "$gendoc_index" ] && return 0

    # Parse metadata frå gen-doc
    local version=$(grep "^| Versjon" "$gendoc_index" | sed 's/.*| \([^ ]*\) |/\1/' | head -1)
    local status=$(grep "^| Status" "$gendoc_index" | sed 's|.*status/\([^)]*\).*|\1|' | head -1)
    local license=$(grep "^| Lisens" "$gendoc_index" | sed 's|.*/nlod/no/\([0-9.]*\).*|\1|' | head -1)

    # Valideringsstatus
    local validation_json=$(get_validation_json_path "$domain" "$schema")
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/manifest.yaml"
    local policy=$(get_validation_policy "$manifest")
    local val_status="ukjent"
    local val_color="lightgrey"

    if [ -f "$validation_json" ]; then
        local errors=$(python3 -c "import json; d=json.load(open('$validation_json')); print(d.get('result', {}).get('error_count', 0))" 2>/dev/null || echo "0")
        [ -z "$errors" ] && errors="0"
        if [ "$errors" -eq 0 ]; then
            val_status="✓_godkjent"
            val_color="green"
        else
            val_status="${errors}_feil"
            val_color="yellow"
        fi
    fi

    # Normaliser status-namn
    local status_label="$status"
    local status_color="blue"
    case "$status" in
        Completed) status_label="Ferdigstilt"; status_color="green" ;;
        UnderDevelopment) status_label="Under_utvikling"; status_color="orange" ;;
        Deprecated) status_label="Foreldet"; status_color="red" ;;
        Withdrawn) status_label="Trukket_tilbake"; status_color="red" ;;
    esac

    # URL-encode
    local val_status_encoded="${val_status// /_}"
    val_status_encoded="${val_status_encoded//✓/%E2%9C%93}"
    local policy_encoded="${policy//-/_}"

    # Output badges
    echo "[![Versjon](https://img.shields.io/badge/versjon-${version}-blue)]()"
    echo "[![Status](https://img.shields.io/badge/status-${status_label}-${status_color})]()"
    echo "[![Validering](https://img.shields.io/badge/${policy_encoded}-${val_status_encoded}-${val_color})]()"
    [ -n "$license" ] && echo "[![Lisens](https://img.shields.io/badge/NLOD-${license}-blue)]()"
    echo ""
}
```

**Eksempel 2: `lib/sections/description.sh`**

```bash
#!/usr/bin/env bash
# Generer description.md-seksjon (seksjon 4 i index.md)
set -euo pipefail

generate_description() {
    local domain="$1"
    local schema="$2"
    local description_file="$REPO_ROOT/src/linkml/$domain/$schema/description.md"

    [ ! -f "$description_file" ] && return 0

    cat "$description_file"
    echo ""
    echo ""
}
```

**Eksempel 3: `lib/sections/validation.sh`**

```bash
#!/usr/bin/env bash
# Generer valideringsresultat-seksjon (seksjon 17 i index.md)
set -euo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/../utils/metadata_parsers.sh"

generate_validation_results() {
    local domain="$1"
    local schema="$2"
    local validation_json=$(get_validation_json_path "$domain" "$schema")

    echo ""
    echo "---"
    echo ""

    if [ -f "$validation_json" ]; then
        python3 "$REPO_ROOT/src/assets/scripts/generate-validation-md.py" "$validation_json"
    else
        echo "## Valideringsresultat"
        echo ""
        echo "*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*"
    fi
}
```

### Steg 4: Opprett `lib/copy_artifacts.sh`

Flytt filkopi-logikken (linjer 224-257 i `process_schema`) til eigen fil:

```bash
#!/usr/bin/env bash
# Kopier genererte artefakter til mkdocs/docs/
set -euo pipefail

copy_schema_artifacts() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$3"
    local out="$4"

    mkdir -p "$out/klasser"

    # Kopier artefaktfiler (berre filer, ikkje docs/-underkatalog)
    find "$schema_dir" -maxdepth 1 -type f -exec cp {} "$out/" \;

    # Kopier CHANGELOG.md dersom den finst
    local changelog_src="$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"
    [ -f "$changelog_src" ] && cp "$changelog_src" "$out/CHANGELOG.md"

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
            local base=$(basename "$f")
            local lower=$(echo "$base" | tr '[:upper:]' '[:lower:]')
            if [ "$base" != "$lower" ]; then
                mv "$f" "$out/klasser/${lower}.tmp"
                mv "$out/klasser/${lower}.tmp" "$out/klasser/$lower"
            fi
        done
        # Oppdater alle interne .md-lenkjer til lowercase
        find "$out/klasser" -maxdepth 1 -name "*.md" \
            -exec sed -i 's/](\([^)]*\.md\))/](\L\1)/g' {} \;
    fi
}
```

### Steg 5: Opprett `lib/generate_index.sh`

Hovudorkestreringsfil for `index.md`-generering:

```bash
#!/usr/bin/env bash
# Orkestrer generering av index.md per skjema
set -euo pipefail

# Source alle seksjonsgenererande funksjonar
SECTIONS_DIR="$(dirname "${BASH_SOURCE[0]}")/sections"
for section_file in "$SECTIONS_DIR"/*.sh; do
    source "$section_file"
done

generate_schema_index() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$3"
    local out="$4"

    local gendoc_index="$schema_dir/docs/index.md"

    # Finn klasse-kjelde (index.md eller ${schema}.md)
    local klasse_src=""
    [ -f "$out/klasser/index.md" ] && klasse_src="$out/klasser/index.md"
    [ -z "$klasse_src" ] && [ -f "$out/klasser/${schema}.md" ] && klasse_src="$out/klasser/${schema}.md"

    {
        generate_header "$schema"
        generate_badges "$domain" "$schema" "$gendoc_index"
        generate_external_reference "$domain" "$schema"
        generate_description "$domain" "$schema"
        generate_quickstart "$domain" "$schema"
        generate_example "$domain" "$schema"
        generate_metadata "$gendoc_index"
        generate_publishing_info "$domain" "$schema"
        generate_dependencies "$domain" "$schema"
        generate_er_diagram "$schema" "$out"
        generate_classes_section "$klasse_src"
        generate_artifacts_table "$out" "$schema"
        generate_validation_results "$domain" "$schema"
        generate_changelog "$domain" "$schema"
        generate_contact_info "$domain" "$schema"
    } > "$out/index.md"
}
```

### Steg 6: Refactorer `publish.sh:process_schema()`

Erstatt den lange funksjonen med to funksjonskall:

```bash
# mkdocs/publish.sh

# Source lib-filer
source "$(dirname "${BASH_SOURCE[0]}")/lib/copy_artifacts.sh"
source "$(dirname "${BASH_SOURCE[0]}")/lib/generate_index.sh"
source "$(dirname "${BASH_SOURCE[0]}")/lib/utils/formatters.sh"
source "$(dirname "${BASH_SOURCE[0]}")/lib/utils/metadata_parsers.sh"

process_schema() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$GEN/$domain/$schema"
    local out="$DOCS/$domain/$schema"
    local t0
    t0=$(date +%s%3N)

    # Steg 2a: Kopier artefakter
    copy_schema_artifacts "$domain" "$schema" "$schema_dir" "$out"

    # Steg 2b: Generer index.md
    generate_schema_index "$domain" "$schema" "$schema_dir" "$out"

    local elapsed_ms=$(( $(date +%s%3N) - t0 ))
    printf "${CLR_STEP}  → %s/%s${CLR_RST} (%d.%ds)\n" \
        "$domain" "$schema" \
        $((elapsed_ms / 1000)) \
        $((elapsed_ms % 1000 / 100))
}
```

## Fordeler med denne refactoringa

### 1. **Testbarheit**

Kvar seksjonsgenerator kan testast isolert:

```bash
# Test badge-generering
source mkdocs/lib/sections/badges.sh
output=$(generate_badges "samt" "samt-bu" "$REPO_ROOT/generated/samt/samt-bu/docs/index.md")
echo "$output" | grep -q "[![Versjon]" && echo "OK" || echo "FEIL"
```

### 2. **Vedlikehald**

Endring i éin seksjon krev berre endring i éin fil:

```bash
# Før: Søk gjennom 390 linjer heredoc i process_schema()
# Etter: Rediger mkdocs/lib/sections/badges.sh (30 linjer)
```

### 3. **Gjenbruk**

Seksjonsgenererande funksjonar kan gjenbrukast i andre kontekstar (t.d. README-generering):

```bash
source mkdocs/lib/sections/metadata.sh
generate_metadata "$gendoc_index" > docs/metadata-only.md
```

### 4. **Parallelisering**

Valfrie seksjonar kan køyrast parallelt dersom dei ikkje deler tilstand:

```bash
generate_badges "$domain" "$schema" "$gendoc_index" &
generate_description "$domain" "$schema" &
generate_quickstart "$domain" "$schema" &
wait
```

### 5. **Dokumentasjon**

Kvar fil i `lib/sections/` mappar direkte til ein rad i tabellen i `index-md-struktur.md`:

| Seksjon | Fil |
|---|---|
| Hovudoverskrift | `lib/sections/header.sh` |
| Badge-rad | `lib/sections/badges.sh` |
| Offisiell referanse | `lib/sections/external_reference.sh` |
| ... | ... |

## Tiltak

- [x] **Tiltak 1:** Opprett `mkdocs/lib/{sections,utils}/`-katalogstruktur
- [x] **Tiltak 2:** Ekstraher `lib/utils/formatters.sh` (`artifact_label`, `domain_label`)
- [x] **Tiltak 3:** Ekstraher `lib/utils/metadata_parsers.sh` (alle `get_*`-funksjonar)
- [x] **Tiltak 4:** Ekstraher `lib/sections/header.sh` (seksjon 1)
- [x] **Tiltak 5:** Ekstraher `lib/sections/badges.sh` (seksjon 2)
- [x] **Tiltak 6:** Ekstraher `lib/sections/external_reference.sh` (seksjon 3)
- [x] **Tiltak 7:** Ekstraher `lib/sections/description.sh` (seksjon 4)
- [x] **Tiltak 8:** Ekstraher `lib/sections/quickstart.sh` (seksjon 5)
- [x] **Tiltak 9:** Ekstraher `lib/sections/example.sh` (seksjon 6)
- [x] **Tiltak 10:** Ekstraher `lib/sections/metadata.sh` (seksjon 7)
- [x] **Tiltak 11:** Ekstraher `lib/sections/publishing_info.sh` (seksjon 8)
- [x] **Tiltak 12:** Flytt `build_dependency_graph()` til `lib/sections/dependencies.sh` (seksjon 9)
- [x] **Tiltak 13:** Ekstraher `lib/sections/er_diagram.sh` (seksjon 10)
- [x] **Tiltak 14:** Ekstraher `lib/sections/classes.sh` (seksjon 11-15)
- [x] **Tiltak 15:** Ekstraher `lib/sections/artifacts.sh` (seksjon 16)
- [x] **Tiltak 16:** Ekstraher `lib/sections/validation.sh` (seksjon 17)
- [x] **Tiltak 17:** Ekstraher `lib/sections/changelog.sh` (seksjon 18)
- [x] **Tiltak 18:** Flytt `get_contact_info()` til `lib/sections/contact.sh` (seksjon 19)
- [x] **Tiltak 19:** Opprett `lib/copy_artifacts.sh` (filkopi-logikk)
- [x] **Tiltak 20:** Opprett `lib/generate_index.sh` (orkestreringsfunksjon)
- [x] **Tiltak 21:** Refactorer `publish.sh:process_schema()` til to funksjonskall
- [x] **Tiltak 22:** Oppdater `mkdocs/docs/index-md-struktur.md` med nye filreferansar
- [x] **Tiltak 23:** Test at `mkdocs/publish.sh` framleis fungerer korrekt (0 diff på genererte filer)

## Risiko og migreringsplan

### Risiko

- **Stor endring:** 390 linjer bash-kode skal refactorerast — risiko for regresjon
- **Parallell køyring:** `process_schema()` køyrer parallelt — source-statements må handterast rett
- **Bash-quirks:** Heredoc-logikk, set -e, lokale variablar kan oppføre seg ulikt i subscopes

### Migreringsplan

1. **Steg 1-3 (grunnmur):** Ekstraher hjelpefunksjonar (`formatters.sh`, `metadata_parsers.sh`) og test dei isolert
2. **Steg 4-10 (enkle seksjonar):** Ekstraher valfrie seksjonar som `description.sh`, `external_reference.sh` (få linjer, ingen kompleks logikk)
3. **Steg 11-17 (komplekse seksjonar):** Ekstraher badge-generering, valideringsresultat, artifacts-tabell (meir logikk, meir testing)
4. **Steg 18-20 (orkestrering):** Opprett `copy_artifacts.sh` og `generate_index.sh`, refactorer `process_schema()`
5. **Steg 21-23 (validering):** Test fullstendig bygg med `make docs-publish`, samanlikn output før/etter

### Rollback-plan

Lag ein git-branch for refactoreringa (`refactor/publish-process-schema`). Dersom noko bryt:

```bash
git checkout main
git branch -D refactor/publish-process-schema
```

## Alternativ: Python-basert generator

Dersom bash-refactoreringa viser seg for kompleks, vurder å skrive `generate_schema_index()`
som eit Python-script (`src/assets/scripts/generate-schema-index.py`) i staden:

**Fordeler:**
- Enklare testing (pytest)
- Enklare YAML/JSON-parsing (yaml.safe_load, json.load)
- Enklare strengmanipulering (f-strings, regex)
- Type hints og linting (mypy, ruff)

**Ulemper:**
- Må vedlikehalde både bash (filkopi) og Python (innhaldsgenerering)
- Ekstra avhengigheit (PyYAML, allereie installert)

## Relaterte filer

- **`mkdocs/publish.sh`** — hovudscript (linjer 216-611 skal refactorerast)
- **`mkdocs/docs/index-md-struktur.md`** — dokumentasjon av seksjonsstruktur
- **`src/assets/scripts/generate-validation-md.py`** — eksisterande Python-generator (seksjon 17)
- **`src/assets/scripts/parse-dependency-tree.py`** — eksisterande Python-generator (seksjon 9)

## Sjå også

- **Martin Fowler: Refactoring** — https://refactoring.com/
- **ShellCheck** — https://www.shellcheck.net/ (bash-linting)
- **Bash strict mode** — http://redsymbol.net/articles/unofficial-bash-strict-mode/

---

## Utført

Alle 23 tiltak er utførte. Refactoreringa er fullført med følgjande resultat:

### Ny filstruktur

```
mkdocs/
  publish.sh                             ← Redusert frå ~847 til ~402 linjer
  lib/
    copy_artifacts.sh                    ← 44 linjer (tidlegare linjer 224-257 i process_schema)
    generate_index.sh                    ← 39 linjer (orkestrering av index.md-generering)
    utils/
      formatters.sh                      ← 32 linjer (domain_label, artifact_label)
      metadata_parsers.sh                ← 30 linjer (get_validation_policy m.fl.)
    sections/
      header.sh                          ← 8 linjer (seksjon 1)
      badges.sh                          ← 60 linjer (seksjon 2)
      external_reference.sh              ← 16 linjer (seksjon 3)
      description.sh                     ← 13 linjer (seksjon 4)
      quickstart.sh                      ← 60 linjer (seksjon 5)
      example.sh                         ← 31 linjer (seksjon 6)
      metadata.sh                        ← 13 linjer (seksjon 7)
      publishing_info.sh                 ← 20 linjer (seksjon 8)
      dependencies.sh                    ← 50 linjer (seksjon 9)
      er_diagram.sh                      ← 28 linjer (seksjon 10)
      classes.sh                         ← 13 linjer (seksjon 11-15)
      artifacts.sh                       ← 63 linjer (seksjon 16)
      validation.sh                      ← 19 linjer (seksjon 17)
      changelog.sh                       ← 20 linjer (seksjon 18)
      contact.sh                         ← 77 linjer (seksjon 19)
```

### Nøkkelmetrikkar

- **Før:** `publish.sh` hadde 847 linjer, med `process_schema()` på 390 linjer
- **Etter:** `publish.sh` har 402 linjer (53% reduksjon), `process_schema()` har 15 linjer (96% reduksjon)
- **Nye filer:** 21 modular bash-filer i `lib/`-struktur (totalt ~600 linjer)
- **Testresultat:** 0 diff på alle genererte `index.md`-filer (identisk output)

### Fordeler oppnådd

1. **Testbarheit:** Kvar seksjonsgenerator kan testast isolert
2. **Vedlikehald:** Endring i éin seksjon krev berre endring i éin liten fil
3. **Gjenbruk:** Seksjonsgenererande funksjonar kan gjenbrukast i andre kontekstar
4. **Dokumentasjon:** Kvar fil i `lib/sections/` mappar direkte til ein rad i `index-md-struktur.md`
5. **Modularitet:** `process_schema()` redusert til to funksjonskall

### Dokumentasjon oppdatert

- `mkdocs/docs/index-md-struktur.md` oppdatert med nye filreferansar i "Script/funksjon"-kolonnen
- "Relaterte filer"-seksjonen utvida med alle nye lib-filer
