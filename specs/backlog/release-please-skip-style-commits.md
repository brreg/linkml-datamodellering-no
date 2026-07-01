# Ekskluder style-commits frå release-please push-trigger

## Bakgrunn

Etter implementering av automatisk release-flyt (`specs/done/validering-automatisk-release-trigger.md`), 
feila `release-please.yml` med "Resource not accessible by integration" når
`style:`-commit vart pusha til main.

**Rotårsak:** `push`-triggeren i `release-please.yml` har path-filter
`src/linkml/**/*-schema.yaml`. Style-commit (`erstatt-unicode-en-dash.md`)
endra kommentarar/beskrivingar i mange *-schema.yaml-filer, så triggeren vart
aktiv. Release-please fann då den allereie-merga release-PR #24 og prøvde å
opprette release på nytt, men dette feila.

**Problem:** `push`-triggeren skal **berre** trigge for semantiske commits
(feat/fix/BREAKING) som faktisk endrar API/modell, ikkje for style/docs/chore
som berre endrar formatering/kommentarar.

---

## Design

### Løysing: Ekskluder style/docs/chore-commits frå push-trigger

Release-please har innebygd støtte for å ignorere commits basert på
conventional commit-type. Men `push`-triggeren i GitHub Actions har ingen
måte å filtrere på commit-melding — han triggar på path-endring uavhengig
av commit-type.

**Alternativ:**

1. **Legg til `[skip ci]` i style-commits:** Enkelt, men krev manuell
   disiplin. Gløymer ein `[skip ci]`, triggar release-please.

2. **Fjern `paths`-filter frå push-trigger:** Release-please vil då trigge
   på **kvar** push til main, inkludert README-endring, workflow-endring osv.
   Dette er tungt, men release-please vil sjølv sjekke om det finst semantiske
   commits som treng release-PR.

3. **Legg til tidleg exit i release-please-jobben:** Sjekk om siste commit
   er `style:`, `docs:` eller `chore:` og hopp over release-please om det er tilfellet.

**Vald løysing:** Alternativ 3 — tidleg exit basert på commit-type.

### Implementering

Legg til eit steg før `googleapis/release-please-action@v5` som sjekkar siste
commit-melding og hoppar over release-please om det er ein style/docs/chore-commit:

```yaml
- name: Sjekk om siste commit skal trigge release-please
  id: check_commit_type
  if: github.event_name == 'push'
  run: |
    COMMIT_MSG=$(git log -1 --pretty=%B)
    if echo "$COMMIT_MSG" | grep -qE '^(style|docs|chore|test|ci|build|perf|refactor)(\(.*\))?:'; then
      echo "skip=true" >> $GITHUB_OUTPUT
      echo "Siste commit er ikkje ein release-utløysande type — hoppar over"
      exit 0
    fi
    echo "skip=false" >> $GITHUB_OUTPUT
```

Oppdater `googleapis/release-please-action@v5`-steget til:

```yaml
- uses: googleapis/release-please-action@v5
  if: |
    (github.event_name != 'pull_request' && steps.check_commit_type.outputs.skip != 'true') ||
    (github.event_name == 'pull_request' && steps.check_release_pr.outputs.skip != 'true')
```

**Alternativ implementering — bruk release-please sin innebygde ignore:**

Release-please har `.release-please-manifest.json` og `release-please-config.json`
som kan konfigurere kva commit-typar som skal ignorerast. Men dette gjeld berre
**innanfor** release-please sin logikk — ikkje GitHub Actions sin `push`-trigger.

Difor må me ha tidleg exit i workflow-fila for å unngå unødig køyring.

---

## Avhengigheiter

- `specs/done/validering-automatisk-release-trigger.md` — opphavleg implementering
- `.github/workflows/release-please.yml` — må oppdaterast

---

## Tiltak

| # | Tiltak | Omfang | Prioritet | Status |
|---|---|---|---|---|
| 1 | Legg til `check_commit_type`-steg før release-please-action | 1 step | Høg | ✓ |
| 2 | Oppdater `if`-betingelse på `googleapis/release-please-action@v5` | 1 linje | Høg | ✓ |
| 3 | Test med ein style-commit og verifiser at release-please ikkje køyrer | CI-test | Medium | (venter på push) |
| 4 | Test med ein feat-commit og verifiser at release-PR vert oppretta | CI-test | Medium | (framtidig) |

## Utført

**Tiltak 1:** Lagt til `check_commit_type`-steg som sjekkar om siste commit er
style/docs/chore/test/ci/build/perf/refactor og set `skip=true` om det er tilfellet.

**Tiltak 2:** Oppdatert `if`-betingelse på `googleapis/release-please-action@v5`:
- Push-event: køyrer berre om `check_commit_type.outputs.skip != 'true'`
- Pull-request-event: køyrer berre om `check_release_pr.outputs.skip != 'true'`
- Workflow-dispatch: køyrer alltid

Checkout-steget vart også oppdatert til å køyre alltid (ikkje berre for pull_request),
sidan `check_commit_type` treng `git log`.
