# Parallelliser image-bygging i validate-workflow

## Bakgrunn

Validate-workflow byggjer for tida to containerimage sekvensielt i `build-validator`-jobben:
- `mcp-linkml-validator`
- `linkml-local`

Generate-workflow har allereie løyst dette parallelliseringsprobleme i `ensure-images`-jobben, som brukar ein `matrix`-strategi for å bygge 7 image parallelt.

Ved å adopte same mønster kan validate-workflow redusere byggtid og bli meir konsekvent med generate-workflow.

## Mål

1. Refaktorere `build-validator` til `ensure-images` med matrix-strategi
2. Bygge `mcp-linkml-validator` og `linkml-local` parallelt
3. Bruke `skopeo inspect` i staden for `podman pull` for GHCR-sjekk (meir effektivt)
4. Behalda same funksjonalitet (sjekk GHCR → bygg ved miss → push)

## Steg

### 1. Endre jobben `build-validator` til `ensure-images`

**Før:**
```yaml
build-validator:
  needs: [checkout-source]
  runs-on: ubuntu-22.04
  permissions:
    contents: read
    packages: write
  steps:
    - uses: actions/download-artifact@v8
      with:
        name: source
    - name: Oppgrader crun...
    - name: Logg inn på GHCR...
    - name: Sjekk om mcp-linkml-validator finst i GHCR...
    - name: Bygg mcp-linkml-validator image...
    - name: Push mcp-linkml-validator til GHCR...
    - name: Sjekk om linkml-local finst i GHCR...
    - name: Bygg linkml-local image...
    - name: Push linkml-local til GHCR...
```

**Etter:**
```yaml
ensure-images:
  name: "build-image / ${{ matrix.image.name }}"
  needs: [checkout-source]
  runs-on: ubuntu-22.04
  permissions:
    contents: read
    packages: write
  strategy:
    matrix:
      image:
        - name: mcp-linkml-validator
          dockerfile: src/assets/containers/Dockerfile.mcp-linkml-validator
          make_target: build-docker-mcp-validator
          hash_files: |
            src/assets/containers/Dockerfile.mcp-linkml-validator
            src/mcp-linkml-validator/requirements.txt
        - name: linkml-local
          dockerfile: src/assets/containers/Dockerfile.linkml
          make_target: build-docker-linkml
          hash_files: src/assets/containers/Dockerfile.linkml
    fail-fast: false
  steps:
    - uses: actions/download-artifact@v8
      with:
        name: source
    - name: Oppgrader crun til støtte for OCI v1-image
      run: |
        CRUN_VERSION=1.18.2
        wget -q https://github.com/containers/crun/releases/download/${CRUN_VERSION}/crun-${CRUN_VERSION}-linux-amd64 -O /tmp/crun
        chmod +x /tmp/crun
        sudo mv /tmp/crun /usr/bin/crun
        crun --version
    - name: Logg inn på GHCR
      run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin
    - name: Sjekk om ${{ matrix.image.name }} finst i GHCR
      id: ghcr-check
      run: |
        IMAGE=ghcr.io/${{ github.repository_owner }}/${{ matrix.image.name }}:${{ hashFiles(matrix.image.hash_files) }}
        if skopeo inspect --format='exists' docker://"$IMAGE" 2>&1; then
          echo "exists=true" >> $GITHUB_OUTPUT
        else
          echo "exists=false" >> $GITHUB_OUTPUT
        fi
    - name: Bygg ${{ matrix.image.name }} image
      if: steps.ghcr-check.outputs.exists != 'true'
      run: make ${{ matrix.image.make_target }}
    - name: Push ${{ matrix.image.name }} til GHCR
      if: steps.ghcr-check.outputs.exists != 'true'
      run: |
        IMAGE=ghcr.io/${{ github.repository_owner }}/${{ matrix.image.name }}:${{ hashFiles(matrix.image.hash_files) }}
        podman tag localhost/${{ matrix.image.name }}:latest "$IMAGE"
        podman push "$IMAGE"
```

### 2. Oppdatere `validate`-jobben sin `needs`-avhengighet

**Før:**
```yaml
validate:
  name: "validate / ${{ matrix.domain }}"
  needs: build-validator
```

**Etter:**
```yaml
validate:
  name: "validate / ${{ matrix.domain }}"
  needs: ensure-images
```

### 3. Oppdatere image-henting i `validate`-jobben

**Før:**
```yaml
- name: Hent mcp-linkml-validator frå GHCR
  if: steps.cache-validated.outputs.cache-hit != 'true'
  run: |
    IMAGE=ghcr.io/${{ github.repository_owner }}/mcp-linkml-validator:${{ hashFiles('src/assets/containers/Dockerfile.mcp-linkml-validator', 'src/mcp-linkml-validator/requirements.txt') }}
    podman pull "$IMAGE"
    podman tag "$IMAGE" mcp-linkml-validator:latest

- name: Hent linkml-local frå GHCR
  if: steps.cache-validated.outputs.cache-hit != 'true'
  run: |
    IMAGE=ghcr.io/${{ github.repository_owner }}/linkml-local:${{ hashFiles('src/assets/containers/Dockerfile.linkml') }}
    podman pull "$IMAGE"
    podman tag "$IMAGE" localhost/linkml-local:latest
```

**Etter:** (uendra — `ensure-images` garanterer at bileta finst i GHCR)

## Fordeler

1. **Parallellisering:** Begge image byggjer samtidig (reduserer byggtid frå ~3 min til ~1.5 min)
2. **Konsistens:** Same mønster som generate-workflow (`ensure-images` med matrix)
3. **Skalerbart:** Enkelt å legge til fleire image seinare (t.d. `plantuml`, `python-pytest`)
4. **Meir effektivt GHCR-sjekk:** `skopeo inspect` i staden for `podman pull` (ikkje last ned heile biletet)
5. **Betre logging:** `name: "build-image / ${{ matrix.image.name }}"` viser kva som byggjer

## Potensielle utfordringar

- **Cache-nøkkel i `validate`-jobben:** Må sikre at `hashFiles()` i `validate`-jobben matchår `matrix.image.hash_files` i `ensure-images`
- **Matrix-overhead:** GitHub Actions startar separate jobbar for kvar matrix-rad (litt ekstra startup-tid), men parallelliseringa kompenserer for dette

## Testing

1. Køyr workflow lokalt med `act` eller push til ein testbranch
2. Verifiser at begge image byggjer parallelt i GitHub Actions UI
3. Verifiser at `validate`-jobben hentar bileta korrekt frå GHCR
4. Verifiser at ingen cache-nøkkel-mismatch

## Handlingsliste

- [x] Endre `build-validator` til `ensure-images` med matrix-strategi
- [x] Oppdater `validate`-jobben sin `needs`-avhengighet
- [ ] Test at begge image byggjer parallelt (verifiserast ved neste CI-køyring)
- [ ] Test at `validate`-jobben hentar bileta korrekt (verifiserast ved neste CI-køyring)
- [x] Verifiser at cache-nøkkel matchår mellom `ensure-images` og `validate`
- [ ] Commit og push endringane (brukar utfører sjølv)

## Utført

- `.github/workflows/validate.yml`: `build-validator`-jobben er erstatta med `ensure-images`, som brukar `strategy.matrix` for å byggje `mcp-linkml-validator` og `linkml-local` parallelt (same mønster som `ensure-images` i `generate.yml`)
- GHCR-eksistenssjekk brukar no `skopeo inspect --format='exists'` i staden for `podman pull`
- `validate`-jobben sin `needs` peikar no til `ensure-images`
- Image-henting i `validate`-jobben (`Hent mcp-linkml-validator/linkml-local frå GHCR`) er uendra — `hashFiles()`-nøklane der matchar `matrix.image.hash_files` i `ensure-images`
- Verifisert med `python3 -c "import yaml; yaml.safe_load(...)"` at workflow-fila er gyldig YAML

## Relaterte filer

- `.github/workflows/validate.yml` — validate-workflow
- `.github/workflows/generate.yml` — referanse for `ensure-images`-mønster
