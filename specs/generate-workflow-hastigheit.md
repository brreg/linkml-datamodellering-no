# Reduksjon av generate-og-publish-workflow frå 4 til 1 minutt

## Situasjon og kritisk veg

Workflowen har tre sekvensielle fasar:

```
build-linkml ┐
             ├─→ generate-ap-no ┐
build-python ┘   generate-fair  │
                 generate-fint  ├─→ publish
                 generate-ngr   │
                 generate-oreg  │
                 generate-samt  ┘
```

### Tidskostnad per fase (estimat med cache-treff på image)

| Fase | Kva tek tid | Estimat |
|------|-------------|---------|
| `build-linkml` + `build-python` | Runner-start + checkout + GHCR-treff-sjekk | ~35 s |
| `generate-*` (kritisk veg: ap-no/fint, 6 skjema) | Runner-start (20s) + checkout (10s) + `podman pull` 2 images (40s) + generering (40s) + artifact upload (10s) | ~120 s |
| `publish` | Runner-start (20s) + checkout (10s) + mkdocs image-last (30s) + `make docs-build` (50s) + Pages-deploy (20s) | ~130 s |
| **Total kritisk veg** | build → tyngste generate → publish | **~285 s (≈ 4,75 min)** |

### Kvar er det faktisk rom for innsparing?

Nesten all tid går til faste overheadkostnadar per runner — **ikkje** til sjølve genereringa:

- 8 jobbar × ~20 s runner-start = 160 s
- 8 jobbar × ~10 s checkout = 80 s
- 6 generate-jobbar × ~40 s `podman pull` (2 images) = 240 s
- Sjølve `linkml`-genereringa for alle domener samla: ~80 s

For å koma ned til 1 minutt må me **eliminere flest moglege runner-starter og image-pull-ar**, ikkje optimere sjølve genereringa.

---

## Tiltak 1 (kritisk) — `paths`-filter på workflow-nivå

### Prinsipp

Dei aller fleste push-ar til `main` rører ikkje skjemafiler. Utan `paths`-filter startar workflowen unødvendig for commit-ar som berre endrar dokumentasjon, scripts, specs eller konfigurasjon.

```yaml
on:
  push:
    branches: [main]
    paths:
      - 'src/linkml/**'
      - 'src/assets/containers/Dockerfile.linkml'
      - 'mkdocs/**'
      - 'src/templates/**'
```

### Effekt

- Push som ikkje rører nokon av desse stiane: **0 s** (workflow køyrer aldri)
- Estimert del av push-ar som ikkje rører skjema: ~70 %

**Innsparing: 4 min → 0 s for ~70 % av køyringar.**

---

## Tiltak 2 (kritisk) — Per-domene cache av genererte artefaktar

### Prinsipp

Kvart generate-domene vert nøkla på hash av skjemafilene i det domenet + hash av `Dockerfile.linkml`. Viss nøkkelen treff, vert genereringa hoppa over og cacha output brukt direkte.

```yaml
- name: Cache genererte artefaktar
  id: cache-generated
  uses: actions/cache@v5
  with:
    path: generated/${{ inputs.domain }}/
    key: generated-${{ inputs.domain }}-${{ hashFiles(format('src/linkml/{0}/**', inputs.domain), 'src/assets/containers/Dockerfile.linkml') }}

- name: Generer (berre viss cache-miss)
  if: steps.cache-generated.outputs.cache-hit != 'true'
  run: # alle gen-* steg
```

### Effekt

Viss berre eitt domene er endra (typisk tilfelle): berre éin generate-jobb køyrer generering (~40 s), dei andre fem restorerar frå cache (~5 s kvar).

Ny kritisk veg for typisk enkelt-domene-endring:
- build: ~35 s (cache-treff)
- generate (1 domene): 20 + 10 + 40 + 40 + 10 = **~120 s**
- publish: **~130 s**
- **Total: ~285 s** — Liten endring i kritisk veg, fordi publish framleis dominerer.

For å faktisk nå 1 minutt trengst òg tiltak 3.

---

## Tiltak 3 (kritisk) — Slå saman `build-*` og `generate-*` til éin jobb per domene

### Prinsipp

`build-linkml` og `build-python` er eigne jobbar berre fordi dei lasta imagene som artifact tidlegare. No som imagene ligg i GHCR med stabile SHA-nøklar, kan generate-jobbane sjølv sjekke og hente images utan ein eigen build-jobb.

Dette eliminerer to runner-startar + to checkout-ar (totalt ~60 s) og mogleggjer at generate-jobbar startar **samstundes** i staden for å vente på build-barrier.

```yaml
generate-ap-no:
  runs-on: ubuntu-22.04
  steps:
    - uses: actions/checkout@v6
    - name: Logg inn på GHCR og hent images
      run: |
        echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin
        podman pull ghcr.io/.../linkml-local:${{ hashFiles(...) }}
        # osv.
    - name: Bygg image viss ikkje i GHCR (sjeldan)
      run: make linkml-build-docker && podman push ...
    # ... gen-steg
```

**Innsparing: ~60 s frå kritisk veg (eliminerer build-barrieren).**

---

## Tiltak 4 (kritisk) — Flytt mkdocs-image til GHCR og eliminer `make docs-build-docker` i publish

### Prinsipp

`publish`-jobben bruker ~30–60 s på å laste mkdocs-imaget frå ein lokal `.tar.zst` cache. Same mønster som for dei andre imagene: push til GHCR og pull i publish.

I tillegg: `make docs-build` (mkdocs Material med mange plugin-behandla filer) er truleg den tyngste enkeltoperasjonen i publish (~50 s). Dette kan ikkje eliminerast, men kan reduserast ved å:

1. Unngå å generere docs på nytt dersom ingen av `mkdocs/`, `src/templates/` eller genererte filer er endra (kombinert med tiltak 2)
2. Bruke `mkdocs-build-cache-plugin` som allereie er installert i imaget — denne pluginen cacher uendra sider mellom køyringar. Med `actions/cache` på `mkdocs/.cache/` kan dette gje 30–50 % raskare `docs-build` ved delvise endringar.

```yaml
- name: Cache mkdocs-build-cache
  uses: actions/cache@v5
  with:
    path: mkdocs/.cache/
    key: mkdocs-build-${{ hashFiles('generated/**', 'mkdocs/docs/**') }}
    restore-keys: mkdocs-build-
```

**Estimert innsparing i publish: ~30–40 s.**

---

## Samla effekt og realistisk kjøretid

### Typisk push (eitt domene endra, t.d. ein schema-fix i `samt`)

| Fase | I dag | Etter tiltak 1–4 |
|------|-------|-------------------|
| build-barrier | ~35 s | 0 s (eliminert) |
| generate (5 uendra domener) | ~120 s × 5 parallelt | ~5 s (cache restore) |
| generate (1 endra domene) | ~120 s | ~90 s |
| publish | ~130 s | ~80 s (mkdocs-cache) |
| **Total** | **~285 s** | **~170 s (≈ 2,8 min)** |

### Push som berre endrar docs/scripts (ingen skjema)

| I dag | Etter tiltak 1 |
|-------|----------------|
| ~285 s | **0 s** |

### Alle domener endra samstundes (sjeldan)

| I dag | Etter tiltak 1–4 |
|-------|------------------|
| ~285 s | ~200 s |

---

## Kvifor 1 minutt er vanskeleg

Kvar GitHub-hosted runner har uunngåeleg overhead:
- ~20 s oppstart
- ~10 s checkout

`publish` er sekvensielt etter alle generate-jobbar og inneheld obligatorisk `mkdocs`-bygg (~30–50 s) + Pages-deploy (~20 s). Utan å eliminere sjølve publish-trinnet er 60 s ikkje oppnåeleg med GitHub-hosted runnerar.

**Einaste realistiske veg til 1 minutt:** sjølv-hosta runner (oppstart < 1 s) kombinert med alle tiltak over. Med sjølv-hosta runner fell runner-start + checkout frå ~30 s til ~3 s per jobb.

---

## Tilråding og prioritet

| Prioritet | Tiltak | Innsats | Effekt |
|-----------|--------|---------|--------|
| 1 | `paths`-filter på workflow-nivå | Svært låg (5 linjer) | Eliminerer ~70 % av køyringar |
| 2 | Per-domene cache av genererte artefaktar | Medium | Typisk enkelt-domene-endring: frå 120 s → 5 s per uendra domene |
| 3 | Slå saman build + generate (fjern build-barrier) | Medium | ~60 s frå kritisk veg |
| 4 | mkdocs-build-cache i publish | Låg | ~30–40 s frå publish |
| 5 | Sjølv-hosta runner | Høg (infrastruktur) | -20 s per jobb (~120 s totalt) |

Implementer tiltak 1–4 for å nå **~80 s** for den typiske push-en som berre endrar `main`-filer utan skjemaendringar, og **~2,5–3 min** for ein full re-generering. Tiltak 5 (sjølv-hosta runner) er det einaste som kan ta full re-generering under 1 minutt.
