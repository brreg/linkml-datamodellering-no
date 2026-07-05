# Struktur for `index.md` per modell

Denne sida dokumenterer korleis `index.md`-fila for kvar modell (t.d. `mkdocs/docs/samt/samt-bu/index.md`) blir bygd opp og generert av `mkdocs/publish.sh`.

## Oversikt

`index.md` fungerer som hovudsida for kvar modell i dokumentasjonsportalen. Fila blir **automatisk generert** av `mkdocs/publish.sh` (funksjonen `process_schema()`) basert på ulike kjelder:

- Genererte artefaktar frå LinkML (gen-doc, PlantUML, valideringsresultat)
- Kildefiler i `src/linkml/<domain>/<schema>/` (manifest, eksempel, description.md, CHANGELOG.md)
- Dynamisk parsing av metadata frå gen-doc-output

Tabellen under viser kvar seksjon i `index.md`, kva innhaldet er, og kvar det kjem frå.

## Seksjonsrekkjefølgje og kjelder

| # | Seksjon | Innhald | Kjelde |
|---|---|---|---|
| 1 | **Hovudoverskrift** | `# <schema>` | Skjemanamn frå katalognamn |
| 2 | **Badge-rad** | Versjon, status, validering, lisens | Parsa frå `generated/<domain>/<schema>/docs/index.md` (gen-doc) og `src/linkml/<domain>/<schema>/validation/<versjon>/<policy>.json` (valideringsresultat) |
| 3 | **Offisiell referanse** (valgfri) | Infoboks med lenke til ekstern spesifikasjon (t.d. Digdir) | `mkdocs/publish.sh:get_external_spec_url()` (kun for AP-NO-profilar) |
| 4 | **description.md** (valgfri) | Brukarorientert introduksjonstekst | `src/linkml/<domain>/<schema>/description.md` (dersom den finst) |
| 5 | **Kom i gang** | Quickstart-guide med valideringskommando | Generert dynamisk av `mkdocs/publish.sh:process_schema()` (linjer 345-390). Skiljer mellom AP-NO og domenemodell. |
| 6 | **Eksempeldatafil** (valgfri) | YAML-eksempel (første 20 linjer) + lenke til full fil | Ekstraher frå `src/linkml/<domain>/<schema>/examples/<schema>-eksempel.yaml` (linjer 392-415) |
| 7 | **Modellmetadata** | Tabell med name, title, description, versjon, lisens, utgjevar, status, endringsdato, utgivelsesdato | Ekstraher frå `generated/<domain>/<schema>/docs/index.md` (gen-doc) — seksjonen `## Metadata` (linjer 417-425) |
| 8 | **Publiseringsinfo** (valgfri) | Infoboks dersom skjema er publisert til Felles Begrepskatalog | Syner dersom `src/linkml/<domain>/<schema>/published-uris.lock` finst (linjer 428-443) |
| 9 | **Avhengigheiter** | Hierarkisk avhengigheitstre (direkte og transitive importar) | Generert av `mkdocs/publish.sh:build_dependency_graph()` (linjer 173-215) → kallar `src/assets/scripts/parse-dependency-tree.py` |
| 10 | **ER-diagram** | PlantUML SVG-diagram (filtrert versjon → kun lokale klasser) + lenke til full versjon | Kopiert frå `generated/<domain>/<schema>/diagrams/<schema>-filtered.svg` (linjer 448-469) |
| 11 | **Classes** | Klasseliste per subset (Obligatorisk, Anbefalt, Valgfri, Andre) | Ekstraher frå `generated/<domain>/<schema>/docs/index.md` (gen-doc) — seksjonen `## Classes` og nedover (linjer 471-482) |
| 12 | **Slots** | Slotliste (Verdiar, Referansar, Kodar) | Del av same ekstraksjon som Classes (gen-doc) |
| 13 | **Enumerations** | Enumerationsliste | Del av same ekstraksjon som Classes (gen-doc) |
| 14 | **Types** | Typeliste (inkl. importerte typar) med "Defined in"-kolonne | Del av same ekstraksjon som Classes (gen-doc) |
| 15 | **Subsets** | Subsetliste | Del av same ekstraksjon som Classes (gen-doc) |
| 16 | **Generated artifacts** | Tabell med lenkjer til genererte artefaktar (SHACL, JSON-LD, JSON Schema, OWL, RDF, Python, Protobuf, PlantUML osv.) | Generert dynamisk frå `mkdocs/docs/<domain>/<schema>/` og `diagrams/`-underkatalog (linjer 484-531) |
| 17 | **Valideringsresultat** | Valideringsstatus, feiltal, åtvaringtal + detaljert feil-/åtvaringsliste | Generert av `src/assets/scripts/generate-validation-md.py` frå `src/linkml/<domain>/<schema>/validation/<versjon>/<policy>.json` (linjer 533-565) |
| 18 | **Versjonslog** | CHANGELOG-innhald som rein Markdown | Kopiert frå `src/linkml/<domain>/<schema>/CHANGELOG.md` (linjer 567-580) — hovudoverskrift fjerna, alle andre auka med éin `#` |
| 19 | **Kontakt** | Kontaktinformasjon (forvaltningsansvarleg, support) | Generert av `mkdocs/publish.sh:get_contact_info()` (linjer 584-589) |

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

### Valideringsresultat (seksjon 17)

Valideringsresultata blir genererte av `src/assets/scripts/generate-validation-md.py`:

1. **Les JSON-fil:**
   - `src/linkml/<domain>/<schema>/validation/<versjon>/<policy>.json`
   - Policy-verdi henta frå `manifest.yaml` (`validation_policy`-feltet, default: `bronze`)

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
| Introduksjonstekst | Opprett/rediger `src/linkml/<domain>/<schema>/description.md` |
| Quickstart-kommando | Rediger `mkdocs/publish.sh:process_schema()` (linjer 345-390) |
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
src/linkml/<domain>/<schema>/manifest.yaml          ← SANNKJELDE for generators + validation_policy
src/linkml/<domain>/<schema>/description.md         ← SANNKJELDE for introduksjonstekst
src/linkml/<domain>/<schema>/examples/              ← SANNKJELDE for eksempel
src/linkml/<domain>/<schema>/CHANGELOG.md           ← SANNKJELDE for versjonslog
  ↓
generated/<domain>/<schema>/                        ← Mellomlagring (gen-doc, PlantUML osv.)
  ↓
mkdocs/docs/<domain>/<schema>/index.md              ← OUTPUT (auto-generert, ikkje rediger)
```

## Relaterte filer

- **`mkdocs/publish.sh`** — hovudscript som byggjer `index.md`
- **`src/assets/scripts/parse-dependency-tree.py`** — byggjer avhengigheitstre
- **`src/assets/scripts/generate-validation-md.py`** — formaterer valideringsresultat til Markdown
- **`src/assets/scripts/filter_plantuml.py`** — filterer PlantUML-diagram til kun lokale klasser
- **`src/assets/templates/docgen/index.md.jinja2`** — Jinja2-template for gen-doc (genererer `generated/<domain>/<schema>/docs/index.md`)

## Sjå også

- **`CLAUDE.md`** — normativ kjelde for modelleringsprinsipper
- **`COMMANDS.md`** — fullstendig oversikt over make-targets
- **`mkdocs/docs/ny-domenemodell.md`** — steg-for-steg-rettleiing for å lage ny modell
