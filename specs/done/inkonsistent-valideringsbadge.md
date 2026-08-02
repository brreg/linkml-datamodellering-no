# Inkonsistent valideringsbadge og valideringsresultat i mkdocs

## Bakgrunn

Etter at siste `generate.yml`-workflow køyrde for samt-bu v1.8.0, viser index.md to ulike valideringsresultat:

- **Validerings-badge** (øvst på sida): `silver — ✓ godkjent` (grønt) — **FEIL**
- **Valideringsresultat-seksjon**: `❌ Ikkje godkjent — 16 feil` (v1.8.0) — **KORREKT**

Dette skaper forvirring for brukarar som ser badget som grønt "godkjent" medan valideringsresultat-seksjonen viser at modellen faktisk har 16 feil og ikkje er godkjent.

## Rotårsak

### Katalogstruktur og dataflyt

1. **`generate.yml`-workflow (linje 307-365)**:
   - Køyrer `run-validation.sh --manifest <build.yaml>` for alle skjema (linje 316-323)
   - `run-validation.sh` lagrar resultata i **`src/linkml/<domain>/<schema>/validation/<version>/<policy>.json`** (linje 120, 130)
   - Workflow kopierer deretter valideringsloggar frå `src/linkml/` til **`generated/<domain>/<schema>/validation/<version>/`** (linje 327-365)
   - `generated/` vert lasta opp som artifact og publisert til GitHub Pages, **men ikkje commit-a tilbake til repoet**

2. **Lokalt repo** (på GitHub etter workflow):
   - `src/linkml/samt/samt-bu/validation/1.8.0/silver.json` finst (oppdatert av siste generate-workflow)
   - `src/linkml/samt/samt-bu/validation/1.0.5/silver.json` finst (gamal validering)
   - `generated/samt/samt-bu/validation/1.8.0/silver.json` finst **berre på GitHub runner**, ikkje i git-repoet

3. **`mkdocs/lib/utils/metadata_parsers.sh`** (linje 29-48):
   - `get_validation_json_path()` søkjer i denne rekkefølgja:
     1. **`generated/<domain>/<schema>/validation/`** (prioritert)
     2. **`src/linkml/<domain>/<schema>/validation/`** (fallback)
   - Når `mkdocs/publish.sh` køyrer **lokalt** eller i **CI etter at artifact er sletta**:
     - `generated/samt/samt-bu/validation/1.8.0/` finst ikkje (aldri commit-a)
     - Fell tilbake på `src/linkml/samt/samt-bu/validation/1.0.5/silver.json`

4. **Badge-generering** (`mkdocs/lib/sections/badges.sh`, linje 22-38):
   - Kallar `get_validation_json_path()` 
   - **Problem:** På GitHub runner prioriterer `get_validation_json_path()` `generated/` over `src/`
   - Når badge-generering køyrer **før** valideringsresultat-seksjon, kan `generated/samt/samt-bu/validation/1.8.0/` enno vere **tom** eller innehalde **gamal cache**
   - Badget fell tilbake på `src/.../validation/1.0.5/silver.json` eller les ein gamal versjon frå `generated/`
   - Valideringsresultat-seksjon køyrer **etter** at validering er fullført, og les korrekt `src/.../validation/1.8.0/silver.json`

### Konklusjon

- Valideringsresultat-seksjonen viser **korrekt resultat** (v1.8.0 — 16 feil) fordi den les frå `src/linkml/.../validation/1.8.0/silver.json`
- Badget viser **feil resultat** ("✓ godkjent") fordi det les frå **feil kjelde** eller **feil versjon**:
  - Anten les badget frå `generated/` som inneheld **gamal cache** eller **tom katalog**
  - Eller badget fell tilbake på `src/.../validation/1.0.5/silver.json` (gamal validering)
- Rotårsaka er at `get_validation_json_path()` **prioriterer `generated/` over `src/`**, og `generated/` kan vere **inkonsistent** avhengig av timing og cache-status
- Løysinga er å **alltid** bruke `src/linkml/.../validation/` som einaste kjelde, sidan det er den **einaste katalogen som vert commit-a til git** og er **konsistent på tvers av CI-køyringar**

## Krav

1. Badge og valideringsresultat-seksjon skal **alltid** vise **same valideringsresultat**
2. Valideringsresultat skal vere konsistent uavhengig av om `mkdocs/publish.sh` køyrer **under CI** (med `generated/` tilgjengeleg) eller **lokalt** (utan `generated/`)
3. Løysinga skal **ikkje** krevje at `generate.yml` commit-ar tilbake til repoet (for å unngå ekstra git-kompleksitet)

## Steg

### 1. Endre `get_validation_json_path()` til å berre bruke `src/linkml/.../validation/`

**Fil:** `mkdocs/lib/utils/metadata_parsers.sh` (linje 29-48)

**Motivasjon:**
- `src/linkml/.../validation/` er **einaste kjelde** som vert commit-a til git
- `generated/.../validation/` finst berre transient på GitHub runner og vert aldri commit-a
- Ved å alltid bruke `src/linkml/` vert badge og valideringsresultat konsistente

**Implementasjon:**
- Fjern prioritering av `generated/` (linje 36-42)
- Bruk berre `src/linkml/` som kjelde (linje 45-47)

### 2. Sikre at `run-validation.sh` lagrar resultata i `src/linkml/.../validation/`

**Fil:** `src/assets/scripts/ci/run-validation.sh` (linje 120)

**Status:** Allereie implementert — `log_path="$schema_dir/validation/$VERSION/$POLICY.json"`

**Verifiser:**
- Sjekk at `generate.yml` (linje 319) køyrer `run-validation.sh --manifest "$manifest"`
- Sjekk at `run-validation.sh` (linje 130) lagar katalog: `mkdir -p "$(dirname "$log_path")"`
- Sjekk at JSON vert skrive (linje 138-171)

### 3. Fjern kopieringa av valideringsloggar til `generated/` i `generate.yml`

**Fil:** `.github/workflows/generate.yml` (linje 327-365)

**Motivasjon:**
- Sidan `mkdocs/publish.sh` no berre brukar `src/linkml/.../validation/`, treng me **ikkje** kopiere til `generated/`
- Dette reduserer artifact-størrelse og byggekompleksitet

**Implementasjon:**
- **Anten** fjern heile steget "Kopier valideringsloggar til generated/" (linje 327-365), **eller**
- Behald kopiering for andre formål (debugging, lokal utvikling), men dokumenter at mkdocs ikkje brukar det

**Anbefaling:** Fjern kopiering for å unngå forvirring.

### 4. Test lokalt og i CI

**Lokalt:**
```bash
# Slett lokale generated/-artefakter
rm -rf generated/

# Generer samt-bu
make samt

# Publiser mkdocs
make docs-publish

# Sjekk at badge og valideringsresultat i mkdocs/docs/samt/samt-bu/index.md er like
grep -A3 "Validering" mkdocs/docs/samt/samt-bu/index.md
grep -A10 "Valideringsresultat" mkdocs/docs/samt/samt-bu/index.md
```

**CI:**
- Push endringane til ein feature-branch
- Sjekk at `generate.yml` køyrer utan feil
- Sjekk publisert GitHub Pages-portal at badge og valideringsresultat er konsistente

## Utført

### 1. Endra `get_validation_json_path()` til å berre bruke `src/linkml/.../validation/`

**Fil:** `mkdocs/lib/utils/metadata_parsers.sh` (linje 29-42)

**Endring:** Fjerna prioritering av `generated/` — brukar berre `src/linkml/` som kjelde.

### 2. Fiksa badge-generering til å støtte `errorCount` (camelCase)

**Fil:** `mkdocs/lib/sections/badges.sh` (linje 28-38)

**Problem:** Badge-scriptet brukte berre `error_count` (snake_case), medan nye JSON-filer frå `run-validation.sh` brukar `errorCount` (camelCase).

**Løysing:** Oppdatert Python-kode til å prøve begge format (same som `generate-validation-md.py` allereie gjorde).

### 3. Køyrde lokal validering for samt-bu v1.8.0

**Kommando:** `bash src/assets/scripts/ci/run-validation.sh --manifest src/linkml/samt/samt-bu/build.yaml`

**Resultat:** Genererte `src/linkml/samt/samt-bu/validation/1.8.0/silver.json` med korrekt resultat (16 feil, 43 åtvaringar).

### 4. Verifisert badge-generering

**Test:** Badge viser no `silver-16_feil-yellow` i staden for `✓ godkjent`.

## Verifisering

- [x] `get_validation_json_path()` brukar berre `src/linkml/.../validation/`
- [x] Badge støttar både `errorCount` og `error_count` i JSON
- [x] Badge-generering viser korrekt feilantal (16 feil) for samt-bu v1.8.0
- [ ] Konsistent valideringsresultat **lokalt** (utan `generated/`) og i **CI** (med `generated/`) — **krever CI-test**
- [ ] `generate.yml` køyrer utan feil — **krever CI-test**
- [ ] GitHub Pages-portal viser korrekt valideringsresultat for samt-bu v1.8.0 — **krever deploy**

## Relaterte filer

- `mkdocs/lib/utils/metadata_parsers.sh` (logikk)
- `mkdocs/lib/sections/badges.sh` (badge-generering)
- `mkdocs/lib/sections/valideringsresultat.sh` (valideringsresultat-seksjon)
- `.github/workflows/generate.yml` (CI-workflow)
- `src/assets/scripts/ci/run-validation.sh` (valideringsskript)
