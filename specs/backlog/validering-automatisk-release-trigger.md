# Automatisk release-PR og release-oppretting

## Bakgrunn

`specs/done/validering-historikk-og-portal.md` implementerte at
valideringsresultat skal fanges ved kvar release og visast i
dokumentasjonsportalen. Men etter manuell køyring av release-please-workflowen
viser alle modellar "Valideringsresultat ikkje tilgjengeleg — ingen release enno".

I tillegg køyrer `validate.yml` validering på kvar push og PR, men loggane
vert berre viste i CI-grensesnittet — dei vert ikkje lagra i repoet. Dette gjer
det vanskeleg å samanlikne validering over tid eller finne ut kva som endra
seg mellom versjonar.

**Rotårsak:** `release-please.yml` køyrer berre via `workflow_dispatch` (manuell
trigger). Heile release-prosessen krev **to** manuelle workflow-køyringar:

1. Brukar køyrer `workflow_dispatch` → release-please opprettar release-PR
2. Brukar mergar release-PR manuelt → **ingenting skjer automatisk**
3. Brukar må køyre `workflow_dispatch` **på nytt** → release-please oppdagar
   merga PR og opprettar faktisk release med tags

`capture-validation` og `update-dates`-jobbane køyrer berre når
`releases_created == 'true'`, som berre vert sett i steg 3.

**Ønskt oppførsel:** Release-PR skal opprettast automatisk når ein semantisk
commit (feat/fix/BREAKING) vert merga til `main` og påverkar minst éin
LinkML-modell. Release skal opprettast automatisk når release-PR vert merga.

**Ekstra problem:** `release-please.yml` linje 34 instruerer brukaren om å
"merge manuelt når validate.yml har passert". Dette skapar ein implisitt
avhengigheit til `validate.yml` som ikkje er nødvendig — `validate.yml` køyrer
allereie på kvar feature-PR før merge til `main`, så når release-PR vert
oppretta (basert på allereie-merga commits) er validering allereie gjort.
Release-PR treng ikkje vente på ny validering.

---

## Design

### Del 1: Lagring av validate-loggar

Kvar gong `validate.yml` køyrer `domain-validate-bronze`, 
`domain-validate-examples` eller `domain-validate-data`, skal JSON-utdata frå
`flatten-and-validate.bash` lagrast i repoet:

```
validation/
  logs/
    <domain>/
      <model>/
        <version>/
          bronze.json
          examples.json
          data.json         ← berre for skjema med data/-katalog
```

**Versjonsnummer:** Henta frå `version:`-feltet i skjemaet (same som
release-please brukar). Dersom skjemaet manglar `version:` (t.d. `referanse`),
bruk `0.0.0-dev`.

**Filformat:** Same JSON-struktur som `validation/<domain>/<model>/<version>.json`
frå `capture-validation`-jobben (sjå `specs/done/validering-historikk-og-portal.md`):

```json
{
  "schema": "ngr-adresse",
  "domain": "ngr",
  "version": "1.2.0",
  "validated_at": "2026-07-01T14:33:04Z",
  "validation_type": "bronze",
  "result": {
    "valid": true,
    "error_count": 0,
    "warning_count": 3,
    "issues": [...]
  }
}
```

`validation_type` kan vere `bronze`, `examples`, `data/<katalog>`, eller
`<policy>` (frå `manifest.yaml`).

**Commit-strategi:** `validate.yml` skal **ikkje** committe validerings-loggar
direkte — det ville trigga nye køyringar i ein loop. I staden:

- **På PR:** lagre loggar som GitHub Actions artifact (`validation-logs`)
- **På push til main:** lagre loggar som artifact + commit til `validation/logs/`
  med `[skip ci]` (same mønster som `update-dates`)

**Alternativ vurdert og forkasta:**

- **Commit på kvar PR:** ville trigga `validate.yml` på nytt i ein loop via
  `push`-triggeren med `paths: src/linkml/**`. `validation/logs/` må unntakast
  frå path-filteret.
  
- **Separate workflow:** unødig kompleks; validate.yml har allereie all
  informasjon som trengst.

### Del 2: Automatisk release-flyt

Release-please treng to separate køyringar (same som før, men no automatisk):

1. **Release-PR-oppretting:** Køyrer på `push` til `main` når semantisk commit
   påverkar minst éin modell → opprettar/oppdaterer release-PR
2. **Release-oppretting:** Køyrer på `pull_request` når release-PR vert merga
   → opprettar faktisk release med tags og trigger `capture-validation` +
   `update-dates`

#### Steg 1: `push`-trigger for release-PR-oppretting

```yaml
on:
  workflow_dispatch:
  push:
    branches: [main]
    paths:
      - 'src/linkml/**/*-schema.yaml'
  pull_request:
    types: [closed]
```

`paths`-filteret sikrar at workflowen berre køyrer når eit skjema er endra.
Release-please analyserer sjølv kva packages som treng versjonsbump basert på
Conventional Commits i git-historikken — path-filteret er berre ein førebels
filter for å spare CI-tid.

#### Steg 2: `pull_request`-trigger for release-oppretting

I `release-please`-jobben, detekter om dette er ein merga release-PR:

```yaml
jobs:
  release-please:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v7
        if: github.event_name == 'pull_request'
        with:
          fetch-depth: 0

      - name: Sjekk om dette er ein merga release-PR
        id: check_release_pr
        if: github.event_name == 'pull_request'
        run: |
          if [ "${{ github.event.pull_request.merged }}" != "true" ]; then
            echo "skip=true" >> $GITHUB_OUTPUT
            echo "PR vart ikkje merga — hoppar over"
            exit 0
          fi
          LABELS=$(gh pr view ${{ github.event.pull_request.number }} \
                   --json labels --jq '.labels[].name')
          if ! echo "$LABELS" | grep -q 'autorelease: pending'; then
            echo "skip=true" >> $GITHUB_OUTPUT
            echo "Dette er ikkje ein release-PR — hoppar over"
            exit 0
          fi
          echo "skip=false" >> $GITHUB_OUTPUT
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - uses: googleapis/release-please-action@v5
        if: github.event_name != 'pull_request' || steps.check_release_pr.outputs.skip != 'true'
        # ... resten av jobben
```

**Alternativ vurdert:**

- **Separate workflows:** Mindre komplekst, men gjer det vanskelegare å forstå
  heilskapen. Éin workflow med to triggerår er meir vedlikehaldbart.

- **`workflow_run`-kjedar:** Unødig kompleks avhengigheit; `push` + `pull_request`
  dekkjer begge behova direkte.

- **Path-filter på `src/linkml/**/*-schema.yaml`:** Ville hoppa over endring av
  datafiler (`.yaml`) under `data/`, eksempelfiler under `examples/`, og 
  manifest-endring. Fordi release-please gjer versjonsbump basert på Conventional
  Commits (som allereie er skrivne), og ikkje path-diff, treng me ikkje
  strengare path-filter enn `*-schema.yaml`.

### Fjerning av validate.yml-avhengigheit

`validate.yml` køyrer allereie på **alle feature-PR-ar** før merge til `main`.
Release-PR vert oppretta **etter** at feature-PR er merga — altså basert på
commits som allereie har passert validering.

Difor skal release-PR **ikkje** vente på ny validering. Notisen i linje 34
("merge manuelt når validate.yml har passert") skal fjernast, og release-PR
skal auto-merge så snart den er oppretta (eller vente på manuell godkjenning
utan validerings-avhengigheit).

**Alternativ til auto-merge:**

- **Auto-merge via GitHub:** Krev at repo har auto-merge aktivert og at
  release-please-action set `pull-request-title-pattern` for å matche branch
  protection rules. Komplisert setup.
  
- **Manuell merge utan validering:** Enklast — release-PR vert oppretta
  automatisk, brukar mergar manuelt når han vil (ikkje når validate.yml passerer).
  
- **Automatisk merge via workflow:** `pull_request_target`-workflow som mergar
  release-PR automatisk etter oppretting. Krev ekstra workflow og `gh pr merge`.

**Vald tilnærming:** Manuell merge utan validerings-avhengigheit. Release-PR
vert oppretta automatisk, notisen om validate.yml vert fjerna, og brukaren
kan merge når han vil — typisk umiddelbart etter review.

### Konsekvens

Etter denne endringa:

1. Brukar mergar feature-PR med `feat(ngr-adresse): ...` → `push`-trigger køyrer
2. Release-please opprettar/oppdaterer release-PR automatisk
3. Brukar mergar release-PR (utan å vente på validate.yml) → `pull_request`-trigger køyrer
4. Release-please opprettar faktisk release
5. `capture-validation` og `update-dates` køyrer automatisk

Heile release-prosessen går frå **to manuelle steg** (workflow_dispatch +
workflow_dispatch) til **éin** (merge release-PR).

---

## Avhengigheiter

- `specs/done/validering-historikk-og-portal.md` — problemet vi prøver å fikse
- `.github/workflows/release-please.yml` — må utvidast med `pull_request`-trigger

---

## Tiltak

### Validate-loggar (Del 1)

| # | Tiltak | Omfang | Prioritet | Status |
|---|---|---|---|---|
| 1 | Lag `src/assets/scripts/save-validation-log.py` | 1 script | Høg | ✓ |
| 2 | Oppdater `Makefile` sine validate-targets til å kalle `save-validation-log.py` | 3 targets | Høg | ✓ |
| 3 | Legg til artifact-upload i `validate.yml` for `validation/logs/` | 1 step | Høg | ✓ |
| 4 | Legg til commit-steg i `validate.yml` (berre på push til main, ikkje PR) | 1 jobb | Høg | ✓ |
| 5 | Utvid `validation/logs/` i `.gitignore` for å unngå lokale loggar | 1 linje | Medium | ✓ |

### Automatisk release (Del 2)

| # | Tiltak | Omfang | Prioritet | Status |
|---|---|---|---|---|
| 6 | Legg til `push`-trigger med `paths`-filter i `release-please.yml` | 1 workflow-fil | Høg | ✓ |
| 7 | Legg til `pull_request`-trigger i `release-please.yml` | 1 workflow-fil | Høg | ✓ |
| 8 | Legg til autorelease-label-sjekk i `release-please`-jobben | 1 step | Høg | ✓ |
| 9 | Betingelseslogikk i `release-please`-jobb for å skilje PR-merge frå push | 1 step | Høg | ✓ |
| 10 | Fjern validate.yml-notisen i "Informer om release-PR"-steget (linje 34) | 1 linje | Høg | ✓ |

### Testing og dokumentasjon

| # | Tiltak | Omfang | Prioritet | Status |
|---|---|---|---|---|
| 11 | Test validate-logg-lagring lokalt med `make domain-validate-bronze` | manuell test | Medium | ✓ |
| 12 | Test med ein feature-PR-merge og release-PR-merge i CI | manuell test | Medium | (venter på commit) |
| 13 | Dokumenter ny flyt i `CONTRIBUTING.md` eller workflow-kommentar | 1 kommentar | Låg | ✓ |
