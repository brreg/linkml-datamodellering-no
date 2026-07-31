# Vurdering: Flytte make-script frå src/assets/scripts/makefile/ til make/

## Bakgrunn

Make-relaterte script ligg i `src/assets/scripts/makefile/`, medan Makefile-modular ligg i `make/*.mk`. Spørsmålet er om desse scripta bør flyttast til `make/` for betre samlokalisering.

## Noverande struktur

```
make/
  *.mk                          # Makefile-modular (13 filer)

src/assets/scripts/makefile/
  *.py                          # Python-script brukt av make (15 filer)
  *.sh                          # Bash-script brukt av make (5 filer)
```

**Døme på script:**
- `generate-informasjonsmodell.py` — genererer ModelDCAT-AP-NO-metadata
- `update-modellkatalog.py` — oppdaterer modellkatalog frå annotations
- `gen-dqv-measurements.py` — genererer DQV-kvalitetsmålingar
- `run-schema-validation.py` — køyrer MCP-validering parallelt
- `check-prereqs.bash` — sjekkar at nødvendige verktøy er installerte

## Alternativ 1: Flytt til make/scripts/

**Struktur:**
```
make/
  *.mk
  scripts/
    *.py
    *.sh
```

**Fordelar:**
- **Samlokalisering** — alt relatert til make-systemet på same stad
- **Enklare å finne** — når ein jobbar med Makefile, er scriptet ein naturleg del
- **Kortare sti** — `make/scripts/` vs `src/assets/scripts/makefile/`

**Ulemper:**
- **Bryt skil mellom kjeldekode og byggsystem** — `make/` er byggsystemkonfigurasjon, `src/` er kjeldekode
- **Krev omfattande endringar:**
  - Alle `$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/*.py` → `/work/make/scripts/*.py`
  - Alle `bash src/assets/scripts/makefile/*.sh` → `bash make/scripts/*.sh`
  - Container-mount i `make/01-containers.mk` må justerast
  - CI workflows som refererer desse stiane må oppdaterast
- **Inkonsistent med andre assets** — `src/assets/` inneheld templates, containers, scripts
- **Scripts kan vere nyttige utanfor make** — t.d. `generate-informasjonsmodell.py` kan kallast direkte

## Alternativ 2: Behald i src/assets/scripts/makefile/

**Fordelar:**
- **Etablert struktur som fungerer** — ingen breaking changes
- **Klar separasjon** — `make/` er konfigurasjon, `src/` er kjeldekode
- **Konsistent med andre assets** — `src/assets/templates/`, `src/assets/containers/`
- **Enklare container-mount** — `/work` mountar heile repoet, scriptstiane er stabile

**Ulemper:**
- **Lang sti** — `src/assets/scripts/makefile/` er 4 nivå djupt
- **Ikkje samlokalisert** — må hoppe mellom `make/` og `src/assets/scripts/makefile/`

## Alternativ 3: Hybrid — flytt berre reine make-hjelpeverktøy

Behald script som genererer domenedata i `src/assets/scripts/makefile/`, men flytt reine byggsystem-hjelpeverktøy til `make/scripts/`:

**Flytt til make/scripts/:**
- `gen-config.sh` — genererer config.mk
- `check-prereqs.bash` — sjekkar verktøy
- `detect-validation-policy.py` — auto-detekterer policy

**Behald i src/assets/scripts/makefile/:**
- `generate-informasjonsmodell.py` — genererer domenedata
- `update-modellkatalog.py` — oppdaterer domenedata
- `gen-dqv-measurements.py` — genererer domenedata
- `collect-concepts.py` — genererer domenedata

**Fordelar:**
- **Balanserer samlokalisering og separasjon**
- **Færre endringar** (berre 3 filer flyttast)

**Ulemper:**
- **Subjektiv grense** — kva er "rein make-hjelpeverktøy" vs "domenedatagenerator"?
- **Forvirrande** — kvifor er nokre script i `make/` og andre i `src/`?

## Anbefaling

**Behald i src/assets/scripts/makefile/** (Alternativ 2).

**Grunngjeving:**
1. **Fungerer godt** — ingen konkrete problem med noverande struktur
2. **Scripts er kjeldekode** — dei genererer artefaktar, ikkje byggsystemkonfigurasjon
3. **Kostnad vs nytte** — flytting krev mange endringar for marginal gevinst
4. **Konsistent** — følgjer mønsteret `src/assets/<type>/`

**Mogeleg forbetring utan flytting:**
- Legg til `make/README.md` som dokumenterer kor scripta ligg
- Legg til kommentarar i `.mk`-filer som peikar til relaterte script

## Testar

Dersom vi bestemmer oss for flytting:

```bash
# Identifiser alle referansar
grep -r "src/assets/scripts/makefile" make/ Makefile .github/

# Oppdater alle stiar
find make/ Makefile -type f -exec sed -i 's|src/assets/scripts/makefile|make/scripts|g' {} +

# Flytt filer
mkdir -p make/scripts
mv src/assets/scripts/makefile/* make/scripts/
rmdir src/assets/scripts/makefile

# Test
make test
make validate-bronze DOMAIN=ap-no
```

## Avgjerd

**Status:** Ferdig — scripta vert behaldne i `src/assets/scripts/makefile/`.

**Implementert:**
1. `make/README.md` — dokumenterer struktur, relaterte script og konvensjonar
2. Kommentarar i `.mk`-filer — peikar til relaterte script i `src/assets/scripts/makefile/`
   - `make/30-instances.mk` → `generate-informasjonsmodell.py`, `generate-modellkatalog.py`, `collect-concepts.py`
   - `make/40-validation.mk` → `detect-validation-policy.py`, `run-schema-validation.py`, `save-validation-log.py`, `emit-github-validation-annotations.py`
   - `make/50-docs.mk` → `mkdocs/publish.sh`, `generate-readme-tables.sh`
   - `make/90-tools.mk` → `check-prereqs.bash`

**Resultat:** Lettare å finne relaterte script utan å flytte dei.
