# Git-tag-validering for schema-versjonar

## Bakgrunn

Quickstart.sh genererer versjonerte GitHub raw-URL-ar basert på `schema.version` (t.d. `v1.0.0`), men det er inga garanti for at git-taggen faktisk eksisterer i GitHub.

**Problem:**
- common-ap-no har `version: "1.0.0"` i schema.yaml
- Quickstart genererer: `https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/src/linkml/ap-no/common-ap-no/common-ap-no-schema.yaml`
- Men taggen `common-ap-no-v1.0.0` eller `v1.0.0` finst ikkje i GitHub → 404

Dette gjer at dokumentasjonsportalen viser imports-eksempel med URL-ar som ikkje fungerer.

## Kontekst

- `mkdocs/lib/sections/quickstart.sh` genererer versjonerte import-URL-ar
- Repoet brukar `release-please` for versjonering (sjå `.github/workflows/release.yml`)
- Git-taggar vert oppretta automatisk av `release-please` ved merge av release-PR
- Tagformat: `<schema>-v<versjon>` (t.d. `common-ap-no-v1.0.0`)

## Forslag til løysing

### Alternativ A: CI-validering (anbefalt)

Legg til ein GitHub Actions-sjekk som validerer at alle skjema sin `version`-verdi har ein korresponderande git-tag.

**Pros:**
- Feil oppdagast tidleg (i PR-stage)
- Ingen runtime-overhead i `quickstart.sh`
- Tvingar korrekt versjonering-praksis
- Enkel å implementere
- Blokkerer merge dersom tags manglar

**Cons:**
- Krev eingangs-jobb for å opprette manglande tags for eksisterande skjema
- Kan vere falskt positivt i PR-ar som berre bumpar versjon (taggen vert ikkje oppretta før release-PR er merga)

### Alternativ B: Automatisk tagging ved versjonsbump

Legg til ein GitHub Actions workflow som automatisk opprettar git-tags når `version`-feltet i eit schema endrar seg.

**Implementasjon:**

To hovudtilnærmingar:

#### B.1: Post-merge automatisk tagging

Workflow som køyrer etter merge til `main`, detekterer endra schema-versjonar, og opprettar tilhøyrande git-tags.

```yaml
# .github/workflows/auto-tag-schemas.yml
name: Auto-tag schema versions

on:
  push:
    branches: [main]
    paths:
      - 'src/linkml/**/*-schema.yaml'

jobs:
  auto-tag:
    runs-on: ubuntu-latest
    permissions:
      contents: write  # Treng write-tilgang for å opprette tags
    
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Treng historikk for å samanlikne
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Configure git
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
      
      - name: Detect version changes and create tags
        run: |
          # Samanlikn med førre commit
          CHANGED_SCHEMAS=$(git diff --name-only HEAD~1 HEAD | grep "src/linkml/.*-schema.yaml" || true)
          
          if [ -z "$CHANGED_SCHEMAS" ]; then
            echo "Ingen schema-filer endra"
            exit 0
          fi
          
          for schema_file in $CHANGED_SCHEMAS; do
            if [ ! -f "$schema_file" ]; then
              echo "⚠️  $schema_file vart sletta, hoppar over"
              continue
            fi
            
            # Les noverande versjon
            version=$(grep "^version:" "$schema_file" | sed 's/version: *"\?\([^"]*\)"\?/\1/' | tr -d ' ')
            
            if [ -z "$version" ]; then
              echo "⚠️  $schema_file: mangler version-felt"
              continue
            fi
            
            # Ekstraher schema-namn
            schema=$(basename "$schema_file" .yaml | sed 's/-schema$//')
            domain=$(basename "$(dirname "$(dirname "$schema_file")")")
            tag_name="${schema}-v${version}"
            
            # Sjekk om tag allereie finst
            if git tag -l | grep -q "^${tag_name}$"; then
              echo "✅ Tag $tag_name finst allereie"
              continue
            fi
            
            # Les tidlegare versjon (frå førre commit)
            old_version=$(git show HEAD~1:"$schema_file" 2>/dev/null | grep "^version:" | sed 's/version: *"\?\([^"]*\)"\?/\1/' | tr -d ' ' || echo "")
            
            if [ "$version" != "$old_version" ]; then
              echo "🏷️  Opprettar tag $tag_name (tidlegare: $old_version)"
              git tag -a "$tag_name" -m "Release $schema version $version"
              git push origin "$tag_name"
            else
              echo "ℹ️  $schema: versjon uendra ($version)"
            fi
          done
```

#### B.2: Integrasjon med release-please

Utvid `.github/workflows/release.yml` til å opprette per-schema-tags i tillegg til hovud-release-taggen.

```yaml
# Legg til i .github/workflows/release.yml etter release-please-action
- name: Create per-schema tags
  if: steps.release.outputs.releases_created == 'true'
  run: |
    # Iterér over alle endra schema-filer i release-PR
    for schema_file in $(find src/linkml -name "*-schema.yaml" -type f); do
      version=$(grep "^version:" "$schema_file" | sed 's/version: *"\?\([^"]*\)"\?/\1/' | tr -d ' ')
      schema=$(basename "$schema_file" .yaml | sed 's/-schema$//')
      tag_name="${schema}-v${version}"
      
      # Opprett tag dersom den ikkje finst
      if ! git tag -l | grep -q "^${tag_name}$"; then
        git tag -a "$tag_name" -m "Release $schema version $version"
        git push origin "$tag_name"
      fi
    done
```

**Pros:**
- Fullstendig automatisert — ingen manuell intervensjon
- Garanterer at tags vert oppretta for alle publiserte versjonar
- Konsistent tag-namnegiving
- Integrerer naturleg med eksisterande release-workflow

**Cons:**
- Kompleksitet: Krev ekstra CI-logikk og permissions-konfigurasjon
- Timing: B.1 opprettar tags umiddelbart etter merge (før release-PR), B.2 berre for release-versjonar
- Feilhandtering: Dersom tagging feiler, må det vere retry-logikk eller manuell intervensjon
- Kan opprette tags for arbeid-i-progresjon dersom versjon vert bumpa utan release (B.1)
- Vanskelegare å teste lokalt (krev GitHub Actions-miljø)

**Variasjonar:**

- **B.1 (Post-merge)**: Best for rask prototyping, men kan gi "støy" med tags for upubliserte versjonar
- **B.2 (Release-integrert)**: Best for produksjon, men krev tettare integrasjon med `release-please`

**Anbefaling for B:**

Dersom Alternativ B vert valt, bruk **B.2 (release-integrert)** fordi:
- Tags vert berre oppretta for faktiske releases
- Tettare samanheng mellom versjonering og tagging
- Mindre støy i tag-lista

### Alternativ C: Fallback til `main` ved manglande tag

Endre `quickstart.sh` til å verifisere at taggen finst (via GitHub API eller lokal git), og falle tilbake til `main` dersom taggen manglar.

**Pros:**
- Robust mot manglande tags
- Fungerer alltid (med `main` som fallback)

**Cons:**
- Krev nettverkstilgang under bygging
- Tregare bygg (API-kall per schema)
- Kan gi inkonsistente resultat (tag kan bli oppretta etter bygg)
- Skjuler problemet i staden for å løyse det

## Anbefaling

### Anbefalt strategi: A + B.2 (hybrid)

Kombinér **Alternativ A (CI-validering)** med **Alternativ B.2 (release-integrert automatisk tagging)** for best resultat:

1. **Automatisk tagging ved release** (B.2): 
   - Legg til per-schema-tagging i `.github/workflows/release.yml`
   - Garanterer at alle publiserte versjonar får tags automatisk
   - Minimerer manuelt arbeid

2. **CI-validering som safety net** (A):
   - Køyrer på alle PR-ar som endrar schema-versjonar
   - Fangar opp situasjonar der tags manglar (t.d. dersom B.2 feiler)
   - Gjev klår feilmelding med instruksjonar

**Fordeler med hybrid-tilnærming:**
- ✅ Fullstendig automatisert i normaltilfellet (B.2)
- ✅ Safety net dersom automatikken feiler (A)
- ✅ Klår feilmelding til utviklare (A)
- ✅ Minimerer manuelt arbeid
- ✅ Betre enn berre A: slepp manuell tagging
- ✅ Betre enn berre B: validering fangar opp feil

**Alternativ dersom hybrid er for komplekst:**

Bruk **berre Alternativ A (CI-validering)** dersom:
- Enklare implementasjon er prioritert over automatisering
- Release-frekvens er låg (lite manuelt arbeid)
- Team er komfortabel med manuell tagging

Bruk **berre Alternativ B.2 (release-integrert)** dersom:
- Full automatisering er kritisk
- Teamet stoler på at CI alltid fungerer
- Villig til å akseptere edge cases utan validering

## Steg

**For hybrid-strategi (A + B.2):** Følg steg 1-6 (CI-validering) og steg 7 (automatisk tagging).

**For berre A:** Følg steg 1-6.

**For berre B.2:** Følg steg 7.

### 1. Lag valideringsscript (Alternativ A)

- [ ] Opprett `scripts/validate-schema-tags.sh`
- [ ] Scriptet skal iterere over alle `*-schema.yaml`-filer i `src/linkml/`
- [ ] For kvart schema:
  - Les `version`-feltet
  - Ekstraher schema-namn og domene
  - Sjekk om git-tag finst (format: `<schema>-v<versjon>`)
  - Rapporter manglande tags som feil
- [ ] Exit med feilkode dersom nokon tags manglar

**Script-innhald:**

```bash
#!/usr/bin/env bash
# Valider at alle schema-versjonar har korresponderande git-tags
set -euo pipefail

EXIT_CODE=0
MISSING_TAGS=()

echo "Validerer schema-versjonar mot git-tags..."
echo ""

for schema_file in $(find src/linkml -name "*-schema.yaml" -type f); do
    # Les version-feltet (støtt både "version: 1.0.0" og "version: "1.0.0"")
    version=$(grep "^version:" "$schema_file" | sed 's/version: *"\?\([^"]*\)"\?/\1/' | tr -d ' ')
    
    if [ -z "$version" ]; then
        echo "⚠️  $schema_file: mangler version-felt"
        continue
    fi
    
    # Ekstraher schema-namn (fjern -schema.yaml)
    schema=$(basename "$schema_file" .yaml | sed 's/-schema$//')
    domain=$(basename "$(dirname "$(dirname "$schema_file")")")
    
    # Forventa tag-format: <schema>-v<version>
    expected_tag="${schema}-v${version}"
    
    # Sjekk om tag finst
    if git tag -l | grep -q "^${expected_tag}$"; then
        echo "✅ $domain/$schema: versjon $version har git-tag $expected_tag"
    else
        echo "❌ $domain/$schema: versjon $version manglar git-tag $expected_tag"
        MISSING_TAGS+=("$expected_tag")
        EXIT_CODE=1
    fi
done

echo ""
if [ ${#MISSING_TAGS[@]} -gt 0 ]; then
    echo "Følgjande git-tags manglar:"
    for tag in "${MISSING_TAGS[@]}"; do
        echo "  - $tag"
    done
    echo ""
    echo "Opprett manglande tags med:"
    echo "  git tag <tag-namn>"
    echo "  git push origin <tag-namn>"
fi

exit $EXIT_CODE
```

### 2. Lag GitHub Actions workflow

- [ ] Opprett `.github/workflows/validate-schema-tags.yml`
- [ ] Workflow skal køyre på `push` og `pull_request`
- [ ] Checkout med `fetch-depth: 0` (treng full git-historikk for tags)
- [ ] Køyr `scripts/validate-schema-tags.sh`
- [ ] Fail bygget dersom scriptet returnerer feilkode

**Workflow-innhald:**

```yaml
name: Validate schema versions

on:
  push:
    branches: [main]
    paths:
      - 'src/linkml/**/*-schema.yaml'
      - 'scripts/validate-schema-tags.sh'
      - '.github/workflows/validate-schema-tags.yml'
  pull_request:
    paths:
      - 'src/linkml/**/*-schema.yaml'
      - 'scripts/validate-schema-tags.sh'
      - '.github/workflows/validate-schema-tags.yml'

jobs:
  validate-tags:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Treng full git-historikk for tags
      
      - name: Validate schema versions har git-tags
        run: |
          chmod +x scripts/validate-schema-tags.sh
          ./scripts/validate-schema-tags.sh
```

### 3. Dokumenter tagging-konvensjonen

- [ ] Oppdater `CONVENTIONS.md` med seksjon om git-tagging
- [ ] Dokumenter tag-format: `<schema>-v<versjon>` (t.d. `common-ap-no-v1.0.0`)
- [ ] Forklar at tags vert oppretta automatisk av `release-please` ved release
- [ ] Instruksjonar for manuell tagging dersom nødvendig

**Seksjon i CONVENTIONS.md:**

```markdown
### Git-tagging for schema-versjonar

Kvart schema skal ha ein git-tag for kvar publisert versjon.

**Tag-format:** `<schema>-v<versjon>`

Døme:
- `common-ap-no-v1.0.0`
- `dcat-ap-no-v2.10.0`
- `samt-bu-v1.4.0`

**Automatisk tagging:**
`release-please` opprettar automatisk git-tags når ein release-PR vert merga.

**Manuell tagging (dersom nødvendig):**
```bash
# Opprett tag
git tag <schema>-v<versjon>

# Push tag til origin
git push origin <schema>-v<versjon>
```

**Validering:**
CI validerer at alle `version`-felt i `*-schema.yaml`-filer har korresponderande git-tags.
```

### 4. Opprett manglande tags for eksisterande skjema (eingangs-jobb)

- [ ] Identifiser alle skjema som har `version`-felt men manglar git-tag
- [ ] Opprett manglande tags manuelt:
  ```bash
  git tag <schema>-v<versjon>
  git push origin <schema>-v<versjon>
  ```
- [ ] Verifiser at `scripts/validate-schema-tags.sh` passerer

### 5. Test og validering

- [ ] Køyr `scripts/validate-schema-tags.sh` lokalt og sjekk output
- [ ] Opprett ein test-PR som bumpar ein schema-versjon utan å opprette tag
- [ ] Verifiser at CI feiler med klår feilmelding
- [ ] Opprett taggen og sjekk at CI passerer
- [ ] Verifiser at eksisterande PR-ar som ikkje endrar schema-versjonar passerer

### 6. Dokumenter og avslutt (Alternativ A)

- [ ] Oppdater denne specen med eventuelle avvik frå planlagt løysing
- [ ] Marker spec som fullført og flytt til `specs/done/`

### 7. Legg til automatisk tagging ved release (Alternativ B.2)

- [ ] Les `.github/workflows/release.yml` for å forstå eksisterande release-please-oppsett
- [ ] Legg til ny step etter `release-please-action` for å opprette per-schema-tags
- [ ] Stepet skal:
  - Køyre berre dersom `releases_created == 'true'`
  - Iterere over alle `*-schema.yaml`-filer
  - For kvart schema: ekstrahere versjon, bygge tag-namn (`<schema>-v<versjon>`)
  - Sjekke om tag allereie finst (unngå duplikat)
  - Opprette tag med `git tag -a` og pushe til origin
- [ ] Test at workflow køyrer korrekt ved neste release

**Eksempel-implementasjon:**

Legg til følgjande step i `.github/workflows/release-please.yml` **etter linje 186** (etter "Last opp artefaktar til GitHub Releases"):

```yaml
- name: Opprett per-schema git-tags
  if: ${{ steps.release-please.outputs.releases_created == 'true' }}
  env:
    GH_TOKEN: ${{ secrets.RELEASE_PLEASE_TOKEN }}
  run: |
    git config user.name "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    
    echo "Opprettar per-schema tags for release..."
    
    # Iterer berre over schema i paths_released (ikkje alle schema)
    echo '${{ toJSON(steps.release-please.outputs) }}' | jq -r '.paths_released[]' | while read pkg_path; do
      schema_file=$(find "$pkg_path" -maxdepth 1 -name "*-schema.yaml" -type f | head -1)
      
      if [ -z "$schema_file" ] || [ ! -f "$schema_file" ]; then
        echo "⚠️  Ingen schema-fil funne i $pkg_path"
        continue
      fi
      
      # Les versjon frå schema-fil (yq er allereie installert i steg "Oppdater schema-versjonar")
      version=$(yq eval '.version' "$schema_file" 2>/dev/null | tr -d '"' | tr -d ' ')
      
      if [ -z "$version" ] || [ "$version" = "null" ]; then
        echo "⚠️  $schema_file: mangler version-felt"
        continue
      fi
      
      schema=$(basename "$schema_file" .yaml | sed 's/-schema$//')
      domain=$(basename "$(dirname "$(dirname "$schema_file")")")
      tag_name="${schema}-v${version}"
      
      # Sjekk om tag allereie finst
      if git tag -l | grep -q "^${tag_name}$"; then
        echo "✅ Tag $tag_name finst allereie"
        continue
      fi
      
      echo "🏷️  Opprettar tag $tag_name for $domain/$schema"
      git tag -a "$tag_name" -m "Release $schema version $version"
      git push origin "$tag_name"
      echo "::notice::Oppretta git-tag: $tag_name"
    done
```

**Viktige detaljar:**

1. **Itererer berre over `paths_released`**: Meir effektivt enn å iterere over alle schema-filer — opprettar berre tags for skjema som faktisk vart releaset
2. **Brukar `yq` i staden for `grep`**: Same verktøy som steg "Oppdater schema-versjonar", allereie installert
3. **Brukar `RELEASE_PLEASE_TOKEN`**: Same token som resten av workflowen
4. **`::notice::` output**: Gjer tag-namn synlege i GitHub Actions-loggen

**Analyse av eksisterande permissions:**

`.github/workflows/release-please.yml` har allereie nødvendige permissions på linje 21-23:

```yaml
permissions:
  contents: write
  pull-requests: write
```

- ✅ `contents: write` — nødvendig for å opprette og pushe git-tags
- ✅ `pull-requests: write` — brukt av release-please for å opprette release-PR-ar
- ✅ `${{ secrets.RELEASE_PLEASE_TOKEN }}` — brukt for checkout, gh CLI og git push (linje 56, 63, 124, 164)

**Konklusjon:** B.2-implementasjonen kan leggast til i eksisterande `release-please.yml` **utan** å endre permissions. Steget kan bruke same token (`RELEASE_PLEASE_TOKEN`) som resten av workflowen.

**Plassering i workflow:**

Legg til steget **etter linje 186** (etter `Last opp artefaktar til GitHub Releases`), slik at per-schema-tags vert oppretta når alle artefaktar er genererte og lasta opp.

### 8. Test automatisk tagging (Alternativ B.2)

- [ ] Opprett ein test-PR som bumpar ein schema-versjon
- [ ] Merge PR-en og vent på at `release-please` opprettar ein release-PR
- [ ] Merge release-PR-en
- [ ] Verifiser at både hovud-release-tag og per-schema-tag vert oppretta
- [ ] Sjekk at quickstart-URL peikar til riktig tag
- [ ] Verifiser at `scripts/validate-schema-tags.sh` (dersom implementert) passerer

## Handlingsliste

**For hybrid-strategi (anbefalt):**
- [ ] Steg 1: Lag valideringsscript (A)
- [ ] Steg 2: Lag GitHub Actions workflow for validering (A)
- [ ] Steg 3: Dokumenter tagging-konvensjonen
- [ ] Steg 4: Opprett manglande tags for eksisterande skjema
- [ ] Steg 5: Test validering (A)
- [ ] Steg 7: Legg til automatisk tagging ved release (B.2)
- [ ] Steg 8: Test automatisk tagging (B.2)
- [ ] Steg 6: Dokumenter og avslutt

**For berre A (CI-validering):**
- [ ] Steg 1-6

**For berre B.2 (automatisk tagging):**
- [ ] Steg 3: Dokumenter tagging-konvensjonen
- [ ] Steg 4: Opprett manglande tags for eksisterande skjema
- [ ] Steg 7: Legg til automatisk tagging ved release
- [ ] Steg 8: Test automatisk tagging
- [ ] Steg 6: Dokumenter og avslutt

## Utfall

**Implementert:** Alternativ B.2 (automatisk tagging ved release)

**Endringar:**

1. ✅ Lagt til ny step `Opprett per-schema git-tags` i `.github/workflows/release-please.yml` (etter linje 186)
   - Køyrer berre når `releases_created == 'true'`
   - Itererer over `paths_released[]` for effektivitet
   - Brukar `yq` til å lese versjon (same som steg "Oppdater schema-versjonar")
   - Brukar `RELEASE_PLEASE_TOKEN` (same som resten av workflowen)
   - Sjekkar om tag allereie finst før oppretting
   - Loggar `::notice::` for synlegheit i GitHub Actions

2. ✅ Dokumentert git-tagging-konvensjon i `CONVENTIONS.md` (ny seksjon mellom schema-metadata og URI-segment)
   - Tag-format: `<schema>-v<versjon>`
   - Forklaring om automatisk tagging via `release-please`
   - Bruksområde (quickstart-URL-ar)
   - Instruksjonar for manuell tagging ved behov

3. ✅ Oppretta 13 manglande tags for eksisterande skjema:
   - `enhetsregisteret-bvrinn-v1.0.0`
   - `common-ap-no-v1.0.0`
   - `dqv-ap-no-v1.12.0`
   - `dqv-core-v1.0.0`
   - `modelldcat-katalog-v1.0.0`
   - `modelldcat-modell-v1.11.0`
   - `skos-ap-no-v2.12.0`
   - `xkos-ap-no-v1.0.0`
   - `digdir-modellkatalog-v1.0.0`
   - `kartverket-modellkatalog-v1.0.0`
   - `ksdigital-modellkatalog-v1.0.0`
   - `novari-modellkatalog-v1.0.0`
   - `skatteetaten-modellkatalog-v1.0.0`

**Verifisering:**

Køyrde verifiseringsscript som bekrefta at alle 33 schema no har korresponderande git-tags for sin noverande versjon.

**Testing:**

Automatisk tagging vil bli testa ved neste release-PR merge. Manuelt oppretta tags er klare til å brukast av quickstart.sh umiddelbart.

**Avvik frå opphavleg plan:**

Ingen. Implementerte B.2 som planlagt i specen.
