# Plan: dokumentasjon for begrepsmodellering og mcp-linkml-begrep-generator

## Bakgrunn

Tre ting er implementerte men ikkje dokumenterte:

1. **`src/linkml/begrep/brreg-begrep/`** — første begrepskatalog-skjema i repoet
2. **`examples/begrep/brreg-begrep-eksempel.yaml`** — tilhøyrande instansfil
3. **`src/mcp-linkml-begrep-generator/`** — MCP-server for generering og validering av begrepsinstansar

Dessutan manglar repoet ei generell rettleiing for «ny begrepskatalog» tilsvarende
`ny-domenemodell.md` for vanlege domenemodeller.

---

## Omfang

### Nye filer

| Fil | Innhald |
|---|---|
| `mkdocs/docs/begrep/index.md` | Domeneindeks for begrep-seksjon i portalen |
| `mkdocs/docs/ny-begrepsmodell.md` | Rettleiing: opprett ny begrepskatalog steg for steg |
| `src/mcp-linkml-begrep-generator/README.md` | Kildekode-README for generatoren |

### Oppdaterte filer

| Fil | Kva som endrast |
|---|---|
| `mkdocs/mkdocs.yml` | Legg til `begrep`-seksjon og `ny-begrepsmodell` i nav |
| `mkdocs/docs/index.md` | Oppdater domenetabell, skjematabell, katalogstruktur og kom-i-gang |
| `README.md` (rot) | Same endringar som `index.md` |

> `mkdocs/docs/begrep/brreg-begrep/index.md` vert generert automatisk av
> `make domain-gen-doc DOMAIN=begrep` og skal ikkje skrivast for hand.

---

## Rekkefølgje og avhengigheiter

```
1. src/mcp-linkml-begrep-generator/README.md    (sjølvstendig)
2. mkdocs/docs/begrep/index.md                   (sjølvstendig)
3. mkdocs/docs/ny-begrepsmodell.md               (lesar README frå steg 1)
4. mkdocs/mkdocs.yml                             (peikar til steg 2 og 3)
5. mkdocs/docs/index.md  +  README.md            (siste: oppsummerer alt)
```

---

## Detaljert innhald per fil

---

### 1. `src/mcp-linkml-begrep-generator/README.md`

Kildekode-README. Same format som `src/mcp-linkml-generator/README.md`.

**Seksjonar:**

- **Bruk** — dei tre viktigaste Makefile-kommandoane:
  ```bash
  make mcp-begrep-build
  make mcp-begrep-list-profiles
  # generer YAML via MCP-verktøyet opprett_begrep (eksempelkall)
  ```
  Eitt eksempel-JSON-kall til `opprett_begrep` med `profil: brreg` og alle parametrar.

- **MCP-verktøy** — tabell med dei fire verktøya:

  | Verktøy | Skildring |
  |---|---|
  | `opprett_begrep` | Genererer BegrepContainer-YAML frå strukturerte parametrar (profil, slug, termar, definisjonar, fagomrade) |
  | `valider_begrep` | Validerer ei YAML-instansfil mot eit skos-ap-no-basert skjema (SchemaView med merge_imports) |
  | `list_profiles` | Listar tilgjengelege profiler med namn og skildring |
  | `list_los_tema` | Returnerer statisk liste over gyldige LOS-tema URI-ar |

- **Profiler** — kort forklaring + tabell over konfig-nøklar (same nøklar som i specsn).
  To eksempel-profiler: `default` (krev alle parametrar eksplisitt) og `brreg` (forhåndssett base_uri og utgjevar_uri).
  Korleis legg ein til ny profil: legg til `profiles/<org>.yaml`, ingen kodeendring.

- **Generert YAML-struktur** — kva `opprett_begrep` produserer:
  - `begrep`-seksjon med éin instans
  - `definisjoner` med eitt objekt per oppgjeve språk (fallback: nb-tekst om nn/en-tekst manglar)
  - `organisasjonar`- og `kontaktpunkt`-stub

- **Avgrensingar** — tre punkt:
  - `valider_begrep` er eit rask syntakssjekk; køyr `mcp-validate POLICY=bronze` for full validering
  - `list_los_tema` er statisk; ved oppdatering av LOS må `los_tema.py` oppdaterast og containeren byggjast på nytt
  - `mcp-linkml-validator` sin policy-validering av begrep-skjemaet (`mcp-validate SCHEMA=... POLICY=bronze`) er uendra og framleis tilrådast

- **NB! Etter generering** — same mønster som generator-README:
  Generert YAML er eit utkast. Brukar må sjekke/fylle:
  1. `kontaktpunkt`-objektet (kun `id`-stub generert; treng `fn`, `hasEmail` m.m.)
  2. `identifikator_literal` (sett automatisk lik `id`, men verifiser at base_uri er korrekt)
  3. `sja_ogsa_omgrep`-referansar (kan peike til `data.norge.no/concepts/<uuid>`)
  4. `samlingar`-seksjon (genererast ikkje automatisk; legg til manuelt)

---

### 2. `mkdocs/docs/begrep/index.md`

Domeneindeks for begrep-seksjonen. Same format som `mkdocs/docs/samt/index.md`.

**Innhald:**

```markdown
# Begrep – Begrepskatalogmodellar

Begrepskatalogar modellert i LinkML-format etter
[SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep).
Instansfiler i YAML vert validert og konvertert til SKOS/RDF for publisering til
Felles Begrepskatalog.

| Modell | Beskriving | Tilgjengelege artefakter |
|--------|-----------|--------------------------|
| [brreg-begrep](brreg-begrep/index.md) | Registerenheten i Brønnøysund – Begrepskatalog | JSON-LD kontekst · JSON Schema · RDF/Turtle skjema · ER-diagram (Mermaid) · Eksempeldata (Turtle) |
```

Legg til ei kort note om at `begrep`-domenet skil seg frå andre domener:
AP-NO-profilane (`skos-ap-no`) er allereie ferdigmodellerte; ein ny begrepskatalog treng
berre ei containerklasse. Sjå [Ny begrepskatalog](../ny-begrepsmodell.md) for steg-for-steg.

---

### 3. `mkdocs/docs/ny-begrepsmodell.md`

Rettleiing for å opprette ein ny begrepskatalog. Tilsvarar `ny-domenemodell.md`, men
heilt eigen arbeidsflyt — `make new-model` gjeld ikkje her.

**Seksjonar:**

#### Kvifor eigen rettleiing?

Kort forklaring: begrep-domenet importerer `skos-ap-no` (som allereie har alle
klasser og slots), og workflow brukar `mcp-linkml-begrep-generator` i staden for
`mcp-linkml-generator`. RDF-genereringa (`example_rdf: true`) er essensielt for
eksport til Felles Begrepskatalog.

#### 0 — Føresetnader (éin gong)

```bash
make check-prereqs
make mcp-begrep-build      # byggjer mcp-linkml-begrep-generator
make mcp-val-build         # byggjer mcp-linkml-validator (for bronze-validering)
```

#### 1 — Opprett filstruktur

```bash
mkdir -p src/linkml/begrep/<katalognavn>
# examples/begrep/ finst allereie
```

Namnemønster: `<org>-begrep` (t.d. `digdir-begrep`, `ssb-begrep`).

#### 2 — Skriv `<katalognavn>-schema.yaml`

Berre to delar trengs: metadata og containerklasse. Kopier frå `brreg-begrep-schema.yaml`
og endre `id`, `name`, `title` og `default_prefix`. Alle klasser og slots kjem frå
den importerte `skos-ap-no`.

Heile skjemaet (med placeholders):

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

#### 3 — Skriv `generate.yaml`

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
  example_rdf: true    # ← konverterer instansar til RDF/Turtle
```

#### 4 — Generer YAML-instansar med `opprett_begrep`

Forklar at `mcp-linkml-begrep-generator` kan brukast av ein AI-assistent med MCP-støtte
(t.d. Claude Desktop/Code med MCP-konfigurasjon), eller via Makefile direkte:

```bash
# List tilgjengelege profiler
make mcp-begrep-list-profiles

# List gyldige LOS-tema
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_los_tema","arguments":{}}}' \
  | make mcp-begrep-run
```

Forenkla eksempel-JSON for `opprett_begrep` (manuelt kall til serveren):

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

Resultatet listar inn i `examples/begrep/<katalognavn>-eksempel.yaml`. Fleire begrep
kan leggjast til i same fil under `begrep:`-lista.

#### 5 — Valider

```bash
# Rask syntaksvalidering (direkte mot skjema):
make mcp-begrep-run
# → bruk valider_begrep-verktøyet med yaml_innhald og skjema_sti

# Full policy-validering (tilrådast):
make mcp-validate \
  SCHEMA=src/linkml/begrep/<katalognavn>/<katalognavn>-schema.yaml \
  POLICY=bronze
```

#### 6 — Generer RDF/Turtle

```bash
make domain-gen-examples DOMAIN=begrep
```

Output: `generated/begrep/<katalognavn>/<katalognavn>-eksempel.ttl`

Denne Turtle-fila er SKOS-kompatibel og kan importerast til Felles Begrepskatalog.

#### 7 — CI-pipeline

Ingen endringar i workflow-filer. `validate.yml` og `generate.yml` oppdaga automatisk
begrep-domenet når `begrep` vart lagt til domenematrisen.

Pipelinen køyrer automatisk ved push til `main` om filer under `src/linkml/begrep/**`
eller `examples/begrep/**` er endra.

#### Samandrag — viktige poeng

Lita tabell med dei viktigaste skilnadane frå `ny-domenemodell.md`:

| | Ny begrepskatalog | Ny domenemodell |
|---|---|---|
| Scaffold | Manuelt (kopier skjema) | `make new-model` |
| Import | `skos-ap-no` | `common-ap-no` / AP-NO-profil |
| Generator | `mcp-linkml-begrep-generator` | `mcp-linkml-generator` |
| RDF-eksport | `example_rdf: true` i generate.yaml | Valfritt |
| Valideringspolicy | `bronze` (same krav) | `bronze` / `silver` / `gold` |

---

### 4. `mkdocs/mkdocs.yml`

To endringar i `nav:`-blokken:

**a) Legg til `ny-begrepsmodell` under `Rettleiingar`:**

```yaml
nav:
  - Rettleiingar:
      - Ny domenemodell: ny-domenemodell.md
      - Ny begrepskatalog: ny-begrepsmodell.md    # ← ny linje
      - Generatorkonfigurasjon: generate-config.md
```

**b) Legg til `Begrep`-seksjon mellom `AP-NO` og `FAIR` (eller til slutt — vurder alfabetisk):**

```yaml
  - 'Begrep – Begrepskatalogmodellar':
      - begrep/index.md
      - 'brreg-begrep': begrep/brreg-begrep/index.md
```

Plassering: etter `AP-NO`-seksjonen (begrep er nærast knytt til skos-ap-no).

> `begrep/brreg-begrep/index.md` finst ikkje i kjelda — ho vert generert av
> `make domain-gen-doc DOMAIN=begrep` i CI. `validation: links: not_found: ignore`
> i mkdocs.yml handterer dette.

---

### 5. `mkdocs/docs/index.md`

Tre endringar:

**a) Kom-i-gang-blokken** — legg til `mcp-begrep-build` i byggesteg:

```bash
# 1. Bygg container-images (én gang)
make linkml-build-docker && make python-build-docker \
  && make mcp-val-build && make mcp-gen-build && make mcp-begrep-build
```

**b) Domenetabell** — legg til `begrep`-rad:

| Domene | Beskrivelse | Dokumentasjon |
|---|---|---|
| begrep | Begrepskatalogmodellar etter SKOS-AP-NO-Begrep. Instansar i YAML eksportert til SKOS/RDF for Felles Begrepskatalog. | [SKOS-AP-NO-Begrep](https://data.norge.no/specification/skos-ap-no-begrep) |

**c) Skjematabell** — legg til `begrep`-rad:

| Domene | Skjema | Beskrivelse | Dokumentasjon |
|---|---|---|---|
| begrep | brreg-begrep | Registerenheten i Brønnøysund – Begrepskatalog | |

**d) Katalogstruktur** — legg til `mcp-linkml-begrep-generator` i trestrukturen:

```
│   ├── mcp-linkml-validator/        # MCP-server: policy-basert validering
│   ├── mcp-linkml-generator/        # MCP-server: JSON Schema → LinkML
│   └── mcp-linkml-begrep-generator/ # MCP-server: generering av begrepsinstansar
```

---

### 6. `README.md` (rot)

Same endringar som `index.md`:
- `mcp-begrep-build` i byggesteg
- `begrep` i domenetabell
- `brreg-begrep` i skjematabell
- `mcp-linkml-begrep-generator` i katalogstruktur

---

## Kva som IKKJE er ein del av planen

- `specs/begrep-modellering.md` er allereie komplett og treng ikkje endrast.
  Han er intern spec, ikkje portaldokumentasjon.
- Automatisk genererte `begrep/brreg-begrep/index.md`-sidene treng inga manuell
  handling — dei kjem av `make domain-gen-doc DOMAIN=begrep` i CI.
- `specs/mcp-linkml-begrep-generator.md` og `specs/mcp-linkml-begrep-validator.md`
  er interne spesifikasjonar som ikkje skal publiserast i portalen.

---

## Avvegingar

**`ny-begrepsmodell.md` vs. utviding av `ny-domenemodell.md`**:
Begrepskatalogar har eiga filstruktur, anna generator, og eit krav om RDF-eksport
som ikkje finst i vanlege domenemodeller. Ein separat rettleiing er klarare enn å
blande dei to arbeidsflytane.

**Plassering av begrep i nav**:
Etter AP-NO er naturleg fordi begrep importerer `skos-ap-no`. Alternativet er
alfabetisk (mellom AP-NO og FAIR). AP-NO-plassering er tilrådast.

**README i kildekodekatalogen vs. portaldokumentasjon**:
`src/mcp-linkml-begrep-generator/README.md` er primærdokumentasjonen for
utviklarar som les kjelda direkte. Portalen (`ny-begrepsmodell.md`) er meir
oppgåveorientert — begge trengst.

**Inga MkDocs-side for mcp-linkml-begrep-generator**:
`mcp-linkml-generator` og `mcp-linkml-validator` har heller ingen eigne portalsider
— dei er dokumenterte i `ny-domenemodell.md`. Same mønster for begrep-generator:
dokumentert i `ny-begrepsmodell.md`, ikkje eigen side.
