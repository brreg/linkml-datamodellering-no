# Farg skjemanamna grønt i "<generator> — køyrer: ..."-debug-linja

## Bakgrunn

Brukaren ønsker at skjemanamna i den samla DEBUG-deloverskrifta (jf.
`specs/done/gjer-generator-debug-logging-mer-lesbar.md` og
`specs/done/fjern-hoppar-over-logging-korte-skjemanamn.md`) skil seg
tydelegare ut i loggen. Repoet har alt ein etablert grøn fargekode
(`CLR_OK`, `\033[0;32m`, definert i `make/00-settings.mk` og eksportert)
brukt for suksess-relatert output — same farge attgjevast her for
skjemanamna.

## Steg

1. `make/01-containers.mk`: legg `-e CLR_OK` til `LINKML_RUN` og
   `PYTHON_RUN` (same mønster som `LOGLVL`/`CLR_STEP`/`CLR_RST` frå
   `specs/done/gjenopprett-debug-logging-fjern-make-directory-stoy.md`) —
   utan dette når ikkje fargekoden fram til batch-generate.py/
   batch-generate-instances.py, som køyrer inne i desse kontainerane.
2. `src/assets/scripts/makefile/batch-generate.py`: les `CLR_OK` frå
   `os.environ` (same mønster som `CLR_STEP`), pakk `names` i
   `CLR_OK…CLR_RST` når han ikkje er tom.
3. `src/assets/scripts/makefile/batch-generate-instances.py`: same, i
   `filter_enabled()`.
4. `src/assets/scripts/makefile/run-parallel-gen.sh`: pakk `names` i
   `${CLR_OK}…${CLR_RST}` (køyrer på host, `CLR_OK` alt eksportert direkte
   av Make — treng ikkje `-e`-vidareføring).
5. `src/assets/scripts/makefile/convert-examples.sh`: same.
6. Verifiser med `LOGLVL=DEBUG make domain-samt`, sjekk at
   ANSI-fargekoden `\033[0;32m` (grønt) omsluttar skjemanamnet i alle
   DEBUG-linjene, også dei som køyrer inne i podman (batch-generate.py/
   batch-generate-instances.py).

## Handlingsliste

- [x] Steg 1: -e CLR_OK i LINKML_RUN/PYTHON_RUN
- [x] Steg 2: batch-generate.py
- [x] Steg 3: batch-generate-instances.py
- [x] Steg 4: run-parallel-gen.sh
- [x] Steg 5: convert-examples.sh
- [x] Steg 6: verifiser med domain-samt

## Utført

Verifisert med `LOGLVL=DEBUG make domain-samt` (output filtrert gjennom
`cat -v` for å syne rå escape-sekvensar): alle DEBUG-linjer med
"— køyrer: ..." viser no skjemanamnet omslutta av `^[[0;32m…^[[0m`
(grønt), inkludert generatorane som køyrer inne i podman-kontainarane
(merge, shacl, owl, json-schema osv. via `LINKML_RUN`, og
docgen-examples/gen-openapi/gen-asyncapi via `PYTHON_RUN`).

- `make/01-containers.mk`: `-e CLR_OK` lagt til `LINKML_RUN`/`PYTHON_RUN`
- `src/assets/scripts/makefile/batch-generate.py`: `CLR_OK` frå
  `os.environ`, skjemanamn farga grønt i "køyrer"-linja
- `src/assets/scripts/makefile/batch-generate-instances.py`: same i
  `filter_enabled()`
- `src/assets/scripts/makefile/run-parallel-gen.sh`: same
- `src/assets/scripts/makefile/convert-examples.sh`: same

Ingen biverknader på genererte artefakt- eller manifestfiler denne
gongen (verifisering avgrensa til `domain-samt`).
