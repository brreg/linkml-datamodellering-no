# Manglande make-kommandoar i COMMANDS.md

## Bakgrunn

Systematisk gjennomgang av `.PHONY`-lista og alle faktiske target-definisjonar i
`Makefile` samanlikna med kva som er dokumentert i `COMMANDS.md` (tilstanden per 2026-06-19).

Tidlegare spesifikasjonar (`commands-md-stale.md`, `commands-md-konsistent-kolonnar.md`,
`oppdater-commands-md-roundtrip.md`) er utførte og lukka. Denne specen dekkjer eit
nytt sett med avvik.

---

## Metodikk

Gjennomgang av alle `.PHONY`-deklarerte og faktisk definerte targets:
- **Utelate:** interne CI-targets (`domain-gen-*`, `schema-gen-*`, `domain-validate-*`,
  `_gource-render`), deprecated aliassar (`mcp-build`, `mcp-run`, `mcp-smoke`,
  `mcp-test-policies`, `linkml-gen-*`, `mcp-generate`, `linkml-gen-generate`,
  `mcp-generate`) og `gen-config`/`config.mk` (auto-regenerert, ikkje brukarvendt).
- **Inkludert:** alle targets ein utviklar kan køyre manuelt.

---

## Funn

### 1. Container-image-bygging — to images manglar

`avrotize-build-docker` og `asyncapi-build-docker` er definerte i Makefile men
ikkje dokumenterte i seksjonen «Container-image-bygging».

`avrotize-build-docker` er nødvendig for `gen-xsd` (sjå funn 3).
`asyncapi-build-docker` er nødvendig for `gen-asyncapi` (sjå funn 3).

| Kommando | Image | Brukt av |
|---|---|---|
| `make avrotize-build-docker` | `localhost/avrotize-local:latest` | `gen-xsd` |
| `make asyncapi-build-docker` | `localhost/asyncapi-cli-local:latest` | `gen-asyncapi` |

---

### 2. Ny modell-seksjon — `new-org-catalog` og `new-begrepskatalog` manglar

`new-org-catalog` og `new-begrepskatalog` er i same kategori som `new-model`, men
har ingen dokumentasjon i COMMANDS.md.

| Kommando | Beskriving |
|---|---|
| `make new-org-catalog ORG=<alias>` | Opprettar katalogstruktur og boilerplate for ein ny organisasjonskatalog |
| `make new-begrepskatalog NAME=<katalognavn>` | Opprettar katalogstruktur og boilerplate for ein ny begrepskatalog |

`ny-domenemodell.md` og `ny-begrepsmodell.md` refererer til desse kommandoane — dei
burde difor vere oppdagbare òg frå COMMANDS.md.

---

### 3. Generering av artefakter — fem generatorar manglar

Desse enkeltartefakt-generatorane finst i Makefile men er ikkje lista i tabellen
«Enkeltartefakter (alle skjema)»:

| Kommando | Beskriving | Manifest-flagg |
|---|---|---|
| `make gen-proto` | Protocol Buffers-skjema | *(ingen — alltid på)* |
| `make gen-plantuml` | PlantUML-diagram + SVG (via Kroki) | *(ingen — alltid på)* |
| `make gen-xsd` | XSD-skjema via Avrotize | `xsd: true` i manifest |
| `make gen-asyncapi` | AsyncAPI 3.0-spec | `asyncapi: true` i manifest |
| `make gen-openapi` | OpenAPI 3.1-spec | `openapi: true` i manifest |

`gen-xsd`, `gen-asyncapi` og `gen-openapi` hoppar automatisk over skjema utan
tilsvarande flagg i `manifest.yaml` — det bør gå fram av dokumentasjonen.

---

### 4. `convert-data` — udokumentert datafil-konvertering

`convert-rdf` (eksempel-YAML → TTL) er dokumentert, men `convert-data` (produsjonsdata
i `data/`-underkatalogar → TTL) manglar heilt. Dei to kommandoane handterer ulike
filtypar og -stiar:

| Kommando | Kjelde | Vilkår |
|---|---|---|
| `make convert-rdf` | `src/linkml/*/examples/*-eksempel.yaml` | Alltid (med `example_rdf:` opt-out) |
| `make convert-data` | `src/linkml/*/data/*/*.yaml` | Berre `publish_external: true` i datafil-manifest |

---

### 5. `update-modellkatalog` — udokumentert vedlikehaldskommando

Oppdaterer `Informasjonsmodell`-innslag i modellkatalogen frå `annotations.*` i
alle skjema. Nødvendig å køyre etter at eit skjema legg til/endrar annotasjonar.
Finst ikkje i COMMANDS.md.

---

### 6. `check-published-uris` — udokumentert URI-validering

Verifiserer at alle URI-ar i `published-uris.lock`-filer faktisk finst i tilhøyrande
datafil. Nødvendig for organisasjonar med `publish_external: true`-krav. Ikkje i COMMANDS.md.

---

### 7. Gource-visualisering — heilt udokumentert

Tre targets for git-historikkvisualisering:

| Kommando | Beskriving | Output |
|---|---|---|
| `make gource-build` | Byggjer container-image for Gource + ffmpeg | `localhost/gource-local:latest` |
| `make gource-preview` | Lagar 30fps-preview-video av git-historikken | `tmp/gource-preview.mp4` |
| `make gource-video` | Lagar 60fps fullkvalitetsvideo av git-historikken | `tmp/gource.mp4` |

---

### 8. Unøyaktigheit: `gen-docs` køyrer også `gen-erdiagram`

`make gen-docs` i COMMANDS.md er beskriven som «HTML-klassereferanse», men Makefile
viser at target-en køyrer både `run_gen_doc` og `run_gen_erdiagram`. Dette er
truleg OK oppførsel (ER-diagram er del av docs-prosessen), men skildringa er upresis.

---

## Prioritert tiltaksliste

| # | Funn | Endring i COMMANDS.md | Prioritet |
|---|---|---|---|
| 1 ✓ | Funn 2 | Legg til `new-org-catalog` og `new-begrepskatalog` i «Ny modell»-seksjonen | Høg |
| 2 ✓ | Funn 3 | Legg til `gen-proto`, `gen-plantuml`, `gen-xsd`, `gen-asyncapi`, `gen-openapi` i enkeltartefakt-tabellen | Høg |
| 3 ✓ | Funn 4 | Legg til `convert-data` i enkeltartefakt-tabellen (eigen rad, forklaring av skilnaden frå `convert-rdf`) | Medium |
| 4 ✓ | Funn 5 | Legg til `update-modellkatalog` — ny subseksjon «Vedlikehald» under «Generering av artefakter» | Medium |
| 5 ✓ | Funn 1 | Legg til `avrotize-build-docker` og `asyncapi-build-docker` i container-image-tabellen | Medium |
| 6 ✓ | Funn 6 | Legg til `check-published-uris` under «Validering» | Lav |
| 7 ✓ | Funn 7 | Legg til ny seksjon «Gource-visualisering» med tre targets | Lav |
| 8 ✓ | Funn 8 | Rett skildring av `gen-docs` til å nemne at ER-diagram òg vert generert | Lav |

---

## Utført

Utført 2026-06-19.

Alle 8 tiltak implementerte i `COMMANDS.md`:
- Container-image-tabellen: `avrotize-build-docker` og `asyncapi-build-docker` lagt til
- «Ny modell»-seksjonen: `new-org-catalog` og `new-begrepskatalog` lagt til; duplikat «passerer bronze»-linja fjerna
- Enkeltartefakt-tabellen: `gen-proto`, `gen-plantuml`, `gen-xsd`, `gen-asyncapi`, `gen-openapi`, `convert-data` lagt til
- `gen-docs`-skildringa: «og Mermaid ER-diagram» lagt til
- Ny subseksjon «Vedlikehald» med `update-modellkatalog`
- `check-published-uris` lagt til i Validering-tabellen
- Ny seksjon «Gource-visualisering» med `gource-build`, `gource-preview`, `gource-video`

**Avvik frå plan:** `new-org-catalog` sin output-beskriving brukar `<catalog_slug>` (ikkje `<alias>-modellkatalog`)
etter gjennomgang av `new-org-catalog.sh` — `catalog_slug` kjem frå `CODEOWNERS.md`-frontmatter per organisasjon.
