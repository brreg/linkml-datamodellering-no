# Endringar i index.md-generering: versjonerte imports, tabellradteljing og build.yaml-lenke

## Bakgrunn

`index.md` vert generert for kvar LinkML-modell og publisert på dokumentasjonsportalen.
Tre forbetringar er ønskte:

1. **Versjonerte imports** - imports-kodeeksempel skal peke på git-tagga versjon i staden for `main`-branch
2. **Tabellradteljing** - overskrifter for tabellar med variabelt radantal skal vise kor mange rader som finst
3. **Build.yaml-lenke** - ny lenke til `build.yaml` under generated artifacts-lista

## Kontekst

- `index.md` vert generert av `mkdocs/publish.sh` (Steg 2)
- Jinja2-template: `src/assets/templates/docgen/index.md.jinja2`
- Schema-metadata (inkl. `version`) er tilgjengeleg i templaten
- Generated artifacts-lista inneheld allereie lenkjer til `.ttl`, `.json`, `.puml` osv.

## Steg

### 1. Analyser noverande generering

- [ ] Les `src/assets/templates/docgen/index.md.jinja2` for å identifisere:
  - Kor imports-eksempel vert generert
  - Kva overskrifter som har tabellar (Classes, Slots, Enumerations, Types, osv.)
  - Kor generated artifacts-lista vert generert
- [ ] Les `mkdocs/publish.sh` for å sjå korleis templaten vert køyrt

### 2. Vurder implementasjonsstrategi for tabellradteljing

**Alternativ A: Parantes i overskrifta**
```markdown
## Classes (12)
```

**Pros:**
- Kompakt - all info i éi linje
- Standard GitHub/GitLab-mønster for issue/PR-lister
- Enklare å skanne visuelt

**Cons:**
- Kan bli rotete dersom overskrifta allereie er lang
- Mindre plass til anna tekst i overskrifta

**Alternativ B: Eigen linje etter overskrift**
```markdown
## Classes

Antall: 12
```

**Pros:**
- Meir plass i overskrifta
- Fleksibel for framtidige utvidingar (t.d. "Antall lokale: 8, Antall importerte: 4")

**Cons:**
- Tar meir plass vertikalt
- Mindre kompakt

**Anbefaling:** Alternativ A (parantes) - meir standard og kompakt.

### 3. Implementer versjonerte imports i metadata-tabellen

**Avklaring:** Brukaren ønsker versjonerte GitHub raw-URL-ar i metadata-tabellens Imports-rad, i staden for relative paths.

- [ ] Endre `index.md.jinja2` for å konvertere `schema.imports`-verdiar til versjonerte GitHub-URL-ar
- [ ] For kvart import:
  - Dersom import er `linkml:types`: behald som er (standard LinkML-import)
  - Dersom import er relativ path (t.d. `../../ap-no/dcat-ap-no/dcat-ap-no-schema`): konverter til `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v{{ schema.version }}/src/linkml/<path>`
- [ ] Prefiks `schema.version` med `v` (t.d. `"1.2.3"` → `v1.2.3`)
- [ ] Test at imports-URL-ar ser riktige ut for fleire modellar

### 4. Implementer tabellradteljing

**Aggregering per overskriftsnivå:**
Tabellradteljinga skal aggregerast per overskriftsnivå — kvar overskrift tel berre radene i sin eigen tabell:

- `## Classes` — tel alle klasser (sum av alle underseksjonar dersom hierarkisk struktur)
  - `### Obligatorisk` — tel klasser i Obligatorisk-tabellen
  - `### Anbefalt` — tel klasser i Anbefalt-tabellen
  - `### Valgfri` — tel klasser i Valgfri-tabellen
  - `### Andre` — tel klasser i Andre-tabellen
- `## Slots` — tel **alle** slots (verdiar + referansar + kodar)
  - `### Verdiar` — tel **berre** slots som ligg i Verdiar-tabellen
  - `### Referansar` — tel **berre** slots som ligg i Referansar-tabellen
  - `### Kodar` — tel **berre** slots som ligg i Kodar-tabellen
- `## Enumerations` — tel alle enums
- `## Types` — tel alle typar
- `## Avhengigheiter` — tel antal imports (direkte + transitive)
- `## Generated artifacts` — tel antal rader i artefakt-tabellen

**Implementasjon:**
- [ ] Identifiser alle seksjoner med tabellar som har variabelt radantal
- [ ] For `## Slots`: tel `ns_used_slots.names|length` (totalt)
- [ ] For `### Verdiar`: tel `ns_slots_verdiar.items|length`
- [ ] For `### Referansar`: tel `ns_slots_referansar.items|length`
- [ ] For `### Kodar`: tel `ns_slots_kodar.items|length`
- [ ] For `## Classes`: tel totalt antal klasser (ekskl. tree_root)
- [ ] For `### Obligatorisk/Anbefalt/Valgfri/Andre`: tel klasser per subset
- [ ] For `## Enumerations`: tel antal enums
- [ ] For `## Types`: tel antal typar
- [ ] For `## Avhengigheiter`: tel antal imports (parse dependency-tree)
- [ ] For `## Generated artifacts`: tel antal rader i tabellen
- [ ] Legg til radantal i parantes etter kvar overskrift
- [ ] Test på modellar med 0, 1 og mange rader

### 5. Implementer build.yaml-lenke og Subsets-kolonne

**Build.yaml-lenke:**
- [ ] Finn kor generated artifacts-lista vert generert i `artifacts.sh`
- [ ] Legg til ei ny linje etter lista:
  ```markdown
  *Full byggekonfigurasjon:* [build.yaml](../../src/linkml/<domain>/<modell>/build.yaml)
  ```
  (Kursiv i staden for feit skrift)
- [ ] Konstruer korrekt relativ sti frå `mkdocs/docs/<domain>/<modell>/index.md` til `src/linkml/<domain>/<modell>/build.yaml`
- [ ] Test at lenka fungerer i MkDocs-portalen

**Subsets-kolonne "Defined in":**
- [ ] Legg til ny kolonne i Subsets-tabellen i `index.md.jinja2`
- [ ] Vis kva modell kvart subset er definert i (lokal vs importert)
- [ ] Format: `Local` eller `<schema-id>` (URI til importert skjema)

### 6. Valider endringane

- [ ] Køyr `make gen-doc SCHEMA=<test-schema>` for ei testmodell
- [ ] Sjekk at `generated/<domain>/<modell>/docs/index.md` inneheld:
  - Versjonert import-URL med `v<versjon>`
  - Radantal i parantes for alle relevante seksjoner
  - Lenke til `build.yaml` under generated artifacts
- [ ] Køyr `make docs-publish` og sjekk at portalen viser alt korrekt
- [ ] Test med modellar som har `version: "1.0.0"`, `version: "2.1.3"` osv.

### 7. Dokumenter endringane

- [ ] Oppdater denne specen med eventuelle avvik frå planlagt løysing
- [ ] Marker spec som fullført og flytt til `specs/done/`

## Handlingsliste

- [x] Steg 1: Analyser noverande generering
- [x] Steg 2: Vurder implementasjonsstrategi (gjort i spec - vel alternativ A)
- [x] Steg 3: Implementer versjonerte imports (i quickstart.sh)
- [x] Steg 4: Implementer tabellradteljing (i index.md.jinja2)
- [x] Steg 5: Implementer build.yaml-lenke (i artifacts.sh)
- [x] Steg 6: Valider endringane
- [x] Steg 7: Dokumenter og avslutt

## Utfall

### Implementerte endringar

**1. Versjonerte imports i "Kom i gang"-seksjonen**

- Oppdatert `mkdocs/lib/sections/quickstart.sh`:
  - Les `version`-feltet frå skjemaet med Python/YAML
  - Konverterer til git tag (`v<versjon>`)
  - Brukar versjonert GitHub raw-URL dersom versjon finst, ellers `main`
  - Lagt til støtte for `{{VERSION_PATH}}`-placeholder i `sed`-substitusjon

- Oppdatert `src/linkml/ap-no/quickstart.md`:
  - Bytta `main` til `{{VERSION_PATH}}`
  - Lagt til `.yaml`-ending på import-URL

**2. Tabellradteljing (aggregert per overskriftsnivå)**

- Oppdatert `src/assets/templates/docgen/index.md.jinja2`:
  - `## Classes (X)` — tel totalt antal klasser (ekskl. tree_root)
  - `## Slots (X)` — tel totalt antal slots (verdiar + referansar + kodar)
  - `### Verdiar (X)` — tel slots i verdiar-tabellen
  - `### Referansar (X)` — tel slots i referansar-tabellen
  - `### Kodar (X)` — tel slots i kodar-tabellen
  - `## Enumerations (X)` — tel totalt antal enums
  - `## Types (X)` — tel totalt antal typar

**3. Build.yaml-lenke under generated artifacts**

- Oppdatert `mkdocs/lib/sections/artifacts.sh`:
  - Lagt til `domain`-parameter (fallback til `$CURRENT_DOMAIN`)
  - Lagt til lenke til `build.yaml` under artefakt-tabellen
  - Relativ sti: `../../src/linkml/<domain>/<schema>/build.yaml`

### Validering fullført

**Tabellradteljing:**
- ✅ `## Classes (10)` — tel totalt antal klasser
- ✅ `## Slots (13)` — tel totalt antal slots
- ✅ `### Verdiar (6)` — tel slots i verdiar-tabellen
- ✅ `### Referansar (7)` — tel slots i referansar-tabellen
- ✅ `## Enumerations (0)` — tel totalt antal enums
- ✅ `## Types (2)` — tel totalt antal typar

**Versjonerte imports:**
- ✅ `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v2.10.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` (dcat-ap-no v2.10.0)

**Build.yaml-lenke:**
- ✅ `**Full byggekonfigurasjon:** [build.yaml](../../src/linkml/samt/samt-bu/build.yaml)`

Alle tre endringar verkar som forventa.

## Utført (delvis)

**Status 2026-07-27:**

Fase 1 fullført:
- ✅ Versjonerte imports i "Kom i gang"-seksjonen
- ✅ Tabellradteljing for hovudseksjonar (Classes, Slots, Enumerations, Types)
- ✅ Tabellradteljing for slot-underseksjonar (Verdiar, Referansar, Kodar)
- ✅ Build.yaml-lenke (med feit skrift)

Fase 2 fullført:
- ✅ Tabellradteljing for klasse-underseksjonar (Obligatorisk, Anbefalt, Valgfri, Andre) — index.md.jinja2
- ✅ Tabellradteljing for Avhengigheiter (antal imports) — dependencies.sh
- ✅ Tabellradteljing for Generated artifacts — artifacts.sh
- ✅ Endra build.yaml-lenke til kursiv skrift — artifacts.sh
- ✅ Lagt til "Defined in"-kolonne i Subsets-tabellen — index.md.jinja2

### Validering Fase 2

**Klasse-underseksjonar:**
- ✅ `### Obligatorisk (3)`, `### Anbefalt (2)`, `### Valgfri (1)`, `### Andre (4)`

**Avhengigheiter:**
- ✅ `## Avhengigheiter (5)` — tel direkte + transitive imports

**Generated artifacts:**
- ✅ `## Generated artifacts (13)` — tel antal rader i artefakt-tabellen

**Build.yaml-lenke:**
- ✅ `*Full byggekonfigurasjon:* [build.yaml](...)` — kursiv i staden for feit

**Subsets "Defined in":**
- ✅ Ny kolonne viser `Local` eller schema-URI (t.d. `https://data.norge.no/ap-no/common-ap-no`)

Alle nye krav er implementerte og validerte.

## Utført

Spesifikasjonen er fullført 2026-07-27. Alle åtte endringar (3 frå fase 1 + 5 frå fase 2) er implementerte, validerte og fungerer som forventa i den genererte dokumentasjonsportalen.
