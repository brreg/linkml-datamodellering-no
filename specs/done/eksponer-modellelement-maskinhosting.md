# Plan: Eksponér modellelement for maskinhøsting (MD5)

## Bakgrunn

`specs/backlog/avvik-veileder-modelldcat-ap-no.md` (avvik 3, tiltak MD5) avklarte
at vi går for «alternativ 2» frå Veileder for ModellDCAT-AP-NO: heile modellen
skal eksponeres med faktiske modellelement (`Objekttype`, `Attributt`,
`Kodeliste` osb.), ikkje berre ein lenke til portalen
(`informasjonsmodellidentifikator`). MD1–MD4 og MD6 frå den specen er no
fullførte — alle 23 skjema er registrerte i 6 per-org-modellkatalogar
(`src/linkml/modellkatalog/<org>-modellkatalog/data/<org>-modellkatalog/<org>-modellkatalog.yaml`),
men `inneholder_modellelement` står tomt for alle `Informasjonsmodell`-instansar.

Dette er det største gjenstående gapet mot rettleiaren, og det einaste
tiltaket som var uttrykkeleg utsett til ein eigen spec (jf. MD5 sin tekst:
«Utsett gjennomføring til MD2–MD4 er på plass... Dette er ein eigen større
spec»).

### Kva finst allerede

- **Måldatamodellen er ferdig spesifisert.** `modelldcat-modell-schema.yaml`
  (importert av `modelldcat-katalog-schema.yaml` via
  `./modelldcat-modell-schema`) definerer heile ModellDCAT-AP-NO-modelldelen:
  `Modellelement` (abstrakt) → `Objekttype`, `Rotobjekttype`, `Datatype`,
  `Enkeltype`, `Kodeliste`, `Modul`; `Egenskap` (abstrakt) → `Attributt`,
  `Assosiasjon`, `Rolle`, `Spesialisering`, `Komposisjon`, `Realisering`,
  `Abstraksjon`, `Avhengighet`, `Samling`, `Valg`; samt `Kodeelement`,
  `Note`, `Begrensningsregel`. Ingen skjemaendringar trengst her.
- **Containerstrukturen er no oppdatert (Steg 1+2, sjå nedanfor).**
  `ModellkatalogContainer` (`new-org-catalog.sh`-malen og alle 6
  eksisterande `<org>-modellkatalog-schema.yaml`) har toppnivå-attributtane
  `objekttyper`, `kodelister`, `kodeelementer`, `attributter`,
  `assosiasjoner` (i tillegg til `modellkataloger`, `informasjonsmodeller`,
  `aktoerer`, `kontaktpunkt`). **Opphavleg plan** foreslo éin delt,
  polymorf `egenskaper: range: Egenskap`-liste for både `Attributt`- og
  `Assosiasjon`-instansar — dette vart forkasta etter Steg 1 (BUG-8, sjå
  nedanfor) til fordel for separate, konkret-typa attributt pr. subklasse.
- **Inga eksisterande Python-introspeksjon av LinkML-skjemastruktur i repoet.**
  `gen-dqv-measurements.py` (nærmeste presedens) lèser berre *datafiler*
  (YAML-instansar) med `pyyaml` — det introspekterer ikkje klasser/slots i eit
  `.yaml`-*skjema*. MD5 krev derfor ny funksjonalitet: bruk av
  `linkml_runtime.utils.schemaview.SchemaView` til å gå gjennom klasser,
  slots, ranges og enums i kvart skjema.
- **`SchemaView`/`linkml`-pakken finst i `linkml-local`-imaget, ikkje
  `python-pytest`-imaget.** `gen-dqv-measurements.py` køyrer i dag via
  `$(PYTHON_RUN)` (`python-pytest`-imaget, berre `pyyaml`+`pytest`). Det nye
  skriptet må køyre via `$(LINKML_RUN)` (`linkml-local`-imaget, har
  `linkml==1.11.1` → `linkml_runtime` → `SchemaView`) i staden.

---

## Kartleggingsavklaringar (må avklares før Steg 1, sjå «Opne spørsmål»)

Dette er den komplekse delen av MD5 — å avgjere korleis vilkårlege
LinkML-skjemakonstruksjonar mappar til den ferdige ModellDCAT-modelldelen.
Forslag til mapping, grunngjeve i eksisterande modellerings­prinsipp
(CLAUDE.md):

| LinkML-konstruksjon | ModellDCAT-element | Grunngjeving |
|---|---|---|
| Konkret klasse (ikkje `abstract`, ikkje `mixin`, ikkje `tree_root`) | `Objekttype` | Standardtilfellet — ein klasse med eigenskapar |
| `tree_root: true`-containerklasse | *(ikkje generert)* | CLAUDE.md: containerklassen «er eit serialiseringsankerpunkt, ikkje ein semantisk klasse» |
| `abstract: true` / `mixin: true`-klasse | *(ikkje generert)* | Ikkje ein instansierbar domeneklasse |
| Klasse definert i **importert** skjema (t.d. `Aktoer`, `Konsept` frå common-ap-no/dcat-ap-no) | *(ikkje generert i det importerande skjemaet)* | Unngår at felles AP-NO-klasser dukkar opp dupliserte i alle 23 modellelement-sett — kvart skjema eksponerer berre det som er *definert* der (`SchemaView.all_classes(imports=False)`) |
| Slot med range = primitiv/innebygd type (`string`, `integer`, `date`, `LangString`, `uri`, `uriorcurie` …) | `Attributt` (`har_enkel_type` → delt `Enkeltype`-instans pr. XSD-type) | Verdieigenskap, ikkje relasjon |
| Slot med range = enum | `Attributt` (`har_verdi_fra` → generert `Kodeliste`) | Kontrollert vokabular |
| Slot med range = annan klasse, **ikkje** `inlined: true` (normaltilfellet, jf. «lenking fremfor inlining») | `Assosiasjon` (`refererer_til` → target-klassen sin `Objekttype`-id) | Referanse via URI, ikkje sammensetning |
| Slot med range = annan klasse, **`inlined: true`** | `Attributt` (`inneholder_objekttype` → target-klassen sin `Objekttype`-id) | Faktisk nøsta innhald |
| `enums:`-definisjon | `Kodeliste` | Kontrollert vokabular på skjemanivå |
| `permissible_values` i ein enum | `Kodeelement` (`kode` = verdien, `anbefalt_kodetekst`/`definisjon` = `description`) | Kvar tillaten verdi |
| `required: true` på slot | `nedre_multiplisitet: 1` (elles `0`) | minOccurs |
| `multivalued: true` på slot | `oevre_multiplisitet: "*"` (elles `"1"`) | maxOccurs |

**Ikkje dekt i v1 (eksplisitt utelate, ikkje feil):** `Rolle`, `Spesialisering`,
`Komposisjon`, `Realisering`, `Abstraksjon`, `Avhengighet`, `Samling`, `Valg`,
`Modul`, `Note`, `Begrensningsregel` — desse krev semantisk informasjon
LinkML ikkje uttrykker direkte (t.d. arv vert dekt av `is_a`, men
`Spesialisering` som eksplisitt `Egenskap`-instans er ekstra modellering vi
ikkje hentar ut automatisk). `Rotobjekttype` brukast ikkje i v1 — alle
konkrete klasser blir `Objekttype` (forenkling; kan revurderes seinare om
det er ønskjeleg å markere «hovudklassar» særskilt).

---

## Steg

### Steg 1 — Proof-of-concept på eitt skjema, verifiser polymorf inlining ✓

**Status: KRASJ STADFESTA — design må endres før Steg 2.**

Bygde ein handskriven test-instans (1 `Objekttype` i `objekttyper`, 1
`Attributt` + 1 `Assosiasjon` i `egenskaper`) direkte i
`kartverket-modellkatalog.yaml` (reverter etter test, ikkje committa).
Resultat:

- `mcp-validate POLICY=felles-datakatalog` / `linkml.validator.validate()`
  (jsonschema-basert): **valider feilfritt** (`errorCount: 0`) — JSON Schema-
  generatoren ekspanderer `range: Egenskap` til `anyOf` over alle subklassar,
  og strukturell matching lykkast utan typediskriminator.
- `linkml-convert --output-format ttl` / `yaml_loader.load(target_class=...)`
  (python-dataclass-basert, brukt for RDF/TTL-generering av datafiler):
  **hard krasj** — `TypeError: Egenskap.__init__() got an unexpected keyword
  argument 'refererer_til'`. Eit `@type`-diskriminatorfelt i dataen hjelper
  ikkje (`unexpected keyword argument '@type'`) — `yamlutils._normalize_inlined`
  instansierer alltid den statiske range-klassa, aldri ein subklasse.

Dokumentert som **BUG-8** (`specs/bugs/polymorphic-inlined-list-yaml-loader.md`,
indeksert i `specs/bugs/README.md`). Dette er ein ny variant av BUG-6/BUG-7-
familien (SchemaView/JSON-Schema-generatorar er polymorfi-medvitne;
SchemaLoader/YAML-baserte kodepatar er det ikkje).

**Konsekvens:** den planlagte containerstrukturen — éin delt
`egenskaper: range: Egenskap`-liste med blanding av `Attributt`- og
`Assosiasjon`-instansar — er **ikkje brukbar** slik den står, sidan
`linkml-convert`/RDF-generering av dei publiserte katalogdatafilene ville
krasje. Verifisert workaround (jf. BUG-8): gje konkrete subklassar eigne,
ikkje-delte containerattributt (t.d. `attributter: range: Attributt`,
`assosiasjoner: range: Assosiasjon` i staden for delt `egenskaper`).

Steg 2–6 i denne planen må derfor revurderes før dei held fram — sjå oppdatert
«Opne spørsmål»-seksjon. Originalt steg 1-forslag (sjå krysset-ut tekst i
git-historikk) er bevart for kontekst.

### Steg 2 — Legg til `kodeelementer` + del `egenskaper` i `attributter`/`assosiasjoner` ✓

**Avvik frå opphavleg plan (jf. BUG-8-funnet i Steg 1):** i tillegg til å
leggje til `kodeelementer`, vart den opphavleg planlagte delte
`egenskaper: range: Egenskap`-attributten **aldri lagt til** noko sted —
ho er erstatta direkte med to konkret-typa attributt, sidan den polymorfe
varianten ville krasja `linkml-convert`/RDF-generering.

Oppdaterte malen i `new-org-catalog.sh` (`attributes:`-blokka,
`ModellkatalogContainer`) med:
```yaml
kodeelementer:
  range: Kodeelement
  multivalued: true
  inlined: true
  inlined_as_list: true
attributter:
  range: Attributt
  multivalued: true
  inlined: true
  inlined_as_list: true
assosiasjoner:
  range: Assosiasjon
  multivalued: true
  inlined: true
  inlined_as_list: true
```
Patcha deretter alle 6 allereie-genererte `<org>-modellkatalog-schema.yaml`
(brreg, digdir, novari, ksdigital, skatteetaten, kartverket) med same
attributt-sett (erstatta deira `egenskaper`-attributt).

Verifisert: `make lint` (uendra føreeksisterande warnings, ingen nye),
`make mcp-validate POLICY=felles-datakatalog` for alle 6 (`errorCount: 0`),
`make roundtrip` for alle 6 (`roundtrip-json`/`roundtrip-ttl` OK).

**Tillegg oppdaga under Steg 3:** planen sin mappingtabell brukar delte
`Enkeltype`-instansar (`Attributt.har_enkel_type`), men ingen
containerattributt for `Enkeltype` fanst — verken i opphavleg plan eller i
eksisterande skjema. Lagt til `enkeltyper: range: Enkeltype, multivalued:
true, inlined: true, inlined_as_list: true` på `ModellkatalogContainer` i
malen og alle 6 skjema, ellers ville `har_enkel_type`-referansane vore
daudreferansar (peika på instansar som ikkje finst nokon stad i katalogen).
Verifisert på nytt med same kommandoar som over — ingen regresjon.

### Steg 3 — Skriv `gen-modelldcat-elements.py` ✓

Nytt skript `src/assets/scripts/gen-modelldcat-elements.py`, etter mønsteret
frå `update-modellkatalog.py` — `load_org_registry()`, `load_annotated_schemas()`,
`group_schemas_by_org()`, `find_catalog_data()`, `entry_name()` er importerte
direkte frå `update-modellkatalog.py` via `importlib` (ikkje duplisert).

Implementert som planlagt, med tre presiseringar/avvik:

1. **Range-klassifisering brukar `sv.get_class()`/`sv.get_enum()`** (med
   `strict=False`) i staden for å gjette frå namn — robust mot at `range`
   ikkje er sett eksplisitt (då fallar SchemaView attende til
   `default_range`, håndtert likt).
2. **Interne referansar krev at målklassen faktisk fekk ein `Objekttype`**
   (lokal **og** konkret — ikkje abstrakt/mixin), elles brukar
   `Assosiasjon.refererer_til`/`Attributt.inneholder_objekttype`
   skjema-URI-fallbacket (open spørsmål 3) i staden for ein daud
   `Objekttype`-referanse. Dette dekkjer **både** ekte eksterne klasser
   (importerte) **og** lokale abstrakte klasser brukt som range (reelt
   funne i `samt-bu`: `Skole.har_skoleeier → range: Skoleeier`, der
   `Skoleeier` er `abstract: true`) — planen sin tabell nemnde berre det
   første tilfellet.
3. **`Modellelement.har_egenskap`** (URI-referanseliste frå `Objekttype` til
   sine `Attributt`/`Assosiasjon`-instansar) er fylt ut for hver genererte
   `Objekttype` — nødvendig for at elementa skal være knytte saman (ikkje
   eksplisitt nemnt i planen sitt steg 3, men ein direkte konsekvens av
   mappingtabellen).

**ID-skjema** (under `{catalog_base}` = `modellkataloger[0].id`) er som
planlagt: `Objekttype` → `{catalog_base}/{skjemanavn}/{KlasseNavn}`,
`Attributt`/`Assosiasjon` → `{objekttype_id}/{slot_navn}`, `Kodeliste` →
`{catalog_base}/{skjemanavn}/{EnumNavn}`, `Kodeelement` →
`{kodeliste_id}/{permissible_value}`, delt `Enkeltype` →
`{catalog_base}/types/{type_navn}` (org-globalt, aldri fjerna — berre
union-mergea ved ny køyring via `merge_enkeltyper()`).

**Idempotens:** `replace_schema_scoped()` fjernar alle eksisterande element
med id-prefiks `{catalog_base}/{skjemanavn}/` før nye blir lagt til —
enklare og meir robust enn `gen-dqv-measurements.py` sin
tekstpatching-tilnærming, sidan denne skrivinga er strukturelt mykje større
(5 nye toppnivølister). Full `yaml.dump()` av heile katalogen ved skriving
(som `update-modellkatalog.py`), ikkje target tekstinnsetting.

**Bug funnen og fiksa under implementasjon:** `class_def.name`/`slot.name`/
`enum_name` (og `permissible_value.description`) er `linkml_runtime`-typar
som er `str`-subklassar (`ClassDefinitionName`, `extended_str`, m.fl.) —
`yaml.safe_dump()` feilar med ein useriliserbar `!!python/object/new`-tag
dersom dei skrivast direkte til datastrukturen. Fiksa ved å tvinge `str()`
konsekvent i `as_langstring_list()` og dei to direkte
`anbefalt_kodetekst`/`definisjon`-tilordningane i `build_kodeliste()`.

### Steg 4 — Makefile-mål `gen-modelldcat-elements` ✓

Lagt til i `Makefile` (etter `gen-dqv-measurements`), via `$(LINKML_RUN)`
(ikkje `$(PYTHON_RUN)`, sidan `SchemaView` krev `linkml`-pakken):
```makefile
gen-modelldcat-elements:
	$(LINKML_RUN) python3 src/assets/scripts/gen-modelldcat-elements.py $(if $(ORG),--org $(ORG)) $(if $(DRYRUN),--dry-run)
```
**Avvik frå plan:** bruk `make gen-modelldcat-elements ORG=<alias>
DRYRUN=1` i staden for `make gen-modelldcat-elements --dry-run` — Make sender
`--dry-run` til `make` sjølv (ikkje til skriptet), så planen sitt forslag om
direkte CLI-flagg-overlevering til `make` var ugyldig. Lagt til i
`.PHONY`-lista.

### Steg 5 — Køyr og verifiser ✓

1. Dry-run for éin org (`make gen-modelldcat-elements ORG=kartverket
   DRYRUN=1`), deretter for alle 6 (`make gen-modelldcat-elements DRYRUN=1`)
   — ingen exceptions, rimelege element-tal for alle 23 skjema.
2. Køyrt for reelt for alle 6 org (`make gen-modelldcat-elements`).
3. `make mcp-validate SCHEMA=... POLICY=felles-datakatalog INSTANCE=...` for
   alle 6 katalogar: `errorCount: 0` for alle.
4. `make roundtrip SCHEMA=...` for alle 6 (testar eksempelfila, jf. tidlegare
   funn): `roundtrip-json`/`roundtrip-ttl` OK for alle.
5. **Utvida verifisering** utover planen: køyrde `gen-python` +
   `yaml_loader.load(target_class=ModellkatalogContainer)` direkte på den
   **reelle, no-utfylte** datafila for kartverket — dette er den eksakte
   kodepatan som krasja under BUG-8 (Steg 1). Stadfesta: ingen `TypeError`,
   lastar 58 objekttyper/47 attributter/92 assosiasjoner korrekt. `gen-owl`
   og `gen-shacl` på skjemaet køyrde òg feilfritt (kun pre-eksisterande
   deprecation-warnings, ingen nye).
6. **Idempotens stadfesta:** re-køyrde `gen-modelldcat-elements ORG=kartverket`
   ein gong til — identiske element-tal etter andre køyring (ingen duplikat).
7. **Ikkje-regresjon stadfesta, men ikkje fiksa (utanfor scope):**
   `linkml-convert --output-format ttl` på den reelle kartverket-datafila
   krasjar med `ValueError: Unknown CURIE prefix: @base` — stadfesta via
   `git stash` at dette **allereie** skjedde før MD5-endringane (utløyst av
   eksisterande `tema: - TODO`-plassholderverdiar, ikkje av denne specen).
   Ikkje ein ny regresjon; uavhengig av BUG-8.

### Steg 6 — CI-integrasjon ✓

Brukar avklarte (2026-06-21): legg til i CI no, samme staden og same
utløysingspunkt som `gen-dqv-measurements` (`update-dates`-jobben i
`release-please.yml`, køyrer etter ein release er oppretta — `if:
releases_created == 'true'`).

**Avvik frå plan:** `gen-dqv-measurements` køyrer med plain `python3` +
`pip install pyyaml` direkte på runneren (ingen container), men
`gen-modelldcat-elements.py` krev `SchemaView` frå `linkml`-pakken, som er
for tungt å `pip install` direkte. Følgde i staden mønsteret frå
`capture-validation`-jobben (som hentar `mcp-linkml-validator`-imaget frå
GHCR): lagt til eit steg som `podman pull`ar det allereie publiserte
`ghcr.io/<owner>/linkml-local:latest`-imaget (bygd og pusha av
`release.yml`) og taggar det `localhost/linkml-local:latest`, deretter
køyrer skriptet via `podman run` (samme image som `$(LINKML_RUN)` brukar
lokalt). Lagt til to nye steg i `update-dates`-jobben («Hent
linkml-local-image frå GHCR», «Oppdater ModelDCAT-modellelement») mellom
DQV-steget og commit-steget; commit-steget sin melding er utvida til å
nemne modellelement-oppdateringa.

---

## Opne spørsmål — avklarte av brukar 2026-06-21

1. **Rotobjekttype-bruk:** ✓ avklart — alle konkrete klasser → `Objekttype`
   i v1. Ingen særskild `Rotobjekttype`-markering.
2. **Delte vs. skjema-lokale `Enkeltype`-instansar:** ✓ avklart — delte
   instansar pr. XSD-type **pr. org-katalog** (planen sitt opphavlege
   forslag), ikkje globalt på tvers av alle 6 katalogar.
3. **Eksterne/importerte ranges:** ✓ avklart — `Assosiasjon.refererer_til`
   peikar på **skjema-URI-en til klassen** (`class_uri` eller skjemaet sin
   `default_prefix` + klassenamn) for klasser definerte i importerte skjema
   (t.d. `common-ap-no`). Ingen `Objekttype`-stub genereres for desse.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit | Status |
|---|---|---|---|---|
| 1 | Proof-of-concept: polymorf `Egenskap`-inlining | `kartverket-modellkatalog.yaml` (test, reverted) | — | ✓ — krasja, dokumentert som BUG-8 |
| 2 | Legg til `kodeelementer`/`enkeltyper` + del `egenskaper` i `attributter`/`assosiasjoner` | `new-org-catalog.sh` + 6 eksisterande `<org>-modellkatalog-schema.yaml` | Steg 1 OK | ✓ |
| 3 | Skriv `gen-modelldcat-elements.py` | `src/assets/scripts/gen-modelldcat-elements.py` | Steg 2, opne spørsmål avklarte | ✓ |
| 4 | Makefile-mål (via `$(LINKML_RUN)`) | `Makefile` | Steg 3 | ✓ |
| 5 | Køyr for alle 6 org + valider | alle 6 `<org>-modellkatalog.yaml` | Steg 4 | ✓ |
| 6 | CI-integrasjon | `.github/workflows/release-please.yml` | Steg 5 | ✓ |

---

## Avhengigheiter

- Krev `linkml-local`-imaget (`$(LINKML_RUN)`), ikkje `python-pytest`
  (`$(PYTHON_RUN)`) — `SchemaView` finst berre i førstnemnde.
- Føresetnad: MD2 (alle 23 skjema registrerte i 6 org-katalogar) er allereie
  fullført — `gen-modelldcat-elements.py` skriv inn i `Informasjonsmodell`-
  oppføringar som MD2 oppretta.
- Uavhengig av MD6 (relasjon-slots for begrep/datasett) — ingen
  datadelt tilstand.
- Steg 1 (proof-of-concept) var ein hard føresetnad for Steg 2–5: polymorf
  inlining av `Egenskap`-subklassar krasja generatorane (BUG-8), og
  modelleringa er derfor revurdert — separate containerattributt
  (`attributter`, `assosiasjoner`) i staden for éin delt `egenskaper`-liste.
  Steg 2 implementerer denne revurderinga; Steg 3 sitt skript skal **aldri**
  skrive til ei delt polymorf liste.

---

## Utført

Alle 6 tiltak i den prioriterte handlingslista er fullførte og verifiserte
(2026-06-21). Sjå detaljerte avvik under hvert steg ovanfor; oppsummert:

1. **Proof-of-concept** stadfesta at éin delt, polymorf
   `egenskaper: range: Egenskap`-liste krasjar `linkml-convert`/RDF-generering
   (`yamlutils._normalize_inlined` instansierer alltid statisk range-klasse,
   aldri ein subklasse). Dokumentert som **BUG-8**
   (`specs/bugs/polymorphic-inlined-list-yaml-loader.md`).
2. Containerskjemaet (`new-org-catalog.sh` + alle 6 `<org>-modellkatalog-schema.yaml`)
   fekk konkret-typa attributt i staden: `kodeelementer`, `attributter`,
   `assosiasjoner`, og (oppdaga som manglande under Steg 3) `enkeltyper`.
   `egenskaper` blei aldri tatt i bruk.
3. Nytt skript `src/assets/scripts/gen-modelldcat-elements.py` — genererer
   `Objekttype`/`Attributt`/`Assosiasjon`/`Kodeliste`/`Kodeelement`/`Enkeltype`
   frå LinkML-skjemastruktur via `SchemaView`, idempotent, skriv inn i alle 6
   org-katalogdatafiler. To avvik frå plan: (a) interne referansar krev at
   målklassen er **konkret** (ikkje berre lokal) — lokale abstrakte klasser
   brukt som slot-range (funne i `samt-bu`) løyses via skjema-URI på same
   måte som ekte eksterne klasser; (b) `Modellelement.har_egenskap` fylt ut
   for å knyte `Objekttype` til sine `Attributt`/`Assosiasjon`-instansar.
4. Makefile-mål `gen-modelldcat-elements` (via `$(LINKML_RUN)`,
   `ORG=`/`DRYRUN=`-parametre i staden for planen sitt ugyldige
   `make ... --dry-run`-forslag).
5. Køyrt for alle 6 org. Validert: `make mcp-validate POLICY=felles-datakatalog`
   (`errorCount: 0` for alle 6), `make roundtrip` (OK for alle 6), direkte
   `gen-python`+`yaml_loader.load()`-test på reell produksjonsdata (stadfesta
   BUG-8 løyst), idempotens stadfesta ved dobbel køyring. Eit pre-eksisterande,
   ikkje-relatert `linkml-convert --output-format ttl`-problem
   (`Unknown CURIE prefix: @base`, utløyst av `tema: - TODO`-plassholderverdiar)
   blei identifisert og stadfesta **uendra** av denne specen (ikkje fiksa,
   utanfor scope).
6. CI-integrasjon i `update-dates`-jobben i `release-please.yml`: hentar
   publisert `linkml-local`-image frå GHCR (samme mønster som
   `capture-validation`-jobben) og køyrer skriptet via podman etter hver
   release.

**Filer endra:** `specs/bugs/polymorphic-inlined-list-yaml-loader.md` (ny),
`specs/bugs/README.md`, `src/assets/scripts/new-org-catalog.sh`,
`src/assets/scripts/gen-modelldcat-elements.py` (ny), `Makefile`,
`.github/workflows/release-please.yml`, 6× `<org>-modellkatalog-schema.yaml`,
6× `<org>-modellkatalog.yaml` (datafiler).
