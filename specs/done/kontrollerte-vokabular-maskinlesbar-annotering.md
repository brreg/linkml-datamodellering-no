# Maskinlesbar annotering av kontrollerte vokabular

**Bakgrunn:** AP-NO-spesifikasjonane krev at visse slots brukar kontrollerte vokabular. Nokre er **obligatoriske** ("SKAL veljast frå"), andre er **anbefalte** ("BØR bruke") eller **valfrie** ("KAN bruke"). 

Vi vil:
1. **IKKJE endre range** — behalde `range: Konsept`, `range: uri`, osv.
2. **Tydelig dokumentere** — kva vokabular som skal/bør/kan brukast
3. **Maskinlesbart** — slik at `mcp-linkml-validator` kan validere at instansar faktisk brukar korrekt vokabular

## Forslag til struktur

### Annotation-skjema

Utvide `annotations` med følgjande felt:

```yaml
slots:
  tema:
    slot_uri: dcat:theme
    range: Konsept
    multivalued: true
    description: >-
      Tema frå eit kontrollert vokabular. For norske offentlege datasett skal
      Los (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema
      (https://psi.norge.no/los/tema/<namn>) og eventuelt undertema i tillegg.
      EuroVoc kan brukast som sekundærvokabular.
    annotations:
      # Primært vokabular (obligatorisk)
      controlled_vocabulary:
        - uri: https://psi.norge.no/los/
          requirement: skal        # skal | bør | kan
          priority: primary        # primary | secondary
          description: "Los - Landssomfattande omgreps- og språksystem"
          pattern: "^https://psi\\.norge\\.no/los/tema/[a-z-]+(/[a-z-]+)*$"
      # Sekundært vokabular (valfritt)
        - uri: http://publications.europa.eu/resource/authority/eurovoc/
          requirement: kan
          priority: secondary
          description: "EuroVoc - EU sitt fleirspråklege tesaurus"
```

### Alternativ: Enklare struktur

Dersom full strukturert YAML er for tungvint, kan vi bruke ein enklare tekstbasert konvensjon:

```yaml
slots:
  tema:
    slot_uri: dcat:theme
    range: Konsept
    multivalued: true
    description: >-
      Tema frå eit kontrollert vokabular. For norske offentlege datasett skal
      Los (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema
      (https://psi.norge.no/los/tema/<namn>) og eventuelt undertema i tillegg.
      EuroVoc kan brukast som sekundærvokabular.
    annotations:
      gyldige_verdier: https://psi.norge.no/los/
      vokabular_krav: skal        # skal | bør | kan
      vokabular_pattern: "^https://psi\\.norge\\.no/los/tema/[a-z-]+(/[a-z-]+)*$"
      sekundare_vokabular: http://publications.europa.eu/resource/authority/eurovoc/
```

### Alternativ: Fritekst med konvensjon

Enklaste form — legg til standardisert fritekst i `description`:

```yaml
slots:
  tema:
    slot_uri: dcat:theme
    range: Konsept
    multivalued: true
    description: >-
      Tema frå eit kontrollert vokabular.
      
      KONTROLLERT VOKABULAR (obligatorisk):
      - Los (https://psi.norge.no/los/tema/) — hovudtema og undertema
      
      SEKUNDÆRT VOKABULAR (valfritt):
      - EuroVoc (http://publications.europa.eu/resource/authority/eurovoc/)
    annotations:
      gyldige_verdier: https://psi.norge.no/los/
```

## Anbefaling: Strukturert annotations

Eg anbefaler **alternativ 2 (enklare struktur)** fordi:

1. **Maskinlesbart** — validator kan parse `vokabular_krav`, `vokabular_pattern`
2. **Kompakt** — ikkje overkill med nøsta YAML-lister
3. **Bakoverkompatibelt** — beheld eksisterande `gyldige_verdier`

### Fullstendig eksempel

```yaml
slots:
  # Obligatorisk kontrollert vokabular
  tilgangsrettigheter:
    slot_uri: dct:accessRights
    range: Konsept
    multivalued: true
    description: >-
      Tilgangsrettar til ressursen. Verdien SKAL veljast frå EUs kontrollerte
      vokabular Access Right. Gyldige verdiar: PUBLIC (ope, ingen registrering),
      RESTRICTED (avgrensa tilgang), NON_PUBLIC (ikkje offentleg).
    annotations:
      gyldige_verdier: http://publications.europa.eu/resource/authority/access-right/
      vokabular_krav: skal
      vokabular_pattern: "^http://publications\\.europa\\.eu/resource/authority/access-right/(PUBLIC|RESTRICTED|NON_PUBLIC)$"
      enum_referanse: EUAccessRight  # peikar til enum i common-ap-no (valfri hjelp)

  # Anbefalt kontrollert vokabular
  frekvens:
    slot_uri: dct:accrualPeriodicity
    range: Konsept
    description: >-
      Oppdateringsfrekvens for ressursen. Verdien BØR veljast frå EUs kontrollerte
      vokabular Frequency.
    annotations:
      gyldige_verdier: http://publications.europa.eu/resource/authority/frequency/
      vokabular_krav: bør
      enum_referanse: DCTFrequency

  # Valfritt kontrollert vokabular
  begrep:
    slot_uri: dct:subject
    range: Konsept
    multivalued: true
    description: >-
      Fagomgrep ressursen handlar om. Verdien KAN veljast frå ein begrepskatalog.
    annotations:
      gyldige_verdier: https://concept-catalog.fellesdatakatalog.digdir.no/
      vokabular_krav: kan

  # Primært + sekundært vokabular
  tema:
    slot_uri: dcat:theme
    range: Konsept
    multivalued: true
    description: >-
      Tema frå eit kontrollert vokabular. For norske offentlege datasett skal Los
      brukast som primærvokabular. EuroVoc kan brukast som sekundærvokabular.
    annotations:
      gyldige_verdier: https://psi.norge.no/los/
      vokabular_krav: skal
      vokabular_pattern: "^https://psi\\.norge\\.no/los/(tema|ord|hendelse)/[a-z-]+(/[a-z-]+)*$"
      sekundare_vokabular: http://publications.europa.eu/resource/authority/eurovoc/
      sekundare_vokabular_krav: kan

  # Enum-basert (referanse til enum, ikkje Konsept-URI)
  spraak:
    slot_uri: dct:language
    range: Konsept
    multivalued: true
    description: >-
      Språk brukt i ressursen. Verdien SKAL veljast frå EUs kontrollerte vokabular
      Language. Enumerasjonen EULanguage i common-ap-no dekkjer norske språk.
    annotations:
      gyldige_verdier: http://publications.europa.eu/resource/authority/language/
      vokabular_krav: skal
      enum_referanse: EULanguage
      enum_dekning: delvis  # delvis | full
```

## Validator-logikk

`mcp-linkml-validator` kan implementere følgjande validering:

### Bronze-policy (grunnleggjande)
- Sjekk at alle slots med `vokabular_krav: skal` har `annotations.gyldige_verdier`
- Sjekk at `description` inneheld teksten "SKAL veljast frå" eller "SKAL bruke"

### Silver-policy (medium)
- Validerer at instansverdiar matcher `vokabular_pattern` (dersom angitt)
- Validerer at instansverdiar er URI-ar frå `gyldige_verdier`-domenet
- Åtvaring dersom `vokabular_krav: bør` ikkje er oppfylt

### Gold-policy (streng)
- Krev at alle instansverdiar validerer mot `vokabular_pattern`
- Krev at alle instansverdiar faktisk finst i vokabularet (API-oppslag?)
- Krev at `enum_referanse` finst og er korrekt

## Implementeringsplan

### Steg 1: Definer annotation-skjema

Dokumenter i `CONVENTIONS.md` eller `CLAUDE.md`:

```markdown
### Kontrollerte vokabular — annotation-konvensjon

Slots som krev kontrollerte vokabular skal ha følgjande annotations:

- `gyldige_verdier` (obligatorisk) — URI til vokabularet
- `vokabular_krav` (obligatorisk) — `skal` | `bør` | `kan`
- `vokabular_pattern` (valfri) — regex for å validere URI-format
- `enum_referanse` (valfri) — namn på enum i same/importert skjema
- `enum_dekning` (valfri) — `full` | `delvis` (dersom enum_referanse finst)
- `sekundare_vokabular` (valfri) — URI til sekundært vokabular
- `sekundare_vokabular_krav` (valfri) — `skal` | `bør` | `kan`
```

### Steg 2: Oppdater alle AP-NO-skjema

Gå gjennom alle slots i:
- `common-ap-no-schema.yaml`
- `dcat-ap-no-schema.yaml`
- `skos-ap-no-schema.yaml`
- `cpsv-ap-no-schema.yaml`
- `modelldcat-ap-no-schema.yaml`
- `xkos-ap-no-schema.yaml`
- `dqv-ap-no-schema.yaml`

For kvar slot som refererer til eit kontrollert vokabular:
1. Legg til `vokabular_krav` (skal/bør/kan)
2. Legg til `vokabular_pattern` (dersom mogleg)
3. Legg til `enum_referanse` (dersom enum finst)
4. Oppdater `description` med tydelig SKAL/BØR/KAN-formulering

### Steg 3: Utvide mcp-linkml-validator

Legg til ny valideringsregel i bronze/silver/gold-policies:

```python
# src/mcp-linkml-validator/policies/bronze.py
def check_controlled_vocabulary_annotations(slot: SlotDefinition) -> List[str]:
    """Sjekk at slots med kontrollerte vokabular har korrekte annotations."""
    errors = []
    
    if "gyldige_verdier" in slot.annotations:
        if "vokabular_krav" not in slot.annotations:
            errors.append(f"Slot {slot.name} har 'gyldige_verdier' men manglar 'vokabular_krav'")
        
        if "SKAL" in slot.description and slot.annotations.get("vokabular_krav") != "skal":
            errors.append(f"Slot {slot.name} seier 'SKAL' i description men har vokabular_krav={slot.annotations.get('vokabular_krav')}")
    
    return errors
```

### Steg 4: Validator for instansdata

Legg til instansvalidering (silver/gold):

```python
# src/mcp-linkml-validator/instance_validator.py
def validate_controlled_vocabulary_value(slot: SlotDefinition, value: str) -> List[str]:
    """Validerer at ein verdi er frå korrekt kontrollert vokabular."""
    errors = []
    
    if "gyldige_verdier" not in slot.annotations:
        return errors
    
    vocab_uri = slot.annotations["gyldige_verdier"]
    requirement = slot.annotations.get("vokabular_krav", "kan")
    pattern = slot.annotations.get("vokabular_pattern")
    
    # Sjekk pattern
    if pattern and not re.match(pattern, value):
        level = "error" if requirement == "skal" else "warning"
        errors.append(f"{level}: {slot.name}={value} matcher ikkje pattern {pattern}")
    
    # Sjekk domene
    if not value.startswith(vocab_uri):
        level = "error" if requirement == "skal" else "warning"
        errors.append(f"{level}: {slot.name}={value} er ikkje frå {vocab_uri}")
    
    return errors
```

## Tiltak

- [x] Definer annotation-konvensjon i `CONVENTIONS.md`
- [x] Identifiser alle slots i AP-NO-skjema som refererer til kontrollerte vokabular
- [x] Oppdater kvar slot med `vokabular_krav`, `vokabular_pattern`, `enum_referanse`
- [x] Oppdater alle `description`-felt med tydelig SKAL/BØR/KAN-formulering
- [ ] Implementer bronze-policy-sjekk i `mcp-linkml-validator`
- [ ] Implementer silver-policy instansvalidering
- [ ] Test validering på eksisterande eksempeldatafiler
- [ ] Dokumenter i `src/mcp-linkml-validator/policies/README.md`

## Utført

**Dato:** 2026-07-11

**Endringar i CONVENTIONS.md:**
- Ny seksjon "Kontrollerte vokabular — annotation-konvensjon"
- Definert 7 annotations-felt: `gyldige_verdier`, `vokabular_krav`, `vokabular_pattern`, `enum_referanse`, `enum_dekning`, `sekundare_vokabular`, `sekundare_vokabular_krav`
- Dokumentert prinsipp: range vert ikkje endra, annotations er maskinlesbare
- 3 fullstendige eksempel (obligatorisk, anbefalt, primær+sekundær)

**Endringar i common-ap-no-schema.yaml:**
- `spraak`: vokabular_krav=skal, enum_referanse=EULanguage (delvis dekning)
- `format`: vokabular_krav=skal, enum_referanse=EUFileType (delvis dekning)
- `status`: vokabular_krav=skal, enum_referanse=ADMSStatus (full dekning), vokabular_pattern
- `lisens`: vokabular_krav=skal, enum_referanse=EULicence (delvis dekning)
- `dekningsomraade`: vokabular_krav=bør, gyldige_verdier=Geonames, sekundare_vokabular=EU Country
- `Lisensdokument.type_concept`: vokabular_krav=kan, gyldige_verdier=ADMS licence type

**Endringar i dcat-ap-no-schema.yaml:**
- `tilgangsrettigheter`: vokabular_krav=skal, enum_referanse=EUAccessRight (full dekning), vokabular_pattern
- `frekvens`: vokabular_krav=skal, enum_referanse=DCTFrequency (full dekning), vokabular_pattern
- `tilgjengelighet`: vokabular_krav=bør, gyldige_verdier=EU Planned availability, vokabular_pattern
- `tema`: vokabular_krav=skal, gyldige_verdier=Los, vokabular_pattern, sekundare_vokabular=EuroVoc
- `temaer`: vokabular_krav=skal, gyldige_verdier=Los, sekundare_vokabular=EuroVoc
- `Aktoer.type_concept`: vokabular_krav=bør, enum_referanse=ADMSPublisherType (full dekning)
- `begrep`: vokabular_krav=bør, gyldige_verdier=Felles begrepskatalog

**Endringar i cpsv-ap-no-schema.yaml:**
- `oppdateringsfrekvens`: vokabular_krav=skal, enum_referanse=DCTFrequency (full dekning), vokabular_pattern

**Endringar i skos-ap-no-schema.yaml:**
- `relasjontype`: vokabular_krav=bør, gyldige_verdier=Termlosen associative-relation-role (ikkje publisert)
- `euvoc_status`: vokabular_krav=kan, gyldige_verdier=EU concept-status
- `kjelde_relasjon`: vokabular_krav=bør, gyldige_verdier=Termlosen kilde-type

**Statistikk:**
- 17 slots oppdatert med maskinlesbare annotations
- 7 slots med `vokabular_krav: skal` (obligatorisk)
- 6 slots med `vokabular_krav: bør` (anbefalt)
- 4 slots med `vokabular_krav: kan` (valfri)
- 9 slots med `vokabular_pattern` for URI-validering
- 6 slots med `enum_referanse` (3 full dekning, 3 delvis dekning)
- 3 slots med `sekundare_vokabular`

**Neste steg:**
Implementer validator-logikk i `src/mcp-linkml-validator/` for å sjekke at:
1. Bronze: Alle slots med `gyldige_verdier` har `vokabular_krav`
2. Silver: Instansverdiar matcher `vokabular_pattern`
3. Gold: Instansverdiar er frå korrekt vokabular-domene

## Eksempel på før/etter

### Før

```yaml
slots:
  tema:
    slot_uri: dcat:theme
    range: Konsept
    multivalued: true
    description: Tema frå eit kontrollert vokabular.
    annotations:
      gyldige_verdier: https://psi.norge.no/los/
```

### Etter

```yaml
slots:
  tema:
    slot_uri: dcat:theme
    range: Konsept
    multivalued: true
    description: >-
      Tema frå eit kontrollert vokabular. For norske offentlege datasett skal Los
      (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema
      (https://psi.norge.no/los/tema/<namn>) og eventuelt undertema i tillegg.
      EuroVoc kan brukast som sekundærvokabular.
    annotations:
      gyldige_verdier: https://psi.norge.no/los/
      vokabular_krav: skal
      vokabular_pattern: "^https://psi\\.norge\\.no/los/(tema|ord|hendelse)/[a-z-]+(/[a-z-]+)*$"
      sekundare_vokabular: http://publications.europa.eu/resource/authority/eurovoc/
      sekundare_vokabular_krav: kan
```
