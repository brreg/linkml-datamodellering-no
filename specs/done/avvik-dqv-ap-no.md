# Kartlegging: Avvik mot Spesifikasjon for beskrivelse av kvalitet på datasett (DQV-AP-NO)

**Kjelde:** [data.norge.no/specification/dqv-ap-no](https://data.norge.no/specification/dqv-ap-no/)  
**Teknisk spec:** [informasjonsforvaltning.github.io/dqv-ap-no](https://informasjonsforvaltning.github.io/dqv-ap-no/)  
**Implementasjon i repoet:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Avhengig av:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

---

## Bakgrunn

`dqv-ap-no-schema.yaml` implementerer DQV-AP-NO som ein LinkML-applikasjonsprofil.
Skjemaet importerer `dcat-ap-no-schema.yaml` og definerer klassane for
kvalitetsinformasjon (`Kvalitetsmerknad`, `Kvalitetsmaaling`, `Standard` osb.).

DQV-AP-NO omhandlar beskriving av *datakvalitet* — ikkje sjølve datasettinnhaldet.
Dei viktigaste klassane er:

| Klasse | URI | Kravnivå i spec |
|---|---|---|
| `Datasett` | `dcat:Dataset` | Obligatorisk (via dcat-ap-no) |
| `Kvalitetsmerknad` | `dqv:QualityAnnotation` | Anbefalt |
| `Kvalitetsmaaling` | `dqv:QualityMeasurement` | Anbefalt |
| `Brukartilbakemelding` | `dqv:UserQualityFeedback` | Anbefalt |
| `Standard` | `dct:Standard` | Anbefalt |
| `Kvalitetsdimensjon` | `dqv:Dimension` | Valgfri |
| `Kvalitetsdeldimensjon` | `dqvno:SubDimension` | Valgfri |
| `Kvalitetsmaal` | `dqv:Metric` | Valgfri |
| `Kvalitetssertifikat` | `dqv:QualityCertificate` | Valgfri |
| `Motivasjon` | `oa:Motivation` | Valgfri |
| `Tekstdel` | `oa:TextualBody` | Valgfri |

---

## Kartlegging av avvik

### 1 — `Standard`-klassen skapar sirkulær avhengigheit mellom `dcat-ap-no` og `dqv-ap-no`

Dette er det viktigaste strukturelle avviket i heile DQV-AP-NO-implementasjonen.

**Opphavleg situasjon:**
- `Standard`-klassen (`dct:Standard`) var berre definert i `dqv-ap-no-schema.yaml`
- `i_samsvar_med.range: Standard` i `dcat-ap-no-schema.yaml` var ei framover-referanse
- `dqv-ap-no-schema.yaml` importerer `dcat-ap-no-schema.yaml` → sirkulær avhengigheit

**Noverande situasjon (etter innkommentering):**

`Standard`-klassen er no kommentert inn i `dcat-ap-no-schema.yaml`. Framover-referansen
frå `i_samsvar_med.range: Standard` er dermed løyst for skjema som berre importerer
`dcat-ap-no`.

Men det finst to attståande problem:

1. **Duplikat-definisjon:** `Standard` er no definert *to stader* — i `dcat-ap-no` og i
   `dqv-ap-no` (som importerer `dcat-ap-no`). Dei to definisjonane er ute av sync:

   | Eigeskap | `dcat-ap-no` (innkommentert) | `dqv-ap-no` (aktiv) |
   |---|---|---|
   | versjon-slot | `versjonsnummer` (owl:versionInfo) | `versjon` (dcat:version) |
   | `er_i_kvalitetsdimensjon` | Manglar | Til stades |
   | `in_subset` | Manglar | `Metadata` |
   | `har_merknad` | Manglar | Til stades |

2. **`versjonsnummer` i `dcat-ap-no`:** Den innkommenterte blokka brukar det gamle
   `versjonsnummer`-slottet. Etter DA3 skal det vere `versjon` (`dcat:version`).

**Moglege løysingar:**

*Anbefalt: Flytt all definisjon til `dcat-ap-no`, bruk class override i `dqv-ap-no`* —
Oppdater den innkommenterte `Standard`-klassen i `dcat-ap-no` til å bruke `versjon`
og inkludere alle felles slots (`id`, `tittel`, `har_referanse`, `har_merknad`, `versjon`).
I `dqv-ap-no`, erstatt den fullstendige klasse-definisjonen med ein minimal class override
som berre legg til det DQV-spesifikke slottet:

```yaml
# I dqv-ap-no-schema.yaml — erstatt Standard-klassen med:
Standard:
  slots:
    - er_i_kvalitetsdimensjon
  slot_usage:
    er_i_kvalitetsdimensjon:
      in_subset:
        - Anbefalt
```

**Filer:**
- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
- `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`

**Status:** ✓ Løyst — `Standard` er definert i `dcat-ap-no`; `dqv-ap-no` har minimal class override med `er_i_kvalitetsdimensjon`

---

### 2 — `har_tekstdel` (`oa:hasBody`) er ikkje `multivalued`

Spesifikasjonen seier `oa:hasBody` har kardinalitet 0..n på `Kvalitetsmerknad`.
Ein merknad kan ha fleire tekstdelar (t.d. på fleire språk, eller med ulik format).

Noverande implementasjon:

```yaml
har_tekstdel:
  slot_uri: oa:hasBody
  range: Tekstdel
  description: Tekstleg innhald i merknaden.
  # manglar multivalued: true
```

Konsekvens: Berre éin tekstdel per `Kvalitetsmerknad` er mogleg. For fleirspråklege
kvalitetsmerknader er dette for avgrensande.

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Status:** ✓ Løyst — `multivalued: true` lagt til på `har_tekstdel`

---

### 3 — `har_verdi` (`dqv:value`) brukar `range: string` — tap av typeinfo

Spesifikasjonen seier `dqv:value` kan ha desse datatypane:

| XSD-type | Eksempel |
|---|---|
| `xsd:boolean` | `true` / `false` |
| `xsd:double` | `0.95` |
| `xsd:nonNegativeInteger` | `1042` |
| `rdfs:Literal` | fritekst |

Noverande implementasjon:

```yaml
har_verdi:
  slot_uri: dqv:value
  range: string
  description: >-
    Målt verdi (xsd:boolean, xsd:double, xsd:nonNegativeInteger eller
    rdfs:Literal avhengig av kvalitetsmålet).
```

`range: string` vil serialisere alle verdiar som `xsd:string` i generert RDF.
Det betyr at målinga `0.95` vert `"0.95"` i staden for `"0.95"^^xsd:double`.
Maskinell prosessering som reknar på målingsresultat (t.d. finne gjennomsnitt
for fullstendigheit) vil ikkje fungere korrekt.

**Valt løysing: Separate slots per datatype**

LinkML støttar ikkje `union_of` på `range`. Vi går for separate slots som
mappar alle til `dqv:value` men med korrekt range per type. Sjå DQ3 for implementasjon.

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Status:** ✓ Løyst — `har_verdi` erstatta med `har_boolean_verdi`, `har_numerisk_verdi`, `har_tekst_verdi`

---

### 4 — `Motivasjon`-klassen ikkje modellert; gyldige verdiar udokumenterte

Spesifikasjonen listar `Motivasjon` (`oa:Motivation`) som Valgfri klasse.
I schema er `er_motivert_av.range: uriorcurie` — ein ren URI-referanse.

Dette betyr at schema ikkje dokumenterer eller validerer kva motivasjonsverdiar
som er gyldige. Relevante verdiar per DQV-AP-NO og `dqvno:`-vokabularet er:

| URI | Tydning |
|---|---|
| `oa:assessing` | Allgemein vurdering |
| `oa:classifying` | Klassifisering |
| `dqvno:availability` | Tilgjengelegheit |
| `dqvno:completeness` | Fullstendigheit |
| `dqvno:currentness` | Aktualitet |
| `dqvno:validity` | Gyldighet |
| `dqvno:accuracy` | Nøyaktigheit |

Utan desse verdiane dokumentert i schema, er det uklårt for implementørar kva
motivasjonar som er gyldige i norsk kontekst.

**Valt løysing: `enum`-type `DqvMotivasjon`**

Namn følgjer konvensjonen om at særnorske bokstavar translittererast i identifikatorar
(`Motivasjon` → `Motivasjon`; prefiks `Dqv` gjer det tydeleg at enumen høyrer til
DQV-AP-NO-skjemaet). Sjå DQ4 for implementasjon.

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Status:** ✓ Løyst — `DqvMotivasjon` enum lagt til; `er_motivert_av.range` endra til `DqvMotivasjon`

---

### 5 — `har_maal` (`oa:hasTarget`) brukar `range: uri` i staden for `KatalogisertRessurs`

Spesifikasjonen seier `oa:hasTarget` på `Kvalitetsmerknad` skal peike på
`dcat:Resource` (ein katalogisert ressurs — datasett, distribusjon eller datatjeneste).

Noverande implementasjon:

```yaml
har_maal:
  slot_uri: oa:hasTarget
  range: uri
  description: Ressursen merknaden gjeld.
  annotations:
    gyldige_verdier: dcat:Resource
```

`range: uri` accepterer kva som helst URI, ikkje berre `dcat:Resource`-instansar.
Betre ville vere `range: KatalogisertRessurs` (den abstrakte basisklassen i schema).

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Status:** ✓ Løyst — `har_maal.range` endra til `KatalogisertRessurs`

---

### 6 — `Datasett`-klassen kommentert ut — `er_i_samsvar_med`-kommentar er forvirrande

I `dqv-ap-no-schema.yaml` er `Datasett`-klassen og `er_i_samsvar_med`-sloten
begge kommenterte ut (linje 49-68 og 257-261). Kommentarane antydar at desse
eigenskapane kjem frå `dcat-ap-no`.

I praksis:
- `har_kvalitetsmerknad` og `har_kvalitetsmaaling` er definert i `dcat-ap-no-schema.yaml`
  og lagt til `Datasett`-klassen der ✓
- `er_i_samsvar_med` (`dct:conformsTo`) er definert i `dcat-ap-no-schema.yaml`
  og lagt til `Datasett` der ✓

Men kommentarane forvirrar: ein lesar av `dqv-ap-no-schema.yaml` forstår ikkje
kvifor `Datasett` ikkje er her og kvar dei DQV-eigenskapane faktisk ligg.

**Tilrådde tiltak:** Erstatt kommentarane med ein klår tekstkommentar:

```yaml
# Datasett-klassen er definert i dcat-ap-no-schema.yaml (importert).
# har_kvalitetsmerknad, har_kvalitetsmaaling og i_samsvar_med er lagt
# til Datasett der, sidan dcat-ap-no vert importert av mange skjema
# som ikkje treng full DQV-funksjonalitet.
```

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Status:** ✓ Løyst — kommenterte blokkar erstatta med klare tekstkommentarar

---

### 7 — `Standard.versjonsnummer` vs. DCAT-AP-NO: konflikt mellom standardar ✓

`Standard`-klassen i `dqv-ap-no-schema.yaml` brukte tidlegare `versjonsnummer` (`owl:versionInfo`),
som er korrekt per DQV-AP-NO-spesifikasjonen:

> har versjonsnummer | `owl:versionInfo` | `rdfs:Literal` | 0..1 | Valgfri

Men `avvik-dcat-ap-no.md` (tiltak DA3) endra `Standard` til å bruke
`versjon` (`dcat:version`), basert på DCAT-AP-NO-spec.

**Dei to standardane er i konflikt:**

| Standard | Krav for Standard.versjon |
|---|---|
| DQV-AP-NO | `owl:versionInfo` → `versjonsnummer` |
| DCAT-AP-NO | `dcat:version` → `versjon` |

**Løysing (utført via DA3):** Konflikten vart løyst til fordel for DCAT-AP-NO.
`Standard`-klassen brukar no `versjon` (`dcat:version`) i `dqv-ap-no-schema.yaml`.
Sidan DCAT-AP-NO er det primære skjemaet som definerer bruksområdet til `Standard`
(`dct:conformsTo`), er DCAT-AP-NO-kravet gjeldande.

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Status:** ✓ Avklart — `versjon` (`dcat:version`) er no gjeldande på `Standard`

---

## Samandrag

| # | Avvik | Alvor | Prioritet |
|---|---|---|---|
| 1 | `Standard`-klassen skapar framover-referanse frå `dcat-ap-no` → `dqv-ap-no` | Strukturell | **Høg** ✓ |
| 2 | `har_tekstdel` ikkje `multivalued: true` | Kardinalitet | **Høg** ✓ |
| 3 | `har_verdi.range: string` — tap av XSD-typeinfo | Semantisk | Middels ✓ |
| 4 | `Motivasjon`-klasse ikkje modellert; gyldige verdiar udokumentert | Manglande validering | Middels ✓ |
| 5 | `har_maal.range: uri` i staden for `KatalogisertRessurs` | Avvik | Låg ✓ |
| 6 | Kommenterte blokkar forvirrande — manglar klargjering | Lesbarheit | Låg ✓ |
| 7 | `Standard.versjonsnummer` vs. DCAT-AP-NO — løyst via DA3 (`versjon`) | Avklart ✓ | — |

---

## Tilrådde tiltak

### DQ1 — Fullfør `Standard`-klassen i `dcat-ap-no`; reduser `dqv-ap-no` til class override (Avvik 1)

`Standard`-klassen er no kommentert inn i `dcat-ap-no`, men den innkommenterte definisjonen
er utdatert og ufullstendig. To steg gjenstår:

**Steg 1 — Oppdater `Standard` i `dcat-ap-no-schema.yaml`:**

```yaml
Standard:
  in_subset:
    - Metadata
  class_uri: dct:Standard
  description: Ein standard eller spesifikasjon.
  slots:
    - id
    - tittel
    - har_referanse
    - har_merknad
    - versjon           # dcat:version — ikkje versjonsnummer (owl:versionInfo)
  slot_usage:
    tittel:
      required: true
      in_subset:
        - Obligatorisk
    har_referanse:
      in_subset:
        - Anbefalt
    har_merknad:
      in_subset:
        - Valgfri
    versjon:
      in_subset:
        - Valgfri
```

**Steg 2 — Reduser `Standard` i `dqv-ap-no-schema.yaml` til class override:**

Erstatt den fullstendige `Standard`-definisjonen med ein minimal blokk som berre
legg til det DQV-spesifikke slottet. Alle andre slots og `slot_usage`-innskrenkingar
arves frå `dcat-ap-no` via import:

```yaml
# Standard-klassen er definert i dcat-ap-no-schema.yaml (importert).
# Her vert berre det DQV-spesifikke slottet lagt til via class override.
Standard:
  slots:
    - er_i_kvalitetsdimensjon
  slot_usage:
    er_i_kvalitetsdimensjon:
      in_subset:
        - Anbefalt
```

**Filer:**
- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
- `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`

---

### DQ2 — Legg til `multivalued: true` på `har_tekstdel` (Avvik 2)

```yaml
har_tekstdel:
  slot_uri: oa:hasBody
  range: Tekstdel
  multivalued: true        # ← legg til
  description: Tekstleg innhald i merknaden (0..n).
```

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`

---

### DQ3 — Erstatt `har_verdi` med separate slots per datatype (Avvik 3)

Fjern `har_verdi` og legg til tre separate slots som alle mappar til `dqv:value`
men med korrekt LinkML-type per datatype. Legg dei til `Kvalitetsmaaling` via `slot_usage`.

```yaml
# Slots:
har_boolean_verdi:
  slot_uri: dqv:value
  range: boolean
  description: Målt verdi som sann/usann (xsd:boolean).

har_numerisk_verdi:
  slot_uri: dqv:value
  range: double
  description: Målt verdi som desimaltal eller heiltal (xsd:double).

har_tekst_verdi:
  slot_uri: dqv:value
  range: string
  description: Målt verdi som fritekst (rdfs:Literal).

# Klasse:
classes:
  Kvalitetsmaaling:
    slots:
      - ...
      - har_boolean_verdi
      - har_numerisk_verdi
      - har_tekst_verdi
    slot_usage:
      har_boolean_verdi:
        in_subset:
          - Anbefalt
      har_numerisk_verdi:
        in_subset:
          - Anbefalt
      har_tekst_verdi:
        in_subset:
          - Anbefalt
```

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`

---

### DQ4 — Legg til `enum`-type `DqvMotivasjon` og endre `er_motivert_av.range` (Avvik 4)

```yaml
# Enums:
enums:
  DqvMotivasjon:
    description: >-
      Gyldige motivasjonsverdiar for kvalitetsmerknader per DQV-AP-NO og
      dqvno-vokabularet.
    permissible_values:
      oa:assessing:
        description: Allgemein vurdering av kvalitet.
      oa:classifying:
        description: Klassifisering av kvalitet.
      dqvno:availability:
        description: Tilgjengelegheit.
      dqvno:completeness:
        description: Fullstendigheit.
      dqvno:currentness:
        description: Aktualitet.
      dqvno:validity:
        description: Gyldighet.
      dqvno:accuracy:
        description: Nøyaktigheit.

# Slot:
er_motivert_av:
  slot_uri: oa:motivatedBy
  range: DqvMotivasjon
  description: Motivasjonen bak kvalitetsmerknaden.
```

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`

---

### DQ5 — Endre `har_maal.range` til `KatalogisertRessurs` (Avvik 5)

```yaml
har_maal:
  slot_uri: oa:hasTarget
  range: KatalogisertRessurs    # dcat:Resource
  description: Datasett, distribusjon eller datatjeneste merknaden gjeld.
```

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`

---

### DQ6 — ~~Oppdater `avvik-dcat-ap-no.md` om `Standard.versjonsnummer`~~ (Avvik 7) ✓ N/A

~~Tiltak DA3 i `avvik-dcat-ap-no.md` bør oppdaterast: `Standard`-klassen brukar
`owl:versionInfo` per DQV-AP-NO-spec, og bør **ikkje** endrast til `dcat:version`.~~

DA3 vart utført og valde `versjon` (`dcat:version`). Konflikten er løyst til fordel
for DCAT-AP-NO. Dette tiltaket er ikkje lenger aktuelt — avvik 7 er oppdatert
med den faktiske løysinga.

**Status:** ✓ N/A — DA3 allereie utført; konflikten løyst via Avvik 7

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | DQ2: `multivalued: true` på `har_tekstdel` | `dqv-ap-no-schema.yaml` | — |
| 2 | DQ1: Flytt `Standard`-klassen til `dcat-ap-no` | begge schema | — |
| 3 | DQ4: Gyldige motivasjonsverdiar på `er_motivert_av` | `dqv-ap-no-schema.yaml` | — |
| 4 | DQ3: XSD-type-annotasjon på `har_verdi` | `dqv-ap-no-schema.yaml` | — |
| 5 | DQ5: `har_maal.range: KatalogisertRessurs` | `dqv-ap-no-schema.yaml` | DQ1 |
| 6 | DQ6: ~~Oppdater DA3~~ — N/A, DA3 allereie utført | — | — |

---

## Avhengigheiter

- DQ1 (flytt `Standard`) er den tyngste endringa og krev at alle skjema som
  importerer `dcat-ap-no` vert re-generert og re-validert
- DQ5 (`har_maal.range: KatalogisertRessurs`) er avhengig av at DQ1 er gjort
  (elles finst ikkje `KatalogisertRessurs` i `dqv-ap-no`-konteksten — men
  han vert importert frå `dcat-ap-no`)
- DQ2, DQ3, DQ4 er uavhengige og kan gjerast i kva rekkjefølge som helst

---

## Utført

Alle tiltak gjennomførte 2026-06-17. Avvik frå opphavleg plan:

- **DQ1:** `Standard`-klassen var allereie delvis kommentert inn av brukar i `dcat-ap-no`. Fullstendig definisjon med `versjon`, `har_merknad` og korrekt `in_subset` vart lagt til. `dqv-ap-no` vart redusert til minimal class override med `er_i_kvalitetsdimensjon` og ein `description`.
- **DQ3:** `har_verdi` erstatta med `har_boolean_verdi` (boolean), `har_numerisk_verdi` (double) og `har_tekst_verdi` (string) — alle mappande til `dqv:value`. Alle tre lagt til `Kvalitetsmaaling` som `Anbefalt`.
- **DQ4:** `DqvMotivasjon` enum lagt til med `meaning:`-nøklar for CURIE-mapping. Enumverdiane brukar korte engelske nøklar (`assessing`, `availability` osb.) som mappar til `oa:`/`dqvno:`-URI-ar.
- **DQ5:** `har_maal.range` endra til `KatalogisertRessurs`; `annotations.gyldige_verdier` fjerna.
- **Avvik 6:** Kommenterte blokkar i `dqv-ap-no` (Datasett-klassen og `er_i_samsvar_med`-sloten) erstatta med klare enkeltlinje-kommentarar.
- **DQ6:** Ikkje utført (N/A — DA3 var allereie gjennomført).
