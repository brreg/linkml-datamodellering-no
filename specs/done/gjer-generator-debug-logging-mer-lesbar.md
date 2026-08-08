# Gjer generator-DEBUG-logging meir lesbar + to desimalar i tidtaking

## Bakgrunn

Etter forrige retting (`specs/done/gjenopprett-debug-logging-fjern-make-directory-stoy.md`)
kjem DEBUG-deloverskrifta for kvar generator no fram att, men som to
separate `log_debug`-linjer når nokre skjema er filtrert vekk av eit
build.yaml-flagg, t.d.:

```
[DEBUG] linkml-convert (example_rdf: true) for schemas: (ingen eksempel aktivert)
[DEBUG]   hoppar over linkml-convert (example_rdf: false): ap-no/cpsv-ap-no, ap-no/dcat-ap-no, ...
```

Ønskt: éi samla, lettlesen linje. I tillegg loggar mange raske gen-steg
`(0.0s)` fordi tidtakinga berre har éin desimal — brukaren ønsker to
desimalar.

## Steg

1. **Merge dei to debug-linjene til éi**, format
   `<generator>[ (<flag>: true)] — køyrer: <namn eller "(ingen)">[; hoppar
   over (<flag>: false): <namn>]`, i dei tre stadene som i dag skriv to
   linjer:
   - `src/assets/scripts/makefile/batch-generate.py` (`main()`)
   - `src/assets/scripts/makefile/run-parallel-gen.sh`
   - `src/assets/scripts/makefile/convert-examples.sh`

   (`batch-generate-instances.py` sin `filter_enabled()` skreiv frå før
   berre éi skip-linje, ikkje eit duplikatpar — uendra.)

2. **To desimalar i elapsed-tid.** DRY-konsolider den gjentekne
   `printf '(%d.%ds)' $((ms/1000)) $((ms%1000/100))`-formelen (7 stader,
   over DRY-terskelen på 3) til éin delt bash-funksjon `fmt_elapsed_ms` i
   `define LOG_FUNCTIONS` (`make/00-settings.mk`), brukt av:
   - `timed_run()` (same fil)
   - `src/assets/scripts/makefile/run-parallel-gen.sh`
   - `src/assets/scripts/makefile/batch-render-plantuml.sh`
   - `make/40-validation.mk` (validate-bronze, validate-data,
     validate-examples)

   Python-sida (`batch-generate.py`/`batch-generate-instances.py` sin
   `fmt_elapsed()`) oppdaterast til same avkorta to-desimal-formel
   (millisekund-basert, konsistent med bash-varianten).

3. Verifiser med `LOGLVL=DEBUG make domain-samt` og
   `LOGLVL=DEBUG make domain-ap-no` (sistnemnde har fleire skjema med
   filtrerte flagg, så begge grenene av den nye eitt-linje-logikken vert
   trefte) — stadfest at kvar generator no berre skriv éi debug-linje, og
   at alle elapsed-tider har to desimalar (ingen `0.0s`).

## Handlingsliste

- [x] Steg 1: merge debug-linjer i batch-generate.py, run-parallel-gen.sh,
      convert-examples.sh
- [x] Steg 2: delt `fmt_elapsed_ms` i LOG_FUNCTIONS, brukt i timed_run,
      run-parallel-gen.sh, batch-render-plantuml.sh, 40-validation.mk;
      to-desimal fmt_elapsed i begge batch-generate*.py
- [x] Steg 3: verifiser med domain-samt og domain-ap-no

## Utført

Verifisert med `LOGLVL=DEBUG make domain-samt` og
`LOGLVL=DEBUG make domain-ap-no`: kvar generator skriv no éi samla
DEBUG-linje (t.d. `shacl (shacl: true) — køyrer: ap-no/cpsv-ap-no, ...;
hoppar over (shacl: false): ap-no/common-ap-no`), og alle elapsed-tider har
to desimalar (`1.42s`, `0.26s`, `0.08s` osv. — ingen `0.0s`-linjer i
loggen).

- `make/00-settings.mk`: ny delt `fmt_elapsed_ms()` i `LOG_FUNCTIONS`,
  `timed_run()` bruker han
- `make/40-validation.mk`: validate-bronze/validate-data/validate-examples
  bruker `fmt_elapsed_ms`
- `src/assets/scripts/makefile/run-parallel-gen.sh`: merga debug-linje +
  `fmt_elapsed_ms`
- `src/assets/scripts/makefile/batch-render-plantuml.sh`: `fmt_elapsed_ms`
- `src/assets/scripts/makefile/convert-examples.sh`: merga debug-linje
- `src/assets/scripts/makefile/batch-generate.py`: merga debug-linje,
  to-desimal `fmt_elapsed`
- `src/assets/scripts/makefile/batch-generate-instances.py`: to-desimal
  `fmt_elapsed`

Verifiseringskøyringane sin biverknad på 9 `*-manifest.yaml`-filer under
`src/linkml/ap-no/` (regenerert `finnes_i_format` frå lokal, ufullstendig
`generated/`-tilstand) vart reverterte — ikkje ei tilsikta endring.
