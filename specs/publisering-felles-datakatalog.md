# Plan: Publisering til Felles Datakatalog

## Mål

Publisere informasjonsmodellar frå dette repoet til
[Felles Datakatalog](https://data.norge.no) via høstingsendepunkt,
i ModelDCAT-AP-NO-format (Turtle). Modellane skal vera søkbare i
data.norge.no sin modellkatalog og lenke vidare til dokumentasjonsportalen.

## Bakgrunn

Repoet inneheld LinkML-modellar for fleire offentlege domene (NGR, FINT, SAMT, OREG)
og norske applikasjonsprofiler (DCAT-AP-NO, SKOS-AP-NO, ModelDCAT-AP-NO m.fl.).
Det finst allereie:

- `src/linkml/ap-no/modelldcat-ap-no/` — norsk applikasjonsprofil for informasjonsmodellar
- `examples/ap-no/modelldcat-ap-no-eksempel.yaml` — illustrativt døme
- `tests/fixtures/modelldcat-ap-no-fixture.yaml` — fixturskjema med `tree_root` for validering

Det som manglar er:

1. Eit **reelt modellkatalog-skjema** med containerklasse og import av modelldcat-ap-no
2. Ein **kataloginstansfil** som skildrar dei faktiske LinkML-modellane i repoet
3. Ein **`felles-datakatalog`-policy** i `mcp-linkml-validator`
4. Registrering av GitHub Pages-URL som høstingsendepunkt

---

## Del 1 — Ny modellkatalog-schema: `brreg-modellkatalog`

### Plassering

```
src/linkml/modell/brreg-modellkatalog/brreg-modellkatalog-schema.yaml
examples/modell/brreg-modellkatalog-eksempel.yaml
```

### Føremål

Eit eige schema for katalog over Brønnøysundregistra sine informasjonsmodellar,
på same mønster som `brreg-begrep` importerer `skos-ap-no-schema`. Containeren
eksponerer `Modellkatalog`, `Informasjonsmodell` og aktuelle modellelementklassar.

### YAML-struktur (brreg-modellkatalog-schema.yaml)

```yaml
id: https://data.norge.no/linkml/brreg-modellkatalog
name: brreg-modellkatalog
title: Brønnøysundregistra – Modellkatalog
description: >
  Modellkatalog for Brønnøysundregistra sine informasjonsmodellar.
  Implementerer ModelDCAT-AP-NO direkte via import.
version: "1.0.0"

default_prefix: https://data.norge.no/linkml/brreg-modellkatalog/
default_range: string

prefixes:
  linkml: https://w3id.org/linkml/

imports:
  - linkml:types
  - ../../ap-no/modelldcat-ap-no/modelldcat-ap-no-schema

classes:
  ModellkatalogContainer:
    tree_root: true
    attributes:
      modellkatalogar:
        range: Modellkatalog
        multivalued: true
        inlined: true
        inlined_as_list: true
      informasjonsmodellar:
        range: Informasjonsmodell
        multivalued: true
        inlined: true
        inlined_as_list: true
      objekttypar:
        range: Objekttype
        multivalued: true
        inlined: true
        inlined_as_list: true
      kodelister:
        range: Kodeliste
        multivalued: true
        inlined: true
        inlined_as_list: true
      eigenskapar:
        range: Eigenskap
        multivalued: true
        inlined: true
        inlined_as_list: true
```

### Kataloginstansfil (brreg-modellkatalog-eksempel.yaml)

Fila skildrar Brønnøysundregistra sine reelle informasjonsmodellar.
Kvar `Informasjonsmodell` peikar til den publiserte LinkML-dokumentasjonen
på GitHub Pages. Utdrag:

```yaml
modellkatalogar:
  - id: https://brreg.no/modellkatalogar/brreg-modellkatalog
    tittel:
      - "@value": "Brønnøysundregistra – Modellkatalog"
        "@language": "nb"
    beskrivelse:
      - "@value": "Informasjonsmodellar frå Brønnøysundregistra i LinkML-format."
        "@language": "nb"
    identifikator_literal: brreg-modellkatalog
    utgiver: https://data.norge.no/organizations/974760673
    kontaktpunkt:
      - https://brreg.no/kontakt/modellforvaltning
    har_del:
      - https://brreg.no/modellkatalogar/brreg-modellkatalog/ngr-adresse
      - https://brreg.no/modellkatalogar/brreg-modellkatalog/register-over-aksjeeiere
    modell:
      - https://brreg.no/modellkatalogar/brreg-modellkatalog/ngr-adresse
      - https://brreg.no/modellkatalogar/brreg-modellkatalog/register-over-aksjeeiere
    spraak:
      - http://publications.europa.eu/resource/authority/language/NOB
    lisens: http://publications.europa.eu/resource/authority/licence/CC_BY_4_0

informasjonsmodellar:
  - id: https://brreg.no/modellkatalogar/brreg-modellkatalog/ngr-adresse
    tittel:
      - "@value": "Nasjonale grunndata – Adresse"
        "@language": "nb"
    beskrivelse:
      - "@value": "Informasjonsmodell for offisielle adresser frå Matrikkelen."
        "@language": "nb"
    utgiver: https://data.norge.no/organizations/974760673
    identifikator_literal: ngr-adresse
    informasjonsmodellidentifikator: >-
      https://brreg.github.io/linkml-datamodellering-no/ngr/ngr-adresse/
    inneholder_modellelement: []
    kontaktpunkt:
      - https://brreg.no/kontakt/modellforvaltning
    tema:
      - https://psi.norge.no/los/tema/bolig-og-eiendom
    lisens: http://publications.europa.eu/resource/authority/licence/CC_BY_4_0
```

Éin `Informasjonsmodell`-entry per schema. Prioriterte modeller:

| Modell | Domene | LOS-tema |
|---|---|---|
| `ngr-adresse` | NGR | Bolig og eiendom |
| `ngr-eiendom` | NGR | Bolig og eiendom |
| `ngr-person` | NGR | Familie og sivilstand |
| `ngr-virksomhet` | NGR | Næring, arbeid og sysselsetting |
| `register-over-aksjeeiere` | OREG | Næring, arbeid og sysselsetting |
| `samt-bu` | SAMT | Familie og sivilstand |

### URI-stabilitet

`id:`-feltet for `Modellkatalog` og `Informasjonsmodell` er permanent etter første publisering.
Bruk mønsteret `https://brreg.no/modellkatalogar/brreg-modellkatalog/<schema-name>`.

Opprett `src/linkml/modell/brreg-modellkatalog/published-uris.lock` etter same mønster
som `specs/publisering-felles-begrepskatalog.md § URI-stabilitet`.

---

## Del 2 — Generering og publisering av Turtle

### Pipeline

`make convert-rdf` oppdagar automatisk `examples/modell/brreg-modellkatalog-eksempel.yaml`
og konverterer ho til Turtle ved hjelp av `brreg-modellkatalog-schema.yaml`:

```
examples/modell/brreg-modellkatalog-eksempel.yaml
  → make convert-rdf
  → generated/modell/brreg-modellkatalog/brreg-modellkatalog-eksempel.ttl
  → GitHub Actions (generate.yml) publiserer til GitHub Pages
```

### Publisert URL

```
https://brreg.github.io/linkml-datamodellering-no/modell/brreg-modellkatalog/brreg-modellkatalog-eksempel.ttl
```

### Validering

```bash
make mcp-validate \
  SCHEMA=src/linkml/modell/brreg-modellkatalog/brreg-modellkatalog-schema.yaml \
  POLICY=felles-datakatalog
```

---

## Del 3 — Policy: `felles-datakatalog`

### Føremål

Validerer at eit modellkatalogskjema (t.d. `brreg-modellkatalog-schema.yaml`) er
strukturelt klart for publisering til Felles Datakatalog:

- Importerer ModelDCAT-AP-NO (direkte eller transitivt)
- Containerklassen eksponerer `Modellkatalog` og `Informasjonsmodell`
- `Modellkatalog` har alle obligatoriske ModelDCAT-AP-NO-slots
- `Informasjonsmodell` har alle obligatoriske og anbefalte slots

Policyen arvar `bronze` (schema `id`/`name`, HTTP-URI-sjekk).

### Plassering

```
src/mcp-linkml-validator/policies/felles-datakatalog.yaml
```

### YAML-struktur

```yaml
version: 1
extends: bronze

description: >
  Policy for modellkatalogskjema som skal publiserast til Felles Datakatalog.
  Validerer at skjemaet importerer ModelDCAT-AP-NO og eksponerer dei nødvendige
  klassane og slotsa via containerklassen (tree_root).
  Arvar bronselaget: grunnleggande metadata- og modelleringskrav.

required:
  schema: [id, name]
  class: []
  slot: []

recommended:
  schema: [description, title, version]
  class: []
  slot: []

checks:

  # ── Import-krav ─────────────────────────────────────────────────────────────

  schema_importerer_modelldcat_ap_no:
    severity: error
    description: >
      Skjemaet må importere modelldcat-ap-no-schema (direkte eller transitivt).
    check: schema_imports
    must_import: modelldcat-ap-no-schema
    characteristic_class: Modellkatalog

  # ── Prefiks-krav ─────────────────────────────────────────────────────────────

  schema_brukar_dct_prefix:
    severity: error
    description: >
      Skjemaet må deklarere dct:-prefikset (Dublin Core Terms).
    check: schema_declares_standard_prefix
    standard_prefixes: [dct]

  schema_brukar_dcat_prefix:
    severity: error
    description: >
      Skjemaet må deklarere dcat:-prefikset.
    check: schema_declares_standard_prefix
    standard_prefixes: [dcat]

  # ── Containerklasse-krav ─────────────────────────────────────────────────────

  container_har_modellkatalog:
    severity: error
    description: >
      Containerklassen (tree_root) må ha eit attributt med range Modellkatalog.
    check: container_has_class
    class: Modellkatalog

  container_har_informasjonsmodell:
    severity: error
    description: >
      Containerklassen må ha eit attributt med range Informasjonsmodell.
    check: container_has_class
    class: Informasjonsmodell

  # ── Modellkatalog-krav (dcat:Catalog) — obligatoriske ─────────────────────────

  modellkatalog_har_tittel:
    severity: error
    description: Modellkatalog må ha dct:title. Obligatorisk i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Modellkatalog
    slot_uri: dct:title

  modellkatalog_har_beskrivelse:
    severity: error
    description: Modellkatalog må ha dct:description. Obligatorisk i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Modellkatalog
    slot_uri: dct:description

  modellkatalog_har_identifikator:
    severity: error
    description: Modellkatalog må ha dct:identifier. Obligatorisk i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Modellkatalog
    slot_uri: dct:identifier

  modellkatalog_har_utgjevar:
    severity: error
    description: Modellkatalog må ha dct:publisher. Obligatorisk i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Modellkatalog
    slot_uri: dct:publisher

  modellkatalog_har_kontaktpunkt:
    severity: error
    description: Modellkatalog må ha dcat:contactPoint. Obligatorisk i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Modellkatalog
    slot_uri: dcat:contactPoint

  modellkatalog_har_del:
    severity: error
    description: Modellkatalog må ha dct:hasPart. Obligatorisk i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Modellkatalog
    slot_uri: dct:hasPart

  # ── Modellkatalog-krav — anbefalte ─────────────────────────────────────────────

  modellkatalog_har_lisens:
    severity: warning
    description: Modellkatalog bør ha dct:license. Anbefalt i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Modellkatalog
    slot_uri: dct:license

  modellkatalog_har_modell:
    severity: warning
    description: >
      Modellkatalog bør ha modelldcatno:model (liste over informasjonsmodellar).
      Anbefalt i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Modellkatalog
    slot_uri: modelldcatno:model

  # ── Informasjonsmodell-krav (modelldcatno:InformationModel) — obligatoriske ───

  informasjonsmodell_har_tittel:
    severity: error
    description: Informasjonsmodell må ha dct:title. Obligatorisk i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: dct:title

  informasjonsmodell_har_utgjevar:
    severity: error
    description: >
      Informasjonsmodell må ha dct:publisher. Obligatorisk i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: dct:publisher

  # ── Informasjonsmodell-krav — anbefalte ───────────────────────────────────────

  informasjonsmodell_har_beskrivelse:
    severity: warning
    description: Informasjonsmodell bør ha dct:description. Anbefalt i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: dct:description

  informasjonsmodell_har_identifikator:
    severity: warning
    description: Informasjonsmodell bør ha dct:identifier. Anbefalt i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: dct:identifier

  informasjonsmodell_har_modellidentifikator:
    severity: warning
    description: >
      Informasjonsmodell bør ha modelldcatno:informationModelIdentifier.
      Anbefalt i ModelDCAT-AP-NO — peikar til maskinlesbar modell-URL.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: modelldcatno:informationModelIdentifier

  informasjonsmodell_har_kontaktpunkt:
    severity: warning
    description: Informasjonsmodell bør ha dcat:contactPoint. Anbefalt i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: dcat:contactPoint

  informasjonsmodell_har_lisens:
    severity: warning
    description: Informasjonsmodell bør ha dct:license. Anbefalt i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: dct:license

  informasjonsmodell_har_tema:
    severity: warning
    description: Informasjonsmodell bør ha dcat:theme (LOS-tema). Anbefalt i ModelDCAT-AP-NO.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: dcat:theme

  informasjonsmodell_har_modellelement:
    severity: warning
    description: >
      Informasjonsmodell bør ha modelldcatno:containsModelElement.
      Anbefalt i ModelDCAT-AP-NO — lister innhaldselementa i modellen.
    check: merged_class_has_slot_with_uri
    class: Informasjonsmodell
    slot_uri: modelldcatno:containsModelElement

instance_checks:

  # ── Instans-validering av utgjevar-URI ────────────────────────────────────────

  utgjevar_er_kjend_org:
    severity: error
    description: >
      dct:publisher-verdien i instansen må vere ein URI på formatet
      https://data.norge.no/organizations/<9-sifra orgnr> og liggje
      i lista over kjente utgivarar.
    check: instance_slot_uri_pattern
    slot_uri: dct:publisher
    pattern: "^https://data\\.norge\\.no/organizations/\\d{9}$"
    known_values:
      - https://data.norge.no/organizations/974760673
```

### Sjekkoversikt

#### Import og prefiks

| Check | URI / Krav | Alvor |
|---|---|---|
| `schema_imports` | `modelldcat-ap-no-schema` | error |
| `schema_declares_standard_prefix` | `dct` | error |
| `schema_declares_standard_prefix` | `dcat` | error |

#### Containerklasse

| Check | Klasse | Alvor |
|---|---|---|
| `container_has_class` | `Modellkatalog` | error |
| `container_has_class` | `Informasjonsmodell` | error |

#### Modellkatalog (dcat:Catalog)

| URI | Krav per ModelDCAT-AP-NO | Alvor |
|---|---|---|
| `dct:title` | Obligatorisk | error |
| `dct:description` | Obligatorisk | error |
| `dct:identifier` | Obligatorisk | error |
| `dct:publisher` | Obligatorisk | error |
| `dcat:contactPoint` | Obligatorisk | error |
| `dct:hasPart` | Obligatorisk | error |
| `dct:license` | Anbefalt | warning |
| `modelldcatno:model` | Anbefalt | warning |

#### Informasjonsmodell (modelldcatno:InformationModel)

| URI | Krav per ModelDCAT-AP-NO | Alvor |
|---|---|---|
| `dct:title` | Obligatorisk | error |
| `dct:publisher` | Obligatorisk | error |
| `dct:description` | Anbefalt | warning |
| `dct:identifier` | Anbefalt | warning |
| `modelldcatno:informationModelIdentifier` | Anbefalt | warning |
| `dcat:contactPoint` | Anbefalt | warning |
| `dct:license` | Anbefalt | warning |
| `dcat:theme` | Anbefalt | warning |
| `modelldcatno:containsModelElement` | Anbefalt | warning |

#### Instans-sjekkar

| Check | Slot-URI | Krav | Alvor |
|---|---|---|---|
| `instance_slot_uri_pattern` | `dct:publisher` | Mønster `https://data.norge.no/organizations/\d{9}` og i `known_values` | error |

Pluss arva frå `bronze`: `schema_id_is_http_uri`, `all_classes_have_class_uri` (warning),
`all_slots_have_slot_uri` (warning), `all_classes_have_identifier` (warning).

---

## Del 4 — Publisering via høstingsendepunkt

### Steg 1 — Opprett skjema og instansfil

1. Lag `src/linkml/modell/brreg-modellkatalog/brreg-modellkatalog-schema.yaml` (sjå Del 1)
2. Lag `examples/modell/brreg-modellkatalog-eksempel.yaml` med reelle katalogoppføringer (sjå Del 1)
3. Valider:

```bash
make mcp-validate \
  SCHEMA=src/linkml/modell/brreg-modellkatalog/brreg-modellkatalog-schema.yaml \
  POLICY=felles-datakatalog
```

### Steg 2 — Generer og verifiser Turtle

```bash
make convert-rdf
```

Sjekk at `generated/modell/brreg-modellkatalog/brreg-modellkatalog-eksempel.ttl`
inneheld gyldige `dcat:Catalog`- og `modelldcatno:InformationModel`-triples:

```bash
grep -c "dcat:Catalog\|InformationModel" \
  generated/modell/brreg-modellkatalog/brreg-modellkatalog-eksempel.ttl
```

### Steg 3 — Tilgang til administrasjonsgrensesnittet

Krev **ID-porten-innlogging** og **Altinn-rolle** for organisasjonen (Brønnøysund, orgnr. 974760673).

1. Logg inn på [data.norge.no/publishing](https://data.norge.no/publishing) med ID-porten
2. Verifiser at du ser Registerenheten i Brønnøysund i oversikta

> Same tilgangskrav som for Felles Begrepskatalog — sjå
> `specs/publisering-felles-begrepskatalog.md § Steg 2`.

### Steg 4 — Registrer høstingsendepunkt

Legg til ny datakjelde i [data.norge.no/publishing](https://data.norge.no/publishing):

| Felt | Verdi |
|---|---|
| **Utgjevar** | Registerenheten i Brønnøysund (974760673) |
| **Katalogtype** | Informasjonsmodellar |
| **Datakildentype** | ModelDCAT-AP-NO |
| **Format** | Turtle |
| **Datakjelde-URL** | `https://brreg.github.io/linkml-datamodellering-no/modell/brreg-modellkatalog/brreg-modellkatalog-eksempel.ttl` |
| **Autentisering** | (tomt — endepunktet er offentleg) |

### Steg 5 — Utløys manuell høsting og verifiser

Klikk **«Høst»** for umiddelbar høsting. Verifiser på
[data.norge.no/models](https://data.norge.no/models) at modellane viser seg
med riktig utgjevar, tittel og LOS-tema.

### Automatisk oppdatering

```
rediger examples/modell/brreg-modellkatalog-eksempel.yaml
    → make modell  (eller CI-pipeline ved push til main)
    → generated/modell/brreg-modellkatalog/brreg-modellkatalog-eksempel.ttl
    → GitHub Pages publiserer ny .ttl
    → Felles Datakatalog høstar automatisk ved neste syklus
```

---

## Del 5 — Dokumentasjon

### Ny rettleiingsside i portalen

Lag `mkdocs/docs/publisering-modell.md` etter same mønster som
`mkdocs/docs/publisering-begrep.md`. Sida bør dekke:

- Oversikt med flowchart (same mønster som begrep-sida)
- Dagleg arbeidsflyt — redigere instansfila og pushe til `main`
- Legg til ny modell i katalogen
- URI-stabilitet og `published-uris.lock`
- Registrering av høstingsendepunkt (éin gong)
- CI-pipeline-oversikt
- Sett opp for ny organisasjon

Legg sida til i `mkdocs/publish.sh` sin nav-heredoc (Rettleiingar-seksjonen)
saman med dei andre publiseringsrettleiingane:

```yaml
- Publiser til Felles Datakatalog: publisering-modell.md
```

### Automatisk portalboks

`mkdocs/publish.sh` viser allereie ein informasjonsboks og «Publisert til»-kolonne
for skjema som har `published-uris.lock`. Opprett lock-fila for `brreg-modellkatalog`
etter publisering:

```bash
cat > src/linkml/modell/brreg-modellkatalog/published-uris.lock << 'EOF'
# Publiserte URI-ar for brreg-modellkatalog — IKKJE endre eller slett eksisterande linjer.
# Nye URI-ar leggast til nedst etter publisering.
https://brreg.no/modellkatalogar/brreg-modellkatalog
EOF
```

Portalen oppdaterer seg automatisk neste gong `make publish` køyrer.

### README-oppdatering

Oppdater `README.md` med det nye `modell`-domenet i domene-tabellen:

| Domene | Skildring | Dokumentasjon |
|---|---|---|
| modell | Modellkatalog for Brønnøysundregistra sine informasjonsmodellar i ModelDCAT-AP-NO-format. Publisert til Felles Datakatalog. | [ModelDCAT-AP-NO](https://data.norge.no/specification/modelldcat-ap-no) |

### generate.yaml

Legg til `data_policy: felles-datakatalog` i
`src/linkml/modell/brreg-modellkatalog/generate.yaml` slik at CI-pipelinen
køyrer rett valideringspolicy automatisk.

---

## Kjende avgrensingar

### Modellelement-djupn

ModelDCAT-AP-NO støttar `modelldcatno:containsModelElement` som peikar til
Objekttype, Kodeliste, Attributt, Assosiasjon osv. Det er eit ope spørsmål
kor detaljert modellelementnivået skal presenterast i kataloginstansen.

**Tilråding**: Start med berre `tittel`, `utgiver` og `informasjonsmodellidentifikator`
på `Informasjonsmodell`-nivå — ikkje detaljer ned på modellelementnivå enno.
`informasjonsmodellidentifikator` peikar til dokumentasjonsportalen der full
modelldokumentasjon er tilgjengeleg.

### generate.yml og ny domene

`generate.yml` køyrer per-domene (`make ngr`, `make begrep`, osv.). Eit nytt
`modell`-domene krev at:
1. `modell` vert lagt til i domene-lista i `generate.yml`
2. `convert-rdf` i same workflow inkluderer `modell`-eksempelfiler

Sjekk `.github/workflows/generate.yml` og legg til `modell` på same vis som
dei eksisterande domena.

### LOS-tema-identifikatorar

LOS-tema-URI-ar (`https://psi.norge.no/los/tema/…`) er ikkje validerte av
LinkML — berre at feltet finst. Riktig LOS-identifikator må verifiserast
manuelt mot [psi.norge.no/los](https://psi.norge.no/los).

### modelldcatno-prefiks i LinkML

`modelldcatno:`-namespaceprefikset (`https://data.norge.no/vocabulary/modelldcatno#`)
vert ikkje automatisk løyst til fullt URI-namn i alle RDF-konverterar.
Sjekk at generert Turtle inneheld korrekte `modelldcatno:`-prefiksdefinisjonar.

---

## Referansar

- [ModelDCAT-AP-NO spesifikasjon](https://data.norge.no/specification/modelldcat-ap-no)
- [Veileder for beskrivelse av informasjonsmodeller](https://informasjonsforvaltning.github.io/veileder-modelldcat-ap-no/)
- [Felles Datakatalog — modellar](https://data.norge.no/models)
- [Registrering av høstingsendepunkt](https://data.norge.no/publishing)
- [LOS temataksonomi](https://psi.norge.no/los)
