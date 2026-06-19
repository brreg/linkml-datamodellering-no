# Plan: Legg til generert modellutkast-eksempel i ny-domenemodell.md

**Kortnamn:** `ny-domenemodell-mcp-eksempel`  
**Fil som skal oppdaterast:** `mkdocs/docs/ny-domenemodell.md`  
**Referansefil:** `mkdocs/docs/ny-begrepsmodell.md` (§4 — Generer YAML-instansar)  
**Dato:** 2026-06-19

---

## Bakgrunn

`ny-domenemodell.md` beskriv `make new-model` i steg 1a, men viser ikkje kva
som faktisk vert generert. Ein ny brukar veit ikkje kva filer som vert oppretta
eller kva `TODO`-stubbar betyr og må erstattast.

`ny-begrepsmodell.md` §4 viser heile flyten med eit konkret eksempel på generert
YAML — same mønster skal inn i `ny-domenemodell.md` direkte i steg 1a.

**Kjelda:** `src/assets/scripts/new-model.sh` og
`src/mcp-linkml-modell-utkast/converter.py` er autoritative. Eksempla nedanfor
er lese ut frå kjeldekoden og stemmer med faktisk output.

---

## Kva `make new-model` genererer

For `make new-model NAME=tilskudd DOMAIN=eksempel` vert desse filene oppretta:

```
src/linkml/eksempel/tilskudd/
├── tilskudd-schema.yaml
├── manifest.yaml
├── description.md
└── examples/
    └── tilskudd-eksempel.yaml
```

### `tilskudd-schema.yaml`

```yaml
id: https://data.norge.no/eksempel/tilskudd
name: tilskudd
title: 'TODO: tittel for tilskudd'
description: Generert frå JSON Schema 'tilskudd'.
version: 0.1.0
license: https://creativecommons.org/licenses/by/4.0/

prefixes:
  linkml:   https://w3id.org/linkml/
  tilskudd: https://data.norge.no/eksempel/tilskudd/
  dct:      http://purl.org/dc/terms/
  dcat:     http://www.w3.org/ns/dcat#
  foaf:     http://xmlns.com/foaf/0.1/
  skos:     http://www.w3.org/2004/02/skos/core#
  xsd:      http://www.w3.org/2001/XMLSchema#
  rdf:      http://www.w3.org/1999/02/22-rdf-syntax-ns#
  rdfs:     http://www.w3.org/2000/01/rdf-schema#

default_prefix: https://data.norge.no/eksempel/tilskudd/
default_range: string

imports:
  - linkml:types

subsets:
  Obligatorisk:
    description: Obligatoriske eigenskapar.
  Anbefalt:
    description: Anbefalte eigenskapar.
  Valgfri:
    description: Valfrie eigenskapar.

classes:
  tilskudd:                        # ← stub — gi eit norsk PascalCase-namn
    description: Generert frå JSON Schema 'tilskudd'.
    class_uri: tilskudd:tilskudd   # ← byt med faktisk vokabular-URI
    annotations:
      begrepsidentifikator: https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO
    slots:
      - id

  TilskuddContainer:
    description: TODO: beskriv containerklassen
    tree_root: true
    attributes:
      tilskudder:
        description: TODO: beskriv eigenskapen
        range: tilskudd
        multivalued: true
        inlined: true
        inlined_as_list: true

slots:
  id:
    description: Unik URI-identifikator for ressursen.
    identifier: true
    range: uriorcurie

# TODO: Legg til domene-spesifikke imports etter 'linkml:types', t.d.:
#   - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
# TODO: Gi stub-klassen eit meiningsfult norsk namn (PascalCase).
# TODO: Legg til slots og slot_usage for eigenskapane i modellen.
```

### `examples/tilskudd-eksempel.yaml`

```yaml
# Eksempel for tilskudd
# Tilpass instansane med reelle verdiar etter at skjemaet er ferdigstilt.
---
TilskuddContainer:
  tilskudder:
    - id: https://data.norge.no/eksempel/tilskudd/eksempel-1
```

### `manifest.yaml`

```yaml
publish_external: false
data_policy: silver

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
```

### `description.md`

```markdown
<!-- Valfri skildring av tilskudd. Vert vist i portalen mellom ER-diagrammet og klasselista. -->
<!-- Fyll ut eller slett denne fila. -->
```

---

## Kva TODO-stubbar tyder

| Stubb | Kva som skal inn |
|-------|-----------------|
| `title: 'TODO: tittel for tilskudd'` | Norsk bokmål-tittel, t.d. `Tilskuddsregister` |
| `class tilskudd` (ikkje PascalCase) | Gi eit norsk PascalCase-namn, t.d. `Tilskudd` |
| `class_uri: tilskudd:tilskudd` | Faktisk RDF-URI, t.d. `dcat:Dataset` eller eigen namespace |
| `begrepsidentifikator: .../TODO` | URI til begrep i Felles begrepskatalog |
| `description: Generert frå JSON Schema ...` | Skildring av kva klassen representerer |
| `description: TODO: beskriv containerklassen` | Kan slettast eller utfyllast |
| `imports: [linkml:types]` | Legg til AP-NO-profil, t.d. `../../ap-no/dcat-ap-no/dcat-ap-no-schema` |
| `license: https://creativecommons.org/licenses/by/4.0/` | Endre til NLOD 2.0 for offentlege data |

---

## Kvar i dokumentet

Eksempla ovanfor skal inn som eit nytt underavsnitt i eksisterande steg 1a,
slik at steg 1a vert:

```
### 1a — Scaffold

make new-model NAME=<modell> DOMAIN=<domain>    ← eksisterande kommando

#### Kva vert generert?                          ← NY SEKSJON
[filstruktur, schema-eksempel, eksempelfil, manifest, TODO-tabell]
```

---

## Tiltak

| # | Tiltak | Fil | Merknad |
|---|--------|-----|---------|
| 1 | Legg til underavsnitt «Kva vert generert?» i steg 1a | `ny-domenemodell.md` | Hovudarbeidet |
| 2 | Verifiser at schema-eksemplet stemmer med faktisk output | — | `make new-model NAME=tilskudd DOMAIN=eksempel` i testmiljø |

---

## Avhengigheiter

- Ingen endringar i skjema, Makefile eller MCP-server — berre dokumentasjon
- Schema-eksemplet er utlese frå `converter.py` + `bronze.yaml` + `new-model.sh`
  og skal verifiserast mot faktisk køyring (tiltak 2) før publisering

---

## Utført

**2026-06-19** — Tiltak 1 og 2 utførte.

Lagt til nytt underavsnitt `#### Kva vert generert?` i `mkdocs/docs/ny-domenemodell.md`
direkte etter filstrukturlista i steg 1a. Innhaldet:

- Komplett `tilskudd-schema.yaml` med stub-klasse (`tilskudd`, lowercase), `TilskuddContainer`,
  `id`-slot og dei tre TODO-kommentarane frå `new-model.sh`
- `examples/tilskudd-eksempel.yaml` med minimal instans
- TODO-tabell med forklaring per stubb
- Referanse til `manifest.yaml` og `description.md` via lenkje til Modellmanifest-sida

**Avvik frå plan:** Spec-fila hadde `description: Generert frå JSON Schema 'tilskudd'.`
for stub-klassen (linje 75), men faktisk output frå `converter.py` er
`description: TODO: beskriv klassen` (tom `desc` → fallback). `ny-domenemodell.md`
brukar korrekt verdi; spec-fila er ikkje oppdatert sidan den vert arkivert.
