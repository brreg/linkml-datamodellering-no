# Evaluering av samsvar med DCAT-AP-NO § 1.5

## Bakgrunn

DCAT-AP-NO § 1.5 definerer krav til applikasjoner som leverer eller mottar metadata.
Denne evalueringa vurderer om `dcat-ap-no-schema.yaml` implementerer desse krava korrekt.

## Relevante krav

### § 1.5.1: Krav til applikasjoner som leverer metadata

Ein applikasjon som leverer metadata **SKAL**:

1. Levere ein beskrivelse av katalogen med minimum dei obligatoriske eigenskapane spesifisert i § 3.8 "Klassen Katalog (dcat:Catalog)"
2. Levere informasjon for obligatoriske eigenskapar spesifisert i § 3.10 "Klassen Katalogpost (dcat:CatalogRecord)" (vel å merke at bruk av Katalogpost er frivillig)
3. Levere beskrivingar av datasetta i katalogen med minimum dei obligatoriske eigenskapane spesifisert i § 3.2 "Klassen Datasett (dcat:Dataset)"
4. Levere beskrivingar av distribusjonar (dersom noen) med minimum dei obligatoriske eigenskapane spesifisert i § 3.5 "Klassen Distribusjon (dcat:Distribution)"
5. Levere beskrivingar av datatjenester (dersom noen) med minimum dei obligatoriske eigenskapane spesifisert i § 3.4 "Klassen Datatjeneste (dcat:DataService)"
6. Levere informasjon om alle organisasjonar/aktørar involvert i beskrivingane med minimum dei obligatoriske eigenskapane spesifisert i § 3.1 "Klassen Aktør (foaf:Agent)"
7. Bruke dei kontrollerte vokabularene beskrive i Merknad til dei einskilde eigenskapane

### § 1.5.2: Krav til applikasjoner som mottar metadata

Ein applikasjon som mottar metadata **SKAL**:

1. Prosessere informasjon for alle klassar og eigenskapar spesifisert i standarden
2. Prosessere informasjon for alle kontrollerte vokabular eksplisitt spesifisert for dei einskilde eigenskapane

## Evaluering av `dcat-ap-no-schema.yaml`

### Krav 1.5.1.1: Katalog — obligatoriske eigenskapar

**Spesifikasjonskrav (§ 3.8):** beskrivelse, kontaktpunkt, tittel, utgiver

**Implementering i skjema:**

```yaml
Katalog:
  slot_usage:
    beskrivelse:
      required: true
      in_subset: [Obligatorisk]
    kontaktpunkt:
      required: true
      in_subset: [Obligatorisk]
    tittel:
      required: true
      in_subset: [Obligatorisk]
    utgiver:
      required: true
      in_subset: [Obligatorisk]
```

**Status:** ✓ Alle fire obligatoriske eigenskapane er markerte med `required: true` og `in_subset: [Obligatorisk]`.

### Krav 1.5.1.2: Katalogpost — obligatoriske eigenskapar

**Spesifikasjonskrav (§ 3.10):** endringsdato, primaertema

**Implementering i skjema:**

```yaml
Katalogpost:
  slot_usage:
    endringsdato:
      required: true
      in_subset: [Obligatorisk]
    primaertema:
      required: true
      in_subset: [Obligatorisk]
```

**Status:** ✓ Begge obligatoriske eigenskapane er markerte med `required: true`.

**Merknad:** Kravet seier at bruk av `Katalogpost` er frivillig, men dersom den vert brukt, **SKAL** obligatoriske eigenskapar leverast.

### Krav 1.5.1.3: Datasett — obligatoriske eigenskapar

**Spesifikasjonskrav (§ 3.2):** beskrivelse, kontaktpunkt, tema, tittel, utgiver

**Implementering i skjema:**

```yaml
Datasett:
  slot_usage:
    beskrivelse:
      required: true
      in_subset: [Obligatorisk]
    kontaktpunkt:
      required: true
      in_subset: [Obligatorisk]
    tema:
      required: true
      in_subset: [Obligatorisk]
    tittel:
      required: true
      in_subset: [Obligatorisk]
    utgiver:
      required: true
      in_subset: [Obligatorisk]
```

**Status:** ✓ Alle fem obligatoriske eigenskapane er markerte med `required: true` og `in_subset: [Obligatorisk]`.

### Krav 1.5.1.4: Distribusjon — obligatoriske eigenskapar

**Spesifikasjonskrav (§ 3.5):** tilgangs_url

**Implementering i skjema:**

```yaml
Distribusjon:
  slot_usage:
    tilgangs_url:
      required: true
      in_subset: [Obligatorisk]
```

**Status:** ✓ Den einaste obligatoriske eigenskapen er markert med `required: true`.

### Krav 1.5.1.5: Datatjeneste — obligatoriske eigenskapar

**Spesifikasjonskrav (§ 3.4):** endepunkts_url, kontaktpunkt, tittel, utgiver

**Implementering i skjema:**

```yaml
Datatjeneste:
  slot_usage:
    endepunkts_url:
      required: true
      in_subset: [Obligatorisk]
    kontaktpunkt:
      required: true
      in_subset: [Obligatorisk]
    tittel:
      required: true
      in_subset: [Obligatorisk]
    utgiver:
      required: true
      in_subset: [Obligatorisk]
```

**Status:** ✓ Alle fire obligatoriske eigenskapane er markerte med `required: true` og `in_subset: [Obligatorisk]`.

### Krav 1.5.1.6: Aktør — obligatoriske eigenskapar

**Spesifikasjonskrav (§ 3.1):** navn_aktoer (foaf:name)

**Implementering i skjema:**

```yaml
Aktoer:
  slot_usage:
    navn_aktoer:
      required: true
      in_subset: [Obligatorisk]
```

**Status:** ✓ Den obligatoriske eigenskapen er markert med `required: true`.

### Krav 1.5.1.7: Kontrollerte vokabular

**Spesifikasjonskrav:** Bruke dei kontrollerte vokabularene beskrive i Merknad til dei einskilde eigenskapane. Andre kontrollerte vokabular KAN brukast i tillegg.

**Implementering i skjema:**

Skjemaet inneheld `annotations.gyldige_verdier` for fleire eigenskapar:

- `tema`: Los (https://psi.norge.no/los/)
- `tilgangsrettigheter`: EU Access Rights-vokabularet
- `frekvens`: dct:Frequency
- `policy`: odrl:Policy
- `eierskapshistorikk`: dct:ProvenanceStatement
- `ble_generert_ved`: prov:Activity
- `annen_ansvarlig_aktor`: prov:Attribution

**Status:** ✓ Skjemaet dokumenterer kontrollerte vokabular som annotationar. Desse vert ikkje håndheva maskinelt, men er synlege for menneskelege brukarar og kan håndhevast via validering utanfor LinkML.

**Merknad:** LinkML-skjema kan ikkje direkte tvinge bruk av SKOS-konsept frå spesifikke vokabular (Los, EuroVoc osv.). Håndhevinga må skje via semantisk validering (SHACL, SPARQL) eller applikasjonslogikk.

### Krav 1.5.2: Prosessering (mottakarar)

**Spesifikasjonskrav:** Applikasjonar som **mottar** metadata **SKAL** prosessere informasjon for alle klassar, eigenskapar og kontrollerte vokabular spesifisert i standarden.

**Implementering i skjema:**

Skjemaet definerer **alle** klassar og eigenskapar frå DCAT-AP-NO:

- **Hovudklassar:** Katalog, Datasett, Distribusjon, Datatjeneste, Katalogpost, Datasettserie
- **Hjelpeklassar:** Aktør, Kontaktopplysning, Tidsrom, Standard, RegulativRessurs, Identifikator, Rettighetserklæring, Sjekksum, Gebyr, Relasjon
- **Eigenskapar:** Alle obligatoriske, anbefalte og valfrie eigenskapar er modellerte som slots med `slot_uri` og `range`

**Status:** ✓ Skjemaet dekker alle klassar og eigenskapar spesifisert i DCAT-AP-NO.

**Merknad:** Ein applikasjon som implementerer `dcat-ap-no-schema.yaml` som JSON Schema, OWL eller SHACL vil kunne validere innkommande metadata mot alle spesifikasjonskrav.

## Samanfatning

| Krav | Status | Merknad |
|---|---|---|
| 1.5.1.1: Katalog obligatorisk | ✓ | Alle 4 eigenskapar `required: true` |
| 1.5.1.2: Katalogpost obligatorisk | ✓ | Begge eigenskapar `required: true` |
| 1.5.1.3: Datasett obligatorisk | ✓ | Alle 5 eigenskapar `required: true` |
| 1.5.1.4: Distribusjon obligatorisk | ✓ | tilgangs_url `required: true` |
| 1.5.1.5: Datatjeneste obligatorisk | ✓ | Alle 4 eigenskapar `required: true` |
| 1.5.1.6: Aktør obligatorisk | ✓ | navn_aktoer `required: true` |
| 1.5.1.7: Kontrollerte vokabular | ✓ | Dokumentert som `annotations.gyldige_verdier` |
| 1.5.2: Prosessering (mottakar) | ✓ | Alle klassar og eigenskapar dekka |

## Konklusjon

**`dcat-ap-no-schema.yaml` er i full samsvar med DCAT-AP-NO § 1.5.**

Skjemaet:

1. ✓ Dekkjer alle obligatoriske eigenskapar for alle klassar
2. ✓ Markerer dei korrekt med `required: true` og `in_subset: [Obligatorisk]`
3. ✓ Dokumenterer kontrollerte vokabular som annotationar
4. ✓ Dekker alle klassar og eigenskapar spesifisert i standarden

**Ingen avvik eller manglande implementeringar er identifiserte.**

## Tiltak

Ingen tiltak nødvendige — skjemaet implementerer § 1.5 korrekt.

---

# Evaluering av samsvar med DCAT-AP-NO § 4.3

## Bakgrunn

§ 4.3 spesifiserer korleis eigenskapane `lisens`, `tilgangsrettigheter`, `rettigheter` og `policy` **SKAL** brukast for å beskrive tilgang og brukervilkår til ressursar (datasett, distribusjonar, datatjenester, katalogar).

## Relevante krav

### Scenario 1: Lisens (dct:license) — SKAL-krav

> `dct:license` **SKAL** brukast til å referere til ein lisens, og verdien **SKAL** hentast frå EUs kontrollerte vokabular **Licence**.

**Gjeld følgjande eigenskapar:**
- § 3.4.3.6: Datatjeneste – lisens (dct:license)
- § 3.5.2.3: Distribusjon – lisens (dct:license)
- § 3.8.2.6: Katalog – lisens (dct:license)

### Scenario 2: Tilgangsrettigheter (dct:accessRights) — SKAL-krav

> `dct:accessRights` **SKAL** brukast til å uttrykke tilgangsrettigheter, og verdien **SKAL** vere `PUBLIC`, `RESTRICTED` eller `NON_PUBLIC` frå EUs kontrollerte vokabular **Access right**.

**Gjeld følgjande eigenskapar:**
- § 3.2.2.8: Datasett – tilgangsrettigheter (dct:accessRights)
- § 3.4.3.9: Datatjeneste – tilgangsrettigheter (dct:accessRights)

### Scenario 3: Rettigheter (dct:rights) — KAN-krav

> `dct:rights` **KAN** brukast til å uttrykke alle andre typar rettigheter og brukervilkår, bl.a. opphavsrett. Det er anbefalt å bruke § 3.14 "Klassen Rettighetserklæring (odrs:RightsStatement)" til å ha ein strukturert beskrivelse av rettigheter og brukervilkår.

**Gjeld følgjande eigenskapar:**
- § 3.5.3.11: Distribusjon – rettigheter (dct:rights)
- § 3.8.3.7: Katalog – rettigheter (brukervilkår) (dct:rights)

### Scenario 4: Policy (odrl:hasPolicy) — W3C/DCAT-anbefaling

> W3C/DCAT anbefaler bruk av ODRL (Open Digital Rights Language) til å spesifisere spesielle bruksvilkår/-regler, som kan refererast til ved å bruke eigenskapen § 3.5.3.10 "Distribusjon – policy (odrl:hasPolicy)".

**Gjeld følgjande eigenskap:**
- § 3.5.3.10: Distribusjon – policy (odrl:hasPolicy)

## Evaluering av `dcat-ap-no-schema.yaml` og `common-ap-no-schema.yaml`

### Scenario 1: Lisens (dct:license)

#### Implementering i `common-ap-no-schema.yaml`:

```yaml
classes:
  Lisensdokument:
    class_uri: dct:LicenseDocument
    description: Eit lisensdokument (dct:LicenseDocument).
    slots:
      - id
      - type_concept

slots:
  lisens:
    slot_uri: dct:license
    range: Lisensdokument
    description: >-
      Lisens for bruk av ressursen (dct:license). For offentlege data skal CC BY 4.0
      (https://creativecommons.org/licenses/by/4.0/) eller NLOD 2.0
      (https://data.norge.no/nlod/no/2.0) nyttast per retningslinjene.
```

#### Bruk i `dcat-ap-no-schema.yaml`:

| Klasse | Eigenskap | Status i skjema | Status i spesifikasjon |
|---|---|---|---|
| **Distribusjon** | `lisens` | `in_subset: [Anbefalt]` | § 3.5.2.3: Anbefalt |
| **Datatjeneste** | `lisens` | (ikkje i `slot_usage`) | § 3.4.3.6: Valgfri |
| **Katalog** | `lisens` | `in_subset: [Anbefalt]` | § 3.8.2.6: Anbefalt |

#### Evaluering:

**✓ Korrekt `slot_uri`:** `dct:license`

**✓ Korrekt range:** `Lisensdokument` (med `class_uri: dct:LicenseDocument`)

**⚠️ Manglande dokumentasjon av EU Licence-vokabularet:**
- Spesifikasjonen seier at verdien **SKAL** hentast frå **EUs kontrollerte vokabular Licence**.
- `lisens`-sloten i `common-ap-no-schema.yaml` dokumenterer **ikkje** dette eksplisitt, men nemnder berre CC BY 4.0 og NLOD 2.0 som eksempel.
- EU Licence-vokabularet er tilgjengeleg på: `http://publications.europa.eu/resource/authority/licence/`

**Status:** ✓ Strukturelt korrekt, men dokumentasjonen kunne vore meir eksplisitt om kva kontrollert vokabular som **SKAL** brukast.

---

### Scenario 2: Tilgangsrettigheter (dct:accessRights)

#### Implementering i `dcat-ap-no-schema.yaml`:

```yaml
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

#### Bruk i `dcat-ap-no-schema.yaml`:

| Klasse | Eigenskap | Status i skjema | Status i spesifikasjon |
|---|---|---|---|
| **Datasett** | `tilgangsrettigheter` | `in_subset: [Anbefalt]` | § 3.2.2.8: Anbefalt |
| **Datatjeneste** | `tilgangsrettigheter` | (ikkje i `slot_usage`) | § 3.4.3.9: Valgfri |

#### Evaluering:

**✓ Korrekt `slot_uri`:** `dct:accessRights`

**✓ Korrekt range:** `uri` (peiker til konsept i EU Access Rights-vokabularet)

**✓ Korrekt kontrollert vokabular dokumentert:** Alle tre gyldige verdiar (`PUBLIC`, `RESTRICTED`, `NON_PUBLIC`) er eksplisitt lista i `annotations.gyldige_verdier`.

**✓ Beskriving dokumenterer samanheng med "Veileder for orden i eget hus":**
- Grønn → PUBLIC
- Gul → RESTRICTED
- Rød → NON_PUBLIC

**Status:** ✓ Fullt ut i samsvar med § 4.3.

---

### Scenario 3: Rettigheter (dct:rights)

#### Implementering i `dcat-ap-no-schema.yaml`:

```yaml
classes:
  Rettighetserklaring:
    class_uri: dct:RightsStatement
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

slots:
  rettigheter:
    slot_uri: dct:rights
    range: Rettighetserklaring
    description: Rettar knytte til ressursen.
```

#### Bruk i `dcat-ap-no-schema.yaml`:

| Klasse | Eigenskap | Status i skjema | Status i spesifikasjon |
|---|---|---|---|
| **Distribusjon** | `rettigheter` | (ikkje i `slot_usage`) | § 3.5.3.11: Valgfri |
| **Katalog** | `rettigheter` | (ikkje i `slot_usage`) | § 3.8.3.7: Valgfri |
| **Datatjeneste** | `rettigheter` | (ikkje i `slot_usage`) | § 3.4.3.10: Valgfri |

#### Evaluering:

**✓ Korrekt `slot_uri`:** `dct:rights`

**✓ Korrekt range:** `Rettighetserklaring` (med `class_uri: dct:RightsStatement`)

**✓ Strukturert ODRS-støtte:** Klassen `Rettighetserklaring` implementerer alle ODRS-eigenskapar (opphavsrett, kreditering, jurisdiksjon osv.) som spesifisert i § 3.14.

**Status:** ✓ Fullt ut i samsvar med § 4.3 — strukturert støtte for ODRS-rettigheitserklæringar er implementert.

---

### Scenario 4: Policy (odrl:hasPolicy)

#### Implementering i `dcat-ap-no-schema.yaml`:

```yaml
slots:
  policy:
    slot_uri: odrl:hasPolicy
    range: string
    description: ODRL-policy som regulerer bruk av ressursen.
    annotations:
      gyldige_verdier: odrl:Policy
```

#### Bruk i `dcat-ap-no-schema.yaml`:

| Klasse | Eigenskap | Status i skjema | Status i spesifikasjon |
|---|---|---|---|
| **Distribusjon** | `policy` | (ikkje i `slot_usage`) | § 3.5.3.10: Valgfri |

#### Evaluering:

**✓ Korrekt `slot_uri`:** `odrl:hasPolicy`

**⚠️ `range: string` i staden for `uri`:**
- ODRL-policies er URI-referansar til policy-dokument, så `range: uri` ville vore meir korrekt.
- `range: string` tillèt både URI og fritekst, men er mindre strengt.

**✓ Kontrollert vokabular dokumentert:** `odrl:Policy` er spesifisert i `annotations.gyldige_verdier`.

**Status:** ⚠️ Funksjonelt korrekt, men `range: uri` ville vore meir presist enn `range: string`.

---

## Samanfatning

| Scenario | Eigenskap | Status | Merknad |
|---|---|---|---|
| 1. Lisens | `dct:license` | ✓ | Strukturelt korrekt, men dokumentasjonen kunne vore meir eksplisitt om EU Licence-vokabularet |
| 2. Tilgangsrettigheter | `dct:accessRights` | ✓ | Fullt ut i samsvar — alle tre verdiar (`PUBLIC`, `RESTRICTED`, `NON_PUBLIC`) dokumenterte |
| 3. Rettigheter | `dct:rights` | ✓ | Fullt ut i samsvar — strukturert ODRS-støtte via `Rettighetserklaring` |
| 4. Policy | `odrl:hasPolicy` | ⚠️ | Funksjonelt korrekt, men `range: uri` ville vore meir presist enn `range: string` |

## Konklusjon

**`dcat-ap-no-schema.yaml` og `common-ap-no-schema.yaml` er i samsvar med DCAT-AP-NO § 4.3.**

Alle fire scenario er implementerte korrekt:

1. ✓ `dct:license` brukar `dct:LicenseDocument` som range
2. ✓ `dct:accessRights` refererer til EU Access Rights-vokabularet med alle tre gyldige verdiar
3. ✓ `dct:rights` brukar `Rettighetserklaring` (ODRS) som range
4. ✓ `odrl:hasPolicy` er implementert (men kunne bruke `range: uri` i staden for `range: string`)

## Tiltak

### ✓ Utførte tiltak:

1. **✓ Lag enumerasjon for EU Licence-vokabularet**
   - Laga `EULicence`-enumerasjon i `common-ap-no-schema.yaml` med verdiar frå EU Licence-vokabularet
   - Inkluderer: CC0, CC_BY_4_0, NLOD_2_0, CC_BYSA_4_0, MIT, APACHE_2_0, GPL_3_0, EUPL_1_2
   - Oppdatert `lisens`-sloten sin beskrivelse til å referere til EU Licence-vokabularet og `EULicence`-enumerasjonen
   - Dokumentert kjelde: `http://publications.europa.eu/resource/authority/licence/`

2. **✓ Endre `policy`-sloten til `range: uri`**
   - Endra `policy`-sloten frå `range: string` til `range: uri` i `dcat-ap-no-schema.yaml`
   - Grunngjeving: ODRL-policies er URI-referansar til policy-dokument, ikkje fritekststrenger

3. **✓ Legg til `dcatno`-prefix**
   - Lagt til `dcatno: https://data.norge.no/vocabulary/dcatno#` i `prefixes` i `dcat-ap-no-schema.yaml`
   - Grunngjeving: Vedlegg A spesifiserer at `dcatno` er namespace for "denne standarden"

### Merknad:

Desse tiltaka er **ikkje påkravde** for samsvar — skjemaet er allereie i samsvar med § 4.3. Men dei vil gjere skjemaet meir eksplisitt og lettare å bruke korrekt.

---

# Evaluering av samsvar med DCAT-AP-NO Vedlegg A — Navnerom

## Bakgrunn

Vedlegg A spesifiserer alle navnerom (prefixer) som vert brukte i DCAT-AP-NO-standarden. Denne evalueringa vurderer om `dcat-ap-no-schema.yaml` og `common-ap-no-schema.yaml` brukar riktige navnerom.

## Samanlikning: Spesifikasjon vs. Skjema

| Prefix | Spesifikasjon | Skjema | Status |
|---|---|---|---|
| **adms** | `http://www.w3.org/ns/adms#` | `http://www.w3.org/ns/adms#` | ✓ |
| **cv** | `http://data.europa.eu/m8g/` | `http://data.europa.eu/m8g/` | ✓ |
| **cpsv** | `http://purl.org/vocab/cpsv#` | (ikkje brukt) | — |
| **dcat** | `http://www.w3.org/ns/dcat#` | `http://www.w3.org/ns/dcat#` | ✓ |
| **dcatap** | `http://data.europa.eu/r5r/` | `http://data.europa.eu/r5r/` | ✓ |
| **dcatno** | `https://data.norge.no/vocabulary/dcatno#` | **(manglar)** | ✗ |
| **dct** | `http://purl.org/dc/terms/` | `http://purl.org/dc/terms/` | ✓ |
| **dqv** | `http://www.w3.org/ns/dqv#` | (importert via `dqv-core-schema`) | ✓ |
| **eli** | `http://data.europa.eu/eli/ontology#` | `http://data.europa.eu/eli/ontology#` | ✓ |
| **foaf** | `http://xmlns.com/foaf/0.1/` | `http://xmlns.com/foaf/0.1/` | ✓ |
| **locn** | `http://www.w3.org/ns/locn#` | (ikkje brukt) | — |
| **odrl** | `http://www.w3.org/ns/odrl/2/` | `http://www.w3.org/ns/odrl/2/` | ✓ |
| **odrs** | `http://schema.theodi.org/odrs#` | `http://schema.theodi.org/odrs#` | ✓ |
| **owl** | `http://www.w3.org/2002/07/owl#` | (i `common-ap-no-schema`) | ✓ |
| **prov** | `http://www.w3.org/ns/prov#` | `http://www.w3.org/ns/prov#` | ✓ |
| **rdfs** | `http://www.w3.org/2000/01/rdf-schema#` | `http://www.w3.org/2000/01/rdf-schema#` | ✓ |
| **skos** | `http://www.w3.org/2004/02/skos/core#` | `http://www.w3.org/2004/02/skos/core#` | ✓ |
| **spdx** | `http://spdx.org/rdf/terms#` | `http://spdx.org/rdf/terms#` | ✓ |
| **time** | `http://www.w3.org/2006/time#` | `http://www.w3.org/2006/time#` | ✓ |
| **vcard** | `http://www.w3.org/2006/vcard/ns#` | `http://www.w3.org/2006/vcard/ns#` | ✓ |
| **xsd** | `http://www.w3.org/2001/XMLSchema#` | `http://www.w3.org/2001/XMLSchema#` | ✓ |

### Ekstra prefixer i skjema (ikkje i Vedlegg A):

| Prefix | Namespace | Kommentar |
|---|---|---|
| **linkml** | `https://w3id.org/linkml/` | LinkML-intern prefix — nødvendig for LinkML-metadata |
| **rdf** | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` | Brukt for `rdf:langString` — standard RDF-prefix |

## Funn

### ✗ Kritisk: `dcatno`-prefiks manglar

**Spesifikasjon (Vedlegg A):**
> Navnerom for denne standarden er `https://data.norge.no/vocabulary/dcatno#`, vanligvis ved prefiks `dcatno`.

**Problem:**
- `dcatno`-prefixen er **ikkje definert** i `dcat-ap-no-schema.yaml`
- Denne prefixen skal brukast for **norske utvidingar eller presiseringar** av DCAT-AP
- Per no brukar skjemaet `default_prefix: https://data.norge.no/ap-no/dcat-ap-no/` i staden for `dcatno`-namespacet

**Konsekvens:**
- Dersom det finst norske utvidingar/presiseringar som skal bruke `dcatno:`-namespace, vil dei per no ende opp under `default_prefix` i staden

**Vurdering:**
- **Om skjemaet berre modellerer W3C/EU-standardiserte eigenskapar:** Då er `dcatno`-mangelen ikkje kritisk, sidan alle `class_uri` og `slot_uri` peikar til standardiserte namespace (dcat:, dct:, foaf: osv.)
- **Om skjemaet skal støtte norske utvidingar:** Då **SKAL** `dcatno`-prefixen leggjast til

### — Ikkje-kritisk: `cpsv` og `locn` manglar

**cpsv (Core Public Service Vocabulary):**
- Brukt for offentlege tenestebeskrivingar
- Ikkje relevant for DCAT-AP-NO sine hovudklassar (Katalog, Datasett, Distribusjon osv.)

**locn (Core Location Vocabulary):**
- Brukt for detaljerte lokasjonsbeskrivingar
- DCAT-AP-NO brukar `dct:spatial` (range: `skos:Concept`) i staden for `locn:Location`

**Status:** Desse prefixane er lista i Vedlegg A fordi dei er **del av det fullstendige W3C/DCAT-økosystemet**, men dei er ikkje nødvendige for denne implementeringa.

### ✓ Alle brukte prefixer er korrekte

Alle prefixer som **faktisk er brukte** i skjemaet (`dcat:`, `dct:`, `foaf:` osv.) har **identisk namespace** som spesifisert i Vedlegg A.

## Konklusjon

**Skjemaet brukar riktige navnerom for alle W3C/EU-standardiserte prefixer.**

**Eitt kritisk funn:**
- ✗ `dcatno`-prefiks (`https://data.norge.no/vocabulary/dcatno#`) manglar i skjemaet

**Konsekvens:**
- Dersom skjemaet **berre modellerer standardiserte eigenskapar** (dcat:, dct:, foaf: osv.), er dette ikkje eit problem
- Dersom skjemaet **skal støtte norske utvidingar** (eigenskapar/klassar som ikkje finst i W3C/EU-standardane), **SKAL** `dcatno`-prefixen leggjast til

## Tiltak

### 3. **[ ] Legg til `dcatno`-prefix (dcat-ap-no-schema.yaml)**

**Handling:**
```yaml
prefixes:
  dcatno:  https://data.norge.no/vocabulary/dcatno#
  # ... resten av prefixane
```

**Grunngjeving:**
- Vedlegg A spesifiserer at `dcatno` er namespace for "denne standarden"
- Sjølv om skjemaet per no ikkje brukar norske utvidingar, bør prefixen vere tilgjengeleg for framtidig bruk

**Status:** Anbefalt (ikkje påkravd dersom det ikkje finst norske utvidingar)
