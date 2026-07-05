---
name: parallelliser-image-load
description: Reduser tidsbruk på image-innlasting i generate-jobbane frå ~100s til ~25s ved parallellisering
metadata:
  type: optimization
---

# Parallelliser image-innlasting i generate-jobbar

## Bakgrunn

Kvar `generate / <domain>`-jobb i `.github/workflows/generate.yml` lastar inn fire container-imager sekvensielt (linje 168-188):

1. `linkml-local.tar.zst` → `podman load` (~25s)
2. `python-pytest.tar.zst` → `podman load` (~25s)
3. `avrotize-local.tar.zst` → `podman load` (~25s)
4. `asyncapi-cli-local.tar.zst` → `podman load` (~25s)

**Totalt: ~100 sekund** (observert: 1m 41s i `generate / ap-no`-loggen)

Desse fire `load_image()`-kallane er **uavhengige av kvarandre** og kan køyre parallelt.

## Løysing

Endre `load_image()`-kallane (linje 181-188) til å køyre i bakgrunnen med `&` og vente på alle med `wait` etterpå.

## Implementasjon

### 1. Parallelliser `load_image()`-kallane

Endre `.github/workflows/generate.yml` linje 168-188:

**Før:**
```yaml
- name: Last images inn i podman (cache eller GHCR)
  if: steps.cache-generated.outputs.cache-hit != 'true'
  run: |
    load_image() {
      local tar="$1" local_tag="$2" ghcr_tag="$3"
      if [ -f "$tar" ]; then
        podman load < <(zstd -d -c "$tar")
      else
        echo "Cache miss for $tar — hentar frå GHCR: $ghcr_tag"
        podman pull "$ghcr_tag"
        podman tag "$ghcr_tag" "$local_tag"
      fi
    }
    load_image linkml-local.tar.zst localhost/linkml-local:latest \
      "ghcr.io/${{ github.repository_owner }}/linkml-local:${{ hashFiles('src/assets/containers/Dockerfile.linkml') }}"
    load_image python-pytest.tar.zst localhost/python-pytest:latest \
      "ghcr.io/${{ github.repository_owner }}/python-pytest:${{ hashFiles('src/assets/containers/Dockerfile.python', 'src/assets/containers/requirements-python-test.txt') }}"
    load_image avrotize-local.tar.zst localhost/avrotize-local:latest \
      "ghcr.io/${{ github.repository_owner }}/avrotize-local:${{ hashFiles('src/assets/containers/Dockerfile.avrotize') }}"
    load_image asyncapi-cli-local.tar.zst localhost/asyncapi-cli-local:latest \
      "ghcr.io/${{ github.repository_owner }}/asyncapi-cli-local:${{ hashFiles('src/assets/containers/Dockerfile.asyncapi-cli') }}"
```

**Etter:**
```yaml
- name: Last images inn i podman (cache eller GHCR)
  if: steps.cache-generated.outputs.cache-hit != 'true'
  run: |
    load_image() {
      local tar="$1" local_tag="$2" ghcr_tag="$3"
      if [ -f "$tar" ]; then
        podman load < <(zstd -d -c "$tar")
      else
        echo "Cache miss for $tar — hentar frå GHCR: $ghcr_tag"
        podman pull "$ghcr_tag"
        podman tag "$ghcr_tag" "$local_tag"
      fi
    }
    load_image linkml-local.tar.zst localhost/linkml-local:latest \
      "ghcr.io/${{ github.repository_owner }}/linkml-local:${{ hashFiles('src/assets/containers/Dockerfile.linkml') }}" &
    load_image python-pytest.tar.zst localhost/python-pytest:latest \
      "ghcr.io/${{ github.repository_owner }}/python-pytest:${{ hashFiles('src/assets/containers/Dockerfile.python', 'src/assets/containers/requirements-python-test.txt') }}" &
    load_image avrotize-local.tar.zst localhost/avrotize-local:latest \
      "ghcr.io/${{ github.repository_owner }}/avrotize-local:${{ hashFiles('src/assets/containers/Dockerfile.avrotize') }}" &
    load_image asyncapi-cli-local.tar.zst localhost/asyncapi-cli-local:latest \
      "ghcr.io/${{ github.repository_owner }}/asyncapi-cli-local:${{ hashFiles('src/assets/containers/Dockerfile.asyncapi-cli') }}" &
    wait
```

Einaste skilnad: legg til `&` på slutten av kvart `load_image`-kall og `wait` til slutt.

## Forventning

- **Før:** ~100s (sekvensielt: 4 × 25s)
- **Etter:** ~25s (parallelt: max(25s, 25s, 25s, 25s) = 25s)
- **Reduksjon:** 75% raskare

## Teststrategi

Trigger ein workflow-run og sjekk tidsbruken i GitHub Actions-loggane for `generate / ap-no`:

- Verifiser at steget "Last images inn i podman (cache eller GHCR)" tek ~25s (nedfrå ~100s)
- Verifiser at alle fire imager vert lasta inn korrekt (sjekk podman images-lista)
- Verifiser at etterfølgjande steg (`make domain-ap-no`) køyrer utan feil

## Handlingsliste

- [✓] 1. Legg til `&` på slutten av kvart `load_image`-kall (linje 181-188)
- [✓] 2. Legg til `wait` etter siste `load_image`-kall

## Utført

Alle fire `load_image()`-kallane køyrer no i bakgrunnen (`&`) og `wait` ventar på at alle er ferdige før neste steg startar.

Forventa reduksjon: frå ~100s til ~25s (75% raskare).

Test ved neste workflow-run.
