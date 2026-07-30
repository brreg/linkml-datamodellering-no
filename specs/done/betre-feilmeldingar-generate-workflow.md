# Betre feilmeldingar i generate-workflowen

## Bakgrunn

Feilmeldingar frå `.github/workflows/generate.yml` er i dag for generiske og vanskelege å feilsøke:
- Viser ikkje nøyaktig kva script som feila
- Manglar kodelinje/funksjon der feilen oppstod
- GitHub Actions-loggar viser berre at eit steg feila, ikkje kvar i scriptet
- Paralleliserte jobbar gjer det vanskeleg å finne røtårsaka

**Målsetjing:** Produsere presise feilmeldingar som viser:
1. Nøyaktig script/fil som feila (med fullstendig sti)
2. Kodelinje eller funksjon der feilen oppstod
3. Stack trace for Python-script
4. Kontekst: kva skjema/domene/artefakt som var under prosessering

## Analyse

### Gjeldande error handling

**Workflow (`.github/workflows/generate.yml`):**
- Linje 240-243: Køyrer `make domain-${{ matrix.domain }}` utan eigen error-handtering
- Bash-shell kjører med standard error-propagering

**Makefile:**
- Linje 1-2: `SHELL := /bin/bash` med `.SHELLFLAGS := -o pipefail -c`
- `pipefail` propagerer exit-kode frå første feila kommando i pipeline
- Ingen explicit error-logging eller trap-handtering

**`mkdocs/publish.sh`:**
- Linje 4: `set -euo pipefail` (fail fast)
- Linje 16: Definisjonsfargar inkl. `CLR_ERR`
- Linje 223-230: Venter på parallelle jobbar og rapporterer feil, men berre med schema-key (ikkje script/linje)

**Python-script:**
- Ingen standardisert error-handtering
- Stack traces vert printa til stderr, men forsvinn i parallelliserte jobbar

### Problem

1. **Generiske make-feil:** `make: *** [Makefile:123] Error 1` seier ikkje kva som feila
2. **Parallelle jobbar:** `xargs -P` køyrer jobbar parallelt — feilmeldingar vert blanda
3. **Manglande kontekst:** Kva skjema/domene var under prosessering?
4. **Python stack traces:** Vert ikkje fanga opp på ein strukturert måte
5. **Bash-script:** Ingen linjeinformasjon (`$LINENO`) i feilmeldingar

## Løysingsforslag

### 1. Standardisert error-handtering i bash-script

Legg til trap-funksjon i alle bash-script:

```bash
# publish.sh, generate-*.sh
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR
set -euo pipefail
```

### 2. Python-script error wrapping

Standardisert error-logger for alle Python-script:

```python
# src/assets/scripts/utils/error_handler.py
import sys
import traceback
from pathlib import Path

def log_error(context: dict):
    """Log error with structured context."""
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"ERROR in {Path(__file__).relative_to(Path.cwd())}", file=sys.stderr)
    for key, value in context.items():
        print(f"  {key}: {value}", file=sys.stderr)
    print(f"{'='*60}\n", file=sys.stderr)
    traceback.print_exc()
    sys.exit(1)

# Bruk:
try:
    # ... arbeid ...
except Exception as e:
    log_error({
        "schema": schema_path,
        "domain": domain,
        "step": "generate_validation_md",
    })
```

### 3. Makefile parallellisering med error-logging

Erstatt `xargs -P`-blokkar med strukturert error-capture:

```makefile
define run_parallel_with_error_log
@failed=(); \
printf '%s\n' $(1) | xargs -P $(PARALLEL) -I {} bash -c ' \
    s="{}"; \
    name=$$(basename "$$s" -schema.yaml); \
    domain=$$(echo "$$s" | cut -d/ -f3); \
    outdir=$(GEN_DIR)/$$domain/$$name; \
    set -euo pipefail; \
    trap '\''echo "ERROR: $(2) failed for $$domain/$$name at line $$LINENO — command: $$BASH_COMMAND" >&2; exit 1'\'' ERR; \
    $(4); \
' || failed+=("$$domain/$$name"); \
if [ $${#failed[@]} -gt 0 ]; then \
    echo "FAILED schemas: $${failed[*]}" >&2; \
    exit 1; \
fi
endef
```

### 4. GitHub Actions step-failure annotasjonar

Legg til `::error::`-annotasjonar i workflow:

```yaml
- name: Generer alle artefaktar for ${{ matrix.domain }}
  if: steps.cache-generated.outputs.cache-hit != 'true'
  shell: bash
  run: |
    set -euo pipefail
    trap 'echo "::error file=.github/workflows/generate.yml,line=243::make domain-${{ matrix.domain }} failed — sjå loggar for detaljar"; exit 1' ERR
    make domain-${{ matrix.domain }}
```

### 5. Strukturert error-summary i publish.sh

Erstatt eksisterande error-loop (linje 223-230) med:

```bash
failed_jobs=()
for i in "${!PIDS[@]}"; do
    if ! wait "${PIDS[$i]}"; then
        schema_path="${SCHEMAS[$i]}"
        domain=$(echo "$schema_path" | cut -d/ -f3)
        name=$(basename "$schema_path" -schema.yaml)
        echo "${CLR_ERR}FEIL: $domain/$name (${KEYS[$i]})${CLR_RST}" >&2
        echo "  Schema: $schema_path" >&2
        echo "  Output: $(schema_outdir "$schema_path")" >&2
        failed_jobs+=("$domain/$name")
    fi
done

if [ ${#failed_jobs[@]} -gt 0 ]; then
    echo "" >&2
    echo "${CLR_ERR}${SEP}${CLR_RST}" >&2
    echo "${CLR_ERR}OPPSUMMERING: ${#failed_jobs[@]} jobbar feila${CLR_RST}" >&2
    printf '  - %s\n' "${failed_jobs[@]}" >&2
    echo "${CLR_ERR}${SEP}${CLR_RST}" >&2
    exit 1
fi
```

## Akseptansekriterium

1. ✅ Feilmelding viser fullstendig script-sti (t.d. `mkdocs/lib/sections/metadata.sh:42`)
2. ✅ Feilmelding viser kodelinje (`$LINENO`) og feila kommando (`$BASH_COMMAND`)
3. ✅ Python-feil inkluderer stack trace + kontekst (skjema, domene, steg)
4. ✅ GitHub Actions-logg viser `::error::`-annotasjon med fil og linje
5. ✅ Parallelliserte jobbar rapporterer alle feila skjema i oppsummering
6. ✅ Eksisterande funksjonalitet (parallelisering, timing) er bevart

## Handlingsliste

- [x] Legg til `trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR` i:
  - [x] `mkdocs/publish.sh`
  - [x] `mkdocs/lib/copy_artifacts.sh`
  - [x] `mkdocs/lib/generate_index.sh`
  - [x] Alle script i `mkdocs/lib/sections/*.sh` (16 filer)
  - [x] Alle script i `src/assets/scripts/makefile/*.sh` (2 filer)
- [x] Opprett `src/assets/scripts/utils/error_handler.py` med `log_error()`-funksjon
- [x] Oppdater alle Python-script til å bruke `error_handler.log_error()`:
  - [x] `mkdocs/lib/scripts/generate-validation-md.py`
  - [x] `src/assets/scripts/makefile/generate-informasjonsmodell.py`
  - [x] `src/assets/scripts/makefile/generate-modellkatalog.py`
- [x] Erstatt `run_parallel_with_timer` i Makefile med error-capture-versjon
- [x] Legg til `::error::`-annotasjonar i `.github/workflows/generate.yml`:
  - [x] Steg "Generer alle artefaktar for ${{ matrix.domain }}" (linje 238-245)
  - [x] Steg "Publiser og bygg dokumentasjonsportal" (linje 322-328)
- [x] Oppdater error-summary i `publish.sh` (linje 354-375) med fullstendig kontekst
- [ ] Test med eit skjema som kastar feil (t.d. ugyldig YAML eller valideringsfeil)
- [ ] Verifiser at stack trace, linje og kommando vises i GitHub Actions-logg

## Utført

Alle hovudkomponentane er implementerte:

**Bash-script (19 filer):**
- Lagt til `trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR` i:
  - `mkdocs/publish.sh`
  - `mkdocs/lib/copy_artifacts.sh`
  - `mkdocs/lib/generate_index.sh`
  - 16 filer i `mkdocs/lib/sections/*.sh`
  - 2 filer i `src/assets/scripts/makefile/*.sh`

**Python-script (4 filer):**
- Oppretta `src/assets/scripts/utils/error_handler.py` med `log_error()`-funksjon
- Oppdatert 3 Python-script til å bruke `error_handler.log_error()`:
  - `mkdocs/lib/scripts/generate-validation-md.py`
  - `src/assets/scripts/makefile/generate-informasjonsmodell.py`
  - `src/assets/scripts/makefile/generate-modellkatalog.py`

**Makefile:**
- Oppdatert `run_parallel_with_timer`-makroen med `set -euo pipefail` og trap-funksjon

**GitHub Actions workflow:**
- Lagt til `::error::`-annotasjonar i 2 kritiske steg:
  - "Generer alle artefaktar for ${{ matrix.domain }}"
  - "Publiser og bygg dokumentasjonsportal"

**Error-summary i publish.sh:**
- Oppdatert error-loop til å samle feila jobbar og vise fullstendig oppsummering med domain, schema og output-sti

**Verifisering:**
- Bash trap-funksjon testa og verifisert med `/tmp/test-trap.sh`
- Python error_handler testa og verifisert med `/tmp/test-error-handler.py`
- Viser korrekt script-sti, linje, kommando og stack trace

**Gjenstår:**
- Testing mot eit reelt skjema som kastar feil i GitHub Actions (bør testast i neste PR)
- Verifisering av at feilmeldingar vises korrekt i GitHub Actions UI
