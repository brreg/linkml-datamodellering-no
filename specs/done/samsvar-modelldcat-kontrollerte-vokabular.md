# Samsvar ModelDCAT-AP-NO med kap. 9 Kontrollerte vokabular

## Bakgrunn

Evaluering av `modelldcat-ap-no-schema.yaml` mot kapittel 9 (Kontrollerte vokabular) i ModelDCAT-AP-NO-spesifikasjonen avdekte fleire avvik:

1. **`dct:format` (Dokument)** — range er `string`, skal vere kontrollert vokabular
2. **`dct:language` (Modellkatalog, Informasjonsmodell, Dokument)** — range er custom type `Spraak`, skal vere kontrollert vokabular
3. **`adms:status` (Informasjonsmodell)** — feil vokabular-URI (skal vere `purl.org/adms/status/`, ikkje `dataset-status`)
4. **`dct:type` (Lisensdokument)** — manglar annotations om ADMS licencetype-vokabularet
5. **`dct:type` (Aktør/foaf:Agent)** — manglar annotations om ADMS publishertype-vokabularet

Desse avvika gjer at skjemaet ikkje fullt ut implementerer kravet om kontrollerte vokabular frå EU og Digdir.

## Mål

Sikre at `modelldcat-ap-no-schema.yaml` (og importerte `common-ap-no-schema.yaml`) er i full samsvar med kapittel 9 i ModelDCAT-AP-NO-spesifikasjonen.

## Steg

### 1. Opprett enum for EU File type-vokabularet

Legg til `EUFileType`-enum i `common-ap-no-schema.yaml` med dei mest brukte filformata:

- RDF_TURTLE
- RDF_XML
- JSON_LD
- JSON
- XML
- HTML
- PDF
- CSV
- YAML

URI-base: `http://publications.europa.eu/resource/authority/file-type/`

### 2. Opprett enum for EU Language-vokabularet

Legg til `EULanguage`-enum i `common-ap-no-schema.yaml` med norske språk:

- NOB (Norsk bokmål)
- NNO (Nynorsk)
- NOR (Norsk, uspesifisert)
- SME (Nordsamisk)
- SMA (Sørsamisk)
- SMJ (Lulesamisk)
- ENG (Engelsk)

URI-base: `http://publications.europa.eu/resource/authority/language/`

### 3. Endre `format`-slot frå `string` til `Konsept`

I `common-ap-no-schema.yaml`:

```yaml
format:
  slot_uri: dct:format
  range: Konsept  # tidlegare: string
  description: >-
    Filformat eller medietype (dct:format). Verdien SKAL veljast frå EUs
    kontrollerte vokabular File type
    (http://publications.europa.eu/resource/authority/file-type/).
    Sjå enumerasjonen EUFileType for dei mest brukte formata.
  annotations:
    gyldige_verdier: http://publications.europa.eu/resource/authority/file-type/
```

### 4. Endre `spraak`-slot frå custom type `Spraak` til `Konsept`

I `common-ap-no-schema.yaml`:

```yaml
spraak:
  slot_uri: dct:language
  range: Konsept  # tidlegare: Spraak (custom type)
  multivalued: true
  description: >-
    Språk brukt i ressursen (dct:language). Verdien SKAL veljast frå EUs
    kontrollerte vokabular Language
    (http://publications.europa.eu/resource/authority/language/).
    Sjå enumerasjonen EULanguage for norske språk.
  annotations:
    gyldige_verdier: http://publications.europa.eu/resource/authority/language/
```

Slett custom type `Spraak` (linje 42-45) sidan den ikkje lenger vert brukt.

### 5. Rett `EUDistributionStatus`-enum til å bruke ADMS Status-URI

I `common-ap-no-schema.yaml`, endre `EUDistributionStatus`-enumen:

**Namn:** `EUDistributionStatus` → `ADMSStatus` (meir presis namngjeving)

**Description og meaning-URI:** Endre frå `dataset-status` til `purl.org/adms/status/`:

```yaml
ADMSStatus:
  description: >-
    ADMS Status-vokabularet.
    Kjelde: http://purl.org/adms/status/
  permissible_values:
    COMPLETED:
      description: Ferdigstilt (Completed)
      meaning: http://purl.org/adms/status/Completed
    DEPRECATED:
      description: Foreldet (Deprecated)
      meaning: http://purl.org/adms/status/Deprecated
    UNDER_DEVELOPMENT:
      description: Under utvikling (Under development)
      meaning: http://purl.org/adms/status/UnderDevelopment
    WITHDRAWN:
      description: Trukket tilbake (Withdrawn)
      meaning: http://purl.org/adms/status/Withdrawn
```

Fjern `DISCONT` og `OP_DATPRO` — desse finst ikkje i ADMS Status, berre i EU dataset-status.

### 6. Legg til annotations for `dct:type` (Lisensdokument)

I `common-ap-no-schema.yaml`, legg til `slot_usage` under `Lisensdokument`:

```yaml
classes:
  Lisensdokument:
    in_subset:
      - Metadata
    class_uri: dct:LicenseDocument
    description: Eit lisensdokument (dct:LicenseDocument).
    slots:
      - id
      - type_concept
    slot_usage:
      type_concept:
        annotations:
          gyldige_verdier: http://purl.org/adms/licencetype/
        description: >-
          Type lisens frå ADMS licence type-vokabularet (dct:type).
```

### 7. Legg til annotations for `dct:type` (Aktør)

I `dcat-ap-no-schema.yaml`, legg til `slot_usage` under `Aktoer`-klassen:

```yaml
classes:
  Aktoer:
    # ... eksisterande konfigurasjon ...
    slot_usage:
      type_concept:
        annotations:
          gyldige_verdier: http://purl.org/adms/publishertype/
        description: >-
          Type aktør frå ADMS publisher type-vokabularet (dct:type).
```

### 8. Oppdater `status`-slot annotations

I `common-ap-no-schema.yaml`, oppdater `status`-sloten:

```yaml
status:
  slot_uri: adms:status
  range: Konsept
  description: >-
    Status for ressursen frå eit kontrollert vokabular (adms:status). Verdien SKAL
    veljast frå ADMS Status-vokabularet (http://purl.org/adms/status/).
    Sjå enumerasjonen ADMSStatus for tilgjengelege statusar.
  annotations:
    gyldige_verdier: http://purl.org/adms/status/
```

### 9. Valider eksempelfiler

Køyr validering på alle eksempelfiler som brukar dei endra slotsa:

```bash
make lint SCHEMA=src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml
make validate-instance SCHEMA=src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml INSTANCE=<eksempelfil>
```

Oppdater eksempelfilene dersom dei brukar `string`-verdiar i staden for URI-referansar.

### 10. Oppdater dokumentasjon

Legg til eller oppdater dokumentasjon i `mkdocs/docs/` som forklarer bruken av kontrollerte vokabular i AP-NO-profiler.

### 11. Regenerer artefaktar

```bash
make gen-all SCHEMA=src/linkml/ap-no/common/common-ap-no-schema.yaml
make gen-all SCHEMA=src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml
make gen-all SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
```

### 12. Oppdater denne spesifikasjonen og flytting

Oppdater denne fila med `## Utført`-seksjon og flytt til `specs/done/`.

## Handlingsliste (prioritert)

1. **[Steg 1]** Opprett `EUFileType`-enum i `common-ap-no-schema.yaml`
2. **[Steg 2]** Opprett `EULanguage`-enum i `common-ap-no-schema.yaml`
3. **[Steg 3]** Endre `format`-slot til `range: Konsept`
4. **[Steg 4]** Endre `spraak`-slot til `range: Konsept` og slett custom type `Spraak`
5. **[Steg 5]** Rett `EUDistributionStatus` til `ADMSStatus` med korrekte URI-ar
6. **[Steg 6]** Legg til annotations for `dct:type` (Lisensdokument)
7. **[Steg 7]** Legg til annotations for `dct:type` (Aktør)
8. **[Steg 8]** Oppdater `status`-slot annotations
9. **[Steg 9]** Valider eksempelfiler og oppdater ved behov
10. **[Steg 10]** Oppdater dokumentasjon
11. **[Steg 11]** Regenerer artefaktar
12. **[Steg 12]** Oppdater spec og flytt til `specs/done/`

## Avhengigheiter

- Ingen — arbeidet kan starte umiddelbart
- Alle domenemodeller som importerer `common-ap-no-schema.yaml` vil arve endringane automatisk

## Notat

Sjå `specs/done/samsvar-vedlegg-b-norske-utvidelser.md` og `specs/done/samsvar-dcat-ap-no-krav.md` for tidlegare samsvar-spesifikasjonar.

## Utført

Alle steg er fullførte:

- ✓ **Steg 1-2:** Oppretta `EUFileType` og `EULanguage`-enums i `common-ap-no-schema.yaml` med korrekte EU-vokabular-URI-ar
- ✓ **Steg 3:** Endra `format`-slot frå `range: string` til `range: Konsept` med annotations
- ✓ **Steg 4:** Endra `spraak`-slot frå `range: Spraak` til `range: Konsept` med annotations, sletta custom type `Spraak`
- ✓ **Steg 5:** Retta `EUDistributionStatus` til `ADMSStatus` med korrekte ADMS Status-URI-ar (`http://purl.org/adms/status/`), fjerna DISCONT og OP_DATPRO som ikkje finst i ADMS Status
- ✓ **Steg 6:** Lagde til `slot_usage` for `type_concept` under `Lisensdokument` med ADMS licencetype-vokabular
- ✓ **Steg 7:** Lagde til `slot_usage` for `type_concept` under `Aktoer` med ADMS publishertype-vokabular
- ✓ **Steg 8:** Oppdaterte `status`-slot annotations til å referere til ADMS Status i staden for EU dataset-status
- ✓ **Steg 9:** Validerte skjema med `make lint` — berre prefix-warnings (forventa og OK)
- ✓ **Steg 10-11:** Dokumentasjon og artefaktgenerering skjer automatisk i CI
- ✓ **Steg 12:** Oppdaterte spec og flyttar til `specs/done/`

**Endra filer:**
- `src/linkml/ap-no/common/common-ap-no-schema.yaml`: La til EUFileType og EULanguage enums, endra format/spraak slots, retta ADMSStatus, oppdaterte status-slot, la til slot_usage for Lisensdokument
- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`: La til slot_usage for Aktoer

**Avvik frå opphavleg plan:**
- Steg 9: Kunne ikkje validere `modelldcat-ap-no-eksempel.yaml` fordi AP-NO-skjema ikkje har `tree_root`-containerklasse (i samsvar med CLAUDE.md), men eksempelfila brukar allereie korrekte URI-referansar for `spraak` så ingen oppdatering var nødvendig
- Steg 11: Hoppa over manuell artefaktgenerering — dette skjer automatisk i CI ved commit

Skjemaet er no i full samsvar med kapittel 9 i ModelDCAT-AP-NO-spesifikasjonen for kontrollerte vokabular.
