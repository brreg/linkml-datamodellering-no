# Gjer gen-docs raskare i Fase B

## Bakgrunn

`→ Fase B: gen-docs (35 sjekkar) ... (221.60s) OK: 35 ERROR: 0` — klart
tregast av alle Fase B-sjekkane (dei andre ligg på 1-16s summert over 35
skjema).

`test_gen_docs()` (`tests/test_make.sh`) sjekkar KVART `.md`-fil
`gen-docs` produserer, éin for éin, i ein bash-while-løkke
(`find` + `[ -s ]` + `grep -q '^#'`). `gen-docs` produserer 62-225
`.md`-filer PER SKJEMA (éin per klasse/slot/enum/type). Målt direkte på
eitt skjema (`enhetsregisteret-bvrinn`, 225 filer): **4,8s totalt**, men
berre **~1,15s var CPU-tid** (`user`+`sys`) — resten (~3,65s) var
I/O-VENTETID. Repoet ligg under WSL2 sin Windows-filsystem-bru
(`/mnt/c`), som har målbar per-fil-overhead for MANGE SMÅ sekvensielle
filoperasjonar — kvart av dei 225 `grep`-kalla (prosess-spawn) OG kvar
fil-opning krev å krysse denne bruo. Summert over 35 skjema (parallelt
skjema-for-skjema, men SEKVENSIELT fil-for-fil INNI kvart skjema) gjev
dette dei observerte ~221s.

## Tiltak

Batch sjekken til EITT nytt Fase A-steg, same mønster som
`rdf-validity` (`specs/done/optimaliser-make-test-basert-pa-
logginnsikt.md`, Tiltak 1): éin `podman run` for ALLE skjema, i staden
for éin bash-while-løkke PER skjema. Nytt her (utover det etablerte
mønsteret): sjekk filene PARALLELT via `ThreadPoolExecutor` INNI
batch-skriptet — arbeidet er I/O-bunde (fil-opning), så Python sin GIL
vert sloppen under kvar `read()`, og mange samstundes opningar overlappar
VENTETIDA i staden for å stable ho sekvensielt (adresserer den ~3,65s
I/O-ventedelen direkte, ikkje berre kontainar-oppstart-skatten dei andre
batch-skripta amortiserer).

| # | Tiltak | Fil |
|---|---|---|
| 1 | Ny `src/assets/scripts/makefile/batch-docs-validate.py` — les jobs-tsv (`schema<TAB>docsdir`), sjekkar kvart skjema sin docs-katalog (finst, har minst éi `.md`-fil, alle `.md`-filer ikkje-tomme og har `#`-overskrift) — fil-sjekkane INNI eit skjema køyrer via `ThreadPoolExecutor`. Skriv `::error file=<schema>::` (maks éin per skjema, fyrste problemet funne — same granularitet som opphavleg) | ny fil |
| 2 | Ny `run_phase_a_docs_validity()` i `tests/test_make.sh` — bygg jobbliste (skjema, docsdir) for alle `SCHEMAS` (respekter `TEST_FILTER` på `gen-docs`-prefikset), køyr batch-skriptet i `PYTHON_IMAGE`-kontainaren (reint stdlib-arbeid, treng ikkje linkml). Køyr sekvensielt ETTER hovud-wait-løkka i `run_phase_a()` (les `gen-docs` sitt output), same plassering som `run_phase_a_rdf_validity()` | `tests/test_make.sh` |
| 3 | `test_gen_docs()`: fjern heile bash-while-løkka, byt til `phase_a_check docs_validity "$schema"` (i tillegg til eksisterande `phase_a_check docs "$schema"`) | `tests/test_make.sh` |
| 4 | Legg `docs_validity` til `PHASE_A_KEYS` (Fase A-oppsummeringa) | `tests/test_make.sh` |
| 5 | `bash -n tests/test_make.sh`, `python3 -m py_compile batch-docs-validate.py` | — |
| 6 | Verifiser: full `make test` — **591 OK, 5 feil** uendra, `gen-docs`-linja i Fase B-oppsummeringa fell drastisk (mål ny tid), ny `docs-validity`-linje i Fase A-oppsummeringa | — |

## Utført

Alle 6 tiltak gjennomførte og verifiserte:

1. Ny `src/assets/scripts/makefile/batch-docs-validate.py` — les
   `schema<TAB>docsdir`-jobbliste, sjekkar kvart skjema sin docs-katalog
   (finst, minst éi `.md`-fil, alle `.md`-filer ikkje-tomme + har
   `#`-overskrift), fil-sjekkane INNI eit skjema køyrer via
   `ThreadPoolExecutor(max_workers=32)`. Skriv `::error file=<schema>::`
   for feil.
2. Ny `run_phase_a_docs_validity()` i `tests/test_make.sh` — bygg
   jobbliste for alle `SCHEMAS` (respekterer `TEST_FILTER`), køyrer i
   `PYTHON_IMAGE` (ny konstant, `localhost/python-pytest:latest` — treng
   ikkje linkml-importar). Køyrer i ei EIGA bakgrunnsgruppe saman med
   `run_phase_a_rdf_validity()` (uavhengige av kvarandre, parallelle seg
   imellom, begge sekvensielle etter hovud-`PHASE_A_PIDS`-wait-løkka).
3. `test_gen_docs()` forenkla frå ei 11-linjers bash-while-løkke til to
   `phase_a_check`-kall (`docs` + `docs_validity`). Call site i
   `run_schema_tests()` oppdatert (`docsdir`-parameteren er ikkje
   lenger nødvendig).
4. `docs_validity` lagt til `PHASE_A_KEYS`.
5. `bash -n tests/test_make.sh`, `python3 -m py_compile
   batch-docs-validate.py` — begge OK.
6. Full `make test`: **591 OK, 5 feil** — identisk med referansen, ingen
   regresjon. Resultat, langt over forventa:
   - Fase B sin `gen-docs`-linje: **221.60s → 2.39s** (~93× raskare)
   - Ny Fase A `docs-validity`-linje: **5.74s** for alle 35 skjema samla
     (batching + trådpool-parallellisering av 60-225 filer per skjema
     gjorde det som var den TREGASTE Fase B-sjekken til den NEST
     RASKASTE Fase A-sjekken)
