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

**Situasjonen:**
- `Standard`-klassen (`dct:Standard`) er definert i `dqv-ap-no-schema.yaml` (linje 199–227)
- `i_samsvar_med`-sloten i `dcat-ap-no-schema.yaml` har `range: Standard` (linje 886–890)
- `dcat-ap-no-schema.yaml` definerer **ikkje** `Standard`-klassen sjølv (han er kommentert ut)
- `dqv-ap-no-schema.yaml` importerer `dcat-ap-no-schema.yaml`

Dette betyr at `dcat-ap-no-schema.yaml` inneheld ei *framover-referanse* til ein klasse
som berre eksisterer i eit skjema som importerer det:

```
dcat-ap-no → refererer Standard → definert i dqv-ap-no
dqv-ap-no → importerer dcat-ap-no
```

**Konsekvens:** Dersom `dcat-ap-no-schema.yaml` vert brukt utan `dqv-ap-no-schema.yaml`
(t.d. av eit domenemodell som importerer `dcat-ap-no` direkte), vil `i_samsvar_med`
peke på ein udefinert klasse og genereraren vil feile.

Eksempel på sårbare importkjeder:
```
ngr-adresse-schema.yaml
  → dcat-ap-no-schema.yaml    # i_samsvar_med.range: Standard
                               # Standard ikkje definert her!
```

**Moglege løysingar:**

*Alternativ A* — Flytt `Standard`-klassen til `dcat-ap-no-schema.yaml` eller
`common-ap-no-schema.yaml`. Fjern `er_i_samsvar_med`-kommentaren i `dqv-ap-no`.
`Standard.er_i_kvalitetsdimensjon`-sloten (DQV-spesifikk) vert ståande i `dqv-ap-no`.

*Alternativ B* — Bryt sirkelen ved å endre `i_samsvar_med.range` til `uri`
i `dcat-ap-no`, og la `dqv-ap-no` overstyre range til `Standard` via `slot_usage`
på den kommenterte `Datasett`-klassen.

*Anbefalt: Alternativ A* — `dct:Standard` er eit allment DCAT-omgrep, ikkje
DQV-spesifikt.

**Filer:**
- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
- `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`

**Status:** ⚠️ Strukturell avhengigheitsfeil — høg prioritet

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
**Status:** ⚠️ Kardinalitetsavvik — høg prioritet

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

**Moglege løysingar:**

LinkML støttar ikkje direkte `union_of` på `range`. Alternativ:
- Bruk `range: Any` med `annotations.gyldige_datatypar` for dokumentasjon
- Lag separate slots: `har_boolean_verdi`, `har_numerisk_verdi`, `har_tekst_verdi`
- Bruk `range: string` men legg til `annotations.gyldige_datatypar` med XSD-typane

Enklaste tilnærming utan store strukturendringar: legg til annotasjon som
dokumenterer dei gyldige datatypane og tilrår at brukarar bruker riktig XSD-type
i den genererte JSON/TTL-serialiseringa.

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Status:** ⚠️ Tap av semantisk typeinformasjon — middels prioritet

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

**Moglege løysingar:**
- Legg til `enum`-type `MotivasjonEnum` med dei viktigaste verdiane
- Alternativt: legg til `annotations.gyldige_verdier` på `er_motivert_av`

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Status:** ⚠️ Manglande validering — middels prioritet

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
**Status:** ⚠️ Avvik — låg prioritet

---

### 6 — `Datasett`-klassen kommentert ut — `er_i_samsvar_med`-kommentar er forvirrande

I `dqv-ap-no-schema.yaml` er `Datasett`-klassen og `er_i_samsvar_med`-sloten
begge kommenterte ut (linje 49–68 og 257–261). Kommentarane antydar at desse
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
**Status:** ℹ️ Klargjering — låg prioritet

---

### 7 — `Standard.versjonsnummer` vs. DCAT-AP-NO: konflikt mellom standardar

`Standard`-klassen i `dqv-ap-no-schema.yaml` brukar `versjonsnummer` (`owl:versionInfo`),
som er korrekt per DQV-AP-NO-spesifikasjonen:

> har versjonsnummer | `owl:versionInfo` | `rdfs:Literal` | 0..1 | Valgfri

Men `avvik-dcat-ap-no.md` (tiltak DA3) tilrår å endre `Standard.versjonsnummer`
til `versjon` (`dcat:version`), basert på DCAT-AP-NO-spec som krev `dcat:version`.

**Dei to standardane er i konflikt:**

| Standard | Krav for Standard.versjon |
|---|---|
| DQV-AP-NO | `owl:versionInfo` → `versjonsnummer` ✓ |
| DCAT-AP-NO | `dcat:version` → `versjon` |

`Standard`-klassen er formelt ein DQV-AP-NO-klasse (definert der, ikkje i DCAT-AP-NO).
DQV-AP-NO sin bruk av `owl:versionInfo` bør difor prioriterast.

**Tilrådde tiltak:** Oppdater DA3 i `avvik-dcat-ap-no.md` — dette er ikkje eit
avvik i `dqv-ap-no`, men ein konflikt mellom dei to standardane. Hald
`versjonsnummer`/`owl:versionInfo` på `Standard`.

**Filer:** `specs/backlog/avvik-dcat-ap-no.md` (oppdater DA3)  
**Status:** ℹ️ Konfliktavklaring — ikkje eit schema-avvik

---

## Samandrag

| # | Avvik | Alvor | Prioritet |
|---|---|---|---|
| 1 | `Standard`-klassen skapar framover-referanse frå `dcat-ap-no` → `dqv-ap-no` | Strukturell | **Høg** |
| 2 | `har_tekstdel` ikkje `multivalued: true` | Kardinalitet | **Høg** |
| 3 | `har_verdi.range: string` — tap av XSD-typeinfo | Semantisk | Middels |
| 4 | `Motivasjon`-klasse ikkje modellert; gyldige verdiar udokumentert | Manglande validering | Middels |
| 5 | `har_maal.range: uri` i staden for `KatalogisertRessurs` | Avvik | Låg |
| 6 | Kommenterte blokkar forvirrande — manglar klargjering | Lesbarheit | Låg |
| 7 | `Standard.versjonsnummer` vs. DCAT-AP-NO — konflikt mellom standardar | Informasjon | — |

---

## Tilrådde tiltak

### DQ1 — Løys sirkulær avhengigheit: flytt `Standard` til `dcat-ap-no` (Avvik 1)

Flytt `Standard`-klassen frå `dqv-ap-no-schema.yaml` til `dcat-ap-no-schema.yaml`.
Fjern den kommenterte `Standard`-klassen i `dcat-ap-no`. DQV-spesifikke slottar
(`er_i_kvalitetsdimensjon`) vert ståande i `dqv-ap-no` via `slot_usage` på `Standard`.

```yaml
# I dcat-ap-no-schema.yaml — legg til:
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
    - versjonsnummer
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
    versjonsnummer:
      in_subset:
        - Valgfri

# I dqv-ap-no-schema.yaml — hald berre DQV-spesifikke tillegg:
# Standard-klassen kjem frå dcat-ap-no (importert).
# dqv:inDimension vert lagt til via slot_usage i Standard.
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

### DQ3 — Dokumenter gyldige XSD-typar for `har_verdi` (Avvik 3)

Bevar `range: string` men legg til annotasjon og oppdatert skildring:

```yaml
har_verdi:
  slot_uri: dqv:value
  range: string
  description: >-
    Målt verdi for kvalitetsmålet. Bruk riktig XSD-type i serialisering:
    xsd:boolean (sann/usann), xsd:double (desimaltal), 
    xsd:nonNegativeInteger (heiltal >= 0), eller rdfs:Literal (fritekst).
  annotations:
    gyldige_datatypar: >-
      xsd:boolean xsd:double xsd:nonNegativeInteger rdfs:Literal
```

**Filer:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`

---

### DQ4 — Dokumenter gyldige motivasjonsverdiar på `er_motivert_av` (Avvik 4)

```yaml
er_motivert_av:
  slot_uri: oa:motivatedBy
  range: uriorcurie
  description: >-
    Motivasjonen bak kvalitetsmerknaden. Bruk oa:assessing for generelle
    vurderingar, eller dqvno:-motivasjonar for norsk kvalitetsdimensjon.
  annotations:
    gyldige_verdier: >-
      oa:assessing
      oa:classifying
      dqvno:availability
      dqvno:completeness
      dqvno:currentness
      dqvno:validity
      dqvno:accuracy
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

### DQ6 — Oppdater `avvik-dcat-ap-no.md` om `Standard.versjonsnummer` (Avvik 7)

Tiltak DA3 i `avvik-dcat-ap-no.md` bør oppdaterast: `Standard`-klassen brukar
`owl:versionInfo` per DQV-AP-NO-spec, og bør **ikkje** endrast til `dcat:version`.

**Filer:** `specs/backlog/avvik-dcat-ap-no.md`

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | DQ2: `multivalued: true` på `har_tekstdel` | `dqv-ap-no-schema.yaml` | — |
| 2 | DQ1: Flytt `Standard`-klassen til `dcat-ap-no` | begge schema | — |
| 3 | DQ4: Gyldige motivasjonsverdiar på `er_motivert_av` | `dqv-ap-no-schema.yaml` | — |
| 4 | DQ3: XSD-type-annotasjon på `har_verdi` | `dqv-ap-no-schema.yaml` | — |
| 5 | DQ5: `har_maal.range: KatalogisertRessurs` | `dqv-ap-no-schema.yaml` | DQ1 |
| 6 | DQ6: Oppdater DA3 i `avvik-dcat-ap-no.md` | spec-fil | — |

---

## Avhengigheiter

- DQ1 (flytt `Standard`) er den tyngste endringa og krev at alle skjema som
  importerer `dcat-ap-no` vert re-generert og re-validert
- DQ5 (`har_maal.range: KatalogisertRessurs`) er avhengig av at DQ1 er gjort
  (elles finst ikkje `KatalogisertRessurs` i `dqv-ap-no`-konteksten — men
  han vert importert frå `dcat-ap-no`)
- DQ2, DQ3, DQ4 er uavhengige og kan gjerast i kva rekkjefølge som helst
