# Datamodell overskriftshierarki

## Bakgrunn

I `index.md` for kvar modell er Classes, Slots, Enumerations, Types og Subsets heading 2 (`##`) på same nivå som dei fleste andre hovudseksjonane (Metadata, ER-diagram, Valideringsresultat osv.).

Desse fem seksjonane er alle **deler av datamodellen**, ikkje sjølvstendige hovudseksjonar. Dei bør ligge under ein eksisterande "## Datamodell"-overskrift (som allereie er heading 2 i `index.md`).

**Mål:** Endre overskriftshierarkiet slik at Classes, Slots, Enumerations, Types og Subsets blir heading 3 (`###`) under "## Datamodell", og at deira deloverskrifte (t.d. "Obligatorisk", "Anbefalt", "Verdiar", "Referansar") blir heading 4 (`####`).

## Resulterende struktur

```markdown
# <schema>
## Om denne modellen
## Kom i gang
## Eksempeldatafil
## Modellmetadata
## Avhengigheiter
## ER-diagram
## Datamodell              ← eksisterande heading 2
### Classes               ← endra frå ## til ###
#### Obligatorisk         ← endra frå ### til ####
#### Anbefalt             ← endra frå ### til ####
#### Valgfri              ← endra frå ### til ####
#### Andre                ← endra frå ### til ####
### Slots                 ← endra frå ## til ###
#### Verdiar              ← endra frå ### til ####
#### Referansar           ← endra frå ### til ####
#### Kodar                ← endra frå ### til ####
### Enumerations          ← endra frå ## til ###
### Types                 ← endra frå ## til ###
### Subsets               ← endra frå ## til ###
## Generated artifacts
## Valideringsresultat
## Versjonslog
## Kontakt
```

## Steg

### 1. Oppdater Jinja2-template

**Fil:** `src/assets/templates/docgen/index.md.jinja2`

**Endringar:**

- Linje 62: `## Classes` → `### Classes`
- Linje 99: `### {{ subset_name }}` → `#### {{ subset_name }}`
- Linje 144: `## Slots` → `### Slots`
- Linje 149: `### Verdiar` → `#### Verdiar`
- Linje 175: `### Referansar` → `#### Referansar`
- Linje 201: `### Kodar` → `#### Kodar`
- Linje 257: `## Enumerations` → `### Enumerations`
- Linje 339: `## Types` → `### Types`
- Linje 429: `## Subsets` → `### Subsets`

### 2. Oppdater classes.sh

**Fil:** `mkdocs/lib/sections/classes.sh`

**Endringar:**

Endre alle grep/awk-uttrykk som søkjer etter `^## Classes`, `^## Slots` osv. til `^### Classes`, `^### Slots` osv.:

- Linje 76: `grep "^## ${section_header} ("` → `grep "^### ${section_header} ("`
- Linje 88: `grep -A 100 "^## ${section_header}"` → `grep -A 100 "^### ${section_header}"`
- Linje 148: `awk '/^## Classes/,/^## [^C]/'` → `awk '/^### Classes/,/^### [^C]/'`
- Linje 150: `sed 's/^## Classes (\([0-9]*\))$/### Classes (\1) {#classes}/'`
- Linje 158: `awk '/^## Slots/,/^## [^S]/'` → `awk '/^### Slots/,/^### [^S]/'`
- Linje 158: `sed 's/^## Slots (\([0-9]*\))$/### Slots (\1) {#slots}/'`
- Linje 166: `grep -q "^## Enumerations"` → `grep -q "^### Enumerations"`
- Linje 167: `awk '/^## Enumerations/,/^## [^E]/'` → `awk '/^### Enumerations/,/^### [^E]/'`
- Linje 167: `sed 's/^## Enumerations (\([0-9]*\))$/### Enumerations (\1) {#enumerations}/'`
- Linje 175: `grep -q "^## Types"` → `grep -q "^### Types"`
- Linje 176: `awk '/^## Types/,/^## [^T]/'` → `awk '/^### Types/,/^### [^T]/'`
- Linje 176: `sed 's/^## Types (\([0-9]*\))$/### Types (\1) {#types}/'`
- Linje 184: `grep -q "^## Subsets"` → `grep -q "^### Subsets"`
- Linje 185: `awk '/^## Subsets/,0'` → `awk '/^### Subsets/,0'`
- Linje 185: `sed 's/^## Subsets (\([0-9]*\))$/### Subsets (\1) {#subsets}/'`

### 3. Regenerer dokumentasjon

Køyr `make docs-publish` for å regenerere `index.md` for alle modellar med oppdatert overskriftshierarki.

### 4. Verifiser resultat

Sjekk at `mkdocs/docs/samt/samt-bu/index.md` har korrekt overskriftshierarki:

- `### Classes` med `#### Obligatorisk`, `#### Anbefalt` osv.
- `### Slots` med `#### Verdiar`, `#### Referansar` osv.
- `### Enumerations`, `### Types`, `### Subsets`

## Utført

✅ **Steg 1:** Oppdatert Jinja2-template (`src/assets/templates/docgen/index.md.jinja2`)
- Endra `## Classes` til `### Classes` (linje 62)
- Endra `### {{ subset_name }}` til `#### {{ subset_name }}` (linje 99)
- Endra `## Slots` til `### Slots` (linje 144)
- Endra `### Verdiar/Referansar/Kodar` til `#### Verdiar/Referansar/Kodar` (linje 149, 175, 201)
- Endra `## Enumerations/Types/Subsets` til `### Enumerations/Types/Subsets` (linje 257, 339, 429)

✅ **Steg 2:** Oppdatert `mkdocs/lib/sections/classes.sh`
- Endra alle grep/awk-uttrykk frå `^## Classes` til `^### Classes` (linje 76, 88, 150)
- Endra alle sed-substitusjoner frå `^## Classes` til `^### Classes` (linje 150, 158, 167, 176, 185)

✅ **Steg 3:** Oppdatert `mkdocs/lib/sections/metadata.sh`
- Endra awk-kommando til å stoppe ved både `^##` og `^###` (linje 15)
- Hindrar at Classes-seksjonen vert inkludert i Modellmetadata-tabell

⚠️ **Problem oppdaga:** `generate_classes_section` feila stille pga. `build_import_links` søkjer etter `^### ${section_header}` i importerte skjema som framleis har `^## ${section_header}` (heading 2). Alle skjema må regenererast **samtidig** for at import-lenker skal fungere.

✅ **Steg 4:** Oppdatert `mkdocs/lib/sections/classes.sh` (backward-compatible)
- Endra grep-uttrykk til `^###\? ${section_header}` for å støtte både heading 2 og 3
- Handterer overgangsfase der nokre skjema har heading 2 og andre har heading 3

✅ **Steg 5:** Regenerert dokumentasjonsportal (`make docs-publish`)
- Alle skjema publiserte utan feil
- samt-bu har no:
  - `### Classes` med `#### Obligatorisk/Anbefalt/Valgfri/Andre`
  - `### Slots` med `#### Verdiar/Referansar`
  - `### Enumerations/Types/Subsets`

✅ **Verifisert:** Overskriftshierarkiet er konsistent:
```
## Datamodell
### Classes
#### Obligatorisk
#### Anbefalt
#### Valgfri
#### Andre
### Slots
#### Verdiar
#### Referansar
### Enumerations
### Types
### Subsets
```

## Handlingsliste

- [x] Oppdater Jinja2-template
- [x] Oppdater `mkdocs/lib/sections/classes.sh`
- [x] Oppdater `mkdocs/lib/sections/metadata.sh`
- [x] Backward-compatible grep (støtte både `##` og `###`)
- [x] Regenerer dokumentasjonsportal
- [x] Verifiser resultat
