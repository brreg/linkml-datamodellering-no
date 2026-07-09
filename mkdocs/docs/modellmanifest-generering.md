# Modellmanifest-generering

!!! note "Beskrivelse"

    Denne sida dokumenterer korleis modellmanifest (`<modell>-manifest.yaml`) blir automatisk generert for kvart LinkML-skjema som del av `make domain-*`-kommandoane. Manifestet er ein Informasjonsmodell-instans ihht ModelDCAT-AP-NO og samanfattar metadata om modellen frå 6 ulike kjelder.

## Oversikt

Modellmanifestet er ein YAML-datafil som inneheld metadata om eit LinkML-skjema formatert ihht [ModelDCAT-AP-NO](https://informasjonsforvaltning.github.io/modelldcat-ap-no/). Fila blir **automatisk generert** av `make domain-*` (via `gen-informasjonsmodell-instance`) og samlar metadata frå:

1. `<modell>-schema.yaml` (toppnivå-felt og annotations)
2. `build.yaml` (heimeside, har_del)
3. `CODEOWNERS.md` (kontaktpunkt)
4. Skjemaet sine lokale klasser (inneholder_modellelement)
5. Genererte artefaktar (finnes_i_format)
6. `annotations.er_profil_av` (MVP workaround for DX-PROF)

**Output:** `src/linkml/<domain>/<modell>/metadata/<modell>-manifest.yaml`

## Metadata-felt og kjelder

| ModelDCAT-felt | Kjelde | Felt i kjelde | Merknad |
|---|---|---|---|
| `id` | `<modell>-schema.yaml` | `id` | URI til modellen |
| `tittel` (nb/nn) | `<modell>-schema.yaml` | `title` → `tittel.nb`, `annotations.tittel_nn` → `tittel.nn` | LangString-transformasjon |
| `beskrivelse` (nb/nn) | `<modell>-schema.yaml` | `description` → `beskrivelse.nb`, `annotations.beskrivelse_nn` → `beskrivelse.nn` | LangString-transformasjon |
| `versjonsnummer` | `<modell>-schema.yaml` | `version` | Semantisk versjonering |
| `lisens` | `<modell>-schema.yaml` | `license` | Absolutt URI (t.d. NLOD 2.0) |
| `utgiver` | `<modell>-schema.yaml` | `annotations.utgiver` | Organisasjons-URI (data.norge.no) |
| `endringsdato` | `<modell>-schema.yaml` | `annotations.endringsdato` | ISO 8601-dato |
| `utgivelsesdato` | `<modell>-schema.yaml` | `annotations.utgivelsesdato` | ISO 8601-dato |
| `status` | `<modell>-schema.yaml` | `annotations.status` | ADMS Status-URI |
| `tema` | `<modell>-schema.yaml` | `annotations.tema` | Liste av Los-tema-URI-ar (valgfri) |
| `dekningsomraade` | `<modell>-schema.yaml` | `annotations.dekningsomraade` | Geografisk URI (valgfri) |
| `nokkelord` | `<modell>-schema.yaml` | `annotations.nokkelord` | LangString-liste (valgfri) |
| `heimeside` | (generert) | mkdocs-URL | `https://brreg.github.io/linkml-datamodellering-no/<domain>/<modell>/` |
| `er_i_samsvar_med` | `build.yaml` | `external_spec_url` + `external_spec_label` | Standard-instans (inline) |
| `har_del` | `build.yaml` | `submodels` | Liste av submodell-URI-ar |
| `kontaktpunkt` | `CODEOWNERS.md` | `organizations[].contact_uri` + `organizations[].name` | Kontaktopplysning-instans (inline) |
| `er_profil_av` | `<modell>-schema.yaml` | `annotations.er_profil_av` | MVP workaround (valgfri) |
| `inneholder_modellelement` | `<modell>-schema.yaml` | Lokale klasser frå `classes:` | Liste av class_uri (ekskl. tree_root) |
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

1. Les `<modell>-schema.yaml` (toppnivå-felt + annotations)
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
# Kjelder: <modell>-schema.yaml, build.yaml, CODEOWNERS.md, lokale klasser, genererte artefaktar

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
- [index-md-struktur.md](index-md-struktur.md) — Struktur for `index.md` per modell
- [COMMANDS.md](../../COMMANDS.md) — Kommandoreferanse (make-targets)
