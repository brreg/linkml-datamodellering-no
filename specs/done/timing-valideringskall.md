# Time alle valideringskall i validate- og generate-workflowane sine validate-matrisar

## Bakgrunn

Følgjer opp `specs/done/parallelliser-domene-validering.md` og
`specs/done/parallelliser-validate-workflow.md`. No som valideringskalla
(`run-validation.sh --manifest <build.yaml>`) køyrer parallelt i begge
workflowane, er det ikkje lenger openbert frå loggen kor lang tid **kvar
enkelt** valideringskall tek — nyttig for å avdekke treige skjema/domene og
for å vurdere effekten av parallelliseringa.

**Etablert mønster i repoet:** `generate.yml` sitt eige steg "Last images inn
i podman frå GHCR" (linje 208-224) har alt nøyaktig denne timing-stilen:

```bash
local start=$(date +%s%3N)
...
local elapsed=$(( $(date +%s%3N) - start ))
printf "✓ Henta %s frå GHCR (%d.%ds)\n" "$local_tag" $((elapsed / 1000)) $((elapsed % 1000 / 100))
```

Same `date +%s%3N`/`printf "(%d.%ds)"`-mønster er brukt her, tilpassa til å
gjelde per manifest og synleggjere feil-tilfellet òg (viktig sidan mange
kall køyrer samstundes og interlevert output elles gjer det vanskeleg å vite
kva tid som høyrer til kva manifest).

## Steg

### 1. `generate.yml` — steget "Valider alle skjema for `<domene>`"

Pakk kvart bakgrunnskall inn i ein subshell som tek tida og printar resultatet
uansett utfall:

```bash
(
  start=$(date +%s%3N)
  rc=0
  bash src/assets/scripts/ci/run-validation.sh --manifest "$manifest" || rc=$?
  elapsed=$(( $(date +%s%3N) - start ))
  if [ $rc -eq 0 ]; then
    printf "✓ Validert %s (%d.%ds)\n" "$manifest" $((elapsed / 1000)) $((elapsed % 1000 / 100))
  else
    printf "✗ Validering feila for %s (%d.%ds)\n" "$manifest" $((elapsed / 1000)) $((elapsed % 1000 / 100))
  fi
  exit $rc
) &
```

Subshellen sin exit-kode (frå den eksplisitte `exit $rc` til slutt) held fram
å nå `wait "${PIDS[$i]}"` i feilsamlingsløkka uendra.

### 2. `validate.yml` — steget "Valider skjema mot validation_policy"

Same endring, identisk mønster (denne fila manglar `set -euo pipefail`
eksplisitt, men GitHub Actions sin standard bash-shell køyrer alt med
`-e -o pipefail`, så oppførselen er den same).

### 3. Kjør `actionlint` mot begge filene

Obligatorisk etter CI-endring. Berre `[shellcheck]`-stilråd i urelaterte,
eksisterande steg i begge filer — ingen `[expression]`-feil.

## Handlingsliste

- [x] Legg til timing per valideringskall i `generate.yml`
- [x] Legg til timing per valideringskall i `validate.yml`
- [x] Kjør `actionlint` mot begge filene
- [ ] Test i CI og verifiser at timing-linjene syner fornuftige verdiar (krev faktisk CI-køyring)

## Utført

- `.github/workflows/generate.yml`: kvart valideringskall i "Valider alle skjema for `<domene>`" er no pakka inn i ein timande subshell (`✓/✗ ... (%d.%ds)`), same stil som det eksisterande GHCR-pull-timing-mønsteret lenger opp i same fil
- `.github/workflows/validate.yml`: same endring i "Valider skjema mot validation_policy"
- `actionlint` køyrd mot begge filene — ingen `[expression]`-feil
- Ikkje testa i faktisk CI-køyring
