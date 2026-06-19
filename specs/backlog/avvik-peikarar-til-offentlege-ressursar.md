# Kartlegging: Avvik mot Peikarar til offentlege ressursar på nett

**Kjelde:** [digdir.no/standarder/peikarar-til-offentlege-ressursar-pa-nett/1492](https://www.digdir.no/standarder/peikarar-til-offentlege-ressursar-pa-nett/1492)  
**Utgjevar:** Digitaliseringsdirektoratet  
**Status:** Tilrådd standard (innført 12.12.2016, sist endra 21.04.2022)  
**Grunnlagsstandardar:** RFC 3986/3987, EU ISA-program sine 10 reglar for persistente URI-ar

---

## Bakgrunn

Standarden regulerer korleis offentlege verksemder skal utforme URI-ar/IRI-ar for ressursar som
er tilgjengelege på internett. Hovudkrava er:

1. **HTTPS-URI-mønster:** `https://{domene}/{valgfritt(type)}/{valgfritt(konsept)}/{objektidentifikator}`
2. **Persistente URI-ar:** URI-ar skal ikkje innehalde implementasjonsdetaljar (`.php`, `.asp`),
   versjonnummer eller sesjonsinformasjon — dei skal vere stabile over tid
3. **Maskinlesbar respons:** URI-ar til offentlege ressursar skal returnere innhald i
   maskinlesbare format, ikkje berre HTML
4. **IRI-preferanse:** Bruk IRI (RFC 3987) for å støtte Unicode (norske bokstavar i URI-er er OK)

Standarden er primært retta mot *dei URI-ane* som vert brukt som identifikatorar for
offentlege datasett, omgrep og modell-ar — ikkje intern infrastruktur.

---

## Kartlegging av avvik

### 1 — Schema-ID: `register-over-aksjeeiere-schema.yaml` brukar `example.no` — ✓ LØYST

```yaml
# Tidlegare (feil)
id: https://example.no/ontology/aksje-eierskap

# Noverande (korrekt)
id: https://data.norge.no/oreg/register-over-aksjeeiere
```

**Fil:** `src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml`  
**Status:** ✓ Løyst — schema-ID er endra til `https://data.norge.no/oreg/register-over-aksjeeiere`

---

### 1b — `finta:`-prefiks i `fint-common-schema.yaml` peikar til `example.no` — ✓ LØYST

`fint-common-schema.yaml` definerer prefikset:

```yaml
# Tidlegare (feil)
prefixes:
  finta:  https://example.no/fint/

# Noverande (korrekt)
prefixes:
  finta:  https://fint.example.org/
```

Prefikset er brukt som instans-ID-mønster i 6 eksempelfiler (alle FINT-domene). Sidan
dei brukar CURIE-notasjon (`finta:person/ola-nordmann`), var det nok å endre prefiksdefinisjon
i `fint-common-schema.yaml` — eksempelfilene treng inga eiga endring.

Avviket var avgrensa til **eksempelfiler** (`examples/`), ikkje produksjonsdata.
Ingen `class_uri:` eller `slot_uri:` i skjemadefinisjonane brukar `finta:`-prefikset.

**Fil:**
- `src/linkml/fint/fint-common/fint-common-schema.yaml` — prefiksdefinisjon endra

**Status:** ✓ Løyst — `finta:` peikar no til RFC 2606-reservert `https://fint.example.org/`

---

### 2 — Instans-URI-ar i `brreg-begrepskatalog`: domenet `begrep.brreg.no` løyser ikkje opp

Omgrepsinstansar i `brreg-begrepskatalog` brukar URI-ar med formatet:

```
https://begrep.brreg.no/foretaksnavn
https://begrep.brreg.no/nestleder
https://begrep.brreg.no/aksjeklasser
```

Testkall mot `https://begrep.brreg.no/foretaksnavn` returnerer `ECONNREFUSED`
(servaren nektar tilkoplinga). Domenet er lagt ned.

**Kjend kanonisk IRI i Felles Begrepskatalog:**

Brønnøysundregistrene publiserer omgrepa sine i Felles Begrepskatalog under
`concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/`. Den
kanoniske IRI-en for `foretaksnavn` er:

```
https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/47534952-c9c5-4ef1-a76f-8a76c74f11cd
```

**Ope spørsmål — UUID-tildeling:**

Det er uklart om UUID-en (`47534952-...`) er:

- **A) Forhåndsbestemt av Brreg** — Brreg set `dct:identifier` med ein UUID i sitt
  eige system, og Felles Begrepskatalog tek vare på den same UUID-en som del av IRI-en.
  I så fall kan `id:` settast direkte i YAML-fila *før* høsting.
- **B) Automatisk tildelt av Felles Begrepskatalog** — UUID vert tildelt ved første
  høsting og er ikkje kjend på førehand. `id:` kan først settast *etter* at begrepet
  er hosta og UUID-en er henta ut frå API-et.

Dersom det er alternativ B gjeld følgjande for begrep som allereie er publiserte:
UUID-en er kjend og kan slåast opp direkte. For begrep som ikkje er publiserte enno,
vil `id:` måtte bruke ei midlertidig URI og oppdaterast etter første høsting.

Begge `id:` og `identifikator_literal:`-feltet i datafila brukar i dag den nedlagde
`begrep.brreg.no`-URI-en og må oppdaterast:

```yaml
# Noverande (feil)
- id: https://begrep.brreg.no/foretaksnavn
  identifikator_literal: "https://begrep.brreg.no/foretaksnavn"

# Korrekt (for foretaksnavn)
- id: https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/47534952-c9c5-4ef1-a76f-8a76c74f11cd
  identifikator_literal: "https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/47534952-c9c5-4ef1-a76f-8a76c74f11cd"
```

**Filer:**
- `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`
- `src/linkml/begrepskatalog/brreg-begrepskatalog/examples/brreg-begrepskatalog-eksempel.yaml`

**Status:** ⚠️ Kritisk — instans-URI-ar løyser ikkje opp; UUID-spørsmål må avklarast

---

### 3 — Instans-URI-ar i `brreg-modellkatalog`: `brreg.no/modellkatalogar/` løyser truleg ikkje opp

```
https://brreg.no/modellkatalogar/brreg-modellkatalog
https://brreg.no/modellkatalogar/brreg-modellkatalog/ngr-virksomhet
https://brreg.no/kontakt/modellforvaltning
```

Kall mot `https://brreg.no/modellkatalogar/brreg-modellkatalog` resulterte i timeout.
Standarden krev resolvable URI-ar. Enten er desse URI-ane ikkje i drift endå
(planlagde), eller dei er aldri publiserte.

**Filer:**
- `src/linkml/modellkatalog/brreg-modellkatalog/data/brreg-modellkatalog/brreg-modellkatalog.yaml`
- `src/linkml/modellkatalog/brreg-modellkatalog/examples/brreg-modellkatalog-eksempel.yaml`

**Status:** ⚠️ Treng avklaring — URI-ane bør anten vere live eller dokumenterast som «planlagde»

---

### 4 — Schema-ID-ar returnerer HTML, ikkje maskinlesbar RDF (content negotiation manglar)

Schema-ID-ar som `https://data.norge.no/ap-no/dcat-ap-no` løyser opp til Felles
datakatalog si HTML-side, ikkje til sjølve LinkML-skjemaet eller ein RDF-representasjon.

Standarden krev at URI-ar til offentlege ressursar returnerer maskinlesbart innhald
(ISA-regel 8: «Provide multiple representations»). For eit informasjonsmodell-skjema
betyr det at:

```
GET https://data.norge.no/ap-no/dcat-ap-no
Accept: text/turtle
→ Burde returnere TTL/RDF-serialisering av skjemaet (eller 303 til slik ressurs)
```

I dag returnerer alle `data.norge.no/ap-no/`-URI-ane ein HTML-portal utan
`Link: <…>; rel="alternate"` eller innhaldsforhandling.

**Merk:** Dette er ein infrastrukturproblem hjå `data.norge.no` — repoet kan ikkje
løyse dette åleine, men kan bidra ved å publisere skjema-RDF på GitHub Pages og
be om at `data.norge.no` sett opp redirectar.

**Filer:** Alle `src/linkml/ap-no/`-skjema, alle domenemodell-skjema  
**Status:** ⚠️ Strukturgap — krev koordinering med Digdir/data.norge.no-infrastruktur

---

### 5 — Ingen dokumentert URI-konstruksjonsregel

Standarden krev at URI-konstruksjonsreglane er dokumenterte (ISA-regel 3:
«Publish your URI construction policy»).

Repoet har ein god URI-praksis i CLAUDE.md (`Schema-metadata`-seksjonen), men
ho er ufullstendig:
- Det er dokumentert at `id` skal vere ein absolutt HTTPS-URL, og at `default_prefix`
  skal ha avsluttande `/`
- Men det er ikkje dokumentert kva dei ulike segmenta tyder: `ap-no`, `oreg`, `ngr`,
  `fint`, `samt`, `begrepskatalog`, `modellkatalog`
- Ingen policy for kva som skjer om ein skjemamodell vert flytta eller sletta
  (URI-stabilitetspolicy)

**Status:** ⚠️ Dokumentasjonsgap — låg prioritet

---

### 6 — `http://` prefiks for W3C-vokabular: korrekt, men bør verifiserast med tida

Alle W3C- og EU-vokabularprefiksar i skjema (`dcat:`, `dct:`, `foaf:`, `skos:`, `rdf:`,
`rdfs:`, osb.) brukar `http://` — ikkje `https://`.

Dette er **korrekt** fordi desse er dei kanoniske namespace-URI-ane fastsette av
W3C og andre standardorgan. Standarden «Peikarar til offentlege ressursar på nett»
gjeld berre for ressursar som *norske offentlege verksemder* forvaltar.

Merk likevel at W3C gradvis migrerer nokre namespace til `https://` (t.d. `https://www.w3.org/ns/dcat#`
er i bruk i nyare dokument). Dette er eit framtidig oppfølgingspunkt, ikkje eit aktuelt avvik.

**Status:** ✓ Korrekt per i dag — overvak W3C-migrasjon til HTTPS-namespace

---

## Positiv status (krav som er oppfylde)

| Krav | Status |
|---|---|
| HTTPS i alle eigne schema-ID-ar | ✓ Alle `https://data.norge.no/...` |
| Ingen implementasjonsutvidingar (`.php`, `.asp`) | ✓ |
| Ingen spørrjesstreng-baserte ID-ar | ✓ |
| Ingen versjonsnummer i URI-ar | ✓ (versjon i `version:`-feltet, ikkje URI) |
| Slash-basert URI-struktur | ✓ |
| Eige `id` per skjema | ✓ (unntaket er avvik 1) |
| Avsluttande `/` i `default_prefix` | ✓ |

---

## Samandrag

| # | Avvik | Type | Prioritet | Status |
|---|---|---|---|---|
| 1 | `register-over-aksjeeiere-schema.yaml` brukar `example.no` som schema-ID | Schema-ID | **Høg** | ✓ Løyst |
| 1b | `finta:`-prefiks peikar til `example.no` — brukt i FINT-eksempelfiler | Eksempel-URI | Låg | ✓ Løyst |
| 2 | `begrep.brreg.no`-URI-ar løyser ikkje opp (ECONNREFUSED) | Resolvabilitet | **Høg** | ⚠️ Ope |
| 3 | `brreg.no/modellkatalogar/`-URI-ar løyser ikkje opp (timeout) | Resolvabilitet | Middels | ⚠️ Ope |
| 4 | Schema-ID-ar returnerer HTML, ikkje RDF (content negotiation manglar) | Infrastruktur | Middels | ⚠️ Ope |
| 5 | Ingen dokumentert URI-konstruksjonsregel | Dokumentasjon | Låg | ⚠️ Ope |
| 6 | W3C-namespace på `http://` — korrekt no, overvak framtidig | Info | — | ✓ Korrekt |

---

## Tilrådde tiltak

### PO1 — Fiks schema-ID i `register-over-aksjeeiere-schema.yaml` (Avvik 1) — ✓ UTFØRT

`id` er endra til `https://data.norge.no/oreg/register-over-aksjeeiere`. Ingen vidare tiltak.

---

### PO1b — Oppdater `finta:`-prefiks og eksempel-URI-ar (Avvik 1b) — ✓ UTFØRT

`finta:`-prefikset i `fint-common-schema.yaml` er endra frå `https://example.no/fint/` til
`https://fint.example.org/` (RFC 2606-reservert). Alle 6 FINT-eksempelfiler brukar
CURIE-notasjon og treng inga separat endring — prefikset arvas frå skjemaet.

---

### PO2 — Oppdater URI-ar i `brreg-begrepskatalog` til Felles Begrepskatalog-URI-ar (Avvik 2)

`begrep.brreg.no` er lagt ned. Brreg publiserer omgrepa sine i Felles Begrepskatalog
med kanonisk IRI-mønster:
```
https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/<UUID>
```

**Steg 1 — Avklar UUID-tildeling (eksternt spørsmål):**

Kontakt Brreg eller Digdir for å avklare om UUID-en er forhåndsbestemt
(sett av Brreg ved oppretting i deira eige system) eller automatisk tildelt
(sett av Felles Begrepskatalog ved høsting).

- **Viss forhåndsbestemt (alternativ A):** `id:` kan settast i YAML-fila
  direkte til `concept-catalog.fellesdatakatalog.digdir.no`-URI-en, og datafila
  kan oppdaterast *før* neste høsting.
- **Viss automatisk tildelt (alternativ B):** For begrep som allereie er
  publiserte, hent UUID frå Felles Begrepskatalog API og oppdater datafila.
  For nye begrep, bruk `brreg.no`-URI midlertidig og oppdater etter høsting.

**Steg 2 — Oppdater kjende begrep:**

Tabellen under viser begrep med kjende Felles Begrepskatalog-URI-ar.
Oppdater både `id:` og `identifikator_literal:` i datafila:

| Begrep | Ny `id:` |
|---|---|
| `foretaksnavn` | `https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/47534952-c9c5-4ef1-a76f-8a76c74f11cd` |
| `nestleder` | `https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/53125ffd-f655-460b-9d32-e231eb561699` |
| `aksjeklasser` | `https://concept-catalog.fellesdatakatalog.digdir.no/collections/974760673/concepts/0597aab6-14d3-4dbc-a0ac-f4c9658de17e` |

Også `har_definisjon:`-, `kontaktpunkt_vcard:`- og
`sja_ogsa_omgrep:`-referansar som peikar til `begrep.brreg.no` må gjennomgåast.

**Filer:**
- `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`
- `src/linkml/begrepskatalog/brreg-begrepskatalog/examples/brreg-begrepskatalog-eksempel.yaml`

---

### PO3 — Avklar status for `brreg.no/modellkatalogar/`-URI-ar (Avvik 3)

Kontakt Brreg for å avklare om `https://brreg.no/modellkatalogar/` er planlagd
publisert. Dersom ikkje, bruk URI-mønster frå `data.norge.no`-domenet:

```yaml
# Alternativ
- id: https://data.norge.no/oreg/brreg-modellkatalog
```

Merk at repoet sjølv er kjelde for artefaktar (jf. «Pull, ikkje push»-prinsippet),
men instans-URI-ane bør framleis vere live eller eksplisitt merka som «planlagde».

---

### PO4 — Legg til URI-konstruksjonspolicy i CLAUDE.md (Avvik 5)

Utvid `Schema-metadata`-seksjonen i `CLAUDE.md` med ei forklaring av kva dei
ulike segmenta tyder:

| Segment | Tydning | Døme |
|---|---|---|
| `ap-no` | AP-NO-applikasjonsprofil | `https://data.norge.no/ap-no/dcat-ap-no` |
| `oreg` | Offentleg register | `https://data.norge.no/oreg/register-over-aksjeeiere` |
| `ngr` | Nasjonale grunndata | `https://data.norge.no/ngr/ngr-adresse` |
| `fint` | FINT-domenemodell | `https://data.norge.no/fint/fint-administrasjon` |
| `samt` | Samhandlingsmodell | `https://data.norge.no/samt/samt-bu` |
| `begrepskatalog` | Begrepskatalog | `https://data.norge.no/begrepskatalog/brreg-begrepskatalog` |
| `modellkatalog` | Modellkatalog | `https://data.norge.no/modellkatalog/brreg-modellkatalog` |
| `fair` | FAIR-metadatamodell | `https://data.norge.no/fair/fair-metadata` |

Legg til at URI-ar skal vere stabile — at `id`-verdien ikkje skal endrast etter
første publisering utan at det vert dokumentert.

---

## Prioritert handlingsliste

| # | Tiltak | Fil(ar) | Avhengigheit | Status |
|---|---|---|---|---|
| 1 | PO1: Fiks `example.no` schema-ID | `register-over-aksjeeiere-schema.yaml` | — | ✓ Utført |
| 2 | PO1b: Oppdater `finta:`-prefiks og eksempel-URI-ar | `fint-common-schema.yaml`, `fint-administrasjon-eksempel.yaml` | — | ✓ Utført |
| 3 | PO2: Avklar `begrep.brreg.no` og oppdater URI-ar | `brreg-begrepskatalog.yaml`, eksempelfil | Ekstern (Brreg) | Ope |
| 4 | PO3: Avklar `brreg.no/modellkatalogar/` | `brreg-modellkatalog.yaml`, eksempelfil | Ekstern (Brreg) | Ope |
| 5 | PO4: URI-konstruksjonspolicy i `CLAUDE.md` | `CLAUDE.md` | — | Ope |

---

## Merknader

### Standardens avgrensing

Standarden er ein tilrådd (ikkje obligatorisk) standard og er relativt tynn i
teknisk detalj — han refererer primært til RFC 3986/3987 og EU ISA-programmet sine
10 reglar. Den norske tilpassinga er hovudsakleg URI-mønsteret
`https://{domene}/{type}/{konsept}/{id}` og ei tilråding om å bruke IRI (RFC 3987).

Krav om content negotiation (avvik 4) kjem frå EU ISA-reglane og frå
DCAT-AP-NO-spesifikasjonen (som krev at `dcat:accessURL` skal returnere
maskinlesbar respons) — ikkje frå Digdir-standarden aleine.

### `example.no` i produksjonsskjema

`example.no` er i praksis eit norsk domene som er registrert, men ikkje i drift
som ein stabil tjeneste. I motsetning til `example.org` (RFC 2606) er ikkje
`example.no` internasjonalt reservert for eksempelbruk. Bruken er likevel klart
misvisande i ein produksjonssamanheng og bryt intensjonen i standarden.
