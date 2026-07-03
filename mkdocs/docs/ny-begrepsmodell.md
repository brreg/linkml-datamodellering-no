# Rettleiing: ny begrepskatalog

!!! note "Beskrivelse"

    Denne rettleiinga viser korleis du oppretter ein ny begrepskatalog i repoet —
    frå filstruktur til RDF-eksport klar for Felles Begrepskatalog.

## 0 — Føresetnader (éin gong)

```bash
make check-prereqs
make mcp-begrep-build    # byggjer mcp-linkml-begrep-utkast
make mcp-val-build       # byggjer mcp-linkml-validator (for bronze-validering)
```

---

## 1 — Scaffold

**Namnemønster:** `<org>-begrep` eller `<fagdomene>-begrep`, t.d. `digdir-begrep`, `ssb-begrep`, `ngr-begrep`.

```bash
make new-begrepskatalog NAME=<katalognavn>
```

Dette oppretter:

```
src/linkml/begrepskatalog/<katalognavn>/
├── <katalognavn>-schema.yaml  ← skjema med BegrepContainer og import av skos-ap-no
├── manifest.yaml              ← publiserings- og generatorkonfig
├── description.md             ← valfri skildring, injiserast i portalen
└── examples/
    └── <katalognavn>-eksempel.yaml  ← tom BegrepContainer-stub
```

Fyll deretter ut `title`, `description` og `utgiver` i skjemafila.

For `make new-begrepskatalog NAME=test-begrep` ser dei genererte filene slik ut:

**`test-begrep-schema.yaml`**

```yaml
id: https://data.norge.no/begrepskatalog/test-begrep
name: test_begrep
title: 'TODO: <Organisasjon> - Begrepskatalog'
description: 'TODO: beskriv katalogen'
version: "0.1.0"
license: https://data.norge.no/nlod/no/2.0

annotations:
  utgiver: 'TODO: https://data.norge.no/organizations/<orgnr>'
  status: http://purl.org/adms/status/UnderDevelopment

prefixes:
  linkml: https://w3id.org/linkml/

default_prefix: https://data.norge.no/begrepskatalog/test-begrep/
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
      # ... (samlingar, definisjoner, relasjonar, organisasjonar, kontaktpunkt)
```

**`manifest.yaml`**

```yaml
publish_external: false
validation_policy: felles-begrepskatalog

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

**`examples/test-begrep-eksempel.yaml`**

```yaml
# Eksempel for test-begrep
# Generer YAML-blokker med: make mcp-begrep-run (sjå steg 2)
---
BegrepContainer:
  begrep: []
```

---

## 2 — Generer YAML-instansar

Bruk `opprett_begrep`-verktøyet i `mcp-linkml-begrep-utkast` til å byggje
YAML-blokker.

### Eksempel — generer eitt begrep ihht skjema for begrepskatalog

Legg argumenta i ei JSON-fil, t.d. `tmp/mitt-begrep.json`:

```json
{
  "profil": "default",
  "base_uri": "https://begrep.<org>.no",
  "slug": "mitt-begrep",
  "anbefalt_term_nb": "mitt begrep",
  "definisjon_nb": "ein klar og presis formulering av kva omgrepet tyder",
  "kjelde_relasjon": "self-composed",
  "utgjevar_uri": "https://data.norge.no/organizations/<orgnr>",
  "fagomrade_uri": "https://psi.norge.no/los/tema/<slug>"
}
```

```bash
make mcp-linkml-begrep-utkast INPUT=tmp/mitt-begrep.json
```

Resultatet er YAML-blokker som kan limast inn i instansfila
(`src/linkml/begrepskatalog/<katalognavn>/examples/<katalognavn>-eksempel.yaml`):

```yaml
# Generert av mcp-linkml-begrep-utkast — legg til i instansfila di
# Begrep: https://begrep.eksempel.no/mitt-begrep

begrep:
- id: https://begrep.eksempel.no/mitt-begrep
  anbefalt_term:
  - mitt begrep
  har_definisjon:
  - https://begrep.eksempel.no/def/mitt-begrep-nb
  identifikator_literal: https://begrep.eksempel.no/mitt-begrep
  kontaktpunkt_vcard:
  - https://begrep.eksempel.no/kontakt/begrepsansvarleg
  utgjevar: https://data.norge.no/organizations/<orgnr>
  fagomrade:
  - https://psi.norge.no/los/tema/<slug>
definisjoner:
- id: https://begrep.eksempel.no/def/mitt-begrep-nb
  tekst: ein klar og presis formulering av kva omgrepet tyder
  kjelde_relasjon: https://data.norge.no/vocabulary/relationship-with-source-type#self-composed
organisasjonar:
- id: https://data.norge.no/organizations/<orgnr>
kontaktpunkt:
- id: https://begrep.eksempel.no/kontakt/begrepsansvarleg
```

### Profil for eigen organisasjon

Lag `src/mcp-linkml-begrep-utkast/profiles/<org>.yaml` for å forhåndssette
`base_uri`, `utgjevar_uri` og kontaktpunktmønster — så slepp du å oppgje desse
for kvart kall. Sjå `profiles/brreg.yaml` som døme.

### Obligatoriske felt per `Begrep`

| Felt | Merknad |
|---|---|
| `id` | URI under org-eige domene |
| `anbefalt_term` | Minst éin; nb og nn tilrådast |
| `definisjon` eller `har_definisjon` | Minst éin |
| `identifikator_literal` | Same verdi som `id` |
| `kontaktpunkt_vcard` | URI til kontaktpunkt-objekt definert lokalt |
| `utgjevar` | URI til organisasjon-objekt definert lokalt |

---

## 3 — Valider

```bash
# Rask syntaksvalidering direkte mot skjema (via mcp-begrep-generator):
# → bruk valider_begrep-verktøyet med yaml_innhald og skjema_sti

# Full policy-validering — tilrådast før kvar commit:
make mcp-validate \
  SCHEMA=src/linkml/begrepskatalog/<katalognavn>/<katalognavn>-schema.yaml \
  POLICY=bronze
```

| Policy | Sjekkar |
|---|---|
| `bronze` | `id`, `name`, `description`; alle klasser har identifikator |

---

## 4 — Generer RDF/Turtle

```bash
make domain-gen-examples DOMAIN=begrepskatalog
```

Output: `generated/begrepskatalog/<katalognavn>/<katalognavn>-eksempel.ttl`

Denne Turtle-fila er berre for lokal kontroll av at YAML-instansen vert korrekt
serialisert. For publisering til Felles Begrepskatalog — sjå
[Publiser til Felles Begrepskatalog](publisering-begrep.md).

---

## 5 — CI-pipeline

Ingen endringar i workflowfiler nødvendig. `validate.yml` og `generate.yml` fangar
automatisk opp nye skjema under `src/linkml/begrepskatalog/`. Pipelinen køyrer ved push til
`main` når filer under `src/linkml/begrepskatalog/**` er endra.

---

## 6 — Datafil for publisering (valfritt)

Berre nødvendig for katalogar som skal publiserast til Felles Begrepskatalog.

**1.** Lag `src/linkml/begrepskatalog/<katalognavn>/data/<katalognavn>/<katalognavn>.yaml` med stabile produksjons-URI-ar.
Bruk `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml` som mal — same struktur som eksempelfila,
men utan «under utvikling»-merknader og med permanente `id:`-verdiar.

**2.** Lag ei tom URI-lock-fil:

```bash
cat > src/linkml/begrepskatalog/<katalognavn>/published-uris.lock << 'EOF'
# Publiserte URI-ar for <katalognavn> — IKKJE endre eller slett eksisterande linjer.
# Nye URI-ar leggast til nedst etter publisering.
EOF
```

**3.** Valider datafila mot publiseringspolicyen:

```bash
make mcp-validate \
  SCHEMA=src/linkml/begrepskatalog/<katalognavn>/<katalognavn>-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=src/linkml/begrepskatalog/<katalognavn>/data/<katalognavn>/<katalognavn>.yaml
```

For fullstendig rettleiing om registrering og URI-stabilitet:
sjå [Publiser til Felles Begrepskatalog](publisering-begrep.md).

---

## Sjå òg

- [Begrep - domeneindeks](begrep/index.md)
- [Publiser til Felles Begrepskatalog](publisering-begrep.md) — pipeline og URI-stabilitet
- [`specs/begrep-modellering.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/begrep-modellering.md) — fullstendig teknisk spesifikasjon
- [`src/mcp-linkml-begrep-utkast/README.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-begrep-utkast/README.md) — dokumentasjon for MCP-serveren
