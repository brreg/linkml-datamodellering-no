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

### 1 — Schema-ID: `register-over-aksjeeiere-schema.yaml` brukar `example.no`

```yaml
# Noverande (feil)
id: https://example.no/ontology/aksje-eierskap

# Korrekt
id: https://data.norge.no/oreg/register-over-aksjeeiere
```

Skjemaet er eit produksjonsskjema under `oreg/`, men `id`-feltet brukar `example.no` —
eit domene reservert for illustrasjons- og testformål (per RFC 2606/RFC 6761).
`default_prefix` er korrekt (`https://data.norge.no/oreg/register-over-aksjeeiere/`),
noko som gjev ein intern inkonsistens: klasse-URI-ar og slot-URI-ar vert genererte
med riktig prefix, men schema-metadataen sjølv har feil identifikator.

**Fil:** `src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml`  
**Status:** ⚠️ Feil schema-ID — bør rettast

---

### 2 — Instans-URI-ar i `brreg-begrepskatalog`: domenet `begrep.brreg.no` løyser ikkje opp

Omgrepsinstansar i `brreg-begrepskatalog` brukar URI-ar med formatet:

```
https://begrep.brreg.no/foretaksnavn
https://begrep.brreg.no/nestleder
https://begrep.brreg.no/aksjeklasser
```

Testkall mot `https://begrep.brreg.no/foretaksnavn` returnerer `ECONNREFUSED`
(servaren nektar tilkoplinga), som tyder på at domenet ikkje er i drift.

Standarden krev at URI-ar til offentlege ressursar **skal** vere resolvable og
returnere maskinlesbar respons. URI-ar som ikkje løyser opp, bryt
EU ISA-regel 3 (vedtatt for bruk) og regel 6 (korrekt HTTP-statuskode).

Moglege årsaker:
- `begrep.brreg.no` er eit gammalt domene som er lagt ned
- Brreg har flytta begrepskatalogen til `concept-catalog.fellesdatakatalog.digdir.no`

**Filer:**
- `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`
- `src/linkml/begrepskatalog/brreg-begrepskatalog/examples/brreg-begrepskatalog-eksempel.yaml`

**Status:** ⚠️ Kritisk — instans-URI-ar løyser ikkje opp; treng avklaring med Brreg

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

| # | Avvik | Type | Prioritet |
|---|---|---|---|
| 1 | `register-over-aksjeeiere-schema.yaml` brukar `example.no` som schema-ID | Schema-ID | **Høg** |
| 2 | `begrep.brreg.no`-URI-ar løyser ikkje opp (ECONNREFUSED) | Resolvabilitet | **Høg** |
| 3 | `brreg.no/modellkatalogar/`-URI-ar løyser ikkje opp (timeout) | Resolvabilitet | Middels |
| 4 | Schema-ID-ar returnerer HTML, ikkje RDF (content negotiation manglar) | Infrastruktur | Middels |
| 5 | Ingen dokumentert URI-konstruksjonsregel | Dokumentasjon | Låg |
| 6 | W3C-namespace på `http://` — korrekt no, overvak framtidig | Info | — |

---

## Tilrådde tiltak

### PO1 — Fiks schema-ID i `register-over-aksjeeiere-schema.yaml` (Avvik 1)

```yaml
# Endre
id: https://example.no/ontology/aksje-eierskap
# Til
id: https://data.norge.no/oreg/register-over-aksjeeiere
```

Sjekk og oppdater alle referansar til `example.no`-URI-en i same fil.

**Fil:** `src/linkml/oreg/register-over-aksjeeiere/register-over-aksjeeiere-schema.yaml`

---

### PO2 — Avklar status for `begrep.brreg.no` og oppdater URI-ar (Avvik 2)

Kontakt Brreg for å avklare:
- Er `begrep.brreg.no` ein aktiv teneste, eller er han lagt ned?
- Kva er dei kanoniske URI-ane for Brreg sine omgrep i dag?

Sannsynleg korrekt URI-mønster:
```
https://concept-catalog.fellesdatakatalog.digdir.no/collections/<UUID>/concepts/<UUID>
```

Dersom `begrep.brreg.no` er lagt ned, oppdater alle `id:`-verdiar i
`brreg-begrepskatalog.yaml` til dei nye, kanoniske URI-ane.

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

| # | Tiltak | Fil(ar) | Avhengigheit |
|---|---|---|---|
| 1 | PO1: Fiks `example.no` schema-ID | `register-over-aksjeeiere-schema.yaml` | — |
| 2 | PO2: Avklar `begrep.brreg.no` og oppdater URI-ar | `brreg-begrepskatalog.yaml`, eksempelfil | Ekstern (Brreg) |
| 3 | PO3: Avklar `brreg.no/modellkatalogar/` | `brreg-modellkatalog.yaml`, eksempelfil | Ekstern (Brreg) |
| 4 | PO4: URI-konstruksjonspolicy i `CLAUDE.md` | `CLAUDE.md` | — |

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
