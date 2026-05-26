# Rettleiing: ny begrepskatalog

Denne rettleiinga viser korleis du oppretter ein ny begrepskatalog i repoet —
frå filstruktur til RDF-eksport klar for Felles Begrepskatalog.

!!! note "Skil seg frå ny domenemodell"
    Begrepskatalogar har ein eigen arbeidsflyt. `make new-model` gjeld **ikkje** her —
    skjemaet er trivielt og vert skrive for hand. Bruk `mcp-linkml-begrep-utkast`
    for å generere YAML-instansar, ikkje `mcp-linkml-modell-utkast`.

    | | Ny begrepskatalog | Ny domenemodell |
    |---|---|---|
    | Scaffold | Manuelt (kopier skjema) | `make new-model` |
    | Import | `skos-ap-no` | `dcat-ap-no` / `dqv-ap-no` |
    | Generator | `mcp-linkml-begrep-utkast` | `mcp-linkml-modell-utkast` |
    | RDF-eksport | `example_rdf: true` (krav) | Valfritt |

---

## 0 — Føresetnader (éin gong)

```bash
make check-prereqs
make mcp-begrep-build    # byggjer mcp-linkml-begrep-utkast
make mcp-val-build       # byggjer mcp-linkml-validator (for bronze-validering)
```

---

## 1 — Opprett filstruktur

```bash
mkdir -p src/linkml/begrep/<katalognavn>
# examples/begrep/ finst allereie
```

**Namnemønster:** `<org>-begrep` eller `<fagdomene>-begrep`, t.d. `digdir-begrep`, `ssb-begrep`, `ngr-begrep`.

---

## 2 — Skriv `<katalognavn>-schema.yaml`

Skjemaet er minimalt — all semantikk kjem frå den importerte `skos-ap-no`.
Kopier frå `src/linkml/begrep/brreg-begrep/brreg-begrep-schema.yaml` og endre
`id`, `name`, `title` og `default_prefix`:

```yaml
id: https://data.norge.no/linkml/<katalognavn>
name: <katalognavn>
title: <Organisasjon> – Begrepskatalog
version: "1.0.0"

prefixes:
  linkml: https://w3id.org/linkml/

default_prefix: https://data.norge.no/linkml/<katalognavn>/
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

---

## 3 — Skriv `generate.yaml`

```yaml
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
  example_rdf: true    # konverterer instansfila til RDF/Turtle
data_policy: felles-begrepskatalog   # berre for katalogar som skal publiserast
```

`example_rdf: true` er obligatorisk — det er dette som produserer SKOS/Turtle for eksport.

`data_policy` peikar til publiseringspolicyen som `make domain-validate-data`
nyttar for å validere filer under `data/`. Berre nødvendig viss katalogen
skal publiserast til Felles Begrepskatalog.

---

## 4 — Generer YAML-instansar

Bruk `opprett_begrep`-verktøyet i `mcp-linkml-begrep-utkast` til å byggje
YAML-blokkar. Verktøyet kan køyrast av ein AI-assistent med MCP-støtte
(t.d. Claude Code med MCP-konfigurasjon) eller manuelt via Makefile:

```bash
# List tilgjengelege profiler
make mcp-begrep-list-profiles

# List gyldige LOS-tema-URI-ar
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"list_los_tema","arguments":{}}}' \
  | make mcp-begrep-run
```

### Eksempel — generer eitt begrep

Send dette til serveren (t.d. via AI-assistent eller skript):

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

Resultatet er ein `BegrepContainer`-blokk som kan limast inn i instansfila
(`examples/begrep/<katalognavn>-eksempel.yaml`) under dei tilsvarande listene.

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

## 5 — Valider

```bash
# Rask syntaksvalidering direkte mot skjema (via mcp-begrep-generator):
# → bruk valider_begrep-verktøyet med yaml_innhald og skjema_sti

# Full policy-validering — tilrådast før kvar commit:
make mcp-validate \
  SCHEMA=src/linkml/begrep/<katalognavn>/<katalognavn>-schema.yaml \
  POLICY=bronze
```

| Policy | Sjekkar |
|---|---|
| `bronze` | `id`, `name`, `description`; alle klasser har identifikator |

---

## 6 — Generer RDF/Turtle

```bash
make domain-gen-examples DOMAIN=begrep
```

Output: `generated/begrep/<katalognavn>/<katalognavn>-eksempel.ttl`

Denne Turtle-fila er SKOS-kompatibel og kan importerast til
[Felles Begrepskatalog](https://data.norge.no/concepts) via Begrepskatalog-API.

---

## 7 — CI-pipeline

Ingen endringar i workflowfiler nødvendig. `validate.yml` og `generate.yml` fangar
automatisk opp nye skjema under `src/linkml/begrep/`. Pipelinen køyrer ved push til
`main` når filer under `src/linkml/begrep/**`, `examples/begrep/**` eller
`data/begrep/**` er endra.

---

## 8 — Datafil for publisering (valfritt)

Berre nødvendig for katalogar som skal publiserast til Felles Begrepskatalog.

**1.** Lag `data/begrep/<katalognavn>.yaml` med stabile produksjons-URI-ar.
Bruk `data/begrep/brreg-begrep.yaml` som mal — same struktur som eksempelfila,
men utan «under utvikling»-merknader og med permanente `id:`-verdiar.

**2.** Lag ei tom URI-lock-fil:

```bash
cat > src/linkml/begrep/<katalognavn>/published-uris.lock << 'EOF'
# Publiserte URI-ar for <katalognavn> — IKKJE endre eller slett eksisterande linjer.
# Nye URI-ar leggast til nedst etter publisering.
EOF
```

**3.** Valider datafila mot publiseringspolicyen:

```bash
make mcp-validate \
  SCHEMA=src/linkml/begrep/<katalognavn>/<katalognavn>-schema.yaml \
  POLICY=felles-begrepskatalog \
  INSTANCE=data/begrep/<katalognavn>.yaml
```

For fullstendig rettleiing om registrering og URI-stabilitet:
sjå [Publiser til Felles Begrepskatalog](publisering-begrep.md).

---

## Sjå òg

- [Begrep – domeneindeks](begrep/index.md)
- [Publiser til Felles Begrepskatalog](publisering-begrep.md) — pipeline og URI-stabilitet
- [`specs/begrep-modellering.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/specs/begrep-modellering.md) — fullstendig teknisk spesifikasjon
- [`src/mcp-linkml-begrep-utkast/README.md`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/mcp-linkml-begrep-utkast/README.md) — dokumentasjon for MCP-serveren
