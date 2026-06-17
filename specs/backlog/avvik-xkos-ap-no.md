# Kartlegging: Avvik mot Spesifikasjon for klassifikasjonsbeskrivingar (XKOS-AP-NO)

**Kjelde:** [informasjonsforvaltning.github.io/xkos-ap-no](https://informasjonsforvaltning.github.io/xkos-ap-no/)  
**Implementasjon i repoet:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

---

## Bakgrunn

XKOS-AP-NO er ein norsk applikasjonsprofil av XKOS (eXtended Knowledge Organization System)
for å beskrive klassifikasjonar og kodeverk. Spesifikasjonen definerer fem klasser:

| Klasse | RDF-klasse | Status i spec |
|---|---|---|
| `Klassifikasjon` | `skos:ConceptScheme` | Obligatorisk |
| `Kategori` | `skos:Concept` | Obligatorisk |
| `Klassifikasjonsnivaa` | `xkos:ClassificationLevel` | Anbefalt |
| `Klassifikasjonssamanlikning` | `xkos:Correspondence` | Valgfri |
| `Kategorisamanlikning` | `xkos:ConceptAssociation` | Valgfri |

Alle fem klassane er implementerte i skjemaet. Kartlegginga nedanfor identifiserer
avvik på subset-nivå, manglande eigenskapar og ein feil slot-URI.

---

## Kartlegging av avvik

### 1 — Bug: `tidsrom_start`/`tidsrom_slutt` brukar feil slot-URI

`xkos-ap-no-schema.yaml` definerer:

```yaml
tidsrom_start:
  slot_uri: dct:startDate    # feil — finst ikkje i DC Terms
  range: date

tidsrom_slutt:
  slot_uri: dct:endDate      # feil — finst ikkje i DC Terms
  range: date
```

`dct:` er `http://purl.org/dc/terms/`. DC Terms har ikkje `startDate` eller `endDate`
som eigenskapar — desse finst i DCAT 3-namespace:

```yaml
tidsrom_start:
  slot_uri: dcat:startDate   # http://www.w3.org/ns/dcat#startDate
tidsrom_slutt:
  slot_uri: dcat:endDate     # http://www.w3.org/ns/dcat#endDate
```

Skjemaet i `dcat-ap-no-schema.yaml` brukar korrekt `dcat:startDate`/`dcat:endDate`.
`xkos-ap-no-schema.yaml` er inkonsistent med dette og produserer feil URI-ar i RDF-output.

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml` (linjene 393–399)  
**Status:** ⚠️ Bug — bør rettast umiddelbart

---

### 2 — Subset-avvik: `antall_nivaa` burde vere Obligatorisk

XKOS-AP-NO-spesifikasjonen krev `xkos:numberOfLevels` med kardinalitet **1..1** (Obligatorisk) på `Klassifikasjon`.

Skjemaet merkjer dette som Anbefalt (utan `required: true`):

```yaml
# Noverande
antall_nivaa:
  in_subset:
    - Anbefalt
  # required: true manglar

# Korrekt
antall_nivaa:
  in_subset:
    - Obligatorisk
  required: true
```

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml` (Klassifikasjon.slot_usage)  
**Status:** ⚠️ Subset-avvik — middels prioritet

---

### 3 — Subset-avvik: `forste_nivaa` burde vere Anbefalt

Spesifikasjonen lister `xkos:levels` som Anbefalt på `Klassifikasjon`.
Skjemaet merkjer dette som Valgfri:

```yaml
# Noverande
forste_nivaa:
  in_subset:
    - Valgfri

# Korrekt
forste_nivaa:
  in_subset:
    - Anbefalt
```

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Status:** ⚠️ Subset-avvik — låg prioritet

---

### 4 — `skos:notation` manglar på `Kategori` (Anbefalt)

`skos:notation` er Anbefalt i spesifikasjonen på `Kategori` og er fundamentalt for
klassifikasjonar — det er feltet som inneheld sjølve *koden* (t.d. «A», «01.1», «42» i NACE).
Utan `notasjon`-slot kan ikkje kodeverksverdiar representera sin strukturerte kode.

```yaml
notasjon:
  slot_uri: skos:notation
  range: string
  multivalued: true
  description: >-
    Kode for kategorien i klassifikasjonen (skos:notation).
    Til dømes «A», «01», «01.1» i NACE-kodeverk.
```

Legg til som `Anbefalt` i `Kategori.slot_usage`.

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Status:** ⚠️ Manglande Anbefalt eigeskap — høg prioritet (grunnleggjande for klassifikasjonar)

---

### 5 — Dekkingseigeanskapar manglar på `Klassifikasjon` og `Klassifikasjonsnivaa` (Anbefalt)

XKOS-AP-NO spesifiserer tre Anbefalt eigenskapar for å beskrive kva eit klassifikasjonsnivå
dekkjer — og om dekkinga er uttømmande og/eller gjensidig utelukkande. Desse finst
ikkje i skjemaet:

| Eigeskap | URI | Klasse(r) | Status i spec |
|---|---|---|---|
| `dekker` | `xkos:covers` | `Klassifikasjon`, `Klassifikasjonsnivaa` | Anbefalt |
| `dekker_gjensidig_utelukkande` | `xkos:coversMutuallyExclusively` | `Klassifikasjon`, `Klassifikasjonsnivaa` | Anbefalt |
| `dekker_uttomande` | `xkos:coversExhaustively` | `Klassifikasjon`, `Klassifikasjonsnivaa` | Anbefalt |

Desse eigenskapane er særleg viktige for kodeverk der det er eit krav at kategoriane
er gjensidig utelukkande og uttømmande (MECE — Mutually Exclusive, Collectively Exhaustive).

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Status:** ⚠️ Manglande Anbefalt eigenskapar — middels prioritet

---

### 6 — `xkos:organizedBy` manglar på `Klassifikasjonsnivaa` (Anbefalt)

Spesifikasjonen har `xkos:organizedBy` (Anbefalt) på `Klassifikasjonsnivaa` for å peike
til kva prinsipp nivået er organisert etter. Denne manglar i skjemaet.

```yaml
organisert_etter:
  slot_uri: xkos:organizedBy
  range: Konsept
  description: >-
    Prinsippet klassifikasjonsnivået er organisert etter (xkos:organizedBy).
```

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Status:** ⚠️ Manglande Anbefalt eigeskap — låg prioritet

---

### 7 — `xkos:supersedes` manglar på `Klassifikasjon` (Anbefalt)

Spesifikasjonen har `xkos:supersedes` (Anbefalt) for å lenke frå ein nyare til ein eldre versjon
av ein klassifikasjon. Dette er viktig ved oppdatering av kodeverk (t.d. NACE Rev. 1 → Rev. 2).

```yaml
erstattar:
  slot_uri: xkos:supersedes
  range: Klassifikasjon
  multivalued: true
  description: Eldre klassifikasjon som dette kodeverktet erstattar (xkos:supersedes).
```

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Status:** ⚠️ Manglande Anbefalt eigeskap — middels prioritet

---

### 8 — `uneskos:contains` manglar på `Klassifikasjon` (Anbefalt)

Spesifikasjonen har `uneskos:contains` (Anbefalt) for å peike direkte til kategoriane
som høyrer til ein klassifikasjon — ein snarveg framfor å bruke `xkos:levels` + `skos:member`.

```yaml
inneheld_kategori:
  slot_uri: uneskos:contains
  range: Kategori
  multivalued: true
  description: Kategoriar klassifikasjonen inneheld (uneskos:contains).
```

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Status:** ⚠️ Manglande Anbefalt eigeskap — låg prioritet

---

### 9 — Innhaldsmerknadar manglar på `Kategori` (Anbefalt)

Spesifikasjonen har to Anbefalt eigenskapar for å beskrive kva ein kategori inneheld:

| Eigeskap | URI | Skilnad |
|---|---|---|
| `xkos:coreContentNote` | Hovudinnhald — kva er *typisk* inkludert | Anbefalt |
| `xkos:additionalContentNote` | Tilleggsinnhald — kva er *unntaksvis* inkludert | Anbefalt |

Skjemaet har berre `har_notat` → `skos:note` (Valgfri), som er ein generell merknad
utan differensiering mellom hovudinnhald og tilleggsinnhald.

```yaml
hovudinnhald:
  slot_uri: xkos:coreContentNote
  range: LangString
  multivalued: true
  description: Merknad om kva som typisk er inkludert i kategorien (xkos:coreContentNote).

tilleggsinnhald:
  slot_uri: xkos:additionalContentNote
  range: LangString
  multivalued: true
  description: Merknad om kva som unntaksvis er inkludert i kategorien (xkos:additionalContentNote).
```

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Status:** ⚠️ Manglande Anbefalt eigenskapar — middels prioritet

---

### 10 — `skos:topConceptOf` manglar på `Kategori` (Anbefalt)

Spesifikasjonen har `skos:topConceptOf` (Anbefalt) for å merkje toppnivåkategoriar
direkte på `Kategori`. Skjemaet modellerer hierarkiet via `tilhorande_klassifikasjonsnivaa`
og `har_medlem`, men eksponerer ikkje `skos:topConceptOf` direkte.

**Status:** ⚠️ Manglande Anbefalt eigeskap — låg prioritet

---

### 11 — Anbefalt eigenskapar manglar på `Klassifikasjonssamanlikning`

Spesifikasjonen har fire Anbefalt eigenskapar på `xkos:Correspondence` som ikkje
er modellert i skjemaet:

| Eigeskap | URI | Mangl i schema |
|---|---|---|
| `beskrivelse` | `dct:description` | ✗ |
| `endringsdato` | `dct:modified` | ✗ |
| `spraak` | `dct:language` | ✗ |
| `utgivelsesdato` | `dct:issued` | ✗ |

Alle desse kjem frå `common-ap-no-schema` og kan leggast til `Klassifikasjonssamanlikning.slots`
utan nye slot-definisjonar.

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Status:** ⚠️ Manglande Anbefalt eigenskapar — middels prioritet

---

### 12 — Valgfrie eigenskapar på `Kategori` manglar

Ei rekke Valgfri eigenskapar frå XKOS er ikkje modellert. Dei viktigaste for
klassifikasjonsbruk er:

| Eigeskap | URI | Skildring |
|---|---|---|
| `skos:altLabel` | `skos:altLabel` | Tillate alternativnamn |
| `skos:definition` | `skos:definition` | Definisjon av kategorien |
| `inklusjonsnotat` | `xkos:inclusionNote` | Kva som eksplisitt er inkludert |
| `eksklusjonsnotat` | `xkos:exclusionNote` | Kva som eksplisitt er ekskludert |
| `neste_kategori` | `xkos:next` | Neste kategori på same nivå |
| `forrige_kategori` | `xkos:previous` | Forrige kategori på same nivå |
| `generaliserer` | `xkos:generalizes` | Meir generell enn |
| `spesialiserer` | `xkos:specializes` | Meir spesifikk enn |
| `er_del_av` | `xkos:isPartOf` | Kategorien er del av ein annan |
| `bestar_av_kategori` | `xkos:hasPart` | Kategoriar som er delar av denne |

Inklusjons- og eksklusjonsmerknadar (`inclusionNote`/`exclusionNote`) er særleg
brukt i offisielle kodeverk som NACE, ISIC og SSB-klassar.

**Status:** ℹ️ Manglande Valgfri eigenskapar — låg prioritet

---

### 13 — Designavvik: tidsrom via `dct:temporal` vs. `schema:validFrom`/`schema:validThrough`

Spesifikasjonen brukar direkte datoeigeanskapar på `Klassifikasjon`:

```turtle
ex:klassifikasjon schema:validFrom "2020-01-01"^^xsd:date .
ex:klassifikasjon schema:validThrough "2025-12-31"^^xsd:date .
```

Skjemaet brukar DCAT-AP-NO-mønsteret med `dct:temporal` og ein `Tidsrom`-mellomklasse:

```yaml
gjeld_for_tidsrom:
  slot_uri: dct:temporal
  range: Tidsrom
```

Dette er ein bevisst designbeslutning for å harmonisere med `dcat-ap-no-schema.yaml`.
Semantisk er dette ekvivalent, men dei to serialiseringane produserer ulike RDF-grafar.
Etter at bug i avvik 1 (`dct:startDate` → `dcat:startDate`) er retta, er denne
tilnærminga akseptabel — men det bør dokumenterast i skjemaet at det er ein avvikande
implementasjonsval.

**Status:** ℹ️ Designavvik — ikkje ein feil, men bør dokumenterast

---

## Samandrag

| # | Avvik | Alvor | Prioritet |
|---|---|---|---|
| 1 | `tidsrom_start`/`tidsrom_slutt`: `dct:startDate` → `dcat:startDate` | Bug | **Kritisk** |
| 2 | `antall_nivaa`: Anbefalt → Obligatorisk + `required: true` | Subset-avvik | Middels |
| 3 | `forste_nivaa`: Valgfri → Anbefalt | Subset-avvik | Låg |
| 4 | `skos:notation` manglar på `Kategori` | Manglande Anbefalt | **Høg** |
| 5 | `xkos:covers*`-eigenskapar manglar | Manglande Anbefalt | Middels |
| 6 | `xkos:organizedBy` manglar på `Klassifikasjonsnivaa` | Manglande Anbefalt | Låg |
| 7 | `xkos:supersedes` manglar på `Klassifikasjon` | Manglande Anbefalt | Middels |
| 8 | `uneskos:contains` manglar på `Klassifikasjon` | Manglande Anbefalt | Låg |
| 9 | `xkos:coreContentNote`/`additionalContentNote` manglar | Manglande Anbefalt | Middels |
| 10 | `skos:topConceptOf` manglar på `Kategori` | Manglande Anbefalt | Låg |
| 11 | Fire Anbefalt eigenskapar manglar på `Klassifikasjonssamanlikning` | Manglande Anbefalt | Middels |
| 12 | Valgfri eigenskapar på `Kategori` | Manglande Valgfri | Låg |
| 13 | `dct:temporal` vs `schema:validFrom` — designavvik | Info | — |

---

## Tilrådde tiltak

### XK1 — Fiks `tidsrom_start`/`tidsrom_slutt` slot-URI ✱ Kritisk

```yaml
# Endre
tidsrom_start:
  slot_uri: dct:startDate    # → dcat:startDate
tidsrom_slutt:
  slot_uri: dct:endDate      # → dcat:endDate
```

Legg samstundes til `dcat:`-prefiks i `prefixes:`-seksjonen:

```yaml
prefixes:
  dcat: http://www.w3.org/ns/dcat#
```

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

---

### XK2 — Legg til `notasjon` (`skos:notation`) på `Kategori`

```yaml
# Ny slot
notasjon:
  slot_uri: skos:notation
  range: string
  multivalued: true
  description: Kode for kategorien i klassifikasjonen (skos:notation).

# I Kategori.slot_usage
notasjon:
  in_subset:
    - Anbefalt
```

Legg `notasjon` til i `Kategori.slots`-lista.

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

---

### XK3 — Fiks `antall_nivaa` til Obligatorisk (Avvik 2)

```yaml
# I Klassifikasjon.slot_usage
antall_nivaa:
  in_subset:
    - Obligatorisk
  required: true
```

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`

---

### XK4 — Legg til `xkos:covers*`-eigenskapar (Avvik 5)

```yaml
dekker:
  slot_uri: xkos:covers
  range: Konsept
  multivalued: true
  description: Fagleg domene klassifikasjonen/nivået dekkjer (xkos:covers).

dekker_gjensidig_utelukkande:
  slot_uri: xkos:coversMutuallyExclusively
  range: Konsept
  multivalued: true
  description: Domene dekkja gjensidig utelukkande (xkos:coversMutuallyExclusively).

dekker_uttomande:
  slot_uri: xkos:coversExhaustively
  range: Konsept
  multivalued: true
  description: Domene dekkja uttømmande (xkos:coversExhaustively).
```

Legg til som `Anbefalt` i `Klassifikasjon.slot_usage` og `Klassifikasjonsnivaa.slot_usage`.

---

### XK5 — Legg til `xkos:supersedes` og innhaldsmerknadar (Avvik 7 og 9)

```yaml
erstattar:
  slot_uri: xkos:supersedes
  range: Klassifikasjon
  multivalued: true
  description: Eldre klassifikasjon som dette erstattar (xkos:supersedes).

hovudinnhald:
  slot_uri: xkos:coreContentNote
  range: LangString
  multivalued: true
  description: Merknad om kva som typisk er inkludert i kategorien (xkos:coreContentNote).

tilleggsinnhald:
  slot_uri: xkos:additionalContentNote
  range: LangString
  multivalued: true
  description: Merknad om kva som unntaksvis er inkludert i kategorien (xkos:additionalContentNote).
```

---

### XK6 — Legg Anbefalt eigenskapar til `Klassifikasjonssamanlikning` (Avvik 11)

Legg til desse i `Klassifikasjonssamanlikning.slots` (kjem frå `common-ap-no-schema`):

```yaml
Klassifikasjonssamanlikning:
  slots:
    - id
    - identifikator_literal
    - tittel
    - beskrivelse      # ny
    - utgjevar
    - endringsdato     # ny
    - spraak           # ny
    - utgivelsesdato   # ny
    - samanliknar
    - bestar_av
  slot_usage:
    # ... eksisterande ...
    beskrivelse:
      in_subset:
        - Anbefalt
    endringsdato:
      in_subset:
        - Anbefalt
    spraak:
      in_subset:
        - Anbefalt
    utgivelsesdato:
      in_subset:
        - Anbefalt
```

---

### XK7 — Legg til Valgfri notasjons- og merknadsslotar på `Kategori` (Avvik 12)

Prioriterte Valgfri eigenskapar å legge til:

```yaml
tillaten_term:
  slot_uri: skos:altLabel
  range: LangString
  multivalued: true
  description: Tillate alternativtermar for kategorien (skos:altLabel).

definisjon:
  slot_uri: skos:definition
  range: LangString
  multivalued: true
  description: Definisjon av kategorien (skos:definition).

inklusjonsnotat:
  slot_uri: xkos:inclusionNote
  range: LangString
  multivalued: true
  description: Kva som eksplisitt er inkludert i kategorien (xkos:inclusionNote).

eksklusjonsnotat:
  slot_uri: xkos:exclusionNote
  range: LangString
  multivalued: true
  description: Kva som eksplisitt er ekskludert frå kategorien (xkos:exclusionNote).

neste_kategori:
  slot_uri: xkos:next
  range: Kategori
  description: Neste kategori på same nivå i klassifikasjonen (xkos:next).

forrige_kategori:
  slot_uri: xkos:previous
  range: Kategori
  description: Forrige kategori på same nivå i klassifikasjonen (xkos:previous).
```

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | XK1: Fiks `dct:startDate` → `dcat:startDate` | `xkos-ap-no-schema.yaml` | — |
| 2 | XK2: Legg til `notasjon` (`skos:notation`) | `xkos-ap-no-schema.yaml` | — |
| 3 | XK3: `antall_nivaa` Obligatorisk + `required: true` | `xkos-ap-no-schema.yaml` | — |
| 4 | XK4: `xkos:covers*`-eigenskapar | `xkos-ap-no-schema.yaml` | — |
| 5 | XK5: `xkos:supersedes` + innhaldsmerknadar | `xkos-ap-no-schema.yaml` | — |
| 6 | XK6: Anbefalt eigenskapar på Klassifikasjonssamanlikning | `xkos-ap-no-schema.yaml` | — |
| 7 | XK7: Valgfri slotar på Kategori | `xkos-ap-no-schema.yaml` | — |

---

## Avhengigheiter

- XK1 krev at `dcat:`-prefiks vert lagt til i `xkos-ap-no-schema.yaml`
- Etter XK1: køyr `make roundtrip SCHEMA=src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`
  for å verifisere at `tidsrom_start`/`tidsrom_slutt` produserer korrekte DCAT-URI-ar i RDF
- XK2 og XK7 påverkar eksempelfila — `xkos-ap-no-eksempel.yaml` bør oppdaterast med
  `notasjon`-verdiar (t.d. «A», «01» for NACE-seksjoner og -avdelingar)
- XK3–XK6 er uavhengige av kvarandre og kan gjerast i ein commit
