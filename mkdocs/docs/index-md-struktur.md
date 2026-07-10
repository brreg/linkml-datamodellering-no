# Struktur for `index.md` per modell

!!! note "Beskrivelse"

    Denne sida dokumenterer korleis Modell-dokumentasjon `index.md`-fila for kvar modell blir bygd opp og generert av `mkdocs/publish.sh` (t.d. `mkdocs/docs/samt/samt-bu/index.md` som publiseres som [SAMT - Kommunale integrasjonar/samt-bu](https://brreg.github.io/linkml-datamodellering-no/samt/samt-bu/) i navigasjonsmenyen til venstre i denne portalen).

## Oversikt

`index.md` fungerer som hovudsida for kvar modell i dokumentasjonsportalen. Fila blir **automatisk generert** av `mkdocs/publish.sh` (funksjonen `process_schema()`) basert på ulike kjelder:

- Genererte artefaktar frå LinkML (gen-doc, PlantUML, valideringsresultat)
- Kildefiler i `src/linkml/<domain>/<schema>/` (manifest, eksempel, description.md, CHANGELOG.md)
- Dynamisk parsing av metadata frå gen-doc-output

Tabellen under viser kvar seksjon i `index.md`, kva innhaldet er, og kvar det kjem frå.

## Seksjonsrekkjefølgje og kjelder

| # | Seksjon | Innhald | Kjelde | Script/funksjon |
|---|---|---|---|---|
| 1 | **Hovudoverskrift** | `# <schema>` | Skjemanamn frå katalognamn | `lib/sections/header.sh:generate_header()` |
| 2 | **Badge-rad** | Versjon, status, validering, lisens | Parsa frå `generated/<domain>/<schema>/docs/index.md` (gen-doc) og `src/linkml/<domain>/<schema>/validation/<versjon>/<policy>.json` (valideringsresultat) | `lib/sections/badges.sh:generate_badges()` |
| 3 | **Offisiell referanse** (valgfri) | Infoboks med lenke til ekstern spesifikasjon (t.d. Digdir) | `build.yaml` (`external_spec_url`-feltet, valfritt) | `lib/sections/external_reference.sh:generate_external_reference()` |
| 4 | **Om denne modellen** (valgfri) | Brukarorientert introduksjonstekst | `src/linkml/<domain>/<schema>/description.md` (dersom den finst) | `lib/sections/description.sh:generate_description()` |
| 5 | **Kom i gang** | Quickstart-guide med valideringskommando | `src/linkml/<domain>/quickstart.md` (valfri, med `{{SCHEMA}}`- og `{{SCHEMA_UNDERSCORE}}`-substitusjon). Fallback til hardkoda logikk dersom fila manglar. | `lib/sections/quickstart.sh:generate_quickstart()` |
| 6 | **Eksempeldatafil** (valgfri) | YAML-eksempel (første 20 linjer) + lenke til full fil | Ekstraher frå `src/linkml/<domain>/<schema>/examples/<schema>-eksempel.yaml` | `lib/sections/example.sh:generate_example()` |
| 7 | **Modellmetadata** | Tabell med name, title, description, versjon, lisens, utgjevar, status, endringsdato, utgivelsesdato | Ekstraher frå `generated/<domain>/<schema>/docs/index.md` (gen-doc) — seksjonen `## Metadata` | `lib/sections/metadata.sh:generate_metadata()` |
| 8 | **Publiseringsinfo** (valgfri) | Infoboks dersom skjema er publisert til Felles Begrepskatalog | Syner dersom `src/linkml/<domain>/<schema>/published-uris.lock` finst | `lib/sections/publishing_info.sh:generate_publishing_info()` |
| 9 | **Avhengigheiter** | Hierarkisk avhengigheitstre (direkte og transitive importar) | Generert frå `imports:`-seksjonen i skjemaet → kallar `src/assets/scripts/parse-dependency-tree.py` | `lib/sections/dependencies.sh:generate_dependencies()` |
| 10 | **ER-diagram** | PlantUML SVG-diagram (filtrert versjon → kun lokale klasser) + lenke til full versjon | Kopiert frå `generated/<domain>/<schema>/diagrams/<schema>-filtered.svg` | `lib/sections/er_diagram.sh:generate_er_diagram()` |
| **11** | **Datamodell** | Lenke til LinkML-schema (kjeldekode) | `src/linkml/<domain>/<schema>/<schema>-schema.yaml` (relativ lenke: `../../../src/linkml/<domain>/<schema>/<schema>-schema.yaml`) | `lib/sections/datamodell.sh:generate_datamodell()` |
| 12 | **Classes** | Klasseliste per subset (Obligatorisk, Anbefalt, Valgfri, Andre) | Ekstraher frå `generated/<domain>/<schema>/docs/index.md` (gen-doc) — seksjonen `## Classes` og nedover | `lib/sections/classes.sh:generate_classes_section()` |
| 13 | **Slots** | Slotliste (Verdiar, Referansar, Kodar) | Del av same ekstraksjon som Classes (gen-doc) | `lib/sections/classes.sh:generate_classes_section()` |
| 14 | **Enumerations** | Enumerationsliste | Del av same ekstraksjon som Classes (gen-doc) | `lib/sections/classes.sh:generate_classes_section()` |
| 15 | **Types** | Typeliste (inkl. importerte typar) med "Defined in"-kolonne | Del av same ekstraksjon som Classes (gen-doc) | `lib/sections/classes.sh:generate_classes_section()` |
| 16 | **Subsets** | Subsetliste | Del av same ekstraksjon som Classes (gen-doc) | `lib/sections/classes.sh:generate_classes_section()` |
| **17** | **Generated artifacts** | Tabell med lenkjer til genererte artefaktar (**modellmanifest først**, deretter SHACL, JSON-LD, JSON Schema, OWL, RDF, Python, Protobuf, PlantUML osv.) | Generert dynamisk frå `mkdocs/docs/<domain>/<schema>/` og `diagrams/`-underkatalog. Modellmanifest kopiert frå `src/linkml/<domain>/<schema>/metadata/<schema>-manifest.yaml` | `lib/sections/artifacts.sh:generate_artifacts_table()` |
| 18 | **Valideringsresultat** | Valideringsstatus, feiltal, åtvaringtal + detaljert feil-/åtvaringsliste | Generert av `src/assets/scripts/generate-validation-md.py` frå `src/linkml/<domain>/<schema>/validation/<versjon>/<policy>.json` | `lib/sections/validation.sh:generate_validation_results()` → `generate-validation-md.py` |
| 19 | **Versjonslog** | CHANGELOG-innhald som rein Markdown | Kopiert frå `src/linkml/<domain>/<schema>/CHANGELOG.md` — hovudoverskrift fjerna, alle andre auka med éin `#` | `lib/sections/changelog.sh:generate_changelog()` |
| 20 | **Kontakt** | Kontaktinformasjon (forvaltningsansvarleg, support) | Generert frå `CODEOWNERS.md`. Matchdar schema-path mot `path_patterns` per organisasjon. | `lib/sections/contact.sh:generate_contact_info()` |

## Detaljert kjeldekartlegging

### Badge-rad (seksjon 2)

Badges blir generert frå desse kjeldene:

| Badge | Parsa frå | Linjer i publish.sh |
|---|---|---|
| Versjon | `grep "^| Versjon" generated/<domain>/<schema>/docs/index.md` | 274 |
| Status | `grep "^| Status" generated/<domain>/<schema>/docs/index.md` | 275 |
| Validering | `src/linkml/<domain>/<schema>/validation/<versjon>/<policy>.json` (error_count) | 286-298 |
| Lisens | `grep "^| Lisens" generated/<domain>/<schema>/docs/index.md` | 276 |

### Avhengigheiter (seksjon 9)

Avhengigheitstreet blir bygd i to steg:

1. **`build_dependency_graph()`** (publish.sh:173-215)
   - Finn schema-fil: `src/linkml/<domain>/<schema>/<schema>-schema.yaml`
   - Ekstraher direkte importar med `sed`/`grep` frå `imports:`-seksjonen
   - Kall Python-scriptet `src/assets/scripts/parse-dependency-tree.py` for å bygge hierarkisk tre

2. **`parse-dependency-tree.py`**
   - Tar imot skjemanamn og direkte importar som argument
   - Byggjer transitivt avhengigheitstre ved å følgje importkjeda
   - Outputar ASCII-tre-diagram (t.d. `linkml:types → common-ap-no → dcat-ap-no`)

### ER-diagram (seksjon 10)

PlantUML-diagramma finst i to versjonar (sjå CLAUDE.md-seksjonen "PlantUML-diagram"):

- **Filtrert versjon** (`<schema>-filtered.svg/puml`) — kun lokale klasser, prioritert i index.md
- **Full versjon** (`<schema>.svg/puml`) — alle klasser inkl. importerte, vist som lenke "(full)"

Kjelder:

- Kopiert frå `generated/<domain>/<schema>/diagrams/` til `mkdocs/docs/<domain>/<schema>/diagrams/`
- Generert av `make gen-plantuml` (kjeldekode: `Makefile:run_gen_plantuml`, `src/assets/scripts/filter_plantuml.py`)

### Datamodell (seksjon 11)

**Ny seksjon (2026-07-09):** Lenke til LinkML-schema som kjeldekode.

**Generering:** `lib/sections/datamodell.sh:generate_datamodell()`

**Output:**
```markdown
## Datamodell

Kjelde-datamodell i LinkML-format: [`<schema>-schema.yaml`](../../../src/linkml/<domain>/<schema>/<schema>-schema.yaml)
```

**Formål:** Gi direkte tilgang til LinkML-schema-kjeldekoden (YAML) frå modellportalen. Dette skil LinkML-schemaet frå genererte artefaktar (som ligg i "Generated artifacts"-seksjonen).

**Kjelde:** `src/linkml/<domain>/<schema>/<schema>-schema.yaml` (relativ lenke frå `mkdocs/docs/<domain>/<schema>/index.md`)

### Generated artifacts (seksjon 17)

**Oppdatert (2026-07-09):** Modellmanifest lagt til som første rad i tabellen.

Artefakttabellen viser no:

1. **Modellmanifest ihht Modelldcat-ap-no** — `<schema>-manifest.yaml` (Informasjonsmodell-instans, kopiert frå `src/linkml/<domain>/<schema>/metadata/<schema>-manifest.yaml`)
2. SHACL Shapes — `<schema>-shapes.ttl`
3. JSON-LD Context — `<schema>-context.jsonld`
4. JSON Schema — `<schema>-schema.json`
5. ... (resten av artefaktane)

**Sjå:** [modellmanifest-generering.md](modellmanifest-generering.md) for fullstendig dokumentasjon av manifestgenerering.

### Valideringsresultat (seksjon 18)

Valideringsresultata blir genererte av `src/assets/scripts/generate-validation-md.py`:

1. **Les JSON-fil:**
   - `src/linkml/<domain>/<schema>/validation/<versjon>/<policy>.json`
   - Policy-verdi henta frå `build.yaml` (`validation_policy`-feltet, default: `bronze`)

2. **Finn siste versjon:**
   - `ls -v src/linkml/<domain>/<schema>/validation/` → grep versjonsnummer (semver) → tail -n1

3. **Format output:**
   - Statustabel (status, feiltal, åtvaringtal)
   - Nummererte lister for feil og åtvaringar (rein Markdown, ikkje `<details>`-blokkar)
   - Kvar feil/åtvaring viser: regelnamn, affisert element, feilmelding

### Generated artifacts (seksjon 16)

Artefakttabellen blir bygd dynamisk:

1. **Iterer gjennom `ARTIFACT_ORDER`** (definert i publish.sh:~40):
   ```
   shacl_shapes.ttl context.jsonld schema.json schema.xsd openapi.yaml asyncapi.yaml ontology.ttl schema.ttl model.py schema.proto erdiagram.md
   ```

2. **Sjekk om fil finst** i `mkdocs/docs/<domain>/<schema>/`

3. **Legg til rad** med artefaktlabel (frå `artifact_label()`) og lenke

4. **PlantUML-diagram:**
   - Legg til separat rad med lenkjer til filtrert/full SVG og PUML-kjeldekode
   - Prioriterer filtrert versjon (kun lokale klasser)

## Køyreflyt for `publish.sh`

`mkdocs/publish.sh` køyrer i fire hovudsteg (dokumentert i CLAUDE.md):

1. **Steg 1:** Rens tidlegare genererte domene-katalogar frå `mkdocs/docs/<domain>/`
2. **Steg 2:** Generer innhald per domene og skjema (parallelt) — køyrer `process_schema()` for kvart skjema
3. **Steg 3:** Generer `valideringsregler.md` og hovud-`index.md`
4. **Steg 4:** Generer `mkdocs.yml` (dynamisk nav-meny frå `generated/`-struktur)

`process_schema()` (steg 2) genererer `index.md` for eitt skjema og køyrer parallelt for alle skjema.

## Avhengigheiter mellom generatorar

Sekvensiell avhengigheitskjede for å bygge ein komplett `index.md`:

```
make gen-linkml (merge-imports)
  ↓
make gen-plantuml (diagram)
  ↓
make gen-doc (metadata, klasselister)
  ↓
make mcp-validate (valideringsresultat)
  ↓
mkdocs/publish.sh (build index.md)
  ↓
mkdocs serve (portalen er klar)
```

Alle desse køyrer automatisk via `make domain-<schema>` eller `make domain` for alle domenemodellane.

## Oppdatere innhald i `index.md`

For å endre innhaldet i ein modell sin `index.md`:

| Ønskt endring | Kvar du endrar |
|---|---|
| Hovudtittel | Ikkje redigerbar — auto-generert frå skjemanamn |
| Badge-verdiar | Endre versjon/status/lisens i `src/linkml/<domain>/<schema>/<schema>-schema.yaml` (gen-doc parsar dette) |
| Offisiell referanse | Legg til `external_spec_url` i `src/linkml/<domain>/<schema>/build.yaml` |
| Introduksjonstekst | Opprett/rediger `src/linkml/<domain>/<schema>/description.md` |
| Quickstart-kommando | Rediger `src/linkml/<domain>/quickstart.md` (eller opprett fil dersom den manglar) |
| Eksempeldatafil | Rediger `src/linkml/<domain>/<schema>/examples/<schema>-eksempel.yaml` |
| Metadata-tabell | Endre metadata i `src/linkml/<domain>/<schema>/<schema>-schema.yaml` (gen-doc genererer tabellen) |
| Avhengigheiter | Endre `imports:`-seksjonen i `<schema>-schema.yaml` |
| ER-diagram | Endre klasser/slots i `<schema>-schema.yaml` og køyr `make gen-plantuml` |
| Klasselister | Endre klasser/slots/enums i `<schema>-schema.yaml` og køyr `make gen-doc` |
| Valideringsresultat | Køyr `make mcp-validate SCHEMA=...` → genererer `validation/<versjon>/<policy>.json` |
| Versjonslog | Rediger `src/linkml/<domain>/<schema>/CHANGELOG.md` (følgj keep-a-changelog-format) |
| Kontaktinformasjon | Endre `annotations.utgiver` i `<schema>-schema.yaml` (silver-annotasjon) |

**Viktig:** `index.md` skal **aldri redigerast manuelt** — alle endringar vert overskrivne neste gong `make docs-publish` køyrer.

## Sannkjelde-hierarki

```
src/linkml/<domain>/<schema>/<schema>-schema.yaml   ← SANNKJELDE for metadata, klasser, slots
src/linkml/<domain>/<schema>/build.yaml          ← SANNKJELDE for generators + validation_policy
src/linkml/<domain>/<schema>/description.md         ← SANNKJELDE for introduksjonstekst
src/linkml/<domain>/<schema>/examples/              ← SANNKJELDE for eksempel
src/linkml/<domain>/<schema>/CHANGELOG.md           ← SANNKJELDE for versjonslog
  ↓
generated/<domain>/<schema>/                        ← Mellomlagring (gen-doc, PlantUML osv.)
  ↓
mkdocs/docs/<domain>/<schema>/index.md              ← OUTPUT (auto-generert, ikkje rediger)
```

## Relaterte filer

- **`mkdocs/publish.sh`** — hovudscript (orkestrering av steg 1-4)
- **`mkdocs/lib/copy_artifacts.sh`** — kopier genererte artefakter til `mkdocs/docs/`
- **`mkdocs/lib/generate_index.sh`** — orkestrer generering av `index.md` per skjema
- **`mkdocs/lib/sections/*.sh`** — 15 modular som genererer kvar sin seksjon i `index.md`
- **`mkdocs/lib/utils/formatters.sh`** — hjelpefunksjonar for formatering (`artifact_label`, `domain_label`)
- **`mkdocs/lib/utils/metadata_parsers.sh`** — hjelpefunksjonar for parsing av manifest, versjon, validering
- **`src/assets/scripts/parse-dependency-tree.py`** — byggjer avhengigheitstre
- **`src/assets/scripts/generate-validation-md.py`** — formaterer valideringsresultat til Markdown
- **`src/assets/scripts/filter_plantuml.py`** — filterer PlantUML-diagram til kun lokale klasser
- **`src/assets/templates/docgen/index.md.jinja2`** — Jinja2-template for gen-doc (genererer `generated/<domain>/<schema>/docs/index.md`)

## Sjå også

- **`CLAUDE.md`** — normativ kjelde for modelleringsprinsipper
- **`COMMANDS.md`** — fullstendig oversikt over make-targets
- **`mkdocs/docs/ny-domenemodell.md`** — steg-for-steg-rettleiing for å lage ny modell
