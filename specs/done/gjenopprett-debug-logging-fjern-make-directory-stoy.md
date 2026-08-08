# Gjenopprett DEBUG-logging og fjern "Entering/Leaving directory"-støy i domain-<domain>

## Bakgrunn

Etter batching av generatorkall (kommit `77285278`, `3874ffa6` m.fl., sjå
`specs/backlog/effektiviser-generate-workflow-koyretid.md`) forsvann DEBUG-
logginga av kva skjema kvar generator genererer for, og i staden dukka det
opp støy frå GNU Make: `make[1]: Entering directory ...` / `Leaving
directory ...`.

To uavhengige regresjonar identifisert ved kodegransking:

**1. DEBUG-logging (`for schemas: ...`)**

`batch-generate.py` og `batch-generate-instances.py` les `LOGLVL`,
`CLR_STEP`, `CLR_RST` frå `os.environ` (default `LOGLVL=INFO`, tome
fargekodar). Desse skripta køyrer inne i podman via `LINKML_RUN`/
`PYTHON_RUN` (`make/01-containers.mk`), men:

- `LOGLVL` er aldri `export`-a i `make/00-settings.mk` (berre `GEN_DIR`,
  `PARALLEL`, `CLR_STEP`, `CLR_RST`, fargane m.fl. er det).
- Sjølv om han var det, forwardar korkje `LINKML_RUN` eller `PYTHON_RUN`
  miljøvariablar inn i kontaineren via `-e`.

Resultat: `log_debug(...)`-kallet i begge scripta (line ~222 i
batch-generate.py, tilsvarande i batch-generate-instances.py) ser alltid
`LOGLVL == "INFO"` og skriv aldri ut. Dette råkar dei fleste generatorane
(merge, jsonld-context, shacl, python, json-schema, owl, rdf, proto, doc,
erdiagram, plantuml, docgen-examples, openapi, informasjonsmodell-instance).

Dei få DEBUG-linjene som framleis synte seg i eksempel-loggen frå brukaren
(`linkml-convert`, `gen-xsd`, `asyncapi-validate`) kjem frå bash-skript som
køyrer direkte på host (`convert-examples.sh`, `run-parallel-gen.sh`) og
`eval`-ar `$LOG_FUNCTIONS` — der er `LOGLVL` alt bake inn i teksten av
`define LOG_FUNCTIONS`-blokka av Make sjølv, uavhengig av `export`.

**2. `Entering/Leaving directory`-støy**

Før `3874ffa6` kalla `domain_target` alle generator-makroane inline i éin
einaste `make`-prosess (ingen rekursive `$(MAKE)`-kall). No orkestrerer
`src/assets/scripts/makefile/run-domain-pipeline.sh` kvart steg som eit
**rekursivt** `$(MAKE) gen-xxx DOMAIN=$domain`-kall i eit bakgrunns-
bash-delprosess (`run_bg`). GNU Make skrur automatisk på
directory-printing (som om `-w` var gjeve) for alle sub-make-kall som
oppdagar dei køyrer under ein annan make (MAKELEVEL > 0), med mindre
`--no-print-directory` er gjeve eksplisitt.

## Steg

1. `make/00-settings.mk`: legg `LOGLVL` til `export`-lista saman med
   `GEN_DIR`/`PARALLEL`/`CLR_STEP`/`CLR_RST`.
2. `make/01-containers.mk`: legg `-e LOGLVL -e CLR_STEP -e CLR_RST` til
   `LINKML_RUN` og `PYTHON_RUN` (dei to wrapperane som køyrer
   `batch-generate.py`/`batch-generate-instances.py`).
3. `src/assets/scripts/makefile/run-domain-pipeline.sh`: legg
   `--no-print-directory` til kvart `$MAKE`-kall (både `run_bg`-kalla i
   fase 1/2 og det avsluttande fase 3-kallet).
4. Verifiser: køyr `LOGLVL=DEBUG make domain-samt` (eller eit anna lite
   domene) lokalt og stadfest at (a) `[DEBUG] <generator> ... for schemas:
   ...`-linjer dukkar opp for dei batcha generatorane, og (b) ingen
   `Entering/Leaving directory`-linjer finst i output.

## Handlingsliste

- [x] Steg 1: export LOGLVL
- [x] Steg 2: forward LOGLVL/CLR_STEP/CLR_RST i LINKML_RUN/PYTHON_RUN
- [x] Steg 3: --no-print-directory i run-domain-pipeline.sh
- [x] Steg 4: verifiser med LOGLVL=DEBUG make domain-samt

## Utført

Verifisert med `LOGLVL=DEBUG make domain-samt` lokalt: `[DEBUG] <generator>
... for schemas: ...`-linjer dukkar no opp for alle batcha generatorar
(merge, json-schema, owl, jsonld-context, shacl, rdf, python, proto,
plantuml, doc, erdiagram), og `grep -c "Entering directory\|Leaving
directory"` mot full logg gav 0 treff.

- `make/00-settings.mk`: `export LOGLVL` lagt til saman med dei andre
  eksporterte logg-/fargevariablane
- `make/01-containers.mk`: `-e LOGLVL -e CLR_STEP -e CLR_RST` lagt til
  `LINKML_RUN` og `PYTHON_RUN`
- `src/assets/scripts/makefile/run-domain-pipeline.sh`: `--no-print-directory`
  lagt til alle ni `$MAKE`-kall (fase 1, fase 2, fase 3)
