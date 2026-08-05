# Fiks vilkårleg skjemaval i run-validation.sh

## Bakgrunn

I generate-workflowen si "Kopier valideringsloggar til generated/"-steg feila
kopiering for `ap-no/modelldcat-ap-no` konsekvent:

```
⚠️  modelldcat-ap-no: Ingen validering for versjon 1.10.0, hoppar over
```

Valideringssteget hadde nettopp validert og skrive logg for versjon 1.14.0,
men kopisteget leitte etter versjon 1.10.0.

**Rotårsak:** To skript brukar ulike metodar for å finne "skjemafila" til ein
build.yaml-katalog når katalogen har fleire `*-schema.yaml`-filer:

- `src/assets/scripts/ci/run-validation.sh` (manifest-modus):
  `find "$schema_dir" -maxdepth 1 -name "*-schema.yaml" | head -n1` —
  vilkårleg val, `find` sorterer ikkje.
- `.github/workflows/generate.yml` (kopisteg): konstruerer filnamnet
  deterministisk som `$schema_dir/${schema_name}-schema.yaml`, i tråd med
  namnekonvensjonen i `CONVENTIONS.md` (`<modell>-schema.yaml` = katalognamnet).

`src/linkml/ap-no/modelldcat-ap-no/` har tre skjemafiler med ulik versjon
(lagvis imports):

- `modelldcat-ap-no-schema.yaml` v1.10.0 (toppnivå, konvensjonsnamnet)
- `modelldcat-katalog-schema.yaml` v1.0.0 (importerer modell-skjemaet)
- `modelldcat-modell-schema.yaml` v1.14.0

Denne køyringa fekk `find` til å plukke `modelldcat-modell-schema.yaml`
(v1.14.0), medan kopisteget korrekt leitte etter `modelldcat-ap-no-schema.yaml`
(v1.10.0) — dei fann aldri kvarandre.

Same latente feil finst i `src/linkml/ap-no/dqv-ap-no/` (to skjemafiler,
`dqv-ap-no-schema.yaml` v1.15.0 og `dqv-core-schema.yaml` v1.0.0). Denne
køyringa slapp unna fordi `find` tilfeldigvis returnerte rett fil først —
feilen kan dukke opp der ved neste CI-køyring utan kodeendring, sidan
filsystem-rekkjefølgja til `find` ikkje er garantert stabil.

## Steg

1. Endre `run-validation.sh` (manifest-modus) til å finne skjemafila
   deterministisk via katalognamn-konvensjonen (`$schema_dir/$(basename
   "$schema_dir")-schema.yaml`) i staden for `find "$schema_dir" -maxdepth 1
   -name "*-schema.yaml" | head -n1`.
2. Behald `find`-fallback for feilmelding dersom konvensjonsfila ikkje finst
   (uendra feilmelding: "Fann ingen *-schema.yaml i $schema_dir").
3. Verifiser med `actionlint` at `generate.yml` framleis er urørt (ingen
   endring venta der, men skal ikkje trengast — kopisteget sin logikk er
   allereie korrekt).
4. Test lokalt: køyr `run-validation.sh --manifest
   src/linkml/ap-no/modelldcat-ap-no/build.yaml` og stadfest at han validerer
   `modelldcat-ap-no-schema.yaml` (v1.10.0) og skriv logg til
   `validation/1.10.0/gold.json`.
5. Same test for `src/linkml/ap-no/dqv-ap-no/build.yaml` — stadfest v1.15.0.

## Handlingsliste

- [x] Endre skjema-oppslag i `run-validation.sh` til konvensjonsbasert sti
- [x] Lokal test: modelldcat-ap-no validerer v1.10.0
- [x] Lokal test: dqv-ap-no validerer v1.15.0
- [x] Commit-melding

## Utført

Endra manifest-modus i `run-validation.sh` frå `find "$schema_dir" -maxdepth 1
-name "*-schema.yaml" | head -n1` (vilkårleg val ved fleire skjemafiler) til
deterministisk sti `$schema_dir/$(basename "$schema_dir")-schema.yaml`, i tråd
med namnekonvensjonen kopisteget i `generate.yml` allereie føreset.

Verifisert lokalt: `modelldcat-ap-no` validerer no v1.10.0 (var v1.14.0),
`dqv-ap-no` validerer v1.15.0 (uendra, men no garantert deterministisk).
Testgenererte valideringsloggar sletta att etter verifisering — dei vert
skrivne på nytt av neste CI-køyring.
