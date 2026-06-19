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

### A6 — Import av `dcat-ap-no` i `modelldcat-ap-no` krev løysing av tre klassekollidjonar

`avvik-dqv-ap-no.md` er utført: `Standard` ligg no i `dcat-ap-no-schema.yaml`.
`modelldcat-ap-no` definerer framleis sin eigen parallelle `Standard`-klasse utan å
importere `dcat-ap-no`. Evaluering av moglege kollidjonar viser at A6 **ikkje kan
gjennomførast direkte** — tre klassar kolliderer:

| Klasse | modelldcat-ap-no | dcat-ap-no | Konflikt |
|---|---|---|---|
| `KatalogisertRessurs` | ikkje abstract | `abstract: true` | Flagg-konflikt |
| `Kontaktopplysning` | `vcard:Organization`, berre `id` | `vcard:Kind`, + `navn_vcard`, `har_epost`, `har_kontaktside` | **Alvorleg** — ulik `class_uri` og slots |
| `Standard` | slots: `versjonsnummer` (manglar `har_merknad`) | slots: `versjon`, `har_merknad` | Ulike slotnamn — løysing: harmoniser til `har_tittel` (obl.), `har_referanse` (anb.), `har_versjonsnummer` (valg.) |

`Kontaktopplysning`-konflikten er den alvorlegaste: ulik `class_uri` (`vcard:Organization`
vs `vcard:Kind`) vil gi ein hard feil i LinkML. `vcard:Kind` frå `dcat-ap-no` er meir korrekt
(superklasse — dekkjer fleire kontakttypar).

**Planlagde namneavhengigheiter som skapar nye konfliktar:**

`Tidsperiode` i `modelldcat-ap-no` skal omdøypast til `Tidsrom`, og `Aktor` i `dcat-ap-no`
skal omdøypast til `Aktoer`. Desse to renamingane er naudsynte for konsistent namngjeving,
men skapar kvar si nye kollisjon ved import:

| Rename | Ny kollisjon | Løysing |
|---|---|---|
| `Tidsperiode` → `Tidsrom` (modelldcat) | Slot-gap — modelldcat-versjonen manglar `begynnelse` og `slutt` | Fjern lokal definisjon, bruk dcat-versjonen |
| `Aktor` → `Aktoer` (dcat) | Slotnamn-konflikt — dcat brukar `navn_aktor`, modelldcat brukar `navn_aktoer` | Skriv om `navn_aktor` → `navn_aktoer` i `dcat-ap-no` |

`navn_aktor` i `dcat-ap-no` skal skrivast om til `navn_aktoer` (same translitteringskonvensjon
som i `modelldcat-ap-no`). Etter dette er begge klassar kompatible og den lokale
`Aktoer`-definisjonen i `modelldcat-ap-no` kan fjernast.

**Sirkulær importkjede:** `dcat-ap-no` importerer `dqv-ap-no`, og `dqv-ap-no` importerer
`dcat-ap-no` — dei to importerer kvarandre. Sirkulær avhengigheit vart truleg innført av
DQ1-fiksen og må løysast før A6 kan gjennomførast.

**Samla føresetnader for MC8 (5 punkt):**
1. Løys `Kontaktopplysning`: fjern lokal definisjon i `modelldcat-ap-no`, la `vcard:Kind`-varianten frå `dcat-ap-no` gjelde
2. Løys `KatalogisertRessurs`: fjern lokal definisjon i `modelldcat-ap-no`, la `abstract: true`-varianten gjelde
3. Løys `Standard`: harmoniser til éin felles definisjon med `har_tittel` (obligatorisk), `har_referanse` (anbefalt) og `har_versjonsnummer` (valgfri) — fjern `versjonsnummer`, `versjon` og `har_merknad` frå begge skjema
4. Løys `Aktoer`: skriv om `navn_aktor` → `navn_aktoer` i `dcat-ap-no-schema.yaml`
5. Løys sirkulær import mellom `dcat-ap-no` og `dqv-ap-no`

`Tidsrom`-konflikten løyser seg sjølv ved punkt 1–5: fjern den lokale `Tidsperiode`/`Tidsrom`-definisjonen og bruk `dcat-ap-no`-varianten (som har fleire slots, ikkje færre).

**Status:** 🚫 Blokkert — 5 føresetnader må løysast før import kan gjennomførast

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

**Status:** 🚫 Skal ikkje utførast — handsamast i MD2 (`avvik-veileder-modelldcat-ap-no.md`)

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

## Del C: Arkitekturvurdering — splitting av `modelldcat-ap-no-schema.yaml`

ModelDCAT-AP-NO-spesifikasjonen er eksplisitt delt i to delar:
- **Katalogdel** — `Modellkatalog` og `Informasjonsmodell` med tilhøyrande hjelpeklassar
- **Modelldel** — `Modellelement` og alle subklassar (`Objekttype`, `Attributt`, `Assosiasjon` osb.)

Spørsmålet er om `modelldcat-ap-no-schema.yaml` bør splittast tilsvarande.

### Grenselinje i skjemaet

Dei to delane er kopla via éin referanse:

```
Informasjonsmodell.inneholder_modellelement → Modellelement
```

`Modellelement`-hierarkiet (25+ klassar) brukar utelukkande `modelldcatno:`-namespace og
har **ingen overlapp** med klassar i `dcat-ap-no` eller `common-ap-no`. Katalogdelen
brukar `dcat:`- og `modelldcatno:`-namespace og har alle dei dokumenterte konfliktane
med `dcat-ap-no` (MC9).

### Importkjede etter splitting

```
common-ap-no
     ↓
dcat-ap-no          modelldcat-modell
     ↓    ↘               ↓
            modelldcat-katalog
```

`modelldcat-ap-no-modell` treng berre `linkml:types` og `common-ap-no`.
`modelldcat-ap-no-katalog` importerer `dcat-ap-no` + `modelldcat-modell`.

### Vurdering

| Argument | For splitting | Mot splitting |
|---|---|---|
| Spesifikasjonsstruktur | Matchar spec sin eigen todeling ✓ | |
| MC8/MC9 | Isolerer alle dcat-ap-no-konfliktar til katalogdelen ✓ | |
| Gjenbruk | Modelldelen kan importerast uavhengig ✓ | |
| Seam | Éin referanse (`inneholder_modellelement`) — reint skilje ✓ | |
| Filtal | | To skjema + to manifest i staden for eitt |
| Mønster | | Bryt «eitt skjema per standard»-mønsteret i repoet |

### Nye konfliktar ved splitting

Ingen. Modelldelen har null klassenamnoverlapp med `dcat-ap-no`. Splitten skapar
inga nye konfliktar — han reduserer konfliktscopet ved å isolere katalogdelen.

### Tilråding

**Splitting anbefalt.** Seamen er reint definert, modelldelen er fri for
AP-NO-konfliktar, og splitten løyser MC8/MC9 naturleg ved å avgrense `dcat-ap-no`-importen
til katalogdelen åleine. Domenemodeller som berre treng modellelementtypar (ikkje
katalogstrukturen) får òg ein lettare import.

**Sjå MC10.**

---

## Samandrag

| # | Avvik | Type | Prioritet |
|---|---|---|---|
| A1 | `Aktoer.navn_aktoer` manglar `required: true` | Schema | **Høg** |
| A2 | `Kontaktopplysning` manglar vCard-slots og har feil `class_uri` | Schema | **Høg** |
| A3 | `Lokasjon`-klassen ubrukt — `dekningsomraade.range: Konsept` | Schema | Middels |
| A4 | `Modellkatalog.har_del` feilaktig `required: true` | Schema | Middels |
| A5 | `Informasjonsmodell.type_concept` manglar vokabular-annotasjon | Annotasjon | Låg |
| A6 | Import av `dcat-ap-no` krev løysing av 3 klassekollidjonar + sirkulær import | Arkitektur | 🚫 Blokkert |
| B1 | Informasjonsmodell-instansar manglar `status`, datoar, versjon | Data | Middels |
| B2 | Berre 2/21+ skjema i modellkatalogen | Data | 🚫 Ikkje her — sjå MD2 |
| B3 | `Modellkatalog`-instansen manglar `tema` | Data | Låg |

---

## Tilrådde tiltak

### MC1 — Legg til `required: true` på `Aktoer.navn_aktoer` (A1) ✓

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

### MC2 — Utvid `Kontaktopplysning` med vCard-eigenskapar (A2) ✓

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

### MC3 — Kople `Lokasjon`-klassen til `dekningsomraade` eller slett henne (A3) ✓

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

### MC4 — Endre `Modellkatalog.har_del` til Anbefalt (A4) ✓

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

### MC5 — Legg til vokabular-annotasjon på `type_concept` (A5) ✓

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

### MC6 — Legg til silver-felt i `brreg-modellkatalog.yaml` (B1) ✓

Legg til `status`, `utgivelsesdato` og `endringsdato` på begge
`Informasjonsmodell`-instansane:

```yaml
informasjonsmodeller:
- id: https://brreg.no/modellkatalogar/brreg-modellkatalog/ngr-virksomhet
  ...
  status: http://purl.org/adms/status/UnderDevelopment
  utgivelsesdato: "2024-01-01"
  endringsdato: "2026-06-15"
  versjonsnummer: "1.0.0"
```

**Filer:** `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml`

---

### MC7 — Legg til `tema` på `Modellkatalog`-instansen (B3) ✓

Merk: den opphavlege spesifikasjonen brukte `naering-og-sysselsetting` som er ein ugyldig
Los-URI (404, retta i LO1). Korrekte verdiar er hovudtema `naring` og undertema `naringsliv`,
same mønster som i `brreg-begrepskatalog` (LO5).

```yaml
modellkataloger:
- id: https://brreg.no/modellkatalogar/brreg-modellkatalog
  ...
  tema:
  - https://psi.norge.no/los/tema/naring
  - https://psi.norge.no/los/tema/naringsliv
```

**Filer:** `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml`

---

### MC9 — Dokumenter og løys namne- og definisjonskonfliktar mellom AP-NO-profilane ✓ (delvis)

Kartlegginga av A6 avdekte at fleire hjelpeklassar er definert parallelt i
`modelldcat-ap-no-schema.yaml` og `dcat-ap-no-schema.yaml` med inkonsistente namn,
`class_uri`-val eller slots. Nedanfor er alle konfliktar og vedtekne val dokumenterte.

#### Klassenamn-konfliktar (krev rename)

| Klasse i modelldcat | Klasse i dcat | Vedteke val | Handling |
|---|---|---|---|
| `Tidsperiode` | `Tidsrom` | Bruk `Tidsrom` overalt | Rename i `modelldcat-ap-no` |
| `Aktoer` | `Aktor` | Bruk `Aktoer` overalt | Rename i `dcat-ap-no` |

#### Slotnamn-konfliktar (krev rename)

| Slot i modelldcat | Slot i dcat | Vedteke val | Handling |
|---|---|---|---|
| `navn_aktoer` | `navn_aktor` | Bruk `navn_aktoer` overalt | Rename i `dcat-ap-no` |

#### Klassestruktur-konfliktar (krev harmonisering)

| Klasse | modelldcat-definisjon | dcat-definisjon | Vedteke val |
|---|---|---|---|
| `KatalogisertRessurs` | ikkje abstract | `abstract: true` | Fjern lokal def., bruk dcat (`abstract: true`) |
| `Kontaktopplysning` | `vcard:Organization`, berre `id` | `vcard:Kind`, + `navn_vcard`, `har_epost`, `har_kontaktside` | Fjern lokal def., bruk dcat (`vcard:Kind`) |
| `Standard` | slots: `versjonsnummer` | slots: `versjon`, `har_merknad` | Harmoniser begge til `har_tittel` (obl.), `har_referanse` (anb.), `har_versjonsnummer` (valg.) — fjern `versjonsnummer`, `versjon`, `har_merknad` |
| `Tidsperiode`/`Tidsrom` | slots: `id, startdato, sluttdato` | slots: + `begynnelse`, `slutt` | Fjern lokal def., bruk dcat (dcat er eit supersett) |
| `Aktoer`/`Aktor` | `navn_aktoer`, ingen `required: true` | `navn_aktor`, `required: true` | Etter rename: fjern lokal def., bruk dcat |

#### Sirkulær importkjede

`dcat-ap-no` importerer `dqv-ap-no` og `dqv-ap-no` importerer `dcat-ap-no` — sirkulær avhengigheit.

**Vedteke val:** `dcat-ap-no` skal **ikkje** importere `dqv-ap-no`. Korrekt retning er
einveg: `dqv-ap-no → dcat-ap-no` (dqv-ap-no utvidar `Standard` frå dcat med DQV-spesifikke
slots). Fjern `- ../dqv-ap-no/dqv-ap-no-schema` frå `imports`-seksjonen i `dcat-ap-no-schema.yaml`.

**Blokkert:** Forsøk på å fjerne importen viser at `dcat-ap-no` faktisk brukar klassen
`Kvalitetsmerknad` og sloten `har_kvalitetsmaaling` frå `dqv-ap-no` (i `Datasett`-klassen,
DCAT-AP-NO-eigenskapar for datakvalitet). Importen kan difor ikkje fjernast utan at desse
eigenskapane vert flytta — anten til `common-ap-no` eller til ei eiga bru-schema. Dette krev
ein eigen spesifikasjon.

**Filer:**
- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`
- `src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema.yaml`

**Avhengigheit:** MC9 er føresetnad for MC8.

---

### MC10 — Split `modelldcat-ap-no-schema.yaml` i katalog- og modelldel ✓

✓ Utført 2026-06-19. Skjemaet er delt i to nye filer:

```
src/linkml/ap-no/modelldcat-ap-no/
  modelldcat-modell-schema.yaml    ← Modellelement + alle subklassar + modellelement-slots
  modelldcat-katalog-schema.yaml   ← Modellkatalog + Informasjonsmodell + hjelpeklassar + katalog-slots
  modelldcat-ap-no-schema.yaml     ← pass-through (importerer katalog-schema)
```

**`modelldcat-modell-schema.yaml`** importerer:
- `linkml:types`
- `../common/common-ap-no-schema`
(Definerer óg `begrep`-slot sidan det vert brukt av både Modellelement og katalogklassar via importkjeda.)

**`modelldcat-katalog-schema.yaml`** importerer:
- `linkml:types`
- `../common/common-ap-no-schema`
- `./modelldcat-modell-schema`
(Importen av `../dcat-ap-no/dcat-ap-no-schema` er ikkje lagt til enno — det er MC8.)

**`modelldcat-ap-no-schema.yaml`** er gjort om til pass-through som berre importerer `modelldcat-katalog-schema`.
`brreg-modellkatalog-schema.yaml` er ikkje endra — det importerer framleis `modelldcat-ap-no-schema` via pass-through.

Lint: berre forventa `dct` canonical-prefix-åtvaring (same som original). Instansvalidering av `brreg-modellkatalog-eksempel.yaml` er OK.

**Filer:** `src/linkml/ap-no/modelldcat-ap-no/`
**Avhengigheit:** Bør gjerast før MC9 og MC8 for å avgrense omfanget av harmoniseringa.

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Status |
|---|---|---|---|
| 1 | MC1: `required: true` på `Aktoer.navn_aktoer` | `modelldcat-katalog-schema.yaml` | ✓ |
| 2 | MC2: Utvid `Kontaktopplysning` med vCard-slots | `modelldcat-katalog-schema.yaml` | ✓ |
| 3 | MC3: Fjern `Lokasjon`-klassen | `modelldcat-katalog-schema.yaml` | ✓ |
| 4 | MC4: `Modellkatalog.har_del` → Anbefalt | `modelldcat-katalog-schema.yaml` | ✓ |
| 5 | MC5: Vokabular-annotasjon på `type_concept` | `modelldcat-katalog-schema.yaml` | ✓ |
| 6 | MC6: Silver-felt på Informasjonsmodell-instansar | `brreg-modellkatalog.yaml` | ✓ |
| 7 | MC7: `tema` på Modellkatalog-instans | `brreg-modellkatalog.yaml` | ✓ |
| 8 | MC10: Split i `modelldcat-modell` og `modelldcat-katalog` | `modelldcat-ap-no/` | ✓ |
| 9 | MC9: Harmoniser klassenamn, slotnamn og struktur | fleire filer | ✓ (delvis) |
| 10 | MC11: Løys sirkulær import dcat-ap-no ↔ dqv-ap-no | `dqv-ap-no/`, `dcat-ap-no/` | ✓ |
| 11 | MC8: Importer `dcat-ap-no` i `modelldcat-katalog`, fjern lokale duplikatklassar | `modelldcat-katalog-schema.yaml` | ✓ |

---

## MC11 — Løysing av sirkulær import dcat-ap-no ↔ dqv-ap-no ✓

✓ Utført 2026-06-19.

**Problem:** `dcat-ap-no` importerte `dqv-ap-no` (for å bruke `Kvalitetsmerknad` og `har_kvalitetsmaaling`/`har_kvalitetsmerknad` på `Datasett`). `dqv-ap-no` importerte `dcat-ap-no` (for `KatalogisertRessurs` og `Standard`). Sirkulær import.

**Analyse av alternativer:**
- *Alternativ A (klasse-override i dqv-ap-no)*: Fjerne dqv-import frå dcat-ap-no og leggje DQV-slots til `Datasett` via klasseoverride i dqv-ap-no. Fungerer IKKJE — LinkML sine klasseoverrides med `slots:` erstattar foreldrelistа i JSON-skjemavalidering, og alle baseklasseegenskapar vert usynlege for validatoren. Denne LinkML-avgrensinga er stadfesta og gjeld allereie `Standard`-overriden i dqv-ap-no (pre-eksisterande bug).
- *Alternativ B (bridge-fil, valt)*: Trekk ut alle DQV-kjerneklassar til ei ny `dqv-core-schema.yaml` utan referansar til dcat-klasser. `dcat-ap-no` importerer `dqv-core`. `dqv-ap-no` importerer `dcat-ap-no` (som har dqv-core transitivt).

**Implementert løysing — importkjede:**
```
common-ap-no → dqv-core → dcat-ap-no → dqv-ap-no
```

**Filer oppretta/endra:**

`src/linkml/ap-no/dqv-ap-no/dqv-core-schema.yaml` (ny):
- Alle DQV-klasser (Kvalitetsdimensjon, Kvalitetsdeldimensjon, Kvalitetsmaal, Kvalitetsmerknad, Brukartilbakemelding, Kvalitetssertifikat, Kvalitetsmaaling, Tekstdel) og -slots
- `har_maal.range: uriorcurie` (ikkje `KatalogisertRessurs`) — einaste avvik frå dqv-ap-no
- `DqvMotivasjon`-enum
- Importerer berre `common-ap-no`, ingen dcat-avhengigheit

`src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`:
- Importerer `../dqv-ap-no/dqv-core-schema` (i staden for `dqv-ap-no-schema`)
- `Datasett` beheld `har_kvalitetsmerknad` og `har_kvalitetsmaaling` som før — ingen endring i slotlisteа

`src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml`:
- Alle DQV-klasser og -slots fjerna (flytta til dqv-core)
- `DqvMotivasjon`-enum fjerna (flytta til dqv-core)
- Beheld `Standard`-override med `er_i_kvalitetsdimensjon` (pre-eksisterande, uendra)
- Importerer framleis `dcat-ap-no` (gjer dqv-core tilgjengeleg transitivt)

**Kjend avgrensing:** `har_maal.range` er `uriorcurie` i dqv-core, ikkje `KatalogisertRessurs`. Å narrowe rangen i dqv-ap-no via slot_usage er ikkje mogleg utan `slots:` i overriden (lintarfeil `no_invalid_slot_usage`). Sidan instansdata alltid brukar URI-verdiar passerer validering for begge range-typane. `Standard`-override-buggen (pre-eksisterande) er uendra.

---

## Avhengigheiter og krysstilvisingar

- **MD2** (`avvik-veileder-modelldcat-ap-no.md`): Utvid modellkatalogen til å
  dekkje alle skjema i repoet — koordiner med MC6
- **DQ1** (`avvik-dqv-ap-no.md`): ✓ Utført — `Standard`-klassen er flytta til `dcat-ap-no`.
  `modelldcat-ap-no` må no importere `dcat-ap-no` for å dele klassedefinisjon (MC8)

**Merk:** `modelldcat-ap-no-schema.yaml` importerer `common-ap-no-schema` allereie
(via `imports: - ../common/common-ap-no-schema`), så `navn_vcard`, `har_epost`
og `har_kontaktside` er tilgjengelege utan endringar i imports.

---

## Utført

Utført 2026-06-19. MC8 er ikkje gjennomført og vert flytta til eige backlog-punkt.

**Gjennomførte tiltak:**

- **MC1** — `Aktoer.navn_aktoer` → `required: true` i `modelldcat-katalog-schema.yaml`
- **MC2** — `Kontaktopplysning` utvida med `navn_vcard` (`vcard:fn`), `har_epost` (`vcard:hasEmail`), `har_kontaktside` (`vcard:hasURL`)
- **MC3** — `Lokasjon`-klassen fjerna (var definert men aldri referert)
- **MC4** — `Modellkatalog.har_del` endra frå feilaktig `required: true` til `in_subset: [Anbefalt]`
- **MC5** — `Informasjonsmodell.type_concept` fått `gyldige_verdier`-annotasjon med ModelDCAT-AP-NO-vokabular-URI-ar
- **MC6** — `brreg-modellkatalog.yaml`: silver-annotasjonar (`utgiver`, `endringsdato`, `status`, m.fl.) lagt til på alle `Informasjonsmodell`-instansar
- **MC7** — `Modellkatalog`-instansen fått `tema`-verdi (Los)
- **MC9** — Klassenamn og slotnamn harmonisert med `dcat-ap-no` der mogleg (`Aktoer` → `foaf:Agent`, `Tidsrom` → `dct:PeriodOfTime`, `Kontaktopplysning` → `vcard:Kind`). Delvis: `Standard`- og `Lisensdokument`-klassane er dupliserte — slåast saman i MC8.
- **MC10** — `modelldcat-ap-no-schema.yaml` delt i `modelldcat-modell-schema.yaml` (27 Modellelement-klassar) og `modelldcat-katalog-schema.yaml` (Modellkatalog, Informasjonsmodell, hjelpeklassar). Originalen er pass-through for bakoverkompatibilitet.
- **MC11** — Sirkulær import `dcat-ap-no` ↔ `dqv-ap-no` løyst med ny `dqv-core-schema.yaml` (bridge-fil). `har_maal.range` forblir `uriorcurie` pga. LinkML-avgrensing (`no_invalid_slot_usage`).

- **MC8** — Import av `dcat-ap-no` i `modelldcat-katalog-schema.yaml`. Fjerna 5 duplikatklassar (`KatalogisertRessurs`, `Aktoer`, `Kontaktopplysning`, `Standard`, `Tidsrom`) og 10 duplikatslotar (`naam_aktoer`, `naam_vcard`, `har_epost`, `har_kontaktside`, `startdato`, `sluttdato`, `utgiver`, `produsent`, `kontaktpunkt`, `temaer`). Beheld lokal definisjon av 4 slots med avvikande range frå dcat-ap-no: `lisens` (Lisensdokument), `tema` (Konsept), `har_del` (KatalogisertRessurs), `erstatter` (Informasjonsmodell). `vcard:`-prefikset fjerna (ikkje lenger nødvendig). Lint: 0 nye problem. Instansvalidering: OK.
