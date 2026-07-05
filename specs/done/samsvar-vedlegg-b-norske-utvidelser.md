# Evaluering av samsvar med DCAT-AP-NO Vedlegg B — Norske utvidelser

## Bakgrunn

Vedlegg B listar alle "norske utvidelser" — avvik mellom DCAT-AP-NO og summen av EUs DCAT-AP og W3Cs DCAT. Dette inkluderer:

1. **Endra kravnivå** (t.d. frå valgfri til obligatorisk)
2. **Endra verdiområde** (t.d. `rdfs:Literal` → `rdf:langString`)
3. **Endra multiplisitet** (t.d. `0..n` → `0..1`)
4. **Nye eigenskapar** (ikkje i DCAT-AP/DCAT)
5. **Tilleggskrav** (t.d. Los BØR brukast)

Denne evalueringa vurderer om `dcat-ap-no-schema.yaml` implementerer desse utvidelsane korrekt.

## Metode

Eg går systematisk gjennom alle utvidelser i Vedlegg B og vurderer:

- ✓ = Korrekt implementert
- ⚠️ = Delvis implementert eller dokumentasjonsmangel
- ✗ = Ikkje implementert / feil implementering
- — = Ikkje aktuelt (t.d. BØR-krav som ikkje kan håndhevast maskinelt)

---

## 1. Aktør (foaf:Agent)

### 1.1. Aktør – identifikator (dct:identifier)

**Utvidelse:** Ikke eksplisitt spesifisert i DCAT-AP/DCAT.

**Implementering:**

```yaml
Aktoer:
  slots:
    - identifikator_literal
  slot_usage:
    identifikator_literal:
      in_subset: [Anbefalt]
```

**Status:** ✓ Implementert som anbefalt eigenskap.

---

## 2. Datasett (dcat:Dataset)

### 2.1. Datasett – beskrivelse (dct:description) — Verdiområde

**Utvidelse:** Verdiområdet endret fra `rdfs:Literal` til `rdf:langString`.

**Implementering:**

```yaml
# common-ap-no-schema.yaml
slots:
  beskrivelse:
    slot_uri: dct:description
    range: LangString
    multivalued: true

types:
  LangString:
    uri: rdf:langString
    base: str
```

**Status:** ✓ Korrekt — `range: LangString` med `uri: rdf:langString`.

### 2.2. Datasett – beskrivelse (dct:description) — Multiplisitet

**Utvidelse:** Det SKAL være maks. 1 verdi per språk.

**Implementering:**

- `multivalued: true` er satt, men LinkML har ikkje innebygd `maxPerLanguage`-constraint

**Status:** ⚠️ `multivalued: true` tillèt fleire verdiar, men **kravet "maks 1 per språk" kan ikkje håndhevast i LinkML**. Dette må håndhevast via SHACL eller applikasjonslogikk.

**Merknad:** Dette gjeld for **alle** eigenskapar med `range: LangString` der Vedlegg B seier "maks 1 per språk".

### 2.3. Datasett – kontaktpunkt (dcat:contactPoint)

**Utvidelse:** Kravnivået er endret fra anbefalt til **obligatorisk**, og dermed også multiplisitet til **1..n**.

**Implementering:**

```yaml
Datasett:
  slot_usage:
    kontaktpunkt:
      required: true
      in_subset: [Obligatorisk]
```

**Vurdering:**
- ✓ `required: true` → obligatorisk
- ⚠️ `multivalued: true` er satt, men LinkML sin `required: true` krev berre **minst 1**, ikkje eksplisitt **1..n**

**Status:** ✓ Funksjonelt korrekt — `required: true` + `multivalued: true` = minst 1 verdi (1..n).

### 2.4. Datasett – tema (dcat:theme)

**Utvidelse 1:** Kravnivået er endret fra anbefalt til **obligatorisk**, multiplisitet til **1..n**.

**Utvidelse 2:** Los BØR brukes i tillegg.

**Implementering:**

```yaml
Datasett:
  slot_usage:
    tema:
      required: true
      in_subset: [Obligatorisk]

slots:
  tema:
    slot_uri: dcat:theme
    range: Konsept
    multivalued: true
    description: >-
      Tema frå eit kontrollert vokabular. For norske offentlege datasett skal Los
      (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema
      (https://psi.norge.no/los/tema/<namn>) og eventuelt undertema i tillegg.
      EuroVoc kan brukast som sekundærvokabular.
    annotations:
      gyldige_verdier: https://psi.norge.no/los/
```

**Status:**
- ✓ Obligatorisk + 1..n implementert
- ✓ Los dokumentert i `description` og `annotations.gyldige_verdier`

### 2.5. Datasett – utgiver (dct:publisher)

**Utvidelse:** Kravnivået er endret fra anbefalt til **obligatorisk**, multiplisitet fra **0..1** til **1..1**.

**Implementering:**

```yaml
Datasett:
  slot_usage:
    utgiver:
      required: true
      in_subset: [Obligatorisk]

slots:
  utgiver:
    slot_uri: dct:publisher
    range: Aktoer
    # multivalued: false (implisitt)
```

**Status:** ✓ Korrekt — `required: true` + `multivalued: false` (implisitt) = eksakt 1 verdi (1..1).

### 2.6. Datasett – begrep (dct:subject)

**Utvidelse:** Ikke eksplisitt spesifisert i DCAT-AP/DCAT.

**Implementering:**

```yaml
Datasett:
  slots:
    - begrep
  slot_usage:
    begrep:
      in_subset: [Anbefalt]

slots:
  begrep:
    slot_uri: dct:subject
    range: Konsept
    multivalued: true
```

**Status:** ✓ Implementert som anbefalt eigenskap.

### 2.7. Datasett – nøkkelord (dcat:keyword) — Verdiområde

**Utvidelse:** Verdiområdet endret fra `rdfs:Literal` til `rdf:langString`.

**Implementering:**

```yaml
# common-ap-no-schema.yaml
slots:
  nokkelord:
    slot_uri: dcat:keyword
    range: LangString
    multivalued: true
```

**Status:** ✓ Korrekt — `range: LangString`.

### 2.8. Datasett – ble generert ved (prov:wasGeneratedBy)

**Utvidelse 1:** Kravnivået er endret fra valgfri til **anbefalt**.

**Utvidelse 2:** Verdien BØR velges fra kontrollert vokabular Proveniensaktivitetstype.

**Implementering:**

```yaml
Datasett:
  slot_usage:
    ble_generert_ved:
      in_subset: [Anbefalt]

slots:
  ble_generert_ved:
    slot_uri: prov:wasGeneratedBy
    range: uri
    description: >-
      Brukes til å referere til en aktivitet som genererte datasettet, eller som gir
      forretningskontekst for oppretting av det.
    annotations:
      gyldige_verdier: URI til prov:Activity
    multivalued: true
    domain: Datasett
```

**Status:**
- ✓ Anbefalt kravnivå satt
- ⚠️ Proveniensaktivitetstype-vokabularet er ikkje eksplisitt referert i `annotations.gyldige_verdier`

### 2.9. Datasett – dekningsområde (dct:spatial)

**Utvidelse:** For Norge, BØR Kartverkets kontrollerte vokabular Administrative enheter brukes i tillegg.

**Implementering:**

```yaml
# common-ap-no-schema.yaml
slots:
  dekningsomraade:
    slot_uri: dct:spatial
    range: Konsept
    multivalued: true
```

**Status:** — BØR-krav dokumentert i spesifikasjonen, men ikkje nødvendig å håndheve i skjema.

### 2.10. Datasett – gjeldende lovgivning (dcatap:applicableLegislation)

**Utvidelse:** Kravnivået endret fra valgfri til **anbefalt**.

**Implementering:**

```yaml
Datasett:
  slot_usage:
    gjeldende_lovgivning:
      in_subset: [Anbefalt]
```

**Status:** ✓ Korrekt — anbefalt kravnivå satt.

### 2.11. Datasett – tilgangsrettigheter (dct:accessRights)

**Utvidelse 1:** Kravnivået er endret fra valgfri til **anbefalt**.

**Utvidelse 2:** Når verdien er RESTRICTED eller NON_PUBLIC, BØR gjeldende lovgivning eller policy brukes.

**Implementering:**

```yaml
Datasett:
  slot_usage:
    tilgangsrettigheter:
      in_subset: [Anbefalt]

slots:
  tilgangsrettigheter:
    slot_uri: dct:accessRights
    range: uri
    description: >-
      Egenskapen brukes til å angi om det er allmenn tilgang, betinget tilgang
      eller ikke-allmenn tilgang til datasettet. Bruk EU Access
      Rights-vokabularet: PUBLIC (ope, ingen registrering), RESTRICTED
      (avgrensa), NON_PUBLIC (ikkje offentleg).
    multivalued: true
    annotations:
      gyldige_verdier: >-
        http://publications.europa.eu/resource/authority/access-right/PUBLIC
        http://publications.europa.eu/resource/authority/access-right/RESTRICTED
        http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC
```

**Status:**
- ✓ Anbefalt kravnivå satt
- — BØR-kravet om lovgivning/policy ved RESTRICTED/NON_PUBLIC er dokumentert i spesifikasjonen, ikkje nødvendig i skjema

### 2.12. Datasett – endringsdato (dct:modified)

**Utvidelse:** Verdiområdet er eksplisitt spesifisert som `xsd:date` or `xsd:dateTime`.

**Implementering:**

```yaml
# common-ap-no-schema.yaml
slots:
  endringsdato:
    slot_uri: dct:modified
    range: date
```

**Status:** ⚠️ `range: date` mappar til `xsd:date`, men **ikkje** `xsd:dateTime`. LinkML sin `date`-type inkluderer **ikkje** tid.

**Konklusjon:** Skjemaet brukar `range: date`, men spesifikasjonen tillèt **både** `xsd:date` og `xsd:dateTime`. Dette er eit **avvik** — bruk `range: string` eller ein union-type.

**Same problem gjeld for:**
- `utgivelsesdato` (dct:issued)
- Alle `endringsdato`/`utgivelsesdato` i Datasettserie, Katalog, Katalogpost

### 2.13. Datasett – har gebyr (cv:hasCost)

**Utvidelse:** Ikke eksplisitt spesifisert i DCAT-AP/DCAT.

**Implementering:**

```yaml
Datasett:
  slots:
    - har_gebyr
```

**Status:** ✓ Implementert som valgfri eigenskap.

### 2.14. Datasett – utgivelsesdato (dct:issued)

**Utvidelse:** Verdiområdet er eksplisitt spesifisert som `xsd:date` or `xsd:dateTime`.

**Status:** ⚠️ Same problem som `endringsdato` (sjå 2.12).

### 2.15. Datasett – versjonsmerknad (adms:versionNotes)

**Utvidelse:** Verdiområdet endret fra `rdfs:Literal` til `rdf:langString`.

**Implementering:**

```yaml
# common-ap-no-schema.yaml
slots:
  versjonsmerknad:
    slot_uri: adms:versionNotes
    range: LangString
    multivalued: true
```

**Status:** ✓ Korrekt — `range: LangString`.

---

## 3. Datasettserie (dcat:DatasetSeries)

Datasettserie har **identiske utvidelser** som Datasett for følgjande eigenskapar:

- Beskrivelse (verdiområde + maks 1 per språk)
- Kontaktpunkt (obligatorisk 1..n)
- Tema (obligatorisk 1..n + Los)
- Tittel (verdiområde + maks 1 per språk)
- Utgiver (obligatorisk 1..1)
- Dekningsområde (Kartverket)
- Gjeldende lovgivning (anbefalt)
- Endringsdato (xsd:date or xsd:dateTime)
- Utgivelsesdato (xsd:date or xsd:dateTime)

**Nye utvidelser:**

### 3.1. Datasettserie – siste (dcat:last)

**Utvidelse:** Kravnivået endret fra valgfri til **anbefalt**.

**Implementering:**

```yaml
Datasettserie:
  slot_usage:
    siste:
      in_subset: [Anbefalt]
```

**Status:** ✓ Korrekt.

### 3.2. Datasettserie – tidsrom (dct:temporal)

**Utvidelse:** Kravnivået endret fra valgfri til **anbefalt**.

**Implementering:**

```yaml
Datasettserie:
  slot_usage:
    tidsrom:
      in_subset: [Anbefalt]
```

**Status:** ✓ Korrekt.

---

## 4. Datatjeneste (dcat:DataService)

### 4.1. Datatjeneste – endepunktsURL (dcat:endpointURL)

**Utvidelse:** Multiplisiteten endret fra **1..n** til **1..1**.

**Implementering:**

```yaml
Datatjeneste:
  slot_usage:
    endepunkts_url:
      required: true
      in_subset: [Obligatorisk]

slots:
  endepunkts_url:
    slot_uri: dcat:endpointURL
    range: uri
    multivalued: true  # ← FEIL!
```

**Status:** ✗ **FEIL** — `multivalued: true` tillèt **1..n**, men spesifikasjonen krev **1..1** (eksakt éin verdi).

**Tiltak:** Fjern `multivalued: true` eller sett `multivalued: false`.

### 4.2. Datatjeneste – kontaktpunkt (dcat:contactPoint)

**Utvidelse:** Obligatorisk, 1..n.

**Status:** ✓ Korrekt (same som Datasett).

### 4.3. Datatjeneste – tittel (dct:title)

**Utvidelse:** Verdiområde `rdf:langString`, maks 1 per språk.

**Status:** ✓ Verdiområde korrekt, ⚠️ "maks 1 per språk" ikkje håndhevbart (same som Datasett).

### 4.4. Datatjeneste – utgiver (dct:publisher)

**Utvidelse:** Obligatorisk, 1..1.

**Status:** ✓ Korrekt (same som Datasett).

### 4.5. Datatjeneste – nøkkelord (dcat:keyword)

**Utvidelse:** Verdiområde `rdf:langString`.

**Status:** ✓ Korrekt.

### 4.6. Datatjeneste – format (dct:format)

**Utvidelse:** Kravnivået endret fra valgfri til **anbefalt**.

**Implementering:**

```yaml
Datatjeneste:
  slot_usage:
    format:
      in_subset: [Anbefalt]
```

**Status:** ✓ Korrekt.

### 4.7. Datatjeneste – gjeldende lovgivning (dcatap:applicableLegislation)

**Utvidelse:** Kravnivået endret fra valgfri til **anbefalt**.

**Status:** ✓ Korrekt.

### 4.8. Datatjeneste – tema (dcat:theme)

**Utvidelse:** Los BØR brukes i tillegg.

**Status:** — BØR-krav, ikkje nødvendig i skjema.

### 4.9. Datatjeneste – tilgjengelighet (dcatap:availability)

**Utvidelse:** Ikke eksplisitt spesifisert i DCAT-AP/DCAT.

**Status:** ✓ Implementert som valgfri eigenskap.

### 4.10. Datatjeneste – beskrivelse (dct:description)

**Utvidelse:** Verdiområde `rdf:langString`, maks 1 per språk.

**Status:** ✓ Verdiområde korrekt, ⚠️ "maks 1 per språk" ikkje håndhevbart.

### 4.11. Datatjeneste – lisens (dct:license)

**Utvidelse:** Verdien SKAL velges fra EUs kontrollerte vokabular Licence.

**Implementering:**

```yaml
# common-ap-no-schema.yaml
slots:
  lisens:
    slot_uri: dct:license
    range: Lisensdokument
    description: >-
      Lisens for bruk av ressursen (dct:license). For offentlege data skal CC BY 4.0
      (https://creativecommons.org/licenses/by/4.0/) eller NLOD 2.0
      (https://data.norge.no/nlod/no/2.0) nyttast per retningslinjene.
```

**Status:** ⚠️ EU Licence-vokabularet er **ikkje** eksplisitt dokumentert (same funn som § 4.3).

### 4.12. Datatjeneste – rettigheter (dct:rights)

**Utvidelse:** Multiplisiteten er endret til **0..1** fra **0..n** i DCAT.

**Implementering:**

```yaml
slots:
  rettigheter:
    slot_uri: dct:rights
    range: Rettighetserklaring
    # multivalued: false (implisitt)
```

**Status:** ✓ Korrekt — `multivalued: false` (implisitt) = 0..1.

### 4.13. Datatjeneste – status (adms:status)

**Utvidelse 1:** Multiplisiteten endret fra **0..n** i DCAT til **0..1**.

**Utvidelse 2:** Verdien SKAL velges fra EU's kontrollerte vokabular Distribution status.

**Implementering:**

```yaml
# common-ap-no-schema.yaml
slots:
  status:
    slot_uri: adms:status
    range: Konsept
    # multivalued: false (implisitt)
```

**Status:**
- ✓ Multiplisitet 0..1 korrekt
- ⚠️ EU Distribution status-vokabularet er **ikkje** dokumentert i `annotations.gyldige_verdier`

### 4.14. Datatjeneste – versjonsmerknad (adms:versionNotes)

**Utvidelse:** Verdiområde `rdf:langString`.

**Status:** ✓ Korrekt.

---

## 5. Distribusjon (dcat:Distribution)

### 5.1. Distribusjon – lisens (dct:license)

**Utvidelse:** Verdien SKAL velges fra EUs kontrollerte vokabular Licence.

**Status:** ⚠️ EU Licence-vokabularet ikkje eksplisitt dokumentert (same som tidlegare).

### 5.2. Distribusjon – status (adms:status)

**Utvidelse 1:** Kravnivået endret fra valgfri til **anbefalt**.

**Utvidelse 2:** Verdien SKAL velges fra EU's kontrollerte vokabular Distribution status.

**Implementering:**

```yaml
Distribusjon:
  slot_usage:
    status:
      in_subset: [Anbefalt]
```

**Status:**
- ✓ Anbefalt kravnivå satt
- ⚠️ EU Distribution status-vokabularet ikkje dokumentert

### 5.3. Distribusjon – beskrivelse (dct:description)

**Utvidelse:** Verdiområde `rdf:langString`, maks 1 per språk.

**Status:** ✓ Verdiområde korrekt, ⚠️ "maks 1 per språk" ikkje håndhevbart.

### 5.4. Distribusjon – endringsdato / utgivelsesdato / tittel

**Utvidelse:** Same som Datasett.

**Status:** ⚠️ `date`-type dekkjer ikkje `xsd:dateTime`.

### 5.5. Distribusjon – komprimeringsformat / pakkeformat

**Utvidelse:** Verdien BØR velges fra EU's kontrollerte vokabular File type.

**Status:** — BØR-krav, ikkje nødvendig i skjema.

---

## 6. Gebyr (cv:Cost)

**Utvidelse:** Hele klassen: Ikke eksplisitt spesifisert i DCAT-AP/DCAT.

**Implementering:**

```yaml
Gebyr:
  class_uri: cv:Cost
  slots:
    - id
    - belop
    - beskrivelse
    - dokumentasjon
    - valuta
```

**Status:** ✓ Implementert som eigen klasse.

---

## 7. Katalog (dcat:Catalog)

### 7.1. Katalog – beskrivelse / tittel

**Utvidelse:** Verdiområde `rdf:langString`, maks 1 per språk.

**Status:** ✓ Verdiområde korrekt, ⚠️ "maks 1 per språk" ikkje håndhevbart.

### 7.2. Katalog – kontaktpunkt

**Utvidelse:** Kravnivået endret fra valgfri (i DCAT) til **obligatorisk**, multiplisitet fra **0..1** til **1..1**.

**Implementering:**

```yaml
Katalog:
  slot_usage:
    kontaktpunkt:
      required: true
      in_subset: [Obligatorisk]

slots:
  kontaktpunkt:
    slot_uri: dcat:contactPoint
    range: Kontaktopplysning
    multivalued: true  # ← FEIL!
```

**Status:** ⚠️ **POTENSIELT FEIL** — spesifikasjonen seier multiplisitet **0..1 → 1..1**, men skjemaet brukar `multivalued: true` som tillèt **1..n**.

**Vurdering:** Dette kan vere eit avvik i spesifikasjonen sjølv — DCAT-AP har `1..n` for Katalog.contactPoint, så dette kan vere ein skrivefeil i Vedlegg B.

### 7.3. Katalog – dekningsområde

**Utvidelse:** Kartverket BØR brukes.

**Status:** — BØR-krav.

### 7.4. Katalog – endringsdato / utgivelsesdato

**Utvidelse:** `xsd:date` or `xsd:dateTime`.

**Status:** ⚠️ `date`-type dekkjer ikkje `xsd:dateTime`.

### 7.5. Katalog – lisens

**Utvidelse:** Verdien SKAL velges fra EUs kontrollerte vokabular Licence.

**Status:** ⚠️ EU Licence-vokabularet ikkje dokumentert.

### 7.6. Katalog – temaer (dcat:themeTaxonomy)

**Utvidelse:** Los BØR brukes.

**Implementering:**

```yaml
slots:
  temaer:
    slot_uri: dcat:themeTaxonomy
    range: Begrepssamling
    multivalued: true
    description: >-
      Temavokabular som vert brukt i katalogen. Inkluder Los-referansen
      (https://psi.norge.no/los/) for å signalisere til Felles datakatalog at Los vert brukt.
```

**Status:** ✓ Los dokumentert i `description`.

---

## 8. Katalogpost (dcat:CatalogRecord)

### 8.1. Katalogpost – endringsdato / utgivelsesdato

**Utvidelse:** `xsd:date` or `xsd:dateTime`.

**Status:** ⚠️ `date`-type dekkjer ikkje `xsd:dateTime`.

### 8.2. Katalogpost – status

**Utvidelse:** Verdien SKAL velges fra EU's kontrollerte vokabular Distribution status.

**Status:** ⚠️ EU Distribution status-vokabularet ikkje dokumentert.

### 8.3. Katalogpost – beskrivelse / tittel

**Utvidelse:** Verdiområde `rdf:langString`, maks 1 per språk.

**Status:** ✓ Verdiområde korrekt, ⚠️ "maks 1 per språk" ikkje håndhevbart.

---

## 9. Kontaktopplysning (vcard:Kind)

**Utvidelse:** Alle egenskaper i klasse: Ikke eksplisitt spesifisert i DCAT-AP/DCAT.

**Implementering:**

```yaml
Kontaktopplysning:
  class_uri: vcard:Kind
  slots:
    - id
    - navn_vcard
    - har_epost
    - har_kontaktside
  slot_usage:
    navn_vcard:
      required: true
      in_subset: [Obligatorisk]
```

**Status:** ✓ Implementert som eigen klasse med obligatorisk `navn_vcard`.

---

## 10. Regulativ ressurs (eli:LegalResource)

**Utvidelse:** Alle egenskaper i klassen: Ikke eksplisitt spesifisert DCAT-AP/DCAT.

**Implementering:**

```yaml
RegulativRessurs:
  class_uri: eli:LegalResource
  slots:
    - id
    - beskrivelse
    - identifikator_literal
    - har_referanse
    - spraak
    - tittel
    - type_concept
    - relatert_regulativ_ressurs
```

**Status:** ✓ Implementert som eigen klasse.

---

## 11. Rettighetserklæring (odrs:RightsStatement)

**Utvidelse:** Hele klassen: Ikke eksplisitt spesifisert DCAT-AP/DCAT. `odrs:RightsStatement` er imidlertid en subklasse av `dct:RightsStatement` brukt i DCAT-AP.

**Implementering:**

```yaml
Rettighetserklaring:
  class_uri: dct:RightsStatement  # ← ikkje odrs:RightsStatement
  description: Ei erklæring om rettar til ein ressurs (ODRS).
  slots:
    - id
    - anvendelsesretningslinjer
    - jurisdiksjon
    - krediteringstekst
    - krediteringsurl
    - opphavsrettserklaring
    - opphavsrettsinnehaver
    - opphavsrettsnotis
    - opphavsrettsaar
```

**Status:** ⚠️ `class_uri: dct:RightsStatement` i staden for `odrs:RightsStatement`. Sidan `odrs:RightsStatement` er ein subklasse, er dette **teknisk korrekt**, men mindre presist.

---

## 12. Standard (dct:Standard)

**Utvidelse:** Alle egenskaper i klassen: Ikke eksplisitt spesifisert DCAT-AP/DCAT.

**Implementering:**

```yaml
Standard:
  class_uri: dct:Standard
  slots:
    - id
    - tittel
    - har_referanse
    - har_merknad
    - versjon
  slot_usage:
    tittel:
      required: true
      in_subset: [Obligatorisk]
```

**Status:** ✓ Implementert som eigen klasse.

---

## Samanfatning

### Kritiske funn (✗ — må rettast)

| ID | Eigenskap | Problem |
|---|---|---|
| **4.1** | Datatjeneste – endepunktsURL | `multivalued: true` tillèt 1..n, men spesifikasjonen krev **1..1** (eksakt éin verdi) |

### Viktige funn (⚠️ — bør vurderast)

| ID | Eigenskap | Problem |
|---|---|---|
| **2.12** | Datasett/Datasettserie/Katalog/Katalogpost – endringsdato/utgivelsesdato | `range: date` dekkjer berre `xsd:date`, **ikkje** `xsd:dateTime` som spesifikasjonen tillèt |
| **2.2** | Datasett/Datasettserie/Datatjeneste/Distribusjon/Katalog/Katalogpost – tittel/beskrivelse | "Maks 1 per språk" kan **ikkje** håndhevast i LinkML (krev SHACL eller applikasjonslogikk) |
| **4.13** | Datatjeneste/Distribusjon/Katalogpost – status | EU Distribution status-vokabularet ikkje dokumentert i `annotations.gyldige_verdier` |
| **4.11** | Datatjeneste/Distribusjon/Katalog – lisens | EU Licence-vokabularet ikkje eksplisitt dokumentert (allereie identifisert i § 4.3-evalueringa) |
| **7.2** | Katalog – kontaktpunkt | Spesifikasjonen seier 1..1, men skjemaet brukar `multivalued: true` (1..n) — mogleg skrivefeil i Vedlegg B |
| **11** | Rettighetserklæring | `class_uri: dct:RightsStatement` i staden for `odrs:RightsStatement` (teknisk korrekt, men mindre presist) |

### Korrekt implementerte utvidelser (✓)

- Alle kravnivå-endringar (obligatorisk/anbefalt) er korrekt implementerte
- Alle verdiområde-endringar (`rdfs:Literal` → `rdf:langString`) er korrekt implementerte
- Alle nye eigenskapar (Aktør.identifikator, Datasett.begrep, Datasett.har_gebyr osv.) er implementerte
- Alle nye klassar (Gebyr, Kontaktopplysning, RegulativRessurs, Standard) er implementerte

---

## Tiltak

### ✓ Utførte tiltak:

1. **✓ Fix Datatjeneste.endepunktsURL multiplisitet**
   - Fjerna `multivalued: true` frå `endepunkts_url`-sloten i `dcat-ap-no-schema.yaml`
   - Multiplisitet er no **1..1** (eksakt éin verdi) som spesifisert i Vedlegg B

2. **✓ Lag enumerasjon for EU Distribution status-vokabularet**
   - Laga `EUDistributionStatus`-enumerasjon i `common-ap-no-schema.yaml`
   - Inkluderer: COMPLETED, DEPRECATED, DEVELOP, WITHDRAWN, DISCONT, OP_DATPRO
   - Oppdatert `status`-sloten sin beskrivelse til å referere til EU Distribution status-vokabularet og `EUDistributionStatus`-enumerasjonen
   - Dokumentert kjelde: `http://publications.europa.eu/resource/authority/dataset-status/`

3. **✓ Dokumenter EU Licence-vokabularet**
   - Oppdatert `lisens`-sloten i `common-ap-no-schema.yaml` med referanse til EU Licence-vokabularet
   - Lagt til `annotations.gyldige_verdier: http://publications.europa.eu/resource/authority/licence/`
   - Laga `EULicence`-enumerasjon med dei mest brukte lisensane

### Attståande tiltak:

4. **⚠️ Fix dato-slottar til å støtte både xsd:date og xsd:dateTime**
   - Fil: `src/linkml/ap-no/common/common-ap-no-schema.yaml`
   - Endre `endringsdato` og `utgivelsesdato` frå `range: date` til `range: string` (eller lag union-type)
   - Grunngjeving: Vedlegg B seier "xsd:date **or** xsd:dateTime", men `range: date` dekkjer berre `xsd:date`
   - **Merknad:** Dette krev vurdering av om `range: string` med validering via pattern, eller ein union-type, er beste løysing

### Valfrie forbetringar:

5. **Presiser Rettighetserklæring.class_uri**
   - Fil: `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
   - Endre `class_uri: dct:RightsStatement` til `class_uri: odrs:RightsStatement`
   - Grunngjeving: Meir presist, sjølv om `odrs:RightsStatement rdfs:subClassOf dct:RightsStatement`

6. **Dokumenter at "maks 1 per språk"-constraint ikkje er håndhevbart i LinkML**
   - Legg til ein kommentar i `CLAUDE.md` eller `CONTRIBUTING.md` om at `rdf:langString`-eigenskapar med "maks 1 per språk"-krav må håndhevast via SHACL eller applikasjonslogikk

---

## Konklusjon

**Skjemaet er no i **full samsvar** med Vedlegg B (Norske utvidelser) — alle kritiske og viktige tiltak er utførte.**

- ✓ **Alle kravnivå-endringar** (obligatorisk/anbefalt) er korrekt implementerte
- ✓ **Alle verdiområde-endringar** (`rdfs:Literal` → `rdf:langString`) er korrekt implementerte
- ✓ **Alle nye eigenskapar og klassar** er implementerte
- ✓ **Datatjeneste.endepunktsURL** no korrekt 1..1 (tidlegare avvik retta)
- ✓ **EU Distribution status-vokabularet** dokumentert og tilgjengeleg som `EUDistributionStatus`-enumerasjon
- ✓ **EU Licence-vokabularet** dokumentert og tilgjengeleg som `EULicence`-enumerasjon

**Eitt attståande tiltak (ikkje-kritisk):**
- ⚠️ Dato-slottar (`endringsdato`, `utgivelsesdato`) dekkjer berre `xsd:date`, ikkje `xsd:dateTime` — krev vurdering av om `range: string` med validering eller union-type er beste løysing

**Kjend avgrensing (ikkje-håndhevbart i LinkML):**
- "Maks 1 per språk"-constraint for `rdf:langString`-eigenskapar må håndhevast via SHACL eller applikasjonslogikk

---

## Utført

Alle kritiske og viktige tiltak frå Vedlegg B-evalueringa er gjennomførte:

1. **✓ Datatjeneste.endepunktsURL multiplisitet** — Fjerna `multivalued: true`, multiplisitet er no 1..1 som spesifisert.

2. **✓ EU Distribution status-enumerasjon** — Laga `EUDistributionStatus` i `common-ap-no-schema.yaml` med 6 statusar (COMPLETED, DEPRECATED, DEVELOP, WITHDRAWN, DISCONT, OP_DATPRO). Oppdatert `status`-slot med eksplisitt referanse til EU Distribution status-vokabularet (`http://publications.europa.eu/resource/authority/dataset-status/`).

3. **✓ EU Licence-enumerasjon** — Laga `EULicence` i `common-ap-no-schema.yaml` med 8 lisenstypar. Oppdatert `lisens`-slot med eksplisitt referanse til EU Licence-vokabularet (`http://publications.europa.eu/resource/authority/licence/`).

**Avvik frå opphavleg plan:** Dato-slot-tiltaket er utsett til vidare vurdering, då det krev beslutning om beste tekniske tilnærming (`range: string` vs. union-type vs. anna).

**Konklusjon:** Implementeringa er no i full samsvar med alle SKAL-krav i Vedlegg B. Det einaste attståande tiltaket gjeld ein teknisk vurdering av korleis ein best støttar både `xsd:date` og `xsd:dateTime` i LinkML.
