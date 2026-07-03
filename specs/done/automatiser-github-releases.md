# Automatiser GitHub Releases etter release-PR merge

## Bakgrunn

Repoet brukar **release-please** for å opprette release-PR-ar automatisk når det kjem semantiske commits (feat, fix, BREAKING CHANGE) til `main`. Dette fungerer bra, men:

**Noverande flyt:**
1. Commit med `feat:` eller `fix:` → release-please opprettar/oppdaterer release-PR automatisk
2. Brukar mergar release-PR manuelt
3. **Brukar må opprette GitHub Releases manuelt** (via GitHub UI eller `gh release create`)

**Problem:**
Steg 3 er manuelt og tungvindt. Kvar modell som vert oppdatert krev at brukaren:
- Går til GitHub Releases-sida
- Lagar ein ny release for kvar modell
- Kopierer CHANGELOG-innhald frå release-PR
- Lastar opp artefaktar (JSON Schema, SHACL, OWL, osv.)

**Motivasjon:**
Automatiser oppretting av GitHub Releases slik at dei vert oppretta automatisk når release-PR vert merga.

## Foreslått løysing

**Endre `.github/workflows/release-please.yml` til å opprette GitHub Releases automatisk:**

1. **Fjern `skip-github-release: true`** (eller sett til `false`)
2. **Legg til artefakt-opplasting** til kvar release

**Alternativt:** Legg til ein **separat workflow** som triggar på merge av release-PR og opprettar releases.

### Alternativ A: Fjern skip-github-release (enklaste)

**Endring i `.github/workflows/release-please.yml`:**

**Før:**
```yaml
- uses: googleapis/release-please-action@v5
  with:
    config-file: release-please-config.json
    manifest-file: .release-please-manifest.json
    skip-github-release: true
```

**Etter:**
```yaml
- uses: googleapis/release-please-action@v5
  with:
    config-file: release-please-config.json
    manifest-file: .release-please-manifest.json
    skip-github-release: false  # eller fjern linja heilt (false er default)
```

**Resultat:**
- Når release-PR vert merga, opprettar release-please automatisk GitHub Releases for kvar pakke som hadde versjonsendringar
- Release-notes vert generert frå CHANGELOG
- Tags vert oppretta automatisk (t.d. `dcat-ap-no-v1.2.0`)

**Problem:**
- Artefaktar (JSON Schema, SHACL, OWL, osv.) vert **ikkje** lasta opp automatisk
- Må leggjast til manuelt eller via separat workflow

### Alternativ B: Separat workflow for release-artefaktar

Lag ein ny workflow `.github/workflows/upload-release-assets.yml` som triggar når ein release vert oppretta:

```yaml
name: Upload Release Assets

on:
  release:
    types: [published]

jobs:
  upload-assets:
    runs-on: ubuntu-22.04
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v7
        with:
          ref: ${{ github.event.release.tag_name }}
      
      - name: Hent pakke-info frå tag
        id: pkg
        run: |
          TAG="${{ github.event.release.tag_name }}"
          # Tag-format: <component>-v<version> (t.d. dcat-ap-no-v1.2.0)
          COMPONENT=$(echo "$TAG" | sed 's/-v[0-9].*//')
          VERSION=$(echo "$TAG" | sed 's/.*-v//')
          echo "component=$COMPONENT" >> $GITHUB_OUTPUT
          echo "version=$VERSION" >> $GITHUB_OUTPUT
      
      - name: Bygg artefaktar
        run: |
          # Finn schema-fil basert på component
          SCHEMA=$(find src/linkml -name "${{ steps.pkg.outputs.component }}-schema.yaml")
          make gen-jsonschema SCHEMA="$SCHEMA"
          make gen-shacl SCHEMA="$SCHEMA"
          make gen-owl SCHEMA="$SCHEMA"
          # osv.
      
      - name: Last opp artefaktar til release
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          DOMAIN=$(echo "${{ steps.pkg.outputs.component }}" | cut -d- -f1)
          MODEL="${{ steps.pkg.outputs.component }}"
          
          gh release upload "${{ github.event.release.tag_name }}" \
            "generated/$DOMAIN/$MODEL/$MODEL-schema.json" \
            "generated/$DOMAIN/$MODEL/$MODEL-shapes.ttl" \
            "generated/$DOMAIN/$MODEL/$MODEL-ontology.ttl" \
            # osv.
```

**Fordel:** Artefaktar vert genererte og lasta opp automatisk
**Ulempe:** Meir kompleks, krev bygging i CI

### Alternativ C: Hybrid (anbefalt)

**Steg 1:** Fjern `skip-github-release: true` for å få automatisk release-oppretting

**Steg 2:** Legg til artefakt-opplasting i release-please workflow **etter** release vert oppretta:

```yaml
- uses: googleapis/release-please-action@v5
  id: release-please
  with:
    config-file: release-please-config.json
    manifest-file: .release-please-manifest.json

- name: Last opp artefaktar til releases
  if: ${{ steps.release-please.outputs.releases_created == 'true' }}
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    # release-please.outputs.paths_released inneheld liste av pakkar
    for pkg_path in $(echo '${{ steps.release-please.outputs.paths_released }}' | jq -r '.[]'); do
      # Hent component-namn og tag frå outputs
      component=$(jq -r ".[\"$pkg_path\"].component" <<< '${{ steps.release-please.outputs.releases }}')
      tag=$(jq -r ".[\"$pkg_path\"].tag_name" <<< '${{ steps.release-please.outputs.releases }}')
      
      echo "Lastar opp artefaktar for $component (tag: $tag)"
      
      # Finn genererte artefaktar
      domain=$(echo "$pkg_path" | cut -d/ -f3)
      model=$(echo "$pkg_path" | cut -d/ -f4)
      
      # Last opp artefaktar
      gh release upload "$tag" \
        "generated/$domain/$model/$model-schema.json" \
        "generated/$domain/$model/$model-shapes.ttl" \
        "generated/$domain/$model/$model-ontology.ttl" \
        --clobber
    done
```

**Problem:** Artefaktar må vere genererte **før** release-please køyrer. Løysing:
1. Generer artefaktar i ein eigen workflow som køyrer før release-please
2. Eller: trigger artefakt-generering i release-please workflow før opplasting

## Kva slags artefaktar skal lastast opp?

For kvar modell som vert releaset:
- `<modell>-schema.json` (JSON Schema)
- `<modell>-shapes.ttl` (SHACL)
- `<modell>-ontology.ttl` (OWL)
- `<modell>-context.jsonld` (JSON-LD context)
- `<modell>-schema.yaml` (LinkML-skjema)
- `<modell>-erdiagram.md` (ER-diagram)
- `CHANGELOG.md` (frå release-PR)

**Valfritt:**
- `<modell>-model.py` (Python dataklassar)
- `<modell>.proto` (Protobuf)
- Dokumentasjon (docs-katalog som ZIP)

## Nødvendige permissions

GitHub Releases krev `contents: write` permission, som release-please allereie har.

## Steg

1. **Avklar kva løysing som skal brukast:**
   - Alternativ A: Berre auto-releases, ingen artefaktar
   - Alternativ B: Separat workflow for artefaktar
   - Alternativ C: Hybrid (auto-releases + artefakt-opplasting i same workflow)

2. **Oppdater `.github/workflows/release-please.yml`**
   - Fjern eller endre `skip-github-release: true`
   - Legg til artefakt-opplasting (dersom Alternativ C)

3. **Test med ein modell**
   - Lag ein feat-commit som endrar ein modell
   - Merge release-PR
   - Verifiser at GitHub Release vert oppretta automatisk
   - Verifiser at artefaktar vert lasta opp (dersom relevant)

4. **Oppdater CONTRIBUTING.md**
   - Fjern/oppdater seksjon om manuell release-oppretting
   - Dokumenter at releases no skjer automatisk

## Prioritert handlingsliste

- [ ] Avklar kva artefaktar som skal lastast opp til releases
- [ ] Vel løysingsalternativ (A, B, eller C)
- [ ] Oppdater `.github/workflows/release-please.yml`
  - [ ] Fjern `skip-github-release: true`
  - [ ] Legg til artefakt-opplasting (dersom Alternativ C)
- [ ] Test med ein modell
- [ ] Oppdater CONTRIBUTING.md

## Avhengigheiter

- `.github/workflows/release-please.yml`
- `release-please-config.json`
- `.release-please-manifest.json`
- `generated/<domain>/<modell>/` (artefaktar må vere genererte)

## Merknader

- **skip-github-release: true** vart sett fordi kommentaren i workflow sa "GITHUB_TOKEN manglar tilgang til å opprette releases via REST API"
  - Dette er **ikkje lenger sant** — `contents: write` permission er nok
  - `skip-github-release: true` kan trygt fjernast
- **Artefakt-generering:** Må skje **før** release vert oppretta
  - Kan bruke `generate.yml` workflow som allereie køyrer på push til main
  - Eller: generer artefaktar i release-please workflow før release-oppretting
- **Tag-format:** release-please brukar `<component>-v<version>` (t.d. `dcat-ap-no-v1.2.0`)
- **Multiple releases:** Dersom fleire modellar vert oppdatert i same PR, opprettar release-please **fleire releases** (éin per modell)

## Eksempel: output frå release-please

Når release-PR vert merga:

```json
{
  "releases_created": true,
  "paths_released": ["src/linkml/ap-no/dcat-ap-no", "src/linkml/samt/samt-bu"],
  "releases": {
    "src/linkml/ap-no/dcat-ap-no": {
      "tag_name": "dcat-ap-no-v1.2.0",
      "name": "dcat-ap-no v1.2.0",
      "body": "## [1.2.0](https://github.com/...) (2026-07-03)\n\n### Features\n\n* add new slot ..."
    },
    "src/linkml/samt/samt-bu": {
      "tag_name": "samt-bu-v1.1.0",
      "name": "samt-bu v1.1.0",
      "body": "..."
    }
  }
}
```

Desse kan brukast til å identifisere kva artefaktar som skal lastast opp.

## Testing

**Før testing:** Sjekk at `generate.yml` køyrer **før** release-please:

```yaml
# I release-please.yml, legg til:
needs: [generate]  # dersom generate.yml lagar ein jobb som heiter "generate"
```

**Alternativt:** Generer artefaktar direkte i release-please workflow:

```yaml
- name: Generer artefaktar
  if: ${{ steps.release-please.outputs.releases_created == 'true' }}
  run: |
    for pkg_path in $(echo '${{ steps.release-please.outputs.paths_released }}' | jq -r '.[]'); do
      schema=$(find "$pkg_path" -name "*-schema.yaml")
      make gen-jsonschema SCHEMA="$schema"
      make gen-shacl SCHEMA="$schema"
      make gen-owl SCHEMA="$schema"
    done
```

## Referansar

- [release-please documentation](https://github.com/googleapis/release-please)
- [GitHub Releases API](https://docs.github.com/en/rest/releases)
- [gh release upload](https://cli.github.com/manual/gh_release_upload)

## Utført

Implementert **Alternativ C (Hybrid)**: automatiske GitHub Releases + artefakt-opplasting.

**Endringar i `.github/workflows/release-please.yml`:**

1. **Fjerna `skip-github-release: true`**
   - GitHub Releases vert no oppretta automatisk når release-PR vert merga

2. **Lagt til artefakt-generering (steg 3)**
   - Checkout kode
   - Installer podman
   - Bygg nødvendige container-images (linkml, python, avrotize)
   - Generer artefaktar for kvar releaset pakke:
     - JSON Schema (`gen-jsonschema`)
     - SHACL (`gen-shacl`)
     - OWL (`gen-owl`)
     - JSON-LD context (`gen-jsonld`)
     - ER-diagram (`gen-erdiagram`)

3. **Lagt til artefakt-opplasting (steg 4)**
   - Iterer gjennom alle releases frå `steps.release-please.outputs.paths_released`
   - Hent tag-namn for kvar release
   - Last opp artefaktar til tilhøyrande GitHub Release:
     - `<modell>-schema.json`
     - `<modell>-shapes.ttl`
     - `<modell>-ontology.ttl`
     - `<modell>-context.jsonld`
     - `<modell>-erdiagram.md`
     - `<modell>-schema.yaml` (LinkML-kjelde)
   - `--clobber` overskriver eksisterande filer

4. **Oppdatert kommentar øvst i fila**
   - Fjerna "brukar må opprette GitHub Releases manuelt"
   - Dokumentert at releases vert oppretta automatisk med artefaktar

**Flyt etter endring:**

1. Developer pusher `feat:` eller `fix:` commit til main
2. release-please opprettar/oppdaterer release-PR
3. Brukar mergar release-PR
4. **Automatisk:**
   - GitHub Release vert oppretta (éin per modell)
   - Tag vert laga (`<modell>-v<version>`)
   - Release notes vert generert frå CHANGELOG
   - Artefaktar vert genererte og lasta opp til release

**Testing:**

For å teste dette treng me ein faktisk release-PR merge. Alternativ:
1. Lag ein `feat:` commit som endrar ein modell
2. Vent til release-please opprettar PR
3. Merge PR
4. Verifiser at GitHub Release vert oppretta med artefaktar

**Potensielle forbetringer:**

- Cache container-images for raskare bygging
- Parallellisere artefakt-generering for fleire modellar
- Legg til fleire artefaktar (Python model, Protobuf, osv.)
- Komprimer docs-katalog og last opp som ZIP

**Kjente avgrensingar:**

- Artefaktar vert genererte **etter** release-oppretting, ikkje før
- Dersom artefakt-generering feiler, vert release likevel oppretta (utan artefaktar)
- `--clobber` kan overskrive eksisterande artefaktar dersom release vert re-køyrt

**BREAKING CHANGE:** GitHub Releases vert no oppretta automatisk. Brukarar som forventar manuell kontroll over release-oppretting må vente med å merge release-PR til dei er klare.
