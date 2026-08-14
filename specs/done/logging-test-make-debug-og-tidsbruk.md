# DEBUG-logging av testkall og INFO-logging av tidsbruk i test_make.sh

## Bakgrunn

Brukaren ønskjer at `tests/test_make.sh` DEBUG-loggar alle testkall og
INFO-loggar tidsbruken for kvart kall, på same måte som logginga i
`make domain-<domain>` (t.d. `[DEBUG] gen-rdf (rdf: true) — køyrer:
referansemodell-bronze, ...` følgt av `→ rdf  referanse/referansemodell-bronze
(2.43s)`). I tillegg skal standard `LOGLVL` for test-kommandoane vere
`DEBUG` (ikkje den globale standarden `INFO`), slik at DEBUG-utskrifta er
synleg utan at brukaren treng eksportere `LOGLVL=DEBUG` manuelt kvar gong —
men eksplisitt `LOGLVL=<verdi>`-overstyring på kommandolinja skal framleis
respekterast.

## Undersøking

### Den etablerte logg-infrastrukturen finst alt, delt via `LOG_FUNCTIONS`

`make/00-settings.mk` (linje 53-121) definerer `LOG_FUNCTIONS` — eit
`define...endef`-bash-snippet, `export`-ert som miljøvariabel — med
`log_debug()`/`log_info()`/`log_error()`/`fmt_elapsed_ms()`/`timed_run()`/
`run_logged()`. `LOGLVL`/fargevariablane (`CLR_STEP`, `CLR_DBG` osv.) er
òg `export`-erte (linje 126-142). Dette ER kjelda til «make
domain-<domain>»-logginga brukaren refererer til:

- `run-domain-pipeline.sh:34` (drivar for `make domain-<domain>`): `eval
  "$LOG_FUNCTIONS"` rett etter `set -euo pipefail`.
- `mkdocs/publish.sh:7-8` (drivar for `make docs-publish`): same mønster,
  med ein eksplisitt `:?`-sjekk på at variabelen faktisk er sett.

Fordi `LOG_FUNCTIONS` er `export`-ert som Make-variabel, arvar **alle**
`make`-recipe-subprosessar han automatisk (inkludert
`bash tests/test_make.sh "$(SCHEMA)"` i `Makefile:84`) — utan at
Makefile-recipa treng eit eksplisitt `eval`. Skriptet må berre gjere
`eval "$LOG_FUNCTIONS"` sjølv, akkurat som dei to eksempla over.

**`tests/test_make.sh` brukar IKKJE denne infrastrukturen i dag** — han
definerer sine eigne, lokale `CLR_OK`/`CLR_ERR`/`CLR_RST` (linje 18-20) og
har ingen `log_debug`/`log_info`/`LOGLVL`-medvit i det heile.

### To ulike lag med testkall — ulik status i dag

**Fase A** (batch-generering/-konvertering på tvers av skjema,
`run_phase_a_step()`/`_run_phase_a_convert_batch()`/`run_phase_a_lint()`/
`run_phase_a_mcp_instance()`/`run_phase_a_linkml_validate()`): den
underliggande `make "$target" SCHEMAS=...`/`batch-*.py`-koden **har alt**
DEBUG/INFO-logging med tidsbruk innebygd (`batch-generate.py` sine eigne
`log_debug()`/`log_info()`, som les `LOGLVL`/`CLR_STEP` direkte frå
`os.environ` — jf. kommentaren i `00-settings.mk:123-125`). Denne
utskrifta hamnar i dag i ei per-nøkkel loggfil
(`phase_a_logfile()`/`$LOGDIR/phase_a_<key>.log`) som vert limt inn i
`$LOG` **etter** at steget er ferdig — synleg i den endelege loggfila,
men ikkje strøymd live til terminalen, og **utan noka steg-nivå
tidsmåling** (berre dei individuelle per-skjema-linjene frå Python-sida).
Sidan Del 1 (jf. `specs/done/paralleliser-fase-a-test-make.md`) no køyrer
alle 17 Fase A-steg samstundes, er det medvite at rå-utskrifta **ikkje**
strøymer live (17 samstundes interleava DEBUG-straumar ville vore
ulesarleg) — men steget sjølv manglar ei samla `timed_run`-liknande
INFO-linje som seier «steg X tok Y sekund totalt».

**Fase B** (`_run_one()`, det faktiske per-skjema-per-testtype-kallet —
`validate (samt-bu)`, `roundtrip-ttl (fint-utdanning)` osv.) **har INGEN**
DEBUG- eller tidsloggmedvit i det heile i dag — berre eit
`OK`/`FEIL`-symbol på terminalen (`>&3`), ingen `(X.XXs)`-tidsangjeving,
og ingen `[DEBUG]`-linje før kallet startar.

## Tiltak

| # | Tiltak | Fil |
|---|---|---|
| 0 | Sett standard `LOGLVL=DEBUG` for test-kommandoane (`test`, `roundtrip`, `roundtrip-json-schema` — alle tre kallar `bash tests/test_make.sh` direkte) via target-spesifikk Make-variabel, med eksplisitt `origin`-sjekk slik at `LOGLVL=<verdi> make test` (kommandolinje-overstyring) framleis vinn: `test roundtrip roundtrip-json-schema: LOGLVL := $(if $(filter command line,$(origin LOGLVL)),$(LOGLVL),DEBUG)`. Den globale standarden (`LOGLVL ?= INFO` i `00-settings.mk`, brukt av `gen-*`/`domain-*`-mål m.fl.) er uendra | `Makefile` |
| 1 | Fjern dei lokale `CLR_OK`/`CLR_ERR`/`CLR_RST`-definisjonane (linje 18-20) og legg til `eval "$LOG_FUNCTIONS"` rett etter `set -euo pipefail`/`cd "$REPO_ROOT"` — same mønster og plassering som `run-domain-pipeline.sh:25,34` og `mkdocs/publish.sh:7-8` (inkl. `:?`-sjekk på at `LOG_FUNCTIONS` faktisk er sett, for tydeleg feil dersom scriptet nokon gong køyrer utanfor `make`) | `tests/test_make.sh` |
| 2 | I `_run_one()`: legg til `log_debug "→ $tname"` rett før `"$@" 2>&1` køyrer, og mål tidsbruk (`t0=$(date +%s%3N)` … `elapsed=$(( $(date +%s%3N) - t0 ))`, same mønster som `timed_run()` i `LOG_FUNCTIONS`) — på suksess, legg til ei `log_info`-linje med `$(fmt_elapsed_ms $elapsed)`, i **tillegg til** (ikkje i staden for) den eksisterande `>&3`-OK/FEIL-terminallinja, som held fram uendra som det primære interaktive framdriftsbiletet | `tests/test_make.sh` |
| 3 | I `run_phase_a_step()`, `run_phase_a_lint()`, `run_phase_a_mcp_instance()`, `_run_phase_a_convert_batch()`, `run_phase_a_linkml_validate()`: pakk sjølve `make "$target" ...`/`podman run ...`-kallet i `timed_run "<steg>" ...` (eller tilsvarande manuell t0/elapsed + `log_info`), slik at kvart Fase A-steg får ei eiga, samla INFO-tidslinje (`→ <steg> (X.XXs)`) — utfyller (ikkje erstattar) dei eksisterande per-skjema-DEBUG/INFO-linjene som alt kjem frå `batch-generate.py` sjølv inne i den fangede loggfila | `tests/test_make.sh` |
| 4 | Stadfest at `LOGLVL`-vidareføringa framleis fungerer heile vegen: host-miljøvariabel → `make test` → `bash tests/test_make.sh` (arva via Make sin `export`) → sub-`make "$target" ...` → `$(LINKML_RUN)` sin `-e LOGLVL` → `batch-generate.py` sin `os.environ.get("LOGLVL", "INFO")` — ingen brot i kjeda etter tiltak 1-3 | — |
| 5 | Verifiser: `make test SCHEMA=<eitt skjema>` **utan** eksplisitt `LOGLVL` — stadfest at DEBUG er ny standard (tiltak 0) og at både Fase A-steg-tidslinjer OG Fase B sine per-test `[DEBUG]`/tidslinjer er synlege i `$LOG`/stderr, utan at brukaren treng setje noko sjølv | — |
| 6 | Verifiser eksplisitt overstyring framleis fungerer og at INFO-åtferda er uendra: `LOGLVL=INFO make test SCHEMA=<eitt skjema>` — stadfest at DEBUG-linjene er usynlege, at den eksisterande `>&3`-OK/FEIL-terminalutskrifta er heilt uendra, og at `##RESULT:OK`/`##RESULT:FAIL`-markørane (brukt av `wait_for_tests()` sin parsing) er upåverka. Stadfest òg at `LOGLVL`-standarden for `gen-*`/`domain-*`-mål (INFO) er uendra av tiltak 0 | — |
| 7 | `bash -n tests/test_make.sh` (syntakssjekk) | — |

## Utført

Alle 8 tiltak (0-7) gjennomførte og verifiserte:

0. `Makefile`: ny target-spesifikk variabel rett før `test:`/`roundtrip:`/
   `roundtrip-json-schema:` — `LOGLVL := $(if $(filter command line,$(origin LOGLVL)),$(LOGLVL),DEBUG)`.
   Verifisert med `origin`-baserte probe-testar: `make test` → `LOGLVL=DEBUG`,
   `make LOGLVL=INFO test` (korrekt kommandolinje-syntaks, stadfesta mot
   `COMMANDS.md` sin dokumenterte konvensjon) → `LOGLVL=INFO` respektert,
   `make gen-python ...` (urelatert mål) → uendra global standard (INFO).
1. `tests/test_make.sh`: dei lokale `CLR_OK`/`CLR_ERR`/`CLR_RST`-definisjonane
   fjerna, erstatta med `: "${LOG_FUNCTIONS:?...}"` + `eval "$LOG_FUNCTIONS"`
   rett etter `set -euo pipefail` — same mønster som
   `run-domain-pipeline.sh`/`mkdocs/publish.sh`.
2. `_run_one()`: `log_debug "→ $tname"` lagt til før testkallet, samt
   tidsmåling (`date +%s%3N`) med ei `log_info`-tidslinje etter — i tillegg
   til, ikkje i staden for, den eksisterande `>&3`-OK/FEIL-terminallinja.
3. Alle fem Fase A-funksjonar (`run_phase_a_step`, `run_phase_a_lint`,
   `run_phase_a_mcp_instance`, `_run_phase_a_convert_batch`,
   `run_phase_a_linkml_validate`) fekk steg-nivå tidsmåling. **Viktig
   presisering oppdaga under implementering:** desse funksjonane køyrer
   backgrounda UTAN ein omsluttande redirect (ulikt `_run_one()`, som ligg
   inni eit alt-redirigert blokk via `run_schema_tests()`) — direkte
   `log_info`-kall her ville skrive til reell stderr og interleave uleseleg
   med dei 16 andre samstundes Fase A-stega (jf.
   `specs/done/paralleliser-fase-a-test-make.md`, Del 1). Tidsmålinga er
   difor bygd inn i den eksisterande `{ header; cat logfile; } >> "$LOG"`-
   blokka i staden for via direkte `log_info`-kall — konsistent med korleis
   resten av kvart steg sitt output alt vart handtert. `run_phase_a_mcp_instance()`
   vart i tillegg omstrukturert til å skrive til ei eiga loggfil først
   (matcha dei andre fire), sidan han tidlegare køyrde kommandoen direkte
   inne i loggblokka og difor ikkje kunne vite tidsbruken før blokka alt var
   skriven.
4. Stadfesta: `LOGLVL`-kjeda (host → `make test` → `bash test_make.sh` →
   sub-`make` → `$(LINKML_RUN)` → `batch-generate.py`) fungerer uendra —
   stadfesta empirisk i tiltak 5-6.
5. Verifisert: `make test SCHEMA=<eitt skjema>` (ingen eksplisitt `LOGLVL`)
   — `$LOG` inneheld no både `[DEBUG]`-linjer (frå `batch-generate.py` sjølv
   OG frå `_run_one()` sin nye `log_debug`) og INFO-tidslinjer for kvart
   testkall (`→ validate (register-over-aksjeeiere) (0.00s)` osv.) og for
   kvart Fase A-steg (`FASE A: gen-docs  (19:39:10, 26.48s)`) — utan at
   nokon miljøvariabel vart sett manuelt.
6. Verifisert: `make LOGLVL=INFO test SCHEMA=<eitt skjema>` — 0 `[DEBUG]`-
   linjer i `$LOG`, INFO-tidslinjene framleis til stades, `##RESULT:OK`-
   markørane uendra (18/18). `make roundtrip SCHEMA=...` stadfesta same
   DEBUG-standard som `test`.
7. `bash -n tests/test_make.sh` — syntaks OK.

**Full regresjonstest:** `make test` (alle 35 skjema, ny DEBUG-standard) —
**591 OK, 5 feil**, identisk resultatsett som referansen frå
`specs/done/paralleliser-fase-a-test-make.md` (same fem kjende,
pre-eksisterande BUG-3-feil). Veggklokketid 3m6,9s — uendra innanfor normal
støy (ingen meiningsfull overhead frå dei nye `date`/`printf`-kalla).

## Referanse

- `make/00-settings.mk:53-121` — `LOG_FUNCTIONS`-definisjonen (`log_debug`/`log_info`/`log_error`/`fmt_elapsed_ms`/`timed_run`/`run_logged`)
- `make/00-settings.mk:123-142` — eksport av `LOGLVL`/fargevariablar, med grunngjeving for kvifor `batch-generate.py` treng dei
- `src/assets/scripts/makefile/run-domain-pipeline.sh:25,34` — etablert `eval "$LOG_FUNCTIONS"`-mønster (drivar for «make domain-<domain>», stilen brukaren refererer til)
- `mkdocs/publish.sh:7-8` — same mønster, med eksplisitt `:?`-sjekk
- `src/assets/scripts/makefile/batch-generate.py` sine `log_debug()`/`log_info()` (linje ~81-96) — kjelda til dei individuelle per-skjema-DEBUG/INFO-linjene Fase A alt produserer
- `specs/done/paralleliser-fase-a-test-make.md` — Del 1 (kvifor Fase A sine 17 steg køyrer samstundes i dag, og kvifor rå-utskrift difor framleis bør gå til loggfil, ikkje strøymast live)
