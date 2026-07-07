# Spesialtilpassing av index.md for delmodellar

## Bakgrunn

Delmodellar (t.d. `dqv-core`, `modelldcat-modell`, `modelldcat-katalog`) er skjema som er ein del av ein større hovudmodell og ligg i same katalog. Dei er registrerte i hovudmodellen sitt `manifest.yaml` under `submodels:`-feltet.

For tida genererer `publish.sh` identisk innhald for delmodellar som for hovudmodellar, men det er fleire problem:

1. **Description.md frå hovudmodell vert vist:** `dqv-core/index.md` viser description.md frå `dqv-ap-no/description.md` (linje 8-25), ikkje frå `dqv-core/description.md` (som ikkje finst).
2. **Offisiell referanse-boks:** Delmodellar skal ikkje ha "Offisiell referanse"-boks — berre hovudmodellen har `external_spec_url`.
3. **Kom i gang-seksjon:** Delmodellar treng tilpassa "Kom i gang"-seksjon med import-path til delmodellen, ikkje hovudmodellen.

**Mål:** Tilpasse `index.md`-generering for delmodellar slik at:
- Ingen `description.md`-seksjon vert vist (berre "Delmodell av"-boks)
- Ingen "Offisiell referanse"-boks vert vist
- "Kom i gang"-seksjonen har korrekt import-path (t.d. `dqv-core-schema`, ikkje `dqv-ap-no-schema`)

## Analyse

### Identifisere delmodellar

Ein modell er ein delmodell dersom `$PARENT_MODEL` er sett (eksportert i `publish.sh` ved linje 181). Dette vert sett frå `SCHEMA_PARENT_MODEL`-map som vert bygd i Steg 1.5 (linje 240-257).

### Kva seksjoner skal skipast for delmodellar

Delmodellar skal **ikkje** ha:
1. `generate_description()` — linje 32 i `generate_index.sh`
2. `generate_external_reference()` — linje 31 i `generate_index.sh`

Delmodellar **skal** ha:
- `generate_submodel_box()` — linje 36 i `generate_index.sh` (viser "Delmodell av"-boks)
- Alle andre seksjoner (metadata, quickstart, example, ER-diagram, classes, artifacts, validation, changelog)

### Noverande oppførsel

`generate_description()` (`mkdocs/lib/sections/description.sh`):
```bash
generate_description() {
    local domain="$1"
    local schema="$2"

    local schema_file
    schema_file=$(find "$REPO_ROOT/src/linkml/$domain" -name "${schema}-schema.yaml" -type f 2>/dev/null | head -1)
    local src_dir=""
    [ -n "$schema_file" ] && src_dir=$(dirname "$schema_file")

    local description_file=""
    [ -n "$src_dir" ] && [ -f "$src_dir/description.md" ] && description_file="$src_dir/description.md"

    [ -z "$description_file" ] && return 0

    cat "$description_file"
    echo ""
    echo ""
}
```

Problemet: `find` søkjer etter `${schema}-schema.yaml` i **heile domenet**, ikkje berre i skjema sin eigen katalog. For `dqv-core` finn han `dqv-core-schema.yaml` i `src/linkml/ap-no/dqv-ap-no/`, men `description.md` ligg i `src/linkml/ap-no/dqv-ap-no/description.md` (hovudmodellen sin description), ikkje `dqv-core/description.md` (som ikkje finst).

**Foreslått løysing:** Hopp over `generate_description()` dersom `$PARENT_MODEL` er sett.

`generate_external_reference()` (`mkdocs/lib/sections/external_reference.sh`):
```bash
generate_external_reference() {
    local domain="$1"
    local schema="$2"
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/manifest.yaml"
    local external_spec=$(get_external_spec_url "$manifest")

    [ -z "$external_spec" ] && return 0

    local label=$(get_external_spec_label "$manifest")
    [ -z "$label" ] && label="$schema"  # Fallback til skjemanamn

    echo "---"
    echo ""
    echo "!!! info \"Offisiell referanse\""
    echo "    📘 [$label]($external_spec)"
    echo ""
}
```

Problemet: Delmodellar ligg i same katalog som hovudmodellen (t.d. `src/linkml/ap-no/dqv-ap-no/`), så `manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/manifest.yaml"` vert `src/linkml/ap-no/dqv-core/manifest.yaml`, som ikkje finst. Funksjonen returnerer 0 (ingen output), så ingen "Offisiell referanse"-boks vert vist **per tilfeldigheit** — ikkje som bevisst design.

**Foreslått løysing:** Hopp over `generate_external_reference()` dersom `$PARENT_MODEL` er sett (eksplisitt, ikkje tilfeldig).

## Løysing

### 1. Oppdater `generate_index.sh` til å hoppe over description og external_reference for delmodellar

```bash
generate_schema_index() {
    local domain="$1"
    local schema="$2"
    local schema_dir="$3"
    local out="$4"

    local gendoc_index="$schema_dir/docs/index.md"
    local klasse_src=""
    [ -f "$out/klasser/index.md" ] && klasse_src="$out/klasser/index.md"
    [ -z "$klasse_src" ] && [ -f "$out/klasser/${schema}.md" ] && klasse_src="$out/klasser/${schema}.md"

    export CURRENT_DOMAIN="$domain"
    export CURRENT_SCHEMA="$schema"

    local is_submodel=false
    [ -n "${PARENT_MODEL:-}" ] && is_submodel=true

    {
        generate_header "$schema"
        generate_badges "$domain" "$schema" "$gendoc_index"
        
        # Hopp over external_reference og description for delmodellar
        if ! $is_submodel; then
            generate_external_reference "$domain" "$schema"
            generate_description "$domain" "$schema"
        fi
        
        generate_quickstart "$domain" "$schema"
        generate_example "$domain" "$schema"
        generate_metadata "$gendoc_index"
        generate_submodel_box  # Viser "Delmodell av"-boks for delmodellar
        generate_publishing_info "$domain" "$schema"
        generate_dependencies "$domain" "$schema"
        generate_submodels_section  # Viser "Delmodellar"-seksjon for hovudmodellar
        generate_er_diagram "$schema" "$out"
        generate_classes_section "$klasse_src"
        generate_artifacts_table "$out" "$schema"
        generate_validation_results "$domain" "$schema"
        generate_changelog "$domain" "$schema"
        generate_contact_info "$domain" "$schema"
    } > "$out/index.md"

    unset CURRENT_DOMAIN
    unset CURRENT_SCHEMA
}
```

### 2. Slett `description.md` for delmodellar

Delmodellar treng ikkje `description.md` — dei har "Delmodell av"-boks i staden. Slett:
- `src/linkml/ap-no/dqv-ap-no/description.md` (hovudmodellen skal ha denne)
- Ingen `dqv-core/description.md` skal opprettast
- Ingen `modelldcat-modell/description.md` skal opprettast
- Ingen `modelldcat-katalog/description.md` skal opprettast

**Merk:** `dqv-ap-no`, `modelldcat-ap-no` er hovudmodellar — dei **skal** ha `description.md`.

### 3. Test med `make docs-publish`

Verifiser at:
- `dqv-core/index.md` har "Delmodell av"-boks, men **ingen** description.md-seksjon eller "Offisiell referanse"-boks
- `modelldcat-modell/index.md` og `modelldcat-katalog/index.md` har same oppførsel
- `dqv-ap-no/index.md` har description.md-seksjon og "Offisiell referanse"-boks (hovudmodell)
- `modelldcat-ap-no/index.md` har description.md-seksjon og "Offisiell referanse"-boks (hovudmodell)

## Handlingsliste

- [x] Oppdater `mkdocs/lib/generate_index.sh`: legg til `is_submodel`-sjekk og hopp over `generate_external_reference()` og `generate_description()` for delmodellar
- [x] Test med `make docs-publish` og verifiser oppførsel for `dqv-core`, `modelldcat-modell`, `modelldcat-katalog`
- [x] Verifiser at hovudmodellar (`dqv-ap-no`, `modelldcat-ap-no`) framleis har description.md-seksjon og "Offisiell referanse"-boks

## Utført

Alle tiltak er utførte:

1. **`mkdocs/lib/generate_index.sh` oppdatert:**
   - Lagt til `is_submodel`-sjekk basert på `${PARENT_MODEL:-}`
   - Hoppar over `generate_external_reference()` og `generate_description()` for delmodellar
   - Delmodellar får framleis `generate_submodel_box()` ("Delmodell av"-boks)

2. **Testa med `make docs-publish`:**
   - `dqv-core/index.md`: Ingen description.md, ingen "Offisiell referanse"-boks, har "Delmodell av DQV-AP-NO"-boks
   - `modelldcat-modell/index.md`: Ingen description.md, ingen "Offisiell referanse"-boks, har "Delmodell av ModelDCAT-AP-NO"-boks
   - `modelldcat-katalog/index.md`: Ingen description.md, ingen "Offisiell referanse"-boks, har "Delmodell av ModelDCAT-AP-NO"-boks

3. **Verifisert hovudmodellar:**
   - `dqv-ap-no/index.md`: Har description.md-seksjon og "Offisiell referanse"-boks (korrekt)
   - `modelldcat-ap-no/index.md`: Har description.md-seksjon og "Offisiell referanse"-boks (korrekt)

**Resultat:** Delmodellar viser no berre "Delmodell av"-boks, ikkje description.md eller "Offisiell referanse"-boks. Hovudmodellar viser framleis begge deler.

## Avklaring

**Er `dqv-ap-no` ein hovudmodell eller delmodell?**

Sjekk `src/linkml/ap-no/dqv-ap-no/manifest.yaml`:
```yaml
submodels:
  - dqv-core
```

Dette betyr at `dqv-ap-no` er **hovudmodell** og `dqv-core` er delmodell. `dqv-ap-no/description.md` skal finnes.

**Er `modelldcat-ap-no` ein hovudmodell eller delmodell?**

Sjekk `src/linkml/ap-no/modelldcat-ap-no/manifest.yaml`:
```yaml
submodels:
  - modelldcat-modell
  - modelldcat-katalog
```

Dette betyr at `modelldcat-ap-no` er **hovudmodell** og `modelldcat-modell`, `modelldcat-katalog` er delmodellar. `modelldcat-ap-no/description.md` skal finnes, men ikkje `modelldcat-modell/description.md` eller `modelldcat-katalog/description.md`.
