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

## Tiltak 4 — Batch dei fire attverande generatorane (linkml-convert, gen-erdiagram, gen-plantuml Fase A, gen-doc Fase B)

Etter Tiltak 1–3 står fire generatorar att heilt eller delvis ubatcha (jf.
«kva gjenstår»-svaret gitt undervegs i denne specen):

| Generator | Status i dag | Kontainarar/skjema |
|---|---|---|
| `linkml-convert` (eksempel-RDF) | Heilt ubatcha — eiga manuell bash-løkke i `domain_target` | 1 (LINKML_RUN) |
| `gen-erdiagram` | Heilt ubatcha | 2 (LINKML_RUN + PYTHON_RUN) — awk-steget imellom er allereie host-køyrt, ikkje kontainerisert |
| `gen-plantuml` Fase A (`.puml`-generering) | Ubatcha (berre Fase B, SVG-rendering, vart batcha i Tiltak 2) | 3 (LINKML_RUN + 2× PYTHON_RUN) |
| `gen-doc` Fase B (sjølve CLI-et) | Ubatcha (berre `docgen-examples`-forsteget vart batcha i Tiltak 3) | 1 (LINKML_RUN) |

**Verifisert føresetnad for dette tiltaket:** alle fire brukar Click-kommandoar
frå same familie som Tiltak 1 sine generatorar:

- `linkml-convert` → `linkml.converter.cli:cli` (stadfesta via
  `importlib.metadata.entry_points()`)
- `gen-erdiagram` → `linkml.generators.erdiagramgen.cli`
- `gen-plantuml` → `linkml.generators.plantumlgen.cli` (alt kjent frå
  Tiltak 2)
- `gen-doc` → `linkml.generators.docgen.cli`

Import-kostnad målt for dei tre nye modulane (same mønster som Tiltak 1
sitt «Funn»): `linkml.converter.cli` 5,47 s, `erdiagramgen` 5,74 s,
`docgen` 5,72 s — konsistent med dei ~5,4–5,7 s alle andre linkml-
generator-modular alt viste.

**Kritisk spike verifisert før dette tiltaket vart skrive:** `gen-doc` er
annleis enn Tiltak 1 sine generatorar — `DocGenerator` **skriv fleire
filer til ein katalog** (via `-d`), returnerer ikkje éin streng til
stdout. Testa eksplisitt om `batch-generate.py` sitt `run_click()`-mønster
(`make_context()` + `invoke()`) framleis fungerer korrekt for denne typen
kommando: køyrde `gen-doc` in-process mot `register-over-aksjeeiere`,
samanlikna heile output-katalogen (60 `.md`-filer) mot ein ekte CLI-
subprosess-køyring — **`diff -rq` fann ingen skilnader i det heile**.
Dette stadfestar at Click-drive-invokering-mønsteret generaliserer til
katalog-skrivande generatorar utan endring, ikkje berre dei stdout-
returnerande frå Tiltak 1.

**Viktig skilnad frå Tiltak 1 sine generatorar — dei to filter-scripta må
refaktorerast først:** `filter_plantuml.py` og `filter_erdiagram.py` er,
i motsetnad til `gen-docgen-examples.py` (alt refaktorert reint i Tiltak
3), **flate modul-nivå-script** — dei les `sys.argv` direkte som
modul-nivå-kode, har ingen `main()`-funksjon og ingen
`if __name__ == "__main__":`-vakt. Dei kan difor **ikkje** importerast
trygt i dag (import ville køyrt heile skriptlogikken med feil/manglande
argv med det same). Dette er den einaste reelle blokkeringa for Fase B av
`gen-erdiagram`/`gen-plantuml` — sjølve genereringssteget (Fase A) er
uavhengig av dette og kan batchast med det same.

`filter_container.awk` (brukt av `gen-erdiagram`, mellom generering og
python-filter) køyrer allereie **direkte på CI-runnaren/host**, ikkje i
ein kontainar (ingen `podman run`-innpakking i dagens `GEN_CMD`) — han ber
difor ikkje kontainar-oppstart-kostnaden dei andre stega gjer, og **er
ikkje ein kandidat for batching** (ingenting å vinne, jf. same grunngjeving
som «Ikkje eit tiltak: gen-xsd»).

### Steg

1. **`gen-doc` Fase B** (lågast risiko, alt spike-verifisert): legg til
   `"doc"` som ny generator-kind i `batch-generate.py`. `DocGenerator`
   sitt filskrivings-mønster (katalog, ikkje éin streng) passar ikkje heilt
   inn i dagens `GeneratorSpec.out_suffix`-felt (som antek éin
   utfil-streng) — utvid `GeneratorSpec` med eit `writes_directory: bool`-
   felt (eller tilsvarande), slik at `main()`-løkka anten skriv
   `run_click()` sin returverdi til éi fil (som i dag) eller berre kallar
   `run_click()` for biverknaden (filene DocGenerator alt skreiv via
   `-d`/`directory`-kwarget) utan å skrive noko sjølv. Flytt
   `sed -i "/Container/d" index.md`-oppryddinga inn i same batch-steg som
   ei enkel Python-strengoperasjon (fjernar ein liten, unødvendig
   host-avhengigheit til `sed`).
2. **`linkml-convert`:** legg til ein ny batch-funksjon (i
   `batch-generate-instances.py`, sidan jobb-lista her ikkje er reint
   schema→utfil, men schema+eksempel+utfil-triplar). Gjenbruk
   `convert-examples.sh` sin eksisterande discovery/filtrerings-logikk
   (finn eksempelfiler, filtrer mot `example_rdf: false`) — anten ved å
   halde fram å køyre det scriptet for å produsere jobb-TSV-en og lese ho
   inn i batch-Python-et, eller ved å portere same filtreringslogikk til
   Python (vurder kva som gjev minst duplisering). Kall
   `linkml.converter.cli:cli` sitt Click-API in-process per triple,
   isolert feilhandtering per triple (same mønster som resten av
   `batch-generate-instances.py`). Erstatt `domain_target` sin manuelle
   `while read`-løkke med eitt batch-kall.
3. **`gen-erdiagram` Fase A (generering):** legg til `"erdiagram"` som ny
   kind i `batch-generate.py` sitt REGISTRY (same mønster som dei 8
   eksisterande), skriv til `$name-erdiagram-unfiltered.md` **før** awk-
   steget (uendra, held fram å køyre per skjema på host).
4. **`gen-erdiagram` Fase B (python-filter):** refaktorer
   `filter_erdiagram.py` etter same mønster som Tiltak 3 sin
   `gen-docgen-examples.py`-refaktorering — trekk ut ein
   `process_file(schema_path, mmd_path) -> str`-funksjon, behald
   ein tynn CLI-kompatibel `main()` som kallar henne. Legg til ein
   `"erdiagram-filter"`-modus i `batch-generate-instances.py` som løkkar
   over N skjema sine (alt awk-filtrerte) mellomresultat i éin prosess.
5. **`gen-plantuml` Fase A (generering):** legg til `"plantuml"` som ny
   kind i `batch-generate.py` sitt REGISTRY, skriv `$name-raw.puml`.
6. **`gen-plantuml` Fase B (python-filter, to modus):** refaktorer
   `filter_plantuml.py` same måte som steg 4 — trekk ut
   `process_file(schema_path, puml_path, mode) -> str`. Legg til ein
   `"plantuml-filter"`-modus i `batch-generate-instances.py` som løkkar
   over (skjema × modus)-kombinasjonar (2 per skjema: `filtered` og
   `full`) i éin prosess.
7. **Verifiser** alle fire som i Tiltak 1–3: byte-for-byte-diff (eller
   RDF-isomorfi der relevant — `linkml-convert` sitt TTL-output er
   underlagt same kjende non-determinisme som `gen-shacl`/`gen-rdf`, jf.
   Tiltak 1) mot ikkje-batcha køyring, for minst eitt lite og eitt stort
   domene, pluss ein isolert feilhandteringstest for kvar av dei to
   refaktorerte filter-scripta.
8. **Oppdater `make/20-domain-targets.mk`** — fjern `linkml-convert`-
   løkka og pek `run_gen_doc_parallel`/`run_gen_erdiagram_parallel`/
   `run_gen_plantuml_parallel` sine attverande fasar til dei nye batch-
   kalla.

### Forventa gevinst

Kontainar-tal for eit domene med maksimalt aktiverte skjema, dei fire
generatorane samla (baserte på dagens repo-breie flagg-tal: `example_rdf`
16, `erdiagram` 33, `plantuml` 19, `docs` 33):

| Generator | Kontainarar i dag (repo-breitt) | Etter Tiltak 4 (repo-breitt, ~9 domene) |
|---|---|---|
| `linkml-convert` | 16 | ≤9 |
| `gen-erdiagram` (generering) | 33 | ≤9 |
| `gen-erdiagram` (filter) | 33 | ≤9 |
| `gen-plantuml` (generering) | 19 | ≤9 |
| `gen-plantuml` (filter, 2×) | 38 | ≤9 |
| `gen-doc` | 33 | ≤9 |
| **Sum** | **172** | **≤54** |

Same atterhald som Tiltak 1 og 2: den reelle veggklokkegevinsten avheng av
om steget alt var fullt overlappa av `xargs -P16` lokalt (som Tiltak 1) eller
strukturelt flytta ut av ein per-skjema-kritisk-sti (som Tiltak 2 synte
ekte gevinst for). `gen-doc` og `gen-erdiagram` gjer også reelt
malararbeid/traversering (ikkje berre import), så gevinsten der vil vere
mindre enn dei reint import-dominerte stega — mål lokalt og i CI før
konklusjon, same metodikk som Tiltak 1–3.

### Risiko

**Moderat.** Høgast risiko-element:

- Refaktoreringa av `filter_plantuml.py`/`filter_erdiagram.py` frå flate
  script til importerbare funksjonar er meir ein reell kodeendring enn
  Tiltak 1–3 sine reint additive endringar — begge må verifiserast å
  produsere **identisk** output før/etter refaktorering, isolert frå
  batch-spørsmålet (same to-stegs verifiseringsmetodikk som
  `gen-docgen-examples.py`-refaktoreringa i Tiltak 3: test standalone-CLI
  uendra FØRST, deretter test batch-modus).
- `GeneratorSpec`-utvidinga for katalog-skrivande generatorar (`gen-doc`)
  er den einaste strukturelle endringa i sjølve `batch-generate.py` sidan
  Tiltak 1 vart implementert — hold ho minimal (eitt nytt felt, ikkje ein
  ny abstraksjonsklasse) for å unngå å komplisere REGISTRY-et unødvendig
  for dei 8 eksisterande, uendra generatorane.

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
- [x] Tiltak 2: batch PlantUML SVG-rendering til éitt `podman run`-kall per
      domene, verifiser identisk SVG-output og feilhandtering per fil
- [x] Tiltak 3: batch `gen-openapi`/`gen-asyncapi`/
      `gen-informasjonsmodell-instance`/`gen-docgen-examples` sine
      Python-script til éin prosess per domene per scripttype
- [x] Parallellisering: implementer `&`/`wait`-mønster mellom dei
      uavhengige batch-gruppene per domene (etter Tiltak 1-4), med korrekt
      avhengigheit (`openapi`/`asyncapi`/`xsd` ventar på `gen-jsonschema`,
      `gen-informasjonsmodell-instance` ventar på alt)
- [ ] Mål reell veggklokkegevinst i CI (ikkje berre lokalt) for minst eitt
      lite domene (`oreg`) og eitt stort (`ap-no` eller `fint`), samanlikna
      mot baseline før denne specen
- [x] Oppdater `make/README.md` og `mkdocs/docs/`-rettleiingar dersom
      `gen-*`-targeta sin observerbare oppførsel (loggformat, feilmeldingar)
      endrar seg som følgje av batchinga (`make/README.md` oppdatert;
      loggformatet er uendra utetter, ingen `mkdocs/docs/`-endring naudsynt)
- [x] Tiltak 4: refaktorer `filter_plantuml.py`/`filter_erdiagram.py` til
      importerbare `process_file()`-funksjonar, verifiser standalone-CLI
      uendra
- [x] Tiltak 4: legg til `"doc"`/`"erdiagram"`/`"plantuml"`-kind i
      `batch-generate.py` sitt REGISTRY (utvida `GeneratorSpec` med
      `extra_argv_fn`/`post_fn`/`out_subdir`-felt, ikkje `writes_directory`
      som opphavleg skissert — sjå «Utført» for grunngjeving)
- [x] Tiltak 4: batch `linkml-convert` (schema+eksempel+utfil-triplar) i
      `batch-generate-instances.py`, gjenbruk `convert-examples.sh` sin
      discovery-logikk
- [x] Tiltak 4: batch `"erdiagram-filter"`/`"plantuml-filter"` (2 modus)
      i `batch-generate-instances.py`
- [x] Tiltak 4: verifiser byte-for-byte/RDF-isomorfi for alle fire mot
      ikkje-batcha køyring (fullstendig domene-diff, `oreg`, 330 filer +
      enkeltprimitiv-verifisering av kvart steg separat før integrasjon),
      isolert feilhandteringstest for erdiagram-filter
- [x] Tiltak 4: oppdater `make/20-domain-targets.mk` — fjern
      `linkml-convert`-løkka, pek attverande fasar til nye batch-kall

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

**Attverande arbeid (etter Tiltak 1):** Tiltak 2, Tiltak 3, parallellisering
mellom batch-gruppene, og CI-måling er ikkje gjennomførte i denne runden.

## Utført (Tiltak 2 — 2026-08-07)

Implementert som planlagt: `gen-plantuml` er delt i to fasar. Fase A
(`gen-plantuml` + `filter_plantuml.py` × 2) er **uendra** — framleis éin
kontainar-triple per skjema via `run-parallel-gen.sh`, sidan denne delen
lagar per-skjema-spesifikke `.puml`-filer (ikkje eit reint linkml-API-kall
som i Tiltak 1, så det høyrer ikkje naturleg inn i `batch-generate.py`
sitt REGISTRY). Fase B er ny: **éitt** `podman run … plantuml -tsvg
<alle .puml-filer for domenet>`-kall renderer SVG for samtlege skjema i eitt
steg, i staden for eitt kall per fil (full + filtrert × N skjema).

**Nye/endra filer:**

- `src/assets/scripts/makefile/batch-render-plantuml.sh` (ny) — for kvart
  skjema i lista, sjekkar om `<name>.puml`/`<name>-filtered.puml` faktisk
  vart skrivne av Fase A (filnærvær er einaste gate — dupliserer **ikkje**
  build.yaml sin `plantuml:true`-sjekk, sidan Fase A alt handhevar han).
  Samlar opp alle funne filer og gjer eitt samla `podman run` mot
  `PLANTUML_IMAGE`. Skriv null filer → hoppar over kallet heilt (ingen tom
  kontainar-start).
- `make/10-generator-macros.mk`: `run_gen_plantuml_parallel` kallar no
  Fase A (uendra `run-parallel-gen.sh`, men SVG-render-linjene fjerna frå
  `GEN_CMD`) etterfølgt av Fase B (`batch-render-plantuml.sh`).

**Verifisert (målt lokalt, WSL2/podman, varme image-lag):**

| Domene | Skjema med `plantuml: true` | Før (per-fil render) | Etter (batcha) | Gevinst |
|---|---|---|---|---|
| `oreg` | 2 | 31 s | 24 s | **−23 %** |
| `ap-no` | 7 (20 filer inkl. raw) | — (ikkje målt separat før Tiltak 2) | 33 s (Fase A 20,6s + Fase B **8,0s for 20 filer**) | — |

**Merk kvifor dette tiltaket VISER veggklokkegevinst lokalt, i motsetnad
til Tiltak 1** (som ikkje gjorde det, jf. eige avsnitt der): Tiltak 1
batcha arbeid som **allereie var fullt overlappa** av `xargs -P16` i den
gamle arkitekturen (schema-parallelt, ingen ekstra struktur å vinne på
lokalt med 16 kjernar tilgjengeleg). Tiltak 2 er strukturelt annleis — før
denne endringa var SVG-renderinga **inne i** kvart skjema sin eigen
parallelle kritiske sti (2 ekstra sekvensielle podman-kall per skjema,
lagt til slutt i kvar sin xargs-jobb), så total kritisk sti = det
tregaste skjemaet sin EIGEN render-tid. Etter endringa er rendering flytta
**ut** av per-skjema-kritisk-sti og inn i eitt konsolidert steg — alle
skjema sine renderingar deler no éin JVM-/kontainar-oppstart i staden for
at kvart skjema sin parallelle gein må vente på sine eigne to. Dette er ei
ekte strukturell endring (ikkje berre sekvensialisert import-amortisering
som i Tiltak 1), og gjev difor målbar gevinst sjølv med rikeleg lokal
kjernetilgang.

**Semantisk verifisering:** samanlikna alle `.puml`/`.svg`-filer
byte-for-byte mot ei ikkje-batcha (per-fil-render) køyring —
**`oreg`: 10/10 filer identiske. `ap-no`: 50/50 filer identiske.**
SVG-rendering er (i motsetnad til `gen-shacl`/`gen-rdf`, jf. Tiltak 1) ikkje
underlagt blanknode-non-determinisme — byte-diff er eit gyldig
identitetskriterium her.

**Feilhandtering verifisert eksplisitt** (spec-krav, steg 3): testa eit
batch-kall med éin gyldig og éin bevisst øydelagd `.puml`-fil.
PlantUML-biletet **fullfører framleis rendering av den gyldige fila**
(skriv korrekt SVG) OG skriv ei eiga feil-SVG for den øydelagde fila, men
returnerer exit-kode ≠ 0 for heile kallet. `batch-render-plantuml.sh` sin
`set -euo pipefail` + `trap ERR` fangar dette og **feilar heile
byggesteget** (ingen stille feil) — PlantUML sin eigen feilmelding («Error
line N in file: …») går til stderr (ikkje undertrykt av
`> /dev/null`, som berre gjeld stdout) og identifiserer konkret kva fil som
var øydelagd, sjølv utan per-skjema-isolert feilmelding frå vårt eige
script.

**Avvik frå opphavleg plan:** ingen — implementert nøyaktig som skissert.

**Testa:**
- `make gen-plantuml DOMAIN=oreg` og `make gen-plantuml DOMAIN=ap-no` —
  begge fullførte med exit-kode 0.
- `make -n` (dry-run) verifisert for både frittståande
  `gen-plantuml SCHEMA=...`-target og `domain-<domain>`-pipelinen —
  begge kallar `batch-render-plantuml.sh` korrekt.
- Isolert feilhandteringstest (god + øydelagd `.puml` i same batch) —
  stadfesta partial-success-skriving + korrekt heil-feil-signalisering.

**Attverande arbeid (etter Tiltak 2):** Tiltak 3, parallellisering mellom
batch-gruppene, og CI-måling er ikkje gjennomførte i denne runden.

## Utført (Tiltak 3 — 2026-08-07)

Implementert som planlagt for alle fire scripta: `gen-docgen-examples.py`,
`generate-informasjonsmodell.py`, `gen-openapi.py`, `gen-asyncapi.py`.
Alle fire er UENDRA i åtferd (framleis brukbare frittståande éin-skjema-
CLI-ar) — eit nytt orkestreringsskript importerer dei reine funksjonane
deira og løkkar over N skjema i same prosess.

**Nye/endra filer:**

- `src/assets/scripts/makefile/batch-generate-instances.py` (ny) —
  REGISTRY-liknande dispatcher (`--generator docgen-examples|openapi|
  asyncapi|informasjonsmodell`). Importerer kvart underliggjande script
  med `importlib.util.spec_from_file_location` (handterer bindestrek-i-
  filnamn). Kvar `run_*`-funksjon replikerer run-parallel-gen.sh sin
  filtreringssemantikk eksplisitt (build.yaml-flagg-gating via
  `filter_enabled()`, `--check-suffix schema.json`-gating via
  `json_schema.is_file()`, same «ÅTVARING: … finst ikkje»-melding),
  isolerer feil per skjema (eitt skjema sin feil stoppar ikkje resten av
  batchen — matchar Tiltak 1/2 sitt etablerte mønster), og batchar
  `openapi-spec-validator` saman med sjølve openapi-genereringa (same
  python-pytest-image, ingen ekstra kontainar) ved å kalle
  `openapi_spec_validator.__main__.main()` sitt Python-API direkte
  (fangar `SystemExit` per skjema, same «kall verktøyet sin eigen
  main()»-mønster som batch-generate.py sin Click-baserte tilnærming i
  Tiltak 1, men her eit vanleg argparse-`main(args)`, ikkje eit
  Click-`Command`).
- `src/assets/scripts/makefile/gen-docgen-examples.py`: reint refaktorert
  (åtferd uendra) — per-skjema-kroppen flytta frå `main()` til ein ny
  `process_schema(schema_path, example_path, out_dir)`-funksjon, slik at
  `batch-generate-instances.py` kan importere og kalle henne direkte.
  `main()` kallar no berre `process_schema()` — verifisert identisk
  standalone-CLI-åtferd.
- `make/10-generator-macros.mk`: `run_gen_doc_parallel` delt i Fase A
  (batcha `docgen-examples`) + Fase B (uendra per-skjema `gen-doc`-CLI +
  sed-opprydding, sidan `gen-doc` skriv til ein katalog og krev framleis
  éin kontainar per skjema). `run_gen_openapi_parallel` er no éin einaste
  batcha kall (generering + validering saman). `run_gen_asyncapi_parallel`
  delt i Fase A (batcha generering) + Fase B (uendra `asyncapi validate`,
  MEDVITE ikkje batcha — sjå grunngjeving under).
- `make/30-instances.mk`: `run_gen_informasjonsmodell_instance_parallel`
  er no éin batcha kall for heile skjemalista.

**Medvite ikkje batcha: `asyncapi validate`.** Node.js-CLI-et
(`ASYNCAPI_IMAGE`) er eit heilt anna image enn generatorskripta (python-
pytest), og kan difor ikkje delta i den same in-process-batchinga. Berre
**1 skjema i heile repoet** (`samt-bu`) har `asyncapi: true` i dag — det
finst difor ingenting å batche i praksis, same grunngjeving som «Ikkje eit
tiltak: gen-xsd» i spec-hovuddelen. Fase B for asyncapi held difor fram
uendra (éin kontainar per skjema via run-parallel-gen.sh), men er no
åtskild frå Fase A (generering), som sjølv batchar korrekt for framtidige
fleir-skjema-scenario.

**Verifisert (målt lokalt, WSL2/podman, varme image-lag):**

Semantisk ekvivalens for alle fire generatorane, verifisert med
byte-for-byte-diff mot ikkje-batcha (frittståande CLI-) køyring:

| Generator | Testa mot | Resultat |
|---|---|---|
| `informasjonsmodell` | `oreg` (2 skjema) + `samt-bu` (mot committa manifest) | Byte-identisk |
| `docgen-examples` | `oreg` (2 skjema, 30 splitta eksempelfiler) | Byte-identisk, CLI-refaktoreringa endra ingenting |
| `openapi` (generering + validering) | `oreg` (2 skjema) | Byte-identisk, `openapi-spec-validator: OK` begge vegar |
| `asyncapi` (berre generering) | `samt-bu` (einaste aktiverte skjema) | Byte-identisk |

**Feilisolasjon verifisert eksplisitt for `openapi`:** kalla
`openapi_spec_validator.__main__.main()` direkte mot ein bevisst ugyldig
spec (manglande obligatorisk `version`-felt) — stadfesta at funksjonen
kastar `SystemExit(1)` med feilmeldinga fanga korrekt, som batch-scriptet
omset til ein per-skjema-isolert feil (loggar, tel opp, held fram med
neste skjema, feilar heile steget til slutt) — ingen stille feil, ingen
krasj som stoppar resten av batchen.

**Full domene-integrasjonstest:** `make domain-oreg` (alle steg, inkl.
Tiltak 1+2+3 saman) — fullførte med exit-kode 0, alle 6 batch-steg
(informasjonsmodell, docgen-examples, openapi, pluss dei 8 frå Tiltak 1 og
plantuml-fasane frå Tiltak 2) synleg i loggen med korrekt per-skjema-
timing. `make domain-samt` (einaste domenet med `asyncapi: true`) —
stadfesta at Fase A (`gen-asyncapi`, batcha) → Fase B
(`asyncapi-validate`, uendra) rekkjefølgja fungerer i full pipeline-
kontekst, og at `generate-informasjonsmodell.py` sin
`discover_artifacts()`-funksjon korrekt fann det nygenererte
`*-openapi.yaml`-artefaktet (stadfester at kryss-generator-rekkjefølgja i
`domain_target` — openapi/asyncapi før informasjonsmodell-instans — held
seg riktig etter omstruktureringa).

**Uhell undervegs, retta:** under oppryddinga etter `make domain-samt`-
testen sletta eg ved eit mistak `src/linkml/samt/samt-bu/metadata/
samt-bu-manifest.yaml` (ein `rm -rf metadata/`-vane frå `oreg`-testinga,
der tilsvarande katalog **ikkje** var committa frå før — men `samt-bu` sin
VAR det). Oppdaga umiddelbart via `git status`, gjenoppretta med
`git checkout --`, og verifiserte separat at ein fersk regenerering av
same fil er byte-identisk med den committa versjonen (`git diff --stat`
tomt output). Ingen tapt endring, men eit godt døme på kvifor
`git status` bør sjekkast før og etter opprydding av testartefaktar i eit
repo der nokre `generated`-liknande katalogar (`metadata/`) faktisk ER
committa kjeldedata, ikkje reint byggoutput.

**Testa:**
- `make -n` (dry-run) verifisert for alle fire generator-måla
  (`gen-informasjonsmodell-instance`, `gen-openapi`, `gen-asyncapi`,
  `gen-docs`) — korrekt batcha kommandolinje generert i alle tilfelle.
- `make gen-docs DOMAIN=oreg` — isolert test av Fase A/B-splitten.
- `make domain-oreg`, `make domain-samt` — fulle domene-integrasjonstestar,
  begge exit-kode 0.
- Isolert feilhandteringstest for `openapi-spec-validator` (ugyldig spec).

**Attverande arbeid (etter Tiltak 3):** parallellisering mellom batch-
gruppene, og CI-måling er ikkje gjennomførte.

## Utført (Tiltak 4 — 2026-08-07)

Implementert som planlagt for alle fire attverande generatorane
(`linkml-convert`, `gen-erdiagram`, `gen-plantuml` Fase A, `gen-doc`
Fase B). Alle 11 generator-«kind»-namn i `batch-generate.py` sitt REGISTRY
(dei 8 frå Tiltak 1 + `erdiagram`/`plantuml`/`doc`) og alle 7 i
`batch-generate-instances.py` (dei 4 frå Tiltak 3 +
`erdiagram-filter`/`plantuml-filter`/`convert`) brukar no det same
Click-drivne in-process-mønsteret som vart etablert og verifisert i
Tiltak 1.

**Nye/endra filer:**

- `src/assets/scripts/makefile/filter_plantuml.py`,
  `filter_erdiagram.py`: refaktorert frå flate modul-nivå-script (ingen
  `main()`, `global`-basert tilstand) til `process_file(...) -> str`-
  funksjonar med lokal tilstand (`nonlocal` i staden for `global`), pluss
  ein tynn CLI-kompatibel `main()`. Verifisert standalone-CLI-åtferd
  uendra FØR batch-integrasjonen vart testa.
- `src/assets/scripts/makefile/batch-generate.py`: `GeneratorSpec` utvida
  med tre nye, valfrie felt — `extra_argv_fn` (per-skjema-argv-bygging med
  biverknad, t.d. mkdir), `post_fn` (etterhandsaming etter vellukka kall,
  t.d. sed-erstatning), `out_subdir` (for `gen-plantuml` sin
  `diagrams/`-underkatalog). Nye REGISTRY-oppføringar: `erdiagram`
  (`--no-mergeimports`, skriv `-erdiagram-raw.md`), `plantuml` (skriv
  `diagrams/-raw.puml`), `doc` (`out_suffix=None` — DocGenerator skriv
  sjølv til katalog via eigne `-d`/`--example-directory`-flagg bygde av
  `extra_argv_fn`, opprydding via `post_fn`).
- `src/assets/scripts/makefile/batch-generate-instances.py`: tre nye
  `run_*`-funksjonar — `run_erdiagram_filter`/`run_plantuml_filter`
  (importerer dei refaktorerte filter-scripta, same per-skjema-isolasjon
  som resten av fila) og `run_convert` (importerer
  `linkml.converter.cli:cli`, les jobbar frå ei TSV-fil via nytt
  `--jobs-tsv`-flagg — attributta til `main()` sin argparse, sidan
  `convert`-jobbar ikkje er ei enkel skjemaliste). `_import_from_path()`
  fekk ein kritisk fiks (sjå eige avsnitt under).
- `make/10-generator-macros.mk`: `run_gen_doc_parallel` er no HEILT
  batcha (ingen `run-parallel-gen.sh`-fase att for gen-doc).
  `run_gen_erdiagram_parallel` er tre fasar (batcha generering → per-
  skjema awk, framleis host-køyrt/ubatcha sidan han aldri kosta noko → batcha
  filter). `run_gen_plantuml_parallel` er no tre fasar (batcha generering
  → batcha filter, ny → batcha SVG-render frå Tiltak 2).
- `make/20-domain-targets.mk`: `linkml-convert`-steget bytt frå ei
  manuell `while read`-løkke (éin kontainar per eksempelfil) til å skrive
  `convert-examples.sh` sin jobbliste til ei mellombels TSV-fil
  (`$(GEN_DIR)/.convert-jobs.XXXXXX`, sletta etterpå) og gjere **eitt**
  batcha kall — hoppar over kallet heilt dersom jobblista er tom (unngår
  ein unødvendig tom kontainar-start for domene utan konverterbare
  eksempel).
- `make/README.md`: oppdatert til å nemne dei nye kinda.

**Avvik frå opphavleg plan:** `GeneratorSpec` fekk **tre** nye felt
(`extra_argv_fn`, `post_fn`, `out_subdir`), ikkje det eine
`writes_directory`-feltet som vart skissert i spec-planen. Grunngjeving,
avdekt undervegs: `out_suffix=None` (alt eksisterande, brukt av `merge`)
dekte allereie «diskarder run_click()-returverdien»-semantikken `doc`
treng — den reelle nye kompleksiteten var **å bygge dei rette CLI-flagga**
(`--template-directory`, `--example-directory <per-skjema-sti>`, `-d
<per-skjema-sti>`) og **rydde opp etterpå** (sed-erstatninga), ikkje sjølve
skrivemåten. To presist namngjevne, valfrie felt (brukt av éin einaste
REGISTRY-oppføring kvar) vurderast som minimal nok utviding, i tråd med
spec-planen sitt uttrykte mål om å ikkje komplisere REGISTRY-et for dei 10
andre, uendra oppføringane.

### Kritisk bug avdekt og retta undervegs: dataclass-import via `importlib.util` krasjar utan `sys.modules`-registrering

`batch-generate-instances.py` sin `_import_from_path()`-hjelpar (etablert i
Tiltak 3 for bindestrek-namngjevne script) kasta
`AttributeError: 'NoneType' object has no attribute '__dict__'` når
`run_convert()` prøvde å importere `batch-generate.py` (for å gjenbruke
`run_click()`). Rotårsak: `batch-generate.py` sin `GeneratorSpec` brukar
`@dataclass`, og `dataclasses` sin interne typeoppløysing slår opp
`sys.modules[cls.__module__]` — men eit modulobjekt bygd via
`importlib.util.module_from_spec()` er **ikkje** automatisk registrert i
`sys.modules` før `exec_module()` er kalla, med mindre ein eksplisitt
gjer det sjølv. Retting: `sys.modules[module_name] = module` lagt til
**før** `spec.loader.exec_module(module)` i `_import_from_path()` — ein
éin-linjes, standard Python-idiom for dynamiske modulimportar, no
verifisert naudsynt her (ikkje berre defensiv kode). Påverkar alle
kallarar av `_import_from_path()`, ikkje berre `run_convert()` — retta éin
stad.

**Verifisert (målt lokalt, WSL2/podman, varme image-lag):**

Kvart nytt steg vart FØRST verifisert isolert (byte-for-byte mot ekte
CLI-subprosess-output) FØR integrasjonstesten:

| Steg | Testa mot | Resultat |
|---|---|---|
| `doc` (rå Click-invokering, katalog-skrivande) | `oreg` (60 `.md`-filer, med eksempel via `docgen-examples`) | `diff -rq` — 0 skilnader |
| `erdiagram` (rå generering) | `oreg` | Byte-identisk |
| `plantuml` (rå generering) | `oreg` | Byte-identisk |
| `erdiagram-filter` | `oreg` | Byte-identisk mot refaktorert `filter_erdiagram.py` sin eigen CLI |
| `plantuml-filter` (2 modus) | `oreg` | Byte-identisk **etter** ein fiks (manglande avsluttande linjeskift — sjå under) |
| `convert` | `oreg` | Byte-identisk |

**Mindre bug avdekt og retta:** `plantuml-filter` sin første
implementasjon skreiv `process_file()` sin returverdi direkte til fil,
men glømte at CLI-en sin `main()` brukte `print(...)`, som legg til eit
avsluttande linjeskift `process_file()` sjølv ikkje inkluderer. Avdekt
ved byte-diff (1 linje differanse: «No newline at end of file»), retta
ved å leggje til `+ "\n"` i skrivestegen. `erdiagram-filter` trong ingen
tilsvarande fiks sidan `filter_erdiagram.py` sin `process_file()` alt
bakar inn alle tre opphavlege `print()`-linjeskifta strukturelt i
returverdien.

**Full domene-integrasjonstest (`oreg`, mot ei uavhengig, fullstendig
attståande baseline):** bygde ei FERSK, sjølvstendig baseline ved å
reversere `make/10-generator-macros.mk`, `make/20-domain-targets.mk` til
committa `HEAD` (som på dette tidspunktet var Tiltak 1+2+3, committa av
brukaren mellom øktene — IKKJE Tiltak 4), køyrde `make domain-oreg` reint,
tok vare på resultatet, gjenoppretta Tiltak 4-endringane, køyrde
`make domain-oreg` på nytt, og samanlikna heile `generated/oreg/`
fil-for-fil (byte-diff for dei fleste filtypar, RDF-graf-isomorfi for
`.ttl`, jf. Tiltak 1 sin grunngjeving for kvifor byte-diff ikkje er eit
gyldig kriterium for `gen-shacl`/`gen-rdf`-output):

- **330 felles filer.** Berre **6 avvik** — nøyaktig dei same 6 kjende,
  harmlause avvika som Tiltak 1 sin verifisering fann (2× embedda
  `generation_date`-tidsstempel i `.jsonld`/`.py`, 2× kjend RDF-non-
  determinisme i `.ttl`, same triple-tal, stadfesta pre-eksisterande og
  ikkje-relatert til denne endringa).
- **2 nye filer** (berre i den nye arkitekturen):
  `<name>-erdiagram-raw.md` — venta og korrekt: den nye arkitekturen
  skriv rå-linkml-output til disk FØR awk-steget (i staden for å pipe det
  direkte inn i awk utan mellomlagring, slik den gamle arkitekturen
  gjorde) — eit reint tilleggs-mellomsteg, ikkje eit tap av data.
- **0 manglande filer.**

**Feilisolasjon verifisert eksplisitt for `erdiagram-filter`:** batcha eit
gyldig og eit bevisst øydelagd skjema (ugyldig YAML) i same kall —
stadfesta at det gyldige skjemaet framleis produserer korrekt output,
feilen for det øydelagde skjemaet vert logga synleg (ikkje stille,
inkluderer den faktiske YAML-parse-feilen), og skriptet returnerer
korrekt feil-exit-kode for heile batchen.

**Veggklokketid:** `oreg` (2 skjema) — baseline (Tiltak 1-3) 176 s, etter
Tiltak 4 172 s. Ingen målbar endring, same forklaring som Tiltak 1: denne
sandkassa har 16 lokale CPU-kjernar, langt fleire enn dei 2 skjemaa i
`oreg`, så den gamle arkitekturen sin xargs-parallellitet var alt nær
optimal her. Same atterhald som før: den reelle gevinsten (færre
kontainar-oppstartar, mindre CPU-kontensjon) er venta å vise seg tydelegare
på ein ressurs-avgrensa CI-runner, ikkje nødvendigvis i denne lokale
målinga.

**Testa:**
- Alle 11 (`batch-generate.py`) + 7 (`batch-generate-instances.py`)
  generator-kind testa individuelt før integrasjon.
- `make -n domain-oreg` (dry-run) — stadfesta korrekt batcha kommandolinje
  for kvart steg, inkludert den nye `linkml-convert`-TSV-mekanismen.
- `make domain-oreg` — fullt, uavhengig før/etter-samanlikna
  integrasjonstest (sjå over).
- Isolert feilhandteringstest for `erdiagram-filter`.

**Attverande arbeid (etter Tiltak 4):** parallellisering mellom
batch-gruppene og CI-måling er ikkje gjennomførte.

## Utført (Parallellisering etter batching — 2026-08-07)

Implementert som skissert i «Parallellisering etter batching»-avsnittet,
men oppdatert til å dekke ALLE gruppene som finst etter Tiltak 1-4 (avsnittet
vart opphavleg skrive før Tiltak 4 fanst og nemnde berre "3-4 grupper" —
det reelle talet no er 11 uavhengige grupper i fase 1 åleine).

**Design:** i staden for å reimplementere podman-kall i rå bash (risikabelt
— ville kravd å rekonstruere `LINKML_RUN`/`PYTHON_RUN` sine monterings-
strengar med anførselsteikn utanfor Make sin eigen `$$`-escaping, jf.
kvoteringsfellene alt dokumenterte i Tiltak 4 sitt `run_convert`-arbeid),
vart kvart steg i domain_target eit **rekursivt `$(MAKE) <target>
DOMAIN=<domene>`-kall til eit alt eksisterande, sjølvstendig verifisert
gen-*-target**. Det nye orkestreringsskriptet reimplementerer difor
ingen genereringslogikk i det heile — berre fase-rekkjefølgje,
samstundes-oppstart og feilsamling.

**Nye/endra filer:**

- `src/assets/scripts/makefile/run-domain-pipeline.sh` (ny) — tek imot eit
  domenenamn, startar Fase 1 (11 uavhengige grupper: `gen-linkml-merge`,
  `gen-jsonld-context`, `gen-shacl`, `gen-python`, `gen-jsonschema`,
  `gen-owl`, `gen-rdf`, `gen-proto`, `gen-linkml-convert`, `gen-docs`
  [doc+erdiagram saman], `gen-plantuml`) som separate baksgrunnsprosessar
  via ein `run_bg()`-hjelpar (`( … ) &` + PID-array, same mønster som
  `parallelliser-domene-validering.md`), ventar **spesifikt** på
  `gen-jsonschema` (ikkje resten av fase 1) før Fase 2 (`gen-xsd`,
  `gen-openapi`, `gen-asyncapi` — alle les `<name>-schema.json`) startar,
  ventar så på ALLE attverande PID-ar (resten av fase 1 + heile fase 2),
  og køyrer til slutt Fase 3 (`gen-informasjonsmodell-instance`, som
  skannar heile `generated/<domain>/<name>/` for `finnes_i_format`-lista
  og difor må vente på absolutt alt).
- `make/11-generator-targets.mk`: ny `gen-linkml-merge`-target (wrappar
  `run_gen_linkml_parallel`, som før berre fanst som eit internt steg i
  `domain_target` — trengst no som eit frittståande mål for det rekursive
  `$(MAKE)`-kallet).
- `make/20-domain-targets.mk`: ny `gen-linkml-convert`-target (flytta
  `linkml-convert`-logikken frå å vere inline `domain_target`-kode til eit
  eige, frittståande mål, av same grunn). `domain_target` sjølv er no
  redusert til eitt `print_header` + eitt kall til
  `run-domain-pipeline.sh` — heile den tidlegare 30-linjers pipelinen er
  borte frå Makefile-et, flytta til scriptet.

**Kritisk, men ufarleg funn: GNU Make sin dry-run-oppdaging av `$(MAKE)`.**
Første `make -n domain-oreg`-testen køyrde **faktisk** heile pipelinen i
staden for å berre skrive ut kommandoane — GNU Make kjenner att `$(MAKE)`
(eller `${MAKE}`) **som tekst kvar som helst i ei recipe-linje** og
tvingar då linja til å køyre for reelt, sjølv under `-n`, for å støtte
rekursive byggjesteg. Mi eiga `MAKE="$(MAKE)"`-miljøvariabel-vidareføring
inneheldt nettopp denne understrengen. **Stadfesta ufarleg**: same
`-n`-flagget vert automatisk vidareført til dei rekursive
`$(MAKE)`-underkalla via `MAKEFLAGS`, så DEI køyrer sjølve i dry-run-modus
òg — heile kjeda skriv berre ut kommandoar, ingenting vert faktisk bygd.
Verifisert ved at ingen filer i `generated/` fekk nyare tidsstempel etter
testen.

**Verifisert (målt lokalt, WSL2/podman, varme image-lag):**

| Domene | Skjema | Før (Tiltak 1-4, sekvensielt) | Etter (parallellisert) | Gevinst |
|---|---|---|---|---|
| `oreg` | 2 | 172 s | **59 s** | **−66 %** |
| `ap-no` | 7 | 207 s (Tiltak 1-baseline; ikkje re-målt sekvensielt etter Tiltak 4) | **123 s** | minst −41 % |

**Dette er den klart største enkeltgevinsten i heile denne specen, og
den FØRSTE som viser stor lokal veggklokkegevinst utan atterhald om
CI-spesifikk kontensjon** — i motsetnad til Tiltak 1 (ingen lokal gevinst,
sidan batching berre gjorde alt-som-var-parallelt-skjult sekvensielt-i-éin-
kontainar) og Tiltak 2 (moderat lokal gevinst frå strukturell konsolidering),
skaper denne endringa **heilt ny samstundes arbeid** som **aldri fanst før i
det heile** — dei 11 fase 1-gruppene køyrde tidlegare 100 % sekvensielt som
separate Make-recipe-linjer, uavhengig av kor raske dei individuelt var
etter batching. Denne gevinsten er difor venta å halde seg (eller bli endå
større relativt) i CI, sidan han ikkje er avhengig av rikeleg lokal
kjernetilgang slik Tiltak 1 sin (manglande) gevinst var.

**Feilhandtering verifisert (utilsikta, men reelt):** første forsøket på
`make domain-oreg` feila reelt — ein forbigåande DNS-oppløysingsfeil i
`gen-rdf` (`<urlopen error [Errno -3] Try again>`, stadfesta forbigåande
ved eit isolert `gen-rdf`-attempt rett etterpå som lukkast). Dette synte
feilhandteringa i praksis: `rdf`-jobben feila synleg (ikkje stille),
`FAILED`-teljaren auka, **alle andre uavhengige fase 1/2-jobbar fullførte
framleis korrekt** (isolasjon stadfesta), og scriptet stoppa **korrekt før
Fase 3** (`gen-informasjonsmodell-instance` vart ikkje køyrd, sidan han
ville lese ufullstendige/manglande RDF-artefakter). Retry lukkast fullt ut.

**Korrektheit verifisert:** `gen-informasjonsmodell-instance` (Fase 3) sin
`finnes_i_format`-liste inneheldt **alle** 7 forventa artefakttypar
(context.jsonld, ontology.ttl, openapi.yaml, schema.json, schema.proto,
schema.ttl, shapes.ttl) etter den vellukka `oreg`-køyringa — stadfestar at
Fase 3 korrekt ventar på at ALT frå Fase 1+2 er skrive før han les
`generated/`-katalogen, ingen race condition.

**Testa:**
- `make -n domain-oreg` — stadfesta korrekt fase-rekkjefølgje (json-schema
  ventast på spesifikt, xsd/openapi/asyncapi startar rett etter,
  informasjonsmodell-instance sist).
- `make domain-oreg` × 2 (éin feila forbigåande, éin lukkast) — stadfesta
  både feilisolasjon/-stopp og fullt vellukka køyring.
- `make domain-ap-no` (7 skjema, større domene) — vellukka, ingen feil,
  korrekt filtal.
- Manuell inspeksjon av `finnes_i_format` for race-condition-fri Fase 3.

**Ikkje testa/gjenstår:** CI-måling (reell gevinst på ein ressurs-avgrensa
runner, venta minst like stor som lokalt målt sidan denne gevinsten ikkje
avheng av rikeleg kjernetilgang, jf. drøftinga over) — det einaste
attverande punktet i heile specen sin opphavlege handlingsliste.
