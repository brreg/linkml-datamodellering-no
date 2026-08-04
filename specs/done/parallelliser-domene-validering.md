# Parallelliser "Valider alle skjema for domene"-steget i generate.yml

## Bakgrunn

I `.github/workflows/generate.yml`, steget `Valider alle skjema for
${{ matrix.domain }}` (linje 247-285), køyrer valideringa av alle skjema i eit
domene **i sekvens**:

```bash
for manifest in $(find src/linkml/${{ matrix.domain }} -name build.yaml -type f | grep -v '/begrepssamling-'); do
  if grep -q "^generators:" "$manifest" 2>/dev/null; then
    echo "→ Validerer skjema frå manifest: $manifest"
    if ! bash src/assets/scripts/ci/run-validation.sh --manifest "$manifest"; then
      echo "::error file=$manifest::Validering feila"
      FAILED=$((FAILED + 1))
    fi
  fi
done
```

For domene med mange skjema (t.d. `fint` med 8, `ap-no` med 7) blir dette
steget ein flaskehals — kvart skjema validerast ferdig før neste startar.

**Invarianten brukaren peika på — «alle skjema må køyre utflating før
validering av respektive skjema» — er alt strukturelt garantert** og krev
ingen endring: `run-validation.sh` → `flatten-and-validate.bash` flatar ut
(`gen-linkml --mergeimports`) **berre sitt eige skjema** til ein unik
temp-fil (`mktemp /tmp/flat-XXXXXX.yaml`) og validerer deretter same
utflata skjema, heilt isolert frå andre skjema sin køyring. Det finst ingen
delt tilstand mellom skjema-valideringar — kvar `run-validation.sh --manifest
<build.yaml>`-kall er sjølvstendig frå flatning til logg-skriving
(`src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`, unik sti
per skjema). Parallellisering av **sjølve for-løkka** (ikkje av
flaten-så-valider-rekkjefølgja *innanfor* eitt skjema) er difor trygt.

**Etablert mønster i repoet:** `mkdocs/publish.sh` (Steg 2, linje 343-369)
løyser akkurat dette problemet for skjema-dokumentasjonsgenerering —
uavgrensa parallellisering med `&` + `PIDS`-array + `KEYS`-array for å spore
kva jobb som feila, og ein etterfølgande `wait`-løkke som samlar feil per
jobb. Denne spesifikasjonen gjenbruker same mønster for konsistens (DRY —
same løysing på same problemtype, ikkje ein ny eigen mekanisme).

## Steg

### 1. Erstatt sekvensiell for-løkke med parallell jobb-oppstart

I `.github/workflows/generate.yml`, steget `Valider alle skjema for
${{ matrix.domain }}`:

```bash
declare -a PIDS=()
declare -a MANIFESTS=()

for manifest in $(find src/linkml/${{ matrix.domain }} -name build.yaml -type f | grep -v '/begrepssamling-'); do
  if grep -q "^generators:" "$manifest" 2>/dev/null; then
    echo "→ Validerer skjema frå manifest: $manifest"
    bash src/assets/scripts/ci/run-validation.sh --manifest "$manifest" &
    PIDS+=($!)
    MANIFESTS+=("$manifest")
  fi
done
```

### 2. Vent på alle jobbar og samle feil (same mønster som publish.sh)

```bash
FAILED=0
for i in "${!PIDS[@]}"; do
  if ! wait "${PIDS[$i]}"; then
    echo "::error file=${MANIFESTS[$i]}::Validering feila"
    FAILED=$((FAILED + 1))
  fi
done

if [ "$FAILED" -gt 0 ]; then
  echo "::error::Validering feila for $FAILED manifest(ar) i ${{ matrix.domain }} — stoppar bygget"
  exit 1
fi

echo "✓ Validering fullført for ${{ matrix.domain }}"
```

### 3. Behald eksisterande kommentar om [skip ci]-kontrollen

Kommentaren over steget (linje 248-255) om kvifor dette steget ikkje kan
fjernast som «dobbeltarbeid» skal stå urørt — gjeld framleis uansett
sekvensiell/parallell køyring.

### 4. Merk ressursomsyn (ingen kode-endring, berre observasjon for revjuar)

Kvart `run-validation.sh`-kall startar to podman-containarar i sekvens
(`LINKML_IMAGE` for utflating, `MCP_IMAGE` for validering). Ved full
parallellisering av eit stort domene (t.d. `fint` med 8 skjema) kan opp mot
16 containarar vere i gang samstundes på CI-runneren. `mkdocs/publish.sh` har
same uavgrensa fan-out-mønster for skjemagenerering utan kjend
ressursproblem i dette repoet, så same tilnærming er brukt her utan eiga
throttling. Dersom CI-runnerane viser seg overbelasta ved store domene, bør
ei `xargs -P<N>`-avgrensing vurderast som eige oppfølgingsarbeid.

### 5. Test lokalt / i CI

- Trigge `generate.yml` manuelt (`workflow_dispatch` eller push) for eit
  domene med fleire skjema (t.d. `fint` eller `ap-no`)
- Verifiser at alle skjema sine valideringsloggar vert skrivne korrekt til
  `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`
- Verifiser at ein injisert valideringsfeil i eitt skjema framleis stoppar
  bygget med `::error`-annotasjon på riktig manifest

## Handlingsliste

- [x] Erstatt sekvensiell for-løkke med parallell jobb-oppstart (`&` + `PIDS`)
- [x] Legg til `wait`-løkke med feilsamling (same mønster som `publish.sh`)
- [x] Kjør `actionlint` mot `generate.yml` (obligatorisk etter CI-endring, jf. CLAUDE.md)
- [ ] Test i CI med eit fleirskjema-domene og verifiser feilhandtering (krev faktisk CI-køyring — ikkje testbart lokalt)

## Utført

- `.github/workflows/generate.yml`: steget "Valider alle skjema for `<domene>`" startar no alle manifest-valideringar i bakgrunnen (`&`), sporar PID + manifest-sti i parallelle array, og samlar feil i ei `wait`-løkke etterpå (same mønster som `mkdocs/publish.sh` Steg 2)
- `actionlint` køyrd mot `generate.yml` — berre `[shellcheck]`-stilråd i urelaterte, eksisterande steg (linje 177, 210, 347), ingen `[expression]`-feil
- Ikkje testa i faktisk CI-køyring — krev at nokon triggar `generate.yml` (t.d. push eller `workflow_dispatch`) for eit fleirskjema-domene for å stadfeste oppførselen i praksis
