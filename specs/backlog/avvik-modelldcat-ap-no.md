# Kartlegging: Avvik mot Spesifikasjon for beskrivelse av informasjonsmodeller (ModelDCAT-AP-NO)

**Kjelde:** [data.norge.no/specification/modelldcat-ap-no](https://data.norge.no/specification/modelldcat-ap-no/)  
**Versjon:** 1.3.3 (gjeldande per 2026-03-20)  
**Primær implementasjon:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`  
**Datafil:** `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml`

---

## Bakgrunn

`modelldcat-ap-no-schema.yaml` implementerer ModelDCAT-AP-NO som ein LinkML-
applikasjonsprofil. Skjemaet dekkjer alle 30+ klassar i spesifikasjonen (frå
`Informasjonsmodell` til `Begrensningsregel`, `Kodeelement` og alle eigenskapstypar).
Overordna er implementasjonen svært god — dei identifiserte avvika er primært
knytte til manglande felthandhaving, inkonsistente hjelpeklassar og data-gap
i `brreg-modellkatalog.yaml`.

Kartlegginga er delt i tre:

1. **Schema-strukturelle avvik** — feil eller manglar i `modelldcat-ap-no-schema.yaml`
2. **Data-gap** — manglar i `brreg-modellkatalog.yaml` relativt til schema-krav
3. **Krysstilvisingar** — avvik allereie handsama i andre specs

---

## Del A: Schema-strukturelle avvik

### A1 — `Aktoer.navn_aktoer` manglar `required: true`

Sloten `navn_aktoer` (`foaf:name`) er merka som `in_subset: [Obligatorisk]` på
`Aktoer`-klassen, men manglar `required: true`:

```yaml
Aktoer:
  slot_usage:
    navn_aktoer:
      in_subset:
        - Obligatorisk          # ← ikkje enforcement
        # required: true        # ← manglar!
```

LinkML sin validator kontrollerer ikkje `in_subset` — berre `required: true`
fører til valideringsfeil. Ein `Aktoer`-instans utan namn vil difor passere
validering trass i at spec krev det.

**Status:** ⚠️ Manglande validering — høg prioritet

---

### A2 — `Kontaktopplysning` manglar `vcard:fn` og andre vCard-eigenskapar

`Kontaktopplysning` i `modelldcat-ap-no-schema.yaml` er definert med berre `id`:

```yaml
Kontaktopplysning:
  class_uri: vcard:Organization
  slots:
    - id
```

I `dcat-ap-no-schema.yaml` er den tilsvarande klassen rikare:

```yaml
Kontaktopplysning:
  class_uri: vcard:Kind
  slots:
    - id
    - navn_vcard       # vcard:fn — Obligatorisk
    - har_epost        # vcard:hasEmail
    - har_kontaktside  # vcard:hasURL
```

Konsekvensen er at ein `Kontaktopplysning` i `brreg-modellkatalog.yaml` kan
opprettast med berre ein URI utan namn, e-post eller nettside — og vil validere
utan feil. Dette er utilstrekkeleg for eit menneskelesbart register.

I tillegg er det ein inkonsistens mellom dei to skjema i same repo:
- `dcat-ap-no`: `class_uri: vcard:Kind` (superklasse — meir allment ✓)
- `modelldcat-ap-no`: `class_uri: vcard:Organization` (subklasse — meir spesifikt)

**Status:** ⚠️ Manglande slots + inkonsistens — høg prioritet

---

### A3 — `Lokasjon`-klassen er definert men ikkje brukt som `range`

`Lokasjon` (`dct:Location`) er definert i skjemaet:

```yaml
Lokasjon:
  class_uri: dct:Location
  slots:
    - id
```

Men `dekningsomraade`-sloten (arva frå `common-ap-no-schema`) brukar
`range: Konsept`, ikkje `range: Lokasjon`:

```yaml
# I common-ap-no-schema.yaml:
dekningsomraade:
  slot_uri: dct:spatial
  range: Konsept           # ← Konsept, ikkje Lokasjon
```

Spec seier `dct:spatial` → `dct:Location`. Klassen er definert men kopla aldri
inn — han er eit "dead code"-element i skjemaet.

**Status:** ⚠️ Ubrukt klasse / feil range — middels prioritet

---

### A4 — `Modellkatalog.har_del` er feilaktig `required: true`

```yaml
Modellkatalog:
  slot_usage:
    har_del:
      required: true
      in_subset:
        - Obligatorisk
```

`dct:hasPart` er i DCAT-familien vanlegvis ein Anbefalt eigeskap — ein katalog
bør tillate å eksistere utan innhald (t.d. under oppretting). At `required: true`
er satt betyr at ein tom modellkatalog ikkje kan serialiserast og validere.

Spesifikasjonen har ikkje `dct:hasPart` som Obligatorisk (1..n) på `Modellkatalog`.
`modelldcatno:model` er den primære måten å liste modellar, og den er Anbefalt.

**Status:** ⚠️ Feil subset/required — middels prioritet

---

### A5 — `Informasjonsmodell.type_concept` manglar vokabular-annotasjon

`type_concept` (`dct:type`) på `Informasjonsmodell` har range `Konsept` men
ingen annotasjon om kva vokabular tilrådde verdiar kjem frå:

```yaml
type_concept:
  in_subset:
    - Valgfri
  # ingen gyldige_verdier-annotasjon
```

Spec tilrår at `dct:type` på `Informasjonsmodell` brukar eit kontrollert
vokabular for modelltype (f.eks. `modelldcatno:InformationModelType`-vokabularet
som skil mellom `LogiskDatamodell`, `Begreptsmodell`, `Fysiskdatamodell` osb.).

**Status:** ⚠️ Manglande annotasjon — låg prioritet

---

### A6 — `Standard`-klassen i `modelldcat-ap-no` er uavhengig av `dqv-ap-no`

`modelldcat-ap-no-schema.yaml` definerer sin eigen `Standard`-klasse:

```yaml
Standard:
  class_uri: dct:Standard
  slots:
    - id
    - tittel
    - har_referanse
    - versjonsnummer
```

`dqv-ap-no-schema.yaml` definerer òg ein `Standard`-klasse (med ekstra DQV-slot
`er_i_kvalitetsdimensjon`). Desse er parallelle definisjonar utan kryssinmport.

Sidan `modelldcat-ap-no` ikkje importerer `dqv-ap-no`, er det inga sirkulær
avhengigheit her — men dei to `Standard`-klassane er ikkje same klasse i
schema-grafen. Data som brukar `modelldcat-ap-no`-varianten vil ikkje automatisk
arve DQV-eigenskapar.

Når DQ1 i `specs/backlog/avvik-dqv-ap-no.md` er gjennomført (flytt `Standard`
til `dcat-ap-no`), bør `modelldcat-ap-no` importere `dcat-ap-no` for å dele
`Standard`-definisjonen.

**Status:** ℹ️ Arkitektur-observasjon — låg prioritet, avhengig av DQ1

---

## Del B: Data-gap i `brreg-modellkatalog.yaml`

Datafila er publisert eksternt (`publish_external: true`, `data_policy: felles-datakatalog`).
God metadata-kvalitet er difor viktig.

### B1 — `Informasjonsmodell`-instansar manglar silver-felt

Begge instansane (`ngr-virksomhet` og `register-over-aksjeeiere`) manglar:

| Felt | Slot | Subset |
|---|---|---|
| Status | `status` | Valgfri (bør Anbefalt per god praksis) |
| Utgivelsesdato | `utgivelsesdato` | Valgfri |
| Endringsdato | `endringsdato` | Valgfri |
| Versjonsnummer | `versjonsnummer` | Valgfri |

Desse felta er Valgfri per spec, men er anbefalt per ADMS og god
datakatalog-praksis. Felles datakatalog nyttar desse til å vise versjonsstatus
og endringshistorikk.

Tilrådde verdiar for `status`:
```
http://purl.org/adms/status/Completed       # Ferdigstilt
http://purl.org/adms/status/UnderDevelopment # Under utarbeidelse
```

**Status:** ⚠️ Data-gap — middels prioritet

---

### B2 — Berre 2 av ~21 skjema er i modellkatalogen

Datafila inneheld berre `ngr-virksomhet` og `register-over-aksjeeiere` som
informasjonsmodellar. Repoet inneheld langt fleire modellerte domenemodeller:
`ngr-adresse`, `ngr-person`, `ngr-eiendom`, `enhetsregisteret-bvrinn`,
alle FINT-modellane, `samt-bu` osb.

Dette er allereie identifisert som tiltak **MD2** i
`specs/backlog/avvik-veileder-modelldcat-ap-no.md`.

**Status:** ⚠️ Data-gap — sjå MD2 i `avvik-veileder-modelldcat-ap-no.md`

---

### B3 — `Modellkatalog`-instansen manglar `tema`-verdi

```yaml
modellkataloger:
- id: https://brreg.no/modellkatalogar/brreg-modellkatalog
  # tema:  ← manglar (Anbefalt)
```

Spec tilrår `dcat:theme` (tema) på `Modellkatalog` som Anbefalt.
EuroVoc-URI eller Los-URI bør nyttast.

**Status:** ⚠️ Data-gap — låg prioritet

---

## Samandrag

| # | Avvik | Type | Prioritet |
|---|---|---|---|
| A1 | `Aktoer.navn_aktoer` manglar `required: true` | Schema | **Høg** |
| A2 | `Kontaktopplysning` manglar vCard-slots og har feil `class_uri` | Schema | **Høg** |
| A3 | `Lokasjon`-klassen ubrukt — `dekningsomraade.range: Konsept` | Schema | Middels |
| A4 | `Modellkatalog.har_del` feilaktig `required: true` | Schema | Middels |
| A5 | `Informasjonsmodell.type_concept` manglar vokabular-annotasjon | Annotasjon | Låg |
| A6 | `Standard`-klassen parallell med `dqv-ap-no` — bør samordnast | Arkitektur | Låg |
| B1 | Informasjonsmodell-instansar manglar `status`, datoar, versjon | Data | Middels |
| B2 | Berre 2/21+ skjema i modellkatalogen | Data | Middels (MD2) |
| B3 | `Modellkatalog`-instansen manglar `tema` | Data | Låg |

---

## Tilrådde tiltak

### MC1 — Legg til `required: true` på `Aktoer.navn_aktoer` (A1)

```yaml
Aktoer:
  slot_usage:
    navn_aktoer:
      required: true
      in_subset:
        - Obligatorisk
```

**Filer:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`

---

### MC2 — Utvid `Kontaktopplysning` med vCard-eigenskapar (A2)

Juster `class_uri` til `vcard:Kind` (slik som i `dcat-ap-no`) og legg til
`vcard:fn` (namn) som Obligatorisk:

```yaml
Kontaktopplysning:
  class_uri: vcard:Kind        # ikkje vcard:Organization
  slots:
    - id
    - navn_vcard               # vcard:fn — legg til
    - har_epost                # vcard:hasEmail — legg til
    - har_kontaktside          # vcard:hasURL — legg til
  slot_usage:
    navn_vcard:
      in_subset:
        - Obligatorisk
    har_epost:
      in_subset:
        - Anbefalt
    har_kontaktside:
      in_subset:
        - Valgfri
```

Slots `navn_vcard`, `har_epost` og `har_kontaktside` er allereie definert i
`common-ap-no-schema.yaml` og kan importerast direkte.

**Filer:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`

---

### MC3 — Kople `Lokasjon`-klassen til `dekningsomraade` eller slett henne (A3)

*Alternativ A* — Endre `dekningsomraade` i `Informasjonsmodell.slot_usage` til
`range: Lokasjon`:

```yaml
Informasjonsmodell:
  slot_usage:
    dekningsomraade:
      range: Lokasjon
```

*Alternativ B* — Slett `Lokasjon`-klassen og behald `range: Konsept`
(då treng ein ikkje endre slot-definisjonen).

*Anbefalt: Alternativ B* — `dct:Location` utan eigenskapar er berre eit URI-peikar;
`Konsept`-range gjev same funksjon utan ein overflødug klasse.

**Filer:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`

---

### MC4 — Endre `Modellkatalog.har_del` til Anbefalt (A4)

```yaml
Modellkatalog:
  slot_usage:
    har_del:
      required: false          # fjern required: true
      in_subset:
        - Anbefalt             # Obligatorisk → Anbefalt
```

**Filer:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`

---

### MC5 — Legg til vokabular-annotasjon på `type_concept` (A5)

```yaml
# I Informasjonsmodell.slot_usage:
type_concept:
  in_subset:
    - Valgfri
  annotations:
    gyldige_verdier: >-
      https://data.norge.no/vocabulary/modelldcatno#LogicalDataModel
      https://data.norge.no/vocabulary/modelldcatno#ConceptualDataModel
      https://data.norge.no/vocabulary/modelldcatno#PhysicalDataModel
```

**Filer:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`

---

### MC6 — Legg til silver-felt i `brreg-modellkatalog.yaml` (B1)

Legg til `status`, `utgivelsesdato` og `endringsdato` på begge
`Informasjonsmodell`-instansane:

```yaml
informasjonsmodeller:
- id: https://brreg.no/modellkatalogar/brreg-modellkatalog/ngr-virksomhet
  ...
  status: http://purl.org/adms/status/Completed
  utgivelsesdato: "2024-01-01"
  endringsdato: "2026-06-15"
  versjonsnummer: "1.0.0"
```

**Filer:** `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml`

---

### MC7 — Legg til `tema` på `Modellkatalog`-instansen (B3)

```yaml
modellkataloger:
- id: https://brreg.no/modellkatalogar/brreg-modellkatalog
  ...
  tema:
  - https://psi.norge.no/los/tema/naering-og-sysselsetting
```

**Filer:** `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml`

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | MC1: `required: true` på `Aktoer.navn_aktoer` | `modelldcat-ap-no-schema.yaml` | — |
| 2 | MC2: Utvid `Kontaktopplysning` med vCard-slots | `modelldcat-ap-no-schema.yaml` | — |
| 3 | MC4: `Modellkatalog.har_del` → Anbefalt | `modelldcat-ap-no-schema.yaml` | — |
| 4 | MC6: Silver-felt på Informasjonsmodell-instansar | `brreg-modellkatalog.yaml` | — |
| 5 | MC3: Fjern `Lokasjon`-klassen (Alternativ B) | `modelldcat-ap-no-schema.yaml` | — |
| 6 | MC7: `tema` på Modellkatalog-instans | `brreg-modellkatalog.yaml` | — |
| 7 | MC5: Vokabular-annotasjon på `type_concept` | `modelldcat-ap-no-schema.yaml` | — |
| 8 | A6: Samordne `Standard` med `dcat-ap-no` | begge schema | DQ1 i `avvik-dqv-ap-no.md` |

---

## Avhengigheiter og krysstilvisingar

- **MD2** (`avvik-veileder-modelldcat-ap-no.md`): Utvid modellkatalogen til å
  dekkje alle skjema i repoet — koordiner med MC6
- **DQ1** (`avvik-dqv-ap-no.md`): Flytt `Standard`-klassen til `dcat-ap-no` —
  etter det bør `modelldcat-ap-no` importere `dcat-ap-no` for samstemming (A6)
- MC2 brukar slots frå `common-ap-no-schema.yaml` som ikkje er importert i
  `modelldcat-ap-no-schema.yaml`; det kan krevje at importen vert lagt til
  (eller at slotdefinisjoane vert dupliserte — unngå det siste)

**Merk:** `modelldcat-ap-no-schema.yaml` importerer `common-ap-no-schema` allereie
(via `imports: - ../common/common-ap-no-schema`), så `navn_vcard`, `har_epost`
og `har_kontaktside` er tilgjengelege utan endringar i imports.
