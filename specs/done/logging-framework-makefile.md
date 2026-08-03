# Innfør strukturert logging med nivå og timing i Makefile

## Bakgrunn

I dag brukar make-systemet fargekodar (`CLR_STEP`, `CLR_HDR` osv.) og ustrukturert echo/printf-logging. Det er vanskeleg å:
- Filtrere loggar basert på alvorlegheitsgrad (feil vs. debug-info)
- Måle kjøretid for individuelle kommandoar
- Få oversikt over kva script og funksjonar som vert køyrte
- Debugge parallelle køyringar (xargs -P)

## Krav

**Loggnivå:**
- `DEBUG` — vis alle script- og funksjonskall + timing + alle eksisterande loggar
- `INFO` (default) — dagens logging (status-meldingar, framgang, summarar)
- `ERROR` — berre feil og kritiske åtvaringar

**Timing:**
- Alle script- og funksjonskall skal loggast med kjøretid (t.d. "→ gen-doc  samt/samt-bu (3.2s)")
- Eksisterande timing-output (t.d. i `run_gen_parallel`) skal behaldast

**Implementasjon:**
- `LOGLVL`-variabel i `make/00-settings.mk` (default: `INFO`)
- Overstyrbar frå kommandolinje: `make gen-doc LOGLVL=DEBUG`
- Logge-hjelpefunksjonar: `log_debug`, `log_info`, `log_error` (bash-funksjonar eller makroar)
- Eksisterande `CLR_*`-fargar skal behaldast for INFO-nivå

**Kompatibilitet:**
- Eksisterande make-targets skal fungere utan endringar
- GitHub Actions skal framleis få strukturerte feilmeldingar (`::error file=...`)
- Parallelle køyringar (xargs -P) skal kunne loggast utan å vri saman output

## Løysing

### 1. Logging-funksjonar i `make/00-settings.mk`

Legg til følgjande variablar og funksjonar:

```makefile
# Logging
LOGLVL ?= INFO

# Logging-hjelpefunksjonar (bash-snippet som kan sourcas eller inliinast)
define LOG_FUNCTIONS
log_debug() {
  [[ "$(LOGLVL)" == "DEBUG" ]] && printf "[DEBUG] %s\n" "$$*" >&2 || true
}
log_info() {
  [[ "$(LOGLVL)" != "ERROR" ]] && printf "%s\n" "$$*" >&2 || true
}
log_error() {
  printf "[ERROR] %s\n" "$$*" >&2
}
timed_run() {
  local label="$$1"; shift
  local start=$$(date +%s%3N)
  log_debug "→ $$label: $$*"
  "$$@"
  local elapsed=$$(( $$(date +%s%3N) - start ))
  log_info "$$(printf '$(CLR_STEP)→ %s$(CLR_RST) (%d.%ds)' "$$label" $$((elapsed / 1000)) $$((elapsed % 1000 / 100)))"
}
endef
export LOG_FUNCTIONS
```

### 2. Bruk i parallelle makroar (`run_gen_parallel`)

I `make/10-generator-macros.mk`, erstatt:

```makefile
printf "$(CLR_STEP)→ $(2)  %s/%s$(CLR_RST) (%d.%ds)\n" \
  "$$domain" "$$name" $$((elapsed / 1000)) $$((elapsed % 1000 / 100));
```

med:

```bash
eval "$$LOG_FUNCTIONS"; \
log_info "$$(printf '$(CLR_STEP)→ $(2)  %s/%s$(CLR_RST) (%d.%ds)' \
  "$$domain" "$$name" $$((elapsed / 1000)) $$((elapsed % 1000 / 100)))";
```

Og før køyring av kommandoar:

```bash
eval "$$LOG_FUNCTIONS"; \
log_debug "Køyrer: $(LINKML_RUN) $(2) $$s ..."; \
# ... eksisterande kommando ...
```

### 3. Bruk i serielle makroar (`run_gen`)

Erstatt `echo "$(CLR_STEP)→ $(2)  $(s)$(CLR_RST)"` med:

```bash
eval "$$LOG_FUNCTIONS"; \
log_info "$(CLR_STEP)→ $(2)  $(s)$(CLR_RST)"; \
log_debug "Kommando: $(LINKML_RUN) $(2) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-$(3)";
```

### 4. Eksempel: `gen-doc` med timing

```makefile
define run_gen_doc
@$(foreach s,$(1), \
  eval "$$LOG_FUNCTIONS"; \
  log_info "$(CLR_STEP)→ gen-doc  $(s)$(CLR_RST)"; \
  log_debug "Køyrer: gen-doc --template-directory ... -d $(call schema_outdir,$(s))/docs $(s)"; \
  start=$$(date +%s%3N); \
  $(LINKML_RUN) gen-doc --template-directory src/assets/templates/docgen ... -d $(call schema_outdir,$(s))/docs $(s); \
  elapsed=$$(( $$(date +%s%3N) - start )); \
  log_info "$$(printf '  Ferdig (%d.%ds)' $$((elapsed / 1000)) $$((elapsed % 1000 / 100)))"; \
)
endef
```

### 5. GitHub Actions-integrering

I `.github/workflows/generate.yml`, sett `LOGLVL=DEBUG` for alle CI-køyringar:

```yaml
- name: Generer alle artefaktar for ${{ matrix.domain }}
  env:
    LOGLVL: DEBUG
  run: make domain-${{ matrix.domain }}
```

**Grunngjeving:** CI-loggar vert lagra i GitHub Actions og er essensielle for feilsøking. DEBUG-nivå gjev full oversikt over kva kommandoar som vert køyrte og kor lang tid kvar kommando tar, utan ekstrakostnad (loggane vert uansett lagra).

Tilsvarande for andre workflows (`validate.yml`, `release.yml` osv.):

```yaml
- name: Valider alle skjema for ${{ matrix.domain }}
  env:
    LOGLVL: DEBUG
  run: |
    for manifest in $(find src/linkml/${{ matrix.domain }} -name build.yaml -type f); do
      bash src/assets/scripts/ci/run-validation.sh --manifest "$manifest"
    done
```

### 6. Dokumentasjon

Oppdater `COMMANDS.md`:

```markdown
## Logging

Køyretid og detaljnivå kan styrast med `LOGLVL`-variabelen:

- `LOGLVL=DEBUG` — vis alle script- og funksjonskall med timing
- `LOGLVL=INFO` (default) — status-meldingar og framgang
- `LOGLVL=ERROR` — berre feil

**Eksempel:**

```bash
make gen-doc SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml LOGLVL=DEBUG
make domain-ngr LOGLVL=ERROR
```
```

## Handlingsliste

- [ ] Legg til `LOGLVL`-variabel og `LOG_FUNCTIONS` i `make/00-settings.mk`
- [ ] Oppdater `run_gen_parallel` i `make/10-generator-macros.mk` til å bruke `log_info`/`log_debug`
- [ ] Oppdater `run_gen_parallel_file_input` i `make/10-generator-macros.mk`
- [ ] Oppdater `run_gen` (serielle køyringar) til å bruke logge-funksjonar
- [ ] Oppdater `run_gen_shacl`, `run_gen_owl`, `run_gen_rdf` til å bruke logge-funksjonar
- [ ] Oppdater `run_gen_doc` til å bruke logge-funksjonar
- [ ] Oppdater `run_gen_erdiagram` til å bruke logge-funksjonar
- [ ] Oppdater `run_gen_plantuml` til å bruke logge-funksjonar
- [ ] Oppdater `run_gen_xsd` til å bruke logge-funksjonar
- [ ] Oppdater `run_gen_asyncapi` til å bruke logge-funksjonar
- [ ] Oppdater `run_gen_openapi` til å bruke logge-funksjonar
- [ ] Oppdater validerings-makroar (`make/40-validation.mk`)
- [ ] Oppdater docs-makroar (`make/50-docs.mk`)
- [ ] Test lokalt med alle tre nivå: `make gen-doc LOGLVL=DEBUG`, `LOGLVL=INFO`, `LOGLVL=ERROR`
- [ ] Verifiser at parallelle køyringar ikkje vrir saman output
- [ ] Oppdater `COMMANDS.md` med logging-dokumentasjon
- [ ] Oppdater `.github/workflows/generate.yml` — sett `LOGLVL=DEBUG` for alle make-kommandoar
- [ ] Oppdater `.github/workflows/validate.yml` — sett `LOGLVL=DEBUG` (dersom den brukar make)
- [ ] Oppdater `.github/workflows/release.yml` — sett `LOGLVL=DEBUG` (dersom den brukar make)
- [ ] Verifiser at GitHub Actions-loggar er lesbare med DEBUG-nivå (ikkje for verbose)

## Kriteria for fullføring

- `make <target>` køyrer med INFO-logging (dagens oppførsel) utan å spesifisere `LOGLVL`
- `make <target> LOGLVL=DEBUG` viser alle script- og funksjonskall med timing
- `make <target> LOGLVL=ERROR` viser berre feil og kritiske åtvaringar
- Alle eksisterande make-targets fungerer utan endringar
- **GitHub Actions brukar `LOGLVL=DEBUG` for alle make-kommandoar** (for full feilsøkingsinfo)
- GitHub Actions-loggar er lesbare og strukturerte med DEBUG-nivå (ikkje for verbose)
- Parallelle køyringar (xargs -P) vrir ikkje saman output
- `COMMANDS.md` dokumenterer `LOGLVL`-variabelen

## Implementasjonsnotat

### Utfordringar med parallelle køyringar

**Problem:** `xargs -P` køyrer kommandoar i parallell, og output frå ulike prosessar kan vri seg saman.

**Løysing 1 (enklast):** Prefikser kvar linje med `[domain/schema]`:

```bash
log_info() {
  [[ "$(LOGLVL)" != "ERROR" ]] && printf "[%s/%s] %s\n" "$$domain" "$$name" "$$*" >&2 || true
}
```

**Løysing 2 (meir avansert):** Buffer output per prosess og skriv atomisk:

```bash
# I xargs-blokka:
output_buffer=$(mktemp)
trap "rm -f $$output_buffer" EXIT
{
  log_info "→ $(2)  $$domain/$$name"
  # ... køyr kommando ...
  log_info "✓ $(2)  $$domain/$$name ($$elapsed)"
} > "$$output_buffer" 2>&1
cat "$$output_buffer" >&2
```

**Valt løysing:** Løysing 1 (prefikser) for enkelheit — parallelle køyringar er allereie separerte per domene/schema, så prefiks gjev nok kontekst.

### Fargar i DEBUG-modus

`CLR_*`-variablane skal behaldast i INFO-modus (dagens fargar), men DEBUG-modus kan bruke ein monokrom stil for å redusere støy:

```bash
log_debug() {
  [[ "$(LOGLVL)" == "DEBUG" ]] && printf "\033[2m[DEBUG]\033[0m %s\n" "$$*" >&2 || true
}
```

### Timing-eksempel

**INFO-nivå:**
```
→ gen-doc  samt/samt-bu (3.2s)
```

**DEBUG-nivå:**
```
[DEBUG] Køyrer: podman run ... gen-doc --template-directory ... samt/samt-bu-schema.yaml
→ gen-doc  samt/samt-bu (3.2s)
```

**ERROR-nivå:**
```
(ingen output dersom ingen feil)
```

## Relaterte filer

- `make/00-settings.mk` — LOGLVL-variabel og LOG_FUNCTIONS
- `make/10-generator-macros.mk` — run_gen_parallel, run_gen, osv.
- `make/40-validation.mk` — validerings-makroar
- `make/50-docs.mk` — docs-makroar
- `COMMANDS.md` — dokumentasjon
- `.github/workflows/generate.yml` — CI-integrering (sett `LOGLVL=DEBUG`)
- `.github/workflows/validate.yml` — CI-validering (sett `LOGLVL=DEBUG` dersom make vert brukt)
- `.github/workflows/release.yml` — Release-workflow (sett `LOGLVL=DEBUG` dersom make vert brukt)

## Utført (delvis implementasjon)

### Endringar

**`make/00-settings.mk`:**
- La til `LOGLVL ?= INFO`-variabel (default INFO)
- La til `LOG_FUNCTIONS`-export med `log_debug()`, `log_info()`, `log_error()` og `timed_run()`-funksjonar
- La til fargar: `CLR_OK`, `CLR_ERR`, `CLR_DBG`

**`make/10-generator-macros.mk`:**
- Oppdatert `run_parallel_with_timer`: brukar `eval "$$LOG_FUNCTIONS"` og `log_info`/`log_debug`/`log_error`
- Oppdatert `run_gen_with_check_parallel`: brukar `eval "$$LOG_FUNCTIONS"` og `log_info`/`log_debug`/`log_error`
- Oppdatert `run_gen` (seriell): brukar `log_info`/`log_debug`
- Oppdatert `run_gen_linkml_serial`: brukar `log_info`/`log_debug`
- Oppdatert `run_gen_shacl`: brukar `log_info`/`log_debug`
- Oppdatert `run_gen_owl`: brukar `log_info`/`log_debug`
- Oppdatert `run_gen_rdf`: brukar `log_info`/`log_debug` (inkl. skip-logikk)
- Oppdatert `run_gen_doc`: brukar `log_info`/`log_debug`
- Oppdatert `run_gen_erdiagram`: brukar `log_info`/`log_debug`
- Oppdatert `run_gen_plantuml`: brukar `log_info`/`log_debug`

**`.github/workflows/generate.yml`:**
- La til `env: LOGLVL: DEBUG` i "Generer alle artefaktar for ${{ matrix.domain }}"-steget
- La til `env: LOGLVL: DEBUG` i "Publiser og bygg dokumentasjonsportal"-steget

### Status

**Fullført:**
- Logging-rammeverket er implementert i `make/00-settings.mk`
- Hovudgeneratorane (`run_gen_parallel`, `run_gen`, `run_gen_doc`, `run_gen_erdiagram`, `run_gen_plantuml`, `run_gen_shacl`, `run_gen_owl`, `run_gen_rdf`) brukar no logge-funksjonar
- GitHub Actions brukar `LOGLVL=DEBUG` for `domain-*` og `docs-publish` targets

**Gjenstår:**
- Oppdatere `run_gen_xsd`, `run_gen_asyncapi`, `run_gen_openapi` til å bruke logge-funksjonar
- Oppdatere validerings-makroar (`make/40-validation.mk`)
- Oppdatere docs-makroar (`make/50-docs.mk`)
- Teste lokalt med alle tre nivå
- Verifisere at parallelle køyringar ikkje vrir saman output
- Oppdatere `COMMANDS.md` med logging-dokumentasjon
- Oppdatere andre workflows (`validate.yml`, `release.yml`) dersom dei brukar make

### Neste steg

For å fullføre implementasjonen:
1. Oppdater resterande generatorar (`run_gen_xsd`, `run_gen_asyncapi`, `run_gen_openapi`)
2. Oppdater validerings- og docs-makroar
3. Test lokalt med `make gen-doc LOGLVL=DEBUG`, `LOGLVL=INFO`, `LOGLVL=ERROR`
4. Verifiser at GitHub Actions-loggar er lesbare (ikkje for verbose)
5. Oppdater `COMMANDS.md` med logging-dokumentasjon
