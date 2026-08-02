# Release-please scope-mapping

## Bakgrunn

**Problem:** Når ein commit skrives som `fix(samt-bu): ...` så skal berre `samt-bu`-pakken få ny versjon, men no vert alle skjema versjonerte. Dette skjer fordi release-please ikkje automatisk mappar commit-scope (`samt-bu`) til package-path (`src/linkml/samt/samt-bu/`).

**Målet:** Berre den spesifikke pakken som er endra skal få ny versjon i release-please-PR-en.

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

## Handlingsliste

- [ ] Oppdater `.github/release-please-config.json` med `separate-pull-requests: true`
- [ ] Verifiser scope-sjekk i `.github/workflows/release-please.yml`
- [ ] Test med ein enkel commit (`fix(samt-bu): test scope-mapping`)
- [ ] Verifiser at berre `samt-bu` får ny versjon i release-please-PR-en
