# AP-NO – Arkitektur, avvik og strukturelle val

Dette dokumentet er den sentrale referansen for å forstå korleis AP-NO-skjemaa er
bygde opp i dette repoet: kva val som er tekne, kvar vi medvite avvik frå
spesifikasjonane, og kvifor. Det er skrive for å vere lett å lese både for
menneske og for LLM-ar.

Detaljerte kartleggingsdokument per skjema ligg i `specs/done/` og `specs/backlog/`.

---

## Importkjede

```
linkml:types
      │
      ▼
common-ap-no
 ┌────┴────────────────────────────────────────────────────────┐
 ▼                 ▼              ▼             ▼              ▼
dqv-core       skos-ap-no   xkos-ap-no   cpsv-ap-no   modelldcat-modell
 │                                                            │
 ▼                                                            ▼
dcat-ap-no                                           modelldcat-katalog
 │                                                            │
 ▼                                                            ▼
dqv-ap-no                                          modelldcat-ap-no (pass-through)
```

Reglane:
- `common-ap-no` er det einaste AP-NO-skjemaet utan AP-NO-overordna
- `domenemodell`-skjema importerer AP-NO-profilene, **ikkje** `common-ap-no` direkte
- `fint-common` og `oreg`-skjema følgjer sine eigne importkjeder (sjå CLAUDE.md)

---

## Arkitektoniske avgrensingar i LinkML

To avgrensingar i LinkML har direkte påverknad på korleis AP-NO-skjemaa er
strukturerte:

### Avgrensing 1 — Class override erstattar (merge ikkje) `slots:`-lista

Når ein subschema redeklarerer ein klasse med ei `slots:`-liste (i staden for
berre `slot_usage:`), vil JSON-schema-generatoren ERSTATTE foreldreschemasins
`slots:`-liste — ikkje slå dei saman. Det fører til at alle slots frå
foreldreschemasinet forsvinn frå JSON-schema-validering.

**Konsekvens:** Vi kan ikkje la `dqv-ap-no` redeklarere `Datasett` med ekstra
DQV-slots — alle `dcat-ap-no`-slots (tittel, beskrivelse m.fl.) ville forsvinne
frå validering.

**Løysing:** `har_kvalitetsmerknad` og `har_kvalitetsmaaling` er definert direkte
på `Datasett` i `dcat-ap-no-schema.yaml`. DQV-slots er tilgjengeleg utan at
`dqv-ap-no` treng å redeklarere `Datasett`.

### Avgrensing 2 — `no_invalid_slot_usage` krev at slot er deklarert i `slots:`

Lint-regelen `no_invalid_slot_usage` krev at ein slot som brukast i `slot_usage:`
i eit subschema allereie er deklarert i klassens eigen `slots:`-liste. Det er
ikkje mogleg å bruke `slot_usage:` i eit importerande skjema til å narrowe ein
slot frå eit importert skjema berre via `slot_usage:`.

**Konsekvens:** `dqv-ap-no` kan ikkje narrowe `har_maal.range` frå `uriorcurie`
til `KatalogisertRessurs` via `slot_usage:` — klassen `Kvalitetsmerknad` eig
ikkje `har_maal` i sitt eige `slots:`-oppslag i `dqv-ap-no`.

**Løysing:** `har_maal.range` forblir `uriorcurie` i `dqv-core-schema.yaml`.
URI-verdiar passerer likevel validering korrekt.

---

## Skjemaoversikt

### `common-ap-no` — Felles basislaget

**Fil:** `src/linkml/ap-no/common/common-ap-no-schema.yaml`

Delt lag for alle AP-NO-profilene. Definerer:
- Basistypar: `LangString`, `Konsept`, `Begrepssamling`, `Spraak`, `Mediatype`
- Delte slots: `id`, `tittel`, `beskrivelse`, `nokkelord`, `endringsdato`,
  `utgivelsesdato`, `versjonsnummer`, `versjonsmerknad`, `status`, `heimeside`,
  `format`, `spraak`, `identifikator_literal`, `type_concept`, `dekningsomraade`,
  `har_referanse`, `har_merknad`

**Kjente avvik:** Ingen dokumenterte.

---

### `dcat-ap-no` — Datasett og distribusjon

**Fil:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`  
**Spesifikasjon:** <https://informasjonsforvaltning.github.io/dcat-ap-no/>  
**Kartlegging:** `specs/done/avvik-dcat-ap-no.md`

**Utførte rettingar:**

| Kode | Avvik | Status |
|------|-------|--------|
| DA1 | `time:`-namespace var feil (`6006` → `2006`) | ✓ Fiksa |
| DA2 | `frekvens` (`dct:accrualPeriodicity`) mangla på `Datasett` | ✓ Fiksa |
| DA3 | `Standard.versjonsnummer` → `versjon` (`dcat:version`) | ✓ Fiksa |
| DA4 | Manglande valfrie slots: `dcat:spatialResolutionInMeters`, versjonslenkjer, `dct:isReferencedBy` | ✓ Fiksa |
| DA5 | `har_gebyr` (`cv:hasCost`) mangla på `Datasett` | ✓ Fiksa |
| DA8 | `Aktor.identifikator_literal` ikkje merka som `Anbefalt` | ✓ Fiksa |

**Opne punkt:**

| Kode | Avvik | Merknad |
|------|-------|---------|
| DA6 | Utgjevar-URI-mønster (`data.norge.no` vs. spesifikasjon) | Avklart — ingen endring nødvendig |

**Arkitektoniske val:**
- `Standard`-klassen er definert her (ikkje i `dqv-ap-no`) for å unngå sirkulær import
- `har_kvalitetsmerknad` og `har_kvalitetsmaaling` er lagt direkte på `Datasett`
  her (får DQV-slots via import av `dqv-core`)
- Importerer `dqv-core-schema` (ikkje `dqv-ap-no-schema`) for å bryte sirkulær import

---

### `dqv-core` — DQV-kjerneklassar (bridge-fil)

**Fil:** `src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml`  
**Opphav:** Oppretta som løysing på sirkulær import (MC11)

Denne fila er ikkje ei eiga AP-NO-profil — det er eit arkitektonisk lag for å bryte
den sirkulære avhengigheita mellom `dcat-ap-no` og `dqv-ap-no`.

**Inneheld:**
- Alle DQV-kjerneklassar: `Kvalitetsdimensjon`, `Kvalitetsdeldimensjon`,
  `Kvalitetsmaal`, `Kvalitetsmerknad`, `Brukartilbakemelding`,
  `Kvalitetssertifikat`, `Kvalitetsmaaling`, `Tekstdel`
- Alle DQV-slots: `har_kvalitetsmerknad`, `har_kvalitetsmaaling`, `har_maal`, m.fl.
- Enum: `DqvMotivasjon`

**Medvitne avvik frå DQV-AP-NO-spesifikasjon:**

| Felt | Implementasjon | Spesifikasjon | Årsak |
|------|---------------|---------------|-------|
| `har_maal.range` | `uriorcurie` | `KatalogisertRessurs` | Unngå sirkulær import (sjå avgrensing 2 ovanfor) |

---

### `dqv-ap-no` — Datakvalitet

**Fil:** `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`  
**Spesifikasjon:** <https://informasjonsforvaltning.github.io/dqv-ap-no/>  
**Kartlegging:** `specs/done/avvik-dqv-ap-no.md`

**Utførte rettingar:**

| Kode | Avvik | Status |
|------|-------|--------|
| DQ1 | Sirkulær import `dcat-ap-no` ↔ `dqv-ap-no` — løyst med `dqv-core` | ✓ Fiksa |
| DQ2 | `har_tekstdel` (`oa:hasBody`) mangla `multivalued: true` | ✓ Fiksa |
| DQ3 | `har_verdi.range: string` — erstatta med tre typeseparerte slots | ✓ Fiksa |
| DQ4 | `Motivasjon`-klasse ikkje modellert — `DqvMotivasjon`-enum lagt til | ✓ Fiksa |
| DQ5 | `har_maal.range: uri` → `uriorcurie` (sjå note under) | ✓ Delvis fiksa |

**Note DQ5:** Full narrowing til `KatalogisertRessurs` er blokkert av LinkML-avgrensing 2.
`uriorcurie` er næraste mogleg range i `dqv-core`. `dqv-ap-no` kan ikkje re-narrowe
via `slot_usage:` utan at `Kvalitetsmerknad` redeklarerer `slots: [har_maal]`,
som igjen ville aktivere avgrensing 1.

**Att i `dqv-ap-no`-skjemaet:**
- `Standard`-klasse override med `er_i_kvalitetsdimensjon` (DQV-spesifikt slot).
  Merk: dette er ein class override med `slots:` — dei avleia slots frå `dcat-ap-no`
  er pre-eksisterande i JSON-schema-validering (kjend avgrensing, uendra frå start).

---

### `skos-ap-no` — Omgrep og begrepskatalog

**Fil:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`  
**Spesifikasjon:** <https://informasjonsforvaltning.github.io/skos-ap-no-begrep/>  
**Kartlegging:** `specs/done/avvik-skos-ap-no.md`

**Status:** SK1–SK4 er fiksa. SK5 (tospråkskrav/språkkonsistens) er delvis
realisert som ein `instance_check` (`begrep_har_definisjon_pa_nb_og_nn`) i
`felles-begrepskatalog`-policyen — dekker `har_definisjon`-varianten via
ID-suffikskonvensjon. Full dekning av `anbefalt_term` og språkkonsistens krev
språktagging av `LangString` på tvers av AP-NO-profilane og er utsett til ein
eigen, ikkje-oppretta spec (`spraaktagging-av-langstring.md`).

---

### `xkos-ap-no` — Klassifikasjonar

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Spesifikasjon:** <https://data.norge.no/specification/xkos-ap-no>  
**Kartlegging:** `specs/backlog/avvik-xkos-ap-no.md`

**Kjente avvik (ikkje fiksa):**

| Kode | Avvik | Prioritet |
|------|-------|-----------|
| XK1 | `tidsrom_start`/`tidsrom_slutt` brukar feil slot-URI (`schema:` i staden for `dcat:`) | Kritisk |
| XK2 | `notasjon` (`skos:notation`) manglar på `Kategori` | Middels |
| XK3 | `antall_nivaa` burde vere Obligatorisk (er Anbefalt) | Middels |
| XK4 | Dekkingseigeanskapar (`xkos:covers*`) manglar | Middels |
| XK5 | `xkos:supersedes` og innhaldsmerknadar manglar | Middels |
| XK6 | Anbefalt eigenskapar manglar på `Klassifikasjonssamanlikning` | Låg |
| XK7 | Valgfrie notasjons- og merknadsslotar manglar på `Kategori` | Låg |

---

### `modelldcat-ap-no` — Informasjonsmodellar

**Hovudfil (pass-through):** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`  
**Modell-del:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml`  
**Katalog-del:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml`  
**Spesifikasjon:** <https://data.norge.no/specification/modelldcat-ap-no>  
**Kartlegging:** `specs/backlog/avvik-modelldcat-ap-no.md`

**Arkitektoniske val (MC10):**

Skjemaet er delt i to filer for å matche spesifikasjonsstrukturen:
- `modelldcat-modell-schema` — alle Modellelement-klassane (27 klassar)
- `modelldcat-katalog-schema` — Modellkatalog, Informasjonsmodell og hjelpeklassar
- `modelldcat-ap-no-schema` — pass-through for bakoverkompatibilitet

`begrep`-sloten (`dct:subject`) er definert i `modell`-skjemaet fordi `Modellelement`
brukar det. `Informasjonsmodell` (i `katalog`-skjemaet) arvar det via import.

**Gjennomførte rettingar (MC10 — del av splitting):**

| Avvik | Løysing |
|-------|---------|
| A1: `Aktoer.navn_aktoer` mangla `required: true` | Fiksa i ny `modelldcat-katalog-schema.yaml` |
| A2: `Kontaktopplysning` mangla vCard-eigenskapar | Fiksa: `navn_vcard`, `har_epost`, `har_kontaktside` lagt til |
| A4: `Modellkatalog.har_del` feilaktig `required: true` | Fiksa: no berre `in_subset: [Anbefalt]` |
| A5: `Informasjonsmodell.type_concept` mangla vokabularannotasjon | Fiksa: `gyldige_verdier`-annotasjon lagt til |

**Kjente avvik (ikkje fiksa):**

| Kode | Avvik | Prioritet |
|------|-------|-----------|
| A3 | `Lokasjon`-klassen er definert men ikkje brukt som `range` | Middels |
| A6/MC8 | Import av `dcat-ap-no` ikkje gjennomført — blokkert av 5 klassekollidjonar | Høg (blokkert) |

**Blokkert: MC8 — Import av `dcat-ap-no` i `modelldcat-katalog`**

`modelldcat-katalog` definerer eigne hjelpeklassar (`Aktoer`, `Kontaktopplysning`,
`Standard`, `Tidsrom`, `Lisensdokument`) som kolliderer med tilsvarande klassar i
`dcat-ap-no`. Import kan ikkje gjennomførast før desse kollisjonane er løyste
(merge, rename, eller dedikert bridge-schema). Sjå `specs/backlog/avvik-modelldcat-ap-no.md`
§A6 for fullstendig oversikt.

---

### `cpsv-ap-no` — Offentlege tenester

**Fil:** `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`  
**Spesifikasjon:** <https://informasjonsforvaltning.github.io/cpsv-ap-no/>

Ingen avvikskartlegging er gjennomført. Skjemaet importerer `common-ap-no` og
definerer klassane `Teneste`, `Hendelse` m.fl. per spesifikasjonen.

---

## Mønster som gjeld alle AP-NO-skjema

### Lenking framfor inlining

Alle klasser med identitet (alle unntatt reine hjelpeklassar som `LangString`)
har eit `id`-slot med `identifier: true` og `range: uriorcurie`. Referansar til
andre klassar er **ikkje** `inlined: true` — dei er URI-referansar i datafiler.

### `slot_usage` for obligatorisk/anbefalt/valgfri

`in_subset` med verdiane `Obligatorisk`, `Anbefalt`, `Valgfri` (og `Metadata`)
markerer kva nivå ein eigenskap ligg på per spesifikasjonen. `required: true`
settast **berre** for `Obligatorisk`-eigenskapar som krev maskinkontroll.

### Containerklasse

Alle toppnivå-domenemodell-skjema (ikkje AP-NO-profilene) har éin containerklasse
med `tree_root: true` og `attributes:` (ikkje `slots:`). AP-NO-profil-skjema har
ikkje eigen containerklasse.

### Norsk translitterering i identifikatorar

Særnorske bokstavar translittererast i klassenamn, slotnamn og URI-lokaldel:
`æ→ae`, `ø→oe`, `å→aa`. Gjeld ikkje fritext-felt (`title`, `description`).

---

## Referansar

- `specs/done/avvik-dcat-ap-no.md` — detaljert kartlegging DCAT-AP-NO
- `specs/done/avvik-dqv-ap-no.md` — detaljert kartlegging DQV-AP-NO
- `specs/done/avvik-skos-ap-no.md` — kartlegging SKOS-AP-NO
- `specs/done/avvik-xkos-ap-no.md` — kartlegging XKOS-AP-NO
- `specs/done/avvik-modelldcat-ap-no.md` — kartlegging ModelDCAT-AP-NO
- `specs/done/avvik-felles-modelleringsregler.md` — Digdir-modelleringsreglar
