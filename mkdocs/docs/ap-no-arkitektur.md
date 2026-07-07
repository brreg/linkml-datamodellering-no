# AP-NO - Arkitektur, avvik og strukturelle val

!!! note "Beskrivelse"

    Dette dokumentet er den sentrale referansen for å forstå korleis AP-NO-skjemaa er bygde opp i dette repoet: kva val som er tekne, kvar vi medvite avvik frå spesifikasjonane, og kvifor. Det er skrive for å vere lett å lese både for menneske og for LLM-ar.

Detaljerte kartleggingsdokument per skjema ligg i `specs/done/` og `specs/backlog/`.

---

## Importkjede

Sjå [Importhierarki](importhierarki.md#ap-no-hierarki) for fullstendig oversikt over AP-NO-importkjeda og korleis den forheld seg til FINT, oreg og andre domene.

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

**Arkitektoniske val:**
- `Standard`-klassen er definert her (ikkje i `dqv-ap-no`) for å unngå sirkulær import
- `har_kvalitetsmerknad` og `har_kvalitetsmaaling` er lagt direkte på `Datasett`
  her (får DQV-slots via import av `dqv-core`)
- Importerer `dqv-core-schema` (ikkje `dqv-ap-no-schema`) for å bryte sirkulær import

**Kjente avvik:** Ingen.

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

**Kjent avvik:**

| Kode | Avvik | Årsak |
|------|-------|-------|
| DQ5 | `har_maal.range: uriorcurie` (spec: `dcat:Resource`) | Bridge-arkitektur + LinkML-avgrensing 2 |

**Forklaring DQ5:** `dqv-core` kan ikkje referere til `KatalogisertRessurs` (finst i `dcat-ap-no` som importerer `dqv-core`). `dqv-ap-no` kan ikkje narrowe rangen via `slot_usage` utan å redeklarere `slots: [har_maal]`, som ville aktivere avgrensing 1. Praktisk validering fungerer då instansdata brukar URI-verdiar.

---

### `skos-ap-no` — Omgrep og begrepskatalog

**Fil:** `src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`  
**Spesifikasjon:** <https://informasjonsforvaltning.github.io/skos-ap-no-begrep/>

**Kjent avvik:**

| Kode | Avvik | Status |
|------|-------|--------|
| SK5 | Tospråkskrav (nb+nn) på `anbefalt_term` ikkje håndheva | Delvis løyst — `felles-begrepskatalog`-policy sjekkar `har_definisjon` |

**Forklaring SK5:** Full språktagging av `LangString` krev ein større refaktorering på tvers av AP-NO-profilane. Delvis realisert via `instance_check` i `felles-begrepskatalog`-policy.

---

### `xkos-ap-no` — Klassifikasjonar

**Fil:** `src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema.yaml`  
**Spesifikasjon:** <https://data.norge.no/specification/xkos-ap-no>

**Designval:** XKOS-AP-NO brukar `dct:temporal` (Tidsrom-mellomklasse) i staden for direkte `schema:validFrom`/`schema:validThrough` — for å harmonisere med DCAT-AP-NO-mønsteret.

**Kjente avvik:** Ingen.

---

### `modelldcat-ap-no` — Informasjonsmodellar

**Hovudfil (pass-through):** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`  
**Modell-del:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-modell-schema.yaml`  
**Katalog-del:** `src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml`  
**Spesifikasjon:** <https://data.norge.no/specification/modelldcat-ap-no>

**Arkitektonisk val:**

Skjemaet er delt i to filer for å matche spesifikasjonsstrukturen:
- `modelldcat-modell-schema` — alle Modellelement-klassane (27 klassar)
- `modelldcat-katalog-schema` — Modellkatalog, Informasjonsmodell, Dokument
- `modelldcat-ap-no-schema` — pass-through for bakoverkompatibilitet

`modelldcat-katalog` importerer `dcat-ap-no` og gjenbrukar hjelpeklassar (`Aktoer`, `Kontaktopplysning`, `Standard`, `Tidsrom`).

**Kjente avvik:** Ingen.

---

### `cpsv-ap-no` — Offentlege tenester

**Fil:** `src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml`  
**Spesifikasjon:** <https://informasjonsforvaltning.github.io/cpsv-ap-no/>

**Kjente avvik:** Ingen avvikskartlegging er gjennomført.

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
