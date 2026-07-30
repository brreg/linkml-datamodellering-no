# Standardiser "Kom i gang"-seksjon i index.md

## Bakgrunn

Alle modellars `index.md`-sider skal ha ein konsistent "Kom i gang"-seksjon med tre faste deloverskrifter:
1. **Importer i LinkML-skjema** — viser korleis ein importerer modellen i eigne LinkML-skjema
2. **Valider datafil** — viser korleis ein validerer ei datafil mot modellen
3. **Python-bruk** — viser korleis ein brukar modellen frå Python

Per i dag genererer `mkdocs/lib/sections/kom_i_gang.sh` ulik innhald basert på:
- Om det finst ein `src/linkml/<domain>/quickstart.md`-fil (brukt for `ap-no` og `samt`)
- Om domenet er `ap-no` eller `fair` (fallback: metadatamodell-quickstart)
- Om det finst ei eksempeldatafil (fallback: domenemodell-quickstart)

Dette gir inkonsistent struktur:
- AP-NO har tre deloverskrifter: "Importer", "Python-bruk", "Valider data mot SHACL"
- SAMT har éin deloverskrift: "Valider eiga datafil"
- Andre modellar får automatisk genererte fallback-varianter

**Mål:** Alle modellar skal ha same struktur med tre faste deloverskrifter, uavhengig av domene eller skjematype.

## Endringar

### 1. Oppdater `kom_i_gang.sh` til å generere standardstruktur

**Fil:** `mkdocs/lib/sections/kom_i_gang.sh`

**Ny logikk:**
- Sjekk først om det finst `src/linkml/<domain>/quickstart.md` → bruk den (med variabel-substitusjon)
- Elles: generer standard tre-delar-struktur basert på skjematype (metadatamodell vs domenemodell)

**Standard tre-delar-struktur:**

**Standard tre-delar-struktur (same for alle modellar):**

```markdown
## Kom i gang

### Importer i LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/{{VERSION_PATH}}/src/linkml/{{DOMAIN}}/{{SCHEMA}}/{{SCHEMA}}-schema.yaml
```

### Valider datafil

Valider datafil mot LinkML-skjemaet:

```bash
make validate-instance SCHEMA=src/linkml/{{DOMAIN}}/{{SCHEMA}}/{{SCHEMA}}-schema.yaml INSTANCE=mine-data.yaml
```

Valider skjemaet mot {{POLICY}}-policy:

```bash
make mcp-validate SCHEMA=src/linkml/{{DOMAIN}}/{{SCHEMA}}/{{SCHEMA}}-schema.yaml
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from {{SCHEMA_UNDERSCORE}}_model import {{EXAMPLE_CLASS}}

{{EXAMPLE_VAR}} = yaml_loader.load('mine-data.yaml', target_class={{EXAMPLE_CLASS}})
```
```

**Variabel-substitusjon:**
- `{{SCHEMA}}` → skjemanamn (t.d. `dcat-ap-no-schema`)
- `{{SCHEMA_UNDERSCORE}}` → skjemanamn med understrek i staden for bindestrek (t.d. `dcat_ap_no_schema`)
- `{{VERSION_PATH}}` → versjonsnummer eller `main` (t.d. `dcat-ap-no-schema-v2.0.0` eller `main`)
- `{{DOMAIN}}` → domenenamn (t.d. `ap-no`, `samt`, `ngr`)
- `{{EXAMPLE_CLASS}}` → representativ klasse frå modellen (auto-detektert eller frå quickstart.md)
- `{{EXAMPLE_VAR}}` → variabelnamn i lowercase (t.d. `datasett`, `adresse`, `aktoer`)
- `{{POLICY}}` → validation_policy frå `build.yaml` (t.d. `bronze`, `silver`, `gold`, `felles-datakatalog`, `felles-begrepskatalog`)

**Auto-deteksjon av `{{EXAMPLE_CLASS}}`, `{{EXAMPLE_VAR}}` og `{{POLICY}}`:**

Dersom `quickstart.md` ikkje finst, skal `kom_i_gang.sh` automatisk detektere:

1. **Representativ klasse** basert på prioritering:
   - **Prioritet 1:** Første klasse i `Obligatorisk`-subset (mest sentral klasse)
   - **Prioritet 2:** Første klasse i `Anbefalt`-subset
   - **Prioritet 3:** Første ikkje-abstrakt, ikkje-containerklasse i skjemaet

2. **Validation policy** frå `build.yaml` (`validation_policy`-feltet)

Python-logikk for auto-deteksjon:
```python
import yaml

# Les skjema
with open(schema_file) as f:
    schema = yaml.safe_load(f)

# Les build.yaml for validation_policy
build_file = os.path.join(os.path.dirname(schema_file), 'build.yaml')
policy = 'bronze'  # default
if os.path.exists(build_file):
    with open(build_file) as f:
        build_config = yaml.safe_load(f)
        policy = build_config.get('validation_policy', 'bronze')

# Finn container-klassenamn
container_class = None
for cls_name, cls_def in schema.get('classes', {}).items():
    if cls_def.get('tree_root'):
        container_class = cls_name
        break

# Finn representativ klasse
example_class = None

# Prioritet 1: Obligatorisk subset
for cls_name, cls_def in schema.get('classes', {}).items():
    if cls_name == container_class:
        continue
    if 'Obligatorisk' in cls_def.get('in_subset', []):
        example_class = cls_name
        break

# Prioritet 2: Anbefalt subset
if not example_class:
    for cls_name, cls_def in schema.get('classes', {}).items():
        if cls_name == container_class:
            continue
        if 'Anbefalt' in cls_def.get('in_subset', []):
            example_class = cls_name
            break

# Prioritet 3: Første ikkje-container-klasse
if not example_class:
    for cls_name, cls_def in schema.get('classes', {}).items():
        if cls_name == container_class:
            continue
        if not cls_def.get('abstract'):
            example_class = cls_name
            break

# Fallback til containerklassen
if not example_class:
    example_class = container_class or "Container"

# Generer variabelnamn (lowercase, konverter PascalCase til snake_case)
import re
example_var = re.sub('([a-z0-9])([A-Z])', r'\1_\2', example_class).lower()
```

### 2. Oppdater eksisterande `quickstart.md`-filer

**Fil:** `src/linkml/ap-no/quickstart.md`

Oppdater til standard tre-delar-struktur med placeholders for auto-deteksjon:

```markdown
## Kom i gang

### Importer i LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/{{VERSION_PATH}}/src/linkml/ap-no/{{SCHEMA}}/{{SCHEMA}}-schema.yaml
```

### Valider datafil

Valider datafil mot LinkML-skjemaet:

```bash
make validate-instance SCHEMA=src/linkml/ap-no/{{SCHEMA}}/{{SCHEMA}}-schema.yaml INSTANCE=mine-data.yaml
```

Valider skjemaet mot {{POLICY}}-policy:

```bash
make mcp-validate SCHEMA=src/linkml/ap-no/{{SCHEMA}}/{{SCHEMA}}-schema.yaml
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from {{SCHEMA_UNDERSCORE}}_model import {{EXAMPLE_CLASS}}

{{EXAMPLE_VAR}} = yaml_loader.load('mine-data.yaml', target_class={{EXAMPLE_CLASS}})
```
```

**Merk:** `{{EXAMPLE_CLASS}}`, `{{EXAMPLE_VAR}}` og `{{POLICY}}` vert auto-detekterte av `kom_i_gang.sh` basert på faktisk skjema.

**Fil:** `src/linkml/samt/quickstart.md`

Oppdater til standard tre-delar-struktur med placeholders for auto-deteksjon:

```markdown
## Kom i gang

### Importer i LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/{{VERSION_PATH}}/src/linkml/samt/{{SCHEMA}}/{{SCHEMA}}-schema.yaml
```

### Valider datafil

Valider datafil mot LinkML-skjemaet:

```bash
make validate-instance SCHEMA=src/linkml/samt/{{SCHEMA}}/{{SCHEMA}}-schema.yaml INSTANCE=mine-data.yaml
```

Valider skjemaet mot {{POLICY}}-policy:

```bash
make mcp-validate SCHEMA=src/linkml/samt/{{SCHEMA}}/{{SCHEMA}}-schema.yaml
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from {{SCHEMA_UNDERSCORE}}_model import {{EXAMPLE_CLASS}}

{{EXAMPLE_VAR}} = yaml_loader.load('mine-data.yaml', target_class={{EXAMPLE_CLASS}})
```
```

**Merk:** `{{EXAMPLE_CLASS}}`, `{{EXAMPLE_VAR}}` og `{{POLICY}}` vert auto-detekterte av `kom_i_gang.sh` basert på faktisk skjema.

### 3. Test generering

**Køyr:** `make docs-publish`

**Verifiser i genererte `mkdocs/docs/<domain>/<schema>/index.md`:**
- Alle modellar har `## Kom i gang`-seksjon
- Alle har tre deloverskrifter: "Importer i LinkML-skjema", "Valider datafil", "Python-bruk"
- Variabelsubstitusjon fungerer (`{{SCHEMA}}` → faktisk skjemanamn osv.)

## Handlingsliste

- [x] Oppdater `mkdocs/lib/sections/kom_i_gang.sh` med:
  - Standard tre-delar-struktur (Importer, Valider datafil, Python-bruk)
  - Auto-deteksjon av `{{EXAMPLE_CLASS}}` basert på subset-prioritering (Obligatorisk → Anbefalt → første ikkje-container-klasse)
  - Auto-deteksjon av `{{POLICY}}` frå `build.yaml` (`validation_policy`-feltet)
  - Variabel-substitusjon for `{{EXAMPLE_CLASS}}`, `{{EXAMPLE_VAR}}` og `{{POLICY}}`
  - "Valider datafil"-seksjon skal innehalde både `make validate-instance` og `make mcp-validate`
- [x] Oppdater `src/linkml/ap-no/quickstart.md` med:
  - Standard tre-delar-struktur
  - `make validate-instance` og `make mcp-validate` i staden for `pyshacl`
  - `{{EXAMPLE_CLASS}}`, `{{EXAMPLE_VAR}}` og `{{POLICY}}` placeholders i staden for hardkoda verdiar
- [x] Oppdater `src/linkml/samt/quickstart.md` med:
  - Standard tre-delar-struktur
  - `make validate-instance` og `make mcp-validate` i "Valider datafil"-seksjonen
  - `{{EXAMPLE_CLASS}}`, `{{EXAMPLE_VAR}}` og `{{POLICY}}` placeholders for auto-deteksjon
- [x] Test med `make docs-publish`
- [x] Verifiser genererte `index.md`-filer for:
  - `dcat-ap-no` → `Aktoer` som eksempelklasse (auto-detektert), `gold` som policy ✅
  - `modelldcat-ap-no` → `Container` som eksempelklasse (containerklassen), `gold` som policy ⚠️
  - `samt-bu` → `Skole` som eksempelklasse (Obligatorisk-subset), auto-detektert policy ✅
  - `ngr-adresse` → `OffisiellAdresse` som eksempelklasse (auto-detektert), `felles-datakatalog` som policy ✅

## Utført

**Dato:** 2026-07-30

**Endringar:**
- `mkdocs/lib/sections/kom_i_gang.sh` — ny `generate_quickstart()`-funksjon med auto-deteksjon og standard tre-delar-struktur
- `src/linkml/ap-no/quickstart.md` — oppdatert med `make validate-instance`, `make mcp-validate` og placeholders
- `src/linkml/samt/quickstart.md` — oppdatert med full tre-delar-struktur og placeholders

**Verifikasjonsresultat:**

Alle modellar har no konsistent "Kom i gang"-seksjon med tre faste deloverskrifter:
1. Importer i LinkML-skjema
2. Valider datafil (med både `make validate-instance` og `make mcp-validate`)
3. Python-bruk

**Auto-deteksjon:**
- ✅ Policy-deteksjon fungerer perfekt (`gold`, `silver`, `felles-datakatalog` osv.)
- ✅ Eksempelklasse-deteksjon fungerer, men ikkje alltid optimalt:
  - Modellar med Obligatorisk-subset på klassenivå (`samt-bu` → `Skole`) fungerer perfekt
  - Modellar utan Obligatorisk-subset på klassenivå (`dcat-ap-no`, `modelldcat-ap-no`) fell tilbake til første ikkje-container-klasse, som kan vere suboptimalt (t.d. `Aktoer` i staden for `Datasett`, `Container` i staden for `Katalog`)

**Kjende begrensingar:**
- AP-NO-modellar brukar `Metadata`-subset i staden for `Obligatorisk`-subset på klassenivå, så auto-deteksjon finn ikkje alltid den mest representative klassen
- Containerklassen kan bli vald dersom ingen andre klasser finst (t.d. `modelldcat-ap-no` → `Container`)

**Løysingsforslag:**
Dersom auto-deteksjon ikkje gir ønska eksempelklasse, kan ein legge til ein dedikert `quickstart.md`-fil i domenet med hardkoda `{{EXAMPLE_CLASS}}` (t.d. `Datasett` for `dcat-ap-no`, `Katalog` for `modelldcat-ap-no`).
