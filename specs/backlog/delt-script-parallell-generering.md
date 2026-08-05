# Delt shell-script for parallell artefaktgenerering

## Bakgrunn

`make/10-generator-macros.mk` har i dag to nesten identiske makroar for
parallell generering, gata mot eit build.yaml-flagg:

- `run_parallel_with_timer` — delt av 7 kallarar (`run_gen_parallel`,
  `run_gen_owl_parallel`, `run_gen_rdf_parallel`, `run_gen_doc_parallel`,
  `run_gen_erdiagram_parallel`, `run_gen_plantuml_parallel`,
  `run_gen_linkml_parallel`). Flagget (`$4`) er valfritt — tom streng
  betyr inga filtrering.
- `run_gen_with_check_parallel` — delt av 2 kallarar (`run_gen_openapi_parallel`,
  `run_gen_asyncapi_parallel`). Flagget (`$3`) er obligatorisk, og han har
  éin ekstra, kjøretidsavhengig sjekk: om input-fila (`$name-$4`, t.d.
  JSON Schema frå eit tidlegare steg i pipelinen) faktisk finst før
  kommandoen køyrer.

Begge implementerer same scaffolding — pre-filtrer skjemalista mot
build.yaml FØR `xargs`-parallelliseringa startar, skriv éi `log_info`-
deloverskrift med aktiverte skjema, skriv éi samla `log_debug`-skip-linje,
og køyrer sjølve genererings-kommandoen per skjema via
`xargs -P $(PARALLEL)` med timer og `ERR`-trap. Denne scaffoldinga er no
duplisert byte-for-byte i to `define`-blokker (~50 linjer kvar), skriven som
sterkt nøsta bash-i-bash-i-xargs-i-make med tre nivå `$`/`$$`/`$$$$`-escaping.
Denne økta (sjå `specs/done/deloverskrift-openapi-asyncapi.md`) trefte
allereie éin reell bug frå denne kompleksiteten — ein feilplassert leiande
`@` frå `run_parallel_with_timer` kopiert inn i `run_gen_with_check_parallel`,
som ville feila med "command not found" fordi sistnemnde vert kalla embedda
midt inne i eit anna, allereie `@`-prefiksert shell-script (`domain_target`
i `make/20-domain-targets.mk`), ikkje som ei sjølvstendig recipe-linje.

Repoet har alt ein etablert konvensjon for å handtere ikkje-triviell logikk:
flytt han ut av Makefile-et og inn i `src/assets/scripts/makefile/*.py`
(`gen-openapi.py`, `filter_plantuml.py`, `filter_erdiagram.py`,
`gen-docgen-examples.py` m.fl.). Denne speccen brukar same prinsipp, men for
sjølve **orkestreringa** (filtrering, deloverskrift, skip-logg, xargs,
timer, feilhandtering) — ikkje for genererings-kommandoane, som framleis er
generator-spesifikke og varierer for mykje (podman-kall, python-script,
multi-steg `&&`-kjeder, awk-pipe) til å generiserast bort.

## Mål

Éi delt fil, `src/assets/scripts/makefile/run-parallel-gen.sh`, som eig
scaffoldinga. Alle 9 eksisterande kallarar (7 via `run_parallel_with_timer`,
2 via `run_gen_with_check_parallel`) kallar dette scriptet i staden for å
duplisere logikken i to parallelle `define`-blokker. `run_gen_xsd` (eiga,
strukturelt ulik serial-løkke) og `domain_target` sin separate,
hand-dupliserte `PARALLEL=1`-inline-kopi av openapi/asyncapi
(`make/20-domain-targets.mk` linje 73-118, kjend tech debt frå
`dry-opprydding.md`) er **utanfor scope** for denne speccen.

## Design

### Scriptgrensesnitt

```
run-parallel-gen.sh --generator <namn> [--flag <build.yaml-flaggnamn>] \
    [--check-suffix <input-filsuffiks>] -- <skjema1> <skjema2> ...
```

- `--generator` — namn brukt i loggmeldingar (t.d. `gen-owl`, `gen-openapi`)
- `--flag` — valfritt. Om sett: filtrer skjemalista mot
  `grep -q "^  <flag>: true" <skjema-dir>/build.yaml` FØR parallellisering.
  Om usett: inga filtrering (svarar til `run_parallel_with_timer` sitt
  tomme `$4`, brukt av `run_gen_linkml_parallel`)
- `--check-suffix` — valfritt. Om sett: kvar arbeidar sjekkar at
  `$outdir/$name-<suffix>` finst før kommandoen køyrer, elles
  `log_error "ÅTVARING: ... finst ikkje"` og hoppar over (svarar til
  `run_gen_with_check_parallel` sin `$4`/input-sjekk). Når sett, eksporterer
  scriptet også `$input` (= `$outdir/$name-<suffix>`) til kommandoen, slik
  openapi/asyncapi-kommandoane kan referere `"$input"` direkte
- Kommandoen som skal køyrast per skjema vert gitt via miljøvariabelen
  `GEN_CMD` (unngår å sende ein multi-linje shell-streng gjennom enda eit
  lag med argv-escaping) — kalt med `eval "$GEN_CMD"` inne i kvar
  xargs-arbeidar, med `$s`, `$name`, `$domain`, `$outdir` (og `$input` der
  `--check-suffix` er sett) tilgjengeleg som lokale shell-variablar
- `PARALLEL` (miljøvariabel, alt sett av Makefile) styrer `xargs -P`
- `LOG_FUNCTIONS` er alt eksportert frå `make/00-settings.mk` — scriptet gjer
  berre `eval "$LOG_FUNCTIONS"` slik dei eksisterande makroane gjer

### Makroane vert tynne wrapparar

```make
define run_gen_owl_parallel
GEN_CMD='mkdir -p "$$outdir" && $(LINKML_RUN) gen-owl $(OWL_DEFAULT_FLAGS) "$$s" > "$$outdir/$$name-ontology.ttl"' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-owl --flag owl -- $(1)
endef
```

```make
define run_gen_openapi_parallel
GEN_CMD='run_logged "gen-openapi $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py /work/$$input /work/$$s --out /work/$$out && run_logged "openapi-spec-validator $$domain/$$name" $(PYTHON_RUN) openapi-spec-validator /work/$$out' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-openapi --flag openapi --check-suffix schema.json -- $(1)
endef
```

(Nøyaktig escaping av `$$` vs `$$$$` må verifiserast per kallstad — særleg
for `run_gen_openapi_parallel`/`run_gen_asyncapi_parallel`, som i dag vert
kalla embedda inne i `domain_target` sitt `PARALLEL≠1`-shell-script, ikkje
som sjølvstendige recipe-linjer. Silencing (`@`) skal **ikkje** liggje i
scriptet eller i wrapper-makroen for desse to — han kjem frå kallestaden,
same feilkjelde som vart retta i denne økta.)

### `out`-variabel for openapi/asyncapi

`run_gen_with_check_parallel` sitt `$5` (output-suffiks) vert i dag brukt av
kommandoen (`$5.` → `"$$out"`) til å byggje output-filnamnet. Scriptet må
tilby tilsvarande — anten som eit eige `--out-suffix`-flagg (eksporterer
`$out`), eller ved å la kallaren byggje `$out` sjølv frå `$outdir`/`$name`
inne i `GEN_CMD`. Avgjer under implementering — hald grensesnittet minimalt.

## Steg

1. Skriv `src/assets/scripts/makefile/run-parallel-gen.sh`:
   - Argument-parsing (`--generator`, `--flag`, `--check-suffix`)
   - Pre-filter-løkke (build.yaml-flagg) → `enabled`/`skipped`
   - Deloverskrift (`log_info`) + samla skip-linje (`log_debug`,
     `hoppar over (<flag>: false): ...`)
   - `xargs -P "$PARALLEL"` over `enabled`, kvar arbeidar: set opp
     `s`/`name`/`domain`/`outdir` (+ `input` om `--check-suffix`), `ERR`-trap,
     valfri input-fil-sjekk, timer, `eval "$GEN_CMD"`, logg elapsed
   - `chmod +x`
2. Migrer **éin** kallar først som pilot — anbefalt `run_gen_owl_parallel`
   (enkel, eitt output, alt brukt i `run_parallel_with_timer`-familien) —
   for å verifisere grensesnittet før resten flyttast
3. `make -n domain-fair` (dry-run) + reell `make domain-fair` for pilot-kallaren
4. Migrer resten av `run_parallel_with_timer`-familien
   (`run_gen_parallel`, `run_gen_rdf_parallel`, `run_gen_doc_parallel`,
   `run_gen_erdiagram_parallel`, `run_gen_plantuml_parallel`,
   `run_gen_linkml_parallel`) éin om gongen, med `make -n` + reell
   domain-test mellom kvar
5. Migrer `run_gen_openapi_parallel`/`run_gen_asyncapi_parallel` (embedda
   kallstad — ekstra varsam verifisering av `@`-plassering og
   `$$`-escaping, sidan dette er der forrige bug oppstod)
6. Fjern `run_parallel_with_timer` og `run_gen_with_check_parallel` frå
   `make/10-generator-macros.mk` når alle kallarar er migrerte
7. Full regresjonstest: `make domain-<eit representativt domene>` med
   standard `PARALLEL` OG `PARALLEL=1`, samanlikn artefakt-output
   (filnamn, innhald) mot ein build frå før migreringa
8. `LOGLVL=DEBUG`-test — stadfest skip-logg framleis fungerer for minst éin
   `--flag`- og éin `--check-suffix`-kallar

## Handlingsliste

- [ ] Skriv `run-parallel-gen.sh` med argument-parsing, filter, deloverskrift, skip-logg, xargs-løkke
- [ ] Pilot: migrer `run_gen_owl_parallel`, verifiser dry-run + reell test
- [ ] Migrer resterande 6 `run_parallel_with_timer`-kallarar
- [ ] Migrer `run_gen_openapi_parallel`/`run_gen_asyncapi_parallel` (embedda kallstad)
- [ ] Fjern `run_parallel_with_timer` og `run_gen_with_check_parallel`
- [ ] Full regresjonstest (standard `PARALLEL` + `PARALLEL=1`, artefakt-diff)
- [ ] `LOGLVL=DEBUG` skip-logg verifisert for begge variantar
- [ ] Commit-melding
