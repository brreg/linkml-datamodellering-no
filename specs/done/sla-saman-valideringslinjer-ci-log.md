# Slå saman duplikat-linjer i CI-valideringslogg

## Bakgrunn

I generate.yml (og identisk i validate.yml) sitt "Valider skjema"-steg vert
kvart validert skjema logga med to separate linjer:

```
✓ Validering vellykka: src/linkml/ap-no/common-ap-no/validation/1.0.0/bronze.json
✓ Validert src/linkml/ap-no/common-ap-no/build.yaml (31.1s)
```

Den første kjem frå `run-validation.sh` sin eigen stderr-echo (nyttig ved
direkte bruk, t.d. `make lint`/`make validate`), den andre frå
wrapper-løkka i workflow-fila som legg til køyretid. Saman er dei redundante
og gjer CI-loggen tyngre å lese.

## Steg

1. Legg til eit `--quiet`-flagg i `run-validation.sh` (manifest- og
   schema-modus). Når sett: undertrykk den menneskelesbare
   "✓ Validering vellykka: ..." / "✗ Validering feila: sjå ..." linja til
   stderr, og skriv i staden berre `$log_path` til stdout (uendra åtferd
   utan flagget, for `make lint`/`make validate`-brukarar).
2. Oppdater løkka i `generate.yml` og `validate.yml` til å kalle med
   `--quiet` og fange `log_path` via command substitution, og bygg éi
   samanslått linje med status, manifest, loggsti og køyretid:
   `✓ Validert <manifest> → <log_path> (<tid>)`.
3. Behald `→ Validerer <domain>/<modell> (v<versjon>) med policy: <policy>`
   sanntidslinja frå run-validation.sh uendra (går til stderr, ikkje
   fanga) — den gir progresjonsinfo medan parallelle jobbar køyrer.
4. Køyr `actionlint` mot begge endra workflow-filer.
5. Test lokalt: køyr wrapper-logikken (eller `run-validation.sh --manifest
   ... --quiet`) og stadfest at output framleis inneheld loggsti ved både
   suksess og feil.

## Handlingsliste

- [x] Legg til `--quiet`-flagg i `run-validation.sh`
- [x] Oppdater `generate.yml` sitt valideringssteg til samanslått linje
- [x] Oppdater `validate.yml` sitt valideringssteg til samanslått linje
- [x] `actionlint` på begge filer
- [x] Lokal test av samanslått output (suksess og feil)
- [x] Commit-melding

## Utført

Lagt til `--quiet`-flagg i `run-validation.sh`: undertrykker den separate
"✓ Validering vellykka: ..."-linja til stderr og skriv i staden berre
loggstien til stdout. Direkte bruk (`make lint`/`make validate`) er uendra
sidan flagget er valfritt.

`generate.yml` og `validate.yml` sine parallelle valideringsløkker kallar no
med `--quiet`, fangar loggstien via command substitution, og byggjer éi
samanslått linje:

```
✓ Validert src/linkml/ap-no/common-ap-no/build.yaml → src/linkml/ap-no/common-ap-no/validation/1.0.0/bronze.json (15.7s)
```

`actionlint` køyrt mot begge filer — ingen `[expression]`-feil, berre
eksisterande `[shellcheck]`-stilråd i urelaterte steg. Verifisert lokalt med
faktisk `run-validation.sh`-køyring; testgenererte valideringsloggar sletta
etterpå.
