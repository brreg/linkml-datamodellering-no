# Auto-detect validation_policy frå manifest.yaml

## Bakgrunn

`make mcp-validate` krev i dag at brukar oppgir både `SCHEMA=` og `POLICY=` kvar gong. Dette bryt med DRY-prinsippet — `validation_policy` ligg allereie i `manifest.yaml` ved sidan av skjemafila, så verdien vert oppgjeven to gonger.

Målet er at `make mcp-validate SCHEMA=sti` automatisk skal lese `validation_policy` frå `manifest.yaml` og bruke det som POLICY-verdi utan at brukar må oppgje det.

## Steg

1. **Parse manifest.yaml frå SCHEMA-sti**
   - Gitt `SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`, les `src/linkml/samt/samt-bu/manifest.yaml`
   - Trekk ut `validation_policy`-verdien med `yq .validation_policy`

2. **Oppdater Makefile-målet mcp-validate**
   - Legg til ein variabel `DETECTED_POLICY` som køyrer `yq` på manifestfila
   - Set `POLICY ?= $(DETECTED_POLICY)` slik at brukar framleis kan overstyre
   - Bruk `$(realpath $(dir $(SCHEMA)))/manifest.yaml` for å finne manifestfila

3. **Valider at yq er tilgjengeleg**
   - Legg til ein prerekvisisjon som feiler dersom `yq` ikkje finst i PATH
   - Alternativt: bruk `python -c 'import yaml; ...'` som fallback

4. **Test integrasjonen**
   - Køyr `make mcp-validate SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`
   - Verifiser at riktig policy (silver) vert brukt utan at POLICY er oppgjeven

5. **Oppdater dokumentasjon**
   - Legg til døme i CONTRIBUTING.md under «Kjøre validering»
   - Oppdater CLAUDE.md-seksjonen «Valider arbeidet ditt» for å forklare at POLICY er valfri

## Prioritert handlingsliste

- [ ] Parse manifest.yaml frå SCHEMA-sti
- [ ] Oppdater Makefile-målet mcp-validate
- [ ] Valider at yq er tilgjengeleg
- [ ] Test integrasjonen
- [ ] Oppdater dokumentasjon

## Avhengigheiter

- `yq` (installert i dev-containerane, men må vere i PATH lokalt)
- Eksisterande `mcp-validate`-mål

## Merknader

- `POLICY`-argumentet skal framleis vere mogleg å overstyre manuelt
- Feilmelding dersom `manifest.yaml` manglar eller ikkje har `validation_policy`-felt
- Alternativ: bruk Python i staden for yq for å unngå ekstra avhengigheit
