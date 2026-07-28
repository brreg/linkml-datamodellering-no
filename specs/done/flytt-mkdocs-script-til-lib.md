# Flytt mkdocs-generatorscript til mkdocs/lib

**Dato:** 2026-07-28  
**Status:** Utført

## Bakgrunn

`src/assets/scripts/` inneheld for tida ein blanding av:
- Script som **kun** vert brukte til mkdocs-generering (`generate-validation-md.py`, `parse-dependency-tree.py`)
- Script som vert brukte i byggelogikk og CI (`run-validation.sh`, `filter-unchanged-logs.py`, `collect-concepts.py`)
- Brukarstøttescript (`new-model.sh`, `bump-version.sh`, `new-begrepskatalog.sh`)

For å forenkle mappestrukturen og samle mkdocs-relatert kode på eitt stad, ønskjer vi å flytte dei reine mkdocs-generatorscripta til `mkdocs/lib/scripts/`.

## Analyseresultat

### Script som **kun** vert brukte til mkdocs-generering

Desse to scripta vert **berre** kallte frå `mkdocs/lib/`:

| Script | Formål | Kallast frå |
|--------|--------|-------------|
| `generate-validation-md.py` | Genererer `## Valideringsresultat`-seksjon frå validation JSON til Markdown | `mkdocs/lib/sections/validation.sh` |
| `parse-dependency-tree.py` | Byggjer hierarkisk avhengigheitstre (direkte og transitive importar) | `mkdocs/lib/sections/dependencies.sh`, `mkdocs/lib/utils/imported_schemas.sh` |

### Script som **ikkje** skal flyttast

Desse scripta vert brukte utanfor mkdocs-generering (CI, byggelogikk, brukarstøtte):

| Script | Formål | Kallast frå |
|--------|--------|-------------|
| `run-validation.sh` | Validering av skjema og logging til co-location-struktur | `.github/workflows/validate.yml`, Makefile |
| `filter-unchanged-logs.py` | Filtrer ut valideringsloggar identiske med eksisterande loggar | `.github/workflows/validate.yml` |
| `collect-concepts.py` | Saml omgrep frå begrepskatalog-datafiler | CI/publiseringspipeline |
| `collect-concepts.sh` | Wrapper for `collect-concepts.py` | CI/publiseringspipeline |
| `new-model.sh` | Interaktivt script for å lage ny domenemodell | Brukarstøtte |
| `new-begrepskatalog.sh` | Interaktivt script for å lage ny begrepskatalog | Brukarstøtte |
| `new-begrepssamling.sh` | Interaktivt script for å lage ny begrepssamling | Brukarstøtte |
| `new-modellkatalog.sh` | Interaktivt script for å lage ny modellkatalog | Brukarstøtte |
| `bump-version.sh` | Bump semantisk versjon for skjema | Brukarstøtte |
| `add-schema-header-comments.py` | Legg til header-kommentarar i schema | Byggelogikk |
| `check-prereqs.bash` | Sjekk at nødvendige verktøy er installerte | Byggelogikk |
| `filter-unchanged-logs.py` | Filtrer uendra valideringsloggar | CI |
| `filter_container.awk` | Filtrer vekk containerklasser i gen-doc | Byggelogikk |
| `filter_erdiagram.py` | Filtrer ER-diagram | Byggelogikk |
| `filter_plantuml.py` | Filtrer PlantUML-diagram | Byggelogikk |
| `fix-xsd-dates.py` | Fiks XSD-datoar i genererte artefaktar | Byggelogikk |
| `gen-asyncapi.py` | Generer AsyncAPI-spec | Byggelogikk |
| `gen-config.sh` | Generer konfigurasjon | Byggelogikk |
| `gen-docgen-examples.py` | Generer eksempel for gen-doc | Byggelogikk |
| `gen-dqv-measurements.py` | Generer DQV-målingar | Byggelogikk |
| `gen-modelldcat-elements.py` | Generer ModellDCAT-element | Byggelogikk |
| `gen-openapi.py` | Generer OpenAPI-spec | Byggelogikk |
| `generate-informasjonsmodell.py` | Generer Informasjonsmodell-instansar | Byggelogikk |
| `generate-modellkatalog.py` | Generer modellkatalog | Byggelogikk |
| `generate-readme-tables.sh` | Generer tabellar i README | Byggelogikk |
| `inject-validation-policy.py` | Inject validation policy i schema | Byggelogikk |
| `list-tool-licenses.py` | List lisensar for verktøy | Byggelogikk |
| `save-validation-log.py` | Lagre valideringsloggar | Byggelogikk |
| `update-modellkatalog.py` | Oppdater modellkatalog | Byggelogikk |
| `update-schema-dates.py` | Oppdater datoar i schema | Byggelogikk |
| `validate-modelldcat.py` | Valider ModellDCAT-instansar | Byggelogikk |

## Tiltak

### 1. Opprett `mkdocs/lib/scripts/` katalog

```bash
mkdir -p mkdocs/lib/scripts
```

### 2. Flytt `generate-validation-md.py`

```bash
git mv src/assets/scripts/generate-validation-md.py mkdocs/lib/scripts/
```

**Oppdater referansar:**

**Fil:** `mkdocs/lib/sections/validation.sh` (linje 18)

```diff
-    python3 "$REPO_ROOT/src/assets/scripts/generate-validation-md.py" "$validation_json"
+    python3 "$REPO_ROOT/mkdocs/lib/scripts/generate-validation-md.py" "$validation_json"
```

### 3. Flytt `parse-dependency-tree.py`

```bash
git mv src/assets/scripts/parse-dependency-tree.py mkdocs/lib/scripts/
```

**Oppdater referansar:**

**Fil:** `mkdocs/lib/sections/dependencies.sh` (linje 29)

```diff
-    dep_tree=$(python3 "$REPO_ROOT/src/assets/scripts/parse-dependency-tree.py" "$schema" "$imports" "$direct_imports_normalized")
+    dep_tree=$(python3 "$REPO_ROOT/mkdocs/lib/scripts/parse-dependency-tree.py" "$schema" "$imports" "$direct_imports_normalized")
```

**Fil:** `mkdocs/lib/utils/imported_schemas.sh` (linje 20)

```diff
-    python3 "$REPO_ROOT/src/assets/scripts/parse-dependency-tree.py" --format flat "$schema" "$imports"
+    python3 "$REPO_ROOT/mkdocs/lib/scripts/parse-dependency-tree.py" --format flat "$schema" "$imports"
```

### 4. Oppdater dokumentasjon

**Fil:** `CLAUDE.md`

```diff
-- **Valideringsresultat** vert generert av `src/assets/scripts/generate-validation-md.py` frå `validation/<versjon>/<policy>.json` med rein Markdown (nummererte lister, ikkje `<details>`-blokkar)
+- **Valideringsresultat** vert generert av `mkdocs/lib/scripts/generate-validation-md.py` frå `validation/<versjon>/<policy>.json` med rein Markdown (nummererte lister, ikkje `<details>`-blokkar)
```

**Fil:** `mkdocs/docs/index-md-struktur.md`

Oppdater alle referansar til `src/assets/scripts/generate-validation-md.py` og `src/assets/scripts/parse-dependency-tree.py` til nye stiar.

### 5. Verifiser at alt køyrer

```bash
# Test mkdocs-generering
make docs-publish

# Verifiser at dokumentasjonen inneheld korrekte seksjons-innhald
ls -la mkdocs/docs/samt/samt-bu/index.md
grep -A5 "## Valideringsresultat" mkdocs/docs/samt/samt-bu/index.md
grep -A5 "## Avhengigheiter" mkdocs/docs/samt/samt-bu/index.md
```

## Handlingsliste

- [x] 1. Opprett `mkdocs/lib/scripts/` katalog
- [x] 2. Flytt `generate-validation-md.py` med `git mv`
- [x] 3. Oppdater referanse i `mkdocs/lib/sections/validation.sh`
- [x] 4. Flytt `parse-dependency-tree.py` med `git mv`
- [x] 5. Oppdater referanse i `mkdocs/lib/sections/dependencies.sh`
- [x] 6. Oppdater referanse i `mkdocs/lib/utils/imported_schemas.sh`
- [x] 7. Oppdater dokumentasjon i `CLAUDE.md`
- [x] 8. Oppdater dokumentasjon i `mkdocs/docs/index-md-struktur.md`
- [x] 9. Verifiser at `make docs-publish` køyrer utan feil
- [x] 10. Verifiser at genererte `index.md`-filer inneheld korrekte seksjons-innhald

## Utført

Alle tiltak er utførte. Verifisering viser:

- ✅ `mkdocs/lib/scripts/generate-validation-md.py` eksisterer
- ✅ `mkdocs/lib/scripts/parse-dependency-tree.py` eksisterer
- ✅ `src/assets/scripts/generate-validation-md.py` eksisterer **ikkje** lenger
- ✅ `src/assets/scripts/parse-dependency-tree.py` eksisterer **ikkje** lenger
- ✅ `make docs-publish` køyrer utan feil (exit code 0, 104.8s)
- ✅ Genererte `mkdocs/docs/*/*/index.md` inneheld korrekte "Valideringsresultat"- og "Avhengigheiter"-seksjons-innhald
  - Verifisert for `samt/samt-bu` og `ap-no/dcat-ap-no`
  - Begge seksjonsane genererast korrekt frå nye script-lokasjonar

Ingen referansar til gamle stiar gjenstår i aktive filer (ekskludert specs/ som arkiv).
