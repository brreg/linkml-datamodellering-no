# Plan: Demo-repo som bootstrapper LinkML frå dette repoet

**Kortnamn:** `plan-demo-repo-dcat-ap-no`  
**Mål:** Lage eit offentleg tilgjengeleg demo-repo (`brreg/linkml-datamodellering-demo`) som viser korleis ein
ekstern verksemnd bootstrappar LinkML-modellering frå `linkml-datamodellering-no` og lagar
ein enkel domenemodell som inkluderer `dcat-ap-no`.

---

## Bakgrunn

`bootstrap.sh` i dette repoet gjer at eksterne verksemder kan kome raskt i gang med
LinkML-modellering basert på norske AP-NO-profil ar. Men det finst ingen fungerande
demo-repo som viser end-to-end-flyten: frå `curl bootstrap.sh` til ein validert
`dcat-ap-no`-basert modell med eksemplar og CI/CD-integrasjon.

Eit slikt demo-repo tener to formål:
1. **Rettleiing for nye brukarar** — dei kan klone eller bruke det som referanse
2. **Røyktesting av bootstrap-infrastrukturen** — CI-pipe, container-images på GHCR,
   reusable workflow — alt saman vert verifisert av eit eksternt repo som faktisk nyttar det

Demoen er eit separat GitHub-repo (`brreg/linkml-datamodellering-demo`) — **ikkje** ein
underkatalog i dette repoet. Han skal vere så minimal som mogleg: éin modell, éi eksempelfil,
éin Makefile, CI.

---

## Designavgjersler

### Kva modell?

Ein **kommunal datakatalog** (`kommunal-datakatalog`): ein enkel katalog der ein
norsk kommune registrerer sine datasett. Modellen:

- Importerer `dcat-ap-no-schema` via HTTP (`raw.githubusercontent.com`)
- Legg til éin ny klasse `KommunalKatalog` som spesialiserer `dcat:Catalog`
  ved å gjere `kommunenummer` til ein obligatorisk eigeskap
- Legg til `KommunaltDatasett` som spesialiserer `dcat:Dataset` med
  `saksnummer` (valfri)

Dette er representativt: det viser import + utviding + eigendefinerte eigenskapar,
utan å vere komplisert.

### Lokal køyring

Ingen lokale avhengigheiter. Alle kommandoar køyrer med `podman` via ein Makefile
som spendar ein `podman run` med same image som dette repoet brukar (`linkml-local`).

Brukarar på macOS/Windows med Docker kan byte ut `podman` → `docker` utan andre endringar.

### Import-mekanisme

Skjemaet importerer via HTTP-URL med ein konkret release-tag:
```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v2.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

`linkml-datamodellering.yaml` i rota festar same versjon:
```yaml
ap-no-version: v2.0.0
```

Desse to må alltid vere i sync — Renovate kan automatisk oppgradere begge ved nye releases.
Den lokale Makefile les versjonen frå `linkml-datamodellering.yaml` for å hente riktig container-image.

### CI/CD

Brukar `reusable-validate.yml` frå dette repoet — same mekanisme som `bootstrap.sh`
set opp. Ingen eigen CI-infrastruktur i demo-repoet.

---

## Steg

### Steg 1 — Opprett GitHub-repo og køyr bootstrap

1. Opprett `brreg/linkml-datamodellering-demo` på GitHub:
   - Synleg: public
   - License: NLOD 2.0
   - Ingen init-filer (tom repo)

2. Klon lokalt og køyr bootstrap med ein konkret release-tag:
   ```bash
   git clone git@github.com:brreg/linkml-datamodellering-demo.git
   cd linkml-datamodellering-demo
   AP_NO_VERSION=v2.0.0 curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v2.0.0/bootstrap.sh | bash
   ```
   Bootstrap-scriptet set `ap-no-version: v2.0.0` i `linkml-datamodellering.yaml` automatisk.

3. Rediger `.github/workflows/linkml.yml` — bytt ut plasshaldaren med riktig stinamn:
   ```yaml
   schema: src/linkml/kommunal/kommunal-datakatalog/kommunal-datakatalog-schema.yaml
   policy: bronze
   instance: src/linkml/kommunal/kommunal-datakatalog/examples/kommunal-datakatalog-eksempel.yaml
   ```

**Leveranse:** Tom repo med `bootstrap.sh`-generert konfig og CI-workflow.

---

### Steg 2 — Lag domenemodellen

Opprett `src/linkml/kommunal/kommunal-datakatalog/kommunal-datakatalog-schema.yaml`:

```yaml
id: https://data.norge.no/demo/kommunal-datakatalog
name: kommunal-datakatalog
title: Kommunal datakatalog (demo)
description: >-
  Demo-modell som viser korleis ein kan importere dcat-ap-no frå
  linkml-datamodellering-no og leggje til kommunespesifikke eigenskapar.

version: "0.1.0"
license: https://data.norge.no/nlod/no/2.0

annotations:
  utgiver: https://data.norge.no/organizations/974760673
  endringsdato: "2026-06-16"
  utgivelsesdato: "2026-06-16"
  status: http://purl.org/adms/status/UnderDevelopment

prefixes:
  linkml:  https://w3id.org/linkml/
  dcat:    http://www.w3.org/ns/dcat#
  dct:     http://purl.org/dc/terms/
  demo:    https://data.norge.no/demo/kommunal-datakatalog/

default_prefix: https://data.norge.no/demo/kommunal-datakatalog/
default_range: string

imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v2.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema

subsets:
  Obligatorisk:
    description: Obligatoriske eigenskapar.
  Anbefalt:
    description: Anbefalte eigenskapar.
  Valgfri:
    description: Valfrie eigenskapar.

slots:
  kommunenummer:
    slot_uri: demo:kommunenummer
    range: string
    description: Firesifra kommunenummer (t.d. "4601" for Bergen).

  saksnummer:
    slot_uri: demo:saksnummer
    range: string
    description: Arkivsaksreferanse (valfri).

classes:
  DemoContainer:
    tree_root: true
    attributes:
      katalogar:
        range: KommunalKatalog
        multivalued: true
        inlined: true
        inlined_as_list: true

  KommunalKatalog:
    is_a: Katalog
    class_uri: demo:KommunalKatalog
    description: >-
      Spesialisering av dcat:Catalog for ein norsk kommune.
      Legg til kommunenummer som obligatorisk eigeskap.
    slots:
      - kommunenummer
    slot_usage:
      kommunenummer:
        required: true
        in_subset:
          - Obligatorisk
      tittel:
        required: true
        in_subset:
          - Obligatorisk
      beskriving:
        in_subset:
          - Anbefalt
      utgjevar:
        in_subset:
          - Anbefalt

  KommunaltDatasett:
    is_a: Datasett
    class_uri: demo:KommunaltDatasett
    description: >-
      Spesialisering av dcat:Dataset for kommunale datasett.
    slots:
      - saksnummer
    slot_usage:
      saksnummer:
        in_subset:
          - Valgfri
```

**Leveranse:** Kompilerbar skjemafil som importerer `dcat-ap-no-schema` via HTTP.

---

### Steg 3 — Lag manifest og eksempelfil

**`manifest.yaml`:**
```yaml
publish_external: false
data_policy: bronze

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: false
  json_schema: true
  owl: false
  owl_flags: ""
  rdf: false
  protobuf: false
  erdiagram: true
  docs: false
  plantuml: false
  example_rdf: true
```

**`examples/kommunal-datakatalog-eksempel.yaml`:**
```yaml
katalogar:
  - id: https://data.bergen.kommune.no/katalog/open-data
    kommunenummer: "4601"
    tittel:
      - value: Bergen kommunes opne datakatalog
        language: nb
    beskriving:
      - value: Oversikt over Bergen kommunes opne datasett.
        language: nb
    utgjevar: https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/964338531
```

**Leveranse:** Manifest og ein minimal, gyldig eksempelfil.

---

### Steg 4 — Lag lokal Makefile

Opprett `Makefile` i rota av demo-repoet:

```makefile
AP_NO_VERSION := $(shell grep '^ap-no-version:' linkml-datamodellering.yaml | awk '{print $$2}')
LINKML_IMAGE  := ghcr.io/brreg/linkml-local:$(AP_NO_VERSION)
SCHEMA        := src/linkml/kommunal/kommunal-datakatalog/kommunal-datakatalog-schema.yaml
INSTANCE      := src/linkml/kommunal/kommunal-datakatalog/examples/kommunal-datakatalog-eksempel.yaml
LINKML_RUN    := podman run --rm -v "$(CURDIR):/work" -w /work \
                   -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root $(LINKML_IMAGE)

.PHONY: pull lint validate generate

pull:
	podman pull $(LINKML_IMAGE)

lint:
	$(LINKML_RUN) gen-linkml --validate $(SCHEMA)

validate: lint
	$(LINKML_RUN) linkml-validate --schema $(SCHEMA) $(INSTANCE)

generate:
	mkdir -p generated
	$(LINKML_RUN) gen-json-schema $(SCHEMA) > generated/kommunal-datakatalog.schema.json
	$(LINKML_RUN) gen-shacl       $(SCHEMA) > generated/kommunal-datakatalog.shacl.ttl
	$(LINKML_RUN) gen-erdiagram   $(SCHEMA) > generated/kommunal-datakatalog.mermaid
```

**Merk:** `AP_NO_VERSION` vert lese frå `linkml-datamodellering.yaml` automatisk, slik at
lokalt image alltid samsvarer med den pinnte versjonen i schema-importen.
`make pull` er nødvendig for brukarar som ikkje allereie har imaget lokalt.

**Leveranse:** Lokal Makefile som let brukarar teste modellen utan å pushe til GitHub.

---

### Steg 5 — Lag README

`README.md` skal vere kortfatta og konsentrert om å kome i gang:

Seksjonar:
1. **Kva er dette?** — éin setning
2. **Kom i gang** — `curl bootstrap.sh`-kommandoen og eit minimum av forklaring
3. **Lokal validering** — `make pull && make validate`
4. **Importer-syntax** — korleis ein refererer til `dcat-ap-no-schema` frå eige skjema
5. **CI** — peik på `.github/workflows/linkml.yml`
6. **Lenker** — `linkml.datamodellering.no`, dette repoet

**Leveranse:** README som kan brukast som mal for nye brukararar.

---

### Steg 6 — Røyktesting av CI

1. Push alle filer til `main`
2. Verifiser at GitHub Actions køyrer `reusable-validate.yml` og at validering passerer
3. Test at `make lint` og `make validate` fungerer lokalt med podman
4. Vurder å leggje til Renovate (`renovate.json`) for automatisk oppgradering av `ap-no-version`

**Leveranse:** Grøn CI-pipeline. Demo-repo er offentleg tilgjengeleg og fungerer.

---

### Steg 7 — Dokumenter bruken i dette repoet

Legg til ein lenke og kort omtale av demo-repoet i dokumentasjonsportalen
(`mkdocs/docs/ny-domenemodell.md` eller ei ny side `mkdocs/docs/ekstern-bruk.md`):

- Korleis bootstrap.sh fungerer
- Korleis importer-via-HTTP fungerer
- Demo-repo som referansepunkt

**Leveranse:** Oppdatert portal-dokumentasjon med lenke til `brreg/linkml-datamodellering-demo`.

---

## Avhengigheiter

| Avhengigheit | Status | Merknad |
|---|---|---|
| `ghcr.io/brreg/linkml-local` publisert på GHCR | ✓ Bekrefta | Tilgjengeleg per versjon-tag. |
| `reusable-validate.yml` funksjonell | ✓ | Steg 6 kan ikkje gjennomførast om denne er broten. |
| `dcat-ap-no-schema` tilgjengeleg via `raw.githubusercontent.com/v2.0.0/…` | ✓ | Stabil per release-tag. |
| Repo-namn avklart | ✓ `brreg/linkml-datamodellering-demo` | — |

---

## Prioritert handlingsliste

| # | Tiltak | Steg | Avhengigheit |
|---|---|---|---|
| 1 | Lag GitHub-repo `brreg/linkml-datamodellering-demo` | 1 | — |
| 2 | Køyr `bootstrap.sh` og rediger workflow | 1 | Repo oppretta |
| 3 | Lag `kommunal-datakatalog-schema.yaml` | 2 | Repo og workflow |
| 4 | Lag `manifest.yaml` og eksempelfil | 3 | Skjema |
| 5 | Verifiser at `gen-linkml --validate` passerer (lint) | 2 | Skjema + podman |
| 6 | Lag lokal `Makefile` | 4 | Skjema + GHCR-image |
| 7 | Lag `README.md` | 5 | — |
| 8 | Push og verifiser CI | 6 | Alt over + GHCR |
| 9 | Oppdater portaldokumentasjon her | 7 | Demo-repo live |

---

## Opne spørsmål

1. **Renovate i demo-repoet?** Vil automatisk oppgradere `ap-no-version` i `linkml-datamodellering.yaml`
   *og* import-URL-en i skjemafila ved nye releases. Krev at Renovate-regexManageren vert konfigurert
   til å matche båe plassar. Bør vurderast etter at grunnstrukturen er på plass (Steg 6).
