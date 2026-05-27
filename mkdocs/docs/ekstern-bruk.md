# Bruk frå eksternt repo

Denne rettleiinga viser korleis eit eksternt repo kan bruke AP-NO-profilene og
verktøya i dette repoet — utan å kopiere filer eller leve inni monorepoet.

Alt du treng er **to filer** og eit enkelt bootstrap-steg.

---

## Bootstrap (éin kommando)

I rota av ditt eige repo:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/scripts/bootstrap.sh | bash
```

For å feste til ein konkret versjon:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/scripts/bootstrap.sh \
  | AP_NO_VERSION=v1.0.0 bash
```

Scriptet opprettar:

| Fil | Innhald |
|---|---|
| `linkml-datamodellering.yaml` | Pinnar AP-NO-versjonen for dette repoet |
| `.github/workflows/linkml.yml` | Minimalt GitHub Actions-oppsett for validering |

---

## AP-NO-skjema-URL-ar

Alle AP-NO-profilar er tilgjengelege via GitHub Raw med versjon-tag eller `main`:

```
https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/{versjon}/src/linkml/ap-no/{profil}/{profil}-schema.yaml
```

| Profil | Import-URL (`main`) | Brukstilfelle |
|---|---|---|
| `dcat-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema` | Datakatalogar og datasett |
| `skos-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/skos-ap-no/skos-ap-no-schema` | Omgrepsamlingar |
| `modelldcat-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema` | Informasjonsmodellar |
| `dqv-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema` | Datakvalitet |
| `cpsv-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema` | Offentlege tenester og hendingar |
| `xkos-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema` | Utvida klassifikasjon |

!!! note "`.yaml`-ending er valfri"
    LinkML løyser importer utan filending — begge variantar fungerer:
    `...dcat-ap-no-schema` og `...dcat-ap-no-schema.yaml`

Døme på importdel i eit eksternt skjema:

```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
```

---

## GitHub Actions: reusable workflows

### Validering

```yaml
# .github/workflows/linkml.yml
name: LinkML

on: [push, pull_request]

jobs:
  validate:
    uses: brreg/linkml-datamodellering-no/.github/workflows/reusable-validate.yml@main
    with:
      schema: src/linkml/mitt-domene/min-modell/min-modell-schema.yaml
      policy: bronze
```

| Input | Type | Standard | Skildring |
|---|---|---|---|
| `schema` | string | — (påkravd) | Sti til skjemafil, relativ til repo-rota |
| `policy` | string | `bronze` | Valideringspolicy: `bronze` / `silver` / `gold` / `felles-datakatalog` / `felles-begrepskatalog` |
| `instance` | string | (automatisk) | Sti til datafil — funnen automatisk i `examples/` om han ikkje er oppgitt |
| `version` | string | (frå `linkml-datamodellering.yaml`) | Overstyrer versjonen som vert lesen frå konfigurasjonsfila |

### Generering av artefakter

```yaml
jobs:
  generate:
    uses: brreg/linkml-datamodellering-no/.github/workflows/reusable-generate.yml@main
    with:
      schema: src/linkml/mitt-domene/min-modell/min-modell-schema.yaml

  use-artifact:
    needs: generate
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/download-artifact@v8
        with:
          name: ${{ needs.generate.outputs.artifact-name }}
```

Workflowen les `manifest.yaml` frå skjemakatalogen og køyrer dei generatorane som er aktiverte
(`jsonld_context`, `json_schema`, `python`, `shacl`, `owl`, `rdf`, `protobuf`, `example_rdf`).
Sjå [Generatorkonfigurasjon](generate-config.md) for detaljar.

---

## Versjonsfesta oppsett

`linkml-datamodellering.yaml` i rota av ditt repo pinnar versjonen:

```yaml
# linkml-datamodellering.yaml
ap-no-version: v1.0.0
```

Dei reusable workflowene les denne fila automatisk og nyttar rett versjon av
container-imagene og AP-NO-skjema. Du treng ikkje sende inn `version`-inputen eksplisitt.

| `ap-no-version` | Åtferd |
|---|---|
| `v1.0.0` | Brukar nøyaktig denne releasen |
| `latest` | Brukar siste release-tag (flytande) |
| (fila manglar) | Brukar `latest` |

---

## Automatisk oppgradering med Renovate

[Renovate](https://docs.renovatebot.com/) kan opna ein PR automatisk kvar gong det kjem
ein ny release av `linkml-datamodellering-no`. Kopier malen til rota av ditt repo:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/scripts/renovate.json \
  -o renovate.json
```

Eller hent han saman med bootstrap:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/scripts/renovate.json \
  -o renovate.json
# (bootstrap.sh er allereie køyrt)
```

`renovate.json` ser etter endringar i `ap-no-version:` i `linkml-datamodellering.yaml`
og brukar GitHub Releases som kjelde:

```json
{
  "customManagers": [{
    "customType": "regex",
    "fileMatch": ["^linkml-datamodellering\\.yaml$"],
    "matchStrings": ["ap-no-version:\\s*(?<currentValue>\\S+)"],
    "depNameTemplate": "brreg/linkml-datamodellering-no",
    "datasourceTemplate": "github-releases"
  }]
}
```

!!! note "Har du allereie renovate.json?"
    Legg berre til `customManagers`- og `packageRules`-blokkane frå
    [`scripts/renovate.json`](https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/scripts/renovate.json)
    i din eksisterande konfig. Ikkje dupliser `extends`.

---

## Lokal utvikling

Container-imagene er offentleg tilgjengelege frå GHCR — ingen innlogging er nødvendig:

```bash
# Valider skjema lokalt
podman run --rm \
  -v "$(pwd):/work" -w /work \
  ghcr.io/brreg/linkml-local:latest \
  gen-linkml --validate src/linkml/mitt-domene/min-modell/min-modell-schema.yaml

# Generer JSON Schema
podman run --rm \
  -v "$(pwd):/work" -w /work \
  ghcr.io/brreg/linkml-local:latest \
  gen-json-schema src/linkml/mitt-domene/min-modell/min-modell-schema.yaml
```

Tilgjengelege image-taggar: `latest`, `v1.0.0`, `v1.1.0`, …
