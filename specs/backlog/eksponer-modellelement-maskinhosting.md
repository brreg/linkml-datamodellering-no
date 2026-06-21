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
- **Containerstrukturen er delvis klar.** `ModellkatalogContainer`
  (`new-org-catalog.sh`-malen) har allerede toppnivå-attributtane
  `objekttyper`, `kodelister`, `egenskaper` (i tillegg til
  `modellkataloger`, `informasjonsmodeller`, `aktoerer`, `kontaktpunkt`).
  **Mangler:** `kodeelementer` — `Kodeelement` er ein sjølvstendig klasse
  utan inlinert tilbakereferanse frå `Kodeliste` (`i_kodeliste` peikar berre
  éin veg, jf. lenking-fremfor-inlining-prinsippet), og trenger derfor eige
  serialiseringsankerpunkt på containeren, som i dag ikkje finst i nokon av
  dei 6 alleede-genererte katalogane.
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

### Steg 1 — Proof-of-concept på eitt skjema, verifiser polymorf inlining

**Risiko å avklare først:** Conteinerattributtet `egenskaper` har
`range: Egenskap` (abstrakt basisklasse) med `inlined_as_list: true`, og skal
i praksis innehalde ei blanding av `Attributt`- og `Assosiasjon`-instansar
(subklassar). Dette er akkurat den typen polymorf inlining/class-override
som har vist seg buggy tidlegare i denne importkjeda (BUG-6
`specs/bugs/dqv-standard-class-override.md`, BUG-7
`specs/bugs/duplicate-slot-merge-konflikt.md` — begge i `modelldcat-ap-no`-
eller nærliggande skjema). **Før noko skript skrivast:** lag ein liten,
handskriven test-instans med 1 `Objekttype`, 1 `Attributt` og 1 `Assosiasjon`
i `egenskaper`-lista i t.d. `kartverket-modellkatalog.yaml` (minste
katalogen), og køyr `make mcp-validate ... POLICY=felles-datakatalog` +
`make roundtrip` for å bekrefte at JSON Schema/SHACL/OWL-generering og
JSON-roundtrip toler dette utan å trigge ein ny BUG-6/7-variant. Dersom det
krasjar: dokumenter som ny BUG-X før Steg 2 held fram.

### Steg 2 — Legg til `kodeelementer` på `ModellkatalogContainer`

Oppdater malen i `new-org-catalog.sh` (linje ~107–136, `attributes:`-blokka)
med:
```yaml
kodeelementer:
  range: Kodeelement
  multivalued: true
  inlined: true
  inlined_as_list: true
```
Patch deretter alle 6 allereie-genererte `<org>-modellkatalog-schema.yaml`
(brreg, digdir, novari, ksdigital, skatteetaten, kartverket) med samme
attributt, sidan dei vart oppretta før denne planen.

### Steg 3 — Skriv `gen-modelldcat-elements.py`

Nytt skript i `src/assets/scripts/`, etter mønsteret frå
`update-modellkatalog.py` (gjenbruk `load_org_registry()`,
`load_annotated_schemas()`, `group_schemas_by_org()` via import — ikkje
dupliser skjema-/org-oppslagslogikk, jf. CLAUDE.md DRY-prinsippet).

For kvar `(org, schema)`-par frå `group_schemas_by_org()`:
1. `SchemaView(schema_path)`, hent `all_classes(imports=False)` og
   `all_enums(imports=False)` — berre lokalt definerte (sjå tabellen over).
2. For kvar konkret, ikkje-abstrakt, ikkje-mixin, ikkje-`tree_root`-klasse:
   bygg ein `Objekttype`-instans (`id`, `tittel`, `beskrivelse`).
3. For kvar slot på klassen (`sv.class_induced_slots(cls)`): avgjer
   `Attributt` vs. `Assosiasjon` per mapping-tabellen, bygg `Egenskap`-instans
   med multiplisitet.
4. For kvar lokal enum: bygg `Kodeliste` + ein `Kodeelement` pr.
   `permissible_value`.
5. Skriv alle genererte instansar inn i riktig org sin katalogdatafil
   (`objekttyper`, `egenskaper`, `kodelister`, `kodeelementer`), og sett
   `inneholder_modellelement` på den tilhøyrande `Informasjonsmodell`-
   oppføringa til lista av genererte `Objekttype`-id-ar for det skjemaet.
6. Idempotent skriving: identifiser eksisterande genererte element via stabil
   ID-skjema (under) og **erstatt** (ikkje dupliser) ved ny køyring — same
   prinsipp som `gen-dqv-measurements.py` sine stabile `.../dqv/<navn>`-id-ar.

**ID-skjema** (under `{catalog_base}` = `modellkataloger[0].id`):
- `Objekttype`: `{catalog_base}/{skjemanavn}/{KlasseNavn}`
- `Egenskap` (Attributt/Assosiasjon): `{objekttype_id}/{slot_navn}`
- `Kodeliste`: `{catalog_base}/{skjemanavn}/{EnumNavn}`
- `Kodeelement`: `{kodeliste_id}/{permissible_value}`
- Delte `Enkeltype`-instansar pr. XSD-type (t.d. `string`, `date`):
  éin global `{catalog_base}/types/{xsd-type}`, gjenbrukt av alle Attributt
  som peikar på samme primitive type (unngår eksplosjon av identiske
  Enkeltype-instansar).

### Steg 4 — Makefile-mål `gen-modelldcat-elements`

Legg til mål i `Makefile` (jf. `gen-dqv-measurements`-mønsteret, men via
`$(LINKML_RUN)` — **ikkje** `$(PYTHON_RUN)`, sidan `SchemaView` krev
`linkml`-pakken som berre finst i `linkml-local`-imaget):
```makefile
gen-modelldcat-elements:
	$(LINKML_RUN) python3 src/assets/scripts/gen-modelldcat-elements.py
```
Legg målet til i `.PHONY`-lista (linje ~248, samme stad som
`gen-dqv-measurements`).

### Steg 5 — Køyr og verifiser

1. `make gen-modelldcat-elements --dry-run` (legg til `--dry-run`-flagg i
   skriptet, same UX som `update-modellkatalog.py`) — sjekk omfang før
   skriving.
2. Køyr for reelt for alle 6 org.
3. `make mcp-validate SCHEMA=... POLICY=felles-datakatalog INSTANCE=...` for
   alle 6 katalogar — krav: `errorCount: 0`.
4. `make roundtrip SCHEMA=...` for å bekrefte JSON/TTL-generering framleis
   fungerer (NB: berre eksempelfila testast her, jf. funn i
   `avvik-veileder-modelldcat-ap-no.md` MD2 steg 4 — den reelle datafila er
   allereie dekt av BUG-1-skipet for desse 6 skjemaa).
5. `make domain-gen-owl DOMAIN=modellkatalog` (eller tilsvarande) for å
   stikkprøve at OWL/SHACL-generering ikkje krasjar med dei nye
   polymorfe `Egenskap`-instansane (jf. Steg 1-risikoen).

### Steg 6 — CI-vurdering (eige spørsmål, ikkje del av kjerneleveransen)

Bør `gen-modelldcat-elements` køyre automatisk i CI (t.d.
`release-please.yml`, jf. korleis `gen-dqv-measurements` er kopla inn der)
slik at modellelement alltid er oppdaterte etter ein skjemaendring? Dette
krev ei eiga avklaring av **når** i CI-flyten (etter merge til main? Etter
release?) og er medvite utelate frå kjerneleveransen i denne planen — kan
gjennomføres som eit tillegg når Steg 1–5 er verifiserte i praksis.

---

## Opne spørsmål (krev brukaravklaring før/under Steg 3)

1. **Rotobjekttype-bruk:** Skal nokon klasser markeres som `Rotobjekttype`
   (t.d. den klassen `tree_root`-containeren peikar mest direkte på), eller
   er «alle konkrete klasser → `Objekttype`» godt nok for v1? (Planen
   foreslår sistnevnte som standard.)
2. **Delte vs. skjema-lokale `Enkeltype`-instansar:** Planen foreslår globale,
   delte instansar pr. XSD-type pr. org-katalog (unngår duplikat). Er det i
   stedet ønskjeleg med éin global, delt instans pr. XSD-type **på tvers av
   alle 6 katalogar** (t.d. i ein 7. delt fil)? Det ville krevd ei eiga
   plassering utanfor per-org-strukturen.
3. **Eksterne/importerte ranges:** Når ein lokalt definert slot sin range er
   ein klasse frå eit **importert** skjema (t.d. ein `samt-bu`-slot med
   `range: Kommune` definert i `common-ap-no`) — skal `Assosiasjon` då peike
   på ein `Objekttype`-id som ikkje finst i noko katalog (sidan
   `common-ap-no` sine klasser ikkje genererer eigne `Objekttype`-ar, jf.
   tabellen)? Forslag: peik på sjølve **skjema-URI-en til klassen**
   (`class_uri` eller skjemaet sin `default_prefix` + klassenamn) som ein
   ekstern referanse, i tråd med lenking-fremfor-inlining — men dette bør
   stadfestast før implementasjon.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | Proof-of-concept: polymorf `Egenskap`-inlining | `kartverket-modellkatalog.yaml` (test) | — |
| 2 | Legg til `kodeelementer` på containerskjemaet | `new-org-catalog.sh` + 6 eksisterande `<org>-modellkatalog-schema.yaml` | Steg 1 OK |
| 3 | Skriv `gen-modelldcat-elements.py` | `src/assets/scripts/gen-modelldcat-elements.py` | Steg 2, opne spørsmål avklarte |
| 4 | Makefile-mål (via `$(LINKML_RUN)`) | `Makefile` | Steg 3 |
| 5 | Køyr for alle 6 org + valider | alle 6 `<org>-modellkatalog.yaml` | Steg 4 |
| 6 | CI-vurdering (eige tillegg) | `.github/workflows/release-please.yml` | Steg 5 |

---

## Avhengigheiter

- Krev `linkml-local`-imaget (`$(LINKML_RUN)`), ikkje `python-pytest`
  (`$(PYTHON_RUN)`) — `SchemaView` finst berre i førstnemnde.
- Føresetnad: MD2 (alle 23 skjema registrerte i 6 org-katalogar) er allereie
  fullført — `gen-modelldcat-elements.py` skriv inn i `Informasjonsmodell`-
  oppføringar som MD2 oppretta.
- Uavhengig av MD6 (relasjon-slots for begrep/datasett) — ingen
  datadelt tilstand.
- Steg 1 (proof-of-concept) er ein hard føresetnad for Steg 2–5: dersom
  polymorf inlining av `Egenskap`-subklassar krasjar generatorane, må
  modelleringa (kanskje separate containerattributt pr. Egenskap-subklasse
  i staden for éin delt `egenskaper`-liste) revurderes før skriptet skrivast.
