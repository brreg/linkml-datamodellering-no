# test_make.sh: vis progresjon i sanntid under testkøyring

## Symptom

```bash
make test SCHEMA=src/linkml/oreg/enhetsregisteret-bvrinn/bvrinn-schema.yaml
```

Terminalen er stille til alle 15 testar er ferdige — ingen indikasjon på
kva som køyrer, om prosessen heng, eller kor langt ein er komen.

## Rotårsak

I `run_schema_tests()` (linje 99–118) vert heile testblokka køyrt som ein
bakgrunnsprosess med all stdout og stderr omdirigert til ein tempfil:

```bash
{
    _run_one "validate ($name)"  ...
    _run_one "gen-jsonld ($name)" ...
    ...
} >> "$tmplog" 2>&1 &          # ← ALT forsvinn hit
```

`wait_for_tests()` les tempfilene berre etter at `wait "$pid"` returnerer —
dvs. etter at alle testar er ferdige. Ingen output når terminalen undervegs.

## Tilrådd løysing: fd 3 som direkte kanal til terminalen

Opne fildesriptor 3 peikande på terminalen i hovudprosessen. Sidan
bakgrunnsprosessane arvar fd 3, kan `_run_one` skrive START- og
RESULT-linjer direkte til terminalen utan å bryte omdirigering av
testoutput (fd 1 og 2) til tempfila.

```
fd 1 (stdout) → tempfil   (podman-output, make-output — uendra)
fd 2 (stderr) → tempfil   (feilmeldingar — uendra)
fd 3          → terminal  (NY: START/RESULT-linjer)
```

### Endring 1 — opne fd 3 i hovudprosessen (før `for schema`-løkka)

```bash
# Rett før: for schema in "${SCHEMAS[@]}"; do
exec 3>&1
```

### Endring 2 — print schema-start umiddelbart i `run_schema_tests()`

Legg til éi linje *utanfor* bakgrunnsboksen — ho køyrer i hovudprosessen
og vises med ein gong:

```bash
run_schema_tests() {
    local schema="$1"
    local domain name outdir
    domain=$(schema_domain "$schema")
    name=$(schema_name "$schema")
    outdir=$(schema_outdir "$schema")
    local tmplog
    tmplog=$(mktemp /tmp/test_make_schema_XXXXXX.log)

    echo "→ Startar testar for $name ..."   # NY linje — køyrer i hovudprosessen

    {
        _run_one "validate ($name)"  ...
        ...
    } >> "$tmplog" 2>&1 &
    ...
}
```

### Endring 3 — skriv START og RESULT til fd 3 i `_run_one()`

```bash
_run_one() {
    local tname="$1"; shift
    printf "  %-50s ..." "$tname" >&3          # NY: vis at testen startar
    echo "========================================"
    echo "TEST: $tname  ($(date '+%H:%M:%S'))"
    echo "========================================"
    if "$@" 2>&1; then
        printf " ${CLR_OK}OK${CLR_RST}\n" >&3  # NY: vis resultat i sanntid
        echo "##RESULT:OK:$tname"
    else
        printf " ${CLR_ERR}FEIL${CLR_RST}\n" >&3  # NY: vis resultat i sanntid
        echo "##RESULT:FAIL:$tname"
    fi
}
```

`CLR_OK`, `CLR_ERR` og `CLR_RST` er allereie definerte i skriptet og er
tilgjengelege i bakgrunnsprosessen (arva miljøvariablar).

### Endring 4 — fjern duplikat-utskrift i `wait_for_tests()`

Sidan `_run_one` no skriv kvart resultat direkte til terminalen via fd 3,
treng ikkje `wait_for_tests` skrive per-test-linjene i tillegg. Behold berre
samandraget og feildetaljar:

```bash
wait_for_tests() {
    local pass=0 fail=0
    for i in "${!SCHEMA_PIDS[@]}"; do
        local pid="${SCHEMA_PIDS[$i]}"
        local tmplog="${SCHEMA_LOGS[$i]}"
        wait "$pid" || true
        while IFS= read -r line; do
            if [[ "$line" == "##RESULT:OK:"* ]]; then
                pass=$((pass + 1))
            elif [[ "$line" == "##RESULT:FAIL:"* ]]; then
                local tname="${line#"##RESULT:FAIL:"}"
                fail=$((fail + 1))
                echo "--- output frå $tname ---" >&2
                grep -A 25 "TEST: $tname " "$tmplog" | tail -25 >&2 || true
            fi
        done < "$tmplog"
        sed 's/\x1b\[[0-9;]*m//g' "$tmplog" >> "$LOG"
        rm -f "$tmplog"
    done
    echo ""
    echo "Resultat: $pass OK, $fail feil"
    echo "Sjå $LOG for detaljar"
    [ "$fail" -eq 0 ]
}
```

## Forventa terminaloutput etter endringa

```
→ Startar testar for bvrinn-schema ...
  validate (bvrinn-schema)                           ... OK
  gen-jsonld (bvrinn-schema)                         ... OK
  gen-python (bvrinn-schema)                         ... OK
  gen-jsonschema (bvrinn-schema)                     ... OK
  gen-rdf (bvrinn-schema)                            ... OK
  gen-erdiagram (bvrinn-schema)                      ... OK
  ...

Resultat: 15 OK, 0 feil
Sjå tests/testlogs/test_make_20260608_143201.log for detaljar
```

Når fleire skjema køyrer parallelt vil linjene frå ulike skjema kunna
flettast, men kvar linje er atomisk (`printf` på Linux er atomisk for
linjestorleik < PIPE_BUF ≈ 4096 byte) og resultata er framleis lesbare.

## Alternativ som vart vurdert

**Polling med `tail -f`**: Krev ein eigen bakgrunnsprosess som les frå ei
delt FIFO eller fil. Meir komplekst, og fd 3 løyser same behovet enklare.

**`tee`-omdirigering**: `{...} 2>&1 | tee "$tmplog"` sender output til
terminalen i sanntid, men blandinga av 15 parallelle `make`-køyringar
vert ulesbar. Fd 3-tilnærminga er meir kontrollert — berre
START/RESULT-linjer vises, ikkje rå make-output.

## Tiltak

- [ ] Legg til `exec 3>&1` rett før `for schema`-løkka (~linje 424)
- [ ] Legg til `echo "→ Startar testar for $name ..."` øvst i
      `run_schema_tests()`, utanfor bakgrunnsboksen (~linje 97)
- [ ] Oppdater `_run_one()` til å skrive START og RESULT til fd 3 (~linje 77)
- [ ] Fjern per-test `printf`-linjene i `wait_for_tests()` (~linje 132–136)
- [ ] Verifiser at parallellkøyring med fleire skjema gir lesbar output
