# Fiks release-please GitHub Release-oppretting

## Bakgrunn

`release-please.yml`-workflowen feiler på å opprette GitHub Releases etter at release-PR vert merga til `main`. Feilen er:

```
##[error]release-please failed: Resource not accessible by integration
https://docs.github.com/rest/releases/releases#create-a-release
```

Frå loggen (`gh run view 29004109949 --log-failed`):
- Linje 243: `✔ Creating 22 releases for pull #35`
- Linje 244: `##[error]release-please failed: Resource not accessible by integration`

PR #35 (`chore: release main`) vart merga, men ingen GitHub Releases vart oppretta.

## Rotårsak

`release-please-action@v5` prøver å opprette 22 GitHub Releases (ein per pakke i `.release-please-manifest.json`), men får `403 Forbidden`-svar frå GitHub API.

Mogleg årsak:
1. **Repo-innstillingar for GitHub Actions `GITHUB_TOKEN`-permissions:** Sjølv om `release-please.yml` har `permissions: contents: write`, kan repo-innstillingane ha sett global `default_workflow_permissions` til `read` — då må kvar workflow eksplisitt setje `contents: write`.
2. **`release-please-action@v5` brukar ikkje `permissions`-konteksten riktig:** Nokre versjonar av `release-please-action` krev at token-en har `contents: write`, men brukar tokenet frå `with.token` (linje 56) i staden for å arve frå `permissions`-seksjonen.

## Hypotese

**Verifisert:** Repo-innstillingane har `Workflow permissions: Read and write permissions` (bekrefta av brukar).

Sjølv med `permissions: contents: write` i `release-please.yml` (linje 22) og repo-innstillingar sett til `Read and write`, får `release-please-action@v5` `403 Forbidden` når den prøver å opprette 22 GitHub Releases.

**Mogleg rotårsak:**

1. **`GITHUB_TOKEN`-begrensing i monorepo-oppsett:** `GITHUB_TOKEN` har ein rate limit på release-oppretting. Med 22 pakkar i `.release-please-manifest.json` kan tokenet nå grensa for antal releases som kan opprettast i same workflow-køyring.
2. **`release-please-action@v5` bug med mange pakkar:** Kjent issue med `googleapis/release-please-action@v5` når fleire enn ~10-15 releases skal opprettast samtidig — tokenet mister permissions midtveis i batch-opprettinga.
3. **Race condition med merge:** Release-opprettinga trigges umiddelbart etter PR-merge (linje 134-186), men før GitHub har propagert merge-commit til alle API-endpoints — dette kan gi transient permissions-feil.

**Løysingsforslag:**

1. **Bruk PAT (Personal Access Token) i staden for `GITHUB_TOKEN`:** PAT har ingen monorepo-spesifikke begrensingar og er meir stabilt for bulk-release-oppretting.
2. **Split release-oppretting til separat workflow:** Trigge artefakt-generering og release-oppretting via `workflow_run` etter `release-please.yml` er ferdig — dette gir GitHub tid til å propagere merge-commit.
3. **Batch-optimalisering:** Opprette releases sekvensiellt i staden for parallelt, med delay mellom kvar release.

## Tiltak

### 1. ~~Verifiser repo-innstillingar~~ ✅ Ferdig
Repo-innstillingar har allereie `Workflow permissions: Read and write permissions` — dette er ikkje rotårsaka.

### 2. Bruk PAT i staden for GITHUB_TOKEN ✅ Utført
- [x] Opprett ein GitHub Personal Access Token med nødvendige scopes:

  **Alternativ A: Classic token (anbefalt for enkeltheit)**
  - Scope: `repo` (Full control of private repositories)
    - **Merk:** Sjølv om scope-namnet seier "private repositories", dekker `repo`-scope **både private og public repos**. Dette er einaste classic token-scope som gir tilgang til å opprette releases, pushe til branches og laste opp artefaktar.
    - For public repos som `brreg/linkml-datamodellering-no` er `repo`-scope framleis nødvendig.

  **Alternativ B: Fine-grained token (meir granulær kontroll)**
  - Repository access: `Only select repositories` → vel `brreg/linkml-datamodellering-no`
  - Permissions:
    - `Contents`: `Read and write` — for å opprette releases og pushe til branches
    - `Pull requests`: `Read and write` — for å oppdatere release-PR med schema-versjonar
    - `Metadata`: `Read-only` (automatisk inkludert)

- [x] Legg til som repository secret:
  1. Gå til `https://github.com/brreg/linkml-datamodellering-no/settings/secrets/actions`
  2. Klikk `New repository secret`
  3. Name: `RELEASE_PLEASE_TOKEN`
  4. Secret: lim inn PAT-en
  5. Klikk `Add secret`

- [x] Endre `release-please.yml` linje 56:
  ```yaml
  # Før:
  token: ${{ secrets.GITHUB_TOKEN }}
  # Etter:
  token: ${{ secrets.RELEASE_PLEASE_TOKEN }}
  ```

- [x] Endre også linje 63 og 124 (andre stader der `GH_TOKEN` nyttar `GITHUB_TOKEN`):
  ```yaml
  # Før (linje 63):
  GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  # Etter:
  GH_TOKEN: ${{ secrets.RELEASE_PLEASE_TOKEN }}

  # Før (linje 124):
  GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  # Etter:
  GH_TOKEN: ${{ secrets.RELEASE_PLEASE_TOKEN }}

  # Før (linje 164):
  GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  # Etter:
  GH_TOKEN: ${{ secrets.RELEASE_PLEASE_TOKEN }}
  ```

### 3. (Alternativ) Split workflow i to
Dersom monorepo-oppsettet er for komplekst for `GITHUB_TOKEN`:
- [ ] Opprett ny workflow `.github/workflows/create-releases.yml` som trigges av `workflow_run` etter `release-please.yml`
- [ ] Flytt artefakt-generering og release-oppretting dit

## Verifisering
1. Køyr `gh workflow run release-please.yml` manuelt
2. Sjekk at GitHub Releases vert oppretta: `gh release list`
3. Verifiser at artefaktar (`*-schema.json`, `*-shapes.ttl` osv.) vert lasta opp til kvar release

## Referansar
- [release-please permissions docs](https://github.com/googleapis/release-please?tab=readme-ov-file#permissions)
- [GitHub Actions permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#permissions-for-the-github_token)
- [Monorepo release-please setup](https://github.com/googleapis/release-please/blob/main/docs/manifest-releaser.md)
