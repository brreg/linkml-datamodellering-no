# Forbedre feilmeldingar i generate-workflow

## Bakgrunn

Generate-workflowen (`generate.yml`) kan feile på ulike stader med lite kontekst:
- Podman exit code-feil ("died not found") gir ikkje info om kva skjema/domene som feila
- `make domain-<domain>` køyrer mange skjema parallelt — når éin feilar, ser ein berre siste feil
- Ingen logg over kva skjema som vart prosesserte før feilen
- Ingen retry-logikk for transiente podman-feil

**Konkret trigger:** Run #338 feila med:
```
time="2026-07-31T17:42:28Z" level=error msg="Could not retrieve exit code from event: died not found"
ERROR in Makefile parallel job for fint/fint-ressurs at line 1
make: *** [make/20-domain-targets.mk:124: domain-fint] Error 123
```

**Kva manglar:**
1. Kontekst om kva skjema som køyrde når feilen oppstod
2. Logg over fullførte skjema (for å sjå kvar det stoppa)
3. Retry-logikk for transiente podman-feil
4. Betre GitHub Actions-annotasjonar (::error, ::warning) med filreferansar

## Mål

Leggje til:
1. **Pre-flight-sjekk** — logg alle skjema som skal genererast før start
2. **Progress-logging** — logg kvar skjema etter kvart som dei vert fullførte
3. **Retry-logikk** — automatisk retry ved podman exit code-feil (maks 2 retrys)
4. **Kontekstuell feilmelding** — ved feil, logg kva skjema som feila + siste 50 linjer av stdout/stderr
5. **GitHub Actions-annotasjonar** — ::error med filreferanse til skjemaet som feila

## Steg

### 1. Legg til pre-flight-sjekk i generate-step

Endre `generate.yml` (steg "Generer alle artefaktar for ${{ matrix.domain }}"):

```yaml
- name: Generer alle artefaktar for ${{ matrix.domain }}
  if: steps.cache-generated.outputs.cache-hit != 'true'
  shell: bash
  run: |
    set -euo pipefail
    
    # Pre-flight: logg alle skjema som skal genererast
    echo "=== Skjema som skal genererast for ${{ matrix.domain }} ==="
    find src/linkml/${{ matrix.domain }} -name "*-schema.yaml" -type f | sort | while read schema; do
      echo "  - $schema"
    done
    echo ""
    
    # Køyr domene-target med retry-logikk
    retry_count=0
    max_retries=2
    while [ $retry_count -le $max_retries ]; do
      if make domain-${{ matrix.domain }}; then
        echo "✓ make domain-${{ matrix.domain }} fullført"
        break
      else
        exit_code=$?
        retry_count=$((retry_count + 1))
        if [ $retry_count -le $max_retries ]; then
          echo "::warning::make domain-${{ matrix.domain }} feila (forsøk $retry_count/$max_retries) — ventar 10s før retry"
          sleep 10
        else
          echo "::error file=.github/workflows/generate.yml,line=239::make domain-${{ matrix.domain }} feila etter $max_retries retrys — sjå loggar for detaljar"
          exit $exit_code
        fi
      fi
    done
```

### 2. Legg til progress-logging i Makefile-targets

Endre `make/20-domain-targets.mk` (eller tilsvarande fil som køyrer parallelle jobbar) til å logge fullførte skjema:

```bash
# I parallell-jobbseksjonen (per skjema)
echo "✓ Fullførte generering av $SCHEMA" >> "$WORK_DIR/progress.log"
```

### 3. Legg til feilkontekst-logging i Makefile

Ved feil i parallell-jobb, logg:
- Skjemanamn
- Siste 50 linjer av stdout/stderr
- GitHub Actions-annotasjon med filreferanse

```bash
trap 'echo "::error file=$SCHEMA::Generering feila for $SCHEMA"; tail -50 "$LOG_FILE"; exit 1' ERR
```

### 4. Test lokalt

```bash
# Simuler podman-feil
make domain-fint

# Verifiser at retry-logikk triggar
# Verifiser at progress.log vert oppdatert
```

### 5. Test i CI

- Push endringane til ei testbranch
- Trigger workflow manuelt via `workflow_dispatch`
- Verifiser at feilmeldingar er meir informative

## Suksesskriterium

- [x] Pre-flight-sjekk listar alle skjema før start
- [ ] Progress-logg viser fullførte skjema (kan brukast til å identifisere kvar det stoppa) — IKKJE IMPLEMENTERT (vurdert som mindre kritisk)
- [x] Retry-logikk kickar inn ved transiente podman-feil (maks 2 retrys, 10s pause)
- [x] Ved feil: GitHub Actions-annotasjon med filreferanse til feila skjema
- [ ] Ved feil: siste 50 linjer av stdout/stderr vert logga — IKKJE IMPLEMENTERT (komplekst i parallell-kontekst)

## Utført

### 1. GitHub Actions-annotasjon i Makefile

Endra `make/10-generator-macros.mk` linje 17:
- La til `::error file=$$s::$(2) feila for $$domain/$$name (linje $$LINENO)` i trap-blokka
- Beheld eksisterande feilmelding for kompatibilitet

### 2. Pre-flight-sjekk i workflow

Endra `.github/workflows/generate.yml` (steg "Generer alle artefaktar for ${{ matrix.domain }}"):
- Logg alle skjema som skal genererast før `make domain-<domain>` køyrer
- Formatert som bullet-liste for oversikt

### 3. Retry-logikk i workflow

Endra `.github/workflows/generate.yml` (same steg):
- While-loop med `retry_count` (maks 2 retrys = 3 forsøk totalt)
- 10 sekund pause mellom retrys
- `::warning`-annotasjon ved retry, `::error` ved endeleg feil

### Endringar gjort

**`make/10-generator-macros.mk`:**
```bash
# Linje 17 (tidlegare):
trap '\''echo "ERROR in Makefile parallel job for $$domain/$$name at line $$LINENO — command: $$BASH_COMMAND" >&2; exit 1'\'' ERR; \

# Linje 17 (no):
trap '{ echo "::error file=$$s::$(2) feila for $$domain/$$name (linje $$LINENO)" >&2; echo "ERROR in Makefile parallel job for $$domain/$$name at line $$LINENO — command: $$BASH_COMMAND" >&2; exit 1; }' ERR; \
```

**`.github/workflows/generate.yml`:**
```yaml
# La til pre-flight-sjekk og retry-logikk i steg "Generer alle artefaktar for ${{ matrix.domain }}"
# Sjå diff for detaljar
```

### Ikkje implementert

**Progress-logging** — krevde modifikasjonar i kvar generator-makro for å skrive til felles loggfil. Vurdert som mindre kritisk sidan:
- Pre-flight-sjekken viser kva som *skal* genererast
- Eksisterande tidsstempla output viser kva som *vart* fullført
- Feilen peikar no eksplisitt til skjemafila som feila

**Last 50 lines of output** — komplekst i parallell-kontekst sidan:
- xargs køyrer parallelle bash-subshells — kvar har eigen stdout/stderr
- For å fange output måtte vi omdirigere til per-schema loggfiler
- Det ville lagt til overhead og kompleksitet utan klår nytte (GitHub Actions loggar allereie all output)
