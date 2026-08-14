# Paralleliser Fase A i tests/test_make.sh (reduser veggklokketid for make test)

## Bakgrunn

Brukaren opplever at `make test` tek lang tid, og bad om ei evaluering av
tiltak for å redusere veggklokketida, med resultatet skrive til spec.

Ein full, rein `make test`-køyring (35 skjema, ingen sesjons-kontaminering,
same maskin som resten av denne økta — **14 CPU-kjernar tilgjengelege**,
`nproc`) vart tidsmålt frå den ferdigskrivne loggfila
(`tests/testlogs/test_make_20260814_153451.log`, tidsstempla per Fase A-steg).
Total køyretid: **~14 minutt** (script-start 15:34:51 → siste loggoppføring
15:48:57).

## Funn — kvantifisert tidsbruk per Fase A-steg

`run_phase_a_step()` sitt `$(date)`-tidsstempel vert skrive **etter** at
`make "$target" ...` har fullført, så differansen mellom to påfølgjande
steg-tidsstempel er varigheita til det **andre** steget. Utrekna frå loggen:

| Steg | Varigheit | Merknad |
|---|---|---|
| `validate` | ~19s | (inkl. tid brukt av `copy-artifacts-click-href`/`run_json_schema_tests` før Fase A) |
| `gen-jsonld-context` | 10s | |
| `gen-python` | 12s | |
| `gen-jsonschema` | 11s | |
| `gen-rdf` | **98s** | 34 skjema × 1,1–5,7s kvar — reint CPU-bunde per-skjema-arbeid, ingen kontainar-overhead att (alt batcha) |
| `gen-erdiagram` | 24s | |
| `gen-docs` | **345s (5m45s)** | **Klårt største enkeltsteg.** 34 skjema × 3,5–16,1s kvar (`DocGenerator` gjer vesentleg meir arbeid per skjema enn dei andre generatorane) |
| `gen-shacl` | 14s | |
| `gen-owl` | 20s | |
| `gen-proto` | 9s | |
| `gen-plantuml` | 41s | |
| `linkml-lint` | 20s | |
| `mcp-validate-instance` | 1s | |
| `convert-rdf` | 34s | |
| `roundtrip-json` | **80s** | |
| `roundtrip-ttl` | 50s | |
| `linkml-validate` | 19s | |
| **Sum Fase A** | **~788s (13m8s)** | **~93 % av total køyretid** |

Fase B (parallelle per-skjema-testar, køyrer etter Fase A) tek dei
attverande ~58s — han er alt rask, sidan han mest re-les filer/loggar Fase A
alt skreiv (`phase_a_check()` grep-ar ei loggfil, ingen ny genereringsjobb).
**Optimaliseringspotensialet ligg nesten utelukkande i Fase A.**

## Rotårsak: Fase A køyrer stega i **sekvens**, sjølv om dei er uavhengige

`run_phase_a()` (`tests/test_make.sh:523-540`) kallar kvart steg
(`run_phase_a_step`, `run_phase_a_lint`, `run_phase_a_mcp_instance`,
`run_phase_a_convert_rdf`, `run_phase_a_roundtrip_json`,
`run_phase_a_roundtrip_ttl`, `run_phase_a_linkml_validate`) **synkront, eitt
om gongen**. Ingen av desse stega les output frå eit **anna** steg i lista —
kvart steg tek berre kjeldeskjemaet (og for konverteringsstega, eksempelfila)
som input og produserer sin eigen artefakttype. Dei kunne difor i prinsippet
alle køyre samstundes.

**Dette er nøyaktig det same mønsteret `run-domain-pipeline.sh` alt løyste**
for den **ekte** genereringspipelinen (`make domain-<domene>`, brukt av
`generate.yml` i CI): der køyrer `gen-jsonld-context`, `gen-shacl`,
`gen-python`, `gen-jsonschema`, `gen-owl`, `gen-rdf`, `gen-proto`,
`gen-graphql`, `gen-linkml-convert`, `gen-docs` og `gen-plantuml` **alle
samstundes** i «Fase 1» via eit enkelt `run_bg`/PID-array/`wait`-mønster
(sjå `src/assets/scripts/makefile/run-domain-pipeline.sh:39-43` for
`run_bg()`-definisjonen, `:61-72` for sjølve Fase 1-oppstarten), med berre
`gen-xsd`/`gen-openapi`/`gen-asyncapi` utsett til ei eiga «Fase 2» sidan dei
faktisk **treng** `gen-jsonschema` sitt output. `tests/test_make.sh` sin
`run_phase_a()` har **ingen** slik avhengigheit mellom stega i det heile —
strukturen er difor enklare enn `run-domain-pipeline.sh` (éi bølgje held,
ingen «Fase 2» naudsynt) — men bruker likevel ikkje parallellisering.

Dette er truleg eit hol som oppstod fordi `test_make.sh` sin Fase A-struktur
vart bygd opp gradvis (batching av éin og éin kommandotype over fleire
spesifikasjonar, jf. `specs/done/effektiviser-generate-workflow-koyretid.md`
Tiltak 1-4) utan å samstundes innføre same fase-parallellisering
`run-domain-pipeline.sh` fekk i eiga oppfølging.

## Estimert gevinst

Dersom alle 17 Fase A-steg køyrer samstundes (éi bølgje, ingen
inter-steg-avhengigheit), avgrensar total Fase A-tid seg til det **lengste
enkeltsteget** — `gen-docs` på 345s — i staden for **summen** (788s).
Grovt overslag: **~788s → ~350-400s** for Fase A (medrekna noko
kontensjons-slark, sjå «Risiko» under), dvs. **total `make test`-tid frå
~14 minutt til ~6-7 minutt** — over 50 % reduksjon, utan å endre noko
generatorlogikk.

Eit sekundært, uavhengig tiltak (sjå «Tiltak, del 2») kan redusere sjølve
`gen-docs`-taket (345s) ytterlegare, og dermed presse total-tida enda lågare.

## Tiltak

### Del 1 — parallelliser Fase A-stega (lågrisiko, gjenbruk eksisterande mønster)

| # | Tiltak |
|---|---|
| 1 | Skriv om `run_phase_a()` til å starte alle 17 delfunksjonane samstundes via same `run_bg`/PID-array/`wait`-mønster som `run-domain-pipeline.sh:39-43` alt har verifisert i produksjon, i staden for sekvensielle kall |
| 2 | **Handter `PHASE_A_LOG`-fallgruva:** `run_phase_a_step()` (og systerfunksjonane) skriv i dag til den globale `PHASE_A_LOG[$key]`-arrayen **synkront i hovudskalet**. Ein bash-bakgrunnsjobb (`( ... ) &` eller `funksjon &`) forkar eit underskal — variabeltilordningar der **går tapt** for foreldreskalet når jobben er ferdig. `phase_a_check()` (kalla frå Fase B) les `PHASE_A_LOG[$key]` for å finne loggfila si sti, så denne koplinga må overleve parallelliseringa. Løysing: bytt frå `mktemp`-genererte, tilfeldig namngjevne loggfiler til ein **fast, føreseieleg stinamn-konvensjon** per nøkkel (t.d. `$LOGDIR/phase_a_<key>.log`), slik at `phase_a_check()` kan konstruere stien direkte i staden for å slå henne opp i eit array som ikkje overlever backgrounding |
| 3 | Same handtering for `PHASE_A_MCP_OUTDIR` (brukt av `mcp_instance_job()`/tilsvarande Fase B-oppslag for `mcp-validate-instance`, jf. `tests/test_make.sh:356-357`) — same fallgruve, same løysing (fast katalognamn) |
| 4 | Verifiser at `FAILED`-oppsummeringslogikken (om nokon finst i denne fila sin variant av mønsteret) korrekt samlar feil frå alle parallelle jobbar via `wait`-returkodar, same som `run-domain-pipeline.sh` sin `wait_job()` |
| 5 | Køyr full `make test` og samanlikn resultatlista (`##RESULT:OK`/`##RESULT:FAIL`-linjene) byte-for-byte mot ein referansekøyring med uendra (sekvensiell) kode — same sett av OK/FEIL, berre annan rekkjefølgje/tidsbruk er akseptabelt |
| 6 | Mål ny total veggklokketid, samanlikn mot ~14 minutt-referansen i denne specen |

### Del 2 — paralleliser per-skjema-arbeid i dei tyngste batch-skripta (valfritt, høgare innsats)

`gen-docs` (345s) og `gen-rdf` (98s) sitt indre `for s in enabled: ...`-lykke
i `batch-generate.py` er **sekvensiell, éin-tråda Python** — kvart skjema sitt
`DocGenerator`/`RDFGenerator`-arbeid (3,5-16s for docs, 1-6s for rdf) køyrer
etter kvarandre, sjølv om maskina har 14 kjernar ledige.

| # | Tiltak |
|---|---|
| 7 | Undersøk om LinkML sine generator-klassar (`DocGenerator`, `RDFGenerator` m.fl.) er trygge å instansiere/køyre i separate prosessar samstundes (venteleg ja — kvar `run_click()`-kall byggjer eigen, uavhengig `SchemaView`/generator-instans i dag alt; ingen delt mutable global tilstand identifisert ved lesing av `batch-generate.py`, men bør stadfestast empirisk før implementering) |
| 8 | Dersom trygt: byt `batch-generate.py` sin sekvensielle `for s in enabled:`-lykke til ein `concurrent.futures.ProcessPoolExecutor` (t.d. 6-8 workers — kvar prosess betaler `linkml`-importskatten ein gong, så for mange workers reduserer nettogevinsten; 6-8 er venta nær det empiriske metningspunktet gjeve dei målte per-skjema-tidene) for generatorar med **mange nok** skjema til at det lønar seg (`gen-docs`, `gen-rdf` — dei to klårt tyngste; ikkje naudsynt for steg under ~30s totalt) |
| 9 | Same vurdering for `batch-convert.py` — MERK at roundtrip-jobbar for **same** skjema har ei ordna avhengigheitskjede (a.json → b.yaml → c.json) som må haldast sekvensiell; berre parallellisering **på tvers av** skjema (ikkje internt i eitt skjema sin jobbsekvens) er trygt, jf. scriptet sin eigen dokumenterte føresetnad («Jobbar for ULIKE skjema kan stå i vilkårleg rekkjefølgje seg imellom») |
| 10 | Verifiser byte-identisk output (generert `.md`/`.ttl`/JSON-innhald) mot sekvensiell køyring for eit representativt utval skjema, sidan parallell prosessering kan endre rekkjefølgje på ikkje-deterministisk generert innhald (jf. den alt kjende blanknode-/eigenskapsrekkjefølgje-ikkje-determinismen nemnd i `batch-generate.py` sin eigen toppkommentar — stadfest at dette **ikkje** vert verre av parallellisering) |

## Risiko

- **CPU-/IO-kontensjon:** 17 samstundes `podman run`-kontainarar (Del 1) er meir enn dei 11 `run-domain-pipeline.sh` alt køyrer samstundes i produksjon, men same storleiksorden — ikkje eit prinsipielt nytt risikonivå, berre noko som bør målast empirisk (om veggklokketida IKKJE fell tilnærma som estimert, er kontensjon den mest sannsynlege forklaringa, og talet på samstundes jobbar bør då avgrensast, t.d. via ein enkel semafor/batch-i-grupper-mekanisme i staden for éi bølgje)
- **`PHASE_A_LOG`/`PHASE_A_MCP_OUTDIR`-fallgruva** (Del 1, tiltak 2-3) er ein reell korrektheitsrisiko dersom han ikkje handterast — ei naiv `run_bg`-omskriving utan denne fiksen ville få `phase_a_check()` til å alltid returnere "Fase A køyrde ikkje" (linje 557: `[ -n "$logfile" ] || return 0`), som **stille** ville få alle Fase B-testar til å rapportere OK utan faktisk å ha sjekka noko — ei alvorleg, stille regresjon dersom han ikkje er med i implementeringa
- **Del 2** er høgare innsats/risiko enn Del 1 og bør handterast som eige, seinare steg — ikkje ein føresetnad for å hauste Del 1 sin gevinst

## Referanse

- `src/assets/scripts/makefile/run-domain-pipeline.sh` — det etablerte, alt verifiserte `run_bg`/PID-array/`wait`-mønsteret Del 1 skal gjenbruke
- `specs/done/effektiviser-generate-workflow-koyretid.md` — den opphavlege batchinga (kontainar-per-skjema → éin delt kontainar) som fjerna oppstart-/import-overhead; denne specen tek NESTE steg (parallellisere DEN batcha eininga)
- `specs/done/evaluer-parallel-flag-etter-batching.md` — konkluderte at det **eksterne** `PARALLEL=N`/`xargs -P`-mønsteret ikkje lenger trengst etter batching; gjeld IKKJE spørsmålet denne specen reiser (intern fase-/prosess-parallellisering av den no batcha eininga er eit anna mekanisme, ikkje N separate kontainarar)
- `tests/testlogs/test_make_20260814_153451.log` — kjeldedata for tidsmålingane over

## Utført

### Del 1 — gjennomført og verifisert

Tiltak 1-6 alle gjennomførte i `tests/test_make.sh`:

1. `run_phase_a()` skriv no om til å starte alle 17 delfunksjonane samstundes
   (`&` + eit lokalt `PHASE_A_PIDS`-array, same idiom som `SCHEMA_PIDS`
   lenger opp i same fil), med ei sekvensiell `wait "$pid" || true`-løkke
   til slutt.
2. **`PHASE_A_LOG`-fallgruva løyst** ved å fjerne heile
   `declare -A PHASE_A_LOG`-mekanismen: loggfilnamn er no faste og
   føreseielege (`phase_a_logfile()`-hjelpefunksjon, `$LOGDIR/phase_a_<key>.log`)
   i staden for `mktemp`-genererte. `phase_a_check()` konstruerer stien
   direkte og sjekkar `[ -f "$logfile" ]` (fil finst = Fase A køyrde) i
   staden for å slå opp i eit array som ikkje overlever
   underskal-backgrounding.
3. Same handtering for `mcp-validate-instance`: `PHASE_A_MCP_OUTDIR`
   (tidlegare `mktemp -d`) er no ein fast katalog
   (`phase_a_mcp_outdir()` → `$LOGDIR/phase_a_mcp`), og
   `PHASE_A_MCP_INDEX` (schema→jobb-indeks, tidlegare eit bash-array) er no
   ei skriven indeksfil (`phase_a_mcp_indexfile()` →
   `$LOGDIR/phase_a_mcp_index.tsv`, `schema<TAB>idx` per linje).
   `phase_a_mcp_check()` slår opp indeksen via `awk` mot denne fila i
   staden for eit array-oppslag.
   - **Ekstra korrektheitsfiks oppdaga under implementering** (ikkje
     eksplisitt i det opphavlege tiltaket, men naudsynt): sidan loggfil-/
     indeksfil-namna no er **faste** (ikkje lenger `mktemp`-unike per
     skript-køyring), måtte `run_phase_a()` få eit oppryddingssteg FØR
     stega startar (`rm -f "$LOGDIR"/phase_a_*.log`, tilsvarande for
     indeksfila/mcp-katalogen) — elles kunne ei fil frå eit **tidlegare**
     skript-kall (med ein annan `TEST_FILTER`) feilaktig få
     `phase_a_check()` til å tru eit hoppa-over steg faktisk køyrde.
     Verifisert direkte: køyrde `TEST_FILTER=roundtrip-ttl` (samt-bu,
     stadfesta FEIL som venta), deretter `TEST_FILTER=gen-rdf` på same
     skjema i same arbeidstre — stadfesta at det andre kallet **ikkje**
     vart påverka av det første sin attverande `roundtrip-ttl`-loggfil.
4. `wait "$pid" || true`-mønsteret handterer alle 17 parallelle jobbar;
   ingen av `run_phase_a_*`-funksjonane returnerer meiningsfulle feilkodar
   i utgangspunktet (feil vert oppdaga av Fase B via loggfil-innhald via
   `phase_a_check()`, ikkje via prosess-exit-kode) — stadfesta ved lesing,
   ingen endring naudsynt utover å ikkje la `wait` sin returkode trigge
   `set -e`.
5. **Full `make test`-køyring samanlikna mot referansen:** identisk
   resultatsett — **591 OK, 5 feil** både før og etter, same fem feil
   (`fint-administrasjon`, `fint-okonomi`, `fint-personvern`,
   `fint-utdanning`, `samt-bu` — alle kjend, pre-eksisterande BUG-3, sjå
   `bugs/mappingerror-rdflib-roundtrip.md`). Ingen nye feil, ingen
   stille-forsvunne feil.
6. **Ny veggklokketid: 4m43s** (`time make test`), ned frå ~14 minutt
   referanse — **~66 % reduksjon**, betre enn det forsiktige
   spec-overslaget på ~6-7 minutt. `user`+`sys`-tid (48s+55s ≈ 1m43s) er
   vesentleg lågare enn `real`-tida, som stadfestar at mesteparten av
   tidsbruken er I/O-/nettverks-/podman-overhead-bunden — nett den typen
   arbeid som parallelliserer godt utan reell CPU-kontensjon (ingen teikn
   til at kontensjons-risikoen nemnd i «Risiko» slo inn i praksis).

Ingen regresjon stadfesta både for enkeltskjema-køyring
(`register-over-aksjeeiere`, 18/18 OK) og full køyring.

### Del 2 — gjennomført og verifisert (tiltak 7-8, batch-generate.py)

7. **Trygt å parallellisere, stadfesta:** `run_click()`-kalla byggjer alt
   eigne, uavhengige generator-/`SchemaView`-instansar per skjema, ingen
   delt mutable global tilstand identifisert. Verifisert empirisk (steg 10
   under) — ingen pickling- eller korrektheitsfeil oppdaga.
8. `batch-generate.py` sin sekvensielle `for s in enabled:`-lykke er no
   splitta i tre delar:
   - `_build_argv()` — reint uttrekk av argv-oppbygginga (uendra logikk).
   - `_generate_one(task)` — ny, topplevel worker-funksjon (pickle-bar) som
     gjer sjølve generatorkallet for **eitt** skjema. Referer Click Command-
     objektet via ein modul-global (`_CLI_CMD`, sett i `main()` **før**
     poolen vert oppretta) i staden for å sende det gjennom
     `pool.map()` — unngår å måtte pickle sjølve Command-objektet, som ikkje
     er trivielt pickle-bart. Fungerer fordi Linux sin standard
     multiprocessing-startmetode er `fork`: worker-prosessar er ein
     copy-on-write-kopi av foreldreprosessen sitt minne på forke-tidspunktet,
     så `_CLI_CMD` er alt sett i kvar worker utan eksplisitt overføring.
   - `main()` grenar no på det nye `GeneratorSpec.parallel`-feltet (sett
     `True` berre for `doc` og `rdf`, dei to klårt tyngste, som spec
     Tiltak 8 føreslo): dersom sett og fleire enn 1 skjema, køyrer
     `ProcessPoolExecutor(max_workers=<BATCH_GENERATE_WORKERS env, standard 6>)`;
     elles uendra sekvensiell sti. `pool.map()` bevarer skjema-rekkjefølgja
     i loggutskrifta uavhengig av fullføringsrekkjefølgje.
   - Tiltak 9 (batch-convert.py) vart **ikkje** gjort — brukaren bad
     spesifikt om Del 2 sine tiltak 7-8-omfang (`batch-generate.py`); same
     vurdering som spec-teksten (kryss-skjema-parallellisering, halde
     jobbsekvensen INNI eitt skjema sekvensiell) kan gjerast seinare dersom
     ønskt, då `batch-convert.py` sine steg (roundtrip-json/-ttl,
     convert-rdf) ikkje lenger er blant dei klårt tyngste etter Del 1
     (roundtrip-json var 80s, roundtrip-ttl 50s — mindre enn `gen-docs`/
     `gen-rdf` sine respektive 189s/105s per-skjema-summerte tider).

**Tiltak 10 — verifisering (`doc` og `rdf`, isolert, reine mellombelse
GEN_DIR-katalogar for å unngå kontaminering frå tidlegare testkøyringar i
same arbeidstre):**

- **`doc`:** sekvensiell (git HEAD-versjon) vs. parallell (ny kode) køyrt
  mot identisk skjemasett (`register-over-aksjeeiere`,
  `enhetsregisteret-bvrinn`, `referansemodell`) — **byte-for-byte identisk**
  output (`diff -rq` — ingen skilnad, inkl. `_doc_post()` sin
  Container-linje-fjerning).
- **`rdf`:** same samanlikning synte skilnadar i dei genererte `.ttl`-filene
  — men ein **kontrollsjekk** (git HEAD-koden køyrd **to gonger** mot same
  skjema, ingen parallellisering involvert i det heile) synte **identisk
  mønster av skilnadar**, inkludert identisk `len(graph)` men
  `isomorphic=False` via `rdflib.Graph.isomorphic()`. Dette stadfestar at
  skilnadane er akkurat den kjende, **pre-eksisterande**
  non-determinismen `batch-generate.py` sin eigen toppkommentar alt
  dokumenterer (blanknode-/eigenskapsrekkjefølgje via hash-baserte
  set/dict internt i linkml/rdflib) — **uendra av parallelliseringa**, ikkje
  ei ny regresjon. `test_gen_rdf()` sin eksisterande `assert_rdf_valid`
  (syntaktisk gyldigheit, ikkje eksakt likskap) var alt den korrekte
  toleransen for dette, uendra av Del 2.

**Målt gevinst — full `make test`:** **591 OK, 5 feil** (identisk
resultatsett som etter Del 1 og som før Del 1 — same fem kjende,
pre-eksisterande BUG-3-feil). Veggklokketid **2m57,9s**, ned frå 4m43s
(Del 1 åleine) — Del 2 gav ytterlegare **~37 % reduksjon** oppå Del 1 sin
gevinst. Total reduksjon frå den opphavlege ~14-minutt-referansen:
**~79 %**.

**Ekstra måling — 10 workers i staden for standard 6:** `make/01-containers.mk`
sin `LINKML_RUN` fekk `-e BATCH_GENERATE_WORKERS` lagt til (var ikkje
vidareført til kontaineren i det heile før dette — same mønster som
`LOGLVL`/`CLR_*`, `os.environ.get(..., "6")`-standarden i
`batch-generate.py` uendra). Full `make test` med
`BATCH_GENERATE_WORKERS=10` eksportert: **591 OK, 5 feil** (uendra
resultatsett), veggklokketid **2m59,2s** — **ingen måleleg skilnad** frå
6 workers (2m57,9s, innanfor normal køyring-til-køyring-støy). Stadfestar
tiltak 8 sitt overslag: 6 workers ligg alt nær metningspunktet for denne
maskina/skjemamengda — fleire workers gjev ikkje ytterlegare gevinst.
Standardverdien (6) er difor behalden uendra; `BATCH_GENERATE_WORKERS` er
no eksponert som miljøvariabel for framtidig ombruk/justering ved behov
(t.d. på maskiner med vesentleg fleire/færre kjernar).
