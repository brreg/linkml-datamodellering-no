# Fiks manglande .github/-mappe i validate.yml sitt source-artefakt

## Bakgrunn

CI-jobben `build-image / linkml-local` (og `build-image / mcp-linkml-validator`)
i `Validate`-workflowen feila konsekvent på steget "Oppgrader crun" med:

```
Can't find 'action.yml', 'action.yaml' or 'Dockerfile' under
'.../.github/actions/upgrade-crun'. Did you forget to run actions/checkout
before running your local action?
```

**Diagnose (via `gh run view 30946613147`):** `actions/download-artifact@v8`-
steget rett før lykkast (grønt hakemerke), men den lokale actionen
`./.github/actions/upgrade-crun` vart likevel ikkje funnen. Feilen oppstod på
commit `9bbf39a9` (før parallelliseringsendringa i `generate.yml`), så det er
ein separat, eksisterande CI-bug — ikkje forårsaka av nyleg arbeid.

**Rotårsak:** `checkout-source`-jobben i `validate.yml` (linje 127-135) lastar
opp eit `source`-artefakt med `.github/` inkludert i `path:`, men manglar
`include-hidden-files: true`. Frå og med `actions/upload-artifact@v4` vert
skjulte filer/mapper (alt som startar med `.`) **ekskludert som standard** —
`.github/` er difor stille droppa frå artefaktet, sjølv om det står eksplisitt
i `path:`-lista. Nedstraums jobbar (`ensure-images`, `validate`) brukar
`actions/download-artifact@v8` i staden for `actions/checkout@v7` (for å
gjenbruke det allereie sjekka ut kjeldetreet), og finn difor ikkje
`.github/actions/upgrade-crun/action.yml`.

`generate.yml` har **det identiske mønsteret** (upload av `.github/` som del
av eit gjenbrukt source-artefakt) og har alt `include-hidden-files: true`
sett (linje 81) — `validate.yml` fekk berre aldri same fiks då mønsteret vart
kopiert/utvikla uavhengig.

## Steg

### 1. Legg til `include-hidden-files: true` i `validate.yml`

`checkout-source`-jobben sitt `actions/upload-artifact@v7`-steg (linje 127-136):

```yaml
- uses: actions/upload-artifact@v7
  with:
    name: source
    path: |
      src/
      .github/
      Makefile
      make/
    retention-days: 1
    include-hidden-files: true
```

### 2. Verifiser at ingen andre workflow-filer har same mangel

Sjekka `release.yml` (brukar `actions/checkout@v7` direkte i kvar jobb før
`upgrade-crun` — ikkje råka) og det andre `upload-artifact`-steget i
`validate.yml` (linje 248, lastar berre opp `validation-logs`, ingen
`.github/`-avhengigheit — ikkje råka). Ingen andre stader treng fiksen.

### 3. Kjør `actionlint`

Obligatorisk etter CI-endring (jf. CLAUDE.md). Berre `[shellcheck]`-stilråd i
urelaterte, eksisterande steg (linje 37, 295) — ingen `[expression]`-feil.

## Handlingsliste

- [x] Legg til `include-hidden-files: true` i `checkout-source` sitt upload-artifact-steg
- [x] Verifiser at ingen andre workflow-filer har same mangel
- [x] Kjør `actionlint` mot `validate.yml`

## Utført

- `.github/workflows/validate.yml`: `include-hidden-files: true` lagt til i `checkout-source` sitt `actions/upload-artifact@v7`-steg — same fiks som alt finst i `generate.yml` for identisk mønster
- Stadfesta via `gh run view` at feilen er ein eksisterande CI-bug, ikkje forårsaka av nyleg parallelliseringsarbeid i `generate.yml`
- `actionlint` køyrd — ingen `[expression]`-feil
