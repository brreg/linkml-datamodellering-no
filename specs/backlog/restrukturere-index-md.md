# Restrukturere index.md-generering — bruk gen-doc sin output i publish.sh

## Bakgrunn

`index.md` vert generert på to ulike måtar:

1. **`gen-doc`** (via Jinja-template `index.md.jinja2`):
   - Genererer `generated/<domain>/<modell>/docs/index.md`
   - Inneheld: Tittel, Beskrivelse, **`## Metadata`**, `## Classes`, `## Slots`, osv.
   - Strukturert og konsistent basert på LinkML-skjemaet

2. **`publish.sh`** (bash-script):
   - **Overstyrer heilt** `gen-doc` sin output ved å bygge ny `index.md` frå scratch
   - Injiserer: ER-diagram, `description.md`, klasseliste, **`## Valideringsresultat`**, artefaktabell
   - **Metadata-seksjonen frå `gen-doc` vert ikkje brukt**

**Problem:**

Brukaren ønskjer følgjande struktur i `index.md`:

1. `## Versjonslog` (kollapsa `<details>` med CHANGELOG.md)
2. `## Valideringsresultat`
3. `## Metadata`
4. `## Classes` / `## Slots` / osv.

Men sidan `publish.sh` overskriver heile `index.md`, må me **enten**:
- A) Injisere Metadata-seksjonen i `publish.sh` (duplikert logikk)
- B) Bruke `gen-doc` sin `index.md` som base og **injisere** ekstra seksjonar (Valideringsresultat, CHANGELOG) i staden for å overskrive

**Anbefalt løysing:** Alternativ B — bruk `gen-doc` sin output som base.

## Foreslått løysing

### Ny struktur i `publish.sh`:

1. `gen-doc` genererer `generated/<domain>/<modell>/docs/index.md` med:
   - Tittel + beskrivelse
   - `## Versjonslog` (placeholder: `<!-- CHANGELOG_PLACEHOLDER -->`)
   - `## Valideringsresultat` (placeholder: `<!-- VALIDATION_PLACEHOLDER -->`)
   - `## Metadata`
   - `## Classes`, `## Slots`, osv.

2. `publish.sh` **post-prosesserer** `index.md` i staden for å overskrive:
   - Injiserer CHANGELOG.md-innhald i `<!-- CHANGELOG_PLACEHOLDER -->`
   - Injiserer valideringsresultat i `<!-- VALIDATION_PLACEHOLDER -->`
   - Injiserer ER-diagram **før** `## Versjonslog` (eller etter beskrivelse)
   - Injiserer `description.md` rett etter beskrivelse (dersom ulik frå `schema.description`)

### Alternativ: Hybrid-tilnærming

**`gen-doc`** genererer:
- `## Versjonslog` (placeholder)
- `## Metadata`
- `## Classes`, `## Slots`, osv.

**`publish.sh`** injiserer **før** `## Metadata`:
- ER-diagram
- `description.md`
- `## Valideringsresultat` (via placeholder eller direkte injeksjon)

## Implementasjon

### Steg 1: Oppdater Jinja-template til å inkludere placeholders

**Fil:** `src/assets/templates/docgen/index.md.jinja2`

```jinja2
# {% if schema.title %}{{ schema.title }}{% else %}{{ schema.name }}{% endif %}

{% if schema.description %}{{ schema.description }}{% endif %}

<!-- ERDIAGRAM_PLACEHOLDER -->

<!-- DESCRIPTION_MD_PLACEHOLDER -->

## Versjonslog

<details>
<summary>Vis full endringshistorikk</summary>

<!-- CHANGELOG_PLACEHOLDER -->

</details>

## Valideringsresultat

<!-- VALIDATION_PLACEHOLDER -->

## Metadata

| Felt | Verdi |
| --- | --- |
{% if schema.id -%}
| Schema URI | [{{ schema.id }}]({{ schema.id }}) |
{% endif -%}
...
```

### Steg 2: Oppdater `publish.sh` til å post-prosessere i staden for å overskrive

**Fil:** `mkdocs/publish.sh`

Erstatt heile `index.md`-generering-blokka (linje 136–244) med post-prosessering:

```bash
# Post-prosesser generated/<domain>/<schema>/docs/index.md
index_src="$out/docs/index.md"
index_dst="$DOCS/$domain/$schema/index.md"

# Kopier gen-doc sin index.md som base
cp "$index_src" "$index_dst"

# 1. Injiser ER-diagram
erdiagram_file="$out/${schema}-erdiagram.md"
if [ -f "$erdiagram_file" ] && grep -q '{' "$erdiagram_file" 2>/dev/null; then
    erdiagram_content=$(awk 'NR==1 && /^# / { next } 1' "$erdiagram_file")
    # Erstatt <!-- ERDIAGRAM_PLACEHOLDER --> med diagram-innhald
    awk -v diagram="$erdiagram_content" '
        /<!-- ERDIAGRAM_PLACEHOLDER -->/ { print diagram; next }
        { print }
    ' "$index_dst" > "$index_dst.tmp"
    mv "$index_dst.tmp" "$index_dst"
fi

# 2. Injiser description.md (dersom ulik frå schema.description)
schema_desc="$REPO_ROOT/src/linkml/$domain/$schema/description.md"
if [ -f "$schema_desc" ]; then
    desc_content=$(cat "$schema_desc")
    awk -v desc="$desc_content" '
        /<!-- DESCRIPTION_MD_PLACEHOLDER -->/ { print desc; next }
        { print }
    ' "$index_dst" > "$index_dst.tmp"
    mv "$index_dst.tmp" "$index_dst"
fi

# 3. Injiser CHANGELOG.md (via inject-changelog-in-index.py)
$(PYTHON_RUN) python3 src/assets/scripts/inject-changelog-in-index.py \
    "$index_dst" \
    "$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"

# 4. Injiser valideringsresultat
validation_json="..."  # (same logikk som tidlegare)
if [ -f "$validation_json" ]; then
    validation_content=$(python3 "$REPO_ROOT/src/assets/scripts/generate-validation-md.py" "$validation_json")
    # Fjern "## Valideringsresultat" frå generate-validation-md.py sin output
    validation_content=$(echo "$validation_content" | sed '/^## Valideringsresultat$/d')
    
    awk -v validation="$validation_content" '
        /<!-- VALIDATION_PLACEHOLDER -->/ { print validation; next }
        { print }
    ' "$index_dst" > "$index_dst.tmp"
    mv "$index_dst.tmp" "$index_dst"
else
    # Fjern placeholder dersom ingen validering
    sed -i '/<!-- VALIDATION_PLACEHOLDER -->/d' "$index_dst"
fi

# 5. Fjern eventuelle gjenverande placeholders
sed -i '/<!-- .*_PLACEHOLDER -->/d' "$index_dst"
```

### Steg 3: Oppdater `generate-validation-md.py` til å ikkje inkludere overskrift

**Fil:** `src/assets/scripts/generate-validation-md.py`

Legg til `--no-header`-flag:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("validation_json", type=Path)
parser.add_argument("--no-header", action="store_true", help="Skip ## Valideringsresultat header")
args = parser.parse_args()

...

lines = []
if not args.no_header:
    lines += ["", "## Valideringsresultat", ""]
lines += [
    f"*Siste validering: {validated_at} — v{version}*",
    "",
    "| Status | Feil | Åtvaringar |",
    ...
]
```

Eller: bruk eksisterande script utan overskrift, og legg overskrifta til i templaten.

## Fordeler

- **Konsistent struktur:** Metadata-seksjonen vert generert éin stad (`gen-doc`)
- **Enklare vedlikehald:** Mindre duplikert logikk
- **Meir fleksibel:** Enklare å endre rekkjefølgja på seksjonar
- **Gjenbruk av gen-doc sin output:** Utnyttar LinkML sin innebygde dokumentasjonsgenerator

## Ulemper

- **Meir kompleks post-prosessering:** Fleire `awk`/`sed`-operasjonar i `publish.sh`
- **Avhengig av placeholder-konvensjon:** Placeholders må vere unike og konsistente

## Alternativ: Minst mogleg endring

Dersom me **ikkje** vil endre `publish.sh` sin grunnstruktur, kan me i staden:

1. Legg til `## Metadata`-generering direkte i `publish.sh` (duplikat av `index.md.jinja2` sin logikk)
2. Flytt `## Valideringsresultat` til **før** `## Metadata` i `publish.sh`
3. Legg til `## Versjonslog` heilt i starten

**Ulempe:** Duplikert logikk — Metadata-tabellen må genererast både i Jinja-template og i `publish.sh`.

## Anbefaling

**Fase 1 (rask løysing):** Bruk Alternativ — legg til Metadata-generering i `publish.sh` og flytt Valideringsresultat.

**Fase 2 (refaktorering):** Gå over til placeholder-basert tilnærming for betre vedlikehald.

---

## Steg for Fase 1 (rask løysing)

### 1. Legg til Metadata-generering i `publish.sh`

Rett etter `description.md`-injeksjon, legg til Metadata-tabell:

```bash
# Generer Metadata-tabell frå schema.yaml
echo ""
echo "## Versjonslog"
echo ""
echo "<details>"
echo "<summary>Vis full endringshistorikk</summary>"
echo ""
echo "<!-- CHANGELOG_PLACEHOLDER -->"
echo ""
echo "</details>"
echo ""

# Valideringsresultat (flyttet hit)
if [ -f "$validation_json" ]; then
    python3 "$REPO_ROOT/src/assets/scripts/generate-validation-md.py" "$validation_json"
else
    echo "## Valideringsresultat"
    echo ""
    echo "*Valideringsresultat ikkje tilgjengeleg — ingen validering enno.*"
fi
echo ""

# Metadata-tabell
echo "## Metadata"
echo ""
echo "| Felt | Verdi |"
echo "| --- | --- |"

# Les schema.yaml og ekstraher metadata
schema_yaml="$REPO_ROOT/src/linkml/$domain/$schema/${schema}-schema.yaml"
python3 - "$schema_yaml" << 'PYEOF'
import sys, yaml

schema_path = sys.argv[1]
with open(schema_path, encoding="utf-8") as f:
    schema = yaml.safe_load(f)

# Schema URI
if schema.get("id"):
    uri = schema["id"]
    print(f"| Schema URI | [{uri}]({uri}) |")

# Versjon
if schema.get("version"):
    print(f"| Versjon | {schema['version']} |")

# Lisens
if schema.get("license"):
    lic = schema["license"]
    print(f"| Lisens | [{lic}]({lic}) |")

# Utgjevar
if schema.get("annotations", {}).get("utgiver"):
    utgiver = schema["annotations"]["utgiver"]["value"]
    print(f"| Utgjevar | [{utgiver}]({utgiver}) |")

# Status
if schema.get("annotations", {}).get("status"):
    status = schema["annotations"]["status"]["value"]
    print(f"| Status | {status} |")

# Endringsdato
if schema.get("annotations", {}).get("endringsdato"):
    dato = schema["annotations"]["endringsdato"]["value"]
    print(f"| Endringsdato | {dato} |")

# Utgivelsesdato
if schema.get("annotations", {}).get("utgivelsesdato"):
    dato = schema["annotations"]["utgivelsesdato"]["value"]
    print(f"| Utgivelsesdato | {dato} |")

# Imports
if schema.get("imports"):
    imports_html = "<br>".join(schema["imports"])
    print(f"| Imports | {imports_html} |")
PYEOF
```

### 2. Post-prosesser for å injisere CHANGELOG.md

```bash
# Erstatt <!-- CHANGELOG_PLACEHOLDER --> med CHANGELOG.md-innhald
changelog_src="$REPO_ROOT/src/linkml/$domain/$schema/CHANGELOG.md"
if [ -f "$changelog_src" ]; then
    # Les CHANGELOG og fjern hovudoverskrift
    changelog_content=$(tail -n +2 "$changelog_src")
    
    awk -v changelog="$changelog_content" '
        /<!-- CHANGELOG_PLACEHOLDER -->/ { print changelog; next }
        { print }
    ' "$out/index.md" > "$out/index.md.tmp"
    mv "$out/index.md.tmp" "$out/index.md"
else
    # Fjern heile ## Versjonslog-seksjon
    sed -i '/^## Versjonslog$/,/^## Valideringsresultat$/{/^## Versjonslog$/d; /^## Valideringsresultat$/!d;}' "$out/index.md"
fi
```

---

## Neste steg

1. Bestem kva tilnærming me vil bruke (Fase 1 rask vs. Fase 2 refaktorering)
2. Implementer endringane i `publish.sh`
3. Test med ein modell som har CHANGELOG.md og valideringsresultat
4. Verifiser at strukturen er: Versjonslog → Valideringsresultat → Metadata → Classes
