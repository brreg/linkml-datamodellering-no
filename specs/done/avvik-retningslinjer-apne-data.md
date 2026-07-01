# Kartlegging: Avvik mot Retningslinjer ved tilgjengeliggjøring av offentlige data

**Kjelde:** [regjeringen.no/id2536870](https://www.regjeringen.no/no/dokumenter/retningslinjer-ved-tilgjengeliggjoring-av-offentlige-data/id2536870/)  
**Utgjevar:** Kommunal- og moderniseringsdepartementet  
**Status:** Tilrådde retningslinjer (ikkje forskrift)  
**Primær implementasjon i repoet:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

---

## Bakgrunn

Retningslinjene er ei *politisk* styringsdokument — dei krev at offentlege verksemder
tilgjengeleg-gjer data på ein konkret måte, men er ikkje ein teknisk dataspesifikasjon.
Formålet med denne kartlegginga er å vurdere i kva grad `dcat-ap-no-schema.yaml`
gjev *god infrastruktur for at implementørar kan etterleve* dei 15 retningslinjene.

Dei fleste retningslinjene gjeld prosess og organisering — dei kan ikkje modellerast i
eit schema. Kartlegginga fokuserer difor på tre typar avvik:

1. **Subset-avvik** — felt som bør vere Anbefalt/Obligatorisk, men er Valgfri
2. **Manglande annoteringar** — felt utan dokumentasjon av tilrådde verdiar
3. **Manglande slots** — felt retningslinjene impliserer, som ikkje finst i schema

---

## Evaluering (2026-06-20)

Kartlegginga vart kontrollert på nytt mot dagens
`src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`:

- **7 av 8 avvik er fortsatt gjeldande** — ingen endring sidan kartlegginga vart skrive.
- **Avvik 2 (`frekvens`) er delvis løyst.** DA4 i `specs/done/avvik-dcat-ap-no.md`
  la `frekvens` til i `slots:`-lista på `Datasett` (sjå linje 336 i schema), men
  sette **ikkje** `in_subset: Anbefalt` i `slot_usage`. Slottet finst altså no,
  men er klassifisert som Valgfri, ikkje Anbefalt som retningslinje 6 krev.
  RÅ2 er dermed redusert til berre subset-justeringa — sjå oppdatert seksjon under.

---

## Dei 15 retningslinjene — status per repoet

| # | Retningslinje | Schema-støtte | Avvik |
|---|---|---|---|
| 1 | Åpne standardlisenser (CC BY 4.0 / NLOD) | `lisens` finst (Anbefalt) | Subset for laus; ingen tilrådde verdiar |
| 2 | Gratis tilgjenge | Ingen `pris`-slot | Ikkje modellerbart |
| 3 | Ingen brukarregistrering | `tilgangsrettigheter` finst (Anbefalt) | Ingen tilrådde verdiar dokumentert |
| 4 | Dokumentasjon av datasett | `dokumentasjon`, `landingsside` er Valgfri | For laus subset |
| 5 | Datakvalitetsinformasjon | `har_kvalitetsmerknad` er Anbefalt ✓ | — |
| 6 | Oppdaterte data / oppdateringsfrekvens | `frekvens` manglar på `Datasett` | Stort avvik |
| 7 | Synlegheit på data.norge.no | Prosessretningslinje | Ikkje modellerbart |
| 8 | Maskinlesbare format | `format`, `medietype` Anbefalt ✓ | Ingen formatguide |
| 9 | Programmeringsgrensesnitt (API) | `Datatjeneste` er modellert ✓ | — |
| 10 | Fullstendig nedlasting | `nedlastningslenke` er Valgfri | For laus subset |
| 11 | Faste adresser og unike identifikatorar | `identifikator_literal` er Valgfri | For laus subset |
| 12 | Oversikt over eigna data | `Katalog` finst ✓ | Ikkje-opna datasett usynlege |
| 13 | Tilpassing til brukarbehov | Fleire `Distribusjon`ar mogleg ✓ | — |
| 14 | Aktiv oppmuntring | Prosessretningslinje | Ikkje modellerbart |
| 15 | Tilbakemeldingssystem | Prosessretningslinje | Ikkje modellerbart |

---

## Kartlegging av avvik

### 1 — `lisens` er Anbefalt — bør vere Obligatorisk på `Distribusjon`

Retningslinje 1 seier: bruk CC BY 4.0 eller NLOD — open lisens er eit
minimumskrav for offentlege data som tilgjengeleggjerast.

`lisens` (`dct:license`) er i dag merka som `Anbefalt` på `Distribusjon`,
`Katalog` og `Datatjeneste`. For offentlege datasett er mangel på lisens
ei alvorleg etterlevelsesbrist mot retningslinjene.

I tillegg manglar `lisens`-sloten ei `annotations.gyldige_verdier`-markering
som dokumenterer at NLOD og CC BY 4.0 er dei to tilrådde verdiane.

**Tilrådde NLOD-URI-ar (eksempel):**
```
https://data.norge.no/nlod/no/2.0
https://creativecommons.org/licenses/by/4.0/
```

**Status:** ⚠️ Subset-avvik + manglande annotasjon — høg prioritet

---

### 2 — `frekvens` er Valgfri på `Datasett`

Retningslinje 6 krev at oppdateringsfrekvens er tydeleg oppgjeve.

`frekvens` (`dct:accrualPeriodicity`) var opphavleg berre modellert på
`Datasettserie`. **DA4** i `specs/done/avvik-dcat-ap-no.md` la sloten til i
`slots:`-lista på `Datasett`, men ingen `in_subset`-klassifisering vart sett —
sloten er dermed Valgfri i dag, ikkje Anbefalt.

For å etterleve retningslinje 6 bør `frekvens` på `Datasett` vere Anbefalt.

**Status:** ⚠️ Subset-avvik (delvis løyst — slot finst, klassifisering manglar) — høg prioritet  
**Sjå:** DA4 i `specs/done/avvik-dcat-ap-no.md`

---

### 3 — `nedlastningslenke` er Valgfri — bør vere Anbefalt

Retningslinje 10 krev at det alltid er mogleg å laste ned eit komplett datasett
(anten via API eller maskinlesbar fil).

`nedlastningslenke` (`dcat:downloadURL`) er i dag Valgfri på `Distribusjon`.
For distribusjonar som representerer nedlastbare filer (CSV, JSON, RDF osb.)
bør denne vere Anbefalt.

Merk at `tilgangs_url` er Obligatorisk og kan peke på same ressurs, men
retningslinjene legg vekt på *direkte nedlasting* (`dcat:downloadURL`) for
maskinell bruk.

**Status:** ⚠️ Subset-avvik — middels prioritet

---

### 4 — `dokumentasjon` og `landingsside` er Valgfri på `Datasett`

Retningslinje 4 krev skildringar som gjer det mogleg for «både menneske og
maskin å oppdaga, forstå og bruka data».

I dag er:
- `dokumentasjon` (`foaf:page`) Valgfri på `Datasett`
- `landingsside` (`dcat:landingPage`) Valgfri på `Datasett`

For offentlege datasett som tilgjengeleggjerast er ei landingsside eit naturleg
krav for menneskefiendt oppdagbarheit. Begge bør supplerast til Anbefalt.

**Status:** ⚠️ Subset-avvik — middels prioritet

---

### 5 — `identifikator_literal` er Valgfri på `Datasett`

Retningslinje 11 krev permanente URL-ar og standardiserte identifikatorar
slik at datasett kan refereras til på tvers av system.

`identifikator_literal` (`dct:identifier`) er i dag Valgfri på `Datasett`.
For offentlege datasett bør ein stabil, offentleg URI (t.d. på data.norge.no)
vere Anbefalt.

Merk at `id`-feltet (LinkML `identifier: true`) alltid krevst — men dette
er ein intern LinkML-mekanisme, ikkje nødvendigvis den stabile URI-en som
er eksponert mot omverda.

**Status:** ⚠️ Subset-avvik — middels prioritet

---

### 6 — `tilgangsrettigheter` manglar dokumentasjon av tilrådde verdiar

Retningslinje 3 krev at data er tilgjengeleg utan brukarregistrering. Det
primære DCAT-verktøyet for dette er `dct:accessRights` med EU sitt
Access Rights-vokabular:

| URI | Tydning |
|---|---|
| `http://publications.europa.eu/resource/authority/access-right/PUBLIC` | Ope — ingen registrering |
| `http://publications.europa.eu/resource/authority/access-right/RESTRICTED` | Avgrensa tilgang |
| `http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC` | Ikkje offentleg |

`tilgangsrettigheter`-sloten (`dct:accessRights`, `range: uri`) manglar
`annotations.gyldige_verdier` som dokumenterer desse URI-ane.

**Status:** ⚠️ Manglande annotasjon — middels prioritet

---

### 7 — Ikkje-opna datasett kan ikkje katalogiserast med forklaring

Retningslinje 12 seier at «virksomheter bør publisere oversikt over hva slags
data de forvalter, inkludert datasett som ikke er tilgjengeliggjort».

Det finst ingen etablert mekanisme i schema for å modellere *kvifor* eit
datasett ikkje er opna (t.d. personopplysningar, forretningshemmelegheiter,
pågåande anonymisering).

`tilgangsrettigheter: NON_PUBLIC` på `Datasett` kombinert med
`har_kvalitetsmerknad` er den næraste tilnærminga, men det er inga dedikert
eigenskap for «grunnen til at datasettet er unntatt».

`dct:conformsTo` på `Datasett` kan peike på eit unntak-vokabular, men dette
er ikkje standard.

**Status:** ⚠️ Strukturgap — låg prioritet (ikkje dekka av DCAT-AP-NO-spec heller)

---

### 8 — Ingen formatrettleiing mot maskinlesbare standardformat

Retningslinje 8 anbefaler CSV, XML, JSON og RDF-serialisering.

`format` (`range: string`, annotasjon `gyldige_verdier: dct:MediaType`) og
`medietype` (`range: Mediatype`) er Anbefalt på `Distribusjon`, men det er
ingen dokumentasjon i schema om kva format-URI-ar som svarar til dei
tilrådde formata.

Eksempel på manglande URI-er:
```
text/csv              → CSV
application/json      → JSON
application/xml       → XML
application/rdf+xml   → RDF/XML
text/turtle           → Turtle
application/ld+json   → JSON-LD
```

**Status:** ⚠️ Manglande annotasjon — låg prioritet

---

## Samandrag

| # | Avvik | Type | Prioritet |
|---|---|---|---|
| 1 | `lisens` Anbefalt (ikkje Obligatorisk) + ingen tilrådde verdiar | Subset + annotasjon | **Høg** |
| 2 | `frekvens` er Valgfri på `Datasett` (slot finst, DA4 utført) | Subset | **Høg** |
| 3 | `nedlastningslenke` er Valgfri | Subset | Middels |
| 4 | `dokumentasjon` og `landingsside` er Valgfri på `Datasett` | Subset | Middels |
| 5 | `identifikator_literal` er Valgfri på `Datasett` | Subset | Middels |
| 6 | `tilgangsrettigheter` manglar tilrådde verdiar | Annotasjon | Middels |
| 7 | Ikkje-opna datasett kan ikkje katalogiserast med forklaring | Strukturgap | Låg |
| 8 | Ingen formatrettleiing mot maskinlesbare standardformat | Annotasjon | Låg |

---

## Tilrådde tiltak

### RÅ1 — Legg til tilrådde verdiar for `lisens` (`slot_usage` endrast ikkje)

`lisens` held seg `Anbefalt` på `Distribusjon`, `Katalog` og `Datatjeneste` —
`slot_usage` skal **ikkje** endrast til `Obligatorisk`. Tiltaket er avgrensa til
å dokumentere dei tilrådde verdiane via annotasjon på sloten:

```yaml
lisens:
  slot_uri: dct:license
  range: string
  description: >-
    Lisens for bruk av ressursen. For offentlege data skal CC BY 4.0
    (https://creativecommons.org/licenses/by/4.0/) eller NLOD 2.0
    (https://data.norge.no/nlod/no/2.0) nyttast per retningslinjene.
  annotations:
    gyldige_verdier: >-
      https://creativecommons.org/licenses/by/4.0/
      https://data.norge.no/nlod/no/2.0
```

**Valider mot sølv-policyen:** `src/mcp-linkml-validator/policies/silver.yaml` har i
dag **ingen** sjekk for `dct:license` (kontrollert 2026-06-20 — ingen
`class_has_slot_with_uri`-regel med `slot_uri: dct:license`, til forskjell frå
t.d. `katalog_utgiver` og `datasett_tittel`). Sidan `lisens` framleis er
`Anbefalt` (ikkje `Obligatorisk`), bør ein eventuell `distribusjon_lisens`-sjekk
i sølv-policyen ha `severity: warning`, ikkje `error`. Avklar om policyen skal
utvidast med denne sjekken før tiltaket merkast som utført.

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`,
`src/mcp-linkml-validator/policies/silver.yaml` (vurder ny sjekk)

---

### RÅ2 — Klassifiser `frekvens` som Anbefalt på `Datasett` (Avvik 2)

DA4 (`specs/done/avvik-dcat-ap-no.md`) har allereie lagt `frekvens` til i
`slots:`-lista på `Datasett`. Det som står igjen er `slot_usage`-klassifiseringa:

```yaml
Datasett:
  slot_usage:
    frekvens:
      in_subset:
        - Anbefalt
```

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

---

### RÅ3 — Juster subset for `nedlastningslenke`, `dokumentasjon`, `landingsside`, `identifikator_literal`

Endre `Datasett.slot_usage`:

```yaml
landingsside:
  in_subset:
    - Anbefalt
dokumentasjon:
  in_subset:
    - Anbefalt
identifikator_literal:
  in_subset:
    - Anbefalt
```

Endre `Distribusjon.slot_usage`:

```yaml
nedlastningslenke:
  in_subset:
    - Anbefalt
```

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

---

### RÅ4 — Legg til tilrådde verdiar for `tilgangsrettigheter`

```yaml
tilgangsrettigheter:
  slot_uri: dct:accessRights
  range: uri
  description: >-
    Tilgangsrettar for datasettet. Bruk EU Access Rights-vokabularet:
    PUBLIC (ope, ingen registrering), RESTRICTED (avgrensa), NON_PUBLIC (ikkje offentleg).
  annotations:
    gyldige_verdier: >-
      http://publications.europa.eu/resource/authority/access-right/PUBLIC
      http://publications.europa.eu/resource/authority/access-right/RESTRICTED
      http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC
```

**Filer:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avhengigheit |
|---|---|---|---|
| 1 | RÅ2: `frekvens` Anbefalt på `Datasett` | `dcat-ap-no-schema.yaml` | DA4 utført i `specs/done/avvik-dcat-ap-no.md` |
| 2 | RÅ1: tilrådde verdiar for `lisens` (`slot_usage` uendra) | `dcat-ap-no-schema.yaml` | — |
| 3 | RÅ4: `tilgangsrettigheter` annotasjon | `dcat-ap-no-schema.yaml` | — |
| 4 | RÅ3: Subset-justering for 4 slot | `dcat-ap-no-schema.yaml` | — |

---

## Avhengigheiter

- RÅ2 (frekvens-klassifisering) er det som står igjen av DA4 (`specs/done/avvik-dcat-ap-no.md`),
  som allereie la sloten til på `Datasett`
- RÅ1, RÅ3 og RÅ4 er uavhengige av kvarandre
- Subset-endringar (berre RÅ3 — RÅ1 endrar ikkje `slot_usage`) kan bryte
  eksisterande datafiler som ikkje inneheld dei nye `Anbefalt`-felta —
  `brreg-begrepskatalog` og eventuelle framtidige DCAT-implementasjonar bør
  gjennomgåast

## Merknader

Retningslinjene er eit politisk styringsdokument retta mot offentlege verksemder.
Mange av krava (#7 synlegheit, #14 oppmuntring, #15 tilbakemeldingssystem) er
prosess-krav som ikkje kan modellerast i eit LinkML-schema. `dcat-ap-no-schema.yaml`
gjev allereie eit godt fundament — dei resterande gapa handlar primært om kor
*sterkt* schema uttrykkjer at nøkkelkrav bør etterleiast.

---

## Utført (2026-06-20)

Alle fire tiltaka (RÅ1-RÅ4) er implementerte i
`src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`:

- **RÅ1:** `lisens`-sloten har no `description` og
  `annotations.gyldige_verdier` med CC BY 4.0 og NLOD 2.0. `slot_usage` er
  **ikkje** endra — `lisens` er framleis `Anbefalt`, som planlagt.
  I tillegg vart `distribusjon_lisens` lagt til som ny sjekk i
  `src/mcp-linkml-validator/policies/silver.yaml` (`severity: warning`,
  `class_has_slot_with_uri` på `Distribusjon`/`dct:license`) — dette var eit
  avklaringspunkt i planen, brukaren valde å inkludere policy-sjekken.
- **RÅ2:** `Datasett.slot_usage.frekvens` sett til `in_subset: Anbefalt`.
- **RÅ3:** `Datasett.slot_usage` utvida med `dokumentasjon`, `landingsside`
  og `identifikator_literal`, alle `in_subset: Anbefalt`.
  `Distribusjon.slot_usage.nedlastningslenke` sett til `in_subset: Anbefalt`.
- **RÅ4:** `tilgangsrettigheter`-sloten har no utvida `description` og
  `annotations.gyldige_verdier` med dei tre EU Access Rights-URI-ane
  (PUBLIC/RESTRICTED/NON_PUBLIC).

**Avvik frå planen:** ingen, utover at RÅ1 sitt avklaringspunkt (policy-sjekk
ja/nei) blei løyst ved å spørje brukaren direkte, som valde å inkludere sjekken.

**Validering:** `make roundtrip` (JSON + TTL) OK. `make lint` viser same 6
pre-eksisterande `canonical_prefixes`-advarslar som før endringa — ingen nye.
`make mcp-validate POLICY=silver` viser ingen advarsel for `distribusjon_lisens`
(`Distribusjon` har allereie `lisens`-sloten, så sjekken passerer).
`make validate-instance` kan ikkje køyrast direkte mot dette schemaet
(AP-NO-profilar har ingen `tree_root`, jf. CLAUDE.md — `linkml validate` finn
flere potensielle target-klassar). Dette er ikkje knytt til endringane i denne
specen.

**Ikkje del av dette tiltaket:** Avvik 7 (ikkje-opna datasett-strukturgap) er
eit strukturgap utan tilrådd tiltak i kartlegginga, og er ikkje adressert.
