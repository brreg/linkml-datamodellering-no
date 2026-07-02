# Plan: Rulle tilbake release-please til fungerande versjon

## Bakgrunn

Release-please har ikkje fungert sidan commit f65f9086c16091c4c7cd2781c8270b965bbc266e (2026-06-20).

Den committen introduserte:
- Bruk av `RELEASE_PLEASE_TOKEN` (admin PAT) i staden for `GITHUB_TOKEN`
- Auto-merge-funksjonalitet for release-PR-ar
- Direkte push til main etter release (capture-validation og update-dates)

Etterfølgjande commits (337e1581, 8ab8e99a, bc2149ba, 25f8ddae) prøvde å fikse problemer ved å:
- Flytte validation/dates til `update-release-pr.yml` (køyrer på release-PR i staden for post-merge)
- Splitta release-oppretting til eigen `create-releases.yml` workflow
- Legge til diverse permissions (`id-token: write`, `workflows: write`)

**Problem:** Desse endringane har gjort workflowen kompleks og ustabil. Me treng å gå tilbake til ein enklare, fungerende baseline.

## Målet

Rulle tilbake release-please til versjonen **før** commit f65f9086, med desse karakteristikkar:
- Éin einkel `release-please.yml` workflow
- Brukar berre `GITHUB_TOKEN` (ikkje PAT)
- Opprettar release-PR på push til main
- Opprettar faktiske releases når PR vert merga
- Køyrer capture-validation og update-dates **etter** release er oppretta (post-merge push til main)

**Avhengigheiter:**
- `update-release-pr.yml` (ny fil, introdusert i 337e1581) må integrerast eller slettast
- `create-releases.yml` (ny fil, introdusert i 25f8ddae) må slettast
- Repo-innstilling `allow_auto_merge` kan deaktiverast (introdusert i f65f9086)

## Handlingsliste (prioritert)

### RB1: Undersøk status quo
- [✓] Les gjeldande `release-please.yml` for å forstå noverande tilstand
- [✓] Les `update-release-pr.yml` for å forstå kva den gjer
- [✓] Les `create-releases.yml` for å forstå kva den gjer
- [✓] Identifiser kva som er nytt/nyttig vs. kva som kan reverterast

**Resultat:** Gjeldande oppsett splittar release-please i tre workflows. `release-please.yml` berre opprettar PR, `update-release-pr.yml` køyrer validation/dates på PR før merge, `create-releases.yml` opprettar faktiske releases etter merge.

### RB2: Identifiser baseline-versjon
- [✓] Hent ut `release-please.yml` frå commit f65f9086~1 (forelder til den problematiske committen)
- [✓] Verifiser at denne versjonen hadde følgjande struktur:
  - Jobb 1: `release-please` — opprettar PR eller releases
  - Jobb 2: `capture-validation` — køyrer etter releases_created
  - Jobb 3: `update-dates` — køyrer etter releases_created
- [✓] Dokumenter at desse jobbane køyrde **post-merge** (etter at release-PR vart merga og releases oppretta)

**Resultat:** Baseline identifisert. Éin workflow med 3 jobbar som køyrer på `push` til main (både PR-oppretting og release-oppretting i same trigger).

### RB3: Restaurer baseline-versjon
- [✓] Kopier `release-please.yml` frå f65f9086~1 til gjeldande fil
- [✓] Fjern alle referansar til `RELEASE_PLEASE_TOKEN` — bruk berre `GITHUB_TOKEN`
- [✓] Fjern auto-merge-steget (det vart introdusert i f65f9086)
- [✓] Verifiser at `token:` ikkje er spesifisert i `release-please-action` (standard er `GITHUB_TOKEN`)

**Avvik frå opphavleg plan:** Behalde commit-type-filtrering frå f1bb704e (nyttig funksjonalitet). Oppgradere checkout frå `@v6` til `@v7`.

### RB4: Handter nye workflows
- [✓] Slett `.github/workflows/create-releases.yml` (introdusert i 25f8ddae, ikkje nødvendig med baseline-versjon)
- [✓] Vurder `update-release-pr.yml`:
  - Dersom den **berre** handterer oppdatering av release-PR under utvikling, behald han
  - Dersom den **dupliserer** capture-validation/update-dates frå baseline, slett han
- [✓] Dokumenter avgjersla i denne specen

**Avgjerd:** Begge sletta. `update-release-pr.yml` dupliserer capture-validation/update-dates som no køyrer post-merge i baseline-versjonen. `create-releases.yml` er ikkje nødvendig sidan baseline handterer alt i éin workflow.

### RB5: Oppdater GOVERNANCE.md
- [✓] Fjern eller kommenter ut seksjonen om "Unntak frå review-krav for release-PR" (introdusert i f65f9086)
- [✓] Dokumenter at release-PR-ar **krev manuell merge** (ikkje auto-merge)

**Resultat:** GOVERNANCE.md oppdatert — auto-merge-dokumentasjon fjerna, release-PR krev no manuell merge.

### RB6: Verifiser at baseline-logikken er intakt
- [✓] Sjekk at `release-please.yml` triggar på:
  - `on: push: branches: [main]` — for PR-oppretting **og** release-oppretting
- [✓] Sjekk at `capture-validation` og `update-dates` har:
  - `needs: release-please`
  - `if: ${{ needs.release-please.outputs.releases_created == 'true' }}`
- [✓] Sjekk at dei pushar direkte til main etter release

**Resultat:** ✅ Baseline-logikk intakt. Alle tre jobbar køyrer på same trigger (`push` til main).

### RB7: Test lokalt (tørrkøyring)
- [✓] Valider YAML-syntaks: `yamllint .github/workflows/release-please.yml`
- [✓] Sjekk at ingen workflows refererer til sletta filer
- [✓] Kjør `make lint` og `make validate-instance` på eit testsett for å sikre at ingen eksterne avhengigheiter er brote

**Resultat:** ✅ YAML syntaks OK, ingen referansar til sletta workflows funne.

### RB8: Commit og deploy
- [✓] Lag ein commit som **fullstendig erstattar** gjeldande `release-please.yml` med baseline-versjonen
- [✓] Slett `create-releases.yml` i same commit
- [✓] Oppdater `GOVERNANCE.md` i same commit
- [✓] Commit-melding skal referere til denne specen og forklare rollback-grunnen
- [ ] **Ikkje merge via PR** — push direkte til main (dersom tillate), eller be brukar om å merge manuelt

**Commit-melding generert:**
```
fix(ci): rull tilbake release-please til baseline før f65f9086

- .github/workflows/release-please.yml: restaurer éin-workflow-struktur frå f65f9086~1 med 3 jobbar (release-please, capture-validation, update-dates), behalde commit-type-filtrering frå f1bb704e
- .github/workflows/create-releases.yml: slett (introdusert i 25f8ddae, erstattet av baseline)
- .github/workflows/update-release-pr.yml: slett (introdusert i 337e1581, dupliserer baseline-funksjonalitet)
- GOVERNANCE.md: fjern auto-merge-dokumentasjon, release-PR krev no manuell merge
- Løyser ustabilitet introdusert av PAT-bruk, auto-merge og split-workflow-logikk
- Sjå specs/backlog/rollback-release-please.md for fullstendig plan og avgjerdsgrunnar
```

## Risiko

- **Direkte push til main:** Baseline-versjonen pushar valideringsresultat og datoannotasjonar direkte til main etter release. Dersom branch-protection no blokkerer dette, må me:
  1. Midlertidig deaktivere branch-protection for github-actions[bot]
  2. Eller akseptere at desse stega feiler (men releases vert framleis oppretta)

- **RELEASE_PLEASE_TOKEN kan vere nødvendig:** Dersom GitHub sin loop-prevention (GITHUB_TOKEN triggar ikkje andre workflows) er eit reelt problem, kan me ikkje unngå PAT. I så fall må me:
  1. **Ikkje** rulle tilbake heilt
  2. Behalde PAT, men **fjerne auto-merge** og forenkle logikken

**Korleis avgjere:** Test baseline-versjonen først. Dersom release-please fungerer men capture-validation/update-dates ikkje triggar andre workflows, dokumenter dette som eit kjent avvik.

## Suksesskriterium

- [ ] Release-please opprettar ein release-PR når skjema-filer vert endra på main
- [ ] Brukar kan merge release-PR manuelt (ikkje auto-merge)
- [ ] Etter merge opprettar release-please faktiske GitHub releases og tags
- [ ] `capture-validation` og `update-dates` køyrer **etter** releases er oppretta
- [ ] Ingen "Resource not accessible by integration"-feil
- [ ] Ingen "Repository rule violations"-feil (eller desse er dokumenterte og aksepterte)

## Neste steg etter rollback

Når baseline-versjonen fungerer, kan me vurdere inkrementelle forbetringar:
1. Flytte capture-validation/update-dates til **release-PR** (før merge) i staden for post-merge
2. Vurdere auto-merge **berre** dersom det faktisk løyser eit problem (ikkje prematurt)
3. Teste `RELEASE_PLEASE_TOKEN` berre dersom GITHUB_TOKEN er dokumentert som eit faktisk problem

---

## Utført

**Dato:** 2026-07-02

**Resultat:** Rollback fullført. Release-please restaurert til baseline-versjon (f65f9086~1) med følgjande endringar:

- ✅ **RB1-RB3:** Baseline-versjon identifisert og restaurert — éin workflow med 3 jobbar
- ✅ **RB4:** `create-releases.yml` og `update-release-pr.yml` sletta (dupliserte baseline-funksjonalitet)
- ✅ **RB5:** GOVERNANCE.md oppdatert — fjerna auto-merge-dokumentasjon
- ✅ **RB6:** Baseline-logikk verifisert — capture-validation/update-dates køyrer post-merge
- ✅ **RB7:** YAML-syntaks og workflow-referansar validerte
- ✅ **RB8:** Commit-melding generert

**Avvik frå opphavleg plan:**
- Behalde commit-type-filtrering (frå f1bb704e) — nyttig funksjonalitet
- Oppgradere checkout frå `@v6` til `@v7` for konsistens med resten av repoet

**Kjent risiko:**
- Capture-validation og update-dates køyrer **post-merge** (pushar direkte til main)
- Dersom branch-protection blokkerer dette, vil desse jobbane feile
- Løysing: Midlertidig deaktivere branch-protection for github-actions[bot], eller akseptere at validation-loggar/datoar ikkje oppdaterast automatisk

**Neste test:**
Brukar må merge neste release-PR manuelt og verifisere at:
1. Release-please opprettar faktiske releases og tags
2. Capture-validation og update-dates køyrer etter release-oppretting
3. Ingen "Resource not accessible by integration"-feil
