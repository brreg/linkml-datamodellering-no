# Dokumenter modellmanifest-generering

## Bakgrunn

`specs/done/autogenerer-modellmanifest-i-domain-make.md` implementerte automatisk generering av modellmanifest (`<modell>-manifest.yaml`) som del av `make domain-*`-kommandoane. Implementeringa inkluderer:

- Generering av `<modell>-manifest.yaml` per skjema (Informasjonsmodell-instans ihht ModelDCAT-AP-NO)
- Integrasjon i `make domain-*` (parallell køyring etter alle gen-* kommandoar)
- Ny "Datamodell"-seksjon i `index.md` med lenke til LinkML-schema
- Modellmanifest som første rad i "Generated artifacts"-tabellen

Denne funksjonen treng dokumentasjon i dokumentasjonsportalen, tilsvarande `mkdocs/docs/index-md-struktur.md`.

## Forståing

Ny dokumentasjonsside skal:
- Dokumentere modellmanifest-generering som prosess (input → script → output)
- Inkludere tabell med same format som "Seksjonsrekkjefølgje og kjelder" i `index-md-struktur.md`
- Forklare dei 6 kjeldene som vert samla til manifestet
- Vise eksempel på generert manifest
- Dokumentere plassering i `index.md` (Datamodell-seksjon + Generated artifacts)

## Tiltak

### 1. Opprett `mkdocs/docs/modellmanifest-generering.md`

**Fil:** `mkdocs/docs/modellmanifest-generering.md` (ny)

**Struktur:**

```markdown
# Modellmanifest-generering

!!! note "Beskrivelse"

    Denne sida dokumenterer korleis modellmanifest (`<modell>-manifest.yaml`) blir automatisk generert for kvart LinkML-skjema som del av `make domain-*`-kommandoane. Manifestet er ein Informasjonsmodell-instans ihht ModelDCAT-AP-NO og samanfattar metadata om modellen frå 6 ulike kjelder.

## Oversikt

Modellmanifestet er ein YAML-datafil som inneheld metadata om eit LinkML-skjema formatert ihht [ModelDCAT-AP-NO](https://informasjonsforvaltning.github.io/modelldcat-ap-no/). Fila blir **automatisk generert** av `make domain-*` (via `gen-informasjonsmodell-instance`) og samlar metadata frå:

1. `schema.yaml` (toppnivå-felt og annotations)
2. `build.yaml` (heimeside, har_del)
3. `CODEOWNERS.md` (kontaktpunkt)
4. Skjemaet sine lokale klasser (inneholder_modellelement)
5. Genererte artefaktar (finnes_i_format)
6. `annotations.er_profil_av` (MVP workaround for DX-PROF)

**Output:** `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`

## Metadata-felt og kjelder

| ModelDCAT-felt | Kjelde | Felt i kjelde | Merknad |
|---|---|---|---|
| `id` | `schema.yaml` | `id` | URI til modellen |
| `tittel` (nb/nn) | `schema.yaml` | `title` → `tittel.nb`, `annotations.tittel_nn` → `tittel.nn` | LangString-transformasjon |
| `beskrivelse` (nb/nn) | `schema.yaml` | `description` → `beskrivelse.nb`, `annotations.beskrivelse_nn` → `beskrivelse.nn` | LangString-transformasjon |
| `versjonsnummer` | `schema.yaml` | `version` | Semantisk versjonering |
| `lisens` | `schema.yaml` | `license` | Absolutt URI (t.d. NLOD 2.0) |
| `utgiver` | `schema.yaml` | `annotations.utgiver` | Organisasjons-URI (data.norge.no) |
| `endringsdato` | `schema.yaml` | `annotations.endringsdato` | ISO 8601-dato |
| `utgivelsesdato` | `schema.yaml` | `annotations.utgivelsesdato` | ISO 8601-dato |
| `status` | `schema.yaml` | `annotations.status` | ADMS Status-URI |
| `tema` | `schema.yaml` | `annotations.tema` | Liste av Los-tema-URI-ar (valgfri) |
| `dekningsomraade` | `schema.yaml` | `annotations.dekningsomraade` | Geografisk URI (valgfri) |
| `nokkelord` | `schema.yaml` | `annotations.nokkelord` | LangString-liste (valgfri) |
| `heimeside` | (generert) | mkdocs-URL | `https://brreg.github.io/linkml-datamodellering-no/<domain>/<modell>/` |
| `er_i_samsvar_med` | `build.yaml` | `external_spec_url` + `external_spec_label` | Standard-instans (inline) |
| `har_del` | `build.yaml` | `submodels` | Liste av submodell-URI-ar |
| `kontaktpunkt` | `CODEOWNERS.md` | `organizations[].contact_uri` + `organizations[].name` | Kontaktopplysning-instans (inline) |
| `er_profil_av` | `schema.yaml` | `annotations.er_profil_av` | MVP workaround (valgfri) |
| `inneholder_modellelement` | (generert) | Lokale klasser frå `classes:` | Liste av class_uri (ekskl. tree_root) |
| `finnes_i_format` | (generert) | Genererte artefaktar i `generated/<domain>/<modell>/` | GitHub raw URL-ar til `.ttl`, `.json`, `.owl`, `.yaml` osv. |

## Genereringsprosess

### Steg 1: `make domain-*` køyrer alle generatorar

```bash
make domain-ap-no PARALLEL=16
```

Dette køyrer (i rekkjefølgje):
1. `gen-linkml` (merge-imports)
2. `gen-jsonld-context`, `gen-shacl`, `gen-python`, `gen-jsonschema`, `gen-owl`, `gen-rdf`
3. `gen-doc`, `gen-plantuml`, `gen-proto`, `gen-xsd`, `gen-openapi`, `gen-asyncapi`
4. **`gen-informasjonsmodell-instance`** (parallelt, etter alle artefaktar er genererte)

### Steg 2: `gen-informasjonsmodell-instance` samlar metadata

**Script:** `src/assets/scripts/generate-informasjonsmodell.py`

**Input:** `src/linkml/<domain>/<modell>/<modell>-schema.yaml`

**Prosess:**

1. Les `schema.yaml` (toppnivå-felt + annotations)
2. Les `build.yaml` (heimeside, submodels)
3. Parse `CODEOWNERS.md` YAML-frontmatter (match schema-path mot `path_patterns`)
4. Ekstraher lokale klasser (frå `classes:`-blokka, ekskluder `tree_root`)
5. Finn genererte artefaktar (glob `generated/<domain>/<modell>/*`)
6. Generer GitHub raw URL-ar (auto-detektert frå `git remote`)
7. LangString-transformasjon (nb/nn)
8. Inline Kontaktopplysning- og Standard-instansar

**Output:** `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`

### Steg 3: Parallell køyring

Manifestgenerering køyrer parallelt (same mønster som PlantUML-generering):

```bash
# Sekvensielt (debugging)
make domain-ap-no PARALLEL=1

# Parallelt (default: 16 jobbar)
make domain-ap-no PARALLEL=16
```

Feilhandtering: Feil vert logga, men byggeprosessen stoppar ikkje (warning).

## Eksempel: generert manifest

**Kjelde:** `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`

**Output:** `src/linkml/ap-no/dcat-ap-no/metadata/dcat-ap-no-manifest.yaml`

```yaml
# Generert av CI frå generate-informasjonsmodell.py — ikkje rediger manuelt
# Kjelder: schema.yaml, build.yaml, CODEOWNERS.md, lokale klasser, genererte artefaktar

id: https://data.norge.no/ap-no/dcat-ap-no
tittel:
  nb: DCAT-AP-NO
  nn: DCAT-AP-NO
beskrivelse:
  nb: Norsk applikasjonsprofil av DCAT-AP, modellert i LinkML med lenking framfor inlining.
  nn: Norsk applikasjonsprofil av DCAT-AP, modellert i LinkML med lenking framfor inlining.
versjonsnummer: 2.2.0
lisens: https://data.norge.no/nlod/no/2.0
utgiver: https://data.norge.no/organizations/991825827
endringsdato: '2026-07-04'
utgivelsesdato: '2023-01-01'
status: http://purl.org/adms/status/Completed

heimeside: https://brreg.github.io/linkml-datamodellering-no/ap-no/dcat-ap-no/

er_i_samsvar_med:
- id: https://informasjonsforvaltning.github.io/dcat-ap-no/
  tittel:
    nb: DCAT-AP-NO (Norsk applikasjonsprofil av DCAT-AP)
    nn: DCAT-AP-NO (Norsk applikasjonsprofil av DCAT-AP)
  har_referanse: https://informasjonsforvaltning.github.io/dcat-ap-no/

har_del:
- https://data.norge.no/ap-no/common-ap-no

kontaktpunkt:
- id: https://www.digdir.no/om-oss/kontakt-oss/887
  navn_vcard:
    nb: Digitaliseringsdirektoratet
    nn: Digitaliseringsdirektoratet
  har_kontaktside: https://www.digdir.no/om-oss/kontakt-oss/887

inneholder_modellelement:
- https://data.norge.no/ap-no/dcat-ap-no#Datasett
- https://data.norge.no/ap-no/dcat-ap-no#Katalog
- https://data.norge.no/ap-no/dcat-ap-no#Distribusjon

finnes_i_format:
- https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/generated/ap-no/dcat-ap-no/dcat-ap-no-context.jsonld
- https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/generated/ap-no/dcat-ap-no/dcat-ap-no-ontology.ttl
- https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/generated/ap-no/dcat-ap-no/dcat-ap-no-schema.json
- https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/generated/ap-no/dcat-ap-no/dcat-ap-no-shapes.ttl
- https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
```

## Plassering i dokumentasjonsportalen

Modellmanifestet vert inkludert i modell sin `index.md` på to stader:

### 1. Datamodell-seksjon (ny, etter ER-diagram)

**Sekvensnummer:** 11 (etter ER-diagram, før Classes)

**Kjelde:** `mkdocs/lib/sections/datamodell.sh`

**Output:**

```markdown
## Datamodell

Kjelde-datamodell i LinkML-format: [`dcat-ap-no-schema.yaml`](../../../src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml)
```

### 2. Generated artifacts-tabell (første rad)

**Sekvensnummer:** 16 (etter Types, før Valideringsresultat)

**Kjelde:** `mkdocs/lib/sections/artifacts.sh`

**Output:**

```markdown
## Generated artifacts

| Artefakt | Fil |
|----------|-----|
| Modellmanifest ihht Modelldcat-ap-no | [`dcat-ap-no-manifest.yaml`](dcat-ap-no-manifest.yaml) |
| SHACL Shapes | [`dcat-ap-no-shapes.ttl`](dcat-ap-no-shapes.ttl) |
| JSON-LD Context | [`dcat-ap-no-context.jsonld`](dcat-ap-no-context.jsonld) |
| ... | ... |
```

## Oppdatert seksjonsrekkjefølgje i `index.md`

| # | Seksjon | Innhald | Kjelde | Script/funksjon |
|---|---|---|---|---|
| 1 | **Hovudoverskrift** | `# <schema>` | Skjemanamn | `lib/sections/header.sh:generate_header()` |
| 2 | **Badge-rad** | Versjon, status, validering, lisens | gen-doc + validation JSON | `lib/sections/badges.sh:generate_badges()` |
| 3 | **Offisiell referanse** (valgfri) | Infoboks med lenke til ekstern spesifikasjon | `build.yaml` (`external_spec_url`) | `lib/sections/external_reference.sh:generate_external_reference()` |
| 4 | **description.md** (valgfri) | Brukarorientert introduksjonstekst | `src/linkml/<domain>/<schema>/description.md` | `lib/sections/description.sh:generate_description()` |
| 5 | **Kom i gang** | Quickstart-guide med valideringskommando | `src/linkml/<domain>/quickstart.md` | `lib/sections/quickstart.sh:generate_quickstart()` |
| 6 | **Eksempeldatafil** (valgfri) | YAML-eksempel (første 20 linjer) + lenke | `src/linkml/<domain>/<schema>/examples/<schema>-eksempel.yaml` | `lib/sections/example.sh:generate_example()` |
| 7 | **Modellmetadata** | Tabell med name, title, description, versjon, lisens, utgjevar, status, endringsdato, utgivelsesdato | `generated/<domain>/<schema>/docs/index.md` (gen-doc) | `lib/sections/metadata.sh:generate_metadata()` |
| 8 | **Publiseringsinfo** (valgfri) | Infoboks dersom skjema er publisert til Felles Begrepskatalog | `published-uris.lock` | `lib/sections/publishing_info.sh:generate_publishing_info()` |
| 9 | **Avhengigheiter** | Hierarkisk avhengigheitstre (direkte og transitive importar) | `imports:`-seksjon → `parse-dependency-tree.py` | `lib/sections/dependencies.sh:generate_dependencies()` |
| 10 | **ER-diagram** | PlantUML SVG-diagram (filtrert) + lenke til full versjon | `generated/<domain>/<schema>/diagrams/<schema>-filtered.svg` | `lib/sections/er_diagram.sh:generate_er_diagram()` |
| **11** | **Datamodell** (NY) | Lenke til LinkML-schema (kjeldekode) | `src/linkml/<domain>/<schema>/<schema>-schema.yaml` | `lib/sections/datamodell.sh:generate_datamodell()` |
| 12 | **Classes** | Klasseliste per subset (Obligatorisk, Anbefalt, Valgfri, Andre) | gen-doc `## Classes` | `lib/sections/classes.sh:generate_classes_section()` |
| 13 | **Slots** | Slotliste (Verdiar, Referansar, Kodar) | gen-doc (del av Classes) | `lib/sections/classes.sh:generate_classes_section()` |
| 14 | **Enumerations** | Enumerationsliste | gen-doc (del av Classes) | `lib/sections/classes.sh:generate_classes_section()` |
| 15 | **Types** | Typeliste (inkl. importerte typar) med "Defined in"-kolonne | gen-doc (del av Classes) | `lib/sections/classes.sh:generate_classes_section()` |
| **16** | **Generated artifacts** | Tabell med lenkjer til genererte artefaktar (**modellmanifest først**) | `mkdocs/docs/<domain>/<schema>/` + `diagrams/` | `lib/sections/artifacts.sh:generate_artifacts_table()` |
| 17 | **Valideringsresultat** | Valideringsstatus, feiltal, åtvaringtal + detaljert liste | `validation/<versjon>/<policy>.json` → `generate-validation-md.py` | `lib/sections/validation.sh:generate_validation_results()` |
| 18 | **Versjonslog** | CHANGELOG-innhald som rein Markdown | `CHANGELOG.md` | `lib/sections/changelog.sh:generate_changelog()` |
| 19 | **Kontakt** | Kontaktinformasjon (forvaltningsansvarleg, support) | `CODEOWNERS.md` | `lib/sections/contact.sh:generate_contact_info()` |

## Avhengigheiter mellom generatorar

Modellmanifest-generering krev at alle artefaktar er genererte først (for `finnes_i_format`-lista):

```
make gen-linkml (merge-imports)
  ↓
make gen-jsonld-context, gen-shacl, gen-python, gen-jsonschema, gen-owl, gen-rdf (parallelt)
  ↓
make gen-doc, gen-plantuml, gen-proto (parallelt)
  ↓
make gen-informasjonsmodell-instance (parallelt) ← SISTE STEG
  ↓
mkdocs/publish.sh (kopier manifest til mkdocs/docs/)
  ↓
mkdocs serve (portalen er klar)
```

## Kommandoar

| Kommando | Beskriving | Output |
|---|---|---|
| `make gen-informasjonsmodell-instance SCHEMA=<path>` | Generer manifest for eitt skjema | `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml` |
| `make domain-ap-no` | Generer alle artefaktar + manifest for ap-no-domenet | 10 manifest-filer (common-ap-no, dcat-ap-no, dqv-ap-no, ...) |
| `make validate-informasjonsmodell-instance SCHEMA=<path>` | Valider generert manifest mot `modelldcat-katalog-schema.yaml` | Exit 0 (OK) eller Exit 1 (feil) |
| `make gen-modellkatalog-instance` | Samlar alle manifest til per-org modellkatalogfiler | `src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml` |

## Feilhandtering

Dersom `gen-informasjonsmodell-instance` feiler for eit skjema:
- Feilmeldinga vert logga til stdout/stderr
- `make domain-*` stoppar **ikkje** (warning i staden for exit 1)
- Andre skjema i domenet vert likevel prosesserte
- Sjekk loggen for å finne kva skjema som feila og kvifor

**Vanlige feilårsaker:**
- Manglande `build.yaml`
- Manglande `annotations.utgiver` (krav i silver/gold-policy)
- Ugyldig URI-format i annotations
- CODEOWNERS.md manglar YAML-frontmatter eller matchande organisasjon

## Relaterte dokument

- [specs/done/manifest-som-modelldcat-datafil.md](../../specs/done/manifest-som-modelldcat-datafil.md) — Hovudspec for ModelDCAT-manifest-design
- [specs/done/autogenerer-modellmanifest-i-domain-make.md](../../specs/done/autogenerer-modellmanifest-i-domain-make.md) — Implementeringsspec (generering i domain-*)
- [mkdocs/docs/index-md-struktur.md](index-md-struktur.md) — Struktur for `index.md` per modell
- [COMMANDS.md](../../COMMANDS.md) — Kommandoreferanse (make-targets)
```

### 2. Legg til lenke i `mkdocs/mkdocs.yml` (nav-meny)

**Fil:** `mkdocs/mkdocs.yml`

**Seksjon:** `nav: → - Rettleiingar:`

**Plassering:** Etter `index-md-struktur.md`

```yaml
- Rettleiingar:
  - Ny domenemodell: ny-domenemodell.md
  - Modellering: modelleringstips.md
  - Publisering: publisering-oversikt.md
  - Validering: valideringsregler.md
  - Struktur for index.md: index-md-struktur.md
  - Modellmanifest-generering: modellmanifest-generering.md  # NY
```

**Obs:** `mkdocs.yml` vert regenerert av `mkdocs/publish.sh` (Steg 4), så dette må leggast til i `publish.sh` sin heredoc-blokk.

### 3. Integrer i `mkdocs/publish.sh`

**Fil:** `mkdocs/publish.sh`

**Søk etter:** `nav:` heredoc-blokka (rundt linje 400-450)

**Legg til:**

```bash
  - Rettleiingar:
    - Ny domenemodell: ny-domenemodell.md
    - Modellering: modelleringstips.md
    - Publisering: publisering-oversikt.md
    - Validering: valideringsregler.md
    - Struktur for index.md: index-md-struktur.md
    - Modellmanifest-generering: modellmanifest-generering.md  # NY
```

### 4. Verifiser i lokal mkdocs-portal

**Test:**

```bash
# Generer dokumentasjon
make docs-publish

# Start lokal portal
make docs-serve

# Opne http://localhost:8000 i nettlesar
# Naviger til "Rettleiingar" → "Modellmanifest-generering"
```

## Handlingsliste

- [x] 1. Opprett `mkdocs/docs/modellmanifest-generering.md` med fullstendig innhald
- [x] 2. Legg til lenke i `mkdocs/publish.sh` (heredoc `nav:`-seksjon)
- [ ] 3. Verifiser at sida vert vist i lokal mkdocs-portal (`make docs-serve`)
- [ ] 4. Sjekk at alle lenkjer fungerer (interne referansar til specs/, COMMANDS.md, osv.)

## Utført (2026-07-09)

1. ✅ **`mkdocs/docs/modellmanifest-generering.md`** (NY) — fullstendig dokumentasjon med:
   - Oversikt over modellmanifest-generering
   - Tabell "Metadata-felt og kjelder" (19 felt med kjelde, felt i kjelde, merknad)
   - Genereringsprosess (3 steg)
   - Eksempel frå `dcat-ap-no-manifest.yaml`
   - Plassering i dokumentasjonsportalen (Datamodell-seksjon + Generated artifacts)
   - Oppdatert seksjonsrekkjefølgje i `index.md` (19 seksjoner)
   - Avhengigheiter mellom generatorar
   - Kommandoar og feilhandtering
   - Relaterte dokument (lenkjer til specs/, COMMANDS.md)

2. ✅ **`mkdocs/publish.sh`** — lagt til lenke i nav-meny (linje 473):
   ```yaml
   - Modellmanifest-generering: modellmanifest-generering.md
   ```

**Gjenståande:**
- [ ] Verifisering i lokal mkdocs-portal (krev `make docs-publish` og `make docs-serve`)
- [ ] Sjekk at interne lenkjer fungerer

## Viktige implementasjonsdetaljar

- **Tabellfelt:** Same format som `index-md-struktur.md` — kolonnane "ModelDCAT-felt", "Kjelde", "Felt i kjelde", "Merknad"
- **Eksempel:** Inkluder fullstendig YAML-eksempel frå eit reelt generert manifest (t.d. `dcat-ap-no-manifest.yaml`)
- **Oppdatert seksjonsrekkjefølgje:** Nummererte seksjons-liste som viser at "Datamodell" (11) og "Generated artifacts" (16) er oppdaterte
- **Relaterte dokument:** Lenkjer til specs/ for full implementasjonsdetalj
