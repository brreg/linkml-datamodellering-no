# Parallelisering av generate.yml

## Mål

- Bygging av container-image skjer parallelt
- Generering av kvart domene skjer parallelt og er eit eige, namngitt steg
- `publish`-jobben startar så snart alle domenejobbar er ferdige

---

## Problem med dagens struktur

```
build-linkml → build-python → make domains   ← sekvensiell, éin stor svart boks
```

- Image-bygginga er sekvensiell (unødvendig)
- Alle domenar er bundla i eitt steg — ein feil i `ap-no` stoppar `fint`
- Ingen domenespesifikk logg i Actions-UI

---

## Forslag: tre-lags jobb-graf

```
build-linkml  ┐
              ├── parallelle build-jobbar på kvar sin runner
build-python  ┘

generate (matrix: ap-no, fair, fint, ngr, oreg, samt)
  needs: [build-linkml, build-python]   ← ventar på begge

publish ← needs: generate
```

### Kvifor separate build-jobbar?

Kvart domene køyrer på ein **ny, tom runner** — images er ikkje tilgjengelege mellom jobbar. Å byggje images på nytt per domene ville koste 6× byggetid. Løysinga er å:

1. Byggje kvart image i sin eigen parallell jobb (`build-linkml`, `build-python`)
2. Lagre som `.tar`-filer og laste opp som workflow-artefaktar
3. Laste ned og `podman load` i kvar domene-jobb

---

## Composite action for generate-jobbar

Same prinsipp som `validate-domain`-actionen. Gjentakne steg trekkast ut til:

```
.github/actions/generate-domain/action.yml
```

Kvar `generate-<domene>`-jobb blir:

```yaml
  generate-ap-no:
    needs: [build-linkml, build-python]
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: ./.github/actions/generate-domain
        with:
          domain: ap-no
```

### `.github/actions/generate-domain/action.yml`

```yaml
name: Generer domene
description: Last inn images og generer artefaktar for eit domene

inputs:
  domain:
    description: Domenenamn (ap-no, fair, fint, ngr, oreg, samt)
    required: true

runs:
  using: composite
  steps:
    - uses: actions/download-artifact@v4
      with:
        name: linkml-local-image

    - uses: actions/download-artifact@v4
      with:
        name: python-pytest-image

    - name: Last inn images
      shell: bash
      run: |
        podman load < <(gunzip -c linkml-local.tar.gz)
        podman load < <(gunzip -c python-pytest.tar.gz)

    - name: Generer ${{ inputs.domain }}
      shell: bash
      run: make ${{ inputs.domain }}

    - uses: actions/upload-artifact@v4
      with:
        name: generated-${{ inputs.domain }}
        path: generated/${{ inputs.domain }}/
        retention-days: 1
```

Ny domene krev å kopiere 8 linjer i `generate.yml` og byte domenenamnet.

---

## Tidlegare foreslått YAML

```yaml
name: Generate and publish

on:
  push:
    branches: [main]

jobs:

  # -----------------------------------------------------------------------
  # Jobb 1: Bygg begge images parallelt
  # -----------------------------------------------------------------------
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: Bygg container-images parallelt
        run: |
          make linkml-build-docker &
          make python-build-docker &
          wait

      - name: Lagre images som artefaktar
        run: |
          podman save localhost/linkml-local:latest  | gzip > linkml-local.tar.gz
          podman save localhost/python-pytest:latest | gzip > python-pytest.tar.gz

      - uses: actions/upload-artifact@v4
        with:
          name: container-images
          path: |
            linkml-local.tar.gz
            python-pytest.tar.gz
          retention-days: 1

  # -----------------------------------------------------------------------
  # Jobb 2-7: Generer kvart domene parallelt
  # -----------------------------------------------------------------------
  generate-ap-no:
    needs: build
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: container-images
      - name: Last inn images
        run: |
          podman load < <(gunzip -c linkml-local.tar.gz)
          podman load < <(gunzip -c python-pytest.tar.gz)
      - name: Generer ap-no
        run: make ap-no
      - uses: actions/upload-artifact@v4
        with:
          name: generated-ap-no
          path: generated/ap-no/
          retention-days: 1

  generate-fair:
    needs: build
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: container-images
      - name: Last inn images
        run: |
          podman load < <(gunzip -c linkml-local.tar.gz)
          podman load < <(gunzip -c python-pytest.tar.gz)
      - name: Generer fair
        run: make fair
      - uses: actions/upload-artifact@v4
        with:
          name: generated-fair
          path: generated/fair/
          retention-days: 1

  generate-fint:
    needs: build
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: container-images
      - name: Last inn images
        run: |
          podman load < <(gunzip -c linkml-local.tar.gz)
          podman load < <(gunzip -c python-pytest.tar.gz)
      - name: Generer fint
        run: make fint
      - uses: actions/upload-artifact@v4
        with:
          name: generated-fint
          path: generated/fint/
          retention-days: 1

  generate-ngr:
    needs: build
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: container-images
      - name: Last inn images
        run: |
          podman load < <(gunzip -c linkml-local.tar.gz)
          podman load < <(gunzip -c python-pytest.tar.gz)
      - name: Generer ngr
        run: make ngr
      - uses: actions/upload-artifact@v4
        with:
          name: generated-ngr
          path: generated/ngr/
          retention-days: 1

  generate-oreg:
    needs: build
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: container-images
      - name: Last inn images
        run: |
          podman load < <(gunzip -c linkml-local.tar.gz)
          podman load < <(gunzip -c python-pytest.tar.gz)
      - name: Generer oreg
        run: make oreg
      - uses: actions/upload-artifact@v4
        with:
          name: generated-oreg
          path: generated/oreg/
          retention-days: 1

  generate-samt:
    needs: build
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: container-images
      - name: Last inn images
        run: |
          podman load < <(gunzip -c linkml-local.tar.gz)
          podman load < <(gunzip -c python-pytest.tar.gz)
      - name: Generer samt
        run: make samt
      - uses: actions/upload-artifact@v4
        with:
          name: generated-samt
          path: generated/samt/
          retention-days: 1

  # -----------------------------------------------------------------------
  # Jobb 8: Publiser til GitHub Pages
  # -----------------------------------------------------------------------
  publish:
    needs: [generate-ap-no, generate-fair, generate-fint, generate-ngr, generate-oreg, generate-samt]
    runs-on: ubuntu-22.04
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deploy.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4

      - name: Last ned alle genererte artefaktar
        uses: actions/download-artifact@v4
        with:
          pattern: generated-*
          path: generated/
          merge-multiple: true   # flattar ut generated-ap-no/ → generated/ap-no/ osv.

      - name: Last inn mkdocs-image og container-images
        uses: actions/download-artifact@v4
        with:
          name: container-images

      - name: Bygg mkdocs-local image
        run: make docs-build-docker

      - name: Publiser og bygg dokumentasjonsportal
        run: |
          make publish
          make docs-build

      - name: Konfigurer GitHub Pages
        uses: actions/configure-pages@v5

      - name: Last opp Pages-artefakt
        uses: actions/upload-pages-artifact@v3
        with:
          path: mkdocs/site/

      - name: Deploy til GitHub Pages
        id: deploy
        uses: actions/deploy-pages@v4
```

---

## Merknadar

**`merge-multiple: true`** i `download-artifact` krev `actions/download-artifact@v4`.
Flattar `generated-ap-no/` → `generated/ap-no/` automatisk utan ekstra steg.

**`podman load < <(...)`** brukar process substitution (bash). GitHub Actions brukar bash som standard shell, så dette fungerer.

**Ny domene** krev berre å kopiere eit domene-jobb-blokk og leggje til i `needs`-lista til `publish`. Alternativt kan ein bruke matrix-strategi (sjå nedanfor).

---

## Alternativ: matrix-strategi (kortare YAML)

Dei seks `generate-*`-jobbane er identiske bortsett frå domenenamnet. Dei kan kollapserast til éin jobb med matrix:

```yaml
  generate:
    needs: build
    runs-on: ubuntu-22.04
    strategy:
      matrix:
        domain: [ap-no, fair, fint, ngr, oreg, samt]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: container-images
      - name: Last inn images
        run: |
          podman load < <(gunzip -c linkml-local.tar.gz)
          podman load < <(gunzip -c python-pytest.tar.gz)
      - name: Generer ${{ matrix.domain }}
        run: make ${{ matrix.domain }}
      - uses: actions/upload-artifact@v4
        with:
          name: generated-${{ matrix.domain }}
          path: generated/${{ matrix.domain }}/
          retention-days: 1

  publish:
    needs: generate
    ...
```

**Ulempe med matrix:** alle domenar deler same timeout og same `fail-fast`-innstilling. Viss `ap-no` feiler og `fail-fast: true` (default), vert `fint` kansellert sjølv om den ville ha lukkast. Set `fail-fast: false` for å la alle køyre til endes.

**Tilråding:** bruk matrix med `fail-fast: false` — kortare YAML, same parallelisme.
