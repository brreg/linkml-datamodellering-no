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

- [x] Skriv `run-parallel-gen.sh` med argument-parsing, filter, deloverskrift, skip-logg, xargs-løkke
- [x] Pilot: migrer `run_gen_owl_parallel`, verifiser dry-run + reell test
- [x] Migrer resterande 6 `run_parallel_with_timer`-kallarar
- [x] Migrer `run_gen_openapi_parallel`/`run_gen_asyncapi_parallel` (embedda kallstad)
- [x] Fjern `run_parallel_with_timer` og `run_gen_with_check_parallel`
- [x] Full regresjonstest (standard `PARALLEL` + `PARALLEL=1`, artefakt-diff)
- [x] `LOGLVL=DEBUG` skip-logg verifisert for begge variantar
- [x] Commit-melding

## Utført

Alle 9 kallarar (7 tidlegare via `run_parallel_with_timer`, 2 via
`run_gen_with_check_parallel`) migrert til å kalle det nye, delte
`src/assets/scripts/makefile/run-parallel-gen.sh` — parametrisert med
`--generator`, valfri `--flag` (build.yaml-flagg, utelaten for
`run_gen_linkml_parallel` som ikkje har noko flagg å filtrere mot), valfri
`--check-suffix`/`--out-suffix` (openapi/asyncapi sin
input-fil-eksistenssjekk + output-filnamn), og sjølve genererings-kommandoen
via miljøvariabelen `GEN_CMD` (`eval`-a inne i kvar xargs-arbeidar). Dei to
gamle scaffolding-makroane (`run_parallel_with_timer`,
`run_gen_with_check_parallel`) er fjerna frå `make/10-generator-macros.mk`
saman med sine stale kryssreferansar i kommentarar.

Skriptet gjer scaffoldinga (build.yaml-filtrering, deloverskrift,
samla skip-debug-linje, `xargs -P`, per-skjema timer, `ERR`-trap) om til
vanleg, lineært bash — ingen nøsta bash-i-bash-i-xargs-i-make-escaping att.
`GEN_DIR`, `PARALLEL`, `CLR_STEP`, `CLR_RST` er no eksporterte frå
`make/00-settings.mk` (saman med det allereie eksporterte `LOG_FUNCTIONS`)
slik at scriptet — som ein sjølvstendig prosess, ikkje make-generert tekst —
har tilgang til dei same verdiane utan å måtte tekst-substituerast inn.

**Kritisk detalj halden ved lag frå openapi/asyncapi-migreringa i førre
økt:** `run_gen_openapi_parallel`/`run_gen_asyncapi_parallel` vert kalla
embedda inne i `domain_target` sitt `PARALLEL≠1`-shell-script
(`make/20-domain-targets.mk`), IKKJE som sjølvstendige recipe-linjer — dei
har difor ingen leiande `@` i den nye wrapper-makroen (silencing kjem frå
kallestaden). Dei andre 7 wrapper-makroane KALLAST som sjølvstendige
recipe-linjer og har difor leiande `@`. Feil plassering av `@` her var
nøyaktig same feilkjelde som vart oppdaga og retta i
`specs/done/deloverskrift-openapi-asyncapi.md` — no eksplisitt dokumentert
med ein kommentar rett over begge desse to makroane.

**Verifisering:**
- Isolert scripttesting (mocka `LOG_FUNCTIONS`/`GEN_CMD`, utan podman):
  flagg-filtrering, valfri flagg (ingen filtrering), `--check-suffix` (både
  fil-finst og fil-manglar-grein), `ERR`-trap-propagering ved ekte
  kommandofeil (stadfesta at `exit`-builtin i `GEN_CMD` IKKJE utløyser ERR-
  trap, som forventa bash-åtferd — testa med `false` i staden, som stadfesta
  at feilhandteringa fungerer identisk til dei gamle makroane)
- `make -n domain-samt` (standard og `PARALLEL=1`) — dry-run, stadfesta
  korrekt make-escaping for alle 9 kallstader, inkludert embedda
  openapi/asyncapi
- Reell `make domain-samt` (samt-bu — einaste skjema med `xsd`, `openapi`
  OG `asyncapi` alle `true`, jf. `specs/done/parallelliser-image-pull-validate-workflow.md`):
  alle 14 forventa artefaktfiler + diagrams/docs/docgen-examples-katalogar
  generert korrekt, openapi/asyncapi-YAML validert av dei respektive
  spec-validatorane
- Reell `make PARALLEL=1 domain-samt`: same artefaktsett generert korrekt;
  openapi/asyncapi brukte som venta den utanfor-scope, urørte
  `PARALLEL=1`-inline-greina (ikkje det nye scriptet) — stadfesta at dette
  framleis fungerer uendra
- Ikkje-determinisme i TTL/OWL-utdata (blank-node-rekkjefølgje) og
  `generation_date`-tidsstempel stadfesta å vere ein eigenskap ved
  LinkML/rdflib-verktøya sjølve (to reine `podman run gen-owl`-kall utanom
  make, rett etter kvarandre, gav ulik blank-node-rekkjefølgje) — urelatert
  til denne refaktoreringa, difor ikkje eit gyldig regresjonssignal
- `LOGLVL=DEBUG make domain-fair` (mange build.yaml-flagg `false`):
  stadfesta korrekt `(ingen skjema aktivert)` + samla skip-debug-linje for
  BÅDE `run_gen_parallel`-familien (jsonld_context, python, json_schema,
  protobuf) OG dei embedda openapi/asyncapi-kallstadene — inkludert
  "alle skjema hoppa over"-tilfellet for embedda-kallstaden, som ikkje vart
  eksplisitt testa i `specs/done/deloverskrift-openapi-asyncapi.md`

**Sideeffekt oppdaga under testing, ikkje del av denne endringa:**
`make domain-fair`-køyringane regenererte
`src/linkml/fair/fair-metadata/metadata/fair-metadata-manifest.yaml` med
oppdatert `versjonsnummer`/`endringsdato`/`kontaktpunkt` — normal åtferd frå
`gen-informasjonsmodell-instance` (urelatert makro, ikkje del av denne
speccen) som synkroniserer instansen mot noverande skjema-state. Fila var
tydelegvis ute av synk frå før denne økta. Ikkje revertert — brukaren avgjer
sjølv om endringa skal behaldast.
