# Flytt mkdocs-local til ensure-images-jobben

## Bakgrunn

`generate.yml` har to ulike mønster for image-handtering:

- **`ensure-images`-jobben** (linje 45-102) byggjer og pushar `linkml-local`, `python-pytest`, `avrotize-local`, `asyncapi-cli-local` og `plantuml` til GHCR med hash-basert tagging
- **`publish`-jobben** (linje 197-209) byggjer `mkdocs-local` lokalt og cachar den som tarball via GitHub Actions cache

Dette er inkonsekvent og gjev unødvendig kompleksitet i `publish`-jobben. Alle images bør handterast via same mekanisme — bygg i `ensure-images`, push til GHCR, pull i konsumerande jobbar.

## Mål

Flytte `mkdocs-local`-handteringa til `ensure-images`-jobben slik at den blir bygg og pusha til GHCR på same måten som dei andre images. `publish`-jobben skal då berre pulle imagen frå GHCR, ikkje byggje den.

**Avklaringar frå brukar:**
- Dockerfile-namnet skal vere `Dockerfile.mkdocs`
- Dockerfila skal flyttast frå `mkdocs/Dockerfile.mkdocs` til `src/assets/containers/Dockerfile.mkdocs` for konsistens med dei andre container-filene

## Steg

0. **Flytt Dockerfile til src/assets/containers/**:
   - Flytt `mkdocs/Dockerfile.mkdocs` til `src/assets/containers/Dockerfile.mkdocs`
   - Oppdater `DOCS_DOCKERFILE`-variabelen i `Makefile` til å peike på `src/assets/containers/Dockerfile.mkdocs`

1. **Legg til `mkdocs-local` i `ensure-images`-matrisen** (`.github/workflows/generate.yml` linje 54-76):
   ```yaml
   - name: mkdocs-local
     dockerfile: src/assets/containers/Dockerfile.mkdocs
     make_target: build-docker-mkdocs
     hash_files: src/assets/containers/Dockerfile.mkdocs
   ```

2. **Fjern mkdocs-cache-stega frå `publish`-jobben** (`.github/workflows/generate.yml` linje 197-209):
   - Slett linje 197-202 (Cache mkdocs-local image)
   - Slett linje 203-207 (Bygg mkdocs-local image)
   - Slett linje 208-209 (Last inn mkdocs-local image)

3. **Legg til mkdocs-local i image-pulling i `publish`-jobben** (`.github/workflows/generate.yml` linje 218 — etter `docs-publish`-steget):
   Legg til ein ny steg-blokk før "Konfigurer GitHub Pages":
   ```yaml
   - name: Logg inn på GHCR
     run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin

   - name: Last mkdocs-local image frå GHCR
     run: |
       GHCR_TAG="ghcr.io/${{ github.repository_owner }}/mkdocs-local:${{ hashFiles('mkdocs/Dockerfile.mkdocs') }}"
       podman pull "$GHCR_TAG"
       podman tag "$GHCR_TAG" localhost/mkdocs-local:latest
   ```

4. **Verifiser at `publish`-jobben har `needs: [generate]`** — den må vente på `generate`, som i sin tur venter på `ensure-images`, slik at `mkdocs-local` er tilgjengeleg i GHCR før `publish` køyrer.

5. **Oppdater `on.push.paths`** i `generate.yml` til å inkludere `Dockerfile.mkdocs` og `Dockerfile.plantuml` slik at workflow triggast når desse endrar seg.

6. **Oppdater mkdocs-build-cache sin hash_files** til å inkludere `Dockerfile.mkdocs` i staden for `Dockerfile.linkml`.

7. **Test i CI** — push til ein test-branch og sjekk at:
   - `ensure-images` byggjer og pushar `mkdocs-local` til GHCR
   - `publish` pullar `mkdocs-local` frå GHCR og byggjer dokumentasjonsportalen

## Handlingsliste

- [x] Flytt `mkdocs/Dockerfile.mkdocs` til `src/assets/containers/Dockerfile.mkdocs`
- [x] Oppdater `DOCS_DOCKERFILE` i `Makefile`
- [x] Legg til `mkdocs-local` i `ensure-images`-matrisen
- [x] Fjern mkdocs-cache-stega frå `publish`-jobben
- [x] Legg til image-pulling for `mkdocs-local` i `publish`-jobben
- [x] Verifiser `needs`-avhengighet i `publish`-jobben (allereie riktig)
- [x] Oppdater `on.push.paths` til å inkludere `Dockerfile.mkdocs` og `Dockerfile.plantuml`
- [x] Oppdater mkdocs-build-cache sin hash_files til å bruke `Dockerfile.mkdocs`
- [ ] Test i CI (må ventast på brukar-push)
