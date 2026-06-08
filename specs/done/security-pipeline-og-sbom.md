# Sikkerhetspipeline og SBOM

## Status

| Tiltak | Status |
|--------|--------|
| CodeQL statisk analyse | ✅ Aktivert i GitHub |
| Dependency Graph | ✅ Aktivert i GitHub |
| Dependabot automatiske PR-er | ⬜ Gjenstår — krever `.github/dependabot.yml` |
| Trivy requirements-skanning | ⬜ Gjenstår |
| SBOM-generering | ⬜ Delvis — Dependency Graph gir grunnleggende SBOM, Trivy gir mer detaljert dekning |

---

## Hva er allerede på plass

### CodeQL
Aktivert via GitHub UI. Skanner Python-koden i `src/mcp-linkml-validator/` og `src/mcp-linkml-generator/` automatisk ved push og PR. Funn vises under **Security → Code scanning alerts**.

Ingen ytterligere konfigurasjon er nødvendig med mindre du ønsker egendefinerte regler eller scanner-innstillinger.

### Dependency Graph
Aktivert via GitHub UI. GitHub oppdager avhengigheter fra `requirements.txt`-filer automatisk og viser dem under **Insights → Dependency graph**.

Dette gir også:
- **Dependabot alerts** — varsler om kjente CVE-er i registrerte avhengigheter (vises under Security-fanen)
- **SBOM-eksport** — GitHub kan eksportere en SPDX-SBOM direkte fra dependency graph via **Insights → Dependency graph → Export SBOM**

---

## Gjenstående tiltak

### Tiltak 1 — Dependabot automatiske PR-er (Svært lav innsats, høy verdi)

Dependency Graph gir varsler, men sender ikke automatiske PR-er. Det krever en `dependabot.yml`-konfigurasjonsfil.

Med filen nedenfor sender Dependabot automatiske PR-er når:
- Python-pakker i requirements.txt har kjente CVE-er eller nye versjoner
- GitHub Actions-versjoner i workflows er utdaterte

**Konfigurasjon:** `.github/dependabot.yml`

```yaml
version: 2
updates:

  - package-ecosystem: pip
    directory: /src/mcp-linkml-validator
    schedule:
      interval: weekly
    open-pull-requests-limit: 5

  - package-ecosystem: pip
    directory: /src/mcp-linkml-generator
    schedule:
      interval: weekly
    open-pull-requests-limit: 5

  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
    open-pull-requests-limit: 10
```

**Merk:** Dependabot dekker ikke `src/assets/containers/requirements-python-test.txt` siden den ikke er i en standardplassering. Denne fanges av Trivy (tiltak 2).

---

### Tiltak 2 — Trivy requirements-skanning (Lav innsats, høy verdi)

Dependency Graph oppdager avhengigheter fra kjente manifestfiler, men Trivy gjør en dypere skanning:
- Fanger `requirements-python-test.txt` som Dependabot ikke dekker
- Rapporterer CVE-er med SARIF-format direkte i **Security → Code scanning alerts** — samme sted som CodeQL
- Grunnlag for mer detaljert SBOM (tiltak 3)

**Konfigurasjon:** `.github/workflows/trivy.yml`

```yaml
name: Trivy

on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 6 * * 2'   # tirsdag morgen

jobs:

  scan-requirements:
    runs-on: ubuntu-22.04
    permissions:
      security-events: write
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: Skann mcp-linkml-validator/requirements.txt
        uses: aquasecurity/trivy-action@0.31.0
        with:
          scan-type: fs
          scan-ref: src/mcp-linkml-validator/requirements.txt
          format: sarif
          output: trivy-validator.sarif

      - name: Skann mcp-linkml-generator/requirements.txt
        uses: aquasecurity/trivy-action@0.31.0
        with:
          scan-type: fs
          scan-ref: src/mcp-linkml-generator/requirements.txt
          format: sarif
          output: trivy-generator.sarif

      - name: Skann assets/requirements-python-test.txt
        uses: aquasecurity/trivy-action@0.31.0
        with:
          scan-type: fs
          scan-ref: src/assets/containers/requirements-python-test.txt
          format: sarif
          output: trivy-assets.sarif

      - name: Last opp resultater til GitHub Security
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: .
          category: trivy-requirements
```

---

### Tiltak 3 — SBOM-generering med Trivy (Lav innsats, god transparens)

GitHub sin Dependency Graph-SBOM dekker kun avhengigheter fra kjente manifestfiler. Trivy genererer en mer komplett SBOM som også inkluderer OS-pakker, transitive avhengigheter og Dockerfile-innhold.

Legg til en egen jobb i `trivy.yml`:

```yaml
  generate-sbom:
    runs-on: ubuntu-22.04
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4

      - name: Generer SBOM for hele repoet
        uses: aquasecurity/trivy-action@0.31.0
        with:
          scan-type: fs
          scan-ref: .
          format: spdx-json
          output: sbom.spdx.json

      - name: Last opp SBOM som artefakt
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.spdx.json
          retention-days: 90
```

For å gjøre SBOM tilgjengelig ved release kan den legges ved som release-asset via `softprops/action-gh-release`.

---

## Prioritering

| Tiltak | Innsats | Verdi | Anbefalt rekkefølge |
|--------|---------|-------|---------------------|
| Dependabot `.yml` | Svært lav — én YAML-fil | Høy — automatiske CVE-PR-er | 1 |
| Trivy requirements-skanning | Lav — én workflow-fil | Høy — dekker filer Dependabot ikke fanger | 2 |
| SBOM med Trivy | Lav (gjenbruker Trivy) | Medium — mer komplett enn Dependency Graph-SBOM | 3 |

---

## Ikke inkludert

| Verktøy | Årsak |
|---------|-------|
| Trivy image-skanning | Krever at build-jobber eksporterer images videre — øker kompleksiteten, vurder separat |
| OSSF Scorecard | Mest relevant for biblioteksrepo som andre prosjekter bygger på |
| Snyk | Overlapper med Dependabot + Trivy, krever ekstern konto |
| Hadolint (Dockerfile-lint) | Lav sikkerhetsverdi — mer kodekvalitet enn sikkerhet |
