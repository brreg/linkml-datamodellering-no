# Fjern quickstart.md-filer og bruk dynamisk generering

## Bakgrunn

`kom_i_gang.sh` har to modus:
1. **Template-modus:** Les `src/linkml/<domain>/quickstart.md` og inject variablar
2. **Fallback-modus:** Generer standard "Kom i gang"-seksjon dynamisk (linje 124-160)

**Problem:**
- `quickstart.md`-filer per domene er ein ekstra fil å vedlikehalde
- Lite elegant — innhaldet er nesten identisk på tvers av domene
- Fallback-modus fungerer allereie utmerkt og genererer same innhald dynamisk

**Løysing:**
Fjern `quickstart.md`-filene og bruk berre den dynamiske genereringa (fallback-modus).

## Analyse

**Eksisterande quickstart.md-filer:**
- `src/linkml/ap-no/quickstart.md`
- `src/linkml/samt/quickstart.md`

**Innhald i quickstart.md:**
Begge filer har identisk struktur:
1. Importer i LinkML-skjema
2. Valider datafil (`validate-instance`)
3. Valider skjema (`mcp-validate`)
4. Python-bruk (`linkml-runtime`)

**Fallback-generering (kom_i_gang.sh linje 124-160):**
Genererer nøyaktig same struktur med auto-detekterte variablar:
- `{{SCHEMA}}` → schema-namn
- `{{VERSION_PATH}}` → versjon eller `main`
- `{{POLICY}}` → `bronze`/`silver`/`gold` frå `build.yaml`
- `{{EXAMPLE_CLASS}}` → auto-detektert frå skjema (Obligatorisk → Anbefalt → første klasse)
- `{{EXAMPLE_VAR}}` → generert frå `EXAMPLE_CLASS` (PascalCase → snake_case)

**Forskjell mellom template og fallback:**
- Template: må manuelt oppdaterast ved endring i struktur
- Fallback: auto-oppdaterast ved endring i `kom_i_gang.sh`

**Konklusjon:**
Fallback-modusen er meir robust og krev mindre vedlikehald. Template-modusen er overflødig.

## Løysingsforslag

### 1. Fjern template-modusen frå kom_i_gang.sh

Erstatt `generate_quickstart()`-funksjonen med berre den dynamiske genereringa:

```bash
generate_quickstart() {
    local domain="$1"
    local schema="$2"

    # Finn kjeldemappe for skjemaet
    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    # Les versjon frå skjemaet
    local version=""
    if [ -n "$schema_file" ]; then
        version=$(python3 -c "import yaml; d=yaml.safe_load(open('$schema_file')); print(d.get('version', ''))" 2>/dev/null || echo "")
    fi
    local version_tag="${version:+${schema}-v$version}"
    local version_path="${version_tag:-main}"

    # Auto-detekter EXAMPLE_CLASS, EXAMPLE_VAR og POLICY
    local example_class=""
    local example_var=""
    local policy="bronze"

    if [ -n "$schema_file" ]; then
        read -r example_class example_var policy < <(python3 - "$schema_file" <<'PYEOF'
# ... (same Python-script som no) ...
PYEOF
)
    fi

    # Fallback-verdiar
    example_class="${example_class:-Container}"
    example_var="${example_var:-container}"
    policy="${policy:-bronze}"

    # Generer standard struktur (fjerna if [ -f "$quickstart_file" ]-blokk)
    echo "## Kom i gang"
    echo ""
    echo "### Importer i LinkML-skjema"
    echo ""
    echo "\`\`\`yaml"
    echo "imports:"
    echo "  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/$version_path/src/linkml/$domain/$schema/$schema-schema.yaml"
    echo "\`\`\`"
    echo ""
    echo "### Valider skjemaet mot $policy-policy"
    echo ""
    echo "\`\`\`bash"
    echo "make mcp-validate SCHEMA=src/linkml/$domain/$schema/$schema-schema.yaml"
    echo "\`\`\`"
    echo ""
    echo "### Valider datafil mot LinkML-skjemaet"
    echo ""
    echo "\`\`\`bash"
    echo "make validate-instance SCHEMA=src/linkml/$domain/$schema/$schema-schema.yaml INSTANCE=mine-data.yaml"
    echo "\`\`\`"
    echo ""
    echo "### Python-bruk"
    echo ""
    echo "\`\`\`bash"
    echo "pip install linkml-runtime pyyaml"
    echo "\`\`\`"
    echo ""
    echo "\`\`\`python"
    echo "from linkml_runtime.loaders import yaml_loader"
    echo "from ${schema//-/_}_model import $example_class"
    echo ""
    echo "$example_var = yaml_loader.load('mine-data.yaml', target_class=$example_class)"
    echo "\`\`\`"
    echo ""
    echo ""
}
```

### 2. Fjern quickstart.md-filene

```bash
rm src/linkml/ap-no/quickstart.md
rm src/linkml/samt/quickstart.md
```

### 3. Oppdater CLAUDE.md (valfritt)

Dokumenter at "Kom i gang"-seksjonen vert generert dynamisk, ikkje frå template-filer.

## Fordeler

1. **Mindre vedlikehald:** Berre éin stad å oppdatere struktur (`kom_i_gang.sh`)
2. **Konsistens:** Alle skjema får same struktur automatisk
3. **Auto-deteksjon:** `EXAMPLE_CLASS`, `EXAMPLE_VAR` og `POLICY` vert auto-detekterte frå skjema
4. **Færre filer:** Ingen redundante template-filer

## Akseptansekriterium

1. ✅ `kom_i_gang.sh` genererer "Kom i gang"-seksjon dynamisk (utan å sjekke `quickstart.md`)
2. ✅ `quickstart.md`-filer er fjerna frå `src/linkml/ap-no/` og `src/linkml/samt/`
3. ✅ Eksisterande `index.md`-generering fungerer uendra
4. ✅ Auto-detekterte variablar (`EXAMPLE_CLASS`, `POLICY`) vert korrekt injisert

## Handlingsliste

- [x] Fjern `if [ -f "$quickstart_file" ]; then ... fi`-blokk frå `kom_i_gang.sh` (linje 112-123)
- [x] Fjern `local quickstart_file=...`-variabel (linje 9)
- [x] Fjern `src/linkml/ap-no/quickstart.md`
- [x] Fjern `src/linkml/samt/quickstart.md`
- [x] Test generering av `index.md` for eit ap-no-skjema (t.d. `dcat-ap-no`)
- [x] Test generering av `index.md` for eit samt-skjema
- [x] Verifiser at auto-detekterte verdiar er korrekte i generert output

## Utført

**Oppdatert `kom_i_gang.sh`:**
- Fjerna `local quickstart_file="$REPO_ROOT/src/linkml/$domain/quickstart.md"` (linje 9)
- Fjerna `if [ -f "$quickstart_file" ]; then ... fi`-blokk (linje 112-123)
- Brukar no berre dynamisk generering for alle skjema

**Fjerna quickstart.md-filer:**
- `src/linkml/ap-no/quickstart.md`
- `src/linkml/samt/quickstart.md`

**Verifisert auto-deteksjon:**
- **dcat-ap-no:** `EXAMPLE_CLASS=Aktoer`, `EXAMPLE_VAR=aktoer`, `POLICY=gold`, `VERSION_PATH=dcat-ap-no-v2.12.0`
- **samt-bu:** `EXAMPLE_CLASS=Skole`, `EXAMPLE_VAR=skole`, `POLICY=silver`, `VERSION_PATH=samt-bu-v1.8.0`

Alle skjema får no konsistent "Kom i gang"-seksjon generert dynamisk utan behov for vedlikehald av template-filer.
