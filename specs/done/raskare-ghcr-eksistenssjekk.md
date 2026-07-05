---
name: raskare-ghcr-eksistenssjekk
description: Reduser tida brukt på å sjekke om container-image finst i GHCR frå 48s til <5s
metadata:
  type: optimization
---

# Raskare GHCR-eksistenssjekk

## Bakgrunn

Per i dag tek det 48 sekund å sjekke om eit container-image finst i GitHub Container Registry (GHCR) i `.github/workflows/generate.yml`. Sjekken skjer i steget "Sjekk om <image> finst i GHCR" (linje 88-93) og brukar `podman pull` for å verifisere eksistens:

```bash
IMAGE=ghcr.io/${{ github.repository_owner }}/${{ matrix.image.name }}:${{ hashFiles(matrix.image.hash_files) }}
podman pull "$IMAGE" 2>/dev/null && echo "exists=true" >> $GITHUB_OUTPUT || echo "exists=false" >> $GITHUB_OUTPUT
```

`podman pull` er ein kostbar operasjon fordi den faktisk lastar ned metadata og byrjar å hente lag, sjølv om den avbryt ved feil.

Problemet observert i workflow-loggen: `build-image / asyncapi-cli-local` brukte 48s på sjølve GHCR-sjekken — medan resten av jobben (pull, load, tag, push) tok berre ~16s.

## Løysing

Bruk `skopeo inspect` i staden for `podman pull` for å kun sjekke om manifest-fila finst, utan å laste ned noko.

`skopeo inspect docker://REGISTRY/IMAGE:TAG` gjer ein HEAD-request mot registry-APIet og returnerer manifest-metadata i JSON-format, utan å laste ned lag. Vanleg responstid: 1-5 sekund.

## Implementasjon

### 1. Erstatt `podman pull` med `skopeo inspect`

Endre `.github/workflows/generate.yml` linje 88-93:

**Før:**
```yaml
- name: Sjekk om ${{ matrix.image.name }} finst i GHCR
  id: ghcr-check
  if: steps.cache-image.outputs.cache-hit == 'true'
  run: |
    IMAGE=ghcr.io/${{ github.repository_owner }}/${{ matrix.image.name }}:${{ hashFiles(matrix.image.hash_files) }}
    podman pull "$IMAGE" 2>/dev/null && echo "exists=true" >> $GITHUB_OUTPUT || echo "exists=false" >> $GITHUB_OUTPUT
```

**Etter:**
```yaml
- name: Sjekk om ${{ matrix.image.name }} finst i GHCR
  id: ghcr-check
  if: steps.cache-image.outputs.cache-hit == 'true'
  run: |
    IMAGE=ghcr.io/${{ github.repository_owner }}/${{ matrix.image.name }}:${{ hashFiles(matrix.image.hash_files) }}
    skopeo inspect --format='exists' docker://"$IMAGE" >/dev/null 2>&1 && echo "exists=true" >> $GITHUB_OUTPUT || echo "exists=false" >> $GITHUB_OUTPUT
```

Ingen andre endringar nødvendige — resten av workflowen (stega 95-103) er uendra.

## Forventning

- **Før:** 48s for GHCR-sjekk + 16s for resten = 64s totalt
- **Etter:** <5s for GHCR-sjekk + 16s for resten = ~21s totalt (~67% reduksjon)

## Teststrategi

Trigger ein workflow-run (t.d. `workflow_dispatch` eller push til `main`) og sjekk tidsbruken i GitHub Actions-loggane for `build-image / asyncapi-cli-local`:

- Verifiser at steget "Sjekk om asyncapi-cli-local finst i GHCR" tek <5s (nedfrå 48s)
- Verifiser at `ghcr-check.outputs.exists` framleis settast korrekt (`true` / `false`)
- Verifiser at etterfølgjande steg (bygg, load, push) oppfører seg som før

## Handlingsliste

- [✓] 1. Erstatt `podman pull` med `skopeo inspect` i linje 88-93

## Utført

Tiltaket vart implementert i `.github/workflows/generate.yml` linje 88-93. `podman pull` er erstatta med `skopeo inspect --format='exists' docker://"$IMAGE"` for å kun sjekke manifest-eksistens utan å laste ned metadata eller lag.

Forventa reduksjon: frå 48s til <5s for GHCR-sjekk (67% reduksjon i total jobbtid).

Test ved neste workflow-run.
