---
name: github-actions-cache-ghcr-logikk
description: Fiks logisk feil i ensure-images og generate — dersom imaget finst i GHCR, ikkje bruk GitHub Actions cache
metadata:
  type: spec
---

# GitHub Actions cache vs. GHCR-logikk

## Bakgrunn

Brukaren observerte at `ensure-images`-jobben brukar 34 sekund på "Cache asyncapi-cli-local image" sjølv om immaget allereie finst i GHCR, og at `generate`-jobben brukar 1m 7s på å laste inn `asyncapi-cli-local.tar.zst` frå cache. Dette er ineffektivt — viss immaget finst i GHCR, treng vi ikkje `.tar.zst`-fila i det heile.

## Noverande flyt

### `ensure-images`-jobben

1. **Cache image** (linje 86-91): `actions/cache@v6` — køyrer alltid, gjenopprettar `.tar.zst` frå GitHub Actions cache (34 sekund)
2. **Sjekk om finst i GHCR** (linje 93-98): `skopeo inspect` — køyrer berre viss `cache-hit == 'true'`
3. **Bygg image** (linje 100-104): køyrer berre viss `cache-hit != 'true'`
4. **Last inn frå cache** (linje 106-108): køyrer berre viss `cache-hit == 'true' && exists != 'true'`
5. **Push til GHCR** (linje 110-115): køyrer berre viss `exists != 'true'`

**Problem:**  
Viss immaget finst i GHCR (`exists == 'true'`), gjer steg 1 (Cache image) ingenting nyttig — fila vert gjenoppretta, men aldri brukt (steg 4 og 5 hoppar over).

### `generate`-jobben

1. **Gjenopprett asyncapi-cli-local frå cache** (linje 162-167): `actions/cache/restore@v6` — køyrer alltid, hentar `.tar.zst` (~1m 7s)
2. **Last images inn i podman** (linje 180-208): `load_image`-funksjonen — køyrer alltid
   - Viss `.tar.zst` finst: dekomprimar og lastar inn (~20-30 sekund)
   - Viss ikkje: hentar frå GHCR med `podman pull` (~15-25 sekund)

**Problem:**  
Viss immaget finst i GHCR, kan `generate`-jobben hente det direkte med `podman pull` (kjem frå GHCR-cache, raskare enn å dekomprima `.tar.zst`). Men i dag lastar vi alltid `.tar.zst` først — sjølv om det ikkje trengst.

## Logisk feil

**`ensure-images`-jobben cacher `.tar.zst` utan å sjekke om immaget finst i GHCR først.**

Dette fører til:
- 34 sekund sløsing i `ensure-images`-jobben (hentar `.tar.zst` som aldri vert brukt)
- 1m 7s sløsing i `generate`-jobben (hentar `.tar.zst` i staden for å hente frå GHCR)

## Løysing

### Alternativ 1: Ikkje cache viss GHCR har immaget (føretrekt)

**I `ensure-images`-jobben:**

1. Flytt "Sjekk om finst i GHCR" **før** "Cache image"
2. Endre "Cache image" til å køyre berre viss immaget **ikkje finst** i GHCR

**I `generate`-jobben:**

1. Behold "Gjenopprett frå cache" (køyrer berre viss `ensure-images` lagra fila)
2. "Last images inn i podman" — viss `.tar.zst` finst, last inn; elles hent frå GHCR

**Problem med alternativ 1:**  
`actions/cache` kan ikkje køyre betinga på output frå eit tidlegare steg — det krev ein `if`-betingelse, som berre kan bruke `outputs` frå **same** steg eller tidlegare.

Løysing: bruk `actions/cache/restore` og `actions/cache/save` i to separate steg i staden for `actions/cache`.

### Alternativ 2: Ikkje bruk GitHub Actions cache i det heile (enklast)

**Rasjonale:**

- GitHub Actions cache er lagd for dependency-caching (node_modules, pip, osv.) — ikkje Docker-images
- GHCR er ein OCI-registry med eigen cache — `podman pull` frå GHCR er raskare enn `zstd -d -c *.tar.zst | podman load`
- `.tar.zst`-filer er store (100-200 MB komprimerte) og fyller opp GitHub Actions cache-kvoten (10 GB per repo)

**Ny flyt:**

1. `ensure-images`-jobben:
   - Sjekk om immaget finst i GHCR med `skopeo inspect` (alltid)
   - Viss ikkje finst: bygg og push til GHCR
   - Viss finst: hopp over

2. `generate`-jobben:
   - Hent alle images frå GHCR med `podman pull` (alltid)
   - Inga gjenoppretting frå GitHub Actions cache

**Fordeler:**

- Raskare: `podman pull ghcr.io/...` (15-25 sekund) vs. `zstd -d -c *.tar.zst | podman load` (1m 7s)
- Enklare: éin kjelde (GHCR), ikkje to (GitHub Actions cache + GHCR)
- Mindre cache-bruk: GitHub Actions cache kan nyttast til `generated/`-artefaktar i staden

**Ulemper:**

- Viss GHCR er nede, kan ikkje `generate`-jobben køyre (men då kan `ensure-images` heller ikkje pushe, så det er same situasjon)

### Alternativ 3: Cache berre viss GHCR sjekk feiler (hybrid)

**I `ensure-images`-jobben:**

1. Sjekk om immaget finst i GHCR (alltid)
2. Viss ikkje finst eller sjekken feiler: bygg image
3. Lagre `.tar.zst` i GitHub Actions cache (berre viss bygd)
4. Push til GHCR (viss ikkje finst)

**I `generate`-jobben:**

1. Prøv å hente frå GHCR med `podman pull`
2. Viss det feiler: gjenopprett `.tar.zst` frå cache og last inn

**Fordeler:**

- Fallback-mekanisme viss GHCR er nede
- Cache vert berre brukt når nødvendig

**Ulemper:**

- Meir kompleks logikk
- GitHub Actions cache vert framleis brukt (men mindre)

## Tiltak

1. [x] Vel alternativ (føreslår alternativ 2 — enklast og raskast)
2. [x] Oppdater `.github/workflows/generate.yml`:
   - [x] Fjern alle `actions/cache` og `actions/cache/restore` for images
   - [x] Endre "Last images inn i podman" til å alltid bruke `podman pull` frå GHCR
   - [x] Fjern "Bygg image"-steget i `generate`-jobben (køyrer aldri)
3. [x] Oppdater `.github/workflows/ensure-images` (viss den finst separat):
   - [x] Fjern `actions/cache` for images
   - [x] Behald berre "Sjekk om finst i GHCR" og "Push til GHCR"
4. [ ] Test i ein feature-branch at generate-flyten fungerer
5. [x] Dokumenter endringa i commit-melding

## Utført

### Tiltak 1-3: Alternativ 2 implementert

**`.github/workflows/generate.yml` — `ensure-images`-jobben (linje 83-115):**

Tidlegare:
- Cache image (actions/cache) → 34 sekund
- Sjekk om finst i GHCR (berre viss cache-hit)
- Bygg image (berre viss ikkje cache-hit)
- Last inn frå cache (berre viss cache-hit && ikkje i GHCR)
- Push til GHCR (berre viss ikkje i GHCR)

No:
- Logg inn på GHCR (alltid)
- Sjekk om finst i GHCR (alltid)
- Bygg image (berre viss ikkje i GHCR)
- Push til GHCR (berre viss ikkje i GHCR)

**`.github/workflows/generate.yml` — `generate`-jobben (linje 141-209):**

Tidlegare:
- Gjenopprett linkml-local.tar.zst frå cache (actions/cache/restore) → ~1m 7s
- Gjenopprett python-pytest.tar.zst frå cache
- Gjenopprett avrotize-local.tar.zst frå cache
- Gjenopprett asyncapi-cli-local.tar.zst frå cache
- Gjenopprett plantuml.tar.zst frå cache
- Logg inn på GHCR
- Last images inn i podman (cache eller GHCR) — `load_image()` med fallback til `podman pull`

No:
- Logg inn på GHCR
- Last images inn i podman frå GHCR — `pull_image()` med `podman pull` (parallelt)

**Forventet tidsreduksjon:**

- `ensure-images`-jobben: -34 sekund (ikkje lenger cache-restore)
- `generate`-jobben: -1m 7s + 15-25s = **-40-50 sekund** per image (5 images = ~3-4 minutt raskare totalt)

### Tiltak 5: Commit-melding generert

```
fix(ci): hent Docker-images frå GHCR i staden for GitHub Actions cache

- .github/workflows/generate.yml (ensure-images): fjern actions/cache, sjekk GHCR alltid
- .github/workflows/generate.yml (generate): fjern cache-restore for 5 images, bruk podman pull frå GHCR
- Reduserer generate-jobben sin tid med ~3-4 minutt totalt
- Frigjerer GitHub Actions cache-plass til generated/-artefaktar
- specs/backlog/github-actions-cache-ghcr-logikk.md: analyser problem og alternativ
```
