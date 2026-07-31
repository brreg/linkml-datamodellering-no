# Vurdering: Gruppering av script i src/assets/scripts/

## Noverande struktur

```
src/assets/scripts/
  *.py, *.sh                  # 11 script i rotkatalog
  makefile/                   # 22 make-relaterte script
  utils/                      # 1 hjelpemodul (error_handler.py)
  migreringsscript/           # 2 egangs-migreringsscript

.github/scripts/
  filter-unchanged-logs.py    # 1 CI-script

scripts/
  migrate-schema-metadata.sh  # 1 egangs-migreringsscript (bør flyttast til src/assets/scripts/migreringsscript/)
```

**Script i rotkatalog (11):**
- `add-schema-header-comments.py` — manuelt verktøy: legg til header-kommentarar i skjema
- `bump-version.sh` — manuelt verktøy: bump versjon basert på conventional commits
- `inject-validation-policy.py` — manuelt verktøy: injiser validation_policy i index.md
- `list-tool-licenses.py` — manuelt verktøy: list lisensar for verktøy
- `new-begrepskatalog.sh` — scaffolding: brukt av `make new-begrepskatalog`
- `new-begrepssamling.sh` — scaffolding: brukt av `make new-begrepssamling`
- `new-model.sh` — scaffolding: brukt av `make new-model`
- `new-modellkatalog.sh` — scaffolding: brukt av `make new-modellkatalog`
- `pr-linkml-interactive.bash` — dev-verktøy: interaktiv LinkML-REPL
- `run-validation.sh` — **CI-script**: køyr validering med logging (brukt i .github/workflows/validate.yml)
- `update-schema-dates.py` — manuelt verktøy: oppdater dato-felt i skjema
- `validate-modelldcat.py` — manuelt verktøy: valider ModelDCAT-instans

**Observasjonar:**
1. **4 scaffolding-script** (`new-*.sh`) — brukt av `make/70-scaffolding.mk`
2. **2 CI-script** (`run-validation.sh` i `src/assets/scripts/`, `filter-unchanged-logs.py` i `.github/scripts/`)
3. **4 manuelle vedlikehalds-verktøy** (`add-schema-header-comments.py`, `update-schema-dates.py`, `bump-version.sh`, `inject-validation-policy.py`)
4. **1 verktøy-script** (`list-tool-licenses.py`)
5. **1 dev-verktøy** (`pr-linkml-interactive.bash`)
6. **1 validerings-verktøy** (`validate-modelldcat.py`)

## Foreslått gruppering

### Alternativ 1: Full gruppering etter funksjon

```
src/assets/scripts/
  makefile/                   # 22 make-relaterte script (eksisterer)
  scaffolding/                # 4 new-*.sh script
  ci/                         # 2 CI-script (ny)
  maintenance/                # 4 manuelle vedlikehalds-verktøy
  dev-tools/                  # pr-linkml-interactive.bash
  utils/                      # error_handler.py, list-tool-licenses.py, validate-modelldcat.py
  migreringsscript/           # 3 egangs-migreringsscript (eksisterer + migrate-schema-metadata.sh)

.github/scripts/              # TOM (flytta til src/assets/scripts/ci/)
scripts/                      # TOM (flytta til src/assets/scripts/migreringsscript/)
```

**Fordelar:**
- **Klar separasjon** — kvar katalog har eitt ansvar
- **Lettare å finne** — script grupperte etter kva dei gjer
- **Konsekvent** — følgjer eksisterande mønster (`makefile/`, `migreringsscript/`)

**Ulemper:**
- **Krev omfattande endringar:**
  - Alle `bash src/assets/scripts/new-*.sh` → `bash src/assets/scripts/scaffolding/new-*.sh`
  - Oppdater `make/70-scaffolding.mk`
  - Oppdater dokumentasjon

**Mapping:**

| Script | Frå | Til |
|---|---|---|
| `new-begrepskatalog.sh` | `src/assets/scripts/` | `src/assets/scripts/scaffolding/` |
| `new-begrepssamling.sh` | `src/assets/scripts/` | `src/assets/scripts/scaffolding/` |
| `new-model.sh` | `src/assets/scripts/` | `src/assets/scripts/scaffolding/` |
| `new-modellkatalog.sh` | `src/assets/scripts/` | `src/assets/scripts/scaffolding/` |
| `run-validation.sh` | `src/assets/scripts/` | `src/assets/scripts/ci/` |
| `filter-unchanged-logs.py` | `.github/scripts/` | `src/assets/scripts/ci/` |
| `migrate-schema-metadata.sh` | `scripts/` | `src/assets/scripts/migreringsscript/` |
| `add-schema-header-comments.py` | `src/assets/scripts/` | `src/assets/scripts/maintenance/` |
| `update-schema-dates.py` | `src/assets/scripts/` | `src/assets/scripts/maintenance/` |
| `bump-version.sh` | `src/assets/scripts/` | `src/assets/scripts/maintenance/` |
| `inject-validation-policy.py` | `src/assets/scripts/` | `src/assets/scripts/maintenance/` |
| `pr-linkml-interactive.bash` | `src/assets/scripts/` | `src/assets/scripts/dev-tools/` |
| `validate-modelldcat.py` | `src/assets/scripts/` | `src/assets/scripts/utils/` |
| `list-tool-licenses.py` | `src/assets/scripts/` | `src/assets/scripts/utils/` |

### Alternativ 2: Scaffolding + CI + migreringsscript

```
src/assets/scripts/
  makefile/                   # 22 make-relaterte script (eksisterer)
  scaffolding/                # 4 new-*.sh script (ny)
  ci/                         # 2 CI-script (ny)
  *.py, *.sh                  # 5 andre script (beheld i rotkatalog)
  utils/                      # error_handler.py
  migreringsscript/           # 3 egangs-migreringsscript (eksisterer + migrate-schema-metadata.sh)

.github/scripts/              # TOM (flytta til src/assets/scripts/ci/)
scripts/                      # TOM (flytta til src/assets/scripts/migreringsscript/)
```

**Fordelar:**
- **Moderat endring** — flytt 7 script (4 scaffolding + 2 CI + 1 migreringsscript)
- **Scaffolding, CI og migreringsscript er klart avgrensa** — naturlege grupper
- **Samlokaliserer CI-script** — alle CI-script på same stad (i staden for split mellom `.github/scripts/` og `src/assets/scripts/`)
- **Samlokaliserer migreringsscript** — alle migreringsscript i `src/assets/scripts/migreringsscript/`
- **Fjernar `scripts/`-katalog** — berre `src/assets/scripts/` att
- **Reduserer rotkatalog** — frå 11 til 5 script (55% reduksjon)

**Ulemper:**
- **Rotkatalogen framleis har 5 script** — 4 maintenance + 1 dev-tool

**Påverka filer:**
- `make/70-scaffolding.mk` — oppdater 4 stiar til scaffolding-script
- `.github/workflows/validate.yml` — oppdater 2 stiar til CI-script

### Alternativ 3: Berre CI

```
src/assets/scripts/
  makefile/                   # 22 make-relaterte script (eksisterer)
  ci/                         # 2 CI-script (ny)
  *.py, *.sh                  # 9 andre script (beheld i rotkatalog)
  utils/                      # error_handler.py
  migreringsscript/           # 2 egangs-migreringsscript

.github/scripts/              # TOM (flytta til src/assets/scripts/ci/)
```

**Fordelar:**
- **Minimal endring** — flytt berre 2 CI-script
- **Samlokaliserer CI-script** — alle CI-script på same stad
- **Konsekvent** — følgjer mønsteret `src/assets/scripts/<type>/`

**Ulemper:**
- **Rotkatalogen framleis rotete** — 9 script (4 scaffolding + 4 maintenance + 1 dev-tool)

**Påverka filer:**
- `.github/workflows/validate.yml` — oppdater 2 stiar til CI-script

### Alternativ 4: Behald som det er

```
src/assets/scripts/
  *.py, *.sh                  # 11 script i rotkatalog
  makefile/                   # 22 make-relaterte script
  utils/                      # 1 hjelpemodul
  migreringsscript/           # 2 egangs-migreringsscript
```

**Fordelar:**
- **Fungerer godt** — ingen konkrete problem
- **Ingen breaking changes**
- **Etablert struktur**

**Ulemper:**
- **Rotkatalogen kan verte rotete** ved fleire script

## Anbefaling

**Implementer Alternativ 2: Scaffolding + CI**

**Grunngjeving:**
1. **Scaffolding, CI og migreringsscript er naturlege grupper** — klart avgrensa ansvarsområde
2. **Samlokaliserer CI-script** — alle CI-script flyttes frå `.github/scripts/` til `src/assets/scripts/ci/`
3. **Samlokaliserer migreringsscript** — flytt `scripts/migrate-schema-metadata.sh` til `src/assets/scripts/migreringsscript/`
4. **Moderat kostnad** — 7 filer flyttast, 2 filer oppdaterast (`make/70-scaffolding.mk`, `.github/workflows/validate.yml`)
5. **Betydeleg forbetring** — reduserer rotkatalog frå 11 til 5 script (55% reduksjon)
6. **Konsistent med eksisterande mønster** — `makefile/` og `migreringsscript/` er allereie grupperte
7. **Fjernar `scripts/`-katalog** — ryddig struktur med berre `src/assets/scripts/`

**Kvifor ikkje Alternativ 1 (full gruppering)?**
- **Overengineering** — 4 maintenance-script og 1 dev-tool i rotkatalogen er ikkje eit problem
- **Diskutabel kategorisering** — `validate-modelldcat.py` er både validering og utils
- **Meir arbeid** — 14 filer flyttast i staden for 7

**Kvifor ikkje Alternativ 3 (berre CI)?**
- **Halvvegs** — rotkatalogen framleis har 9 script (berre 18% reduksjon)
- **Scaffolding er like naturleg gruppe som CI**

**Kvifor ikkje Alternativ 4 (behald som det er)?**
- **Split av CI-script** — `.github/scripts/` og `src/assets/scripts/` er inkonsistent
- **CI-script bør samlokaliseras** — lettare å finne og vedlikehalde

## Implementering (Alternativ 2)

```bash
# Opprett katalogar
mkdir -p src/assets/scripts/scaffolding
mkdir -p src/assets/scripts/ci

# Flytt scaffolding-script
mv src/assets/scripts/new-*.sh src/assets/scripts/scaffolding/

# Flytt CI-script
mv src/assets/scripts/run-validation.sh src/assets/scripts/ci/
mv .github/scripts/filter-unchanged-logs.py src/assets/scripts/ci/

# Flytt migreringsscript
mv scripts/migrate-schema-metadata.sh src/assets/scripts/migreringsscript/

# Fjern tomme katalogar
rmdir .github/scripts/
rmdir scripts/

# Oppdater make/70-scaffolding.mk
sed -i 's|src/assets/scripts/new-|src/assets/scripts/scaffolding/new-|g' make/70-scaffolding.mk

# Oppdater .github/workflows/validate.yml
sed -i 's|bash src/assets/scripts/run-validation.sh|bash src/assets/scripts/ci/run-validation.sh|g' .github/workflows/validate.yml
sed -i 's|python3 .github/scripts/filter-unchanged-logs.py|python3 src/assets/scripts/ci/filter-unchanged-logs.py|g' .github/workflows/validate.yml

# Test
make new-model
```

**Påverka filer:**
- `make/70-scaffolding.mk` — oppdater 4 stiar til scaffolding-script
- `.github/workflows/validate.yml` — oppdater 2 stiar til CI-script

## Samanlikning

| Alternativ | Script flytta | Påverka filer | Rotkatalog før | Rotkatalog etter | Reduksjon |
|---|---|---|---|---|---|
| 1. Full gruppering | 14 | make/70-scaffolding.mk, .github/workflows/validate.yml | 11 | 0 | 100% |
| 2. Scaffolding + CI + migreringsscript | 7 | make/70-scaffolding.mk, .github/workflows/validate.yml | 11 | 5 | 55% |
| 3. Berre CI | 2 | .github/workflows/validate.yml | 11 | 9 | 18% |
| 4. Behald | 0 | ingen | 11 | 11 | 0% |

**Anbefaling:** Alternativ 2 gjev best balanse mellom forbetring og kostnad.

## Alternativ framtid

Dersom `src/assets/scripts/` veks til 15+ script i rotkatalogen (etter at scaffolding og CI er flytta), kan vi vurdere Alternativ 1 (full gruppering).

## Avgjerd

**Status:** Ferdig — Alternativ 2 implementert.

**Utført:**
- Oppretta `src/assets/scripts/scaffolding/` og `src/assets/scripts/ci/`
- Flytta 4 scaffolding-script til `scaffolding/`
- Flytta 2 CI-script til `ci/`
- Flytta 1 migreringsscript til `migreringsscript/`
- Fjerna `.github/scripts/` og `scripts/`-katalogar
- Oppdatert `make/70-scaffolding.mk` (4 stiar)
- Oppdatert `.github/workflows/validate.yml` (2 stiar)

**Resultat:**
```
src/assets/scripts/
  scaffolding/        # 4 new-*.sh
  ci/                 # 2 CI-script
  makefile/           # 22 make-script
  migreringsscript/   # 3 migreringsscript
  utils/              # 1 hjelpemodul
  *.py, *.sh          # 5 andre script (maintenance + dev-tools)
```

Rotkatalog redusert frå 11 til 5 script (55% reduksjon).
