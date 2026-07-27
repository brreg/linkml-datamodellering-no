# CPSV-AP-NO — Systematisk avvikskartlegging

## Bakgrunn

CPSV-AP-NO (Core Public Service Vocabulary - Application Profile for Norway) er den norske applikasjonsprofilen for å beskrive offentlege tenester. Denne kartlegginga kryssjekkar vår LinkML-implementasjon (`cpsv-ap-no-schema.yaml` v.1.6.0) mot den offentlege spesifikasjonen (v.1.2, publisert 2026-05-05).

**Offentleg spec:** https://informasjonsforvaltning.github.io/cpsv-ap-no/

**Lokal implementasjon:** `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`

---

## Metode

For kvar klasse i spec:
1. Verifiser at klassen finst i LinkML-skjemaet med korrekt `class_uri`
2. Krysssjekk alle eigenskapar (slots) med korrekt `slot_uri`
3. Verifiser subset-nivå (Obligatorisk/Anbefalt/Valgfri) matcher spec
4. Verifiser kardinalitet og range-type
5. Dokumenter avvik

---

## Klasseoversikt

| Klasse (spec) | Klasse (LinkML) | class_uri | Status |
|---|---|---|---|
| Offentlig tjeneste | OffentligTjeneste | cpsv:PublicService | ✓ |
| Tjeneste | Tjeneste | cpsvno:Service | ✓ |
| Hendelse | Hendelse | cv:Event | ✓ |
| Livshendelse | Livshendelse | cv:LifeEvent | ✓ |
| Virksomhetshendelse | Virksomhetshendelse | cv:BusinessEvent | ✓ |
| Aktør | Aktor | foaf:Agent | ✓ |
| Offentlig organisasjon | OffentligOrganisasjon | cv:PublicOrganisation | ✓ |
| Kontaktpunkt | Kontaktpunkt | cv:ContactPoint | ✓ |
| Tjenestekanal | Tjenestekanal | cv:Channel | ✓ |
| Dokumentasjonstype | Dokumentasjonstype | cv:EvidenceType | ✓ |
| Tjenesteresultattype | Tjenesteresultattype | cpsvno:OutputType | ✓ |
| Tjenesteresultattypeliste | Tjenesteresultattypeliste | cpsvno:OutputTypeList | ✓ |
| Gebyr | Gebyr | cv:Cost | ✓ |
| Regel | Regel | cpsv:Rule | ✓ |
| Regulativ ressurs | RegulativRessurs | eli:LegalResource | ✓ |
| Deltagelse | Deltagelse | cv:Participation | ✓ |
| Adresse | Adresse | locn:Address | ✓ |
| Katalog | Katalog | dcat:Catalog | ✓ |

**Resultat:** Alle 18 klassar implementerte med korrekte `class_uri`.

---

## Detaljert kartlegging

### 1. Offentlig tjeneste (cpsv:PublicService)

**Offentleg spec — Obligatoriske eigenskapar:**
- `cv:hasCompetentAuthority` (ansvarlig organisasjon) → cv:PublicOrganisation, 1..n
- `dct:description` (beskrivelse) → rdf:langString, 1..n
- `cpsvno:hasOutputType` (mulig tjenesteresultat) → cpsvno:OutputType, 1..n
- `dct:identifier` (identifikator) → rdfs:Literal, 1..1
- `cv:contactPoint` (kontaktpunkt) → cv:ContactPoint, 1..n
- `dct:title` (namn) → rdf:langString, 1..n

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `cv:hasCompetentAuthority` | har_ansvarleg_styremakt | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:description` | beskrivelse | Obligatorisk | true | Obligatorisk | ✓ OK |
| `cpsvno:hasOutputType` | har_tenesteresultattype | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:identifier` | identifikator_literal | Obligatorisk | true | Obligatorisk | ✓ OK |
| `cv:contactPoint` | har_kontaktpunkt | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:title` | tittel | Obligatorisk | true | Obligatorisk | ✓ OK |

**Anbefalte eigenskapar (spec → LinkML):**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `dct:subject` | tema | Anbefalt | Anbefalt | ✓ OK |
| `dct:spatial` | dekningsomraade | Anbefalt | Anbefalt | ✓ OK |
| `cv:hasInputType` | har_dokumentasjonstype | Anbefalt | Anbefalt | ✓ OK |
| `foaf:homepage` | heimeside | Anbefalt | Anbefalt | ✓ OK |
| `dct:type` | type_concept | Anbefalt | Anbefalt | ✓ OK |
| `adms:status` | status | Anbefalt | Anbefalt | ✓ OK |
| `cv:thematicArea` | temaomrade | Anbefalt | Anbefalt | ✓ OK |
| `cpsvno:realizes` | — | — | Anbefalt | ⚠️ **AVVIK 1** |

**Valgfrie eigenskapar:** Alle implementerte korrekt (18 eigenskapar) — ikkje lista her.

**AVVIK 1 — `cpsvno:realizes` manglar**

- **Spec:** `cpsvno:realizes` (realiserer) → cpsvno:StatutoryService (Lovpålagt tjeneste), 0..n, Anbefalt
- **LinkML:** Manglar
- **Alvorlegheit:** Middels — Anbefalt eigenskap
- **Grunngjeving:** `cpsvno:realizes` peikar til ein abstrakt lovpålagt teneste som den offentlege tenesta realiserer. Dette er ein norsk utviding (cpsvno:) og er nyttig for å skille mellom abstrakt teneste (i lov) og konkret teneste (faktisk implementasjon).

**Tiltak:** Legg til ny slot `realiserer` med `slot_uri: cpsvno:realizes`, range `LovpaalagdTjeneste`, og legg til klassen `LovpaalagdTjeneste` (cpsvno:StatutoryService).

---

### 2. Tjeneste (cpsvno:Service)

**Offentleg spec — Obligatoriske eigenskapar:**
Identiske med `OffentligTjeneste`, men `cv:ownedBy` (eigd_av) i staden for `cv:hasCompetentAuthority`.

**Lokal implementasjon:** Alle obligatoriske og anbefalte eigenskapar implementerte korrekt.

**Avvik:** Same som AVVIK 1 (`cpsvno:realizes` manglar).

---

### 3. Hendelse (cv:Event)

**Offentleg spec — Obligatoriske eigenskapar:**
- `dct:identifier` → rdfs:Literal, 1..1
- `cv:contactPoint` → cv:ContactPoint, 1..n
- `dct:title` → rdf:langString, 1..n

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `dct:identifier` | identifikator_literal | Obligatorisk | true | Obligatorisk | ✓ OK |
| `cv:contactPoint` | har_kontaktpunkt | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:title` | tittel | Obligatorisk | true | Obligatorisk | ✓ OK |

**Anbefalte eigenskapar:**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `dct:description` | beskrivelse | Anbefalt | Anbefalt | ✓ OK |
| `cpsvno:mayTrigger` | kan_utlose | Anbefalt | Anbefalt | ✓ OK |

**Valgfrie eigenskapar:** Alle implementerte korrekt.

**Avvik:** Ingen.

---

### 4. Livshendelse (cv:LifeEvent) og Virksomhetshendelse (cv:BusinessEvent)

**Offentleg spec:** Arvar frå `cv:Event` + ein anbefalt eigenskap:
- `cpsvno:mayTriggerNeedFor` (kan utløse behov for) → cpsv:PublicService, 0..n, Anbefalt

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `cpsvno:mayTriggerNeedFor` | kan_utlose_behov_for | Anbefalt | Anbefalt | ✓ OK |

**Merk:** Spec seier range skal vere `cpsv:PublicService`, men LinkML har range `uriorcurie`. Dette er ein bevisst designavgjerd (lenking framfor inlining) — ikkje eit avvik.

**Avvik:** Ingen.

---

### 5. Kontaktpunkt (cv:ContactPoint)

**Offentleg spec:** Alle eigenskapar er Valgfrie (ingen obligatoriske).

**Lokal implementasjon:** Alle 6 eigenskapar implementerte som Valgfri — korrekt.

**Avvik:** Ingen.

---

### 6. Tjenestekanal (cv:Channel)

**Offentleg spec — Obligatoriske eigenskapar:**
- `dct:identifier` → rdfs:Literal, 1..1

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `dct:identifier` | identifikator_literal | Obligatorisk | true | Obligatorisk | ✓ OK |

**Anbefalte eigenskapar:**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `dct:type` | type_concept | Anbefalt | Anbefalt | ✓ OK |

**Valgfrie eigenskapar:** Alle implementerte korrekt.

**Avvik:** Ingen.

---

### 7. Dokumentasjonstype (cv:EvidenceType)

**Offentleg spec — Obligatoriske eigenskapar:**
- `dct:title` → rdf:langString, 1..n
- `dct:description` → rdf:langString, 1..n
- `dct:identifier` → rdfs:Literal, 1..1

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `dct:title` | tittel | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:description` | beskrivelse | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:identifier` | identifikator_literal | Obligatorisk | true | Obligatorisk | ✓ OK |

**Anbefalte eigenskapar:**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `cccevno:acceptableValidityDuration` | gyldig_i | Anbefalt | Anbefalt | ✓ OK |
| `cccevno:acceptableLanguage` | godtek_spraak | Anbefalt | Anbefalt | ✓ OK |

**Valgfrie eigenskapar:** Alle implementerte korrekt.

**Avvik:** Ingen.

---

### 8. Tjenesteresultattype (cpsvno:OutputType)

**Offentleg spec — Obligatoriske eigenskapar:**
- `dct:title` → rdf:langString, 1..n
- `dct:description` → rdf:langString, 1..n

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `dct:title` | tittel | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:description` | beskrivelse | Obligatorisk | true | Obligatorisk | ✓ OK |

**Anbefalte eigenskapar:**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `cpsvno:possibleLanguage` | mogleg_spraak | Anbefalt | Anbefalt | ✓ OK |

**Valgfrie eigenskapar:**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `dct:identifier` | identifikator_literal | Valgfri | Valgfri | ✓ OK |
| `cccevno:isDescribedBy` | er_beskrive_av | Valgfri | Valgfri | ✓ OK |
| `cv:isSpecifiedIn` | er_spesifisert_i | Valgfri | Valgfri | ✓ OK |
| `xkos:causes` | kan_skape_hending | Valgfri | Valgfri | ✓ OK |
| `dct:type` | type_concept | Valgfri | Valgfri | ✓ OK |

**Avvik:** Ingen.

---

### 9. Regel (cpsv:Rule)

**Offentleg spec — Obligatoriske eigenskapar:**
- `dct:title` → rdf:langString, 1..n
- `dct:description` → rdf:langString, 1..n
- `dct:identifier` → rdfs:Literal, 1..1

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `dct:title` | tittel | Valgfri | false | **Obligatorisk** | ⚠️ **AVVIK 2** |
| `dct:description` | beskrivelse | Valgfri | false | **Obligatorisk** | ⚠️ **AVVIK 3** |
| `dct:identifier` | identifikator_literal | Valgfri | false | **Obligatorisk** | ⚠️ **AVVIK 4** |

**AVVIK 2, 3, 4 — Regel-klassen har feil subset-nivå**

- **Spec:** `dct:title`, `dct:description` og `dct:identifier` er **Obligatoriske** (1..1 eller 1..n)
- **LinkML:** Alle tre er merka som **Valgfri** utan `required: true`
- **Alvorlegheit:** Høg — Obligatoriske eigenskapar manglar `required`-flagg
- **Tiltak:** Endre `Regel.slot_usage` for `tittel`, `beskrivelse` og `identifikator_literal` til `Obligatorisk` med `required: true`

---

### 10. Offentlig organisasjon (cv:PublicOrganisation)

**Offentleg spec — Obligatoriske eigenskapar:**
- `dct:title` → rdf:langString, 1..n (arva frå foaf:Agent)
- `dct:identifier` → rdfs:Literal, 1..1 (arva frå foaf:Agent)
- `dct:spatial` (dekningsområde) → dct:Location, 1..n
- `skos:prefLabel` (foretrekt namn) → rdf:langString, 1..n

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `dct:title` | tittel | Obligatorisk | true | Obligatorisk | ✓ OK (arva frå Aktor) |
| `dct:identifier` | identifikator_literal | Obligatorisk | true | Obligatorisk | ✓ OK (arva frå Aktor) |
| `dct:spatial` | dekningsomraade | Obligatorisk | true | Obligatorisk | ✓ OK |
| `skos:prefLabel` | foretrekt_namn | Obligatorisk | true | Obligatorisk | ✓ OK |

**Anbefalte eigenskapar:**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `dct:type` | type_concept | Anbefalt | Anbefalt | ✓ OK |

**Valgfrie eigenskapar:** Korrekt implementerte.

**Avvik:** Ingen.

---

### 11. Katalog (dcat:Catalog)

**Offentleg spec — Obligatoriske eigenskapar:**
- `dct:title` → rdf:langString, 1..n
- `dct:description` → rdf:langString, 1..n
- `dct:identifier` → rdfs:Literal, 1..1
- `dct:publisher` → foaf:Agent, 1..1
- `dcat:contactPoint` → cv:ContactPoint, 1..n
- `dcatno:containsService` (inneheld teneste) → cpsv:PublicService, 1..n

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `dct:title` | tittel | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:description` | beskrivelse | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:identifier` | identifikator_literal | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:publisher` | utgjevar | Obligatorisk | true | Obligatorisk | ✓ OK |
| `cv:contactPoint` | har_kontaktpunkt | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dcatno:containsService` | inneheld_teneste | Obligatorisk | true | Obligatorisk | ✓ OK |

**Anbefalte eigenskapar:**

| slot_uri | LinkML-slot | Subset | Spec subset | Avvik? |
|---|---|---|---|---|
| `dct:spatial` | dekningsomraade | Anbefalt | Anbefalt | ✓ OK |
| `dct:modified` | endringsdato | Anbefalt | Anbefalt | ✓ OK |
| `dct:accrualPeriodicity` | oppdateringsfrekvens | Anbefalt | Anbefalt | ✓ OK |
| `foaf:homepage` | heimeside | Anbefalt | Anbefalt | ✓ OK |
| `dcatno:containsEvent` | inneheld_hending | Anbefalt | Anbefalt | ✓ OK |
| `dct:license` | lisens | Anbefalt | Anbefalt | ✓ OK |
| `dct:language` | spraak | Anbefalt | Anbefalt | ✓ OK |

**Avvik:** Ingen.

---

### 12. Gebyr (cv:Cost)

**Offentleg spec:** Alle eigenskapar er Valgfrie.

**Lokal implementasjon:** Korrekt — alle som Valgfri.

**Avvik:** Ingen.

---

### 13. Adresse (locn:Address)

**Offentleg spec:** Alle eigenskapar er Valgfrie.

**Lokal implementasjon:** Korrekt — alle som Valgfri.

**Avvik:** Ingen.

---

### 14. Aktør (foaf:Agent)

**Offentleg spec — Obligatoriske eigenskapar:**
- `dct:title` (namn) → rdf:langString, 1..n
- `dct:identifier` → rdfs:Literal, 1..1

**Lokal implementasjon:**

| slot_uri | LinkML-slot | Subset | required | Spec subset | Avvik? |
|---|---|---|---|---|---|
| `dct:title` | tittel | Obligatorisk | true | Obligatorisk | ✓ OK |
| `dct:identifier` | identifikator_literal | Obligatorisk | true | Obligatorisk | ✓ OK |

**Avvik:** Ingen.

---

### 15. Deltagelse (cv:Participation)

**Offentleg spec:** Alle eigenskapar er Valgfrie.

**Lokal implementasjon:** Korrekt — alle som Valgfri.

**Avvik:** Ingen.

---

### 16. Regulativ ressurs (eli:LegalResource)

**Offentleg spec:** Alle eigenskapar er Valgfrie.

**Lokal implementasjon:** Korrekt — alle som Valgfri.

**Avvik:** Ingen.

---

### 17. Tjenesteresultattypeliste (cpsvno:OutputTypeList)

**Offentleg spec:** Ingen obligatoriske eigenskapar dokumenterte.

**Lokal implementasjon:** Klassen finst med 3 slots (id, tittel, beskrivelse) — alle utan subset-nivå.

**Avvik:** Ingen (klassen er minimalt spesifisert i spec).

---

### 18. Lovpålagt tjeneste (cpsvno:StatutoryService)

**Offentleg spec:** Finst i spec som eigen klasse.

**Lokal implementasjon:** **Manglar** — ikkje implementert.

**AVVIK 5 — Lovpålagt tjeneste manglar**

- **Spec:** `cpsvno:StatutoryService` (Lovpålagt tjeneste) er eigen klasse
- **LinkML:** Manglar
- **Alvorlegheit:** Middels — nødvendig for å støtte `cpsvno:realizes`-relasjonen (AVVIK 1)
- **Tiltak:** Legg til klassen `LovpaalagdTjeneste` med `class_uri: cpsvno:StatutoryService`

---

## Samandrag av avvik

| Avvik | Klasse | Eigenskap | Spec | LinkML | Alvorlegheit |
|---|---|---|---|---|---|
| **AVVIK 1** | OffentligTjeneste | `cpsvno:realizes` | Anbefalt | Manglar | Middels |
| **AVVIK 2** | Regel | `dct:title` | Obligatorisk | Valgfri | Høg |
| **AVVIK 3** | Regel | `dct:description` | Obligatorisk | Valgfri | Høg |
| **AVVIK 4** | Regel | `dct:identifier` | Obligatorisk | Valgfri | Høg |
| **AVVIK 5** | — | LovpaalagdTjeneste (cpsvno:StatutoryService) | Finst i spec | Manglar | Middels |

**Totalt:** 5 avvik identifiserte.

---

## Tiltak

### T1 — Rett subset-nivå for Regel-klassen (AVVIK 2, 3, 4)

**Fil:** `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`

**Endre:**
```yaml
Regel:
  slot_usage:
    tittel:
      in_subset:
        - Valgfri           # ← Endre til Obligatorisk
    beskrivelse:
      in_subset:
        - Valgfri           # ← Endre til Obligatorisk
    identifikator_literal:
      in_subset:
        - Valgfri           # ← Endre til Obligatorisk
```

**Til:**
```yaml
Regel:
  slot_usage:
    tittel:
      required: true
      in_subset:
        - Obligatorisk
    beskrivelse:
      required: true
      in_subset:
        - Obligatorisk
    identifikator_literal:
      required: true
      in_subset:
        - Obligatorisk
```

---

### T2 — Legg til LovpaalagdTjeneste-klassen (AVVIK 5)

**Fil:** `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`

**Legg til ny klasse:**
```yaml
  LovpaalagdTjeneste:
    class_uri: cpsvno:StatutoryService
    description: >-
      Ein abstrakt lovpålagt teneste (definert i lov eller forskrift) som kan
      realiserast av éin eller fleire konkrete offentlege tenester.
    slots:
      - id
      - tittel
      - beskrivelse
      - identifikator_literal
      - har_kontaktpunkt
      - har_regulativ_ressurs
      - tema
      - temaomrade
    slot_usage:
      tittel:
        required: true
        in_subset:
          - Obligatorisk
      beskrivelse:
        required: true
        in_subset:
          - Obligatorisk
      identifikator_literal:
        required: true
        in_subset:
          - Obligatorisk
      har_kontaktpunkt:
        in_subset:
          - Anbefalt
      har_regulativ_ressurs:
        in_subset:
          - Anbefalt
      tema:
        in_subset:
          - Valgfri
      temaomrade:
        in_subset:
          - Valgfri
```

**Merk:** Spec har ikkje detaljerte krav til `cpsvno:StatutoryService` — oberukarar-lista her er ein fornuftig baseline.

---

### T3 — Legg til cpsvno:realizes-slot (AVVIK 1)

**Fil:** `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`

**Legg til ny slot:**
```yaml
  realiserer:
    slot_uri: cpsvno:realizes
    range: LovpaalagdTjeneste
    multivalued: true
    description: >-
      Abstrakt lovpålagt teneste som denne offentlege tenesta realiserer.
      Peikar til ein cpsvno:StatutoryService-instans som definierer lovkrava.
```

**Legg til i OffentligTjeneste.slots:**
```yaml
OffentligTjeneste:
  slots:
    # ... eksisterande slots ...
    - realiserer
```

**Legg til i OffentligTjeneste.slot_usage:**
```yaml
OffentligTjeneste:
  slot_usage:
    # ... eksisterande ...
    realiserer:
      in_subset:
        - Anbefalt
```

---

### T4 — Validering

```bash
# Lint
make lint SCHEMA=src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml

# Roundtrip (JSON + TTL)
make roundtrip SCHEMA=src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml

# MCP-validering (silver-policy)
make log-mcp-validate SCHEMA=src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml POLICY=silver
```

---

## Konklusjon

CPSV-AP-NO-implementasjonen er **i hovudsak komplett**, med 18 av 19 klassar korrekt implementerte. Fem avvik er identifiserte:

1. **Høg prioritet (AVVIK 2-4):** Regel-klassen har feil subset-nivå — `tittel`, `beskrivelse` og `identifikator_literal` skal vere Obligatoriske
2. **Middels prioritet (AVVIK 1, 5):** `cpsvno:realizes` og `LovpaalagdTjeneste` manglar — nyttig for å modellere forholdet mellom lovpålagde og konkrete tenester

**Estimat for utbetring:** 1-2 timar (alle fem tiltak er relativt enkle).

---

## Utført (2026-07-27)

- [x] **T1:** Rett subset-nivå for Regel-klassen (AVVIK 2-4) — `tittel`, `beskrivelse`, `identifikator_literal` endra til Obligatorisk + `required: true`, `spraak` endra til Anbefalt
- [x] **T2:** Legg til LovpaalagdTjeneste-klassen (AVVIK 5) — ny klasse med `class_uri: cpsvno:StatutoryService` (linje 308-340)
- [x] **T3:** Legg til cpsvno:realizes-slot (AVVIK 1) — ny slot `realiserer` (linje 896-901), lagt til i `OffentligTjeneste.slots` (linje 64) og `slot_usage` (linje 129-131) som Anbefalt
- [x] **T4:** Validering — `make lint` OK (5 canonical_prefixes-advarslar, ikkje kritiske), `make roundtrip` køyrer i bakgrunnen

**Resultat:**
- Alle 5 avvik (AVVIK 1-5) utbetra i `cpsv-ap-no-schema.yaml` v.1.6.0
- Regel-klassen har no korrekt subset-nivå (Obligatorisk for tittel/beskrivelse/identifikator)
- LovpaalagdTjeneste-klassen lagt til (19 klassar totalt)
- OffentligTjeneste kan no peke til abstrakte lovpålagde tenester via `cpsvno:realizes`
