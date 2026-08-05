# Forenkle og konsolider make-laget

## Bakgrunn

Brukar ba om ein full gjennomgang av `Makefile` og alle `make/*.mk`-filene
(15 filer, ~1580 linjer totalt) for å vurdere om funksjonar kan slåast
saman/forenklast, og om inlina bash-kode bør flyttast til eigne script —
i same ånd som `specs/done/delt-script-parallell-generering.md` og
`specs/done/dry-opprydding.md`.

Denne speccen er ei **kartlegging**, ikkje ei gjennomføring. Kvart funn under
er sjølvstendig og kan brytast ut til eiga oppfølgingsspec (eller fleire
funn kan slåast saman i éi spec) når arbeidet faktisk skal utførast, jf.
arbeidsflyten i `CLAUDE.md`.

Funna er sortert etter alvorsgrad: éin verifisert funksjonsfeil først,
deretter reelle DRY-brot/forenklingar (3+ tilfelle), deretter mindre
opprydding.

## Funn

### 1. [FUNKSJONSFEIL, verifisert] `gen-shacl` i domenebygg ignorerer per-skjema SHACL-flagg

**Kva:** `make/20-domain-targets.mk:41` kallar den generiske
`run_gen_parallel`-makroen for SHACL:

```make
$$(call run_gen_parallel,$$(_schemas_$(1)),gen-shacl,shapes.ttl,shacl)
```

`run_gen_parallel` (`make/10-generator-macros.mk:25-28`) har ingen
per-skjema flagg-oppslag — han køyrer alltid berre `gen-shacl "$s"` utan
ekstra flagg. Men `config.mk` (generert av `gen-config.sh` frå
`build.yaml`) definerer `SHACL_FLAGS_fint_fint_administrasjon :=
--exclude-imports` (og tilsvarande for dei 6 andre FINT-skjemaa), som berre
vert brukt av den **serielle** `run_gen_shacl`-makroen
(`make/10-generator-macros.mk:44-51`) — og den makroen vert i dag **berre**
kalla frå det frittståande `make gen-shacl SCHEMA=...`-targetet
(`make/11-generator-targets.mk:30`), ikkje frå `domain-fint`.

**Verifisert i eksisterande generert artefakt:**
`generated/fint/fint-administrasjon/fint-administrasjon-shapes.ttl` har 53
`sh:targetClass`-shapes — 33 med lokalt `adm:`-prefiks (matchar dei 34 lokale
klassane i skjemaet) og **19 med `fint:`-prefiks, som høyrer til den
importerte `fint-common-schema`**. Dersom `--exclude-imports` faktisk hadde
vore brukt (slik `SHACL_FLAGS_fint_fint_administrasjon` føreset), skulle
desse 19 importerte shapa ikkje vore med. Dette provar at
`domain-fint`-bygget produserer eit anna (større, feil) SHACL-resultat enn
`make gen-shacl SCHEMA=... DOMAIN=fint` gjer.

**Merk:** `run_gen_owl_parallel` har **same avgrensing** for
`OWL_FLAGS_*`, men det er dokumentert med ein eksplisitt kommentar
("`config.mk`-overrides vert ikkje propagerte til xargs"). SHACL-varianten
manglar både funksjonaliteten og kommentaren.

**Tilråding:** Anten (a) legg til per-skjema flagg-oppslag i
`run-parallel-gen.sh` (t.d. ved å eksportere `SHACL_FLAGS_*`/`OWL_FLAGS_*`
som eit shell-assosiativt array eller ved å slå opp flagget frå
`build.yaml` direkte i scriptet i staden for frå Make-variablar), eller (b)
minimum dokumenter avgrensinga for SHACL slik ho alt er dokumentert for OWL,
slik at åtferda er eit medvite (om enn ufullstendig) val og ikkje ein skjult
bug. (a) er å føretrekke sidan det faktisk rettar opp feil SHACL-output for
alle 7 FINT-skjemaa i eit fullstendig domenebygg.

### 2. 12 av 18 `gen-*`-targeta er usynlege i `make help`

**Verifisert:**

```
$ make help | sed -n '/Generering/,/Validering/p'
Generering (per domene eller skjema):
  convert-rdf                   Konverter eksempelfiler frå YAML til RDF/Turtle
  convert-data                  Konverter datafiler (data/*/*.yaml) frå YAML til RDF/Turtle
  gen-dqv-measurements           Generer DQV-kvalitetsmålingar for datafiler
  gen-modelldcat-elements        Generer ModelDCAT-AP-NO-modellelement [ORG=<alias>] [DRYRUN=1]
  gen-docs                       Generer dokumentasjon (gen-doc + gen-erdiagram) [...]
```

`gen-jsonld-context`, `gen-shacl`, `gen-python`, `gen-jsonschema`,
`gen-owl`, `gen-rdf`, `gen-xsd`, `gen-asyncapi`, `gen-openapi`,
`gen-erdiagram`, `gen-proto` og `gen-plantuml` finst alle og fungerer, men
vert **aldri lista** — dei er definerte via `$(eval $(call
make_gen_target,...))` i `make/11-generator-targets.mk`, og
`make_gen_target`-malen (`make/11-generator-targets.mk:11-22`) inneheld
ingen `## `-hjelpetekst.

Dette er **akkurat** fallgruva som `make/80-images.mk` sin toppkommentar
åtvarar mot: "target/kommentar-linjer generert av `$(eval ...)` finst berre
i Make sin minnetilstand, aldri på disk, og ville difor vorte usynlege i
`make help`". `80-images.mk` løyste det ved å skrive `build-docker-*`-targeta
eksplisitt (medan sjølve `podman build`-oppskrifta framleis er delt via
`docker_build`-makroen). `11-generator-targets.mk` fylgjer ikkje same
mønster for `gen-*`.

**Tilråding:** Ikkje fjern `make_gen_target`-generering (sjølve
kroppen/logikken bør framleis vere DRY) — legg i staden til ein liten,
statisk blokk med reint deklarative `<target>: ## <skildring>`-linjer utan
oppskrift (Make tillèt fleire reglar for same target så lenge berre éi har
ei oppskrift), t.d.:

```make
gen-jsonld-context: ## Generer JSON-LD context [SCHEMA=<sti>|DOMAIN=<domain>]
gen-shacl: ## Generer SHACL-shapes [SCHEMA=<sti>|DOMAIN=<domain>]
gen-python: ## Generer Python-klassar [SCHEMA=<sti>|DOMAIN=<domain>]
...
```

plassert i `make/11-generator-targets.mk` sjølv (som **er** på disk og
difor synleg for `make help` sin `grep $(MAKEFILE_LIST)`).

### 3. Fem par duplikerte serial/parallel-makroar i `10-generator-macros.mk`

**Mønster:** For fem generatorar finst det to nesten identiske makroar —
éin serial-variant (bash `for`-løkke skriven direkte i `define`-blokka) og
éin parallell-variant (tynn `GEN_CMD`-wrapper rundt
`run-parallel-gen.sh`). Serial-varianten vert **berre** brukt av det
frittståande targetet i `make/11-generator-targets.mk`; parallell-varianten
vert **berre** brukt av `domain_target` i `make/20-domain-targets.mk`. Dei
to variantane køyrer funksjonelt identisk kommando — skilnaden er reint
orkestrering (bash `for` vs. `xargs -P`), som `run-parallel-gen.sh` alt
handterer generisk (inkludert éin-skjema-tilfellet).

| Generator | Serial-makro (linjer) | Parallell-makro | Brukt av standalone-target |
|---|---|---|---|
| gen-doc | `run_gen_doc` (94-117, 24 linjer) | `run_gen_doc_parallel` | `gen-docs` |
| gen-erdiagram | `run_gen_erdiagram` (141-152, 12 linjer) | `run_gen_erdiagram_parallel` | `gen-docs`, `gen-erdiagram` |
| gen-plantuml | `run_gen_plantuml` (170-192, 23 linjer) | `run_gen_plantuml_parallel` | `gen-plantuml` |
| gen-asyncapi | `run_gen_asyncapi` (255-283, 29 linjer) | `run_gen_asyncapi_parallel` | `gen-asyncapi` |
| gen-openapi | `run_gen_openapi` (294-321, 28 linjer) | `run_gen_openapi_parallel` | `gen-openapi` |

Same mønster finst òg i `make/30-instances.mk` for
`run_gen_informasjonsmodell_instance` / `..._parallel` (brukt av høvesvis
`gen-informasjonsmodell-instance`-targetet og `domain_target`).

**Tilråding:** La dei frittståande targeta i `make/11-generator-targets.mk`
(og `gen-informasjonsmodell-instance` i `make/30-instances.mk`) kalle
`_parallel`-makroen direkte i staden for å halde ved like ein duplikat
serial-variant. `run-parallel-gen.sh` fungerer korrekt for både éitt og
mange skjema (`xargs -P N` på ei liste med 1 element køyrer berre det eine
elementet). Dette fjernar ~120 linjer duplikatkode frå
`10-generator-macros.mk` og ~15 linjer frå `30-instances.mk`, og gjer at
frittståande `make gen-plantuml SCHEMA=...` og `make domain-<x>` alltid
nyttar nøyaktig same kodesti.

### 4. `linkml-convert` for eksempelfiler er duplisert mellom `Makefile` og `domain_target`

`Makefile:119-145` (`convert-rdf`) og `make/20-domain-targets.mk:46-67`
(inni `domain_target`) inneheld nesten byte-for-byte same
bash-for-løkke: finn `*-eksempel.yaml`, ekstraher domene/profil, sjekk
`example_rdf: false`-flagget i `build.yaml`, vel fixture- eller
produksjonsskjema, køyr `linkml-convert`. Einaste skilnaden er at
`domain_target`-varianten er filtrert til éitt domene og manglar
`mkdir -p`-katalogoppretting-mønsteret sitt output-format (skriv til stdout
via `>` i staden for `--output`-flagget — sjølv dette er ein liten,
unødvendig skilnad mellom dei to nesten-identiske blokkene).

**Tilråding:** Flytt løkka til eit delt script,
`src/assets/scripts/makefile/convert-examples.sh`, som tek eit valfritt
domene-filter som argument (jf. mønsteret frå
`specs/done/delt-script-parallell-generering.md`). `convert-rdf`-targetet
kallar det utan filter; `domain_target` kallar det med `$(1)` (domenenamnet)
som filter.

### 5. `gen-xsd` er den einaste generatoren utan parallell-variant

`run_gen_xsd` (`10-generator-macros.mk:214-250`, 37 linjer) er ei serial
`for`-løkke som køyrer tre steg per skjema (`avrotize j2a`, `avrotize a2x`,
`fix-xsd-dates.py`) med manuell timing/logging — same scaffolding som
`run-parallel-gen.sh` alt generaliserer. Han vert kalla direkte (ikkje via
ein `_parallel`-variant) frå **både** `domain_target`
(`20-domain-targets.mk:72`) og det frittståande `gen-xsd`-targetet
(`11-generator-targets.mk:35`) — så det er ikkje duplikatkode her, men det
er den einaste generatoren i heile pipelinen som køyrer heilt serielt i
`domain-<x>`, noko som gjer XSD-steget til ein flaskehals i store
domenebygg (t.d. FINT med 7 skjema).

**Tilråding:** Legg til `run_gen_xsd_parallel` via `run-parallel-gen.sh`
(`--flag xsd --check-suffix schema.json`), med sjølve
`j2a && a2x && fix-xsd-dates.py`-kjeda som `GEN_CMD`. Krev at
`--check-suffix`-mekanismen i scriptet held fram å fungere for
mellomsteget (`.avsc`), som må ryddast opp (`rm -f`) etter kvart kall —
verifiser at dette let seg uttrykke reint i éin `GEN_CMD`-streng, elles ta
ut reinhaldet i eit lite hjelpe-script.

### 6. `run_gen` (serial, ugata) er ein enkel duplikat av `run_gen_parallel`

`run_gen` (`10-generator-macros.mk:14-20`) er ei generisk serial-makro
brukt av 4 frittståande target (`gen-jsonld-context`, `gen-python`,
`gen-jsonschema`, `gen-proto`). Han tek ikkje omsyn til
`build.yaml`-flagg. `run_gen_parallel` (same fil, 25-28) gjer nøyaktig same
jobb, berre parallelt **og** med valfri flagg-gating (4. argument). Kallar
ein `run_gen_parallel` utan 4. argument (slik `run_gen_linkml_parallel` alt
gjer), får ein identisk ugata åtferd som `run_gen`, berre via
`run-parallel-gen.sh` i staden for ei duplisert bash `for`-løkke.

**Tilråding:** Byt dei 4 kalla i `make_gen_target,...,run_gen,...` til
`run_gen_parallel` og fjern `run_gen`-makroen (7 linjer + éin kallar-stad
mindre å halde synkron med `run_gen_parallel` sitt grensesnitt).

### 7. `help`-targetet har 7 nesten identiske grep/sed/awk-blokker

`Makefile:81-99` gjentek same pipeline sju gonger:

```make
@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E '(<kategori-regex>)' | sed 's/^[^:]*://' | awk 'BEGIN {FS = "## "}; {printf "  $(CLR_STEP)%-30s$(CLR_RST) %s\n", $$1, $$2}'
```

— berre kategori-overskrifta og `grep -E`-filteret varierer. Dette er over
DRY-terskelen på 3 like tilfelle frå `CLAUDE.md`.

**Tilråding:** Flytt heile `help`-targetet til eit script,
`src/assets/scripts/makefile/help.sh`, som tek `$(MAKEFILE_LIST)` som input
og itererer over ei liste med `(overskrift, regex)`-par. Dette er òg eit
konkret høve til å følgje brukaren sitt eksplisitte ønske om å "flytte
inlina kode til bash-script" — `help`-targetet er det mest inline-tunge
targetet i heile `Makefile`.

### 8. Dødt/misvisande `PARALLEL ?= 8` i `Makefile`

`Makefile:58` set `PARALLEL ?= 8`, men `make/00-settings.mk:34` (inkludert
på linje 12, **før** linje 58 køyrer) set alt `PARALLEL ?= 16`. Sidan
`?=` berre verkar dersom variabelen er usett, er `Makefile:58` daud kode —
verifisert med `make -p | grep '^PARALLEL '` → `PARALLEL = 16`. Ein lesar av
`Makefile` som ser `PARALLEL ?= 8` på linje 58 vil tru standardverdien er 8,
men han er 16.

**Tilråding:** Fjern `PARALLEL ?= 8` frå `Makefile:58` (han er reint
overflødig sidan `00-settings.mk` alt vert inkludert). Dersom 8 faktisk var
den *tiltenkte* standardverdien, avklar med brukaren og oppdater
`00-settings.mk` i staden.

### 9. (Lågt prioritert, under DRY-terskel) `convert-rdf`/`convert-data` og `validate-bronze`/`validate-examples`

- `convert-rdf` og `convert-data` (`Makefile`) deler struktur (finn
  filer → sjekk `build.yaml`-flagg → køyr `linkml-convert`), men er berre 2
  tilfelle — under CLAUDE.md sin uttalte terskel på 3. Kan likevel vurderast
  saman med funn 4 sidan eit felles `convert-examples.sh`/`convert-data.sh`
  uansett vert oppretta.
- `validate-bronze` og `validate-examples` (`make/40-validation.mk`) deler
  same løkke-skjelett (finn skjema, ekskluder `common`, logg per skjema,
  tel `FAILED`) — 2 tilfelle. `validate-data` er strukturelt likt, men
  itererer over datakatalogar i staden for skjema, så det er ikkje eit
  reint tredje identisk tilfelle. Nemnt her for fullstendigheit, ikkje
  tilrådd som eige tiltak no.

## Ikkje-funn (vurdert, ingen tiltak tilrådd)

- `make/00-settings.mk`, `01-containers.mk`, `02-schema-discovery.mk`,
  `03-output.mk` er alle reine konfigurasjons-/makro-samlingar utan
  duplikasjon.
- `make/50-docs.mk`, `60-mcp.mk`, `70-scaffolding.mk`, `90-tools.mk`
  delegerer alt konsekvent til `bash`-script eller Python — godt eksempel på
  mønsteret resten av gjennomgangen tilrår.
- `make/80-images.mk` sin bevisste `$(eval)`-unngåing (for
  `make help`-synlegheit) er alt korrekt grunngjeve i eiga fil — sjå funn 2
  for kvifor `11-generator-targets.mk` bør følgje same prinsipp.

## Prioritert handlingsliste (for oppfølgande spec(ar))

- [ ] **Funn 1** (bug): rett SHACL-flagg-overstyring i domenebygg (eller
      dokumenter avgrensinga eksplisitt, som for OWL)
- [ ] **Funn 2**: gjer alle 12 skjulte `gen-*`-targeta synlege i `make help`
- [ ] **Funn 3**: kollaps 5 par serial/parallel-makroar (gen-doc,
      gen-erdiagram, gen-plantuml, gen-asyncapi, gen-openapi) +
      informasjonsmodell-instance til éin variant kvar
- [ ] **Funn 6**: kollaps `run_gen`/`run_gen_parallel` til éin makro
- [ ] **Funn 4**: flytt duplisert `linkml-convert`-løkke til delt script
- [ ] **Funn 5**: legg til `run_gen_xsd_parallel`, bruk i `domain_target`
- [ ] **Funn 7**: flytt `help`-targetet sine 7 grep/sed/awk-blokker til
      `help.sh`
- [ ] **Funn 8**: fjern daud `PARALLEL ?= 8` i `Makefile` (etter avklaring
      av tiltenkt standardverdi)

Estimert samla reduksjon: ~250-300 linjer frå `10-generator-macros.mk`,
`Makefile` og `30-instances.mk`, utan tap av funksjonalitet — pluss éin
reell bug retta (funn 1) og 12 target som vert oppdageleg via `make help`
(funn 2).

## Neste steg

Dette er ei kartleggingsspec. Ved gjennomføring bør funn 1 (bug) og funn 2
(discoverability) prioriterast først sidan dei har brukarsynleg effekt.
Funn 3-8 er reint interne forenklingar og kan gjerast samla i éi
oppfølgingsspec, t.d. `konsolider-generator-makroar.md`, når brukaren
ønskjer å gå vidare med gjennomføringa.

## Utført

Alle funn (1-8) er gjennomførte i denne økta.

**Funn 1 (bug):** `run-parallel-gen.sh` har fått eit nytt `--extra-flags-field`-
flagg som les `shacl_flags`/`owl_flags` direkte frå kvart skjema sitt eige
`build.yaml` (ikkje via `config.mk`/Make-variablar, som ikkje er tilgjengelege
i xargs-subshellen). Nye `run_gen_shacl_parallel` og oppdatert
`run_gen_owl_parallel` brukar dette, og `domain_target` kallar no
`run_gen_shacl_parallel` i staden for den generiske, ugata `run_gen_parallel`.
**Verifisert empirisk:** `generated/fint/fint-administrasjon/fint-administrasjon-shapes.ttl`
gjekk frå 53 shapes (33 lokale + 19 importerte frå `fint-common`) til 34
shapes (berre lokale) etter fiksen — `--exclude-imports` vert no korrekt
brukt i fullstendige domenebygg, ikkje berre i frittståande
`make gen-shacl SCHEMA=...`.

**Funn 2:** 12 statiske `<target>: ## <skildring>`-linjer (utan oppskrift)
lagt til i `make/11-generator-targets.mk` for dei tidlegare skjulte
gen-*-targeta. `make help` viser no alle 18 gen-*/convert-*-target i
"Generering"-kategorien (opp frå 5).

**Funn 3+6:** Alle serial-variantane (`run_gen`, `run_gen_shacl`,
`run_gen_owl`, `run_gen_rdf`, `run_gen_doc`, `run_gen_erdiagram`,
`run_gen_plantuml`, `run_gen_asyncapi`, `run_gen_openapi`,
`run_gen_informasjonsmodell_instance`) er fjerna frå
`make/10-generator-macros.mk` og `make/30-instances.mk`. Alle frittståande
gen-*-target og `gen-informasjonsmodell-instance`-targetet kallar no dei
same `_parallel`-makroane som `domain_target` alt brukte. Netto reduksjon:
`10-generator-macros.mk` gjekk frå 327 til 158 linjer.

**Funn 4:** Ny `src/assets/scripts/makefile/convert-examples.sh` — deler
oppdagings-/filtreringslogikken (finn eksempelfiler, sjekk
`example_rdf: false`, vel fixture- eller produksjonsskjema) mellom
`convert-rdf`-targetet (Makefile) og `domain_target`
(`make/20-domain-targets.mk`). Scriptet skriv tab-separerte
(skjema, eksempel, output)-liner til stdout; sjølve `linkml-convert`-kallet
skjer framleis i Make-recipa (krev `$(LINKML_RUN)` sin ekte shell-parsing av
anførselsteikn i mount-flagga, som ikkje overlever eit
miljøvariabel-lag uendra).

**Funn 5:** Ny `run_gen_xsd_parallel` i `make/10-generator-macros.mk`, brukt
av både `domain_target` og det frittståande `gen-xsd`-targetet. Namnerom
hentast med `sed` (ikkje `awk`) for å unngå nøsta anførselsteikn inni den
allereie enkelt-quota `GEN_CMD`-strengen. **Verifisert med ekte
containerkøyring** (`make gen-xsd DOMAIN=samt`): korrekt namnerom i utfila,
og mellomfila (`.avsc`) vart korrekt rydda opp.

**Funn 7:** Ny `src/assets/scripts/makefile/help.sh` — dei 7 nesten
identiske grep/sed/awk-pipelinane i `help`-targetet er no éin
data-drive løkke over (overskrift, mønster)-par.

**Funn 8:** Det daude `PARALLEL ?= 8` i `Makefile` er fjerna (verifisert med
`make -p | grep '^PARALLEL '` → framleis 16, uendra).

**Tilleggsfunn (oppdaga under gjennomføring):** `config.mk`/`gen-config.sh`
sine fire genererte variabelprefiks (`GEN_RDF_SKIP_*`, `EXAMPLE_RDF_SKIP_*`,
`SHACL_FLAGS_*`, `OWL_FLAGS_*`) er no **alle** overflødige — kvar generator
les no det tilsvarande `build.yaml`-feltet direkte i staden. Heile
`config.mk`-mekanismen kunne difor fjernast, men han er kopla til
cache-invalideringslogikk i `.github/workflows/reusable-generate.yml` og ein
ekstern `_linkml-tools`-referanse. Å fjerne han er større kirurgi enn denne
speccen bad om (CI-endring, ikkje berre make-laget) — la stå urørt, men
noter som eige oppfølgingsfunn for ein framtidig spec.

**Valideringsfunn (ikkje ein regresjon):** `roundtrip-ttl (samt-bu)` i
`tests/test_make.sh` feilar med `Unknown CURIE prefix: @base` frå
`linkml_runtime` sin `rdflib_dumper`. Stadfesta 100 % reproduserbart med ein
isolert `podman run ... linkml-convert`-kommando som ikkje rører noko kode
endra i denne speccen — same mønster som dei alt dokumenterte BUG-1/BUG-2 i
`tests/test_make.sh`. Bør dokumenterast som ny BUG i `bugs/` i eiga spec,
utanfor scope her.

**Validert med ekte containerkøyring:**
- `make gen-shacl DOMAIN=fint` — stadfesta bugfiks (funn 1)
- `make domain-fint` — heile pipelinen (linkml, jsonld-context, shacl, python,
  json-schema, owl, rdf, linkml-convert, doc, erdiagram, proto, plantuml,
  xsd (gata, ingen skjema aktiverte — korrekt), openapi, asyncapi (gata,
  ingen skjema aktiverte — korrekt), informasjonsmodell-instance) — alle
  steg fullførte utan feil
- `make gen-xsd DOMAIN=samt` og `make gen-asyncapi DOMAIN=samt` — dei to
  generatorane FINT ikkje brukar
- `bash tests/test_make.sh src/linkml/samt/samt-bu/samt-bu-schema.yaml` —
  16 av 17 deltestar OK (gen-shacl, gen-owl, gen-jsonld, gen-python,
  gen-jsonschema, gen-rdf, gen-erdiagram, gen-docs, convert-rdf,
  linkml-lint, linkml-validate, gen-proto, gen-plantuml,
  mcp-validate-instance, roundtrip-json), éin feil (roundtrip-ttl, sjå over,
  ikkje ein regresjon)
- `make -n` dry-run av alle 16 frittståande gen-*/convert-*-target
- `make help` — stadfesta alle 18 gen-*/convert-*-target no synlege
