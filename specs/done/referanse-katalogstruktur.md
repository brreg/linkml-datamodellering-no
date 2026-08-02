# Normaliser katalogstruktur for referanse-modellen

## Bakgrunn

`referanse`-modellen ligg i dag direkte under `src/linkml/referanse/`, medan alle andre modellar følgjer mønsteret `src/linkml/<domene>/<modell>/`. Dette skaper inkonsistens og gjer at referanse-katalogen ikkje passar inn i CI/CD-pipelinene sine forventningar om katalogstruktur.

`referanse` er eit rettleiingsskjema for nye utviklarar — demonstrerer hovudmønster i repoet (containerklasse, globale slots, import-hierarki osv.). Skjemaet vert ikkje brukt i produksjon.

## Mål

Flytte `referanse`-modellen frå `src/linkml/referanse/` til `src/linkml/referanse/referansemodell/` for å følgje standard domene/modell-struktur. Modellen får namnet `referansemodell` for å vere ekstra tydeleg på at dette er eit rettleiingsskjema.

## Nummererte steg

### 1. Opprette ny katalogstruktur

```bash
mkdir -p src/linkml/referanse/referansemodell
```

### 2. Flytte alle filer frå gammal til ny struktur

```bash
mv src/linkml/referanse/referanse-schema.yaml src/linkml/referanse/referansemodell/referansemodell-schema.yaml
mv src/linkml/referanse/referanse-schema-bronze.yaml src/linkml/referanse/referansemodell/referansemodell-schema-bronze.yaml
mv src/linkml/referanse/referanse-schema-silver.yaml src/linkml/referanse/referansemodell/referansemodell-schema-silver.yaml
mv src/linkml/referanse/referanse-schema-gold.yaml src/linkml/referanse/referansemodell/referansemodell-schema-gold.yaml
mv src/linkml/referanse/description.md src/linkml/referanse/referansemodell/
mv src/linkml/referanse/CHANGELOG.md src/linkml/referanse/referansemodell/
```

### 3. Opprette `build.yaml`

Opprett `src/linkml/referanse/referansemodell/build.yaml` med standard generatorkonfigurasjon:

```yaml
publish_external: false
validation_policy: bronze

generators:
  jsonld_context: true
  shacl: true
  shacl_flags: ""
  python: true
  json_schema: true
  owl: true
  owl_flags: ""
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: false
```

**Grunngjeving:**
- `example_rdf: false` fordi dette er eit rettleiingsskjema utan produksjonsdata
- `validation_policy: bronze` fordi skjemaet allereie importerer `dcat-ap-no-schema` (krever bronze minimum)

### 4. Opprette `examples/`-katalog

```bash
mkdir -p src/linkml/referanse/referansemodell/examples
```

Dersom det finst eksempelfiler i gammal struktur, flytt dei:

```bash
# Sjekk fyrst om examples-katalog finst
if [ -d "src/linkml/referanse/examples" ]; then
    mv src/linkml/referanse/examples/* src/linkml/referanse/referansemodell/examples/
    rmdir src/linkml/referanse/examples
fi

# Sjekk om det finst eksempelfiler i rotkatalogen
if ls src/linkml/referanse/*-eksempel.yaml 1> /dev/null 2>&1; then
    mv src/linkml/referanse/*-eksempel.yaml src/linkml/referanse/referansemodell/examples/
fi
```

### 5. Oppdatere metadata i `referansemodell-schema.yaml`

Oppdater desse felta i hovudskjemaet:

```yaml
id: https://example.org/linkml/referansemodell
name: referansemodell-schema
title: Referansemodell
```

Og oppdater importstiar (éin ekstra `../` fordi fila no ligg eitt nivå djupare):

```yaml
imports:
  - linkml:types
  - ../../ap-no/dcat-ap-no/dcat-ap-no-schema
```

Oppdater `default_prefix`:

```yaml
default_prefix: https://example.org/linkml/referansemodell/
```

### 6. Oppdatere bronze/silver/gold-variantane

Oppdater metadata og importstiar i:
- `referansemodell-schema-bronze.yaml` — endre `id`, `name`, `default_prefix` og importstiar
- `referansemodell-schema-silver.yaml` — endre `id`, `name`, `default_prefix` og importstiar
- `referansemodell-schema-gold.yaml` — endre `id`, `name`, `default_prefix` og importstiar

Alle følgjer same mønster som hovudskjemaet (steg 5).

### 7. Verifisere domenekatalog

Sjekk at `src/linkml/referanse/` no berre inneheld `referansemodell/`-underkatalogen:

```bash
ls -la src/linkml/referanse/
```

**Merk:** `src/linkml/referanse/` skal **ikkje** slettast — det er domene-katalogen.

### 8. Verifisere ny struktur

```bash
# Sjekk katalogstruktur
ls -la src/linkml/referanse/referansemodell/

# Lint og valider
make lint SCHEMA=src/linkml/referanse/referansemodell/referansemodell-schema.yaml

# Sjekk at import-stiagn fungerer
make gen-json-schema SCHEMA=src/linkml/referanse/referansemodell/referansemodell-schema.yaml
```

### 9. Legg til `referanse` i GitHub Actions workflows

Oppdater `matrix.domain`-lista i begge workflows for å inkludere `referanse`-domenet:

**`.github/workflows/generate.yml`:**

```yaml
matrix:
  domain: [ap-no, begrepskatalog, fair, fint, modellkatalog, ngr, oreg, referanse, samt]
```

**`.github/workflows/validate.yml`:**

```yaml
matrix:
  domain: [ap-no, begrepskatalog, fair, fint, modellkatalog, ngr, oreg, referanse, samt]
```

**Plassering:** Legg til `referanse` i alfabetisk rekkjefølgje mellom `oreg` og `samt`.

### 10. Flytt `referanse` til toppen av nav-menyen i mkdocs-portalen

Oppdater `DOMAIN_ORDER` i `mkdocs/publish.sh` (linje 304) for å flytte `referanse` først i nav-menyen:

**Før:**
```bash
DOMAIN_ORDER=("ap-no" "fair" "referanse" "ngr" "oreg" "fint" "samt" "begrepskatalog" "modellkatalog")
```

**Etter:**
```bash
DOMAIN_ORDER=("referanse" "ap-no" "fair" "ngr" "oreg" "fint" "samt" "begrepskatalog" "modellkatalog")
```

**Grunngjeving:** `referanse` er eit rettleiingsdomene for nye utviklarar — skal visast øvst i nav-menyen slik at nye brukarar finn det raskt.

### 11. Oppdatere dokumentasjon (dersom nødvendig)

Sjekk om `referanse`-modellen er referert til i:
- `CLAUDE.md` (truleg ikkje)
- `mkdocs/docs/*.md` (rettleiingar kan referere til den)
- `CONTRIBUTING.md`

Oppdater eventuelle filstiar frå `src/linkml/referanse/referanse-schema.yaml` til `src/linkml/referanse/referansemodell/referansemodell-schema.yaml`.

## Handlingsliste

- [x] Steg 1: Opprett ny katalogstruktur
- [x] Steg 2: Flytt alle filer (med omdøyping til `referansemodell-*`)
- [x] Steg 3: Opprett `build.yaml`
- [x] Steg 4: Opprett `examples/`-katalog og flytt eksempelfiler
- [x] Steg 5: Oppdater metadata og importstiar i `referansemodell-schema.yaml`
- [x] Steg 6: Oppdater metadata og importstiar i bronze/silver/gold-variantane
- [x] Steg 7: Verifiser at `src/linkml/referanse/` no berre inneheld `referansemodell/`-underkatalog
- [x] Steg 8: Verifiser ny struktur (lint + valider)
- [x] Steg 9: Legg til `referanse` i `matrix.domain` i `generate.yml` og `validate.yml`
- [x] Steg 10: Flytt `referanse` til toppen av `DOMAIN_ORDER` i `mkdocs/publish.sh`
- [x] Steg 11: Oppdater dokumentasjon (README.md linje 199)

## Utført

Alle tiltak er utførte:

- ✅ `src/linkml/referanse/referansemodell/referansemodell-schema.yaml` finst
- ✅ `src/linkml/referanse/referansemodell/build.yaml` finst
- ✅ `src/linkml/referanse/referansemodell/examples/` finst
- ✅ Schema-metadata (`id`, `name`, `default_prefix`) er oppdaterte til `referansemodell`
- ✅ Importstiar i alle YAML-filer er oppdaterte (`../../ap-no/...`)
- ✅ `make lint` gir berre warnings (same som tidlegare) — ingen errors
- ✅ `make gen-docs` fungerer med nye importstiar
- ✅ `referanse` er inkludert i `matrix.domain` i `generate.yml` (linje 167) og `validate.yml` (linje 169)
- ✅ `referanse` står fyrst i `DOMAIN_ORDER` i `mkdocs/publish.sh` (linje 304)
- ✅ Dokumentasjon oppdatert: `README.md` linje 199

Endringar:
- `.github/workflows/generate.yml:167`: lagt til `referanse` i `matrix.domain`
- `.github/workflows/validate.yml:169`: lagt til `referanse` i `matrix.domain`
- `mkdocs/publish.sh:304`: flytta `referanse` til toppen av `DOMAIN_ORDER`
- `README.md:199`: oppdatert lenke frå `[referanse](referanse/)` til `[referansemodell](referanse/referansemodell/)`
- `src/linkml/referanse/referansemodell/`: ny katalogstruktur med alle skjemafiler omdøypte
