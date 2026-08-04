# Release-please scope-mapping

## Bakgrunn

**Problem 1:** Når ein commit skrives som `fix(samt-bu): ...` så skal berre `samt-bu`-pakken få ny versjon, men no vert alle skjema versjonerte. Dette skjer fordi release-please ikkje automatisk mappar commit-scope (`samt-bu`) til package-path (`src/linkml/samt/samt-bu/`).

**Problem 2:** Release-please avbryt med feilmeldinga `⚠ There are untagged, merged release PRs outstanding - aborting` når ein release-PR er merga men ikkje tagga enno. Dette skjer fordi workflowen prøver å kjøre igjen før taggingsteg har fullført.

**Målet:** 
1. Berre den spesifikke pakken som er endra skal få ny versjon i release-please-PR-en
2. Merged release-PR-ar skal taggast automatisk utan at dette blokkerer neste release-please-køyring

**Relevante filer:**
- `.github/release-please-config.json` — release-please-konfigurasjon for monorepo
- `.github/release-please-manifest.json` — noverande versjonar per pakke
- `.github/workflows/release-please.yml` — workflow som køyrer release-please

## Steg

### 1. Oppdater release-please-config.json

Legg til `separate-pull-requests: true` på toppnivå (utanfor `packages`) for å sikre at kvar pakke får sin eigen PR, og legg til `include-component-in-tag: false` (standard er `true`, men me vil ha `<schema>-v<version>`-format).

Eksempel:
```json
{
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
  "separate-pull-requests": true,
  "include-component-in-tag": false,
  "packages": {
    "src/linkml/ap-no/cpsv-ap-no": {
      "component": "cpsv-ap-no",
      "release-type": "simple"
    },
    ...
  }
}
```

### 2. Verifiser at scope-sjekk i release-please.yml er aktiv

Workflowen har allereie ein scope-sjekk (linje 29-72) som hoppar over commit som ikkje har gyldig modell-scope. Sjekk at dette fungerer som forventa.

### 3. Test med ein enkel commit

```bash
# Test med ein commit som berre endrar samt-bu
git commit --allow-empty -m "fix(samt-bu): test scope-mapping"
git push
```

Forventa resultat:
- Berre `samt-bu` skal få ny versjon i release-please-PR-en
- Andre pakkar skal ikkje få endringar

## Analyse

**Feil frå siste køyring (2026-08-02T18:17):**

```
❯ Found pull request #50: 'chore: release main'
⚠ pullRequestTitlePattern miss the part of '${scope}'
⚠ pullRequestTitlePattern miss the part of '${component}'
⚠ pullRequestTitlePattern miss the part of '${version}'
✔ Pull request contains releases, but not for component: 
⚠ There are untagged, merged release PRs outstanding - aborting
```

**Rotårsak:**

1. PR #50 vart merga 2026-08-02T18:17:16Z
2. Release-please-workflowen køyrde igjen 2026-08-02T18:17:33Z (17 sekund seinare)
3. Taggingsteg i workflowen hadde ikkje rukke å fullføre før neste køyring starta
4. Release-please avbryt fordi den finn ein merga PR (#50) som ikkje har taggar enno

**Løysing:**

1. `separate-pull-requests: true` er allereie lagt til i `.github/release-please-config.json` (✅)
2. Me må **ikkje** prøve å fikse `pullRequestTitlePattern`-warninga — det er berre ein varselmeld som ikkje hindrar funksjonalitet
3. **Vent til taggingsteg er ferdig** før me testar på nytt

## Løysing

**Deadlock-årsak:** 
PR #50 vart oppretta **før** `separate-pull-requests: true` vart aktivert, så den inneheld endringar for **alle** skjema. Når PR-en vart merga, hadde release-please ikkje tid til å opprette taggar før neste køyring starta. No avbryt release-please fordi den finn ein merga PR utan taggar.

**Løysing:**
1. Behald `separate-pull-requests: true` i config (allereie gjort ✅)
2. Manuelt trigge workflow med `workflow_dispatch` for å la release-please opprette releases og taggar for PR #50
3. Dersom det ikkje fungerer: manuelt trigge `gh release create` for kvar pakke som manglar release

**Alternativ:** Close PR #50 utan å merga (men den er allereie merga, så det hjelper ikkje).

## Handlingsliste

- [x] Oppdater `.github/release-please-config.json` med `separate-pull-requests: true`
- [x] Verifiser scope-sjekk i `.github/workflows/release-please.yml`
- [ ] Trigge workflow manuelt med `gh workflow run release-please.yml`
- [ ] Sjekk om releases vart oppretta
- [ ] Test med ein enkel commit (`fix(samt-bu): test scope-mapping`)
- [ ] Verifiser at berre `samt-bu` får ny versjon i release-please-PR-en

## Kommandoar

```bash
# Trigge workflow manuelt
gh workflow run release-please.yml

# Sjekk status
gh run list --workflow=release-please.yml --limit 3

# Sjekk om releases vart oppretta
gh release list --limit 5
```
