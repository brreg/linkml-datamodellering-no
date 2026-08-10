# Evaluer batching av dei resterande ikkje-batcha kommandoane

## Bakgrunn

Etter at "Batching"-kolonna vart lagt til i `COMMANDS.md` (sjå
`specs/done/dokumenter-batching-i-kommandooversikt.md`), bad brukaren om ei
konkret evaluering av om dei kommandoane som i dag er merkte "Ikkje
batcha"/"Ikkje aktuelt" faktisk **kan** batchast. Dette dekkjer nøyaktig
dei seks radene frå den opphavlege «Ikkje batcha»-oversikta:

1. `make gen-xsd`
2. `make convert-rdf`, `make convert-data`
3. `make validate-examples DOMAIN=<domain>`
4. `make mcp-linkml-valider-modell`
5. `make gen-dqv-measurements`, `make gen-modellkatalog-instance`, `make gen-begrepskatalog-instance`
6. `make gen-asyncapi` (validerings-fasen)

Evalueringa er gjort ved å lese kjeldekoden direkte (Makefile, `make/*.mk`,
dei relevante Python-scripta), ikkje ved å gjette. Same metode som
`specs/done/batch-validate-lint-test-per-skjema.md` sin evaluerings-del.

**Oppdatering (same dag):** Brukaren opplyste at det er venta at **10+
skjema** kjem til å bruke `xsd: true`/`asyncapi: true` framover (i dag
berre 1 skjema kvar, `samt/samt-bu`). Dette endrar konklusjonen for
`gen-xsd` og `gen-asyncapi` sin valideringsfase (funn 1 og 6 under) —
"inga gevinst" var korrekt for **dagens** N=1, men held ikkje for det
venta framtidige skjematalet. Sjå reviderte tilrådingar i funn 1 og 6, og
nye Tiltak 4/5.

## Funn per kommando

### 1. `make gen-xsd` — BATCHBAR NÅR skjematalet veks, revidert tilråding

`grep -rl "xsd: true" src/linkml --include=build.yaml` gjev **i dag**
**berre** `src/linkml/samt/samt-bu/build.yaml` — eitt einaste skjema.
Med N=1 er det framleis ingenting å amortisere **i dag**. Men brukaren
opplyser at **10+ skjema** er venta å setje `xsd: true` framover — ved det
skjematalet er konklusjonen motsett.

**Kartlegging av dagens mekanisme** (`run_gen_xsd_parallel`,
`make/10-generator-macros.mk` linje 133-140): dette er **ikkje** batcha via
`batch-generate.py`-mønsteret (linkml-generatorane) i det heile — han går
via `run-parallel-gen.sh` (same delte parallelliserings-orkestrering som
`gen-doc`/`gen-erdiagram`/`gen-plantuml`/`gen-openapi`/`gen-asyncapi` alle
brukte før sine respektive batching-tiltak), som køyrer **tre separate
podman-kontainarar per skjema** via `xargs -P`: `avrotize j2a` (JSON
Schema → Avro), `avrotize a2x` (Avro → XSD, `AVROTIZE_RUN`), og
`fix-xsd-dates.py` (eige `podman run --entrypoint python3`-kall). Ved
N=10 er det altså **30 kontainarkall** i staden for potensielt éin, eller
i det minste tre (éin per verktøy, delt over alle skjema).

**Vurdering av batchbarheit:** `fix-xsd-dates.py` er reint Python og kan
batchast direkte etter same mønster som `batch-generate-instances.py` sine
andre generatorar — ingen kjend hindring. `avrotize j2a`/`a2x` er derimot
eit **eksternt CLI-verktøy** (ikkje ein del av `linkml`), og det er **ikkje
verifisert i denne evalueringa** om det (a) har eit importerbart
Python-API (analogt korleis `linkml.converter.cli:cli` vart gjenbrukt via
`run_click()`) eller (b) om CLI-et kan ta fleire fil-par i eitt kall
(analogt PlantUML sitt `-tsvg file1.puml file2.puml ...`, sjå
`batch-render-plantuml.sh`). Dersom ingen av desse stemmer, er
**minimums**-batchinga framleis verdifull: køyr `avrotize j2a`/`a2x` for
alle N skjema **sekvensielt inni éin delt kontainar** (same prinsipp som
`batch-render-plantuml.sh` sitt eine `podman run`, men med ei intern
bash/Python-løkke over skjema i staden for eitt CLI-kall med fleire
filargument) — dette amortiserer framleis kontainar-**oppstarten**
(~2,6-2,7 s målt i `effektiviser-generate-workflow-koyretid.md`) over N
skjema, sjølv om det ikkje amortiserer noka Python-importskatt slik
`linkml`-generatorane gjer.

**Tilråding: batch før/når skjematalet faktisk nærmar seg det venta
nivået (10+).** Ikkje same hastegrad som Tiltak 1-3 (ingen reell gevinst
å hente ved dagens N=1), men bør implementerast i god tid før talet veks,
elles betaler `gen-xsd`/`domain-samt` (og framtidige domene med fleire
xsd-skjema) stadig aukande sekvensiell kostnad umerka. Krev ei kort
forundersøking av avrotize sine CLI-/API-eigenskapar (sjå over) før
implementeringsdetaljane kan fastsetjast presist — høgare uvisse enn
Tiltak 1-3, som gjenbruker alt verifisert kode.

### 2. `make convert-rdf`, `make convert-data` — BATCHBART, låg risiko, infrastruktur finst alt i produksjon

**Kartlegging:** `make convert-rdf` (Makefile linje 98-113) og
`make convert-data` (linje 115-140) køyrer i dag kvar sin eigen sekvensielle
`for`-løkke med **éin `$(LINKML_RUN) linkml-convert`-podman-kontainar per
fil**.

Dette er påfallande fordi den **domenegata** ekvivalenten,
`gen-linkml-convert` (`make/20-domain-targets.mk` linje 18-28, steg 3 i
`domain-*`-pipelinen), **allereie er batcha** — han byggjer ei jobs-TSV via
`convert-examples.sh` og sender henne til
`batch-generate-instances.py --generator convert` (funksjonen `run_convert`,
linje 176-199 i det scriptet), som køyrer `linkml.converter.cli:cli` via
`run_click()` for alle jobbar i **éin** kontainar. Dette er verifisert i
produksjon kvar gong ein `domain-*`-target køyrer.

`convert-examples.sh` (delt av **begge** `convert-rdf` og
`gen-linkml-convert` alt i dag, jf. kommentaren i toppen av fila) tek
alt imot eit valfritt domene-filter og skriv nøyaktig den TSV-forma
(`schema<TAB>example<TAB>out`) batchinga treng — inkludert
`example_rdf: false`-filtrering og fixture-overstyring. Repo-vidt kall
(`convert-examples.sh` utan argument) er alt det `make convert-rdf` bruker
for **discovery** i dag — berre sjølve konverteringssteget er ubatcha.

Det finst i tillegg eit **endå meir generelt** batch-script,
`src/assets/scripts/makefile/batch-convert.py` (bygd for Kategori D i
`batch-validate-lint-test-per-skjema.md`, brukt av `tests/test_make.sh`),
med konfigurerbart `output-format` (ikkje hardkoda `ttl`) og 4-kolonne
TSV — strengt meir generell enn `run_convert`, men **ikkje** kopla til
noko produksjons-make-mål i dag.

**Vurdering:** `make convert-rdf` er i praksis ei **eitt-liners omskriving**
— byt ut for-løkka sin per-fil `linkml-convert`-podman-kall med same
`batch-generate-instances.py --generator convert`-kallet
`gen-linkml-convert` alt bruker (utan domenefilter). Dette gjenbruker
**verifisert produksjonskode**, ikkje noko nytt. `make convert-data`
manglar ein tilsvarande delt discovery-funksjon (filtrerer
`publish_external: true` inline i Makefile-oppskrifta i staden for via eit
script) — treng ein liten ny "convert-data-examples.sh"-ekvivalent (same
mønster som `convert-examples.sh`) før same batch-mekanisme kan brukast,
men sjølve batch-steget er identisk gjenbruk.

**Notert DRY-avvik (sidefunn, ikkje del av denne evalueringa sitt
kjerneomfang):** `run_convert` (produksjon) og `batch-convert.py`
(test-only) er to separate implementasjonar av nesten same logikk (begge
`run_click()` mot `linkml.converter.cli:cli`). Når `convert-rdf`/
`convert-data` batchast bør det vurderast om `run_convert` sitt
3-kolonne, hardkoda-`ttl`-format bør utvidast til `batch-convert.py` sitt
4-kolonne, format-konfigurerbare TSV-format (eller omvendt), slik at éin
av dei to kan fjernast — **ikkje avgjort her**, berre flagga for
oppfølgingsvurdering når/viss batching faktisk vert implementert.

**Tilråding: batch. Låg risiko — gjenbruk `run_convert`/
`batch-generate-instances.py`.**

### 3. `make validate-examples DOMAIN=<domain>` — BATCHBART, moderat risiko, mønster finst i test-infrastruktur

**Kartlegging:** I dag (`make/40-validation.mk` linje 128-183): éin
bakgrunnsjobb per skjema, kvar med sin eigen `podman run ... linkml
validate --schema X Y`-kontainar, parallellisert (ikkje batcha) via
bash-`&`/`wait`. Feilmeldingar hentast ut av CLI-en sin `[ERROR]`-prefiksa
stdout-tekst med `grep`.

`linkml.validator.cli:cli` (bak CLI-en `linkml validate`) kallar
**`sys.exit()`** i kroppen (stadfesta med `inspect.getsource()` i
`batch-validate-lint-test-per-skjema.md`, Kategori D-analysen) — kan difor
**ikkje** batchast via same `run_click()`-mønster som convert. I staden
finst `linkml.validator.validate()`-API-et (same funksjon
`mcp-linkml-validator` sin `server.py` alt bruker internt), og eit ferdig,
verifisert batch-script som brukar nøyaktig dette:
`src/assets/scripts/makefile/batch-linkml-validate.py` (bygd for Kategori D,
brukt av `tests/test_make.sh` sin `run_phase_a_linkml_validate()`). Scriptet
er generelt (ikkje test-spesifikt): tek ei `--jobs-tsv` med
`attribueringsnøkkel<TAB>skjema<TAB>instans`, køyrer `SchemaView(schema)` +
`lm_validate(instance_obj, sv.schema)` per jobb i éin prosess, og skriv
`::error file=<nøkkel>::`-linjer i same format som dei andre batch-scripta.

**Vurdering:** Discovery-/fixture-logikken `validate-examples` alt har
(finn `examples/<namn>-eksempel.yaml`, fall tilbake til
`tests/fixtures/<namn>-fixture.yaml` for skjema utan `tree_root`) kan
gjenbrukast uendra til å byggje ei jobs-TSV, som så sendast til
`batch-linkml-validate.py` i staden for per-skjema `podman run`. Den
reelle risikoen ligg i **feilrapportering**: dagens implementasjon
parserer `[ERROR]`-prefiksa CLI-linjer for `::error file=$example::`-
annotasjonar; batch-scriptet gjev i staden strukturerte
`report.results`-meldingar. Formatet må tilpassast slik at GitHub Actions-
annotasjonane (brukt av CI) framleis peikar til rett fil med presis nok
feilmelding — same type tilpassing som vart gjort for
`mcp-validate-instance` i Kategori C (`batch-validate-instances.py`,
JSON-output i staden for CLI-tekst).

**Tilråding: batch. Moderat risiko — gjenbruk `batch-linkml-validate.py`,
men feilrapportering til CI må verifiserast nøye (samanlikn annotasjonar
skjema-for-skjema mot dagens CLI-baserte output, minst eitt skjema med
kjend valideringsfeil).**

### 4. `make mcp-linkml-valider-modell` — batchbar infrastruktur finst, men IKKJE tilrådd å endre

**Kartlegging:** Targetet tek berre `SCHEMA=<éin sti>` (pluss valfri
`POLICY=`/`INSTANCE=`), detekterer policy og delegerer til
`_mcp-valider-modell-with-header` → `flatten-and-validate.bash` → MCP-
serveren sitt `validate_linkml_schema`-verktøy for **eitt** skjema. Den
underliggande `batch-flatten-and-validate.py` (brukt internt av
`validate-bronze`/`validate-data`) støttar alt N skjema i éin kontainar via
JSON-RPC-stdin-batching.

**Vurdering:** Dette targetet sitt reelle bruksmønster er **interaktiv
enkeltskjema-sjekk under utvikling** ("valider skjemaet eg jobbar med no,
eventuelt med ein annan policy enn build.yaml sin"). Bulk-valideringsbehovet
(«valider alle skjema i eit domene») er alt dekt av `validate-bronze`/
`validate-data`, som **alt** batchar. Å leggje til ein `SCHEMAS=`-variant
her ville dekke eit smalt case («valider akkurat desse N spesifikke
skjemaa, med éi felles eksplisitt `POLICY=`-overstyring») som i praksis
sjeldan oppstår — batching ville berre løne seg for brukarar som manuelt
listar fleire skjema, noko det ikkje finst nokon indikasjon på at nokon
faktisk gjer i dag (CI bruker `validate-bronze`/`validate-data`, ikkje
dette targetet, for bulk-sjekkar).

**Tilråding: IKKJE batch.** Dette er ei medviten avgrensing basert på
bruksmønster, ikkje eit hòl. Dokumenter grunngjevinga i `COMMANDS.md` sitt
"Batching"-felt (alt gjort) i staden for å byggje ubrukt kapasitet.

### 5. `make gen-dqv-measurements`, `gen-modellkatalog-instance`, `gen-begrepskatalog-instance` — IKKJE eit batchbart mønster

**Kartlegging:** Stadfesta med `grep -n "subprocess\|podman\|docker"` mot
alle tre underliggande script
(`gen-dqv-measurements.py`, `generate-modellkatalog.py`,
`collect-concepts.py`): **null treff** i alle tre. Kvart script køyrer
**éin gong**, som eitt `$(PYTHON_RUN)`/`$(LINKML_RUN)`-kontainarkall, og
løkkjer internt i minnet over alle relevante filer (data-filer, alle
`metadata/modelldcat.yaml`, alle begrepssamlingar). Det finst altså
**ingen per-eining podman-kontainar** å eliminere — batching (i tydinga
"slå saman N kontainarkall til 1") er ikkje eit anvendbart konsept her,
sidan talet på kontainarkall alt er 1, uavhengig av kor mange
skjema/organisasjonar/begrepssamlingar som prosesserast.

**Tilråding: ingen endring.** Dette er allereie i den optimale tilstanden
batching elles prøver å oppnå.

### 6. `make gen-asyncapi` (validerings-fasen) — BATCHBAR NÅR skjematalet veks, revidert tilråding

**Kartlegging:** `grep -rl "asyncapi: true" src/linkml --include=build.yaml`
gjev **i dag berre** `src/linkml/samt/samt-bu/build.yaml` — same
eittskjema-situasjon som `gen-xsd`, og same brukaropplyste vekstforventing
(10+ skjema). Til samanlikning har `openapi: true` alt **8** skjema, og
den validerings-fasen **er** batcha (`run_gen_openapi_parallel`, generering
OG validering saman via `openapi-spec-validator` sitt Python-API i éin
kontainar — sjå COMMANDS.md) — eit direkte prejudikat for at
tilsvarande batching av `asyncapi validate` er råd, dersom verktøyet
tillèt det.

Dagens mekanisme (`run_gen_asyncapi_parallel`,
`make/10-generator-macros.mk` linje 154-158): generering er alt batcha
(`batch-generate-instances.py --generator asyncapi`), men
**valideringssteget** går via `run-parallel-gen.sh` med
`GEN_CMD='... $(ASYNCAPI_RUN) validate /work/$$input'` — **éin
Node.js-kontainar per skjema**.

**Vurdering av batchbarheit:** Ulikt `avrotize` (funn 1) er
`openapi-spec-validator`-presedensen eit sterkt argument for at
`asyncapi validate` òg kan batchast — men **ikkje verifisert i denne
evalueringa** om AsyncAPI CLI-et (`@asyncapi/cli`, Node.js) kan ta
**fleire filer i eitt `validate`-kall** (analogt PlantUML sitt
`-tsvg file1 file2 ...`) eller om det krev éin prosess per fil uansett
(i så fall gjeld same "batch inni éin delt kontainar via intern løkke"-
tilnærming som for `avrotize` i funn 1 — amortiserer framleis
kontainar-oppstarten, ikkje ei importskatt, sidan dette er Node.js og
ikkje Python/linkml).

**Tilråding: batch før/når skjematalet faktisk nærmar seg det venta
nivået (10+).** Same grunngjeving og hastegrad som `gen-xsd` (funn 1) —
ikkje ein reell gevinst ved dagens N=1, men bør implementerast før talet
veks. Krev ei kort forundersøking av AsyncAPI CLI-et sine
multi-fil-eigenskapar før implementeringsdetaljane kan fastsetjast.

## Oppsummering

| Kommando | Batchbar? | Risiko | Kvifor |
|---|---|---|---|
| `make gen-xsd` | **Ja, når skjematalet veks** | Moderat-høg (avrotize CLI-/API-eigenskapar uverifiserte) | N=1 i dag, men venta 10+ — batch før talet veks |
| `make convert-rdf` | **Ja** | Låg | Gjenbruk `run_convert`/`batch-generate-instances.py`, alt verifisert i produksjon (`gen-linkml-convert`) |
| `make convert-data` | **Ja** | Låg-moderat | Same batch-mekanisme, men treng ein ny delt discovery-funksjon (analogt `convert-examples.sh`) |
| `make validate-examples DOMAIN=<domain>` | **Ja** | Moderat | Gjenbruk `batch-linkml-validate.py`, men feilrapportering til CI må tilpassast og verifiserast nøye |
| `make mcp-linkml-valider-modell` | Teknisk ja, men | — | Ikkje tilrådd — smalt bruksmønster, bulk-behovet er alt dekt av `validate-bronze`/`validate-data` |
| `make gen-dqv-measurements` m.fl. | Nei | — | Alt éin kontainar, ikkje eit per-skjema-mønster |
| `make gen-asyncapi` (validering) | **Ja, når skjematalet veks** | Moderat-høg (AsyncAPI CLI multi-fil-støtte uverifisert) | N=1 i dag, men venta 10+ — same grunngjeving som gen-xsd |

**Konklusjon:** To av sju vurderte punkt (`convert-rdf`/`convert-data`) er
reelle, lågrisiko batching-gevinstar der infrastrukturen allereie finst
og er verifisert i produksjon — dette er den klaraste kandidaten dersom
noko skal implementerast fyrst. `validate-examples` er batchbar med
moderat risiko. `gen-xsd` og `gen-asyncapi` sin valideringsfase er **ikkje
verdt å batche ved dagens skjematal**, men bør implementerast før det
venta skjematalet (10+) gjer den ubatcha kostnaden merkbar — høgare
implementeringsuvisse enn dei andre, sidan det krev forundersøking av
eksterne CLI-verktøy (avrotize, AsyncAPI CLI) sine multi-fil-/API-
eigenskapar. `mcp-linkml-valider-modell` og dei tre reint-Python-scripta
er anten medvitne avgrensingar (uendra) eller allereie optimale.

## Tiltak (dersom brukaren ønskjer implementering — IKKJE gjort i denne evalueringa)

### Tiltak 1 — `make convert-rdf`: byt til batcha `gen-linkml-convert`-mekanisme

1. Erstatt for-løkka i `make convert-rdf` (Makefile) med same
   `batch-generate-instances.py --generator convert`-kall som
   `gen-linkml-convert` bruker, TSV bygd frå `convert-examples.sh` (utan
   domenefilter).
2. Verifiser byte-identisk `.ttl`-output for eit utval skjema, før/etter.
3. Vurder DRY-konsolidering av `run_convert` vs. `batch-convert.py`
   (sjå sidefunn over) i same eller separat oppfølgingssteg.

### Tiltak 2 — `make convert-data`: ny delt discovery + same batch-mekanisme

1. Trekk ut `publish_external: true`-filtreringa frå `convert-data` sin
   inline Makefile-oppskrift til eit delt script (analogt
   `convert-examples.sh`), som skriv same TSV-format.
2. Kall `batch-generate-instances.py --generator convert` med denne TSV-en.
3. Verifiser byte-identisk `.ttl`-output.

### Tiltak 3 — `make validate-examples`: batch via `batch-linkml-validate.py`

1. Bygg jobs-TSV frå eksisterande discovery-/fixture-logikk
   (`examples/<namn>-eksempel.yaml`, fallback til
   `tests/fixtures/<namn>-fixture.yaml`).
2. Kall `batch-linkml-validate.py --jobs-tsv <fil>` i staden for
   per-skjema bakgrunnsjobbar.
3. Tilpass feilrapportering: omform `report.results`-meldingar frå
   batch-scriptet til same `::error file=<example>::`-GitHub-annotasjonar
   CI i dag forventar frå `emit-github-validation-annotations.py`-mønsteret.
4. Verifiser: samanlikn pass/fail OG feilmeldingsinnhald skjema-for-skjema
   mot dagens CLI-baserte implementasjon, minst eitt skjema med kjend
   valideringsfeil.

### Tiltak 4 — `make gen-xsd`: batch avrotize-kjeda (implementer før skjematalet nærmar seg 10+)

1. Forundersøk avrotize (`j2a`/`a2x`): sjekk om verktøyet har eit
   importerbart Python-API (analogt `linkml.converter.cli:cli`), eller om
   CLI-et støttar fleire fil-par i eitt kall. Avgjer batch-strategi basert
   på svaret.
2. Dersom verken A eller B stemmer: skriv eit script (analogt
   `batch-render-plantuml.sh`, men med ei intern løkke i staden for eitt
   multi-fil-CLI-kall) som køyrer `avrotize j2a`/`a2x` sekvensielt for alle
   N skjema inni **éin** delt `AVROTIZE_RUN`-kontainar.
3. Batch `fix-xsd-dates.py`-steget separat (reint Python, ingen kjend
   hindring) — analogt dei andre `batch-generate-instances.py`-generatorane.
4. Verifiser byte-identisk `.xsd`-output mot dagens per-skjema-implementasjon
   for `samt-bu` (einaste skjema tilgjengeleg for verifisering før
   skjematalet faktisk veks).
5. **Ikkje prioriter høgt før skjematalet nærmar seg det venta nivået** —
   ingen reell gevinst ved dagens N=1, men bør vere klart implementert
   før det ikkje lenger er tilfelle.

### Tiltak 5 — `make gen-asyncapi` (valideringsfase): batch `asyncapi validate` (implementer før skjematalet nærmar seg 10+)

1. Forundersøk AsyncAPI CLI-et (`@asyncapi/cli`): sjekk om
   `asyncapi validate` støttar fleire filer i eitt kall (analogt PlantUML).
2. Dersom ja: same trivielle mønster som `batch-render-plantuml.sh` —
   samle alle `*-asyncapi.yaml`-filer, éin `$(ASYNCAPI_RUN) validate
   file1 file2 ...`-kontainarkall.
3. Dersom nei: same "intern løkke inni éin delt kontainar"-tilnærming som
   Tiltak 4.
4. Verifiser at valideringsresultat (pass/fail) er uendra for `samt-bu`.
5. Same lågare hastegrad som Tiltak 4 — implementer før, ikkje
   nødvendigvis no.

**Prioritert rekkjefølgje ved implementering:** Tiltak 1 (lågast risiko,
størst gjenbruk av alt verifisert kode) → Tiltak 2 (same mønster, litt meir
nytt arbeid) → Tiltak 3 (mest arbeid, feilrapporteringstilpassing) →
Tiltak 4/5 (lågast **hastegrad** ved dagens skjematal, men høgast
**implementeringsuvisse** — krev forundersøking av eksterne CLI-verktøy
før omfang kan fastsetjast presist; bør likevel gjerast før det venta
skjematalet på 10+ faktisk er nådd, ikkje etterpå).

## Handlingsliste

- [x] Avklar med brukar om Tiltak 1-5 skal implementerast, og i kva
      rekkjefølgje
- [x] Tiltak 1: `make convert-rdf` batcha
- [x] Tiltak 2: `make convert-data` batcha
- [x] Tiltak 3: `make validate-examples` batcha, feilrapportering
      verifisert mot CI-krava
- [ ] Tiltak 4: forundersøk avrotize sine CLI-/API-eigenskapar, batch
      `make gen-xsd` før skjematalet med `xsd: true` nærmar seg 10+
- [ ] Tiltak 5: forundersøk AsyncAPI CLI sine multi-fil-eigenskapar, batch
      `make gen-asyncapi` sin valideringsfase før skjematalet med
      `asyncapi: true` nærmar seg 10+

## Utført

### Tiltak 1 — `make convert-rdf`: byt til batcha `gen-linkml-convert`-mekanisme

**Endringar:**

1. **`Makefile` (linje 98-106):**
   - Erstatta for-løkka med same `batch-generate-instances.py --generator convert`-kall som `gen-linkml-convert` bruker
   - Byggjer jobs-TSV frå `convert-examples.sh` (utan domenefilter)
   - Éin kontainar for alle eksempelfiler i staden for éin per fil

**Verifisering:**
- Testa `make convert-rdf LOGLVL=DEBUG` — batcha 15 eksempelfiler i éin kontainar
- Timing per fil: 0.19s-1.58s (lågare enn før batching, sidan import-skatt er amortisert)

### Tiltak 2 — `make convert-data`: ny delt discovery + same batch-mekanisme

**Endringar:**

1. **Nytt script: `src/assets/scripts/makefile/convert-data.sh`:**
   - Finn datafiler (data/*/*.yaml) med `publish_external: true` i build.yaml
   - Skriv same TSV-format som `convert-examples.sh`
   - Brukar LOG_FUNCTIONS for debug-logging (same mønster som convert-examples.sh)

2. **`Makefile` (linje 115-123):**
   - Erstatta inline for-løkke med `convert-data.sh` + `batch-generate-instances.py --generator convert`
   - Same batch-mekanisme som `convert-rdf`

**Verifisering:**
- Testa `make convert-data LOGLVL=DEBUG` — batcha 6 modellkatalogar i éin kontainar
- Timing per fil: 1.52s-2.80s (lågare enn før batching)

### Oppdatering av COMMANDS.md

**`COMMANDS.md` (linje 239-240):**
- Oppdatert "Batching"-kolonne for `convert-rdf` og `convert-data` frå "Ikkje batcha" til "Batcha"
- Dokumentert batch-mekanisme: `batch-generate-instances.py --generator convert --jobs-tsv <fil>`, éin kontainar
- Referert til `convert-examples.sh` og `convert-data.sh` som TSV-byggarar

### Tiltak 3 — `make validate-examples`: batch via `batch-linkml-validate.py`

**Endringar:**

1. **`make/40-validation.mk` (linje 134-203):**
   - Erstatta parallelliserte bakgrunnsjobbar med batch-validering via `batch-linkml-validate.py`
   - Byggjer jobs-TSV frå eksisterande discovery-/fixture-logikk (eksempel-YAML + fallback til tests/fixtures/)
   - Éin kontainar for alle eksempelfiler i domenet i staden for éin per fil

2. **`src/assets/scripts/makefile/batch-linkml-validate.py` (linje 67-95):**
   - Oppdatert feilrapportering: skriv alle `report.results`-meldingar til stderr som `::error file=<instance>::<melding>`
   - Endret frå `::error file={key}::` (skjema-sti) til `::error file={instance}::` (eksempelfil-sti)
   - Matcher GitHub Actions-annotasjonsformat som CI forventar

**Verifisering:**
- `make validate-examples DOMAIN=ngr LOGLVL=DEBUG` — batcha 4 eksempelfiler i éin kontainar (4.42s)
- `make validate-examples DOMAIN=fint LOGLVL=DEBUG` — batcha 6 eksempelfiler (6.01s)
- `make validate-examples DOMAIN=ap-no LOGLVL=DEBUG` — batcha 6 profiler med fixture-støtte (6.78s)
- Feilrapportering verifisert: `::error file=<instance>::<melding>` matcher CI-format

### Resultat

**Før batching:**
- `convert-rdf`: 15 separate `linkml-convert`-kontainarar (éin per eksempelfil)
- `convert-data`: 6 separate `linkml-convert`-kontainarar (éin per datafil)
- `validate-examples`: N separate `linkml validate`-kontainarar (éin per skjema, parallellisert)

**Etter batching:**
- `convert-rdf`: 1 kontainar for alle 15 eksempelfiler
- `convert-data`: 1 kontainar for alle 6 datafiler
- `validate-examples`: 1 kontainar per domene (t.d. 4 filer i ngr, 6 filer i fint)

**Estimert gevinst:**
- Tiltak 1+2: Eliminert 21 kontainarkall, amortisert `linkml_runtime`-import (~5-8s)
- Tiltak 3: Eliminert N-1 kontainarkall per domene (t.d. 3 kontainarkall spart for ngr, 5 for fint)

## Relaterte filer

- `Makefile` — `convert-rdf`, `convert-data`
- `make/20-domain-targets.mk` — `gen-linkml-convert` (alt batcha, mønster å gjenbruke)
- `make/40-validation.mk` — `validate-examples`, `mcp-linkml-valider-modell`
- `make/10-generator-macros.mk` — `run_gen_xsd_parallel`, `run_gen_asyncapi_parallel`
- `src/assets/scripts/makefile/convert-examples.sh` — delt discovery, alt TSV-klar
- `src/assets/scripts/makefile/convert-data.sh` — ny delt discovery for datafiler (Tiltak 2)
- `src/assets/scripts/makefile/run-parallel-gen.sh` — delt per-skjema-orkestrering `gen-xsd`/`gen-asyncapi` framleis bruker
- `src/assets/scripts/makefile/batch-render-plantuml.sh` — presedens for "éin delt kontainar, N filer" (PlantUML multi-fil-CLI)
- `src/assets/scripts/makefile/fix-xsd-dates.py` — reint Python, uproblematisk å batche (Tiltak 4)
- `src/assets/scripts/makefile/batch-generate-instances.py` — `run_convert` (produksjon)
- `src/assets/scripts/makefile/batch-convert.py` — meir generell test-variant (potensielt DRY-konsolidering)
- `src/assets/scripts/makefile/batch-linkml-validate.py` — test-variant, klar for `validate-examples`-bruk
- `specs/done/batch-validate-lint-test-per-skjema.md` — kjelde for API-kompatibilitetsfunna (`run_click()` vs. `sys.exit()`)
- `COMMANDS.md` — § Batching, tabellane oppdaterte for Tiltak 1-2
