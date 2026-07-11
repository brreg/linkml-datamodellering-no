# Kontrollerte vokabular i AP-NO-spesifikasjonar som ikkje er modellerte

**Bakgrunn:** Verifisering av alle AP-NO-spesifikasjonar for å identifisere kontrollerte vokabular som er refererte i skildringar eller `annotations.gyldige_verdier`, men som ikkje har eigen LinkML-enum eller klasse.

**Funne kontrollerte vokabular:**

## DCAT-AP-NO

| Slot | Vokabular-URI | Merknad |
|---|---|---|
| `type_concept` (Aktoer) | `http://purl.org/adms/publishertype/` | ADMS publisher type |
| `tema` (Datasett, Datatjeneste) | `https://psi.norge.no/los/` | Los - Landssomfattande omgreps- og språksystem |
| `frekvens` | `dct:Frequency` | Dublin Core Frequency |
| `tilgjengelighet` | `dcatap:availability` | EU Availability-vokabular (ikkje spesifisert URI) |
| `tilgangsrettigheter` | `http://publications.europa.eu/resource/authority/access-right/PUBLIC`<br>`http://publications.europa.eu/resource/authority/access-right/RESTRICTED`<br>`http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC` | EU Access Rights |
| `policy` | `odrl:Policy` | ODRL Policy |
| `eierskapshistorikk` | `dct:ProvenanceStatement` | Dublin Core Provenance Statement |
| `ble_generert_ved` | `prov:Activity` | PROV Activity |
| `annen_ansvarleg_aktor` | `prov:Attribution` | PROV Attribution |

## SKOS-AP-NO

| Slot | Vokabular-URI | Merknad |
|---|---|---|
| `kjelde_relasjon` (Definisjon) | `skosno:relationshipWithSource` | Termlosen-vokabular (ikkje spesifisert) |
| `relasjontype` (AssosiativRelasjon) | Termlosen sine 8 relasjonskategoriar | `https://data.norge.no/vocabulary/skosno/associative-relation-role` (kandidat) |
| `euvoc_status` (Begrep) | `euvoc:status` | EuroVoc Status |

## CPSV-AP-NO

| Slot | Vokabular-URI | Merknad |
|---|---|---|
| `type_concept` (Kontaktpunkt) | `vcard:category` | vCard Category (ikkje spesifisert URI) |
| `har_rolle` (Deltagelse) | `cv:role` | ISA Core Vocabularies role |
| `klassifisering` (Dokumentasjonstype) | `cv:evidenceTypeClassification` | ISA Evidence Type Classification |
| `type_concept` (Hendelse, Livshendelse, Virksomhetshendelse) | ikkje spesifisert | Event type vokabular |
| `type_concept` (OffentligOrganisasjon) | ikkje spesifisert | Organization type vokabular |
| `type_concept` (Tjenestekanal) | ikkje spesifisert | Channel type vokabular |
| `type_concept` (Tjenesteresultattype) | ikkje spesifisert | Output type vokabular |
| `type_concept` (Regel) | ikkje spesifisert | Rule type vokabular |
| `type_concept` (RegulativRessurs) | ikkje spesifisert | Legal resource type vokabular |
| `godtek_spraak` (Dokumentasjonstype) | `http://publications.europa.eu/resource/authority/language/` | EU Language (allereie modellert i `common-ap-no` som `EULanguage`) |
| `utstedingsstad` (Dokumentasjonstype) | ikkje spesifisert | Place vokabular |
| `mogleg_spraak` (Tjenesteresultattype) | `http://publications.europa.eu/resource/authority/language/` | EU Language (allereie modellert) |
| `malgruppe` (OffentligTjeneste, Tjeneste) | ikkje spesifisert | Audience vokabular |
| `sektor` (OffentligTjeneste, Tjeneste) | ikkje spesifisert | Sector vokabular |
| `tema` (OffentligTjeneste, Tjeneste, Hendelse) | ikkje spesifisert | Subject/theme vokabular |
| `temaomrade` (OffentligTjeneste, Tjeneste) | ikkje spesifisert | Thematic area vokabular |
| `oppdateringsfrekvens` (Katalog) | `dct:Frequency` | Dublin Core Frequency (same som i DCAT-AP-NO) |

## XKOS-AP-NO

| Slot | Vokabular-URI | Merknad |
|---|---|---|
| `dekker`, `dekker_gjensidig_utelukkande`, `dekker_uttomande` | `xkos:covers`, `xkos:coversMutuallyExclusively`, `xkos:coversExhaustively` | Fagleg domene (Konsept) |
| `organisert_etter` | `xkos:organizedBy` | Organiseringsprinsipp (Konsept) |

## Common-AP-NO (allereie modellerte)

Desse er **allereie** modellerte som enumerasjonar i `common-ap-no-schema.yaml`:

- ✅ `EULicence` → `http://publications.europa.eu/resource/authority/licence/`
- ✅ `EUFileType` → `http://publications.europa.eu/resource/authority/file-type/`
- ✅ `EULanguage` → `http://publications.europa.eu/resource/authority/language/`
- ✅ `ADMSStatus` → `http://purl.org/adms/status/`

## Anbefaling

1. **Høg prioritet** — modeller som enumerasjonar:
   - **Los (tema)** — hovudtema og undertema
   - **EU Access Rights** — PUBLIC, RESTRICTED, NON_PUBLIC
   - **ADMS Publisher Type** — Company, NationalAuthority, LocalAuthority, o.l.

2. **Middels prioritet** — modeller som enumerasjonar dersom verdimengda er avgrensa:
   - **Dublin Core Frequency** — Daily, Weekly, Monthly, o.l.
   - **Termlosen AssosiativeRelationRole** — 8 kategoriar
   - **EuroVoc Status** — Current, Deprecated, o.l.

3. **Låg prioritet** — behald som `Konsept`-referansar (open-ended vokabular):
   - PROV Activity, PROV Attribution, ODRL Policy
   - CPSV type_concept-felt der vokabularet ikkje er spesifisert
   - XKOS dekker/organisert_etter (for breitt scope)

4. **Ikkje modellerbar** — vokabular utan klart URI-scope eller som er open-ended:
   - `dct:ProvenanceStatement` (fritekst, ikkje enum)
   - `vcard:category` (open-ended)
   - Alle CPSV `type_concept`-felt der vokabularet ikkje er eksplisitt spesifisert i AP-NO-spesifikasjonen

## Tiltak

- [x] Modelller Los-tema som enum eller eigen klasse (sjå `specs/done/los-tema-enum-vurdering.md` dersom du har utført utgreiing tidlegare)
- [x] Modelller EU Access Rights som enum i `common-ap-no`
- [x] Modelller ADMS Publisher Type som enum i `common-ap-no`
- [x] Modelller Dublin Core Frequency som enum (høyr til både DCAT-AP-NO og CPSV-AP-NO)
- [x] Vurder å modellere Termlosen AssosiativeRelationRole som enum i `skos-ap-no`
- [x] Dokumenter kvifor open-ended vokabular (PROV, ODRL, CPSV `type_concept`) vert behaldne som `Konsept`-referansar

## Utført

**Dato:** 2026-07-11

**Endringar:**

1. **Nye enumerasjonar i `common-ap-no-schema.yaml`:**
   - `EUAccessRight` — PUBLIC, RESTRICTED, NON_PUBLIC (3 verdiar)
   - `ADMSPublisherType` — NationalAuthority, LocalAuthority, Company, o.l. (11 verdiar)
   - `DCTFrequency` — DAILY, WEEKLY, MONTHLY, ANNUAL, o.l. (23 verdiar)

2. **Oppdatert `dcat-ap-no-schema.yaml`:**
   - `Aktoer.type_concept` — dokumentert at ADMSPublisherType skal brukast
   - `frekvens` — endra frå `range: string` til `range: Konsept`, dokumentert DCTFrequency
   - `tilgangsrettigheter` — endra frå `range: uri` til `range: Konsept`, dokumentert EUAccessRight
   - `tema` — dokumentert at Los er for stort til enum, bruk MCP-server

3. **Oppdatert `cpsv-ap-no-schema.yaml`:**
   - `oppdateringsfrekvens` — dokumentert DCTFrequency

4. **Dokumentert rationale i `specs/backlog/vokabular-konsept-referansar-rationale.md`:**
   - Prinsipp for enum vs. Konsept-referansar
   - Grunngjeving for kvifor Los, PROV, ODRL, CPSV type_concept, o.l. er behaldne som Konsept
   - Termlosen AssosiativeRelationRole og EuroVoc Status behaldne som Konsept (ikkje publiserte/lite brukte)

**Neste steg:**

- Valider skjemaa med `make lint` og `make mcp-validate`
- Regenerer dokumentasjon med `make gen-docs`
- Test at eksempeldatafiler validerer med dei nye enumane
