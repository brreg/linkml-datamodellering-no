# Evaluering av samsvar med SKOS-AP-NO Vedlegg A — Navnerom

## Bakgrunn

Vedlegg A i SKOS-AP-NO spesifiserer alle navnerom (prefixer) som er brukte i standarden. Denne evalueringa vurderer om `skos-ap-no-schema.yaml` brukar riktige navnerom.

## Samanlikning: Spesifikasjon vs. Skjema

| Prefix | Spesifikasjon | Skjema | Status |
|---|---|---|---|
| **adms** | `http://www.w3.org/ns/adms#` | `http://www.w3.org/ns/adms#` | ✓ |
| **dcat** | `http://www.w3.org/ns/dcat#` | `http://www.w3.org/ns/dcat#` | ✓ |
| **dct** | `http://purl.org/dc/terms/` | `http://purl.org/dc/terms/` | ✓ |
| **euvoc** | `http://publications.europa.eu/ontology/euvoc#` | `http://publications.europa.eu/ontology/euvoc#` | ✓ |
| **org** | `http://www.w3.org/ns/org#` | `http://www.w3.org/ns/org#` | ✓ |
| **owl** | `http://www.w3.org/2002/07/owl#` | (ikkje brukt) | — |
| **rdf** | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` | ✓ |
| **rdfs** | `http://www.w3.org/2000/01/rdf-schema#` | `http://www.w3.org/2000/01/rdf-schema#` | ✓ |
| **skos** | `http://www.w3.org/2004/02/skos/core#` | `http://www.w3.org/2004/02/skos/core#` | ✓ |
| **skosno** | `https://data.norge.no/vocabulary/skosno#` | `https://data.norge.no/vocabulary/skosno#` | ✓ |
| **uneskos** | `http://purl.org/umu/uneskos#` | `http://purl.org/umu/uneskos#` | ✓ |
| **vcard** | `http://www.w3.org/2006/vcard/ns#` | `http://www.w3.org/2006/vcard/ns#` | ✓ |
| **xkos** | `http://rdf-vocabulary.ddialliance.org/xkos#` | `http://rdf-vocabulary.ddialliance.org/xkos#` | ✓ |
| **xsd** | `http://www.w3.org/2001/XMLSchema#` | `http://www.w3.org/2001/XMLSchema#` | ✓ |

### Ekstra prefixer i skjema (ikkje i Vedlegg A):

| Prefix | Namespace | Kommentar |
|---|---|---|
| **linkml** | `https://w3id.org/linkml/` | LinkML-intern prefix — nødvendig for LinkML-metadata |

### Manglande prefix i skjema:

| Prefix | Namespace | Kommentar |
|---|---|---|
| **owl** | `http://www.w3.org/2002/07/owl#` | Lista i Vedlegg A, men **ikkje brukt** i skjemaet |

## Funn

### ✓ Alle brukte prefixer er korrekte

Alle prefixer som **faktisk er brukte** i `skos-ap-no-schema.yaml` har **identisk namespace** som spesifisert i Vedlegg A.

### ✓ `skosno`-prefiks er korrekt implementert

**Spesifikasjon (Vedlegg A):**
> Navnerom for denne standarden er `https://data.norge.no/vocabulary/skosno#`

**Implementering:**
```yaml
prefixes:
  skosno: https://data.norge.no/vocabulary/skosno#
```

**Status:** ✓ Korrekt — `skosno`-prefixen er definert og klar for bruk til norske utvidingar.

### — `owl`-prefix manglar (ikkje-kritisk)

**owl (Web Ontology Language):**
- Lista i Vedlegg A, men **ikkje brukt** i `skos-ap-no-schema.yaml`
- SKOS-AP-NO brukar `rdf:` og `rdfs:` for metadata, ikkje `owl:`

**Status:** — Denne prefixen er lista i Vedlegg A fordi ho er **del av det fullstendige SKOS-økosystemet**, men ho er ikkje nødvendig for denne implementeringa.

**Vurdering:** Det er **ikkje** nødvendig å leggje til `owl`-prefixen dersom ho ikkje vert brukt i skjemaet.

## Konklusjon

**`skos-ap-no-schema.yaml` er i **full samsvar** med SKOS-AP-NO Vedlegg A (Navnerom).**

- ✓ Alle brukte prefixer (`skos:`, `skosno:`, `dct:`, `dcat:`, `euvoc:`, `xkos:`, `uneskos:`, `vcard:`, `org:`, `adms:`, `rdf:`, `rdfs:`, `xsd:`) har **identisk namespace** som spesifisert i Vedlegg A
- ✓ `skosno`-prefixen (`https://data.norge.no/vocabulary/skosno#`) er korrekt implementert for norske utvidingar
- — `owl`-prefixen manglar, men er **ikkje nødvendig** sidan ho ikkje vert brukt i skjemaet

**Ingen avvik eller manglande implementeringar identifiserte.**

## Tiltak

Ingen tiltak nødvendige — skjemaet implementerer Vedlegg A korrekt.

**Valfri forbetring (ikkje nødvendig):**
- Legg til `owl: http://www.w3.org/2002/07/owl#` i `prefixes` for fullstendig samsvar med Vedlegg A-lista, men **berre** dersom prefixen skal brukast i framtida.
