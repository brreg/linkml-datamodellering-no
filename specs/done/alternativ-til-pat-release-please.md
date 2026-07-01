# Alternativ til PAT for release-please

## Bakgrunn

`release-please.yml` brukar `RELEASE_PLEASE_TOKEN` (ein fine-grained PAT frå admin-konto) for å:
1. Opprette release-PR med `googleapis/release-please-action@v5`
2. Aktivere auto-merge på PR-en
3. Pushe direkte til `main` (i `update-dates` og `capture-validation` jobbane)

Dette fungerer fordi PAT-en er knytt til admin-kontoen som står på bypass-lista for branch protection-regelen.

**Problemet:** Vi får ikkje til å opprette ein fungerande PAT. Dette blokkerer release-prosessen.

---

## Prioritert handlingsliste

### Alternativ A: GitHub App med installasjon-token (anbefalt)

Ein GitHub App (installert i organisasjonen/repoet) kan generere korttidslevande installasjon-token som kan brukast i staden for PAT. Fordeler:

- **Ingen personleg konto:** App-en er uavhengig av enkeltbrukarar
- **Finare tilgangskontroll:** Kan avgrensast til spesifikke repo og permissions
- **Korttidslevande token:** Installasjon-token er gyldige i 1 time (auto-fornya av action)
- **Auditerbart:** Alle handlingar vert logga som app-namnet, ikkje ein person
- **Bypass-støtte:** GitHub App kan leggast til på `bypass_actors`-lista i ruleset

#### Steg:

- [ ] **A1:** Opprett ein GitHub App i organisasjonen (Settings → Developer settings → GitHub Apps → New GitHub App)
  - Namn: t.d. `linkml-datamodellering-no Release Bot`
  - Permissions:
    - Repository permissions:
      - Contents: Read and write
      - Pull requests: Read and write
      - Issues: Read and write (for release-please comments)
      - Metadata: Read-only (automatisk)
  - Disable webhook (ikkje nødvendig for denne bruken)
  - Installer app-en på `brreg/linkml-datamodellering-no`

- [ ] **A2:** Generer ein privat nøkkel for app-en (lagre trygt, treng den i A3)

- [ ] **A3:** Legg til app-credentials som repo-secrets:
  - `APP_ID`: App ID frå GitHub App-sida
  - `APP_PRIVATE_KEY`: Innhaldet av .pem-fila generert i A2

- [ ] **A4:** Legg GitHub App til på bypass-lista i branch protection ruleset
  ```bash
  # Hent app integration-id
  gh api /orgs/brreg/installations -q '.[] | select(.app_slug=="linkml-datamodellering-no-release-bot") | .app_id'
  
  # Legg til som bypass_actor på ruleset
  gh api -X PUT repos/brreg/linkml-datamodellering-no/rulesets/16642329 \
    --field bypass_actors[]='{"actor_id": <APP_ID>, "actor_type": "Integration", "bypass_mode": "always"}'
  ```

- [ ] **A5:** Bruk `actions/create-github-app-token` i `release-please.yml` for å generere token:
  ```yaml
  - uses: actions/create-github-app-token@v1
    id: app-token
    with:
      app-id: ${{ secrets.APP_ID }}
      private-key: ${{ secrets.APP_PRIVATE_KEY }}
  
  - uses: googleapis/release-please-action@v5
    with:
      token: ${{ steps.app-token.outputs.token }}
  ```

- [ ] **A6:** Erstatt alle `${{ secrets.RELEASE_PLEASE_TOKEN }}` med `${{ steps.app-token.outputs.token }}` i workflow-fila

- [ ] **A7:** Test ved å trigger ein release (push conventional commit til main)

---

### Alternativ B: GITHUB_TOKEN med ruleset-unntak (enklare, men mindre fleksibel)

Bruk standard `GITHUB_TOKEN`, men juster branch protection til å tillate `github-actions[bot]` å pushe direkte.

**Problem:** GitHub støttar ikkje `github-actions[bot]` som bypass_actor direkte (sjå `specs/done/auto-merge-release-pr.md` linje 67-73). Dette alternativet krev ein workaround.

#### Steg:

- [ ] **B1:** Endre ruleset til å tillate direkte push utan PR for `github-actions[bot]` (ikkje mogleg direkte, sjå problem over)

**Konklusjon:** Dette alternativet er **ikkje gjennomførbart** med dagens GitHub-funksjonalitet.

---

### Alternativ C: Manually triggered release workflow ✅

Gjer release-prosessen manuell — ein workflow som kan triggerast via `workflow_dispatch` av ein admin.

#### Steg:

- ✅ **C1:** Endre `release-please.yml` til å vere `workflow_dispatch` i staden for `on: push`
  - Lagt til `workflow_dispatch` (utan inputs — versjonering følgjer Conventional Commits automatisk)
  - Fjerna `on: push: branches: [main]`

- ✅ **C2:** Bruk standard `GITHUB_TOKEN` (treng ikkje PAT sidan workflow er godkjent manuelt)
  - Erstatta alle `${{ secrets.RELEASE_PLEASE_TOKEN }}` med `${{ secrets.GITHUB_TOKEN }}`
  - Oppdatert kommentarar til å reflektere manuell prosess
  - Fjerna auto-merge-steg (admin mergar PR manuelt)

- ✅ **C3:** Dokumenter i `CONTRIBUTING.md` korleis ein utløyser ein release:
  - Lagt til "Korleis utløyse ein release"-seksjon med 9 steg
  - Forklart at versjonering følgjer Conventional Commits automatisk (fix/feat/BREAKING)
  - Dokumentert at admin må godkjenne og merge PR manuelt

**Bugfix (2026-07-01):** Fjerna ugyldig `release-type` parameter frå `googleapis/release-please-action@v5` — versjonering vert automatisk bestemt frå Conventional Commits, ikkje som workflow-input.

**Fordel:** Ingen PAT/App nødvendig, enklare oppsett

**Ulempe:** Ikkje automatisk — krev manuell triggering og godkjenning

**Utført:** Alternativ C er no implementert og dokumentert.

---

## Anbefaling

**Alternativ A (GitHub App)** er den beste langsiktige løysinga:
- Ingen avhengighet av personlege token
- Fullt automatisert
- Betre sikkerheit og auditerbarheit
- Standard praksis i mange open source-prosjekt (t.d. Semantic Release)

**Alternativ C (manuell workflow)** er no **implementert** som kortsiktig løysing:
- Fungerer utan PAT/App
- Krev manuell triggering og godkjenning av admin
- Akseptabelt dersom release-kadensen er låg (t.d. ukentleg/månadleg)
- Kan oppgraderast til Alternativ A seinare ved behov

---

## Avhengigheiter

- Tilgang til GitHub organisasjonsinnstillingar for å opprette GitHub App (A)
- Repo-admin-tilgang for å oppdatere ruleset (A4)

---

## Referansar

- [actions/create-github-app-token](https://github.com/actions/create-github-app-token)
- [GitHub Apps documentation](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps)
- [Branch protection bypass actors](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets#using-bypass-actors)
