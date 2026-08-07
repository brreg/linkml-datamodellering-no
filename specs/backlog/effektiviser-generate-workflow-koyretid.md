# Effektiviser køyretida til "Matrix: generate"-jobben (generate.yml)

## Bakgrunn

`generate`-jobben i `.github/workflows/generate.yml` ("Matrix: generate" i
GitHub Actions-UI) køyrer `make domain-<domain>` for kvart domene, parallelt
som eigne matrisejobbar. Denne specen kartlegg **kor tida faktisk går
innanfor éin domene-jobb** — dvs. inne i `domain_target`-pipelinen
(`make/20-domain-targets.mk`), som kallar 12+ `gen-*`-steg i sekvens, kvart
parallellisert **på tvers av skjema** via `xargs -P16`
(`src/assets/scripts/makefile/run-parallel-gen.sh`).

Brukaren sin hypotese: same mønster som løyste køyretida for
`mcp-linkml-validator` (sjå
`specs/done/effektiviser-mcp-linkml-validator-koyretid.md`) — batching av
fleire skjema inn i **éin** kontainar-prosess i staden for éin kontainar per
skjema — kan gje tilsvarande gevinst her, t.d. ved å køyre `gen-shacl` for
alle aktuelle skjema i eit domene (eller på tvers av domene, t.d. alle
AP-NO-profilar) i eitt batch-kall.

Denne specen (1) kartlegg og kvantifiserer tidsbruken per kontainar-kall i
dagens pipeline, (2) foreslår konkret batching basert på funna, og (3)
kartlegg kva som kan parallelliserast **etter** at batching er innført
(sidan batching endrar kva som er den naturlege parallelliseringseininga).

**Merk om terminologi:** referansespecen batcha *validering*
(`mcp-linkml-validator`, eigen server.py vi eig sjølve, som alt las
JSON-RPC-meldingar i ei stdin-løkke). Denne specen batchar *generering*
(`gen-shacl`, `gen-owl` m.fl.) — desse er **LinkML sine eigne CLI-verktøy**
(Click-kommandoar frå `linkml`-pakken, ikkje kode dette repoet eig). Det
finst difor ingen ferdig stdin-løkke å sende fleire kall til; batching her
krev i staden å kalle LinkML sitt **Python-API** direkte (generator-klassane
bak kvar CLI-kommando) frå eit orkestreringsskript vi skriv sjølve, éin gong
per domene-jobb, i staden for å starte éin ny CLI-prosess per skjema.

## Funn — kvantifiserte målingar

Målt lokalt (WSL2/podman, varme image-lag, `localhost/linkml-local:latest`,
`localhost/python-pytest:latest`, `localhost/plantuml:latest`).

### 1) Kontainar-startup og import-skatt, isolert

| Steg | Tid | Kommentar |
|---|---|---|
| Bar `linkml-local`-oppstart (`python3 -c "print()"`) | **2,8 s** | Podman/WSL2-baseline |
| Bar `python-pytest`-oppstart | 2,6 s | Brukt av openapi/asyncapi/erdiagram-filter/docgen-scripts |
| Bar `plantuml`-oppstart (JVM, `-version`) | 2,0 s | |
| `import linkml_runtime` (i `linkml-local`) | ~4,0 s | |
| + `import linkml.generators.<gen>` (shacl/owl/python/jsonschema/proto/rdf/linkml/doc/erdiagram/plantuml) | +1,2–1,5 s | Konsistent på tvers av alle 10 testa generator-modular |
| **Sum: kontainar klar til å generere** | **~8,0–8,5 s** | Før noko faktisk skjemaarbeid har starta |

Same kjernefunn som i `effektiviser-mcp-linkml-validator-koyretid.md`:
**import av `linkml`/`linkml_runtime` (~5 s) dominerer totalt over
podman-oppstart (~2,8 s), og vert betalt på nytt for kvar einaste
kontainar-prosess.** Dette gjeld likt for `linkml-local` (gen-*-verktøya)
som for `mcp-linkml-validator` (same avhengigheitstre, ulikt image).

### 2) Full CLI-kontainar, éitt skjema (dagens arkitektur)

| Kommando | Tid | Kommentar |
|---|---|---|
| `podman run … gen-shacl dcat-ap-no-schema.yaml` | **8,36 s** | ~100 % overhead (startup+import), ~0 s faktisk genereringsarbeid |
| `podman run … gen-owl dcat-ap-no-schema.yaml` | **10,52 s** | ~8,2 s overhead + ~2,3 s faktisk OWL-aksiom-genering |

### 3) Verifisert: generatorarbeid amortiserer nesten heilt i éin delt prosess

Spike, same mønster som referansespecen sin «5 kall i éin kontainar»-test:
importerte 4 generator-klassar (`ShaclGenerator`, `OwlSchemaGenerator`,
`PythonGenerator`, `JsonSchemaGenerator`) **éin gong**, kalla deretter
`.serialize()` for 3 skjema (12 kombinasjonar totalt) i same prosess:

```
import 4 generator-modular: 5,37 s   (betalt éin gong)

                              shacl   owl     python  jsonschema
register-over-aksjeeiere      0,55s   0,70s   0,23s   0,10s
enhetsregisteret-bvrinn       0,69s   1,48s   1,49s   0,64s
dcat-ap-no                    0,68s   1,30s   1,53s   0,49s
```

**Total batcha: 5,37 s (import) + 9,88 s (12× generering) = 15,25 s for 12
generator-kall.** Til samanlikning: 12 separate kontainar-kall à ~8–10,5 s
kvar ≈ 100–125 s CPU-tid (sjølv om `xargs -P16` overlappar dei i praksis, jf.
punkt 4 under om reell CPU-kontensjon på CI-runnarar). Kvart einskild
generator-kall etter den første importen tek **0,1–1,5 s** — konsistent med
kor lite faktisk arbeid `.serialize()` gjer for skjema av denne storleiken.

### 4) Verifisert: PlantUML-rendering batchar òg — separat kontainar, separat gevinst

`plantuml`-biletet (Java/GraphViz, ikkje Python/linkml) tek **fleire
`.puml`-filer i éitt kall**:

| Metode | Tid |
|---|---|
| 2 separate `podman run … plantuml -tsvg <fil>`-kall | 3,55 s + 4,31 s = **7,86 s** |
| 1 batcha `podman run … plantuml -tsvg <fil1> <fil2>`-kall | **4,83 s** |

Begge SVG-ane vart generert korrekt i batch-kallet — **38 % reduksjon for
berre 2 filer**, og gevinsten veks med talet på filer per domene sidan
JVM-/kontainar-oppstarten (~2 s) amortiserer over alle filene i staden for
å betalast per fil.

### 5) Reell domene-køyring, full pipeline (`make domain-oreg`, 2 skjema)

Køyrde heile `domain_target`-pipelinen for `oreg` (2 skjema, dei fleste
generatorar aktiverte, `PARALLEL=16`). Totalt **171 s veggklokketid**, 28
loggførte per-kall-tidslinjer (eksisterande timing-infrastruktur i
`run-parallel-gen.sh` — timing finst alt, berre ikkje aggregert/analysert
før no):

| Steg | Tid (schema A / B) | Kontainarar bak eitt steg | Import linkml? |
|---|---|---|---|
| `merge-imports` (gen-linkml) | 8,0s / 9,5s | 1 | Ja |
| `gen-jsonld-context` | 7,1s / 8,0s | 1 | Ja |
| `gen-shacl` | 8,7s / 9,0s | 1 | Ja |
| `gen-python` | 8,6s / 10,3s | 1 | Ja |
| `gen-json-schema` | 7,4s / 7,9s | 1 | Ja |
| `gen-owl` | 8,9s / 9,9s | 1 | Ja |
| `gen-rdf` | 11,3s / 13,1s | 1 | Ja |
| `linkml-convert` (eksempel) | 7,7s / 10,6s | 1 | Ja |
| `gen-docgen-examples + gen-doc` | 15,0s / 22,1s | 2 (python + linkml) | Delvis |
| `gen-erdiagram` | 10,2s / 11,1s | 2 (linkml + python-filter) | Delvis |
| `gen-proto` | 8,2s / 8,8s | 1 | Ja |
| `gen-plantuml` | 22,9s / 24,5s | 5 (linkml + 2× python-filter + 2× plantuml-svg) | Delvis |
| `gen-openapi` | 8,9s / 9,3s | 2 (python gen + python validate) | **Nei** |
| `gen-informasjonsmodell-instance` | 3,2s / 3,4s | 1 (python) | **Nei** |

`gen-plantuml` er det dyraste enkeltsteget (22–24 s) — 5 kontainarar bak éi
tidslinje. `gen-doc` er nest dyrast (15–22 s), men her er ein ikkje-triviell
del faktisk malarbeid (Jinja-templating over alle klassar), ikkje berre
import — batching gjev framleis gevinst her, men mindre relativt enn for
dei reint import-dominerte stega.

**Viktig skilje avdekt:** `gen-openapi`, `gen-asyncapi`,
`gen-docgen-examples` og `gen-informasjonsmodell-instance` køyrer via
`PYTHON_RUN` (`python-pytest`-biletet) med eigne script
(`gen-openapi.py`, `gen-asyncapi.py`, `gen-docgen-examples.py`,
`generate-informasjonsmodell.py`) som **berre importerer `yaml`/`jinja2`**,
ikkje `linkml`/`linkml_runtime` — verifisert ved å grepe import-linjene i
alle fire scripta. Desse ber **ikkje** import-skatten på ~5 s, berre den
generelle ~2,6 s podman/Python-oppstarten. Batching gjev framleis ei
gevinst her (færre kontainar-oppstartar), men prosentvis mindre enn for dei
linkml-baserte stega.

## Kartlegging — kontainar-kall i dag, skalert til heile repoet

36 skjema fordelt på 9 domene. Talet på skjema med kvar generator-flagg
aktivert i `build.yaml` (grepa direkte, autoritativt):

| Generator | Image | Kontainarar/skjema | Skjema aktiverte | Import linkml? |
|---|---|---|---|---|
| `gen-linkml` (merge, ingen flag) | linkml-local | 1 | 36 (alle) | Ja |
| `gen-jsonld-context` | linkml-local | 1 | 18 | Ja |
| `gen-shacl` | linkml-local | 1 | 20 | Ja |
| `gen-python` | linkml-local | 1 | 11 | Ja |
| `gen-json-schema` | linkml-local | 1 | 19 | Ja |
| `gen-owl` | linkml-local | 1 | 27 | Ja |
| `gen-rdf` | linkml-local | 1 | 32 | Ja |
| `linkml-convert` (eksempel) | linkml-local | 1 | 16 | Ja |
| `gen-doc` (docgen-examples + gen-doc) | python-pytest + linkml-local | 2 | 33 | Delvis (1 av 2) |
| `gen-erdiagram` (gen-erdiagram + filter) | linkml-local + python-pytest | 2 | 33 | Delvis (1 av 2) |
| `gen-proto` | linkml-local | 1 | 11 | Ja |
| `gen-plantuml` (raw + 2× filter + 2× svg) | linkml-local + python-pytest + plantuml | 5 | 19 | Delvis (1 av 5) |
| `gen-xsd` (j2a + a2x + fix-dates) | avrotize | 3 | 1 | Nei (avrotize, eige avhengigheitstre) |
| `gen-openapi` (gen + validate) | python-pytest | 2 | 8 | Nei |
| `gen-asyncapi` (gen + validate) | python-pytest | 2 | 1 | Nei |
| `gen-informasjonsmodell-instance` | python-pytest | 1 | 36 (alle) | Nei |

**Totalt ≈ 474 podman-kontainar-oppstartar** for eit fullt generate-løp over
alle 9 domene (sum av kontainarar/skjema × skjema aktiverte per rad).
Grovt estimert **~300 av desse køyrer på `linkml-local`** og ber difor
~5–5,7 s import-skatt kvar — dvs. **~25–28 minutt reint importarbeid**,
betalt om att og om att for identisk kostnad, fordelt (og delvis skjult av)
`xargs -P16`-parallelliseringa innanfor kvart domene.

**Merk om `PARALLEL=16` og reell CI-kapasitet:** GitHub-hosta
`ubuntu-22.04`-runnarar har typisk 4 vCPU. `xargs -P16` let difor opptil 16
`linkml-local`-kontainarar starte samstundes, langt over talet på fysiske
kjernar — dette overlappar veggklokketid, men **reduserer ikkje** den
totale CPU-tida import-skatten kostar, og kan i verste fall gje dårlegare
throughput enn eit lågare `-P`-tal ved sterk CPU-kontensjon (same åtvaring
som `parallelliser-domene-validering.md` og
`effektiviser-mcp-linkml-validator-koyretid.md` (Tiltak 3) alt har
dokumentert for valideringssteget). Batching løyser dette meir grunnleggjande
enn å justere `-P`: han fjernar sjølve importskatt-repetisjonen, i staden
for berre å overlappe ho.

## Tiltak (prioritert etter forventa gevinst / risiko)

### Tiltak 1 — Batch dei linkml-baserte generatorane per domene til éin kontainar-prosess

**Omfattar:** `gen-linkml` (merge), `gen-jsonld-context`, `gen-shacl`,
`gen-python`, `gen-json-schema`, `gen-owl`, `gen-rdf`, `gen-proto`,
`linkml-convert` (eksempel-RDF), samt sjølve LinkML-delen av `gen-doc`
(`DocGenerator`) og `gen-erdiagram` (`ERDiagramGenerator`) og `gen-plantuml`
(`PlantumlGenerator`) — alle desse er reine `linkml`-Python-API-kall som kan
gjerast i same prosess.

**Forventa gevinst:** størst enkelttiltak, jf. «Funn» punkt 3 — import
(~5,4 s) betalt éin gong per domene i staden for éin gong per (skjema ×
generator)-kombinasjon; sjølve genereringa tek 0,1–1,5 s per kall. For
`oreg` (2 skjema, 7 reine linkml-steg) svarar det til: dagens ~67,7 s
(summen av dei 7 linkml-radene i «Funn» punkt 5) → estimert **~15–25 s**
batcha (5,4 s import + 14 × ~1 s generering, konservativt). Skalerer betre
for større domene (`ap-no`, `fint`) sidan import-skatten er fast, men talet
på skjema × generatorar veks.

**Steg:**

1. Lag eit nytt orkestreringsskript
   (`src/assets/scripts/makefile/batch-generate.py`), analogt med
   `src/mcp-linkml-validator/batch-flatten-and-validate.py`: for eit gjeve
   domene, bygg opp lista over (skjema, generator)-kombinasjonar som skal
   køyrast, filtrert mot `build.yaml`-flagg — **same filtreringslogikk som
   `run-parallel-gen.sh` sin `--flag`-handtering** (les `  <flag>: true`
   frå `build.yaml`, unntak for `--check-suffix`-avhengige generatorar som
   `gen-xsd`/`gen-openapi`/`gen-asyncapi`, sjå Tiltak 2/3).
2. Importer kvar generator-modul **éin gong** ved oppstart
   (`ShaclGenerator`, `OwlSchemaGenerator`, `PythonGenerator`,
   `JsonSchemaGenerator`, `RdfGenerator`, `ProtoGenerator`,
   `LinkMLGenerator`, `DocGenerator`, `ERDiagramGenerator`,
   `PlantumlGenerator`), løkk deretter over kombinasjonane og kall
   `.serialize()`/tilsvarande, skriv resultatet til same filsti som
   dagens `GEN_CMD`-mønster i `make/10-generator-macros.mk` produserer
   (bevar filnamn/katalogstruktur uendra — nedstraums forbrukarar,
   `mkdocs/publish.sh` m.fl., skal ikkje merke skilnad).
3. **Kritisk verifiseringssteg:** map kvar CLI-flagg dagens makroar sender
   (t.d. `OWL_DEFAULT_FLAGS`,
   `--skip-vacuous-local-range-axioms --skip-vacuous-min-zero-cardinality-axioms --consolidate-cardinality-axioms`,
   og per-skjema `owl_flags`/`shacl_flags`-override frå `build.yaml`) til
   det tilsvarande **konstruktør-kwarget** i Python-API-et (t.d.
   `OwlSchemaGenerator(schema, skip_vacuous_local_range_axioms=True, …)`
   — deprecation-åtvaringane i «Funn» punkt 2 stadfester namnet på desse
   kwarga). Verifiser at output er **byte-for-byte identisk** (eller
   semantisk identisk der rekkjefølgje/whitespace kan variere) mot dagens
   CLI-output for eit representativt utval skjema, inkludert minst eitt med
   `owl_flags`/`shacl_flags`-override.
4. `gen-doc` og `gen-erdiagram` har etterhandsaming (jf.
   `gen-docgen-examples.py`, `sed -i "/Container/d"`,
   `filter_container.awk`, `filter_erdiagram.py`) — desse er alt reine
   Python/awk-script utan `linkml`-import (jf. «Funn» punkt 5). Vurder å
   flytte denne etterhandsaminga **inn i same batch-prosess** (som
   funksjonskall, ikkje subprocess) for å fjerne endå ein kontainar-start
   per skjema, ikkje berre linkml-delen.
5. Oppdater `run_gen_*_parallel`-makroane i `make/10-generator-macros.mk`
   og `domain_target` i `make/20-domain-targets.mk` til å kalle
   batch-skriptet éin gong per domene i staden for å løkke per generator ×
   skjema.
6. Handter feil per (skjema, generator)-kombinasjon individuelt — eitt
   skjema sin genereringsfeil skal ikkje stoppe resten av batchen, same
   prinsipp som `server.py` sin per-melding exception-handtering frå
   referansespecen sitt Tiltak 1.
7. Test: køyr mot `oreg` (liten, rask iterasjon) og deretter `ap-no`/`fint`
   (større, fleire generatorar aktiverte), samanlikn generert output
   fil-for-fil mot dagens sekvensielle køyring.

**Risiko:** Låg-til-moderat. Same mønster som alt er verifisert i
produksjon for validerings-batchen. Hovudrisikoen er kwarg-mapping (steg 3)
— LinkML sitt Python-API kan ha andre standardverdiar enn CLI-et for enkelte
flagg, så output må verifiserast eksplisitt, ikkje anteke identisk.

### Tiltak 2 — Batch PlantUML SVG-rendering per domene

**Forventa gevinst:** verifisert i «Funn» punkt 4 — 38 % reduksjon for 2
filer, veks med fleire filer. `gen-plantuml` er aktivert for 19 skjema
(2 SVG-render-kall kvar = 38 kontainar-kall i dag) — batcha til éin
`podman run … plantuml -tsvg <alle raw/filtered .puml for domenet>` per
domene (9 kall totalt i staden for opptil 38).

**Steg:**

1. Endre `run_gen_plantuml_parallel` (`make/10-generator-macros.mk`) til å
   generere alle `.puml`-filer for domenet **først** (uendra, framleis
   linkml-baserte kall — eller flytta inn i Tiltak 1 sin batch), samle
   opp filstiane, og gjere **éitt** samla
   `podman run … plantuml -tsvg <fil1> <fil2> …`-kall for heile domenet
   til slutt, i staden for eitt kall (× full/filtered) per skjema.
2. Verifiser at alle SVG-ar vert generert korrekt og identisk med
   enkeltvis rendering (verifisert her for 2 filer — test òg med eit
   domene med fleire skjema, t.d. `ap-no`).
3. Handter feil-tilfelle: dersom éin `.puml`-fil er ugyldig, stadfest at
   PlantUML-biletet framleis genererer SVG for dei andre filene i batchen
   (PlantUML sitt CLI er dokumentert å halde fram med neste fil ved feil i
   éin — verifiser dette eksplisitt, sidan feilhandtering per fil er
   annleis enn per-kontainar exit-kode).

**Risiko:** Låg. Uavhengig av Tiltak 1, kan gjerast separat og først som
eit lite, isolert steg.

### Tiltak 3 — Batch dei ikkje-linkml PYTHON_RUN-generatorane (openapi/asyncapi/informasjonsmodell/docgen-examples)

**Forventa gevinst:** moderat — desse ber ikkje import-skatten (jf. «Funn»
punkt 5), så gevinsten er avgrensa til å spare ~2,6 s podman-oppstart per
kall i staden for ~5,5 s. Likevel meiningsfullt i sum: 8 (`openapi`) × 2 +
1 (`asyncapi`) × 2 + 36 (`informasjonsmodell`) + 33 (`docgen-examples`,
del av `gen-doc`) ≈ 87 kontainar-kall som kan reduserast til éin per
domene per scripttype (9 domene × 4 scripttypar = 36 kall).

**Steg:**

1. Skriv (eller utvid `batch-generate.py` frå Tiltak 1 med) ein enkel
   løkke-modus for dei fire scripta (`gen-openapi.py`, `gen-asyncapi.py`,
   `generate-informasjonsmodell.py`, `gen-docgen-examples.py`) som tek imot
   ei liste med skjema i staden for eitt, og køyrer heile lista i same
   Python-prosess.
2. `gen-openapi`/`gen-asyncapi` sin `validate`-del (`openapi-spec-validator`,
   `asyncapi validate`) er **eksterne CLI-verktøy**, ikkje eige script —
   `asyncapi validate` køyrer i eige `ASYNCAPI_IMAGE` (Node.js), så denne
   delen kan ikkje batchast inn i Python-prosessen, men kan potensielt ta
   fleire filer i eitt kall (verifiser CLI-støtte, same idé som Tiltak 2).
   `openapi-spec-validator` er ein Python-CLI i `python-pytest`-biletet —
   kan kallast via sitt Python-API i same batch-prosess.

**Risiko:** Låg. Minst kritisk av dei tre tiltaka — gjer sist, eller
parallelt som eit uavhengig, lågrisiko-steg.

### Ikkje eit tiltak her: `gen-xsd` (avrotize)

Berre 1 skjema (`samt-bu`) har `xsd: true` i dag. Batching av
`avrotize`-kjeda (3 kontainar-kall) ville gje neglisjerbar gevinst i
absolutte tal og er ikkje prioritert i denne runden — revurder dersom
fleire skjema tek i bruk `xsd: true` seinare.

## Parallellisering etter batching — kva kan køyre samstundes?

Batching (Tiltak 1–3) endrar den naturlege parallelliseringseininga: i dag
er eininga **(skjema, generator)** via `xargs -P16`; etter batching er ho
**(domene, generator-gruppe)** — éin kontainar-prosess per domene per
gruppe (linkml-gruppa frå Tiltak 1, plantuml-gruppa frå Tiltak 2,
python-script-gruppa frå Tiltak 3).

**Kartlagt parallelliseringspotensial:**

1. **På tvers av grupper, innanfor same domene:** Tiltak 1 (linkml-batch),
   Tiltak 2 (plantuml-batch) og Tiltak 3 (python-script-batch) er
   **gjensidig uavhengige** for same domene så snart Tiltak 1 sine
   filutdata (spesielt `gen-json-schema` sin `.json`, som
   `gen-xsd`/`gen-openapi`/`gen-asyncapi` er avhengige av via
   `--check-suffix schema.json`) er skrivne. Dei tre gruppene kan difor
   startast som separate baksgrunnsprosessar (`&`/`wait`, same mønster som
   `mkdocs/publish.sh` og `parallelliser-domene-validering.md`) — men
   Tiltak 3 sin `openapi`/`asyncapi`-del må **vente** på at Tiltak 1 sin
   `gen-json-schema`-batch er ferdig for dei aktuelle skjemaa (uendra
   avhengigheit frå dagens pipeline, berre flytta frå "steg i sekvens" til
   "batch-jobb med ein eksplisitt wait").
2. **På tvers av domene:** uendra — `generate.yml` sin matrise
   (`strategy.matrix.domain`) parallelliserer alt på domene-nivå via
   separate GitHub Actions-jobbar/runnarar. Dette er **ikkje** avgrensa av
   lokal CPU-kontensjon (kvar matrisejobb får sin eigen runnar), så det
   held fram uendra.
3. **Innanfor Tiltak 1 sin batch, mellom domene:** sidan import-skatten
   berre er ~5,4 s og no berre betalast éin gong **per domene-jobb**
   (ikkje éin gong totalt for heile repoet), er det ikkje noko å hente på
   å slå saman fleire domene til éin batch-prosess — kvar matrisejobb
   køyrer alt isolert på sin eigen runnar. **Ikkje eit tiltak**: batching
   på tvers av domene (t.d. «alle AP-NO-profilar i eitt kall uansett kva
   matrisejobb dei høyrer til») krev å endre sjølve matrise-strukturen i
   `generate.yml`, noko som taper den eksisterande domene-nivå CI-
   parallelliseringa (fleire runnarar samstundes) mot ei enkelt, lengre
   batch-jobb — venta netto tap, ikkje gevinst, sidan domene-parallellitet
   i dag alt er "gratis" (fleire runnarar, ikkje delt CPU).
4. **`PARALLEL`-talet (`xargs -P16`) vert i stor grad overflødig** etter
   Tiltak 1–3: talet på gjenverande separate kontainar-kall per domene går
   frå opptil ~50 (for eit domene som `ap-no` med mange skjema/generatorar)
   ned til **3–4** (éin per batch-gruppe, pluss eventuelle
   validator-eksterne kall frå Tiltak 3 punkt 2). Desse 3-4 kan trygt køyre
   samstundes (`&`/`wait`) utan CPU-kontensjonsrisiko, sidan talet er langt
   under CI-runnaren sitt kjernetal — i motsetnad til dagens `-P16` som
   overskrid det kraftig (jf. «Kartlegging»).

**Konklusjon:** etter batching bør parallellisering skje **på gruppe-nivå
innanfor domenet** (3-4 samstundes prosessar, `&`/`wait`), ikkje lenger på
skjema-nivå (`xargs -P16` fell bort som konsept for dei batcha
generatorane). Domene-nivå-parallelliteten i `generate.yml` sin matrise er
uendra og treng ingen endring.

## Handlingsliste

- [x] Tiltak 1: design og implementer `batch-generate.py` for dei 8
      generatorane utan etterhandsaming (merge, jsonld-context, shacl,
      python, json-schema, owl, rdf, proto). `linkml-convert`, `gen-doc`
      og `gen-erdiagram` sin linkml-del er **ikkje** batcha i denne runden
      (sjå «Utført (Tiltak 1)» — avgrensa medvite for å halde endringa
      isolert/verifiserbar; kan takast som eige, lite oppfølgingssteg)
- [x] Tiltak 1: verifiser CLI-flagg → Python-API-kwarg-mapping for
      `shacl_flags`/`owl_flags`-override, inkludert minst eitt skjema med
      eksplisitt override
- [x] Tiltak 1: verifiser output byte-for-byte/semantisk identisk mot
      dagens CLI-basert generering for eit representativt utval skjema
      (minst eitt lite domene, eitt stort domene med mange generatorar)
- [x] Tiltak 1: oppdater `make/10-generator-macros.mk` og
      `make/20-domain-targets.mk` til å bruke batch-skriptet
- [ ] Tiltak 2: batch PlantUML SVG-rendering til éitt `podman run`-kall per
      domene, verifiser identisk SVG-output og feilhandtering per fil
- [ ] Tiltak 3: batch `gen-openapi`/`gen-asyncapi`/
      `gen-informasjonsmodell-instance`/`gen-docgen-examples` sine
      Python-script til éin prosess per domene per scripttype
- [ ] Parallellisering: implementer `&`/`wait`-mønster mellom dei 3-4
      gjenverande batch-gruppene per domene (Tiltak 1/2/3), med korrekt
      avhengigheit (`openapi`/`asyncapi` ventar på `gen-json-schema`)
- [ ] Mål reell veggklokkegevinst i CI (ikkje berre lokalt) for minst eitt
      lite domene (`oreg`) og eitt stort (`ap-no` eller `fint`), samanlikna
      mot baseline før denne specen
- [x] Oppdater `make/README.md` og `mkdocs/docs/`-rettleiingar dersom
      `gen-*`-targeta sin observerbare oppførsel (loggformat, feilmeldingar)
      endrar seg som følgje av batchinga (`make/README.md` oppdatert;
      loggformatet er uendra utetter, ingen `mkdocs/docs/`-endring naudsynt)

## Utført (Tiltak 1 — 2026-08-07)

Implementert som planlagt for dei 8 generatorane utan etterhandsaming:
`merge` (gen-linkml, valideringssteg), `jsonld-context`, `shacl`, `python`,
`json-schema`, `owl`, `rdf`, `proto`. `gen-doc`/`gen-erdiagram`/
`gen-plantuml`/`gen-xsd`/`gen-openapi`/`gen-asyncapi` er **uendra** i denne
runden (framleis `run-parallel-gen.sh`) — dei har etterhandsaming/eksterne
verktøy som gjer dei til eit eige, seinare steg (Tiltak 2/3).

**Nye/endra filer:**

- `src/assets/scripts/makefile/batch-generate.py` (ny) — REGISTRY-basert
  batch-skript. For kvar av dei 8 generator-«kinda» batchar det N skjema inn
  i éin podman-kontainar-prosess. Kritisk designval, verifisert via spike
  før utrulling: i staden for å handoversette kvart Click-flagg til eit
  generator-kwarg sjølv (feilutsett — sjå funnet under om `OwlSchemaGenerator`
  sin skjulte `metadata_profiles`-standardverdi), kallar skriptet
  generator-modulen sin **eigen** Click-`cli`-kommando direkte i prosessen
  via `Command.make_context()` + `Command.invoke()` med stdout fanga via
  `contextlib.redirect_stdout`. Dette gjev identisk åtferd til den ekte
  CLI-en (Click løyser alle standardverdiar sjølv, cli()-funksjonskroppen
  køyrer uendra) utan risiko for hand-transkripsjonsfeil.
- `make/10-generator-macros.mk`: `run_gen_parallel`, `run_gen_linkml_parallel`,
  `run_gen_shacl_parallel`, `run_gen_owl_parallel`, `run_gen_rdf_parallel`
  kallar no `batch-generate.py` (éin `$(LINKML_RUN)`-kontainar for heile
  skjemalista) i staden for `run-parallel-gen.sh` (éin kontainar per skjema
  via xargs). `SHACL_DEFAULT_FLAGS`/`OWL_DEFAULT_FLAGS` Make-variablane er
  fjerna — standardflagga er no einaste-kjelde i `batch-generate.py` sitt
  REGISTRY, ikkje duplisert mellom Makefile og Python.
- `make/11-generator-targets.mk`, `make/20-domain-targets.mk`: kallstadene
  oppdatert til å bruke `batch-generate.py` sine generator-namn
  (`jsonld-context`, `python`, `json-schema`, `proto`) i staden for CLI-
  kommandonamn (`gen-jsonld-context` osv.) — `$3`-suffiks-argumentet er
  fjerna sidan filnamn no er ei eiga kjelde i REGISTRY.
- `make/README.md`: `10-generator-macros.mk`-rada og skript-tabellen
  oppdatert til å nemne batch-arkitekturen.
- `src/assets/scripts/makefile/run-parallel-gen.sh`: toppkommentar
  presisert til å seie kva makroar som **framleis** brukar han (dei med
  etterhandsaming), sidan det ikkje lenger er «alle».

**Kritisk funn undervegs (spike, før utrulling):** eit forsøk på å
handoversette CLI-flagg til generator-kwarg avdekte at `gen-owl` sin CLI
alltid sender `metadata_profiles=[MetadataProfile.linkml]` til
`OwlSchemaGenerator`, sjølv utan `--metadata-profile`-flagg — men
dataklassen sin eigen standardverdi er tom liste (`[]`). Ei hand-skriven
kwarg-mapping ville difor produsert **feil** output for alle OWL-skjema utan
å feile synleg (ingen exception, berre annleis annotasjonsstil). Dette var
den konkrete grunngjevinga for å velje Click-driven-invocation-designet
(`make_context`/`invoke`) i staden for hand-mapping — Click løyser alle
slike skjulte standardverdiar automatisk, sidan det er den **same**
`cli()`-funksjonskroppen som køyrer, uendra.

**Verifisert (målt lokalt, WSL2/podman, varme image-lag):**

Semantisk ekvivalens, `oreg` (2 skjema) og `ap-no` (7 skjema, det største
domenet) — alle genererte filer samanlikna byte-for-byte (`.py`, `.json`,
`.jsonld`, `.proto`) eller via RDF-graf-isomorfi (`.ttl`, sidan
rekkjefølgje på blanknode-eigenskapar ikkje er eit meiningsfullt
identitetskriterium, sjå under):

| Domene | Filer samanlikna | Avvik |
|---|---|---|
| `oreg` | 330 | 0 reelle (6 filer avvik berre i embedda `generation_date`-tidsstempel) |
| `ap-no` | 1715 | 0 reelle (18 `.ttl`-filer «NOT ISOMORPHIC» — sjå under) |

**Dei 18 TTL-avvika i `ap-no` er stadfesta IKKJE ei følgje av denne
endringa.** Køyrde `gen-shacl` (uendra, ingen batching involvert) **to
gonger** direkte mot `dcat-ap-no-schema.yaml` — dei to CLI-køyringane var
**seg imellom** ikkje-isomorfe (same triple-tal, ulik blanknode-/eigenskap-
rekkjefølgje). Dette er ein kjend eigenskap ved korleis `linkml`/`rdflib`
brukar hash-baserte set/dict internt ved SHACL/RDF-serialisering (venteleg
`PYTHONHASHSEED`-avhengig) — han fanst identisk **før** denne specen, og
alle 18 avvika har nøyaktig same signatur (identisk triple-tal, ikkje-
isomorf). Byte-for-byte-diff er difor aldri eit gyldig identitetskriterium
for `gen-shacl`/`gen-rdf`-output i dette repoet, batcha eller ikkje — bruk
graf-isomorfi.

**Talet på kontainar-oppstartar** for dei 8 batcha generatorane, `ap-no`
(7 skjema, varierande talet aktiverte per generator jf. build.yaml-flagg):
**37 → 7** (éin kontainar per generator-kind i staden for éin per
(skjema × generator)-kombinasjon).

**Veggklokketid — VIKTIG, ærleg avvik frå forventing i «Funn»-seksjonen:**
lokal måling synte **ingen** veggklokkegevinst, verken for `oreg` (2 skjema:
171s → 172s) eller `ap-no` (7 skjema: 207s → 212s) — innanfor normal støy,
om noko marginalt tregare. Rotårsak: denne sandkassa har **16 CPU-kjernar**
lokalt (verifisert med `nproc`), langt fleire enn dei 2–7 skjemaa i desse
domena. Den gamle arkitekturen sin `xargs -P16` oppnår difor **allereie
full overlapping** for desse domenestorleikane lokalt — sekvensielt
importskatt-betalt-éin-gong-per-kontainar (ny arkitektur) slår ikkje
parallelt-importskatt-betalt-N-gonger-men-overlappa (gamal arkitektur) når
overlappinga uansett er komplett. Dette **stadfestar** «Kartlegging»-
seksjonen sitt poeng om `PARALLEL=16` vs. CI sine typiske ~4 vCPU — den
faktiske veggklokkegevinsten frå denne endringa er venta å vise seg **i
CI**, der 37 samstundes/nær-samstundes kontainarar (mot 7) på ein
resssurs-avgrensa runner ville skape kø/kontensjon som denne 16-kjerne
sandkassa ikkje reproduserer. Handlingslistepunktet «Mål reell
veggklokkegevinst i CI» er difor **ikkje** kryssa av — det attståande,
avgjerande steget for å stadfeste den opphavlege hypotesen sin faktiske
gevinst.

**Testa:**
- `make domain-oreg` og `make domain-ap-no` — begge fullførte med exit-kode
  0, ingen feil.
- Semantisk fil-for-fil-samanlikning (byte-diff + RDF-isomorfi) mot ei
  reint sekvensiell (før-endring) køyring av same to domene — sjå tabell
  over.
- Verifiserte at éi utilsikta side-effekt (`gen-informasjonsmodell-
  instance` sitt steg oppdaterte `src/linkml/ap-no/*/metadata/*-manifest.yaml`
  under testinga) var **ikkje** knytt til denne endringa — stadfesta at
  same reduserte `finnes_i_format`-liste oppstår med den **gamle**,
  uendra arkitekturen òg (skjema sine `build.yaml`-flagg for
  `json_schema`/`jsonld_context`/`protobuf`/`openapi` er alt `false`; dei
  committa manifest-filene var rett og slett ikkje regenererte sidan
  flagga vart sett). Manifest-filene vart reverterte til committa
  tilstand etter testinga (`git checkout --`), ikkje ein del av denne
  endringa sitt diff.

**Attverande arbeid:** Tiltak 2, Tiltak 3, parallellisering mellom
batch-gruppene, og CI-måling er ikkje gjennomførte i denne runden.
