# Plan: Standardisert CodeQL-workflow (advanced setup)

**Kortnamn:** `standardisert-codeql-workflow`
**Dato:** 2026-08-09

---

## Bakgrunn

GitHub sitt dynamiske **default setup** for code scanning
(`repos/{owner}/{repo}/code-scanning/default-setup`) er i dag aktivert for
`languages: actions, javascript, javascript-typescript, python, typescript`
med `query_suite: default`. Dette produserer to automatiske køyringar per
push til `main`: éin sikkerheits-CodeQL-analyse ("Push on main") og éin
separat "Code Quality"-analyse ("Code Quality: Push on main") — det siste er
eit eige GitHub-produkt som automatisk koplar seg på default setup for
støtta språk.

Default setup er ikkje styrt av ei fil i repoet, og kan difor ikkje
versjonskontrollerast, code-reviewast eller tilpassast (t.d. `paths-ignore`
for `mkdocs/node_modules/`).

**Mål:** Erstatte default setup med ein eksplisitt `.github/workflows/codeql.yml`
("advanced setup") som:
- Slår saman sikkerheit og kodekvalitet i éin køyring (`security-and-quality`
  query suite) — fjernar behovet for den separate automatiske
  Code Quality-køyringa
- Dekker faktisk kjeldekode i repoet: Python (`src/`, `tests/`,
  `mkdocs/lib/scripts/`), JavaScript (`mkdocs/docs/javascripts/`,
  `src/assets/scripts/container/`) og GitHub Actions
  (`.github/workflows/`, `.github/actions/`)
- Ekskluderer generert/tredjeparts-kode (`mkdocs/node_modules/`,
  `mkdocs/site/`, `generated/`)

## Avklarte val (sjå samtale 2026-08-09)

| Val | Avgjerd |
|---|---|
| Query suite | `security-and-quality` |
| Språk-matrise | `python`, `javascript-typescript`, `actions` (droppar redundante separate `javascript`/`typescript`) |
| Schedule | Vekentleg, måndag 02:00 UTC (matchar noverande default-setup-frekvens) |
| Triggers | `push` (main), `pull_request` (main), `schedule`, `workflow_dispatch` — matchar mønsteret i `validate.yml`/`generate.yml` |
| Default setup | Slåast av via `gh api` etter at workflow-fila er verifisert, for å unngå kollisjon/duplisering |

## Steg

1. Opprett `.github/workflows/codeql.yml` med matrise-jobb for
   `python`, `javascript-typescript`, `actions`, query suite
   `security-and-quality`, `paths-ignore` for `mkdocs/node_modules/` og
   `mkdocs/site/`
2. Køyr `actionlint` mot den nye fila (jf. CLAUDE.md § "Actionlint etter
   CI-endring")
3. Slå av GitHub default setup for code scanning via
   `gh api -X PATCH repos/{owner}/{repo}/code-scanning/default-setup -f state=not-configured`
   (reversibelt — kan slåast på att via Settings dersom noko går gale)
4. Verifiser at default setup faktisk er av
   (`gh api repos/{owner}/{repo}/code-scanning/default-setup`)
5. Generer commit-melding, marker spec utført, flytt til `specs/done/`

## Handlingsliste

- [x] `.github/workflows/codeql.yml` oppretta
- [x] `actionlint` køyrd reint mot fila
- [x] Default setup slått av (`state: not-configured`)
- [x] Verifisert via `gh api`
- [x] Commit-melding generert

## Utført

Alle steg utførte 2026-08-09. `.github/workflows/codeql.yml` erstattar
default setup fullt ut — matrise-jobb for `python`, `javascript-typescript`,
`actions` med `security-and-quality` query suite, `paths-ignore` for
`mkdocs/node_modules/`, `mkdocs/site/` og `generated/`. `actionlint` fann
ingen feil. Default setup verifisert slått av via
`gh api repos/{owner}/{repo}/code-scanning/default-setup` (`state:
not-configured`). Neste push til `main` vil trigge éin CodeQL-køyring
(matrise med 3 språk) i staden for to separate automatiske køyringar.
