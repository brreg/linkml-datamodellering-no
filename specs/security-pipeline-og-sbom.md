# Sikkerheitspipeline og SBOM

## Situasjon

Repoet er no offentleg og inneheld:

- Python-kode i `src/mcp-linkml-validator/` og `src/mcp-linkml-generator/` med `requirements.txt`
- Fire Docker-images bygde frå `Dockerfile.linkml`, `Dockerfile.python`, `Dockerfile.mcp-linkml-validator` og `Dockerfile.mkdocs`
- GitHub Actions-workflows med pinned action-versjonar

Det finst per no ingen automatisk skanning av avhengigheiter, containersårbarheiter, kodekvalitet eller generering av programvareinnhaldsliste (SBOM).

---

## Tiltak

### Tiltak 1 — Dependabot (Lav innsats, høg verdi)

Dependabot sender automatiske PR-ar når Python-pakkar eller GitHub Actions-versjonar har kjende CVE-ar eller nye versjonar.

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

**Merknad:** Dependabot dekkar ikkje `requirements.txt` for assets-containerar (`requirements-python-test.txt`). Desse vert fanga av Trivy (tiltak 3).

---

### Tiltak 2 — CodeQL statisk analyse (Lav innsats, medium verdi)

CodeQL skannar Python-koden i dei to MCP-serverane for kjende sårbarheitsmønster (injeksjon, usikker deserialisering, o.l.). Gratis for public repos.

**Konfigurasjon:** `.github/workflows/codeql.yml`

```yaml
name: CodeQL

on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 6 * * 1'   # måndag morgon

jobs:
  analyze:
    runs-on: ubuntu-22.04
    permissions:
      security-events: write
      contents: read

    steps:
      - uses: actions/checkout@v4

      - name: Initialiser CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: python

      - name: Køyr CodeQL-analyse
        uses: github/codeql-action/analyze@v3
```

Funn dukkar opp under **Security → Code scanning alerts** i GitHub.

---

### Tiltak 3 — Trivy container- og avhengigheitsskanning (Medium innsats, høg verdi)

Trivy skannar:
- Bygde container-images for CVE-ar i OS-pakkar og Python-pakkar
- `requirements.txt`-filer direkte (utan å bygge image)

Trivy kan generere SBOM i SPDX- eller CycloneDX-format — same verktøy løyser både skanning og SBOM (tiltak 4).

**Konfigurasjon:** `.github/workflows/trivy.yml`

```yaml
name: Trivy

on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 6 * * 2'   # tysdag morgon

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

      - name: Last opp resultat til GitHub Security
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: .
          category: trivy-requirements
```

SARIF-formatet gjer at funn dukkar opp i **Security → Code scanning alerts** saman med CodeQL.

**Merknad om image-skanning:** Image-skanning av dei bygde Podman-images krev at `build-*`-jobbane eksporterer images og sender dei vidare. Dette aukar kompleksiteten og bør vurderast som eit separat steg etter at requirements-skanningen er på plass.

---

### Tiltak 4 — SBOM-generering (Medium innsats, god transparens)

Ein SBOM (Software Bill of Materials) dokumenterer alle komponentar og avhengigheiter. Trivy genererer SBOM i SPDX-format direkte frå `requirements.txt` og Dockerfiles.

**Konfigurasjon:** Legg til ein eigen jobb i `trivy.yml`:

```yaml
  generate-sbom:
    runs-on: ubuntu-22.04
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4

      - name: Generer SBOM for heile repoet
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

For å gjere SBOM tilgjengeleg ved release kan det leggast ved som release-asset via `softprops/action-gh-release`.

---

## Prioritering og innsats

| Tiltak | Innsats | Verdi | Prioritet |
|--------|---------|-------|-----------|
| Dependabot | Svært lav — éin YAML-fil | Høg — automatiske CVE-PR-ar | 1 |
| CodeQL | Lav — éin workflow-fil | Medium — skannar Python-kode | 2 |
| Trivy requirements-skanning | Lav — éin workflow-fil | Høg — skannar avhengigheiter | 3 |
| SBOM-generering | Lav (reusar Trivy) | Medium — transparens og compliance | 4 |
| Trivy image-skanning | Medium — krev image-eksport | Høg — fanger OS-sårbarheiter | 5 |

---

## Kva som ikkje er inkludert

| Verktøy | Årsak |
|---------|-------|
| OSSF Scorecard | Relevant, men gir mest verdi for biblioteksrepo som andre prosjekt bygger på |
| GitHub secret scanning push protection | Allereie aktivt automatisk på public repos |
| Snyk | Overlapper med Dependabot + Trivy, krev ekstern konto |
| Dockerfile-lint (Hadolint) | Nyttig, men lav sikkerheitsverdi — meir kodekvalitet |

---

## Samandrag

```
Tiltak 1: .github/dependabot.yml         → PR-ar ved CVE-ar i pip og Actions
Tiltak 2: .github/workflows/codeql.yml   → statisk analyse av Python
Tiltak 3: .github/workflows/trivy.yml    → CVE-skanning av requirements.txt
Tiltak 4: SBOM-jobb i trivy.yml          → SPDX-fil som workflow-artefakt
```

Tiltak 1–4 saman utgjer ein fullverdig basissikkerheit med minimal driftsoverhead. Alle funn samlast i **Security**-fana i GitHub utan ekstra verktøy.
