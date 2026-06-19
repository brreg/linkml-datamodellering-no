# Plan: `make new-begrep` — scaffold ny begrepskatalog

**Kortnamn:** `new-begrep-kommando`  
**Dato:** 2026-06-19  

---

## Bakgrunn

`ny-begrepsmodell.md` seier eksplisitt at `make new-model` **ikkje** gjeld for
begrepskatalogar — scaffolding er manuell (steg 1–3). Dette skapar friksjon:

- Brukaren må kopiere frå `brreg-begrepskatalog-schema.yaml` og redigere for hand
- README-seksjonen «Begrepsmodellering» er feil (viser `make new-model`)
- Det er inkonsistens mellom domenemodell-arbeidsflyten (`make new-model`) og
  begrepskatalogar (manuelt) utan god grunn — skjemaet for ein begrepskatalog
  er statisk og veldefinert

Løysinga er ein dedikert `make new-begrep NAME=<katalognavn>`-kommando som
genererer riktig filstruktur og boilerplate utan MCP-kall (skjemaet er fast,
ikkje generert frå input).

---

## Steg

### NB1 — Opprett `src/assets/scripts/new-begrep.sh`

Scriptet tek `NAME` som einaste argument (domenet er alltid `begrepskatalog`).
Det oppretter desse filene:

```
src/linkml/begrepskatalog/<NAME>/
├── <NAME>-schema.yaml
├── manifest.yaml
├── description.md
└── examples/
    └── <NAME>-eksempel.yaml
```

**`<NAME>-schema.yaml`** (statisk boilerplate, ikkje MCP-generert):

```yaml
id: https://data.norge.no/begrepskatalog/<NAME>
name: <NAME_underscore>
title: 'TODO: <Organisasjon> – Begrepskatalog'
description: 'TODO: beskriv katalogen'
version: "0.1.0"
license: https://data.norge.no/nlod/no/2.0

annotations:
  utgiver: 'TODO: https://data.norge.no/organizations/<orgnr>'
  status: http://purl.org/adms/status/UnderDevelopment

prefixes:
  linkml: https://w3id.org/linkml/

default_prefix: https://data.norge.no/begrepskatalog/<NAME>/
default_range: string

imports:
  - linkml:types
  - ../../ap-no/skos-ap-no/skos-ap-no-schema

classes:

  BegrepContainer:
    tree_root: true
    attributes:
      begrep:
        range: Begrep
        multivalued: true
        inlined: true
        inlined_as_list: true
      samlingar:
        range: Samling
        multivalued: true
        inlined: true
        inlined_as_list: true
      definisjoner:
        range: Definisjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      generiske_relasjonar:
        range: GeneriskRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      partitive_relasjonar:
        range: PartitivRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      assosiative_relasjonar:
        range: AssosiativRelasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      organisasjonar:
        range: Organisasjon
        multivalued: true
        inlined: true
        inlined_as_list: true
      kontaktpunkt:
        range: VCardKontakt
        multivalued: true
        inlined: true
        inlined_as_list: true
```

**`manifest.yaml`** (frå ny-begrepsmodell.md steg 3):

```yaml
publish_external: false
data_policy: felles-begrepskatalog

generators:
  jsonld_context: true
  shacl: false
  python: false
  json_schema: true
  owl: false
  rdf: true
  protobuf: false
  erdiagram: true
  docs: true
  plantuml: false
  example_rdf: true
```

**`examples/<NAME>-eksempel.yaml`** (minimal stub):

```yaml
# Eksempel for <NAME>
# Generer YAML-blokker med: make mcp-begrep-run (sjå ny-begrepsmodell.md steg 4)
---
BegrepContainer:
  begrep: []
```

**`description.md`** (same som new-model.sh):

```markdown
<!-- Valfri skildring av <NAME>. Vert vist i portalen. -->
<!-- Fyll ut eller slett denne fila. -->
```

Ingen MCP-kall — alt er statiske heredoc-blokker i bash.

### NB2 — Legg til `new-begrep`-target i Makefile

Etter `new-model`-targeten:

```makefile
# Bruk: make new-begrep NAME=<katalognavn>
new-begrep:
	@test -n "$(NAME)" || \
	  (echo "Bruk: make new-begrep NAME=<katalognavn>"; exit 1)
	bash src/assets/scripts/new-begrep.sh "$(NAME)"
```

Legg til `new-begrep` i `.PHONY`-lista.

### NB3 — Oppdater `ny-begrepsmodell.md`

**a)** Endre samanlikingstabellen (steg 0 / note-boksen):

| | Ny begrepskatalog | Ny domenemodell |
|---|---|---|
| Scaffold | ~~Manuelt (steg 1–3 under)~~ → **`make new-begrep`** | `make new-model` |

**b)** Erstatt steg 1–3 (manuell opprettings av filstruktur, schema og manifest)
med:

```bash
make new-begrep NAME=<katalognavn>
```

og ei forklaring av kva filer som vert oppretta — tilsvarande slik steg 1a i
`ny-domenemodell.md` viser filtre-strukturen.

**c)** Behalda steg 4–8 urørte (YAML-generering, validering, RDF-eksport osb.).

### NB4 — Oppdater README.md

Endre `### Begrepsmodellering`-seksjonen slik at steg 1 viser riktig kommando:

```bash
# 1. Opprett ny begrepskatalog (skjema + filstruktur)
make new-begrep NAME=katalognavn
```

---

## Prioritert handlingsliste

| # | Tiltak | Fil | Avheng av |
|---|--------|-----|-----------|
| 1 | ✓ NB1: `new-begrep.sh` | `src/assets/scripts/new-begrep.sh` | — |
| 2 | ✓ NB2: `new-begrep`-target i Makefile | `Makefile` | NB1 |
| 3 | ✓ NB3: Oppdater `ny-begrepsmodell.md` | `mkdocs/docs/ny-begrepsmodell.md` | NB1 |
| 4 | ✓ NB4: Oppdater README.md | `README.md` | NB1 |

---

## Utført

Alle steg gjennomførte 2026-06-19.

- **NB1:** `src/assets/scripts/new-begrep.sh` oppretta — statisk bash-script utan MCP-kall; genererer schema, manifest, eksempelfil og description.md
- **NB2:** `new-begrep`-target lagt til i Makefile og i `.PHONY`-lista
- **NB3:** `ny-begrepsmodell.md` — steg 1–3 (manuell scaffold) erstatta med `make new-begrep`; samanlikingstabellen oppdatert; steg renummererte 0–6
- **NB4:** `README.md` — `make new-model NAME=katalognavn DOMAIN=begrepskatalog` → `make new-begrep NAME=katalognavn`

---

## Avhengigheiter

- `mcp-linkml-begrep-utkast`-image treng ikkje byggjast — scriptet gjer ingen MCP-kall
- `skos-ap-no-schema` må finnast på relativ sti `../../ap-no/skos-ap-no/skos-ap-no-schema`
  (gjeld allereie for alle eksisterande begrepskatalogar)
- Ingen endringar i CI-workflowane nødvendig
