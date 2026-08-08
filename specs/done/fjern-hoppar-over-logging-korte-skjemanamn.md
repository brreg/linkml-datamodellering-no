# Fjern "hoppar over"-logging, korte skjemanamn i "køyrer"-debug-linja

## Bakgrunn

Oppfølging av `specs/done/gjer-generator-debug-logging-mer-lesbar.md`. Den
merga debug-linja er framleis for støyete:

```
[DEBUG] shacl (shacl: true) — køyrer: ap-no/cpsv-ap-no, ap-no/dcat-ap-no, ...; hoppar over (shacl: false): ap-no/common-ap-no
```

Ønskt:
1. Fjern "hoppar over"-delen heilt (ikkje berre slå ho saman med
   "køyrer"-linja).
2. "køyrer"-lista skal berre vise skjemanamnet, utan domeneprefiks
   (`cpsv-ap-no` i staden for `ap-no/cpsv-ap-no`).

## Steg

1. `src/assets/scripts/makefile/batch-generate.py` (`main()`): fjern
   `skipped`-sporing, bygg `enabled` med éin listeforståing, bruk berre
   `schema_domain_name(s)[1]` (namn utan domene) i `names`.
2. `src/assets/scripts/makefile/run-parallel-gen.sh`: same — fjern
   `skipped`-array og tilhøyrande melding, `names` bygd av berre
   skjemanamn.
3. `src/assets/scripts/makefile/convert-examples.sh`: same — fjern
   `skipped`-array, `enabled_names` lagrar berre `$profil` (ikkje
   `$domain/$profil`).
4. `src/assets/scripts/makefile/batch-generate-instances.py`: `filter_enabled()`
   hadde frå før BERRE ei "hoppar over"-linje (ingen "køyrer"-linje å
   justere) — fjern denne debug-linja heilt, forenkl funksjonen til eit
   reint filter, og fjern det no ubrukte `generator`-parameteret + oppdater
   dei fem kallstadene (`erdiagram-filter`, `plantuml-filter`,
   `docgen-examples`, `gen-openapi`, `gen-asyncapi`).
5. Verifiser med `LOGLVL=DEBUG make domain-samt` (alle flagg true) og
   `LOGLVL=DEBUG make domain-ap-no` (blanda flagg, m.a. `common-ap-no` som
   har fleire flagg av) — stadfest at ingen linje inneheld "hoppar over",
   og at alle namn i "køyrer"-lista manglar domeneprefiks.

## Handlingsliste

- [x] Steg 1: batch-generate.py
- [x] Steg 2: run-parallel-gen.sh
- [x] Steg 3: convert-examples.sh
- [x] Steg 4: batch-generate-instances.py (filter_enabled + kallstader)
- [x] Steg 5: verifiser med domain-samt og domain-ap-no

## Utført

Verifisert med `LOGLVL=DEBUG make domain-samt` og
`LOGLVL=DEBUG make domain-ap-no`: `grep hoppar` mot full logg gav 0 treff,
og "køyrer"-listene viser berre skjemanamn (t.d. `shacl (shacl: true) —
køyrer: cpsv-ap-no, dcat-ap-no, dqv-ap-no, ...`), utan domeneprefiks.

- `src/assets/scripts/makefile/batch-generate.py`: fjerna skip-logging,
  namn utan domene
- `src/assets/scripts/makefile/run-parallel-gen.sh`: same
- `src/assets/scripts/makefile/convert-examples.sh`: same
- `src/assets/scripts/makefile/batch-generate-instances.py`: fjerna
  `filter_enabled()` sin debug-linje, fjerna ubrukt `generator`-parameter
  frå funksjonen og dei fem kallstadene

Verifiseringskøyringane sin biverknad på `*-manifest.yaml`-filer under
`src/linkml/ap-no/` (regenerert `finnes_i_format` frå lokal, ufullstendig
`generated/`-tilstand) vart reverterte igjen — ikkje ei tilsikta endring.

### Rettefølgje

Steg 4 fjerna debug-logginga frå `filter_enabled()` heilt (sidan ho før
berre hadde ei "hoppar over"-linje). Dette var for aggressivt: dei fem
kallarane (`erdiagram-filter`, `plantuml-filter`, `docgen-examples`,
`gen-openapi`, `gen-asyncapi`) mista då ALL debug-synlegheit for kva
skjema dei køyrer for — t.d. var `gen-openapi (openapi: true) — køyrer:
...` heilt borte frå domain-samt-logg. Retta ved å gjenreise ei rein
"køyrer"-linje (ingen "hoppar over") i `filter_enabled()`, med
`generator`-parameteret attgjeve til funksjonen og dei fem kallstadene, i
same format som dei andre generatorane. Verifisert med
`LOGLVL=DEBUG make domain-samt`: alle fem viser no si eiga `<generator>
(<flag>: true) — køyrer: samt-bu`-linje.
