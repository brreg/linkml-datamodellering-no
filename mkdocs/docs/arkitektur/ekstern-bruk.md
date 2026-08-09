# Bruk frå eksternt repo

!!! note "Beskrivelse"

    Denne rettleiinga viser korleis eit eksternt repo kan bruke AP-NO-profilene og verktøya i dette repoet — utan å kopiere filer eller leve inni monorepoet.

Alt du treng er **to filer** og eit enkelt bootstrap-steg.

---

## Bootstrap (éin kommando)

I rota av ditt eige repo:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/bootstrap.sh | bash
```

For å feste til ein konkret versjon:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/bootstrap.sh \
  | AP_NO_VERSION=dcat-ap-no-v2.8.0 bash
```

Scriptet opprettar:

| Fil | Innhald |
|---|---|
| `linkml-datamodellering.yaml` | Pinnar AP-NO-versjonen for dette repoet |
| `.github/workflows/linkml.yml` | Minimalt GitHub Actions-oppsett for validering |

---

## Skjema-URL-ar og versjonering {: #versjonerte-artefakter }

Alle skjema i dette repoet er tilgjengelege via GitHub Raw med ein
versjon-tag eller `main`:

```
https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/{versjon}/{sti}
```

GitHub Pages-URL-ar (`https://brreg.github.io/linkml-datamodellering-no/...`)
peikar alltid til siste versjon på `main`. For ein **stabil, versjonert
adresse** til ein historisk versjon — t.d. for import frå eit eksternt
repo — bruk i staden:

- **[GitHub Releases](https://github.com/brreg/linkml-datamodellering-no/releases)** (anbefalt) — kanonisk adresse for eldre versjonar
- **`raw.githubusercontent.com`-URL med tag**, som over

!!! tip "Anbefaling"
    Bruk alltid ein **skjema-spesifikk versjon-tag** (t.d. `dcat-ap-no-v2.13.0`, `common-ap-no-v1.0.0`) i imports — aldri `main` eller `latest` — for å unngå overraskande endringer når dette repoet vert oppdatert.

!!! warning "Skjema-spesifikke taggar"
    Generelle release-taggar (`v1.0.0`, `v1.1.0`) peikar til ein spesifikk commit, men garanterer **ikkje** at alle skjemafiler finst i den commiten. Bruk **skjema-spesifikke taggar** (t.d. `dcat-ap-no-v2.13.0`, `common-ap-no-v1.0.0`) for stabile import-URL-ar.

### AP-NO-profilar

| Profil | Import-URL (`versjon`) | Brukstilfelle |
|---|---|---|
| `dcat-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.13.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema` | Datakatalogar og datasett |
| `skos-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/skos-ap-no-v2.16.0/src/linkml/ap-no/skos-ap-no/skos-ap-no-schema` | Omgrepsamlingar |
| `modelldcat-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/modelldcat-ap-no-v1.10.0/src/linkml/ap-no/modelldcat-ap-no/modelldcat-ap-no-schema` | Informasjonsmodellar |
| `dqv-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dqv-ap-no-v1.15.0/src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema` | Datakvalitet |
| `cpsv-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/cpsv-ap-no-v1.10.0/src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema` | Offentlege tenester og hendingar |
| `xkos-ap-no` | `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/xkos-ap-no-v1.0.0/src/linkml/ap-no/xkos-ap-no/xkos-ap-no-schema` | Utvida klassifikasjon |

!!! note "`.yaml`-ending er valfri"
    LinkML løyser importer utan filending — begge variantar fungerer:
    `...dcat-ap-no-schema` og `...dcat-ap-no-schema.yaml`

Døme på importdel i eit eksternt skjema:

```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/dcat-ap-no-v2.13.0/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema
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

Workflowen les `build.yaml` frå skjemakatalogen og køyrer dei generatorane som er aktiverte
(`jsonld_context`, `json_schema`, `python`, `shacl`, `owl`, `rdf`, `protobuf`, `example_rdf`).
Sjå [Generatorkonfigurasjon](../kom-i-gang/build-config.md) for detaljar.

---

## Versjonsfesta oppsett

`linkml-datamodellering.yaml` i rota av ditt repo pinnar versjonen:

```yaml
# linkml-datamodellering.yaml
ap-no-version: latest
```

Dei reusable workflowene les denne fila automatisk og nyttar rett versjon av
container-imagene og AP-NO-skjema. Du treng ikkje sende inn `version`-inputen eksplisitt.

| `ap-no-version` | Åtferd |
|---|---|
| `latest` | Brukar siste release-tag (flytande) — anbefalt |
| `dcat-ap-no-v2.8.0` | Brukar nøyaktig denne skjema-versjonen |
| (fila manglar) | Brukar `latest` |

---

## Automatisk oppgradering med Renovate

[Renovate](https://docs.renovatebot.com/) kan opna ein PR automatisk kvar gong det kjem
ein ny release av `linkml-datamodellering-no`. Kopier malen til rota av ditt repo:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/renovate.json \
  -o renovate.json
```

Eller hent han saman med bootstrap:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/renovate.json \
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
    [`renovate.json`](https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/renovate.json)
    i din eksisterande konfig. Ikkje dupliser `extends`.

---

## Lokal utvikling

### 0 — Sjekk føresetnader

Før du køyrer podman-eksempla under, sjekk at Podman (rootless), user
namespace-mapping og diskplass er korrekt konfigurert:

```bash
curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/assets/scripts/makefile/check-prereqs.bash | bash
```

Scriptet krev ingen tilgang til dette repoet sin Makefile eller
katalogstruktur — det sjekkar berre systemføresetnader (Git, Podman,
Podman rootless, `/etc/subuid`/`/etc/subgid`, diskplass) og fungerer difor
identisk i eit eksternt repo.

### 1 — Valider og generer artefakter

Container-imagene er offentleg tilgjengelege frå GHCR — ingen innlogging er nødvendig:

```bash
# Strukturvalidering (fail-fast, ingen fil skriven)
podman run --rm \
  -v "$(pwd):/work" -w /work \
  ghcr.io/brreg/linkml-local:latest \
  gen-linkml src/linkml/mitt-domene/min-modell/min-modell-schema.yaml

# Stilsjekk (namnekonvensjonar, URI-ar, obligatoriske felt)
podman run --rm \
  -v "$(pwd):/work" -w /work \
  ghcr.io/brreg/linkml-local:latest \
  linkml lint src/linkml/mitt-domene/min-modell/min-modell-schema.yaml

# Generer JSON Schema
podman run --rm \
  -v "$(pwd):/work" -w /work \
  ghcr.io/brreg/linkml-local:latest \
  gen-json-schema src/linkml/mitt-domene/min-modell/min-modell-schema.yaml
```

Tilgjengelege image-taggar: `latest`, `main`, skjema-spesifikke taggar (`dcat-ap-no-v2.8.0`, …)

!!! note "`linkml lint` utan `--config` bruker eit anna regelsett enn CI"
    Dette repoet sin eigen lint-config
    ([`.linkmllint.yaml`](https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/assets/containers/.linkmllint.yaml))
    slår av `standard_naming`-regelen (som elles forventar engelske
    namnekonvensjonar, i konflikt med norsk bokmål-namngjeving). Utan denne
    configen brukar `linkml lint` sitt eige standardregelsett. For
    identisk åtferd med CI, hent configen og legg til `--config
    .linkmllint.yaml` i kallet over.

!!! warning "Policy-validering (bronze/silver/gold) krev meir enn éin podman-kommando lokalt"
    `make mcp-linkml-valider-modell` (sjå [Rettleiing: ny domenemodell](../kom-i-gang/ny-domenemodell.md#3-valider-undervegs))
    brukar `ghcr.io/brreg/mcp-linkml-validator` — biletet **er** offentleg
    tilgjengeleg, men i motsetnad til `gen-linkml`/`linkml lint` over held
    det ikkje å montere skjemaet inn: sjølve valideringslogikken vert
    styrt av `flatten-and-validate.bash` og `policies/`-katalogen, som må
    hentast frå dette repoet og monterast inn saman med biletet (sjå
    `src/mcp-linkml-validator/flatten-and-validate.bash`). `gen-linkml`/
    `linkml lint` over dekkjer strukturvalidering og stilsjekk direkte;
    for full bronze/silver/gold-policy (`begrepsidentifikator`,
    `annotations.utgiver` osv.) er GitHub Actions-workflowen frå
    [Bootstrap](#bootstrap-ein-kommando) den enklaste vegen — han hentar
    desse støttefilene og køyrer full policy-validering automatisk via
    `reusable-validate.yml`.
