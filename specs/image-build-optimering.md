# Optimering av image-bygging og -lasting i CI

## Situasjon

Fire images vert handterte i kvar workflow-køyring:

| Image | Kor | Flyt |
|-------|-----|------|
| `linkml-local` | generate.yml | bygg → gzip → upload → (×6) download → load |
| `python-pytest` | generate.yml | bygg → gzip → upload → (×6) download → load |
| `mcp-linkml-validator` | validate.yml | bygg → gzip → upload → (×6) download → load |
| `mkdocs-local` | generate/publish | bygg lokalt i publish-jobben |

Kvar generate-jobb lastar to images. Kvar validate-jobb lastar eitt. Det betyr 12 + 6 = 18 download+load-operasjonar per workflow-køyring.

Problemet er todelt:
- **Bygging** skjer ved kvar push, sjølv om Dockerfile og avhengigheiter ikkje har endra seg
- **Lasting** er treg fordi tarball må lastast ned frå GitHub artifact storage og dekomprimerest + lastast av Podman

---

## Tiltak 1 (tilrådd) — GitHub Container Registry (GHCR)

### Prinsipp

Publiser images til GHCR i staden for å sende dei som workflow-artefakter. Kvar jobb køyrer `podman pull` i staden for download+load. GitHub Actions-runnerar har høghastigheitstilgang til GHCR, og registeret bruker lag-caching automatisk — berre endra lag vert overførd.

### Tagging-strategi

```
ghcr.io/<org>/linkml-local:<sha>          ← deterministisk, aldri overskrive
ghcr.io/<org>/linkml-local:latest         ← peikar alltid til siste bygg på main
```

`<sha>` = `${{ github.sha }}` — sikrar at kvar workflow-køyring bruker nøyaktig rett image.

### Workflow-endring

**Før (i dag):**
```
bygg → podman save | gzip → upload-artifact (247 MB)
…
download-artifact (247 MB) → gunzip | podman load
```

**Etter:**
```
bygg → podman push ghcr.io/…/linkml-local:$SHA
…
podman pull ghcr.io/…/linkml-local:$SHA   ← berre endra lag
```

### Krav

- `packages: write`-permission i build-jobbane
- `packages: read`-permission (standardtilgang for GHCR på offentlege repo) i generate/validate-jobbane
- `podman login ghcr.io -u ${{ github.actor }} --password ${{ secrets.GITHUB_TOKEN }}` i kvart steg som pushar eller pullar

### Estimert effekt

- Eliminerer upload/download av 250–500 MB tar.gz per køyring
- Lag-caching gjer at pull av `linkml-local` (som berre legg til `rdflib` oppå upstream) er marginalt etter første køyring
- Reduserer load-time frå ~30s til ~5s per jobb

---

## Tiltak 2 (komplementært) — Build-cache basert på Dockerfile-hash

### Prinsipp

Bygg images berre når Dockerfile eller avhengigheitsfiler faktisk har endra seg. Bruk `actions/cache` med ein nøkkel basert på hash av relevante filer.

### Nøkkelstrategi

```yaml
key: linkml-local-${{ hashFiles('src/assets/containers/Dockerfile.linkml') }}
key: python-pytest-${{ hashFiles('src/assets/containers/Dockerfile.python', 'src/assets/containers/requirements-python-test.txt') }}
key: mcp-linkml-validator-${{ hashFiles('src/mcp-linkml-validator/Dockerfile', 'src/mcp-linkml-validator/requirements.txt') }}
```

### Workflow-mønster (saman med Tiltak 1)

```yaml
build-linkml:
  steps:
    - uses: actions/checkout@v4
    - name: Logg inn på GHCR
      run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin
    - name: Sjekk om image allereie finst
      id: check
      run: |
        podman pull ghcr.io/${{ github.repository_owner }}/linkml-local:${{ github.sha }} 2>/dev/null \
          && echo "exists=true" >> $GITHUB_OUTPUT \
          || echo "exists=false" >> $GITHUB_OUTPUT
    - name: Bygg og push image
      if: steps.check.outputs.exists == 'false'
      run: |
        make linkml-build-docker
        podman push localhost/linkml-local:latest \
          ghcr.io/${{ github.repository_owner }}/linkml-local:${{ github.sha }}
        podman push localhost/linkml-local:latest \
          ghcr.io/${{ github.repository_owner }}/linkml-local:latest
```

### Estimert effekt

- Bygging av `linkml-local` (tyngst, basert på upstream `linkml/linkml`) hoppar over i ~80 % av køyringar (berre endra ved ny upstream eller rdflib-versjon)
- Bygging av `python-pytest` hoppar over med mindre `requirements-python-test.txt` endrar seg
- Sparer 2–5 minutt per køyring der Dockerfiles ikkje har endra seg

---

## Tiltak 3 (rask gevinst) — zstd i staden for gzip

### Prinsipp

Viss ein ikkje vil bytte til GHCR no, er `zstd` 5–10× raskare enn `gzip` ved komprimering med liknande komprimeringsrate. Endrar berre to linjer per build-jobb og to linjer per load-action.

### Endring

```yaml
# Bygg-jobb (før):
run: podman save localhost/linkml-local:latest | gzip > linkml-local.tar.gz

# Bygg-jobb (etter):
run: podman save localhost/linkml-local:latest | zstd -T0 > linkml-local.tar.zst

# Load-action (før):
run: podman load < <(gunzip -c linkml-local.tar.gz)

# Load-action (etter):
run: podman load < <(zstd -d -c linkml-local.tar.zst)
```

`-T0` = bruk alle tilgjengelege CPU-kjerner for komprimering. `zstd` er installert på ubuntu-22.04 som standard.

### Estimert effekt

- Komprimering: 30–60 % raskare enn gzip
- Dekomprimering: 3–5× raskare enn gzip
- Liten effekt på total workflow-tid samanlikna med Tiltak 1, men trivielt å implementere

---

## Tilråding og rekkefølgje

| Prioritet | Tiltak | Innsats | Effekt |
|-----------|--------|---------|--------|
| 1 | Tiltak 3 — zstd | Svært lav (4 linjer) | Middels |
| 2 | Tiltak 1 — GHCR | Medium | Høg |
| 3 | Tiltak 2 — build-cache | Lav (etter Tiltak 1) | Høg |

Start med **Tiltak 3** (zstd) som ein umiddelbar gevinst utan arkitekturendringar. Implementer deretter **Tiltak 1** (GHCR) som hovudoptimering — dette gjer **Tiltak 2** (build-cache) trivielt å leggje til sidan GHCR-pull allereie er idempotent med SHA-tagging.
