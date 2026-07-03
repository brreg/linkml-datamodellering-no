# Vis metadata på modellens index.md-side

## Bakgrunn

Kvar LinkML-modell har ei `generated/<domain>/<modell>/docs/index.md`-fil som fungerer som hovudside i dokumentasjonsportalen. Denne sida inneheld no:
- Tittel og skildring
- Klassar
- Slots
- Enums
- Typar

**Problem:**
Viktig metadata om modellen (versjon, lisensar, utgjevar, status, osv.) er ikkje synleg på hovudsida. Brukarar må lese sjølve `<modell>-schema.yaml`-fila for å finne denne informasjonen.

**Motivasjon:**
Metadata som versjon, lisens, utgjevar og status er kritisk for å vurdere om ein modell kan brukast i eit system. Dette bør vere synleg på hovudsida, rett over valideringsresultata.

## Foreslått løysing

Legg til ein **Metadata-seksjon** i `index.md` rett over "Valideringsresultat", som viser:
- **URI / Schema ID:** `schema.id`
- **Versjon:** `schema.version`
- **Lisens:** `schema.license`
- **Utgjevar:** `schema.annotations.utgiver` (dersom silver+)
- **Status:** `schema.annotations.status` (dersom silver+)
- **Endrings-/utgivelsesdato:** `schema.annotations.endringsdato` / `utgivelsesdato`
- **Validation policy:** frå `manifest.yaml`
- **Imports:** `schema.imports` (viser avhengigheiter)

**Plassering:**
```markdown
# <Modell tittel>

<Beskrivelse>

## Metadata

| Felt | Verdi |
|---|---|
| Schema URI | https://data.norge.no/... |
| Versjon | 1.0.0 |
| Lisens | https://data.norge.no/nlod/no/2.0 |
| Utgjevar | https://data.norge.no/organizations/123456789 |
| Status | Ferdigstilt |
| Validation policy | silver |
| Imports | dcat-ap-no, skos-ap-no |

## Valideringsresultat

...
```

## Implementasjon

### Alternativ A: Jinja2-template i gen-doc (anbefalt)

LinkML `gen-doc` brukar Jinja2-templates i `src/assets/templates/docgen/`. Me kan lage ein eigen template for metadata-seksjonen.

**Steg:**
1. Lag `src/assets/templates/docgen/metadata.md.jinja2`
2. Injiser metadata i `index.md.jinja2` (eller post-prosesser `index.md`)
3. Pass metadata-variablar via `gen-doc` (dersom muleg)

**Problem:** `gen-doc` har ikkje innebygd støtte for å passe metadata frå manifest.yaml eller annotations.

### Alternativ B: Post-prosessering av index.md (enklaste)

**Steg:**
1. Lag Python-script `src/assets/scripts/inject-metadata-in-index.py`
2. Scriptet les `<modell>-schema.yaml` og `manifest.yaml`
3. Ekstraher metadata og generer Markdown-tabell
4. Injiser tabellen rett **før** `## Valideringsresultat` (eller etter hovudskildring)
5. Køyr scriptet i `run_gen_doc` etter `gen-doc` og før `sed -i '/Container/d'`

**Makefile-endring:**
```makefile
define run_gen_doc
@$(foreach s,$(1), \
  ...
  $(LINKML_RUN) gen-doc ... && \
  $(PYTHON_RUN) python3 src/assets/scripts/inject-metadata-in-index.py \
    $(s) \
    $(call schema_outdir,$(s))/docs/index.md \
    src/linkml/$(call schema_domain,$(s))/$(call schema_name,$(s))/manifest.yaml && \
  sed -i '/Container/d' $(call schema_outdir,$(s))/docs/index.md; \
)
endef
```

### Alternativ C: Utvide publish.sh til å injisere metadata

Når `mkdocs/publish.sh` kopierer genererte filer til `mkdocs/docs/`, kan me injisere metadata der.

**Problem:** Dette skjer **etter** `gen-doc`, så metadata vert berre synleg i publisert portal, ikkje i lokal `generated/`-katalog.

## Metadata-felt som skal visast

| Felt | Kjelde | Fallback | Eksempel |
|---|---|---|---|
| Schema URI | `schema.id` | - | `https://data.norge.no/samt/samt-bu` |
| Versjon | `schema.version` | "Ikkje sett" | `1.0.0` |
| Lisens | `schema.license` | - | `https://data.norge.no/nlod/no/2.0` |
| Utgjevar | `schema.annotations.utgiver` | - | `https://data.norge.no/organizations/974760673` |
| Status | `schema.annotations.status` | - | `http://purl.org/adms/status/Completed` |
| Endringsdato | `schema.annotations.endringsdato` | - | `2026-06-10` |
| Utgivelsesdato | `schema.annotations.utgivelsesdato` | - | `2026-01-15` |
| Validation policy | `manifest.validation_policy` | `bronze` | `silver` |
| Imports | `schema.imports` | `[]` | `dcat-ap-no, skos-ap-no` |

**Visning:**
- **URI-ar:** rendre som klikkbare lenker (Markdown-format: `[tekst](url)`)
- **Status:** vis både URI og lesbar tekst (t.d. "Ferdigstilt")
- **Imports:** vis som kommaseparert liste
- **Utgjevar:** dersom orgNr, slå opp namn i Brreg (valfritt)

## Steg

1. **Lag Python-script `inject-metadata-in-index.py`**
   - Argumenter: `<schema.yaml> <index.md> <manifest.yaml>`
   - Les metadata frå YAML-filer
   - Generer Markdown-tabell
   - Finn injeksjonspunkt i `index.md` (rett før `## Valideringsresultat` eller etter hovudskildring)
   - Skriv oppdatert `index.md`

2. **Oppdater `run_gen_doc` i Makefile**
   - Legg til kall til `inject-metadata-in-index.py` etter `gen-doc`
   - Pass riktige stiar

3. **Test med samt-bu**
   - Køyr `make gen-docs SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`
   - Sjekk at `generated/samt/samt-bu/docs/index.md` har Metadata-seksjon
   - Verifiser at metadata er korrekt
   - Verifiser at seksjonen kjem **før** Valideringsresultat

4. **Oppdater `mkdocs/publish.sh` (valfritt)**
   - Dersom metadata skal visast ulikt i publisert portal vs. lokal generering

## Prioritert handlingsliste

- [ ] Lag `src/assets/scripts/inject-metadata-in-index.py`
  - [ ] Les `schema.yaml` og ekstraher metadata
  - [ ] Les `manifest.yaml` og ekstraher `validation_policy`
  - [ ] Generer Markdown-tabell
  - [ ] Finn injeksjonspunkt i `index.md` (før `## Valideringsresultat` eller etter hovudskildring)
  - [ ] Skriv oppdatert `index.md` med Metadata-seksjon
- [ ] Oppdater `define run_gen_doc` i Makefile
  - [ ] Legg til kall til `inject-metadata-in-index.py` etter `gen-doc`
- [ ] Test med samt-bu
  - [ ] Verifiser at Metadata-seksjon vises i `index.md`
  - [ ] Verifiser at seksjonen kjem før Valideringsresultat
- [ ] Test med modell som har silver-annotasjonar (t.d. dcat-ap-no)

## Avhengigheiter

- `define run_gen_doc` i Makefile
- `<modell>-schema.yaml` (metadata-kjelde)
- `manifest.yaml` (validation_policy)
- `generated/<domain>/<modell>/docs/index.md` (generert av `gen-doc`)

## Merknader

- **Plassering:** Rett etter hovudskildring, før klasselistene (alternativt: rett før Valideringsresultat)
- **Format:** Markdown-tabell for lesbarheit
- **URI-ar:** Rendre som klikkbare lenker
- **Status-mapping:** Map ADMS-URI til lesbar tekst (t.d. `Completed` → "Ferdigstilt")
- **Imports:** Vis liste av importerte skjema (hjelper brukarar forstå avhengigheiter)

## Eksempel: før og etter

### Før
```markdown
# SAMT - Barnehagar og skular

Ontodia-vennlig LinkML-modell for skoler

URI: https://data.norge.no/samt/samt-bu

## Classes
...
```

### Etter
```markdown
# SAMT - Barnehagar og skular

Ontodia-vennlig LinkML-modell for skoler

## Metadata

| Felt | Verdi |
|---|---|
| Schema URI | [https://data.norge.no/samt/samt-bu](https://data.norge.no/samt/samt-bu) |
| Versjon | 1.0.0 |
| Lisens | [NLOD 2.0](https://data.norge.no/nlod/no/2.0) |
| Validation policy | silver |
| Imports | dcat-ap-no, skos-ap-no, dqv-ap-no |

## Classes
...
```

## Status-mapping (ADMS → Norsk)

| ADMS Status URI | Norsk tekst |
|---|---|
| `http://purl.org/adms/status/UnderDevelopment` | Under utarbeidelse |
| `http://purl.org/adms/status/Completed` | Ferdigstilt |
| `http://purl.org/adms/status/Deprecated` | Foreldet |
| `http://purl.org/adms/status/Withdrawn` | Trukket tilbake |

## Injeksjonspunkt

**Alternativ 1: Rett etter hovudskildring (anbefalt)**
```markdown
# Tittel

Beskrivelse

## Metadata     ← injiser her
...

## Classes
```

**Alternativ 2: Før Valideringsresultat**
```markdown
# Tittel

...

## Classes
...

## Metadata     ← injiser her
...

## Valideringsresultat
```

**Anbefaling:** Alternativ 1 — metadata kjem først, før klasselistene, slik at brukarar ser grunnleggande informasjon øvst.

## Python-script skisse

```python
#!/usr/bin/env python3
"""
Injiser metadata-seksjon i index.md generert av gen-doc.

Usage:
    inject-metadata-in-index.py <schema.yaml> <index.md> <manifest.yaml>
"""
import sys
from pathlib import Path
import yaml

def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def generate_metadata_section(schema, manifest):
    """Generer Markdown-tabell med metadata."""
    lines = ["", "## Metadata", "", "| Felt | Verdi |", "|---|---|"]
    
    # Schema URI
    if schema.get("id"):
        uri = schema["id"]
        lines.append(f"| Schema URI | [{uri}]({uri}) |")
    
    # Versjon
    if schema.get("version"):
        lines.append(f"| Versjon | {schema['version']} |")
    
    # Lisens
    if schema.get("license"):
        lic = schema["license"]
        lines.append(f"| Lisens | [{lic}]({lic}) |")
    
    # Validation policy
    policy = manifest.get("validation_policy", "bronze")
    lines.append(f"| Validation policy | {policy} |")
    
    # Imports
    if schema.get("imports"):
        imports = ", ".join(schema["imports"])
        lines.append(f"| Imports | {imports} |")
    
    lines.append("")
    return "\n".join(lines)

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <schema.yaml> <index.md> <manifest.yaml>", file=sys.stderr)
        sys.exit(1)
    
    schema_path = Path(sys.argv[1])
    index_path = Path(sys.argv[2])
    manifest_path = Path(sys.argv[3])
    
    schema = load_yaml(schema_path)
    manifest = load_yaml(manifest_path) if manifest_path.exists() else {}
    
    metadata_section = generate_metadata_section(schema, manifest)
    
    # Les index.md
    content = index_path.read_text(encoding="utf-8")
    
    # Finn injeksjonspunkt (etter hovudskildring, før ## Classes)
    # Enklaste: injiser rett før første ## (utanom tittelen)
    lines = content.split("\n")
    new_lines = []
    injected = False
    for i, line in enumerate(lines):
        if not injected and i > 0 and line.startswith("## "):
            # Injiser før denne seksjonen
            new_lines.append(metadata_section)
            injected = True
        new_lines.append(line)
    
    # Skriv tilbake
    index_path.write_text("\n".join(new_lines), encoding="utf-8")

if __name__ == "__main__":
    main()
```

## Neste steg

Etter at metadata-seksjonen er implementert:
1. Oppdater `mkdocs/publish.sh` for å kopiere metadata riktig
2. Vurder å vise metadata også på klasse-sidene (t.d. kva modell klassen kjem frå)
3. Legg til lenke frå metadata til valideringsresultat (dersom relevant)

## Utført

Implementert med **Alternativ A (Jinja2-template) + post-prosessering for validation_policy**:

**Template-endringar:**
- `src/assets/templates/docgen/index.md.jinja2`: lagt til Metadata-seksjon rett etter hovudskildring
- Viser Schema URI, Versjon, Lisens, Utgjevar, Status, Endringsdato, Utgivelsesdato, Imports
- Status-mapping: ADMS-URI → norsk tekst (t.d. "Ferdigstilt")
- URI-ar vert renderete som klikkbare lenker

**Post-prosessering:**
- `src/assets/scripts/inject-validation-policy.py`: injiserer validation_policy frå manifest.yaml
- Køyrer etter `gen-doc` og før `sed -i '/Container/d'`
- Legg til `| Validation policy | <policy> |` i Metadata-tabellen

**Makefile-endringar:**
- `define run_gen_doc`: lagt til kall til `inject-validation-policy.py` (linje 100-102)

**Testing:**
- samt-bu (silver): viser alle felt inkl. validation_policy
- fair-metadata (silver): viser alle felt
- common-ap-no (silver): viser alle felt

**Resultat:**
```markdown
## Metadata

| Felt | Verdi |
| --- | --- |
| Schema URI | [https://data.norge.no/samt/samt-bu](...) |
| Versjon | 1.0.0 |
| Lisens | [https://data.norge.no/nlod/no/2.0](...) |
| Utgjevar | [https://data.norge.no/organizations/971032146](...) |
| Status | Under utarbeidelse |
| Endringsdato | 2026-06-10 |
| Utgivelsesdato | 2026-06-10 |
| Validation policy | silver |
| Imports | linkml:types, ../../ap-no/dcat-ap-no/dcat-ap-no-schema, ... |
```

**Fordeler med denne løysinga:**
- Metadata vert generert automatisk for alle modellar
- Enklare å vedlikehalde (éin template i staden for mange hardkoda filer)
- Konsekvent visning på tvers av alle modellar
- Validation policy vert henta frå manifest.yaml (sannkjelda)

**Funksjonalitet:**
- ✅ Schema URI, versjon, lisens vises alltid (når dei finst)
- ✅ Silver-annotasjonar (utgjevar, status, datoar) vises når dei finst
- ✅ Validation policy frå manifest.yaml vises
- ✅ Imports-liste vises
- ✅ Status-mapping til norsk tekst
- ✅ URI-ar er klikkbare lenker
