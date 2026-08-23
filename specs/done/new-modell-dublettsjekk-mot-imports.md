# Dublettsjekk mot importerte skjema (`make new-modell` + `make validate`)

## Bakgrunn

`specs/done/oreg-scaffold-generering-feiler.md` dokumenterer eit konkret
hendingsforløp der `make new-modell ... JSON_SCHEMA=<sti>` scaffolda seks nye
enhetsregisteret-domenemodellar (commit `64387d86`) som kvar importerte
`dcat-ap-no-schema` (og transitivt `common-ap-no-schema`), men samtidig
definerte lokale `slots:`/`classes:` med **same namn** som eit element som
alt fanst i importkjeda — t.d. eit lokalt slot `beskrivelse` ved sida av det
importerte `beskrivelse` (`dct:description`), eller ein lokal klasse
`Kontaktopplysning` ved sida av det importerte `Kontaktopplysning`
(`vcard:Kind`). Fordi dei to definisjonane har ulik URI, mergar ikkje LinkML
sitt import-hierarki dei til éitt element slik det gjer for reine namnedublettar
— resultatet er feilen `Conflicting URIs (<uri-a>, <uri-b>) for item: <namn>`.

Denne feilen dukkar **ikkje** opp i `make validate`/`make lint` (den einaste
kontrollen `new-modell.sh` køyrer i dag, sjå linje 306-311 i
`src/assets/scripts/scaffolding/new-modell.sh`) — han dukkar først opp seinare,
djupt inne i spesifikke generatorar (`python`, `proto`, `graphql`,
`jsonld-context`, `plantuml`) som byggjer eit forent SchemaView av heile
importkjeda. Feilmeldinga nemner verken kva fil eller kva linje kollisjonen
kjem frå, og seks separate generatorsteg feila samtidig i CI før dette vart
oppdaga og retta manuelt. Same mønster kan oppstå igjen for kvar ny modell som
vert scaffolda frå JSON Schema (`mcp-linkml-modell-utkast` kjenner ikkje til
namna i importerte AP-NO-skjema når han konverterer JSON Schema-felt til
LinkML-slots/klassar), og for manuelt redigerte skjema som byter `imports:`
eller legg til nye slots/klassar for hand.

Repoet har alt eit etablert mønster for å unngå akkurat denne kollisjonen:
slottet `kontaktinformasjon` er i alle scaffolda oreg-skjema prefikset med
modellnamnet (`enhetsregisteret_bvrfriv_kontaktinformasjon` osv.) fordi det
elles ville kollidert med eit generisk namn. Målet med dette tiltaket er å
automatisk **oppdage** slike kollisjonar ved scaffolding-tidspunkt (og,
sekundært, på førespurnad for eksisterande skjema), i staden for å stole på at
nokon oppdagar det manuelt via ei kryptisk feilmelding seinare i CI.

## Evaluering: `make validate` eller `make lint`?

Sjekken bør køyrast i CI for **alle** skjema, ikkje berre ved scaffolding —
elles fangar han ikkje framtidige handmonterte kollisjonar (t.d. nokon legg
til eit nytt `imports:`-element i eit eksisterande skjema, eller eit nytt
slot/klasse-namn, utan å køyre `new-modell` på nytt). Spørsmålet er kva
eksisterande target som passar som vertskap.

**`make validate` er rett stad, ikkje `make lint`:**

- **`make validate` køyrer alt i kvar CI-jobb.** `validate` er Fase 1 i
  `domain-<x>`-pipelinen (`make/20-domain-targets.mk`), som er nøyaktig
  pipelinen som feila i `specs/done/oreg-scaffold-generering-feiler.md`. Å
  leggje sjekken her gjev CI-dekning for alle skjema **utan** noka endring i
  `.github/workflows/*.yml` — target er alt kalla frå den relevante jobben.
  `make lint` er derimot **ikkje kalla nokon stad i CI**
  (verifisert: ingen treff på `make lint`/`batch-lint` i
  `.github/workflows/*.yml`) — han er eit reint lokalt dev-bekvemmelegheits-
  target («Nyttig for hurtigsjekk under utvikling», jf. `COMMANDS.md`). Å
  leggje sjekken berre i `lint` ville ikkje løyst det opne spørsmålet i det
  heile, sidan han då framleis berre køyrer når nokon hugsar å køyre han
  manuelt.
- **Semantisk høyrer sjekken heime i `validate`, ikkje `lint`.** `lint`
  brukar LinkML sitt eige `linkmllint`-verktøy til **per-skjema**
  konvensjonssjekkar (namngjeving, prefiks — sjå `.linkmllint.yaml`) og
  kjenner ikkje til importkjeda i det heile. `validate` er derimot alt
  dokumentert som «merge-imports, fail-fast»-steget — sjekken vår er
  nøyaktig det: eit strukturelt spørsmål om korleis eit skjema sitt
  namnerom ser ut **etter** at importkjeda er løyst, ikkje ein
  stilkonvensjon for eitt skjema isolert.
- **Presisering — kan ikkje gjenbruke sjølve merge-kallet.** `validate`
  sitt eksisterande steg (`run_gen_linkml_parallel`, generatorkind `merge` i
  `batch-generate.py`, som køyrer `linkml.generators.linkmlgen`) **fangar
  ikkje** kollisjonen sjølv, verifisert empirisk under feilsøkinga i
  `specs/done/oreg-scaffold-generering-feiler.md`: `merge` rapporterte `OK`
  for alle tre skjema som seinare feila i `python`/`proto`/`graphql`/
  `jsonld-context`/`plantuml` med `Conflicting URIs`. `LinkMLGenerator`
  kallar rett og slett ikkje den delen av `SchemaView` som utløyser
  URI-konflikt-sjekken. Sjekken vår må difor vere eit **eige, tillegg**-steg
  i `validate`-recepten, ikkje eit forsøk på å gjenbruke `merge`-generatoren
  sin eksisterande kode.
- **`batch-generate.py` sin generator-registry passar ikkje for denne
  sjekken.** Registryet er bygd rundt å kalle faktiske
  `linkml.generators.<modul>`-klassar (for å amortisere den ~5,4s tunge
  linkml-importen på tvers av mange skjema i éin prosess). Vårt script er
  ikkje ein LinkML-generator — det er ei eiga YAML-parsing/import-oppløysing.
  Han skal difor **ikkje** leggjast inn i `REGISTRY`, men i staden følgje
  same, enklare mønster som `batch-lint.py` (éin prosess, éin
  containerstart, tek éi liste med skjema-stiar som argument) — sjå Tiltak 1.

**Konklusjon:** sjekken vert kalla frå `validate`-recepten i
`make/40-validation.mk`, i tillegg til (ikkje i staden for) det eksisterande
merge-steget. `make lint` vert ikkje endra.

## Tiltak

### 1. Ny, gjenbrukbar sjekk: `src/assets/scripts/makefile/check-import-duplicates.py`

**Revidert under implementering — ikkje ei eiga import-oppløysing.**
Opphavleg utkast til dette tiltaket skisserte eit hand-rulla, rekursivt
YAML-basert import-oppløysingsscript. Kjeldekode-gransking av
`linkml==1.11.1` (installert i `LINKML_IMAGE`) under implementeringa avdekte
at `Conflicting URIs`-feilen kjem frå éin, presis stad:
`linkml.utils.mergeutils.merge_dicts()`:

```python
if k in target and source[k].from_schema != target[k].from_schema:
    raise ValueError(f"Conflicting URIs ({source[k].from_schema}, {target[k].from_schema}) for item: {k}")
```

Dette er eit **reint namne-baserte** sjekk — `from_schema` er kva skjema-`id`
elementet vart *definert* i, ikkje sjølve `slot_uri`/`class_uri`-verdien (som
elles ville kravd at me reimplementerte LinkML sin eigen
CURIE-/prefiks-oppløysingsalgoritme for å samanlikne korrekt). To
top-nivå-element med same namn kolliderer alltid dersom dei kjem frå ulike
skjema i importkjeda — **sjølv om URI-verdiane deira tilfeldigvis er
identiske**. `merge_dicts()` vert kalla frå `merge_schemas()`, som igjen vert
kalla frå `SchemaLoader.resolve()` for kvart import (rekursivt, via
`self.schema.imports`) — nøyaktig den same mekanismen
`pythongen`/`protogen`/`rdfgen`/`graphqlgen`/`plantumlgen`/`jsonldcontextgen`
alt bruker internt (`uses_schemaloader = True`-generatorfamilien, sjå
`linkml/utils/generator.py`).

Sjekken bruker difor **`SchemaLoader` direkte**, i staden for å reimplementere
import-oppløysing for hand:

```python
from linkml.utils.schemaloader import SchemaLoader

try:
    SchemaLoader(schema_path, mergeimports=True).resolve()
except ValueError as exc:
    ...  # match "Conflicting URIs (...) for item: ..." og rapporter
```

Fordelar samanlikna med det opphavlege utkastet:

- **100 % åtferdsparitet** med feilen sjekken skal fange — inga fare for at
  ein hand-rulla heuristikk gir falske positivar/negativar samanlikna med kva
  som faktisk krasjar seinare i pipelinen.
- **Dekkjer `types:`/`enums:`/`subsets:` i tillegg til `classes:`/`slots:`**
  «gratis», sidan `merge_schemas()` kallar `merge_dicts()` for alle fem —
  brukaren spurde spesifikt om klassar/slots, men denne breiare dekninga er
  ei uproblematisk overoppfylling, ikkje eit avvik (same underliggande feil,
  same fiks-mønster).
- **Ingen «lokal arbeidstre vs. pinna tag»-avveging.** `SchemaLoader` hentar
  versjonslåste `raw.githubusercontent.com`-importar over nettverk, nøyaktig
  slik dei andre generatorane alt gjer i CI/lokalt (`raw.githubusercontent.com`
  er alt eit tillate nettverksmål for LinkML-kontaineren) — sjekken ser
  difor det **faktiske** pinna innhaldet, ikkje ein lokal approksimasjon.
  (Det opphavlege utkastet sin «Kjende avgrensingar»-fråsegn om dette er difor
  fjerna.)
- **Vesentleg mindre kode å vedlikehalde** — ingen eigen rekursiv
  import-walker, ingen eiga namnesamling-logikk.

Scriptet er forma som `batch-lint.py` (éin prosess/containerstart, tek éi
liste med skjema-stiar som argument via `argparse` — ikkje via
`batch-generate.py` sin `REGISTRY`, sjå «Evaluering» over, sidan
`SchemaLoader` ikkje er ein `linkml.generators.<modul>`-klasse) og
`linkml_relative_import_patch.apply()` vert kalla først, som i alle andre
batch-script i `src/assets/scripts/makefile/`. For **kvar** skjema-sti:

1. Kall `SchemaLoader(schema_path, mergeimports=True).resolve()`.
2. Fangar `ValueError` — matchar meldinga mot mønsteret
   `Conflicting URIs (<schema-a>, <schema-b>) for item: <namn>` med ein
   regex. Ved treff: rapporter namnet og dei to kjelde-skjemaa i eit
   `::error file=<schema>::`-format (same attribueringskonvensjon som
   `batch-lint.py`/`batch-generate.py`), med forslag om å prefiksa det
   lokale elementet med modellnamnet (jf. `<modell>_kontaktinformasjon`).
   Ved ikkje-treff (ein annan `ValueError` frå `.resolve()`, t.d. ein
   ugyldig prefiks): rapporter likevel, med den rå feilmeldinga — ikkje ei
   stille forbikøyring.
3. Fangar alle andre unntak (t.d. nettverksfeil ved henting av eit
   versjonslåst import, ugyldig YAML) i eit eige, breiare
   `except Exception`-ledd — same per-skjema-isolasjonsmønster som
   `batch-lint.py` (eitt skjema sin feil stoppar ikkje resten av batchen),
   logga tydeleg, aldri stille.

Skriv testar i `tests/` som dekkjer: (a) eit skjema utan kollisjon (skal
returnere 0 funn), (b) eit skjema med ein direkte kollisjon mot eit
førstenivå-import, (c) ein kollisjon som berre finst via eit transitivt
import (t.d. via `dcat-ap-no-schema` → `common-ap-no-schema`), (d) at
`linkml:types` ikkje gir falske positivar.

### 2. Nytt make-target: `make check-import-duplicates [DOMAIN=<domene>|SCHEMA=<sti>]`

Wrapper i `make/40-validation.mk` (saman med `lint`/`validate`), same
oppsett som `lint`:

```makefile
check-import-duplicates: ## Sjekk at lokale slots/klassar ikkje kolliderer med namn frå importerte skjema [DOMAIN=<domene>|SCHEMA=<sti>]
	$(call print_header,check-import-duplicates,$(if $(SCHEMA),SCHEMA=$(SCHEMA),$(if $(DOMAIN),DOMAIN=$(DOMAIN),(alle skjema))))
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/check-import-duplicates.py $(call get_target_schemas)
```

Bruker same `get_target_schemas`-makro som `validate`/`lint` for
DOMAIN=/SCHEMA=/alle-skjema-discovery — målet kan difor køyrast frittståande
på **alle** eksisterande skjema, éin domene, eller berre eitt skjema, same
konvensjon brukarar av repoet alt kjenner frå `lint`/`validate`. Nyttig for
periodisk revisjon og for å verifisere at fiksen i
`specs/done/oreg-scaffold-generering-feiler.md` var fullstendig.

### 3. Kall sjekken frå `validate`-recepten (CI-dekning for alle skjema)

Legg til eit ekstra kall i `validate:`-recepten i `make/40-validation.mk`,
rett etter det eksisterande `run_gen_linkml_parallel`-kallet:

```makefile
validate: ## Valider alle skjema (merge-imports, fail-fast, ingen fil skriven) [DOMAIN=<domene>|SCHEMA=<sti>]
	...
	$(call run_gen_linkml_parallel,$(call get_target_schemas))
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/check-import-duplicates.py $(call get_target_schemas)
```

Sidan `validate` alt er Fase 1 i `domain-<x>`-pipelinen (køyrt for kvar
domene i `.github/workflows/generate.yml`), gjev dette CI-dekning for **alle**
skjema, ved kvar CI-køyring, utan noka endring i sjølve workflow-fila. Feilar
sjekken for eitt skjema, feilar Fase 1 for det domenet — same «stopp tidleg»-
eigenskap som Tiltak 4 gjev for scaffolding, no repo-vidt.

**Åtferd ved funn: hard feil** (exit 1), konsistent med avgjerda for Tiltak 4.

### 4. Kall sjekken frå `new-modell.sh`

Legg til eit kall til `make check-import-duplicates SCHEMA=$SCHEMA_FILE_REL`
i `src/assets/scripts/scaffolding/new-modell.sh`, rett etter at skjemafila er
skriven og før `make lint`-kallet (linje ~308-311) — på dette tidspunktet er
den endelege `imports:`-lista (inkludert den auto-injiserte
dcat-ap-no-importen frå linje 197-203) alt skriven til `$SCHEMA_FILE`, så
sjekken ser same tilstand som CI seinare vil bygge frå.

**Åtferd ved funn: hard feil** (exit 1). Scaffoldinga stoppar med skjemafila
liggande att slik brukaren kan rette henne — grunngjeving: kollisjonen **vil**
uansett få seks+ generatorsteg til å feile seinare i CI (stadfesta empirisk i
denne sesjonen), så å stoppe tidleg med ei presis, handlingsretta feilmelding
er strengt betre enn eit grønt scaffold-steg som garantert feilar i neste
CI-køyring. Feilmeldinga skal foreslå det etablerte disambigueringsmønsteret
(prefiks med modellnamn, jf. `<modell>_kontaktinformasjon`).

### 5. Dokumenter i `COMMANDS.md`

Legg til `make check-import-duplicates` i generator-/valideringstabellen
(same stad som `lint`/`validate`), nemn tillegget i `validate`-rada (så det
går fram at `validate` no òg dekkjer importnamne-kollisjonar, ikkje berre
metaskjema-strukturvalidering), og nemn han i
`mkdocs/docs/kom-i-gang/ny-domenemodell.md` sitt steg for `new-modell` dersom
den sida skildrar feilhandtering ved scaffolding.

## Kjende avgrensingar

- Sjekken krev nettverkstilgang til `raw.githubusercontent.com` for skjema
  med versjonslåste importar (same føresetnad som `python`/`proto`/`rdf`/
  `graphql`/`plantuml`/`jsonld-context`-generatorane alt har i dag — ikkje ei
  ny avgrensing denne spesifikasjonen innfører).
- `SchemaLoader.resolve()` gjer meir enn berre import-samanslåing (validerer
  òg prefiks, `is_a`/mixin-oppløysing m.m.) — ein `ValueError` som **ikkje**
  matchar `Conflicting URIs`-mønsteret vert difor rapportert med den rå
  feilteksten i staden for eit spesialtilpassa forslag. Framleis synleg og
  handterbart, berre mindre presist forklart enn sjølve dublett-tilfellet.

## Utført

Alle fem tiltak gjennomførte 2026-08-23.

- **Tiltak 1:** `src/assets/scripts/makefile/check-import-duplicates.py`
  oppretta, `SchemaLoader`-baserte tilnærminga stadfesta empirisk: verifisert
  at han (a) godkjenner alle 43 skjema i repoet reint (~21s batcha), (b)
  fangar det faktiske `beskrivelse`-kollisjonstilfellet frå
  `oreg-scaffold-generering-feiler.md` når det vert reintrodusert i ein
  mellombels kopi, med korrekt `[ERROR] ::error file=...::`-attribuering.
  Testfixturar oppretta i `tests/fixtures/check-import-duplicates-*.yaml`
  (base/no-collision/direct-collision/middle/transitive-collision — eit lite
  sjølvstendig import-hierarki utan nettverksavhengigheit), og
  `tests/test_check_import_duplicates.py` (5 testar: ingen kollisjon,
  direkte kollisjon, transitiv kollisjon, `linkml:types` ikkje falsk positiv,
  per-skjema-isolasjon ved batching) — alle grøne.
- **Tiltak 2:** `check-import-duplicates`-target lagt til i
  `make/40-validation.mk` (+ `.PHONY` i `Makefile`). Verifisert med
  `make check-import-duplicates DOMAIN=oreg` (rein) og mot ein mellombels
  kopi med reintrodusert kollisjon (feila korrekt, exit 2).
- **Tiltak 3:** Kall til scriptet lagt til i `validate`-recepten, rett etter
  `run_gen_linkml_parallel`. Verifisert at `make validate DOMAIN=oreg` framleis
  er rein, og at `make validate SCHEMA=<kollisjons-kopi>` no hard-feilar
  (exit 2) — stadfestar at `validate` faktisk fangar tilfellet CI-jobben
  som feila i `oreg-scaffold-generering-feiler.md` ikkje fanga.
- **Tiltak 4:** Kall lagt til i `new-modell.sh`, rett før lint-steget.
  Verifisert med ein fullstendig `make new-modell DOMAIN=... NAME=...`-køyring
  (tom stub, ingen JSON_SCHEMA) — nytt steg køyrer synleg og rein, resten av
  scaffoldinga uendra.
- **Tiltak 5:** `COMMANDS.md` oppdatert (ny rad for `check-import-duplicates`,
  `validate`-rada nemner no tillegget). `mkdocs/docs/kom-i-gang/ny-domenemodell.md`
  § "3 — Valider undervegs" nemner no `check-import-duplicates` for manuell
  redigering av `imports:`/slots/klassar (steg 2).

**Ekstra funn under implementering (ikkje i det opphavlege tiltakslista):**
`src/assets/scripts/makefile/help.sh` sin kategori-regex for «Validering»
(`(validate|lint|check-published-uris)`) matcha ikkje målnamnet
`check-import-duplicates` i det heile — targetet fall gjennom ALLE kategoriar
og vart usynleg i `make help`, sjølv om det fungerte korrekt når kalla
direkte. Retta ved å leggje `check-import-duplicates` til som eige,
eksplisitt mønster (same konvensjon som `check-published-uris`), verifisert
med `make help | grep check-import-duplicates`.

Ingen endring i `.github/workflows/*.yml` — `actionlint`-steget er difor
ikkje aktuelt for denne implementeringa.
