# Deloverskrift og samla skip-logg for gen-openapi/gen-asyncapi

## Bakgrunn

`kompakt-generator-logging.md` (sjå `specs/done/`) innførte deloverskrift +
samla skip-debug-linje for 7 generator-makroar via `run_parallel_with_timer`,
men heldt `run_gen_with_check_parallel` (brukt av `gen-openapi` og
`gen-asyncapi`) **eksplisitt utanfor scope** — "strukturelt ulike
skip-vilkår" (manglande input-JSON-Schema-fil er ein ekstra, runtime-avhengig
sjekk desse to har som dei andre generatorane ikkje har).

Brukaren ønskjer no same mønster (deloverskrift + samla debug-skip-linje) for
desse to også, for build.yaml-flagg-sjekken spesifikt.

## Steg

1. Endre `run_gen_with_check_parallel` i `make/10-generator-macros.mk`:
   - Filtrer `$1` mot `$3` (build.yaml-flaggnamn) i build.yaml **før**
     xargs-parallelliseringa startar (same ytre bash-løkke-mønster som
     `run_parallel_with_timer`)
   - Skriv éi deloverskrift via `log_info`: `→ <generator>: domain/skjema1,
     domain/skjema2, ...` (eller `(ingen skjema aktivert)` om tom liste)
   - Skriv éi samla `log_debug`-linje for build.yaml-flagg-skip:
     `hoppar over (<flag>: false): domain/skjemaX, domain/skjemaY` —
     berre synleg på `LOGLVL=DEBUG` (bruk `: false`-formatet, ikkje
     `ikkje sett`, jf. tilsvarande endring nyleg gjort i
     `run_parallel_with_timer`)
   - Køyr xargs berre på dei filtrerte (aktiverte) skjemaa
   - **Uendra:** den separate "input-fil finst ikkje"-sjekken inni
     xargs-workeren (ÅTVARING via `log_error`) — strukturelt ulikt,
     kjøretidsavhengig vilkår, ikkje del av denne endringa
2. **Utanfor scope, urørt:** `domain_target` sin separate, hand-dupliserte
   `PARALLEL=1`-inline-kopi av openapi/asyncapi-logikken i
   `make/20-domain-targets.mk` (linje 73-118) — kallar ikkje
   `run_gen_with_check_parallel` i det heile, så denne endringa når han
   ikkje. Kjent, tidlegare flagga tech debt (`dry-opprydding.md`), ikkje
   del av dette oppdraget.
3. Verifiser med `make -n domain-fair` (eller eit domene med
   openapi/asyncapi-flagg aktivert) — dry-run, sjekk make-escaping.
4. Reell test: `make domain-<domene med openapi/asyncapi>` — stadfest
   deloverskrift + artefaktgenerering framleis fungerer identisk.
5. `LOGLVL=DEBUG` reell test — stadfest skip-samandraget vert vist.

## Handlingsliste

- [x] Endre `run_gen_with_check_parallel` med filtrering + deloverskrift + samla skip-logg
- [x] `make -n` dry-run
- [x] Reell test (INFO-nivå)
- [x] `LOGLVL=DEBUG` skip-logg verifisert
- [x] Commit-melding

## Utført

`run_gen_with_check_parallel` filtrerer no `$1` mot `$3` (build.yaml-flagg)
FØR xargs-parallelliseringa startar, med same mønster som
`run_parallel_with_timer`: éi `log_info`-deloverskrift med aktiverte
domain/skjema (eller `(ingen skjema aktivert)`), og — berre på
`LOGLVL=DEBUG` — éi samla `log_debug`-linje `hoppar over (<flag>: false):
...` for build.yaml-skip. Den separate "input-fil finst ikkje"-sjekken inni
xargs-workeren er urørt.

**Viktig fiks undervegs:** første forsøk kopierte `run_parallel_with_timer`
sin leiande `@` inn i den nye ytre løkka. Det er feil for denne makroen —
`run_gen_with_check_parallel` vert, i motsetnad til `run_parallel_with_timer`,
**aldri** kalla som ei sjølvstendig make-recipe-linje. Han vert berre kalla
(via `run_gen_openapi_parallel`/`run_gen_asyncapi_parallel`) embedda midt inne
i eit anna, allereie `@`-prefikset shell-script i
`make/20-domain-targets.mk` (PARALLEL≠1-greina av `domain_target`). Ein
ekstra `@` der hamnar som eit bokstaveleg teikn midt i bash-scriptet og feilar
med "command not found". Retta ved å fjerne `@`-en — silencing kjem allereie
frå kallestaden.

Verifisert med `make -n domain-fint` (dry-run), reell `make domain-fint`
(stadfesta korrekt deloverskrift + uendra artefaktgenerering, alle 7
openapi-aktiverte fint-skjema, `gen-asyncapi: (ingen skjema aktivert)` sidan
ingen fint-skjema har `asyncapi: true`), og isolert bash-simulering av
filter-/logg-logikken med `LOGLVL=DEBUG` (stadfesta at skip-linja
`[DEBUG]   hoppar over (asyncapi: false): fint/fint-administrasjon,
fint/fint-common` vert vist, og usynleg på default INFO-nivå).

Diskutert, ikkje utført: brukaren spurde om `run_gen_with_check_parallel` og
`run_parallel_with_timer` kan slåast saman til eitt delt script. Vurdering:
den attverande skilnaden (obligatorisk vs. valfritt build.yaml-flagg, pluss
openapi/asyncapi sin ekstra kjøretidsavhengige input-fil-sjekk) gjer ei rein
makro-samanslåing mindre lesbar (fleire posisjonelle argument). Betre
kandidat er å skilje ut sjølve orkestrerings-scaffoldinga (pre-filter →
deloverskrift → samla skip-logg → xargs → per-skjema timer/trap) til eit delt
shell-script under `src/assets/scripts/makefile/`, i tråd med korleis anna
ikkje-triviell logikk (gen-openapi.py, filter_plantuml.py o.l.) allereie er
flytta ut av Makefile-et. Ikkje starta — cross-cutting endring som råkar
genereringsstien til alle domene, føreslått som eiga spec/økt.
