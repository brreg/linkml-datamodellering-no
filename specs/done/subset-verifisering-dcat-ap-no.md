# Verifisering av subset-definisjonar i dcat-ap-no-schema.yaml

## Bakgrunn

I den auto-genererte dokumentasjonen (`mkdocs/docs/ap-no/dcat-ap-no/index.md`) er det 17 klasser totalt:
- **Obligatorisk (12):** Aktoer, Datasett, Datasettserie, Datatjeneste, Distribusjon, Identifikator, Katalog, Katalogpost, Kontaktopplysning, Relasjon, Sjekksum, Standard
- **Andre (5):** Gebyr, KatalogisertRessurs, RegulativRessurs, Rettighetserklaring, Tidsrom

Dei 5 klassane under "Andre" har mange slots som manglar `in_subset`-definisjon i `slot_usage`. Dette må verifikerast mot DCAT-AP-NO-spesifikasjonen.

## Målsetting

1. Verifisere subset-status (Obligatorisk/Anbefalt/Valgfri) for ALLE slots i ALLE klasser mot DCAT-AP-NO-spesifikasjonen
2. Oppdatere `slot_usage` med korrekt `in_subset`-definisjon der det manglar
3. Sikre at skjemaet er i full samsvar med spesifikasjonen

## Referanse: DCAT-AP-NO-spesifikasjon

**Kjelde:** https://informasjonsforvaltning.github.io/dcat-ap-no/

**Klassar og paragrafar:**

| Klasse | Paragraf | Status |
|---|---|---|
| Aktoer (foaf:Agent) | § 3.1 | Metadata |
| Datasett (dcat:Dataset) | § 3.2 | Metadata |
| Datatjeneste (dcat:DataService) | § 3.4 | Metadata |
| Distribusjon (dcat:Distribution) | § 3.5 | Metadata |
| Gebyr (cv:Cost) | § 3.6 | Metadata |
| Tidsrom (dct:PeriodOfTime) | § 3.17 | Metadata |
| Katalog (dcat:Catalog) | § 3.8 | Metadata |
| Standard (dct:Standard) | § 3.16 | Metadata |
| Katalogpost (dcat:CatalogRecord) | § 3.10 | Metadata |
| RegulativRessurs (eli:LegalResource) | § 3.12 | Metadata |
| Identifikator (adms:Identifier) | § 3.11 | Metadata |
| Rettighetserklaring (dct:RightsStatement) | § 3.14 | Metadata |
| Kontaktopplysning (vcard:Kind) | § 3.3 | Metadata |
| Relasjon (dcat:Relationship) | § 3.15 | Metadata |
| Sjekksum (spdx:Checksum) | § 3.18 | Metadata |
| Datasettserie (dcat:DatasetSeries) | § 3.19 | Metadata |
| KatalogisertRessurs (dcat:Resource) | § 3.20 | Abstract base class |

## Verifiserte klasser og deira slots

### 1. Tidsrom (dct:PeriodOfTime) – § 3.17

**Frå spesifikasjonen:**
- **Obligatoriske:** Ingen
- **Anbefalte:** sluttdato (dcat:endDate), startdato (dcat:startDate)
- **Valfrie:** begynnelse (time:hasBeginning), slutt (time:hasEnd)

**Noverande status i skjema:**
- `startdato` — MANGLAR subset
- `sluttdato` — MANGLAR subset
- `begynnelse` — MANGLAR subset
- `slutt` — MANGLAR subset

**Tiltak:**
- [ ] Legg til `in_subset: [Anbefalt]` på `startdato` og `sluttdato`
- [ ] Legg til `in_subset: [Valgfri]` på `begynnelse` og `slutt`

---

### 2. Standard (dct:Standard) – § 3.16

**Frå spesifikasjonen:**
- **Obligatoriske:** tittel (dct:title)
- **Anbefalte:** har_referanse (rdfs:seeAlso)
- **Valfrie:** har_merknad (rdfs:comment), versjon (dcat:version)

**Noverande status i skjema:**
- `tittel` — har `required: true` og `in_subset: [Obligatorisk]` ✓
- `har_referanse` — har `in_subset: [Anbefalt]` ✓
- `har_merknad` — har `in_subset: [Valgfri]` ✓
- `versjon` — har `in_subset: [Valgfri]` ✓

**Tiltak:**
- [x] Standard er korrekt — ingen endringar nødvendige

---

### 3. RegulativRessurs (eli:LegalResource) – § 3.12

**Frå spesifikasjonen:**
- **Obligatoriske:** Ingen
- **Anbefalte:** beskrivelse (dct:description), identifikator_literal (dct:identifier), har_referanse (rdfs:seeAlso), spraak (dct:language), tittel (dct:title), type_concept (dct:type)
- **Valfrie:** relatert_regulativ_ressurs (dct:relation)

**Noverande status i skjema:**
- `beskrivelse` — MANGLAR subset
- `identifikator_literal` — MANGLAR subset
- `har_referanse` — MANGLAR subset
- `spraak` — MANGLAR subset
- `tittel` — MANGLAR subset
- `type_concept` — MANGLAR subset
- `relatert_regulativ_ressurs` — MANGLAR subset

**Tiltak:**
- [ ] Legg til `in_subset: [Anbefalt]` på `beskrivelse`, `identifikator_literal`, `har_referanse`, `spraak`, `tittel`, `type_concept`
- [ ] Legg til `in_subset: [Valgfri]` på `relatert_regulativ_ressurs`

---

### 4. Rettighetserklaring (dct:RightsStatement) – § 3.14

**Frå spesifikasjonen:**
- **Obligatoriske:** Ingen
- **Anbefalte:** anvendelsesretningslinjer (odrs:reuserGuidelines), jurisdiksjon (odrs:jurisdiction), krediteringstekst (odrs:attributionText), krediteringsurl (odrs:attributionURL), opphavsrettserklaring (odrs:copyrightStatement), opphavsrettsinnehaver (odrs:copyrightHolder)
- **Valfrie:** opphavsrettsnotis (odrs:copyrightNotice), opphavsrettsaar (odrs:copyrightYear)

**Noverande status i skjema:**
- `anvendelsesretningslinjer` — MANGLAR subset
- `jurisdiksjon` — MANGLAR subset
- `krediteringstekst` — MANGLAR subset
- `krediteringsurl` — MANGLAR subset
- `opphavsrettserklaring` — MANGLAR subset
- `opphavsrettsinnehaver` — MANGLAR subset
- `opphavsrettsnotis` — MANGLAR subset
- `opphavsrettsaar` — MANGLAR subset

**Tiltak:**
- [ ] Legg til `in_subset: [Anbefalt]` på `anvendelsesretningslinjer`, `jurisdiksjon`, `krediteringstekst`, `krediteringsurl`, `opphavsrettserklaring`, `opphavsrettsinnehaver`
- [ ] Legg til `in_subset: [Valgfri]` på `opphavsrettsnotis`, `opphavsrettsaar`

---

### 5. Gebyr (cv:Cost) – § 3.6

**Frå spesifikasjonen:**
- **Obligatoriske:** Ingen
- **Anbefalte:** belop (cv:hasValue), beskrivelse (dct:description), dokumentasjon (foaf:page), valuta (cv:currency)
- **Valfrie:** Ingen

**Noverande status i skjema:**
- `belop` — MANGLAR subset
- `beskrivelse` — MANGLAR subset
- `dokumentasjon` — MANGLAR subset
- `valuta` — MANGLAR subset

**Tiltak:**
- [ ] Legg til `in_subset: [Anbefalt]` på `belop`, `beskrivelse`, `dokumentasjon`, `valuta`

---

### 6. Aktoer (foaf:Agent) – § 3.1

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.1

---

### 7. Datasett (dcat:Dataset) – § 3.2

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.2

---

### 8. Datatjeneste (dcat:DataService) – § 3.4

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.4

---

### 9. Distribusjon (dcat:Distribution) – § 3.5

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.5

---

### 10. Katalog (dcat:Catalog) – § 3.8

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.8

---

### 11. Katalogpost (dcat:CatalogRecord) – § 3.10

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.10

---

### 12. Identifikator (adms:Identifier) – § 3.11

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.11

---

### 13. Kontaktopplysning (vcard:Kind) – § 3.3

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.3

---

### 14. Relasjon (dcat:Relationship) – § 3.15

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.15

---

### 15. Sjekksum (spdx:Checksum) – § 3.18

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.18

---

### 16. Datasettserie (dcat:DatasetSeries) – § 3.19

**Må hentast frå spesifikasjonen**

**Tiltak:**
- [ ] Verifiser mot § 3.19

---

### 17. KatalogisertRessurs (dcat:Resource) – § 3.20

**Merknad:** Dette er ein abstrakt basisklasse. Skal ikkje ha slot-subset-definisjonar.

**Tiltak:**
- [x] Ingen handling nødvendig

---

## Utføringsplan

1. **[x] Steg 1:** Hent subset-status for alle resterande klasser (§ 3.1, 3.2, 3.3, 3.4, 3.5, 3.8, 3.10, 3.11, 3.15, 3.18, 3.19) frå spesifikasjonen
2. **[x] Steg 2:** Samanlikn med noverande `slot_usage` i `dcat-ap-no-schema.yaml`
3. **[x] Steg 3:** Identifiser alle avvik (manglande subset, feil subset-nivå)
4. **[x] Steg 4:** Oppdater `slot_usage` i `dcat-ap-no-schema.yaml` med korrekt subset (101 endringar)
5. **[x] Steg 5:** Valider skjemaet (`make lint`) — 6 prefix-åtvaringar (ikkje-kritiske)
6. **[ ] Steg 6:** Regenerer dokumentasjon (`make domain-ap-no`)
7. **[ ] Steg 7:** Generer commit-melding

## Avvik funne

**Totalt: 100 avvik**

### Avvik per type:
- **MANGLAR_SLOT_USAGE:** 91 tilfelle — slot finst i `slots:`, men manglar `slot_usage:`-entry
- **FEIL_SUBSET:** 7 tilfelle — slot har `in_subset`, men feil verdi (t.d. Anbefalt i staden for Valgfri)
- **MANGLAR_IN_SUBSET:** 1 tilfelle — slot har `slot_usage:`, men manglar `in_subset:`-felt
- **MANGLAR_I_SLOTS:** 1 tilfelle — slot manglar i klassen sin `slots:`-liste (Datasett.tidsopplosning)

### Avvik per klasse:

| Klasse | Antal avvik | Hovudproblem |
|---|---|---|
| Datasett | 29 | Dei fleste valfrie slots manglar slot_usage |
| Distribusjon | 18 | Dei fleste valfrie slots manglar slot_usage |
| Datatjeneste | 11 | Alle valfrie slots manglar slot_usage |
| Katalog | 8 | Alle valfrie slots manglar slot_usage |
| RegulativRessurs | 7 | Alle anbefalte/valfrie slots manglar slot_usage |
| Rettighetserklaring | 8 | Alle anbefalte/valfrie slots manglar slot_usage |
| Datasettserie | 4 | Alle valfrie slots manglar slot_usage |
| Katalogpost | 4 | Alle valfrie slots manglar slot_usage |
| Tidsrom | 4 | Alle anbefalte/valfrie slots manglar slot_usage |
| Gebyr | 4 | Alle anbefalte slots manglar slot_usage |
| Kontaktopplysning | 2 | Begge anbefalte slots manglar slot_usage |
| Aktoer | 1 | type_concept manglar in_subset |

### Kritiske avvik (FEIL_SUBSET):

1. **Datasett.dokumentasjon** — er Anbefalt, skal vere Valgfri
2. **Datasett.frekvens** — er Anbefalt, skal vere Valgfri
3. **Datasett.har_kvalitetsmerknad** — er Anbefalt, skal vere Valgfri
4. **Datasett.har_kvalitetsmaaling** — er Anbefalt, skal vere Valgfri
5. **Datasett.identifikator_literal** — er Anbefalt, skal vere Valgfri
6. **Datasett.landingsside** — er Anbefalt, skal vere Valgfri
7. **Distribusjon.nedlastningslenke** — er Anbefalt, skal vere Valgfri

### Spesielt avvik:

**Datasett.tidsopplosning** — manglar heilt i `slots:`-lista, men er definert som global slot. Må leggjast til i Datasett.slots.

## Utført

**Dato:** 2026-07-27

**Endringar:**

1. **Lagt til manglande slot i Datasett:** `tidsopplosning` (dcat:temporalResolution) vart lagt til i `Datasett.slots`

2. **Oppdatert slot_usage for 101 slots** i desse klassane:
   - **Aktoer:** type_concept → Anbefalt
   - **Datasett:** 29 slots oppdatert (annen_ansvarlig_aktor, annen_identifikator, dokumentasjon m.fl.)
   - **Kontaktopplysning:** har_epost, har_kontaktside → Anbefalt
   - **Datatjeneste:** 11 valfrie slots oppdatert
   - **Distribusjon:** 18 valfrie slots oppdatert
   - **Katalog:** 8 valfrie slots oppdatert
   - **Katalogpost:** 4 valfrie slots oppdatert
   - **Datasettserie:** 4 valfrie slots oppdatert
   - **Tidsrom:** startdato, sluttdato → Anbefalt; begynnelse, slutt → Valgfri
   - **RegulativRessurs:** 6 anbefalte + 1 valfri slot oppdatert
   - **Rettighetserklaring:** 6 anbefalte + 2 valfrie slots oppdatert
   - **Gebyr:** belop, beskrivelse, dokumentasjon, valuta → Anbefalt

3. **Retta kritiske FEIL_SUBSET-avvik:**
   - Datasett.dokumentasjon: Anbefalt → Valgfri
   - Datasett.frekvens: Anbefalt → Valgfri
   - Datasett.har_kvalitetsmerknad: Anbefalt → Valgfri
   - Datasett.har_kvalitetsmaaling: Anbefalt → Valgfri
   - Datasett.identifikator_literal: Anbefalt → Valgfri
   - Datasett.landingsside: Anbefalt → Valgfri
   - Distribusjon.nedlastningslenke: Anbefalt → Valgfri

**Resultat:**
- Alle 100 avvik retta
- Skjemaet er no i full samsvar med DCAT-AP-NO-spesifikasjonen (https://informasjonsforvaltning.github.io/dcat-ap-no/)
- Alle slots har korrekt subset-definisjon (Obligatorisk/Anbefalt/Valgfri)

**Validering:**
- `make lint`: 6 prefix-åtvaringar (ikkje-kritiske — handlar om alias som `dct` vs. `dcterms`)
- Verifiseringstest: ✅ Alle 14 testtilfelle passerte

**Neste steg:**
- Regenerer dokumentasjon (`make domain-ap-no`) for å oppdatere `mkdocs/docs/ap-no/dcat-ap-no/index.md`
- Generer commit-melding i conventional commits-format
