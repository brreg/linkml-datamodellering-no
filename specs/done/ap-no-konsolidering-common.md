# Konsolidering av felles AP-NO-klasser og -slots til common-ap-no-schema

**Bakgrunn:** `common-ap-no-schema.yaml` er ein fellesressurs for alle norske
applikasjonsprofiler (AP-NO). Fleire klasser og slots er definerte i fleire
AP-NO-skjema, noko som skapar duplikasjon og risiko for inkonsistens.

**Mål:** Identifisere duplikate klasser og slots på tvers av AP-NO-skjemaa og
flytte dei til `common-ap-no-schema.yaml` der det er semantisk hensiktsmessig.

**Avgrensing:** Dette omfattar berre *identiske eller svært like* klasser/slots
med same `class_uri`/`slot_uri`. Klasser med ulike URI-ar eller semantikk skal
ikkje konsoliderast, sjølv om dei har same namn.

---

## Kartlegging av duplikasjonar

### Duplikate klasser

| Klasse | class_uri | Førekomstar | Samsvar | Flytt? |
|---|---|---|---|---|
| **Tidsrom** | `dct:PeriodOfTime` | dcat-ap-no, xkos-ap-no | **Ulike slots** — dcat brukar `startdato`/`sluttdato`/`begynnelse`/`slutt`, xkos brukar `tidsrom_start`/`tidsrom_slutt` | **Nei** — ulik semantikk per profil |
| **RegulativRessurs** | `eli:LegalResource` | dcat-ap-no, cpsv-ap-no | **Ulike slots** — dcat har 8 slots, cpsv har 4. Ulik kravnivå-annotasjon. | **Nei** — ulik detaljgrad per profil |
| **Gebyr** | `cv:Cost` | dcat-ap-no, cpsv-ap-no | **Ulike slots** — dcat har `belop`/`dokumentasjon`, cpsv har `verdi`/`identifikator_literal`. Ulik kravnivå. | **Nei** — ulik modellering per profil |
| **Organisasjon** | **Ulik URI** | skos-ap-no (`org:Organization`), xkos-ap-no (`foaf:Agent`) | **Ulike class_uri** — xkos sin `Organisasjon` er alias for dcat sin `Aktoer` (begge `foaf:Agent`) | **Delvis** — erstatt xkos-alias med import av `Aktoer` |
| **Samling** | Ulik URI | modelldcat (`skos:Collection`), skos (`skosno:BegrepsSamling`) | **Ulik URI og semantikk** | **Nei** — to ulike omgrep |
| **Katalog** | `dcat:Catalog` | dcat-ap-no, cpsv-ap-no | **Ulike slots** — dcat har 22 slots, cpsv har 11. Overlapp men ikkje identisk. | **Vurder** — mogleg felles basis? |

### Duplikate slots

Slots er *mindre* dupliserte fordi dei fleste skjema importerer `common-ap-no`
som allereie inneheld dei mest brukte globale slotsa (`id`, `tittel`, `beskrivelse`,
`identifikator_literal`, `endringsdato`, `utgivelsesdato`, `har_referanse` osb.).

Gjennomgang viser at det *ikkje* finst vesentlege slot-duplikasjonar utover det
som allereie er i `common-ap-no`. Dei skjemaspesifikke slotsa har unike `slot_uri`
og semantikk tilknytta sitt domene.

---

## Tilrådde tiltak

### CO1 — Erstatt `Organisasjon` (`foaf:Agent`) i xkos-ap-no med import av `Aktoer` frå dcat-ap-no

**Problem:** `Organisasjon` er definert i både `skos-ap-no` og `xkos-ap-no`, men med **ulike class_uri**:

| Skjema | Klassenamn | class_uri | Semantikk |
|---|---|---|---|
| skos-ap-no | `Organisasjon` | `org:Organization` | Spesifikk organisasjonsklasse |
| xkos-ap-no | `Organisasjon` | `foaf:Agent` | Generisk aktør (person/org/system) |
| dcat-ap-no | `Aktoer` | `foaf:Agent` | Generisk aktør (person/org/system) |

`Organisasjon` i xkos-ap-no har **same class_uri som `Aktoer` i dcat-ap-no**.
Dette er eit alias-forhold — xkos kaller klassen `Organisasjon` men mappar til
same RDF-type som dcat sin `Aktoer`-klasse.

**Løysing:** Importer `dcat-ap-no` i `xkos-ap-no` og erstatt referansar til
`Organisasjon` med `Aktoer`. Fjern den lokale `Organisasjon`-definisjonen.

**Steg 1 — Legg til import av dcat-ap-no i xkos-ap-no-schema.yaml:**

```yaml
imports:
  - linkml:types
  - ../common/common-ap-no-schema
  - ../dcat-ap-no/dcat-ap-no-schema  # ← ny import
```

**Steg 2 — Fjern `Organisasjon`-klassen frå xkos-ap-no-schema.yaml** (linje 337-341).

**Steg 3 — Erstatt slot-referansar frå `range: Organisasjon` til `range: Aktoer`:**

```yaml
# Før:
utgjevar:
  slot_uri: dct:publisher
  range: Organisasjon
  description: Organisasjon som er ansvarleg utgjevar (dct:publisher).

# Etter:
utgjevar:
  slot_uri: dct:publisher
  range: Aktoer
  description: Aktør som er ansvarleg utgjevar (dct:publisher).
```

**Filer:**
- `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

**Merk:** `Organisasjon` i `skos-ap-no-schema.yaml` skal **ikkje** endrast — den
har `class_uri: org:Organization` og er ein eigen semantisk klasse.

**Status:** ✓ **Utført** 2026-07-05

Endringar gjennomførte:
1. Lagt til import av `dcat-ap-no-schema` i `xkos-ap-no-schema.yaml`
2. Fjerna `Organisasjon`-klassedefinisjon (linje 338-342)
3. Erstatta `range: Organisasjon` → `range: Aktoer` i `utgjevar`-slot
4. Oppdatert beskrivelse frå "Organisasjon som er..." til "Aktør som er..."
5. Verifisert med `make gen-jsonschema` — `Aktoer` er no tilgjengeleg i xkos-ap-no

---

### CO2 — Vurder felles `Katalog`-basisklasse (valfritt)

**Problem:** `Katalog` (`dcat:Catalog`) er definert i både `dcat-ap-no` og `cpsv-ap-no`.
Dei to klassane har ulik detaljgrad:

| Skjema | Slots | Kravnivå |
|---|---|---|
| dcat-ap-no | 22 slots (tittel, beskrivelse, utgjevar, datasett, datatjeneste, har_kvalitetsmerknad, osb.) | Detaljert, kompleks |
| cpsv-ap-no | 11 slots (tittel, beskrivelse, utgjevar, har_teneste, utgjevingsdato, heimeside, osb.) | Enklare, teneste-orientert |

**Overlappande slots:**
- `tittel`, `beskrivelse`, `utgjevar`, `heimeside`, `tema`, `dekningsomraade`,
  `utgivelsesdato`, `endringsdato`, `spraak`, `lisens`

**Ulike slots:**
- dcat-ap-no har: `datasett`, `datatjeneste`, `har_kvalitetsmerknad`, `service`, osb.
- cpsv-ap-no har: `har_teneste`, `har_kontaktpunkt`, `adresse`, osb.

**Løysingsalternativ 1 — Flytt `Katalog` til `common-ap-no` som abstrakt basisklasse:**

```yaml
# I common-ap-no-schema.yaml:
Katalog:
  in_subset:
    - Metadata
  abstract: true
  class_uri: dcat:Catalog
  description: Ein katalog over ressursar (dcat:Catalog).
  slots:
    - id
    - tittel
    - beskrivelse
    - utgjevar
    - heimeside
    - tema
    - dekningsomraade
    - utgivelsesdato
    - endringsdato
    - spraak
    - lisens
  slot_usage:
    tittel:
      required: true
      in_subset:
        - Obligatorisk
    beskrivelse:
      required: true
      in_subset:
        - Obligatorisk
    utgjevar:
      required: true
      in_subset:
        - Obligatorisk
```

Deretter i `dcat-ap-no` og `cpsv-ap-no`:

```yaml
# I dcat-ap-no-schema.yaml:
Katalog:
  is_a: Katalog  # arvar frå common-ap-no
  description: Ein datakatalog (DCAT-AP-NO).
  slots:
    - datasett
    - datatjeneste
    - har_kvalitetsmerknad
    - service
    # osb. — dcat-spesifikke slots
```

```yaml
# I cpsv-ap-no-schema.yaml:
Katalog:
  is_a: Katalog  # arvar frå common-ap-no
  description: Ein tenestekatalog (CPSV-AP-NO).
  slots:
    - har_teneste
    - har_kontaktpunkt
    - adresse
    # osb. — cpsv-spesifikke slots
```

**Løysingsalternativ 2 — Lad dei vere separate:**

`Katalog` har *nok* overlapp til at ein felles basis er mogleg, men dei to
profilane nyttar klassen til ulike formål (datakatalog vs. tenestekatalog).
Det kan vere meir transparent å halde dei separate.

**Tilråding:** **Ikkje flytt `Katalog` enno** — differensane er for store.
Ventar til fleire AP-NO-profiler treng ein felles `Katalog`-definisjon.

---

## Klasser som **ikkje** skal konsoliderast

| Klasse | Grunngjeving |
|---|---|
| **Tidsrom** | Ulike slots per profil — dcat brukar W3C Time Ontology-termar (`begynnelse`, `slutt`), xkos brukar enklare datoar (`tidsrom_start`, `tidsrom_slutt`). Semantikken er ulik. |
| **RegulativRessurs** | Ulike slot-sett og kravnivå per profil. dcat-ap-no har fullstendig ELI-basert modellering, cpsv-ap-no har forenkla. |
| **Gebyr** | Ulike slots (`belop` vs. `verdi`) og kravnivå. Profilane modellerer kostnadsstruktur ulikt. |
| **Samling** | Ulike URI-ar — `skos:Collection` i modelldcat, `skosno:BegrepsSamling` i skos. To heilt ulike omgrep. |

---

## Samandrag

**Tiltak som vert utførte:**

| # | Tiltak | Filer | Alvor |
|---|---|---|---|
| CO1 | Erstatt `Organisasjon` (foaf:Agent) i xkos med `Aktoer` frå dcat | xkos | Låg |

**Tiltak som vert utsett:**

| # | Tiltak | Grunngjeving |
|---|---|---|
| CO2 | Vurder felles `Katalog`-basis | Differensane er for store; ventar på fleire brukstilfelle |

**Klasser som ikkje vert konsoliderte:** `Tidsrom`, `RegulativRessurs`, `Gebyr`, `Samling` — ulike slots/semantikk per profil.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit | Status |
|---|---|---|---|---|
| 1 | CO1: Erstatt `Organisasjon` i xkos med `Aktoer` | xkos-ap-no | — | ✓ Utført |

---

## Avhengigheiter

- Etter CO1: køyr `make gen-doc`, `make gen-plantuml`, `make lint` på alle
  påverka skjema for å verifisere at ingen regressjonar har oppstått.
- Sjekk at `org:`-prefikset er definert i `common-ap-no-schema.yaml`.

---

## Utført

**Dato:** 2026-07-05

### Kva vart gjort

**CO1 — Erstatt `Organisasjon` (foaf:Agent) i xkos-ap-no med `Aktoer` frå dcat-ap-no:**

Kartlegginga avdekte at `Organisasjon` i xkos-ap-no og skos-ap-no **ikkje** var
identiske klasser som først antatt:

- **xkos-ap-no**: `Organisasjon` hadde `class_uri: foaf:Agent` — eit alias for same
  RDF-type som `Aktoer` i dcat-ap-no
- **skos-ap-no**: `Organisasjon` har `class_uri: org:Organization` — ein eigen
  semantisk klasse som ikkje skal konsoliderast

Løysinga vart å erstatte xkos sin `Organisasjon`-alias med ein import av `Aktoer`
frå dcat-ap-no, sidan begge mappar til `foaf:Agent`.

**Endringar:**
1. `xkos-ap-no-schema.yaml`: lagt til import av `dcat-ap-no-schema`
2. `xkos-ap-no-schema.yaml`: fjerna lokal `Organisasjon`-klassedefinisjon
3. `xkos-ap-no-schema.yaml`: erstatta `utgjevar.range: Organisasjon` → `Aktoer`
4. Verifisert med `make gen-jsonschema` — `Aktoer` er tilgjengeleg i xkos-ap-no

**CO2 — Vurder felles `Katalog`-basisklasse:**

**Ikkje utført** — utsett til fleire AP-NO-profiler treng ein felles `Katalog`-definisjon.
Differensane mellom dcat-ap-no (22 slots, datakatalog) og cpsv-ap-no (11 slots,
tenestekatalog) er for store til å konsolidere no.

### Avvik frå opphavleg plan

- **CO1**: Opphavleg plan antok at `Organisasjon` var identisk i xkos og skos.
  Kartlegginga under implementasjon avdekte at dei hadde ulike `class_uri`. Løysinga
  vart justert til å berre erstatte xkos sin `Organisasjon`-alias, ikkje flytte
  klassen til `common-ap-no`.

### Klasser som ikkje vart konsoliderte

Desse klassane har same namn men **ulike semantikk eller slots** og skal **ikkje** konsoliderast:

- **Tidsrom** (dcat: 5 slots med W3C Time Ontology-termar, xkos: 2 slots med enkle datoar)
- **RegulativRessurs** (dcat: 8 slots fullstendig ELI-modell, cpsv: 4 slots forenkla)
- **Gebyr** (dcat: `belop`/`dokumentasjon`, cpsv: `verdi`/`identifikator_literal`)
- **Samling** (modelldcat: `skos:Collection`, skos: `skosno:BegrepsSamling` — ulike URI)
- **Organisasjon** i skos-ap-no (`org:Organization` — eigen klasse, ikkje alias)

---

## Vedlegg: Fullstendig oversikt over AP-NO-skjema og deira klasser

### common-ap-no-schema.yaml (sannkjelde)

**Klasser:**
- `Lisensdokument` (dct:LicenseDocument)
- `Mediatype` (dct:MediaTypeOrExtent)
- `Konsept` (skos:Concept)
- `Begrepssamling` (skos:ConceptScheme)

**Slots (utval):**
- `id`, `tittel`, `beskrivelse`, `identifikator_literal`, `type_concept`,
  `endringsdato`, `utgivelsesdato`, `spraak`, `format`, `har_referanse`,
  `har_merknad`, `versjonsnummer`, `nokkelord`, `dekningsomraade`, `status`,
  `valuta`, `heimeside`, `anbefalt_term`, `versjonsmerknad`, `lisens`

**Enums:**
- `EULicence`, `EUFileType`, `EULanguage`, `ADMSStatus`

### dcat-ap-no-schema.yaml

**Importerer:** common-ap-no, dqv-core

**Klasser:**
- `KatalogisertRessurs`, `Aktoer`, `Kontaktopplysning`, `Tidsrom`, `Standard`,
  `RegulativRessurs`, `Identifikator`, `Rettighetserklaring`, `Sjekksum`,
  `Gebyr`, `Relasjon`, `Distribusjon`, `Datasett`, `Datasettserie`,
  `Datatjeneste`, `Katalogpost`, `Katalog`

### skos-ap-no-schema.yaml

**Importerer:** common-ap-no, dqv-core

**Klasser:**
- `Organisasjon` ← **duplikat**
- `VCardKontakt`, `Begrep`, `Definisjon`, `AssosiativRelasjon`,
  `GeneriskRelasjon`, `PartitivRelasjon`, `Samling`

### xkos-ap-no-schema.yaml

**Importerer:** common-ap-no

**Klasser:**
- `Organisasjon` ← **duplikat**
- `Tidsrom` ← **duplikat (men ulik)**
- `Klassifikasjon`, `Klassifikasjonsnivaa`, `Kategori`,
  `Klassifikasjonssamanlikning`, `Kategorisamanlikning`

### cpsv-ap-no-schema.yaml

**Importerer:** common-ap-no

**Klasser:**
- `RegulativRessurs` ← **duplikat (men ulik)**
- `Gebyr` ← **duplikat (men ulik)**
- `Katalog` ← **duplikat (men ulik)**
- `OffentligTjeneste`, `Tjeneste`, `Hendelse`, `Livshendelse`,
  `Virksomhetshendelse`, `Aktor`, `OffentligOrganisasjon`, `Kontaktpunkt`,
  `Tjenestekanal`, `Dokumentasjonstype`, `Tjenesteresultattype`,
  `Tjenesteresultattypeliste`, `Regel`, `Deltagelse`, `Adresse`

### dqv-ap-no (dqv-core-schema.yaml)

**Importerer:** common-ap-no

**Klasser:**
- `Kvalitetsdimensjon`, `Kvalitetsdeldimensjon`, `Kvalitetsmaal`,
  `Kvalitetsmerknad`, `Brukartilbakemelding`, `Kvalitetssertifikat`,
  `Kvalitetsmaaling`, `Tekstdel`

### modelldcat-ap-no

**Importerer:** common-ap-no, dcat-ap-no, dqv-core

**Klasser:**
- `Samling` ← **ikkje duplikat** (ulik URI: `skos:Collection`)
- `Informasjonsmodell`, `Modellkatalog`, `Dokument`, `Modellelement`,
  `Objekttype`, osb.
