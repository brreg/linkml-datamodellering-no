# SKAL vs. KAN vokabular — range-korrigering

**Bakgrunn:** Spesifikasjonane seier at visse attributtar **SKAL** bruke eit bestemt kontrollert vokabular, medan andre **KAN** bruke eitt eller fleire vokabular. Dette må reflekterast i `range`-feltet i LinkML-skjemaa:

- **SKAL-vokabular** → `range` skal peike direkte til enum-et (t.d. `range: EUAccessRight`)
- **KAN-vokabular** → `range: Konsept` + kommentar som tydeleg beskriv kva vokabular som kan brukast

**Gjeldande situasjon:** Fleire slots brukar `range: Konsept` trass i at spesifikasjonen seier "SKAL veljast frå" eit bestemt vokabular.

## Identifiserte SKAL-vokabular med feil range

### common-ap-no-schema.yaml

| Slot | Noverande range | Korrekt range | Vokabular |
|---|---|---|---|
| `spraak` | `Konsept` | **Problem:** EULanguage dekkjer berre norske språk (7 verdiar), men spec krev heile EU Language-vokabularet (~100 språk) | EU Language |
| `format` | `Konsept` | **Problem:** EUFileType dekkjer berre 9 format, men spec krev heile EU File Type-vokabularet (~50 format) | EU File Type |
| `lisens` | `Lisensdokument` | Korrekt (eigen klasse, ikkje enum) | EU Licence |
| `status` | `Konsept` | `ADMSStatus` (?) — enum har 4 verdiar, vokabularet kan ha fleire | ADMS Status |

### dcat-ap-no-schema.yaml

| Slot | Noverande range | Korrekt range | Vokabular |
|---|---|---|---|
| `frekvens` | `Konsept` | **Vurder:** DCTFrequency eller Konsept? | DCT Frequency |
| `tilgangsrettigheter` | `Konsept` | **Vurder:** EUAccessRight eller Konsept? | EU Access Right |
| `tema` | `Konsept` | Korrekt (Los er for stort) | Los |

### cpsv-ap-no-schema.yaml

| Slot | Noverande range | Korrekt range | Vokabular |
|---|---|---|---|
| `oppdateringsfrekvens` | `Konsept` | **Vurder:** DCTFrequency eller Konsept? | DCT Frequency |
| `spraak` | `Konsept` | Same som common-ap-no | EU Language |

## Problem: Delvis enum-implementering

**EU Language-eksempel:**
- Enum `EULanguage` har 7 verdiar (norske språk)
- EU Language-vokabularet har ~100 verdiar (alle EU-språk)
- Dersom vi set `range: EULanguage`, kan brukarar **ikkje** bruke t.d. `http://publications.europa.eu/resource/authority/language/SWE` (svensk)

**Tre løysingar:**

### Alternativ A: Utvide enumane til full dekning

**Fordel:** `range` kan peike direkte til enum
**Ulempe:** 
- EULanguage: 7 → ~100 verdiar
- EUFileType: 9 → ~50 verdiar
- DCTFrequency: 23 verdiar (allereie full dekning)
- EUAccessRight: 3 verdiar (allereie full dekning)

**Arbeidsmengd:** Høg — må hente alle verdiar frå EU Publications Office

### Alternativ B: Behalde `range: Konsept` for delvise enum

**Fordel:** Brukarar kan bruke verdiar utanfor enum
**Ulempe:** `range: Konsept` gjev ikkje typetryggleik — ingen validering av at URI faktisk er frå korrekt vokabular

**Arbeidsmengd:** Låg — berre dokumentasjonsjustering

### Alternativ C: Lag full enum, men tillat any_of

**Fordel:** Typetryggleik for vanlege verdiar, fleksibilitet for resten
**Ulempe:** LinkML støttar ikkje `any_of: [EULanguage, Konsept]` på ein semantisk korrekt måte

**Arbeidsmengd:** Middels

## Anbefaling

**Kort sikt (denne spesifikasjonen):**

1. **Fullt dekkja enum (range: enum):**
   - `status` → `range: ADMSStatus` (4 verdiar, full dekning)
   - `tilgangsrettigheter` → `range: EUAccessRight` (3 verdiar, full dekning)

2. **Delvis dekkja enum (range: Konsept + kommentar):**
   - `spraak` → behald `range: Konsept`, dokumenter: "SKAL veljast frå EU Language. EULanguage-enum dekkjer norske språk; bruk http://publications.europa.eu/resource/authority/language/ for andre."
   - `format` → behald `range: Konsept`, dokumenter: "SKAL veljast frå EU File Type. EUFileType-enum dekkjer vanlege format; bruk http://publications.europa.eu/resource/authority/file-type/ for andre."
   - `frekvens` → behald `range: Konsept`, dokumenter: "SKAL veljast frå EU Frequency. DCTFrequency-enum dekkjer alle standardverdiar."
   - `oppdateringsfrekvens` → same som `frekvens`

3. **KAN-vokabular (range: Konsept + kommentar):**
   - `tema` → behald `range: Konsept`, dokumenter: "SKAL bruke Los som primærvokabular (https://psi.norge.no/los/tema/<namn>). EuroVoc kan brukast som sekundærvokabular. Bruk MCP-server mcp__linkml-begrep-utkast__list_los_tema for å søkje."

**Lang sikt:**

- Lag full dekning av EULanguage, EUFileType, DCTFrequency frå EU Publications Office
- Vurder LinkML-pattern for "base enum + open extension" dersom LinkML får støtte

## Tiltak

- [ ] Endre `status` til `range: ADMSStatus` (dersom full dekning)
- [ ] Endre `tilgangsrettigheter` til `range: EUAccessRight` (dersom full dekning)
- [ ] Oppdater kommentarar for `spraak`, `format`, `frekvens`, `oppdateringsfrekvens` med klar SKAL/KAN-guideline
- [ ] Oppdater kommentar for `tema` med Los-primær/EuroVoc-sekundær-guideline
- [ ] Dokumenter i `common-ap-no` kva enum som er full dekning vs. delvis dekning

## Open spørsmål

1. **Skal vi tillate verdiar utanfor enum?**
   - Dersom `range: EUAccessRight`, kan brukarar **ikkje** bruke eigendefinerte URI-ar
   - Dersom `range: Konsept`, kan brukarar bruke kva som helst URI (ingen validering)

2. **Skal vi utvide EULanguage til alle EU-språk?**
   - Ja → arbeidsmengd ~90 nye verdiar
   - Nei → behald `range: Konsept` for `spraak`

3. **Skal vi utvide EUFileType til alle EU-filformat?**
   - Ja → arbeidsmengd ~40 nye verdiar
   - Nei → behald `range: Konsept` for `format`

4. **Skal vi sjekke om ADMS Status har fleire verdiar enn dei 4 i enum?**
   - http://purl.org/adms/status/ — sjekk om det er fleire statusar

## Neste steg

1. Verifiser full dekning av eksisterande enum mot autoritativ kjelde
2. Bestem strategi: full dekning (A) eller delvis + Konsept (B)
3. Implementer valgt strategi
4. Oppdater dokumentasjon i alle skjema
