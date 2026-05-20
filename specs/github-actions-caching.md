# GitHub Actions dependency caching

## Situasjon

Tre build-jobbar køyrer ved kvar push og PR — uansett om Dockerfile eller avhengigheiter har endra seg:

| Jobb | Image | Typisk byggtid | Endrar seg når |
|------|-------|---------------|----------------|
| `build-linkml` | `linkml-local` | ~4–5 min | `Dockerfile.linkml` endrar seg |
| `build-python` | `python-pytest` | ~1–2 min | `Dockerfile.python` eller `requirements-python-test.txt` endrar seg |
| `build-validator` | `mcp-linkml-validator` | ~2–3 min | `Dockerfile` eller `requirements.txt` endrar seg |
| `docs-build-docker` (i publish) | `mkdocs-local` | ~1 min | `Dockerfile.mkdocs` endrar seg |

Desse Dockerfilane er svært stabile — dei fleste pushar rører ikkje avhengigheitene. Likevel byggast alle images på nytt kvar gong.

Kvar image brukast av **6 nedstrøms-jobbar** (generate-* og validate-*), og vert allereie overført via `zstd`-komprimerte workflow-artefaktar. Caching påverkar berre **build-steget** — ikkje korleis images vert overført til nedstrøms-jobbar.

---

## Tilrådd løysing — `actions/cache` på zstd-tarballs

### Prinsipp

Cache den komprimerte image-tarballen mellom køyringar med ein nøkkel basert på hashen av Dockerfile og eventuelle `COPY`'d filer. Ved cache-treff hoppar build-steget over; tarballen vert direkte lasta opp som workflow-artefakt for nedstrøms-jobbar.

```
Cache-treff:  restore tarball → upload-artifact  (~15 sek)
Cache-miss:   build → compress → upload-artifact + save cache  (same as today)
```

Nedstrøms-jobbar (generate-*, validate-*) er **uendra** — dei lastar framleis ned via `download-artifact`.

### Nøkkelstrategi

```yaml
# build-linkml
key: linkml-local-${{ hashFiles('src/assets/containers/Dockerfile.linkml') }}

# build-python
key: python-pytest-${{ hashFiles('src/assets/containers/Dockerfile.python', 'src/assets/containers/requirements-python-test.txt') }}

# build-validator
key: mcp-linkml-validator-${{ hashFiles('src/mcp-linkml-validator/Dockerfile', 'src/mcp-linkml-validator/requirements.txt') }}

# docs-build-docker (i publish-jobb)
key: mkdocs-local-${{ hashFiles('mkdocs/Dockerfile.mkdocs') }}
```

Nøkkelen endrar seg automatisk ved Dockerfile-endringar. Ingen manuell invalidering nødvendig.

### Mønster per build-jobb

```yaml
build-linkml:
  runs-on: ubuntu-22.04
  permissions:
    contents: read
  steps:
    - uses: actions/checkout@v4

    - name: Cache linkml-local image
      id: cache
      uses: actions/cache@v4
      with:
        path: linkml-local.tar.zst
        key: linkml-local-${{ hashFiles('src/assets/containers/Dockerfile.linkml') }}

    - name: Bygg linkml-local image
      if: steps.cache.outputs.cache-hit != 'true'
      run: |
        make linkml-build-docker
        podman save localhost/linkml-local:latest | zstd -T0 > linkml-local.tar.zst

    - name: Last opp image-artefakt
      uses: actions/upload-artifact@v4
      with:
        name: linkml-local-image
        path: linkml-local.tar.zst
        retention-days: 1
```

`build-python` og `build-validator` følgjer same mønster med respektive nøklar.

### Publish-jobben (mkdocs-local)

```yaml
    - name: Cache mkdocs-local image
      id: cache-mkdocs
      uses: actions/cache@v4
      with:
        path: mkdocs-local.tar.zst
        key: mkdocs-local-${{ hashFiles('mkdocs/Dockerfile.mkdocs') }}

    - name: Bygg mkdocs-local image
      if: steps.cache-mkdocs.outputs.cache-hit != 'true'
      run: |
        make docs-build-docker
        podman save localhost/mkdocs-local:latest | zstd -T0 > mkdocs-local.tar.zst

    - name: Last inn mkdocs-local image
      run: podman load < <(zstd -d -c mkdocs-local.tar.zst)
```

---

## Praktiske detaljar

### Cachestorleik og grenser

GitHub Actions-cache er avgrensa til **10 GB per repository**. Estimerte komprimerte storleikar:

| Image | Estimert storleik (zstd) |
|-------|--------------------------|
| `linkml-local` | ~250–350 MB |
| `python-pytest` | ~40–60 MB |
| `mcp-linkml-validator` | ~150–250 MB |
| `mkdocs-local` | ~80–120 MB |
| **Totalt** | **~520–780 MB** |

Godt innanfor 10 GB-grensa, sjølv med fleire nøklar frå ulike branches.

### Cache-levetid og eviction

- Cacher som ikkje er brukt på **7 dagar** vert automatisk sletta av GitHub
- Ved neste køyring etter eviction vert images rebuild og cache fylt på nytt
- Cache er tilgjengeleg på tvers av branches — PR-jobbar kan bruke cache frå `main`

### Cache-treffrate (estimat)

Basert på stabile Dockerfiles og krav som sjeldan endrar seg:

| Image | Forventa treffrate |
|-------|-------------------|
| `linkml-local` | ~90 % (endrar seg berre ved ny linkml-versjon) |
| `python-pytest` | ~90 % (endrar seg berre ved ny pytest/pyyaml) |
| `mcp-linkml-validator` | ~85 % (endrar seg ved linkml-versjonsbump) |
| `mkdocs-local` | ~95 % (svært stabil) |

### Estimert tidsgevinst per køyring med cache-treff

| Jobb | Innspart |
|------|---------|
| `build-linkml` | ~4 min |
| `build-python` | ~1 min |
| `build-validator` | ~2 min |
| `docs-build-docker` | ~1 min |
| **Totalt** | **~8 min per køyring** |

Gevinsten er størst for `validate.yml` som køyrer på kvar PR — der er build-validator typisk cache-treff.

---

## Kva som ikkje bør cachast

| Kandidat | Årsak til å ikkje cache |
|---------|------------------------|
| Genererte artefaktar (`generated-*`) | Skal alltid regenererast frå kjeldekode |
| `mkdocs/.cache` (MkDocs build-cache) | Innhaldet er generert dynamisk, nøkkel vanskeleg å definere |
| Podman layer-cache (`~/.local/share/containers`) | For stor og ustabil for `actions/cache` |

---

## Samandrag

| Aspekt | Vurdering |
|--------|-----------|
| Innsats | Lav — 4 ekstra `actions/cache`-steg |
| Effekt | Høg — ~8 min spart per køyring ved cache-treff |
| Risiko | Svært lav — cache-miss fallback til ordinær bygging |
| Nedstrøms-påverknad | Ingen — generate-* og validate-* jobbar er uendra |
| Storleik | ~750 MB total, godt under 10 GB-grensa |
