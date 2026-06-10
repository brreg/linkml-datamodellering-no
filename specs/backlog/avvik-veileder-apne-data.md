# Kartlegging: Avvik mot Veileder for tilgjengeliggjøring av åpne data

**Kjelde:** [data.norge.no/guide/veileder-apne-data](https://data.norge.no/guide/veileder-apne-data)  
**Utgitt av:** Digitaliseringsdirektoratet (Digdir), oppdatert 2026-01-23  
**Lisens:** CC BY 4.0

---

## Bakgrunn

Digdirs rettleiar definerer 15 krav/anbefalingar (frå regjeringas *Retningslinjer ved
tilgjengeliggjøring av offentlige data*) som offentlege verksemder skal følgje når dei
tilbyr åpne data. Dette repoet publiserer informasjonsmodellar og begrepsdata som åpne
data — rettleiaren gjeld difor òg her.

Kartlegginga nedanfor går gjennom kvart av dei 15 punkta og vurderer om repoet er i
samsvar, har eit delvis avvik eller eit fullstendig avvik. Prioriterte tiltak er lista til
slutt.

---

## Kartlegging av avvik

### Punkt 1 — Bruk åpne standardlisenser

**Krav:** Data skal ha klare vilkår for bruk. Digdir anbefaler CC0 eller CC BY 4.0.
Lisens skal angis i samsvar med DCAT-AP-NO (`dct:license`) og synleggjørast på portalen.

| Kilde | Status | Merknad |
|---|---|---|
| LinkML-skjema (`.yaml`) | ⚠️ Avvik | Ingen `dct:license`-annotasjon i skjemametadata |
| Portalen (GitHub Pages) | ⚠️ Avvik | Ingen synleg lisenserklæring på portalen |
| Modellkatalog-instansar | ⚠️ Avvik | `modelldcat-ap-no` har `dct:license`-slot, men det er ikkje fylt ut |
| Begrepskatalog-instansar | ⚠️ Avvik | Same som modellkatalog |

**Tiltak:** Legg til `dct:license`-annotasjon i skjemametadata (silver-policy) og legg til
lisenserkæring på portalen. CC BY 4.0 er naturleg val for denne typen modelldata.

---

### Punkt 2 — Tilby data gratis

**Krav:** Data skal vere gratis.

| Status | Merknad |
|---|---|
| ✅ Samsvar | GitHub Pages og GitHub Releases er gratis og ope tilgjengeleg |

---

### Punkt 3 — Tilby data uten brukerregistrering

**Krav:** Data skal vere tilgjengeleg utan at brukaren must søkje om løyve eller registrere seg.

| Status | Merknad |
|---|---|
| ✅ Samsvar | GitHub Pages krev ingen innlogging |

---

### Punkt 4 — Dokumenter datasettene

**Krav:** Beskrivingar skal gjere det mogleg å oppdage, forstå og bruke data — for både
menneske og maskiner. For API-ar anbefaler rettleiaren OpenAPI Specification.

| Kilde | Status | Merknad |
|---|---|---|
| Portalen | ✅ Samsvar | Portalen har menneskeleseleg dokumentasjon per skjema |
| OpenAPI-spesifikasjonar | ⚠️ Delvis | Generert for skjema med `openapi: true`, men flagget er `false` som standard |
| Maskinlesbar katalogoversikt | ⚠️ Avvik | Ingen `catalog.json` eller tilsvarende maskinlesbar oversikt over alle skjema |
| Registrering på data.norge.no | ⚠️ Delvis | Berre skjema med `publish_external: true` registrerast via modellkatalogen |

---

### Punkt 5 — Tilby informasjon om datakvalitet

**Krav:** Datakvalitet bør dokumenterast, kjente utfordringar skal nemnast eksplisitt.
DQV-AP-NO er det relevante rammeverket.

| Status | Merknad |
|---|---|
| ⚠️ Avvik | Bronze/silver/gold-policy dekker *skjemakvalitet*, ikkje *datakvalitet* i DQV-forstand |
| ⚠️ Avvik | Repoet har `dqv-ap-no`-skjema, men brukar det ikkje til å beskrive eigen datakvalitet |
| ⚠️ Avvik | Kjente feil er dokumenterte i `specs/bugs/`, men er ikkje eksponerte i skjemametadata |

**Tiltak:** Vurder å leggje til `dqv:hasQualityAnnotation` eller tilsvarende i skjemametadata,
t.d. med referanse til kjent mangel/avvik.

---

### Punkt 6 — Tilby oppdaterte data

**Krav:** Verksemda bør tilby oppdaterte data og vere tydeleg på oppdateringsfrekvens.

| Status | Merknad |
|---|---|
| ✅ Samsvar | GitHub Pages vert oppdatert automatisk ved kvar push til `main` |
| ⚠️ Delvis | `annotations.endringsdato` er påkravd ved silver/gold, men oppdateringsfrekvens er ikkje eksponert som metadata |
| ⚠️ Avvik | Ingen `dct:accrualPeriodicity` i skjemametadata |

---

### Punkt 7 — Gjør data synlige

**Krav:** Beskrivingar av datasett skal vere tilgjengelege på data.norge.no.
Rettleiaren anbefaler òg engelske beskrivingar.

| Status | Merknad |
|---|---|
| ⚠️ Delvis | Berre skjema med `publish_external: true` er synlege på data.norge.no |
| ⚠️ Avvik | Fleste skjema har berre `publish_external: false` og er ikkje registrerte nokon stad utanfor portalen |
| ⚠️ Avvik | Alle skildringer er på norsk bokmål — ingen engelske omsetjingar |

---

### Punkt 8 — Bruk maskinlesbare og standardiserte formater

**Krav:** Data skal vere i maskinlesbare og standardiserte formater (CSV, XML, JSON, RDF-serialiseringar).

| Status | Merknad |
|---|---|
| ✅ Samsvar | JSON Schema, JSON-LD, SHACL, OWL, RDF/Turtle, XSD, OpenAPI, AsyncAPI, Protobuf — svært god formatdekning |

---

### Punkt 9 — Tilby data gjennom et programmeringsgrensesnitt

**Krav:** API gjer det mogleg for programvare å gjere oppslag direkte. Rettleiaren
anbefaler REST-API med OpenAPI-dokumentasjon og Semantic Versioning.

| Status | Merknad |
|---|---|
| ⚠️ Delvis | OpenAPI-spesifikasjonar vert generert, men berre for skjema med `openapi: true` (standard: false) |
| ⚠️ Avvik | Det finst ikkje noko live querybart API — berre statiske filer på GitHub Pages |
| ⚠️ Avvik | `raw.githubusercontent.com`-tilgangen er funksjonell men udokumentert som offisiell API-overflate |

**Merknad:** For informasjonsmodeller er statiske filer på faste URL-ar eit akseptabelt
alternativ til live API, men det bør dokumenterast eksplisitt.

---

### Punkt 10 — Tilby komplett nedlasting

**Krav:** Brukare skal kunne laste ned komplette datasett.

| Status | Merknad |
|---|---|
| ✅ Samsvar | Alle artefaktar er tilgjengelege som nedlastbare filer på GitHub Pages og GitHub Releases |

---

### Punkt 11 — Bruk faste adresser og unike identifikatorer

**Krav:** Data skal ha unike, permanente og hensiktsmessige adressar. Versionar og
dataelement bør vere adresserbare.

| Status | Merknad |
|---|---|
| ✅ Samsvar | Kvart skjema har `id`-felt med absolutt HTTPS-URL |
| ✅ Samsvar | GitHub Releases gir stabile versjonerte nedlastings-URL-ar |
| ⚠️ Delvis | GitHub Pages-URL-ar er stabile, men utan eksplisitt versjonssegment — `https://brreg.github.io/…/samt-bu/` peikar alltid til siste versjon |
| ⚠️ Avvik | Ingen dedikerte versjonerte URL-ar for eldre versjonar av artefaktar via GitHub Pages |

---

### Punkt 12 — Publiser oversikt over virksomhetens data

**Krav:** Verksemda bør vedlikehalde og publisere ei oversikt over kva data dei forvaltar —
òg for data som ikkje er tilgjengelege enno. Oversikten må vere maskinlesbar (DCAT-AP-NO).

| Status | Merknad |
|---|---|
| ✅ Samsvar | Portalen listar alle skjema med menneskeleseleg oversikt |
| ⚠️ Avvik | Ingen maskinlesbar katalogoversikt (t.d. `catalog.json` eller DCAT-katalog) som dekker *alle* skjema |
| ⚠️ Avvik | Skjema med `publish_external: false` er ikkje registrerte på data.norge.no, sjølv om dei er offentlege |

---

### Punkt 13 — Tilpass data til brukernes behov

**Krav:** Data bør tilpassast slik at brukarar enkelt kan ta dei i bruk.

| Status | Merknad |
|---|---|
| ✅ Samsvar | Mange format (JSON Schema, Python, Protobuf, OpenAPI osb.) dekker ulike brukargrupper |
| ⚠️ Delvis | Bootstrap-scriptet gjer det enklare å bruke AP-NO-profilene ekstern, men det er ikkje tydeleg dokumentert kva format som er meint for kva brukargruppe |

---

### Punkt 14 — Oppmuntre til bruk

**Krav:** Utgivarar bør samhandle med brukarar og aktivt oppmuntre til bruk.

| Status | Merknad |
|---|---|
| ⚠️ Delvis | Bootstrap-scriptet og portalen er passive tiltak |
| ⚠️ Avvik | Ingen aktiv promotering, workshops, hackathon-deltaking eller brukarundersøkingar |

---

### Punkt 15 — Legg til rette for tilbakemeldinger

**Krav:** Brukare skal kunne gje tilbakemeldingar. Verksemda skal ha rutinar for å følgje
opp innspel.

| Status | Merknad |
|---|---|
| ⚠️ Delvis | GitHub Issues er tilgjengeleg, men er ikkje eksplisitt vist fram på portalen som tilbakemeldingskanal |
| ⚠️ Avvik | Ingen kontaktinfo, e-postadresse eller dedikert tilbakemeldingsside på portalen |

---

## Samandrag av avvik

| # | Punkt | Status | Prioritet |
|---|---|---|---|
| 1 | Åpne standardlisenser | ⚠️ Avvik | Høg |
| 2 | Data gratis | ✅ | — |
| 3 | Uten registrering | ✅ | — |
| 4 | Dokumentasjon av datasett | ⚠️ Delvis | Høg |
| 5 | Datakvalitet | ⚠️ Avvik | Middels |
| 6 | Oppdaterte data | ⚠️ Delvis | Låg |
| 7 | Synlegheit på data.norge.no | ⚠️ Delvis | Høg |
| 8 | Maskinlesbare format | ✅ | — |
| 9 | Programmeringsgrensesnitt | ⚠️ Delvis | Middels |
| 10 | Komplett nedlasting | ✅ | — |
| 11 | Faste adresser og identifikatorar | ⚠️ Delvis | Middels |
| 12 | Oversikt over data | ⚠️ Avvik | Høg |
| 13 | Tilpassing til brukarar | ⚠️ Delvis | Låg |
| 14 | Oppmuntre til bruk | ⚠️ Delvis | Låg |
| 15 | Tilbakemeldingar | ⚠️ Delvis | Middels |

---

## Tilrådde tiltak

### Høg prioritet

**T1 — Lisens i skjema og på portal (Punkt 1)**
- Legg til `annotations.lisens` i silver-policy-krava (saman med utgjevar, endringsdato osb.)
- Legg til `dct:license: https://creativecommons.org/licenses/by/4.0/` i alle silver/gold-skjema
- Legg til lisensfooter på portalen (`mkdocs/docs/`)

**T2 — Maskinlesbar katalogoversikt (Punkt 4, 12)**
- Generer `catalog.json` til GitHub Pages med metadata om alle skjema
  (namn, tittel, versjon, format-URL-ar, policy, status)
- Vurder å generere ein full DCAT-katalog (`catalog.ttl`) som data.norge.no kan hauste

**T3 — Synlegheit på data.norge.no for fleire skjema (Punkt 7)**
- Vurder om fleire skjema bør ha `publish_external: true`
- Publiserte modellkatalog-oppslag bør ha `dct:license` satt (sjå T1)

### Middels prioritet

**T4 — Tilbakemeldingskanal synleg på portalen (Punkt 15)**
- Legg til kontaktinfo / GitHub Issues-lenke i portalens footer eller «Om»-side

**T5 — Versjonerte URL-ar (Punkt 11)**
- Vurder om GitHub Releases-URL-ar bør dokumenterast som kanoniske adressar for
  historiske versjonar, i tillegg til GitHub Pages (som alltid peikar til siste)

**T6 — OpenAPI aktivert for fleire skjema (Punkt 9)**
- Vurder å sette `openapi: true` som standard for skjema med `publish_external: true`
  for å oppfylle rettleiarens krav om API-dokumentasjon

**T7 — Oppdateringsfrekvens i metadata (Punkt 6)**
- Legg til `dct:accrualPeriodicity` i silver-annotasjonar

### Låg prioritet

**T8 — Engelske beskrivingar (Punkt 7)**
- Vurder å leggje til `title_en` og `description_en` i skjemametadata for internasjonalt
  synlege skjema

**T9 — Tilbakemeldingsrutinar (Punkt 14, 15)**
- Opprett ein enkel `CONTRIBUTING.md` eller portalside som forklarer korleis brukarar
  kan gje innspel og korleis dei vert handsama

---

## Prioritert handlingsliste

| # | Tiltak | Fil / område | Avhengigheit |
|---|---|---|---|
| 1 | T1: Lisens i silver-policy og portal | `mcp-linkml-validator/policies/`, `mkdocs/docs/` | — |
| 2 | T2: Generer `catalog.json` til GitHub Pages | `src/assets/scripts/gen-catalog-manifest.py`, `generate.yml` | — |
| 3 | T3: Gjennomgå `publish_external` for fleire skjema | Alle `manifest.yaml` | T1 (lisens bør vere på plass) |
| 4 | T4: Tilbakemeldingskanal på portal | `mkdocs/docs/` | — |
| 5 | T5: Dokument versjonerte URL-ar | `mkdocs/docs/` | — |
| 6 | T6: OpenAPI default for `publish_external: true` | `manifest.yaml`-malen, dokumentasjon | — |
| 7 | T7: `dct:accrualPeriodicity` i silver | `mcp-linkml-validator/policies/` | T1 |
| 8 | T8: Engelske beskrivingar | Skjema, portal | — |
| 9 | T9: CONTRIBUTING.md / tilbakemeldingsside | `mkdocs/docs/` | — |

---

## Avhengigheiter

- T1 bør gjennomførast før T3 sidan `dct:license` er ein DCAT-AP-NO-føresetnad for
  registrering på data.norge.no
- T2 (`catalog.json`) er grunnlag for maskinlesbar oppdaging og er uavhengig av dei andre
  tiltaka — kan gjennomførast raskt
