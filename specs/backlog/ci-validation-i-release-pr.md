# CI: Inkluder validation-loggar og datoannotasjonar i release-PR

## Bakgrunn

`release-please.yml` har to jobbar som køyrer **etter** at release-PR er merga:
- `capture-validation` — fangar valideringsresultat og committer til `validation/logs/`
- `update-dates` — oppdaterer `annotations.endringsdato`, DQV-kvalitetsmålingar og ModelDCAT-modellelement

Desse jobbane prøver å pushe direkte til `main` med `GITHUB_TOKEN`, men branch protection-reglar blokkerer direkte push:

```
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: - Changes must be made through a pull request.
remote: - Required status check "validate" is expected.
```

**Løysing:** Flytt desse oppdateringane til **release-PR-en sjølv**, slik at dei vert inkluderte i merge-committen i staden for å verte pusha etterpå.

## Krav

1. `release-please-action` skal **automatisk committe** validation-loggar, datoannotasjonar, DQV-målingar og ModelDCAT-element til release-PR-en før ho vert merga
2. Branch protection-reglar skal forbli aktive — ingen bypass for `github-actions[bot]`
3. Release-PR-en skal innehalde alle endringar som no ligg i `capture-validation` og `update-dates`-jobbane

## Steg

### Steg 1: Opprett ny workflow `update-release-pr.yml`

Ny workflow som triggas når `release-please-action` **opprettar eller oppdaterer** ein release-PR (identifisert via `autorelease: pending`-label).

Workflow-struktur:

```yaml
on:
  pull_request:
    types: [labeled, synchronize]

jobs:
  update-release-pr:
    if: contains(github.event.pull_request.labels.*.name, 'autorelease: pending')
    runs-on: ubuntu-22.04
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v7
        with:
          ref: ${{ github.event.pull_request.head.ref }}
          token: ${{ secrets.GITHUB_TOKEN }}
      
      # Køyr same steg som no ligg i capture-validation og update-dates
      - name: Hent mcp-validator-image
      - name: Fang valideringsresultat
      - name: Oppdater datoannotasjonar
      - name: Oppdater DQV-kvalitetsmålingar
      - name: Hent linkml-local-image
      - name: Oppdater ModelDCAT-modellelement
      
      - name: Commit og push til release-PR
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          if ! git diff --quiet; then
            git add validation/ src/linkml/
            git commit -m "chore(*): oppdater validation-loggar, datoannotasjonar, DQV og ModelDCAT-element [skip ci]"
            git push
          fi
```

**Trigger-betingelse:** Køyrer når ein PR med `autorelease: pending`-labelen vert oppretta eller oppdatert.

### Steg 2: Fjern `capture-validation` og `update-dates` frå `release-please.yml`

Desse jobbane skal **ikkje lenger køyre** etter at release-PR er merga, fordi endringane allereie ligg i PR-en.

Slett linene 93–197 i `release-please.yml`.

### Steg 3: Oppdater kommentar om race condition i `release-please.yml`

Kommentaren på linje 130–146 skildrar ein race condition mellom `update-dates` og `generate.yml`. Denne race condition-en vert løyst av denne endringa — oppdater kommentaren eller fjern ho.

### Steg 4: Test workflowen

**Pre-test validering:**
- ✓ YAML-syntaks validert med Python yaml.safe_load()
- ✓ Workflow brukar same label-sjekk som release-please.yml (`autorelease: pending`)
- ✓ Permissions set: `contents: write`, `pull-requests: write`

**Testplan (krev manuell køyring av brukar):**

1. **Commit dei nye workflow-filene:**
   ```bash
   git add .github/workflows/update-release-pr.yml
   git add .github/workflows/release-please.yml
   git add specs/backlog/ci-validation-i-release-pr.md
   git commit -m "fix(ci): flytt validation/dates-oppdatering til release-PR i staden for post-merge push

     - .github/workflows/update-release-pr.yml: ny workflow som oppdaterer release-PR
     - .github/workflows/release-please.yml: fjerna capture-validation og update-dates-jobbar
     - specs/backlog/ci-validation-i-release-pr.md: spesifikasjon og testplan
     - løyser GH013 branch protection-feil ved å inkludere alle endringar i PR før merge"
   ```

2. **Push til main** (trigger release-please dersom det finst uutgjevne feat/fix-commits):
   ```bash
   git push
   ```

3. **Sjekk om release-PR vert oppretta:**
   ```bash
   gh pr list --label "autorelease: pending"
   ```

4. **Verifiser at `update-release-pr.yml` køyrer:**
   - Gå til Actions-fana i GitHub
   - Sjekk at "Update Release PR"-workflowen køyrer når PR-en vert oppretta/labela
   - Verifiser at workflowen committer til release-PR-branchen

5. **Sjekk commit-historikken i release-PR:**
   ```bash
   gh pr view <PR_NUMBER> --json commits --jq '.commits[].messageHeadline'
   ```
   Skal innehalde: `chore(*): oppdater validation-loggar, datoannotasjonar, DQV og ModelDCAT-element`

6. **Merge release-PR** og verifiser at `release-please.yml` køyrer utan "push declined"-feil:
   ```bash
   gh pr merge <PR_NUMBER> --squash
   gh run list --workflow=release-please.yml --limit 1
   ```

7. **Verifiser at releases vert oppretta:**
   ```bash
   gh release list --limit 5
   ```

## Avhengigheiter

- Ingen

## Prioritert handlingsliste

- [x] Steg 1: Opprett `update-release-pr.yml` — `.github/workflows/update-release-pr.yml` oppretta med trigger på `labeled` og `synchronize` for PR-ar med `autorelease: pending`-label
- [x] Steg 2: Fjern `capture-validation` og `update-dates` frå `release-please.yml` — linene 94–198 fjerna, race condition-kommentaren fjerna saman med jobbane
- [x] Steg 3: Oppdater/fjern race condition-kommentar — ikkje lenger nødvendig, allereie fjerna i Steg 2
- [x] Steg 4: Test workflowen — YAML-syntaks validert, testplan dokumentert (krev manuell køyring av brukar)

## Alternativ (ikkje føretrekt)

Leggje til GitHub Actions som bypass-actor i branch protection-reglar:

```bash
gh api repos/brreg/linkml-datamodellering-no/rulesets/16642329 \
  --method PUT \
  --field bypass_actors[][actor_id]=15368 \
  --field bypass_actors[][actor_type]=Integration \
  --field bypass_actors[][bypass_mode]=always
```

Dette ville late `github-actions[bot]` pushe direkte til `main`, men bryt prinsippet om at **alle endringar skal gå gjennom PR**.
