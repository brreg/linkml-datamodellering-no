# Ytterlegare optimalisering av make test, basert på Fase A-oppsummeringa

## Bakgrunn

Etter at Fase A-oppsummeringa (`specs/done/fase-a-oppsummering-test-make.md`)
vart innført, viser ein full køyring følgjande fordeling (35 skjema, total
tidsbruk 177.99s):

```
→ Fase A: validate (35 skjema) ... (42.61s)
→ Fase A: gen-jsonld-context (35 skjema) ... (28.53s)
→ Fase A: gen-python (35 skjema) ... (34.40s)
→ Fase A: gen-jsonschema (35 skjema) ... (29.39s)
→ Fase A: gen-rdf (35 skjema) ... (52.73s)
→ Fase A: gen-erdiagram (35 skjema) ... (59.56s)
→ Fase A: gen-docs (35 skjema) ... (130.80s)
→ Fase A: gen-shacl (35 skjema) ... (40.68s)
→ Fase A: gen-owl (35 skjema) ... (52.20s)
→ Fase A: gen-proto (35 skjema) ... (27.21s)
→ Fase A: gen-plantuml (35 skjema) ... (91.89s)
→ Fase A: linkml-lint --ignore-warnings (35 skjema) ... (57.19s)
→ Fase A: mcp-validate-instance (21 skjema) ... (41.25s)
→ Fase A: convert-rdf (13 jobb(ar)) ... (44.75s)
→ Fase A: roundtrip-json (63 jobb(ar)) ... (134.73s)   ← lengste enkeltsteg
→ Fase A: roundtrip-ttl (40 jobb(ar)) ... (96.69s)
→ Fase A: linkml-validate (31 skjema) ... (45.81s)
```

Sidan alle 17 stega køyrer parallelt, er `roundtrip-json` (134.73s) den
reelle nedre grensa for Fase A sin del av veggklokketida — resten av dei
177.99s totalt kjem frå Fase B (per-skjema-testblokkene, som må vente på at
Fase A er ferdig sidan dei les Fase A sine loggfiler via `phase_a_check()`).

To konkrete, kjeldekode-verifiserte funn peikar på reelt sløseri:

### Funn 1: `assert_rdf_valid()` spinn opp éin ny podman-kontainar PER KALL

`tests/test_make.sh:779` (`assert_rdf_valid()`) køyrer eit HEILT NYTT
`podman run`-kall (full container-oppstart + `import rdflib`) for kvar
einaste RDF-fil som skal sjekkast. Han vert kalla frå Fase B for **kvart
skjema**, opptil **4 gonger** (`test_gen_rdf`, `test_gen_shacl`,
`test_gen_owl`, `test_convert_rdf` — sjå linje 842, 870, 877, 994) — til
saman over 100 separate kontainar-oppstartar for heile testkøyringa, kvar
målt til rundt 2,5s (jf. `convert-rdf (brreg-modellkatalog)(2.51s)` i
rålogg, markant tregare enn dei andre Fase B-sjekkane som er reine
loggfil-grep og typisk tek 0.00–0.06s). Desse køyrer INNI kvart skjema sin
EIGEN sekvensielle bakgrunnsblokk (jf. `run_schema_tests()`), så eit
skjema med alle fire (`rdf`, `shacl`, `owl`, `convert-rdf`) legg opptil
~10s sekvensiell kontainar-oppstart-overhead til akkurat DEN
bakgrunnsblokka si køyretid — og den TREGASTE skjema-blokka set golvet
for Fase B sin del av veggklokketida.

### Funn 2: `batch-convert.py` cachar ikkje skjema/Python-modul på tvers av jobbrader for same skjema

Kjeldekode-verifisert (`linkml.converter.cli.cli.callback`, via
`podman run ... python3 -c "import inspect; ...inspect.getsource(...)"`):
kvart `linkml-convert`-kall gjer, HEILT UAVHENGIG av tidlegare kall i same
prosess:

```python
python_module = PythonGenerator(schema).compile_module()  # kodegenerering + exec() — INGEN caching, verifisert i linkml_runtime.utils.compile_python()
sv = SchemaView(schema)                                    # ny SchemaView, ingen caching
```

`batch-convert.py` (nytta av `convert-rdf`/`roundtrip-json`/
`roundtrip-ttl`) prosesserer jobbrader **strengt sekvensielt i éin
prosess** (allereie batcha, sjå fila sin toppkommentar), men kallar
`run_click(convert_cli, argv)` **på nytt for kvar jobbrad** — inkludert
når fleire jobbrader **på rad** deler nøyaktig same `--schema`-argument.
Dette er tilfellet for:

- `roundtrip-json`: **3 jobbrader per skjema**, same skjema (134.73s
  totalt, 63 jobbrader ÷ 3 ≈ 21 skjema)
- `roundtrip-ttl`: **4 jobbrader per skjema**, same skjema (96.69s
  totalt, 40 jobbrader ÷ 4 = 10 skjema)
- `convert-rdf`: 1 jobbrad per skjema (44.75s, 13 jobbrader) — ingen
  duplisering her, men delar same rotårsak/kode.

`PythonGenerator(schema).compile_module()` (kodegenerering frå LinkML-
skjema til Python-dataklassar via templating, deretter `compile()`+
`exec()`) er den dyraste delen av eit `linkml-convert`-kall utanom sjølve
I/O-en, og vert altså betalt **3–4 gonger per skjema** i staden for éin
gong, i dei to største Fase A-stega (samla 231.42s av 664.44s total
Fase A-arbeid).

## Tiltak

| # | Tiltak | Grunngjeving | Fil | Risiko |
|---|---|---|---|---|
| 1 | Flytt RDF-gyldigheitssjekk (`assert_rdf_valid`) frå 4 separate per-skjema Fase B-kall til ETT nytt batcha Fase A-steg (t.d. `rdf-validity`), same mønster som resten av Fase A: samle (nøkkel, filsti)-par frå `test_gen_rdf`/`test_gen_shacl`/`test_gen_owl`/`test_convert_rdf` sine output-filer i éi jobbliste, valider alle med rdflib i ÉIN podman-kontainar (`for f in files: g=Graph(); g.parse(f); assert len(g)>0`), skriv `::error file=<sti>::` for feil (same universelle konvensjon). Fase B-funksjonane byter til `phase_a_check()`-stil oppslag i staden for direkte `assert_rdf_valid`-kall. Eliminerer >100 separate kontainar-oppstartar (~2,5s kvar) frå den kritiske stien til dei tregaste skjema-blokkene i Fase B. | Same amortiserings-prinsipp som ALLE andre Fase A-steg alt brukar (linkml/rdflib-importskatt betalt éin gong, ikkje N gonger) — reint mekanisk, låg risiko, ingen endring i KVA som vert validert | `tests/test_make.sh` (ny `run_phase_a_rdf_validity()`-funksjon + endra `test_gen_rdf`/`test_gen_shacl`/`test_gen_owl`/`test_convert_rdf`) | Låg — same, alt verifiserte mønster |
| 2 | I `batch-convert.py`: grupper jobbrader per `schema`-verdi (jobbradene kjem alt i rett rekkjefølgje for avhengigheiter innanfor same skjema, jf. fila sin toppkommentar), og cache `SchemaView(schema)` + `PythonGenerator(schema).compile_module()` **éin gong per unikt skjema** i staden for éin gong per jobbrad. Krev å BYPASSE `run_click(convert_cli, ...)`-mønsteret for dette steget og i staden kalle dei underliggjande primitiva direkte (`get_loader`/`get_dumper`, `infer_root_class`, m.fl. — same type bypass som `batch-linkml-validate.py` alt gjer for `linkml.validator.validate()`, dokumentert i den fila sin toppkommentar). | Kjeldekode-verifisert: INGEN caching finst i linkml sjølv (`compile_python()` gjer rå `compile()`+`exec()` kvar gong). Råkar dei to STØRSTE Fase A-stega (134.73s + 96.69s = 231.42s), som saman dominerer total Fase A-veggklokketid. Potensielt stort utbytte (opptil 2–3× færre skjema-parsingar for roundtrip-ttl), men krev at konverteringslogikken vert reimplementert manuelt utanfor Click-laget — reell korrektheitsrisiko dersom noko av CLI-callback sin logikk (prefixhandtering, XSV-spesifikke flagg, RDF-spesifikke `schemaview`/`fmt`-args) vert gløymt. | `src/assets/scripts/makefile/batch-convert.py` | Middels — krev nøye replikering av CLI-callback-logikken; MÅ verifiserast grundig mot full regresjonskøyring før aksept |
| 3 | Verifiser tiltak 1: full `make test` — stadfest identisk resultatsett (591 OK, 5 feil), stadfest at Fase A-oppsummeringa no viser ein NY `rdf-validity`-linje, og mål ny total tidsbruk mot referansen 177.99s | — | — | — |
| 4 | Verifiser tiltak 2: full `make test` — stadfest identisk resultatsett (591 OK, 5 feil), samanlikn INNHALDET i genererte `roundtrip-json`/`roundtrip-ttl`/`convert-rdf`-artefakt byte-for-byte mot ein referansekøyring FØR endringa (ikkje berre OK/FEIL-talet — ein subtil semantikkskilnad mellom manuell reimplementasjon og CLI-callback ville elles kunne passere umerka dersom testane sjølv ikkje fangar akkurat det avviket), og mål ny tidsbruk for `roundtrip-json`/`roundtrip-ttl`/`convert-rdf`-linjene mot referansen (134.73s/96.69s/44.75s) | — | — | — |
| 5 | `bash -n tests/test_make.sh` og syntakssjekk av endra Python-script etter kvart tiltak | — | — | — |

## Prioritering

Tiltak 1 (lågare risiko, mekanisk, følgjer eit alt etablert mønster)
foreslås gjort først og verifisert isolert. Tiltak 2 (høgare potensielt
utbytte, men reell korrektheitsrisiko sidan det inneber å reimplementere
delar av `linkml-convert` sin CLI-logikk manuelt) foreslås gjort som eit
eige, seinare steg — berre etter eksplisitt godkjenning, gitt
kompleksiteten og risikoen for subtile semantikkavvik.

## Utført

Begge tiltak gjennomførte og verifiserte.

### Tiltak 1

1. Ny `src/assets/scripts/makefile/batch-rdf-validate.py` — validerer ei
   liste av filer (éin per linje) med `rdflib` i éin prosess, skriv
   `::error file=<filsti>::` for ugyldig/tom graf (same konvensjon som
   dei andre batch-skripta).
2. Ny `run_phase_a_rdf_validity()` i `tests/test_make.sh`: samlar
   `gen-rdf`/`gen-shacl`/`gen-owl`/`convert-rdf` sine output-filer (berre
   dei som faktisk finst og er ikkje-tomme, og berre dei som er omfatta
   av eventuell `TEST_FILTER`) til éi jobbliste, køyrer
   `batch-rdf-validate.py` i éin podman-kontainar. Køyrer **sekvensielt
   ETTER** hovud-`PHASE_A_PIDS`-wait-løkka i `run_phase_a()` (ikkje i
   parallell med han), sidan han les output-filer dei fire andre stega
   produserer.
3. `test_gen_rdf`/`test_gen_shacl`/`test_gen_owl`/`test_convert_rdf` byta
   frå `assert_rdf_valid "$outfile"` (eige `podman run` per kall) til
   `phase_a_check rdf_validity "$outfile"` (gjenbruker den eksisterande
   helperen uendra — han tek berre ein vilkårleg matchestreng, ikkje
   nødvendigvis eit skjema).
4. `assert_rdf_valid()`-funksjonen sletta (ingen attverande kallarar).
5. `rdf_validity` lagt til i `PHASE_A_KEYS` (Fase A-oppsummeringa).
6. `bash -n tests/test_make.sh` og `python3 -m py_compile
   batch-rdf-validate.py` — begge OK.
7. Full `make test` køyrt to gonger: **591 OK, 5 feil** begge gonger
   (identisk med referansen, ingen regresjon). Ny `rdf-validity`-linje i
   Fase A-oppsummeringa viste konsekvent `(120 fil(er)) ... (~26s) OK:
   120 ERROR: 0` — stadfestar at alle tidlegare ~100+ separate
   `assert_rdf_valid`-kontainarkall no er batcha til ÉIN.
8. **Ikkje mogleg å talfeste den forventa tidsgevinsten i denne økta**:
   brukaren merka undervegs at berbar PC gjekk over frå straumadapter
   (referansemålinga, 177.99s total) til batteridrift med lågare yting
   FØR desse to verifiseringskøyringane — alle 17 andre Fase A-steg (heilt
   uendra av dette tiltaket) synte òg omtrent dobla tid samanlikna med
   referansen, som stadfestar at auken kjem frå straum-/yting-tilstanden
   til maskina, ikkje frå koden. Strukturell korrektheit
   (591 OK/5 feil, 0 feil i rdf-validity, éin kontainar i staden for
   100+) er difor verifisert, men ei absolutt før/etter-tidsmåling må
   gjerast på nytt på straumadapter for å talfeste den faktiske
   gevinsten.

### Tiltak 2

1. `src/assets/scripts/makefile/batch-convert.py` reimplementert: kallar
   `PythonGenerator`, `SchemaView`, `get_loader`/`get_dumper`,
   `infer_root_class`, `datautils._is_rdf_format` **direkte**, i staden
   for `run_click(convert_cli, argv)`. Reimplementasjonen dekkjer BERRE
   dei kodestigane som er nåbare med den faste argv-forma
   `--schema <s> --output-format <f> --no-validate --output <o> <input>`
   (stadfesta ved full gjennomlesing av `cli.callback` sin kjeldekode via
   `inspect.getsource()` FØR reimplementasjonen vart skriven).
2. **Første forsøk (feil, retta før commit):** cacha `(python_module, sv,
   target_class)` saman per skjema. Ein manuell reproduksjon (3 skjema:
   `brreg-modellkatalog`, `novari-modellkatalog`, `fint-utdanning`, alle
   Kategori D-jobbtypar for kvart) synte ei NY feilmelding for
   `brreg-modellkatalog`/`novari-modellkatalog` sin roundtrip-ttl:
   `Modellkatalog.__init__() got an unexpected keyword argument
   'tittel_literal'` + `Inconsistent URI to class map`. Målte
   `PythonGenerator(schema).compile_module()` (~3,3s) mot
   `SchemaView(schema)` (~0,014s) — SchemaView utgjer under 1 % av
   kostnaden. Retta ved å cache **BERRE** `python_module` og byggje
   `SchemaView`/`target_class` FERSKT per jobbrad (identisk med original
   åtferd for desse to) — null grunn til å ta risikoen for eit
   neglisjerbart tidstap.
3. **Falsk alarm oppdaga og avvist:** Same feil dukka OPP ATT etter
   retting nr. 2 (steg over) på nøyaktig same manuelle reproduksjon.
   Mistanke om attverande feil vart undersøkt ved å køyre den HEILT
   UENDRA (`git show HEAD:...`) originalskriptet mot NØYAKTIG same
   jobbmengd — originalen feila IDENTISK (same feilmelding, same to
   skjema). Rotårsak: den manuelle reproduksjonen batcha convert-rdf +
   roundtrip-json + roundtrip-ttl for SAME skjema i ÉIN jobbliste/prosess
   — noko produksjonskoden (`_run_phase_a_convert_batch()` i
   `tests/test_make.sh`) ALDRI gjer (kvar steg-type får si EIGA,
   separate `jobs_tsv`/podman-kontainar-køyring). Feilen er difor ein
   pre-eksisterande, uendra eigenskap ved å blande steg-typar i éin
   prosess (truleg global/prosess-nivå tilstand i linkml_runtime sin
   RDFLib-lastar/dumpar), IKKJE ein regresjon frå dette tiltaket.
4. **Verifisering (byte-for-byte, jf. Tiltak 4 i tabellen over):** Same
   manuelle jobbmengd (3 skjema, 24 jobbrader) køyrt med både original-
   og ny skriptversjon. Identisk filsett produsert, identisk feilsett (2
   feila jobbar, same feilmeldingar), og **byte-for-byte identisk
   innhald** i alle filer som lykkast (verifisert med `diff -q` per
   fil).
5. **Tidsmåling (kontrollert, same maskin-/yting-tilstand, rett
   etter kvarandre):** original-skriptet mot ny skriptet på same
   jobbmengd — `1m35.388s` → `0m29.409s` (**~3,24× raskare**, isolert
   frå Fase A-parallelliseringa/straum-tilstand-støy elles i økta).
6. `python3 -m py_compile batch-convert.py` — OK.
7. Full `make test` (35 skjema): **591 OK, 5 feil** — identisk med
   referansen, ingen regresjon. Samanlikna mot den IMMEDIATE FØREGÅANDE
   køyringa (same batteridrift-tilstand, difor gyldig samanlikning):
   `roundtrip-json` 233.73s → 153.16s, `roundtrip-ttl` 167.82s → 91.73s —
   samsvarar med den isolerte ~3,24×-målinga.
8. Ein tom fil (`src/assets/scripts/makefile/batch-convert-old.py`)
   materialiserte seg i repoet frå eit mislukka podman bind-mount-forsøk
   under manuell verifisering (kjent, tidlegare dokumentert
   sandbox-artefakt) — fanga opp via `git status` og sletta før avslutning.

## Referanse

- `specs/done/fase-a-oppsummering-test-make.md` — kjelda til
  tidsdataene denne analysen byggjer på
- `specs/done/paralleliser-fase-a-test-make.md` — det opphavlege Fase
  A/B-batchingsarbeidet desse tiltaka byggjer vidare på
- `src/assets/scripts/makefile/batch-linkml-validate.py` — presedens
  for å bypasse ein linkml CLI-kommando sin `sys.exit()`/manglande
  caching-oppførsel ved å kalle det underliggjande API-et direkte
