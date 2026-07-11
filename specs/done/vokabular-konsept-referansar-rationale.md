# Rationale: Kvifor open-ended vokabular vert behaldne som Konsept-referansar

**Bakgrunn:** AP-NO-spesifikasjonane refererer til fleire kontrollerte vokabular. Nokre av desse er modellerte som LinkML-enumerasjonar i `common-ap-no-schema.yaml`, medan andre er behaldne som `Konsept`-referansar (range: Konsept).

## Prinsipp

**Enum-kandidatar:** Vokabular med:
- Avgrensa, stabil verdimengd (< 30 verdiar)
- Klart definerte URI-ar per verdi
- Autorisert av standardiseringsorganisasjon (W3C, EU Publications Office, o.l.)
- Låg endringsfrekvens

**Konsept-referansar:** Vokabular med:
- Open-ended verdimengd (kan vekse over tid)
- Domenespesifikke eller kontekstavhengige verdiar
- Høg endringsfrekvens eller ingen autoritativ kjelde
- Fritekst eller lokalt definerte vokabular

## Modellerte som enum (common-ap-no)

| Enum | Vokabular-URI | Verdiar | Grunngjeving |
|---|---|---|---|
| `EULicence` | `http://publications.europa.eu/resource/authority/licence/` | 8 | Stabil, autorisert av EU Publications Office |
| `EUFileType` | `http://publications.europa.eu/resource/authority/file-type/` | 9 | Stabil, autorisert av EU Publications Office |
| `EULanguage` | `http://publications.europa.eu/resource/authority/language/` | 7 (norske) | Stabil, ISO 639-basert, autorisert |
| `ADMSStatus` | `http://purl.org/adms/status/` | 4 | Stabil, W3C-standard |
| `EUAccessRight` | `http://publications.europa.eu/resource/authority/access-right/` | 3 | Stabil, autorisert av EU Publications Office |
| `ADMSPublisherType` | `http://purl.org/adms/publishertype/` | 11 | Stabil, W3C-standard |
| `DCTFrequency` | `http://publications.europa.eu/resource/authority/frequency/` | 23 | Stabil, autorisert av EU Publications Office |

## Behaldne som Konsept-referansar

### 1. Los (tema) — `https://psi.norge.no/los/`

**Kvifor ikkje enum:**
- ~200 hovudtema + ~800 undertema = for stort til enum
- Hierarkisk struktur (tre-nivå) passar ikkje enum-modellen
- Oppdaterast med jamne mellomrom av Digdir

**Løysing:**
- Bruk `range: Konsept` med `annotations.gyldige_verdier: https://psi.norge.no/los/`
- MCP-server `mcp__linkml-begrep-utkast__list_los_tema` gjev tilgang til Los-APIet
- Dokumentasjon i `tema`-slot-skildringa viser korleis ein brukar Los

**Eksempel:**
```yaml
tema:
  - https://psi.norge.no/los/tema/helse-og-omsorg
  - https://psi.norge.no/los/tema/helse-og-omsorg/helsetjenester
```

### 2. PROV Activity — `prov:Activity`

**Kvifor ikkje enum:**
- Open-ended — kvar domene kan definere eigne aktivitetstypar
- PROV-O er eit generisk rammeverk, ikkje eit lukka vokabular
- Verdien er ofte ein URI til ein domenespesifikk aktivitetsbeskrivelse

**Løysing:**
- Bruk `range: uri` med `annotations.gyldige_verdier: URI til prov:Activity`
- Brukaren definerer sjølv aktiviteten som passen for deira datasett

### 3. PROV Attribution — `prov:Attribution`

**Kvifor ikkje enum:**
- Same grunngjeving som PROV Activity
- Kvalifisert attributering er kontekstspesifikk

**Løysing:**
- Bruk `range: string` med `annotations.gyldige_verdiar: prov:Attribution`
- LinkML har ikkje innebygd støtte for PROV-attributeringsstruktur

### 4. ODRL Policy — `odrl:Policy`

**Kvifor ikkje enum:**
- ODRL-policyer er komplekse strukturar med permissions, prohibitions, duties
- Krev eigen LinkML-modell (utanfor scope for AP-NO)
- Verdien er vanlegvis ein URI til ein ekstern policy-ressurs

**Løysing:**
- Bruk `range: uri` med `annotations.gyldige_verdiar: odrl:Policy`
- Brukaren peikar til ein ODRL-policy-URI

### 5. Dublin Core ProvenanceStatement — `dct:ProvenanceStatement`

**Kvifor ikkje enum:**
- Fritekst-beskrivelse av eierskapshistorikk og opphav
- Ingen kontrollert vokabular — kvart datasett har unik historikk

**Løysing:**
- Bruk `range: string` (allereie korrekt i `dcat-ap-no`)
- `annotations.gyldige_verdiar: dct:ProvenanceStatement` er misvisande — fjern det

### 6. CPSV type_concept-felt utan spesifisert vokabular

**Kvifor ikkje enum:**
- CPSV-AP-NO-spesifikasjonen definerer ikkje kontrollerte vokabular for desse felta
- Ulike land/kontekstar kan bruke ulike vokabular
- Opptil implementerande verksemd å velje vokabular

**Løysing:**
- Bruk `range: Konsept` (allereie korrekt)
- Dokumenter i slot-skildringa at verdien er open-ended
- Eksempel: `type_concept` for Hendelse kan vere ISO 8601-event-typar, nasjonale livshendingskodar, o.l.

### 7. vCard Category — `vcard:category`

**Kvifor ikkje enum:**
- vCard 4.0-spesifikasjonen definerer ikkje eit lukka vokabular for category
- Verdien er open-ended fritekst eller URI

**Løysing:**
- Bruk `range: string` (allereie korrekt i `cpsv-ap-no`)

### 8. XKOS covers/organizedBy

**Kvifor ikkje enum:**
- `xkos:covers` peikar til fagleg domene klassifikasjonen dekkjer (Konsept)
- `xkos:organizedBy` peikar til organiseringsprinsipp (Konsept)
- Begge er open-ended — avheng av klassifikasjonsdomenet

**Løysing:**
- Bruk `range: Konsept` (allereie korrekt)
- Dokumenter i slot-skildringa at verdien er kontekstspesifikk

### 9. Termlosen AssosiativeRelationRole

**Kvifor ikkje enum (enno):**
- Vokabularet `https://data.norge.no/vocabulary/skosno/associative-relation-role` finst ikkje (404)
- SKOS-AP-NO-spesifikasjonen nemner «8 kategoriar» men definerer dei ikkje
- Truleg referanse til ISO 25964-1, men ikkje publisert som norsk vokabular

**Løysing (mellombels):**
- Bruk `range: Konsept` med dokumentasjon: «Kandidat: Termlosen sine 8 relasjonskategoriar (ikkje publisert enno)»
- Dersom vokabularet vert publisert seinare, kan det modellerast som enum

### 10. EuroVoc Status — `euvoc:status`

**Kvifor ikkje enum (enno):**
- EuroVoc-spesifikt statusvokabular for omgrep
- Lite brukt utanom EuroVoc-kontekst
- Manglar klar URI-dokumentasjon

**Løysing (mellombels):**
- Bruk `range: Konsept` (allereie korrekt)
- Dersom det er behov, kan det modellerast som enum seinare

## Oppsummering

**Modellerte som enum (7):**
- EULicence, EUFileType, EULanguage, ADMSStatus, EUAccessRight, ADMSPublisherType, DCTFrequency

**Behaldne som Konsept-referansar (10):**
- Los (for stort), PROV Activity/Attribution (open-ended), ODRL Policy (kompleks struktur), dct:ProvenanceStatement (fritekst), CPSV type_concept (ikkje spesifisert), vCard category (open-ended), XKOS covers/organizedBy (kontekstspesifikk), Termlosen AssosiativeRelationRole (ikkje publisert), EuroVoc Status (lite brukt)

**Prinsippet:** Enum for lukka, stabile, autoritative vokabular. Konsept-referansar for open-ended, kontekstspesifikke eller ikkje-publiserte vokabular.
