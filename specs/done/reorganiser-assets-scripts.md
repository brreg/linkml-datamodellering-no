# Reorganiser src/assets/scripts etter bruksområde

**Dato:** 2026-07-28  
**Status:** Utført

## Bakgrunn

`src/assets/scripts/` inneheld for tida ein blanding av:
- **Byggelogikk-script** — brukte av Makefile til å generere artefaktar (filter, gen-*, fix-*)
- **Validerings-script** — brukte av Makefile og CI til å validere skjema
- **Brukarstøttescript** — interaktive script for å lage nye modellar (new-*, bump-*)
- **CI-spesifikke script** — brukte berre i GitHub Actions
- **Modellkatalog-script** — generering og oppdatering av modellkatalogar
- **Diverse verktøy** — lisensverkty, README-generering

For å forenkle strukturen og gjere det lettare å finne rett script, ønskjer vi å flytte byggelogikk-script til ein eigen katalog `src/assets/scripts/makefile/`.

## Analyseresultat

### Script brukte av Makefile (byggelogikk)

Desse scripta vert **kallte frå Makefile** som del av bygge- og genereringsprosessen:

| Script | Formål | Kallast frå |
|--------|--------|-------------|
| `filter_container.awk` | Filtrer vekk containerklasser i gen-doc og erdiagram | Makefile (gen-doc, gen-erdiagram) |
| `filter_erdiagram.py` | Filtrer ER-diagram til kun lokale klasser | Makefile (gen-erdiagram) |
| `filter_plantuml.py` | Filtrer PlantUML-diagram (filtrert/full versjon) | Makefile (gen-plantuml) |
| `fix-xsd-dates.py` | Fiks XSD-datoar i genererte artefaktar | Makefile (gen-json-schema) |
| `gen-asyncapi.py` | Generer AsyncAPI-spec frå LinkML-schema | Makefile (gen-asyncapi) |
| `gen-openapi.py` | Generer OpenAPI-spec frå LinkML-schema | Makefile (gen-openapi) |
| `gen-docgen-examples.py` | Generer eksempel for gen-doc | Makefile (gen-doc) |
| `gen-dqv-measurements.py` | Generer DQV-målingar | Makefile (gen-dqv) |
| `gen-modelldcat-elements.py` | Generer ModellDCAT-element | Makefile (gen-modelldcat) |
| `generate-informasjonsmodell.py` | Generer Informasjonsmodell-instansar | Makefile (diverse targets) |
| `generate-modellkatalog.py` | Generer modellkatalog | Makefile (publish-modellkatalog) |
| `update-modellkatalog.py` | Oppdater modellkatalog | Makefile (update-modellkatalog) |
| `save-validation-log.py` | Lagre valideringsloggar til co-location-struktur | Makefile (mcp-validate) |
| `run-schema-validation.py` | Køyr schema-validering mot policy | Makefile (mcp-validate) |
| `generate-readme-tables.sh` | Generer tabellar i README.md | Makefile (readme-tables) |
| `gen-config.sh` | Generer config.mk | Makefile (config) |
| `check-prereqs.bash` | Sjekk at nødvendige verktøy er installerte | Makefile (check-prereqs) |

### Script brukte av både Makefile og CI

| Script | Formål | Kallast frå |
|--------|--------|-------------|
| `run-validation.sh` | Wrapper for validering med logging | Makefile, `.github/workflows/validate.yml` |

### Script brukte **berre** av CI

| Script | Formål | Kallast frå |
|--------|--------|-------------|
| `filter-unchanged-logs.py` | Filtrer uendra valideringsloggar | `.github/workflows/validate.yml` |
| `collect-concepts.py` | Saml omgrep frå begrepskatalog-datafiler | CI/publiseringspipeline |
| `collect-concepts.sh` | Wrapper for `collect-concepts.py` | CI/publiseringspipeline |

### Brukarstøttescript (interaktive)

| Script | Formål | Bruk |
|--------|--------|------|
| `new-model.sh` | Interaktivt script for å lage ny domenemodell | Manuelt køyrd av brukarar |
| `new-begrepskatalog.sh` | Interaktivt script for å lage ny begrepskatalog | Manuelt køyrd av brukarar |
| `new-begrepssamling.sh` | Interaktivt script for å lage ny begrepssamling | Manuelt køyrd av brukarar |
| `new-modellkatalog.sh` | Interaktivt script for å lage ny modellkatalog | Manuelt køyrd av brukarar |
| `bump-version.sh` | Bump semantisk versjon for skjema | Manuelt køyrd av brukarar |

### Diverse verktøy (ikkje brukte i bygg eller CI)

| Script | Formål | Bruk |
|--------|--------|------|
| `add-schema-header-comments.py` | Legg til header-kommentarar i schema | Ad-hoc vedlikehald |
| `inject-validation-policy.py` | Inject validation policy i schema | Ad-hoc vedlikehald |
| `list-tool-licenses.py` | List lisensar for verktøy | Ad-hoc vedlikehald |
| `update-schema-dates.py` | Oppdater datoar i schema | Ad-hoc vedlikehald |
| `validate-modelldcat.py` | Valider ModellDCAT-instansar | Ad-hoc vedlikehald |
| `pr-linkml-interactive.bash` | Interaktiv PR-rettleiing | Utviklarhjelp |

## Forslag til ny struktur

```
src/assets/scripts/
  makefile/           ← NY — script brukte av Makefile til å generere artefaktar
    filter_container.awk
    filter_erdiagram.py
    filter_plantuml.py
    fix-xsd-dates.py
    gen-asyncapi.py
    gen-openapi.py
    gen-docgen-examples.py
    gen-dqv-measurements.py
    gen-modelldcat-elements.py
    generate-informasjonsmodell.py
    generate-modellkatalog.py
    update-modellkatalog.py
    save-validation-log.py
    run-schema-validation.py
    generate-readme-tables.sh
    gen-config.sh
    check-prereqs.bash
  
  ci/                   ← NY — script brukte berre i CI
    filter-unchanged-logs.py
    collect-concepts.py
    collect-concepts.sh
  
  validation/           ← NY — validerings-script (delt mellom Makefile og CI)
    run-validation.sh
  
  tools/                ← NY — brukarstøttescript og diverse verktøy
    new-model.sh
    new-begrepskatalog.sh
    new-begrepssamling.sh
    new-modellkatalog.sh
    bump-version.sh
    add-schema-header-comments.py
    inject-validation-policy.py
    list-tool-licenses.py
    update-schema-dates.py
    validate-modelldcat.py
    pr-linkml-interactive.bash
```

**Alternativ:** Behald kun `makefile/`-katalogen for Makefile-script, flytt reine CI-script til `.github/scripts/`, og la resten stå i `src/assets/scripts/` (enklare, mindre endringar).

## Tiltak

### Alternativ A: Full reorganisering (4 nye katalog)

1. Opprett nye katalogar
2. Flytt script til `makefile/`
3. Flytt script til `ci/`
4. Flytt script til `validation/`
5. Flytt script til `tools/`
6. Oppdater referansar i Makefile
7. Oppdater referansar i `.github/workflows/validate.yml`
8. Oppdater dokumentasjon

### Alternativ B: makefile/ + .github/scripts/ (anbefalt — enklare)

1. Opprett `src/assets/scripts/makefile/`
2. Opprett `.github/scripts/`
3. Flytt Makefile-brukte script til `makefile/`
4. Flytt reine CI-script til `.github/scripts/`
5. Oppdater referansar i Makefile
6. Oppdater referansar i `.github/workflows/validate.yml`
7. Oppdater dokumentasjon

**Anbefaling:** **Alternativ B** — det gjer størstedelen av gevinsten (skil byggelogikk frå CI frå brukarstøtte) utan å introdusere for mange nye katalogar. Reine CI-script høyrer naturleg heime i `.github/`-katalogen.

## Handlingsliste (Alternativ B)

- [x] 1. Opprett `src/assets/scripts/makefile/` katalog
- [x] 2. Opprett `.github/scripts/` katalog
- [x] 3. Flytt 17 Makefile-brukte script til `makefile/`
- [x] 4. Flytt 3 reine CI-script til `.github/scripts/`
- [x] 5. Oppdater alle Makefile-referansar (ca. 40 stader)
- [x] 6. Oppdater referansar i `.github/workflows/validate.yml` (1 stad)
- [x] 7. Verifiser at `make check-prereqs` køyrer utan feil
- [ ] 8. Verifiser at CI-workflow køyrer utan feil (validér lokalt eller i PR)
- [x] 9. Oppdater dokumentasjon (mkdocs/docs/index-md-struktur.md)

## Utført

Alle tiltak er utførte. Verifisering viser:

- ✅ `src/assets/scripts/makefile/` inneheld 17 script
- ✅ `.github/scripts/` inneheld 3 script (filter-unchanged-logs.py, collect-concepts.py, collect-concepts.sh)
- ✅ `src/assets/scripts/` inneheld 12 script (run-validation.sh + brukarstøtte + diverse)
- ✅ `make check-prereqs` køyrer utan feil
- ✅ Ingen referansar til gamle stiar i Makefile (alle oppdaterte)
- ✅ Referansar i `.github/workflows/validate.yml` oppdaterte (1 stad)
- ✅ Dokumentasjon oppdatert (`mkdocs/docs/index-md-struktur.md`)

**Git-status:**
- 17 script flytta frå `src/assets/scripts/` til `src/assets/scripts/makefile/`
- 3 script flytta frå `src/assets/scripts/` til `.github/scripts/`
- Makefile oppdatert (17 scriptnamn × fleire referansar = ~40 endringar)
- `.github/workflows/validate.yml` oppdatert (1 referanse)

CI-verifisering (punkt 8) vert gjort i PR.

## Script som skal flyttast til `.github/scripts/` (Alternativ B)

Desse skal flyttast til `.github/scripts/` fordi dei **berre** vert brukte i CI:

- `filter-unchanged-logs.py` — brukt av `.github/workflows/validate.yml`
- `collect-concepts.py` — brukt av CI/publiseringspipeline
- `collect-concepts.sh` — brukt av CI/publiseringspipeline

## Script som **ikkje** skal flyttast (Alternativ B)

Desse skal bli verande i `src/assets/scripts/`:

- `run-validation.sh` — brukt av **både** Makefile og CI (delt)
- `new-model.sh` — brukarstøtte
- `new-begrepskatalog.sh` — brukarstøtte
- `new-begrepssamling.sh` — brukarstøtte
- `new-modellkatalog.sh` — brukarstøtte
- `bump-version.sh` — brukarstøtte
- `add-schema-header-comments.py` — diverse
- `inject-validation-policy.py` — diverse
- `list-tool-licenses.py` — diverse
- `update-schema-dates.py` — diverse
- `validate-modelldcat.py` — diverse
- `pr-linkml-interactive.bash` — diverse
