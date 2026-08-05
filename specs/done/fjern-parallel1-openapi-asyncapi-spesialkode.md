# Fjern PARALLEL=1-spesialbehandling for gen-openapi/gen-asyncapi

## Bakgrunn

`domain_target` i `make/20-domain-targets.mk` (linje 73-118) har ei tredje,
hand-duplisert kopi av openapi/asyncapi-genereringslogikken, bak eit
`@if [ "$(PARALLEL)" = "1" ]; then ... else $(call run_gen_X_parallel,...) fi`.
Når `PARALLEL=1` køyrer han ein eigen, inline `for schema in ...`-løkke
(ingen build.yaml-flagg-filtrering før løkka, ingen deloverskrift, ingen
samla skip-logg, ingen `run_logged`/`ERR`-trap-feilhandtering) i staden for
å kalle `run_gen_openapi_parallel`/`run_gen_asyncapi_parallel` slik alle
andre generator-steg i pipelinen gjer uavhengig av `PARALLEL`-verdi.

Dette er kjend, tidlegare flagga tech debt:

- `specs/done/dry-opprydding.md` fjerna akkurat denne typen
  "PARALLEL=1 → eigen serial-grein"-mekanisme frå `run_parallel_with_timer`
  (brukt av dei 7 andre generator-stega), og stadfesta empirisk at
  `xargs -P 1` gir identisk, korrekt output som ei eigentleg serialisert
  løkke — men fann samstundes at `domain_target` sin EIGEN,
  hand-dupliserte openapi/asyncapi-spesialgrein var eit anna, urelatert
  funn, og let han stå urørt for å halde den økta sitt omfang handterleg.
- `specs/done/deloverskrift-openapi-asyncapi.md` og
  `specs/done/delt-script-parallell-generering.md` (siste økt, som flytta
  openapi/asyncapi over på det delte `run-parallel-gen.sh`-scriptet) heldt
  begge denne PARALLEL=1-greina eksplisitt utanfor scope av same grunn.

Konsekvensar av at spesialgreina framleis finst:
- **Under `PARALLEL=1` mister openapi/asyncapi** den nye deloverskrifta og
  samla skip-debug-linja som resten av pipelinen no har (frå
  `run-parallel-gen.sh`) — inkonsistent brukaropplevd logg avhengig av
  `PARALLEL`-verdi
- **Feilhandtering er svakare**: inline-greina manglar `run_logged`
  (fangar ikkje stdout/stderr ved feil, ingen strukturert
  `::error file=...`-annotasjon til GitHub Actions) og manglar `ERR`-trap
  — eit skjema som feilar midt i `&&`-kjeda kan i verste fall halde fram
  til neste skjema utan tydeleg feilsignal, i strid med "Ingen stille
  feil"-prinsippet i CLAUDE.md
- **Kodeduplikasjon**: same logikk (flagg-sjekk, input-fil-sjekk,
  podman-kall) finst no tre stader for openapi (serial `run_gen_openapi`,
  parallell `run_gen_openapi_parallel`/scriptet, OG denne inline-greina) —
  DRY-prinsippet i CLAUDE.md set terskelen til tre identiske tilfelle, som
  er nådd

## Mål

Fjern PARALLEL=1-spesialgreina heilt frå `domain_target`. La openapi/asyncapi
alltid gå gjennom `run_gen_openapi_parallel`/`run_gen_asyncapi_parallel`
(→ `run-parallel-gen.sh`, som allereie køyrer korrekt med `xargs -P 1` når
`PARALLEL=1` — same mekanisme som dei 7 andre generator-stega i pipelinen
alt brukar uavhengig av `PARALLEL`-verdi).

## Design

### `make/20-domain-targets.mk`

Erstatt linje 73-118 (dei to `@if [ "$(PARALLEL)" = "1" ]; then ... else ... fi`-
blokkene) med to enkle, sjølvstendige recipe-linjer, i same stil som dei
andre kalla i `domain_target` (t.d. linje 39, 44-45, 68-71):

```make
	$$(call run_gen_openapi_parallel,$$(_schemas_$(1)))
	$$(call run_gen_asyncapi_parallel,$$(_schemas_$(1)))
```

### `make/10-generator-macros.mk`

`run_gen_openapi_parallel`/`run_gen_asyncapi_parallel` er i dag medvite
**utan** leiande `@`, fordi dei vert kalla embedda inne i domain_target sitt
`PARALLEL≠1`-shell-script (sjå kommentaren rett over kvar makro, sett i
`specs/done/delt-script-parallell-generering.md`). Når dei no i staden vert
kalla som sjølvstendige recipe-linjer (same mønster som dei 7 andre
`_parallel`-makroane), MÅ dei ha leiande `@` for å ikkje ekko kommandoen —
akkurat som `run_gen_owl_parallel` m.fl. Fjern samstundes "NB: kalla
embedda..."-kommentaren over begge makroane, sidan han ikkje lenger er
korrekt.

**Kritisk å verifisere:** dette er nøyaktig den type endring som tidlegare
gav ein reell bug i denne serien av økter (feilplassert `@` gav
"command not found" — sjå `specs/done/deloverskrift-openapi-asyncapi.md`).
Denne gongen er endringa MOTSETT retning (leggje TIL `@` fordi kallstaden
vert enklare, ikkje fjerne han) — men same varsemd gjeld: verifiser med
`make -n` at det ikkje oppstår dobbel-`@` eller manglande `@` nokon stad.

## Steg

1. Fjern PARALLEL=1-if/else-greinene i `make/20-domain-targets.mk` (linje
   73-118), erstatt med dei to enkle `$$(call run_gen_X_parallel, ...)`-
   linjene
2. Legg til leiande `@` på `run_gen_openapi_parallel` og
   `run_gen_asyncapi_parallel` i `make/10-generator-macros.mk`; fjern
   "NB: kalla embedda..."-kommentarane over begge
3. `make -n domain-samt` (både utan `PARALLEL` og med `PARALLEL=1`) —
   dry-run, stadfest korrekt make-escaping og at ingen linje har dobbel
   eller manglande `@`
4. Reell test: `make domain-samt` (standard `PARALLEL`) — stadfest
   deloverskrift + artefaktgenerering identisk til før
5. Reell test: `make PARALLEL=1 domain-samt` — stadfest at openapi/asyncapi
   NO OGSÅ får deloverskrift + samla skip-logg-mønster (tidlegare synte
   denne køyringa den gamle, mindre kompakte `→ gen-openapi  <sti>`-forma)
6. `LOGLVL=DEBUG make PARALLEL=1 domain-fair` — stadfest at skip-debug-linja
   for openapi/asyncapi no også vert vist under `PARALLEL=1` (tidlegare
   berre verifisert under standard `PARALLEL`, jf.
   `specs/done/delt-script-parallell-generering.md`)
7. Stadfest at standalone `make gen-openapi SCHEMA=...`/`make gen-asyncapi
   SCHEMA=...` (som brukar dei separate serial-makroane `run_gen_openapi`/
   `run_gen_asyncapi` i `make/11-generator-targets.mk`, urørt av denne
   endringa) framleis fungerer uendra

## Handlingsliste

- [x] Fjern PARALLEL=1-if/else-greinene i `domain_target`
- [x] Legg til leiande `@` på dei to wrapper-makroane, fjern stale kommentarar
- [x] `make -n` dry-run (standard + `PARALLEL=1`)
- [x] Reell test `make domain-samt` (standard `PARALLEL`)
- [x] Reell test `make PARALLEL=1 domain-samt`
- [x] `LOGLVL=DEBUG` skip-logg verifisert under `PARALLEL=1`
- [x] Stadfest standalone `make gen-openapi`/`gen-asyncapi` SCHEMA=... urørt
- [x] Commit-melding

## Utført

`domain_target` (`make/20-domain-targets.mk`) sine to
`@if [ "$(PARALLEL)" = "1" ]; then ... else $(call run_gen_X_parallel,...) fi`-
blokker (46 linjer) er erstatta med to enkle, sjølvstendige recipe-linjer:

```make
	$$(call run_gen_openapi_parallel,$$(_schemas_$(1)))
	$$(call run_gen_asyncapi_parallel,$$(_schemas_$(1)))
```

`run_gen_openapi_parallel`/`run_gen_asyncapi_parallel`
(`make/10-generator-macros.mk`) har no leiande `@` (dei vert ikkje lenger
kalla embedda inne i eit anna shell-script), og dei tilhøyrande
"NB: kalla embedda..."-kommentarane er fjerna sidan dei ikkje lenger er
korrekte. Openapi/asyncapi går no gjennom akkurat same kodesti som dei 7
andre generator-stega i pipelinen, uavhengig av `PARALLEL`-verdi — den
tredje, hand-dupliserte kopien av openapi/asyncapi-logikken (flagga som
tech debt i `dry-opprydding.md`, halden utanfor scope i
`deloverskrift-openapi-asyncapi.md` og `delt-script-parallell-generering.md`)
er dermed borte.

**Verifisering:**
- `make -n domain-samt` (standard og `PARALLEL=1`) — dry-run stadfesta
  korrekt make-escaping, ingen dobbel eller manglande `@`, openapi/asyncapi
  no som separate, sjølvstendige `GEN_CMD=...`-linjer identisk i form til
  dei andre 7 migrerte makroane
- Reell `make domain-samt` (standard `PARALLEL=16`): alle 14 forventa
  artefaktfiler generert korrekt, uendra frå før denne endringa
- Reell `make PARALLEL=1 domain-samt`: same 14 artefaktfiler generert
  korrekt. **Loggforma for gen-openapi/gen-asyncapi er no identisk til
  standard-`PARALLEL`-køyringa** (`→ gen-openapi: samt/samt-bu` +
  `→ gen-openapi  samt/samt-bu (Xs)`) — tidlegare synte `PARALLEL=1` den
  eldre, mindre kompakte `→ gen-openapi  <sti>`-forma utan deloverskrift
- `LOGLVL=DEBUG make PARALLEL=1 domain-fair`: stadfesta at
  `(ingen skjema aktivert)` + samla `hoppar over (openapi: false)`/
  `hoppar over (asyncapi: false)`-debug-linjene no også vert viste under
  `PARALLEL=1` — dette var ikkje mogleg å teste før denne endringa, sidan
  `PARALLEL=1` gjekk gjennom den gamle inline-greina utan build.yaml-
  filtrering eller logging i det heile
- `make gen-openapi SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml`
  (standalone target, brukar den urørte serial-makroen `run_gen_openapi`):
  fungerer uendra, stadfesta `openapi-spec-validator: OK`
