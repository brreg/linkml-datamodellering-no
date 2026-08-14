# Splitt Fase A-batchane for gen-docs, gen-plantuml og roundtrip-json i to parallelle halvdelar

## Bakgrunn

Brukaren ønskjer at Fase A-batchane for `gen-docs`, `gen-plantuml` og
`roundtrip-json` (dei tre tyngste stega, ~85-135s kvar i seinaste
målingar) vert delt i to like store halvdelar som køyrer parallelt med
kvarandre, i staden for éin kontainar som handsamar alle 35 skjema.

## Undersøking: kor mykje intern parallellitet finst alt?

Sjekka `REGISTRY` i `batch-generate.py` og dei tre steg-macroane i
`make/10-generator-macros.mk`:

| Steg | Intern parallellitet i dag |
|---|---|
| `gen-docs` (`doc`-generator) | `parallel=True` — brukar alt `ProcessPoolExecutor` (`BATCH_GENERATE_WORKERS`, standard 6). Steget har OGSÅ ein FØRSTE, ikkje-parallell del (`docgen-examples` via `batch-generate-instances.py`) |
| `gen-plantuml` (`plantuml`-generator) | **Ingen** — `parallel` er IKKJE sett for `plantuml`-nøkkelen i `REGISTRY`, prosesserer skjema sekvensielt. To ekstra sekvensielle steg (`plantuml-filter`, SVG-rendering via `batch-render-plantuml.sh`) |
| `roundtrip-json` (`batch-convert.py`) | **Ingen** — skriptet sin eigen toppkommentar seier eksplisitt "prosesserer jobbane strengt sekvensielt (éin prosess, ingen parallellitet internt)" |

Tidlegare i økta vart `BATCH_GENERATE_WORKERS=10` testa mot standard 6
utan målbar gevinst (maskina si praktiske grense for SAMSTUNDES arbeid
verka nådd rundt 6). Dette betyr at ei todeling av `gen-docs` (som alt
har 6 interne workers) potensielt gjev MINDRE gevinst enn for
`gen-plantuml`/`roundtrip-json` (som har NULL intern parallellitet i
dag) — men vert likevel implementert som bede om, og målt ærleg
etterpå.

## Tiltak

Same idé i alle tre, ulik mekanikk avhengig av korleis steget byggjer
arbeidet sitt:

| # | Tiltak | Fil |
|---|---|---|
| 1 | Ny `run_phase_a_step_split2()` — som `run_phase_a_step()`, men deler `SCHEMAS` i to omtrent like store halvdelar (`SCHEMAS[@]:0:mid` / `SCHEMAS[@]:mid`) og køyrer `make "$target" SCHEMAS=<halvdel>` TO GONGER PARALLELT (kvar sin eigen bakgrunnsprosess/podman-kontainar-kjede), slår saman dei to loggfilene til éi FØR dei skriv til `$LOG`/metafil — held `phase_a_logfile`/`phase_a_metafile`-grensesnittet UENDRA, så `phase_a_check()`/`print_phase_a_summary()` treng ingen endring | `tests/test_make.sh` |
| 2 | Bytt `run_phase_a_step docs ...` og `run_phase_a_step plantuml ...` til `run_phase_a_step_split2` i `run_phase_a()` | `tests/test_make.sh` |
| 3 | Ny `_run_phase_a_convert_batch_split2()` — som `_run_phase_a_convert_batch()`, men deler jobbrader-fila i to halvdelar ETTER TAL UNIKE SKJEMA (ikkje tal jobbrader) via `awk`, held kvart skjema sine jobbrader samla og i uendra rekkjefølgje i SAME halvdel (kritisk — jobbrader for same skjema har skrive-før-les-avhengigheiter seg imellom, jf. `batch-convert.py` sin toppkommentar), køyrer `batch-convert.py` TO GONGER PARALLELT, slår saman loggfilene | `tests/test_make.sh` |
| 4 | Bytt siste linja i `run_phase_a_roundtrip_json()` frå `_run_phase_a_convert_batch roundtrip_json ...` til `_run_phase_a_convert_batch_split2 roundtrip_json ...`. `run_phase_a_convert_rdf()`/`run_phase_a_roundtrip_ttl()` er UENDRA (brukar framleis éin batch) — brukaren bad berre om roundtrip-json | `tests/test_make.sh` |
| 5 | `bash -n tests/test_make.sh` | — |
| 6 | Verifiser: full `make test` — **591 OK, 5 feil** uendra, mål ny tid for dei tre stega mot referansen (gen-docs ~109s, gen-plantuml ~85s, roundtrip-json ~82-134s), rapporter ærleg dersom éin eller fleire av dei IKKJE vert raskare (t.d. venta for gen-docs, sidan han alt har intern parallellitet) | — |

## Utført

Alle 6 tiltak gjennomførte og verifiserte:

1. Ny `run_phase_a_step_split2()` — deler `SCHEMAS` i to halvdelar,
   køyrer `make "$target" SCHEMAS=<halvdel>` to gonger parallelt, slår
   saman loggfilene til same `$key` som før splitting.
2. `run_phase_a()`: `docs`/`plantuml` bytt frå `run_phase_a_step` til
   `run_phase_a_step_split2`.
3. Ny `_run_phase_a_convert_batch_split2()` — deler `jobs_tsv` med `awk`
   etter TAL UNIKE SKJEMA (kolonne 1), held kvart skjema sine jobbrader
   samla og i uendra rekkjefølgje i same halvdel, køyrer
   `batch-convert.py` to gonger parallelt.
4. `run_phase_a_roundtrip_json()`: siste linje bytt til
   `_run_phase_a_convert_batch_split2`. `convert_rdf`/`roundtrip_ttl` er
   UENDRA (framleis éin batch), som bede om.
5. `bash -n tests/test_make.sh` — OK. Splitting-logikken i `awk`
   verifisert isolert med ei handbygd 3-skjema jobbliste (2 skjema →
   halvdel A, 1 skjema → halvdel B, radrekkjefølgje innanfor kvart
   skjema uendra).
6. Full `make test`: **591 OK, 5 feil** — identisk med referansen, ingen
   regresjon. Målt mot NÆRAST-i-tid FØR-køyring (same straumtilstand,
   difor gyldig samanlikning):

   | Steg | Før | Etter | Endring |
   |---|---|---|---|
   | `roundtrip-json` | 83.67s | 65.67s | **~21,5 % raskare** |
   | `gen-docs` | 109.86s | 99.15s | ~9,7 % raskare |
   | `gen-plantuml` | 87.07s | 85.68s | ~1,6 % raskare (neglisjerbart) |
   | **Total tidsbruk** | 131.13s | 120.48s | ~8 % raskare |

   Resultatet stadfestar undersøkinga sin spådom: `roundtrip-json`
   (null intern parallellitet FØR dette tiltaket) fekk den klart
   største gevinsten, `gen-docs` (hadde alt `ProcessPoolExecutor`)
   moderat, og `gen-plantuml` nesten ingen — sannsynleg fordi
   PlantUML-rendering-steget (`batch-render-plantuml.sh`, JVM-basert)
   har ein FAST oppstartskostnad som no vert betalt TO GONGER (éin per
   halvdel) i staden for éin, som deler av gevinsten frå halvert
   skjema-arbeidsmengd. Ikkje undersøkt vidare i denne økta — rapportert
   ærleg, ingen tiltak att for `gen-plantuml` spesifikt.

## Tillegg: gen-plantuml-splitting reversert, BATCH_GENERATE_WORKERS-standard heva til 8

Gitt at `gen-plantuml`-splittinga synte neglisjerbar gevinst (~1,6 %,
sjå over), og eit oppfølgjande eksperiment med
`BATCH_GENERATE_WORKERS=12` (mot standard 6) heller ikkje synte målbar
gevinst utover normal køyring-til-køyring-varians (591 OK/5 feil
uendra, total tid 118.00s mot 120.48s — same mønster som det
TIDLEGARE `WORKERS=10`-eksperimentet i
`specs/done/paralleliser-fase-a-test-make.md`), vart to justeringar
gjorde saman:

1. `run_phase_a()`: `gen-plantuml` bytt TILBAKE frå
   `run_phase_a_step_split2` til vanleg `run_phase_a_step` (splittinga
   gav ikkje nok att for kompleksiteten han la til).
2. `batch-generate.py`: standardverdien for `BATCH_GENERATE_WORKERS`
   heva frå `6` til `8` (framleis overstyrbar via miljøvariabelen).

**Verifisering:** Full `make test` — **591 OK, 5 feil**, ingen
regresjon. Total tidsbruk **115.71s** — best målte totaltid i heile
denne optimaliserings-rekkja (mot 120.48s med splitta gen-plantuml +
standard 6 workers, og 118.00s med splitta gen-plantuml + 12 workers).
`gen-docs` (framleis splitta i to): 94.49s. `gen-plantuml` (usplitta):
88.31s, om lag som før splitting-forsøket (87.07s), som venta sidan
splittinga uansett ikkje gav noko å miste.
