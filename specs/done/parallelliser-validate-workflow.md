# Parallelliser "Valider skjema mot validation_policy" i validate.yml

## Bakgrunn

Følgjer opp `specs/done/parallelliser-domene-validering.md`, som
parallelliserte det tilsvarande steget i `generate.yml`. `validate.yml` sin
`validate`-jobb hadde nøyaktig same sekvensielle for-løkke i steget "Valider
skjema mot validation_policy" (linje 211-225):

```bash
FAILED=0
for manifest in $(find src/linkml/${{ matrix.domain }} -name build.yaml -type f | grep -v '/begrepssamling-'); do
  if grep -q "^generators:" "$manifest"; then
    echo "Validerer skjema frå manifest: $manifest"
    if ! bash src/assets/scripts/ci/run-validation.sh --manifest "$manifest"; then
      FAILED=$((FAILED + 1))
    fi
  fi
done
exit $FAILED
```

Same invariant og grunngjeving som i den førre specen gjeld uendra: kvart
`run-validation.sh --manifest`-kall flatar ut og validerer berre sitt eige
skjema, heilt isolert (unik `mktemp`-fil, unik loggsti) — parallellisering av
løkka er trygt.

## Steg

### 1. Erstatt sekvensiell for-løkke med parallell jobb-oppstart + wait-samling

Same `&`/`PIDS`/`MANIFESTS`/`wait`-mønster som no brukt i `generate.yml`:

```bash
declare -a PIDS=()
declare -a MANIFESTS=()
for manifest in $(find src/linkml/${{ matrix.domain }} -name build.yaml -type f | grep -v '/begrepssamling-'); do
  if grep -q "^generators:" "$manifest"; then
    echo "Validerer skjema frå manifest: $manifest"
    bash src/assets/scripts/ci/run-validation.sh --manifest "$manifest" &
    PIDS+=($!)
    MANIFESTS+=("$manifest")
  fi
done

FAILED=0
for i in "${!PIDS[@]}"; do
  if ! wait "${PIDS[$i]}"; then
    echo "::error file=${MANIFESTS[$i]}::Validering feila"
    FAILED=$((FAILED + 1))
  fi
done
exit $FAILED
```

**Tillegg utover rein parallellisering:** `::error file=...`-annotasjonen er
lagt til for å matche `generate.yml` sin feilrapportering (peikar til kva
manifest som feila) — `exit $FAILED` er halde uendra (eksisterande
oppførsel/konvensjon i denne fila, ikkje del av oppgåva å endre).

### 2. Kjør `actionlint`

Obligatorisk etter CI-endring. Berre `[shellcheck]`-stilråd i urelaterte,
eksisterande steg — ingen `[expression]`-feil.

## Handlingsliste

- [x] Erstatt sekvensiell for-løkke med parallell jobb-oppstart (`&` + `PIDS`)
- [x] Legg til `wait`-løkke med feilsamling og `::error`-annotasjon
- [x] Kjør `actionlint` mot `validate.yml`
- [ ] Test i CI med eit fleirskjema-domene og verifiser feilhandtering (krev faktisk CI-køyring)

## Utført

- `.github/workflows/validate.yml`: steget "Valider skjema mot validation_policy" i `validate`-jobben startar no alle manifest-valideringar i bakgrunnen og samlar feil i ei `wait`-løkke, same mønster som `generate.yml`
- `actionlint` køyrd — ingen `[expression]`-feil
- Ikkje testa i faktisk CI-køyring
