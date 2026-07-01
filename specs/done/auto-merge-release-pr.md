# Plan: Auto-merge av release-please-PR utan review/godkjenning

**Kortnamn:** `auto-merge-release-pr`
**Dato:** 2026-06-20

---

## Bakgrunn

`release-please.yml` (jobben `release-please`) brukar
`googleapis/release-please-action@v5` til å opprette ein automatisk PR mot
`main` med versjonsbump og changelog, basert på conventional commits.
I dag må denne PR-en (som alle andre PR-ar mot `main`) gjennom vanleg
branch-protection — review og godkjenning, jf. `GOVERNANCE.md`:

> Endringar krev review og godkjenning frå **repo-administrator** [for felles
> infrastruktur].

Bruker ønskjer at akkurat denne release-PR-en skal kunne merges automatisk,
**utan** at eit menneske må godkjenne den først.

**Viktig avgrensing:** Dette er ei endring i GitHub sine repo-/branch-
innstillingar (branch protection på `main`), **ikkje** i workflow-koden i
seg sjølv — `release.yml` og `release-please.yml` har i dag ingen interne
godkjenningstrinn (ingen `environment:`-blokk med required reviewers).
Godkjenningskravet kjem **utelukkande** frå branch protection-regelen på
`main`. Eg har ikkje `gh auth`-tilgang i dette sandkasse-miljøet og kan derfor
ikkje inspisere eller endre denne innstillinga utan at brukar autentiserer
(`! gh auth login`) eller utfører endringa sjølv i GitHub-grensesnittet.

**Sikkerheitsmerknad:** Å fjerne godkjenningskravet for release-PR-en betyr at
versjonsbump + changelog-endringar (og dermed alle nye Git-tags/releases) går
til `main` utan menneskelig kontroll. Risikoen er avgrensa — release-please
genererer berre `version:`-felt, `CHANGELOG.md` og dato-annotasjonar, ikkje
fritt redigerbart innhald — men det er framleis ei reell endring i
sikkerheitsposituren til repoet, og bør gjennomføras med eksplisitt
stadfesting frå brukar før utføring, ikkje berre fordi planen er skriven.

---

## AM0 — Avklar og verifiser nåværende branch protection-status ✓

**Utført:** Brukar autentiserte (`gh auth login`, konto `AudunVindenesEggeBR`,
`admin: true` på repoet). Repoet brukar **rulesets** (ikkje berre klassisk
branch protection) — ruleset `main protection` (id 16642329) på default branch,
med `required_approving_review_count: 1` og status-sjekk `validate`.
Eksisterande `bypass_actors`: `RepositoryRole id 5` (Admin), `bypass_mode: always`.
`allow_auto_merge` var `false` på repo-nivå (avdekt, fiksa i AM2).

Krev `gh auth login` (brukar må køyre dette sjølv, t.d. via `! gh auth login`
i denne sesjonen) eller eit `GH_TOKEN`-miljøvariabel med repo-admin-tilgang.

```bash
gh api repos/brreg/linkml-datamodellering-no/branches/main/protection
# evt. (nyare rulesets-API, dersom repoet brukar rulesets i staden for klassisk protection):
gh api repos/brreg/linkml-datamodellering-no/rulesets
```

Identifiser om repoet brukar **klassisk branch protection** (har feltet
`required_pull_request_reviews.bypass_pull_request_allowances`) eller
**rulesets** (har ein `bypass_actors`-liste). Mekanismen for AM1 avheng av kva
som er i bruk.

## AM1 — Legg release-please-boten til på bypass-lista for review-krav ✓

**Utført — men med ein heilt annan mekanisme enn planlagt.** Forsøk på å
leggje appen `github-actions` (Integration, app-id 15368) til
`bypass_actors` på ruleset-en vart **avvist** av GitHub:

```
422 Validation Failed: "Actor GitHub Actions integration must be part of
the ruleset source or owner organization"
```

`github-actions[bot]` er ein innebygd systemidentitet, ikkje ein installert
GitHub App — GitHub støtter **ikkje** å bypasse review for denne identiteten
direkte. Ruleset-en sin `bypass_actors`-liste er **uendra** frå AM0
(verifisert etter det avviste forsøket).

**Faktisk løysing:** Ein fine-grained PAT (`RELEASE_PLEASE_TOKEN`) frå
admin-kontoen (som allereie står på bypass-lista som `RepositoryRole id 5`)
er oppretta av brukar og lagra som repo-secret
(`gh secret set RELEASE_PLEASE_TOKEN`, kjørt av brukar sjølv slik at
token-verdien ikkje gikk via samtalen). `release-please.yml` brukar no denne
PAT-en i staden for `GITHUB_TOKEN`, slik at handlingane (PR-oppretting,
merge, direkte push) utføres «som» admin-kontoen og dermed faktisk bypassar
review-kravet.

## AM2 — Legg til auto-merge-steg i release-please.yml ✓

**Utført, med to avvik frå utkastet:**

1. `allow_auto_merge` var `false` på repo-nivå — aktivert via
   `gh api -X PATCH repos/.../linkml-datamodellering-no -f allow_auto_merge=true`.
2. Auto-merge-steget brukar `GH_TOKEN: ${{ secrets.RELEASE_PLEASE_TOKEN }}`
   (ikkje `GITHUB_TOKEN` som i utkastet) — nødvendig for at merge-handlinga
   faktisk bypassar review-kravet (sjå AM1).

I tillegg vart `googleapis/release-please-action@v5`-steget sjølv endra til
å bruke `RELEASE_PLEASE_TOKEN` (`with: token:`), **utover planen sitt
opphavlege omfang**: PR-ar oppretta med standard `GITHUB_TOKEN` utløyser
ikkje andre workflows (GitHub sin loop-prevention for å hindre uendelege
løkker), så `validate.yml` sin required status check ville aldri køyrt på
release-PR-en — og auto-merge ville aldri fullført, sidan den ventar på
grønn `validate`-sjekk.

**Bifunn fiksa i samme omgang (etter avtale med brukar):** Jobbane
`capture-validation` og `update-dates` i `release-please.yml` pusha direkte
til `main` med `GITHUB_TOKEN`, og var **allereie brotne** av samme
ruleset (stadfesta via `gh run view` på køyring 27878549460 —
`update-dates` feila med «GH013: Repository rule violations... Changes
must be made through a pull request»). Begge job-ane brukar no
`RELEASE_PLEASE_TOKEN` for `actions/checkout`, som løyser dette.

## AM3 — Oppdater GOVERNANCE.md og CONTRIBUTING.md ✓

**Utført — berre `GOVERNANCE.md`.** Unntaket lagt til rett etter
felles-infrastruktur-regelen. `CONTRIBUTING.md` vart **ikkje** endra — den
beskriv teknisk bidragsflyt for menneskelege bidragsytarar (PR-steg,
commit-format), og release-PR-en er ikkje noko ein bidragsytar sjølv opprettar
eller forhandlar om, så det fanst ikkje noko naturleg stad å nevne unntaket
der utan å duplisere GOVERNANCE.md.

## AM4 — Verifiser

1. Trigger ein test-release (t.d. ein `chore`-commit til `main` som
   release-please plukkar opp) og stadfest at PR-en opprettast med
   auto-merge aktivert og **ingen** godkjenning kravd
2. Stadfest at ein **vanleg** PR (ikkje frå release-please) framleis krev
   godkjenning som før — bypass-lista skal **ikkje** gjelde generelt

**Status: ikkje utført i denne omgangen** — krev at ein faktisk
release-PR opprettast og går gjennom heile løpet (neste push til `main`
med ein releasable conventional commit). Brukar bør stadfeste resultatet
ved neste faktiske release.

---

## Prioritert handlingsliste

| # | Tiltak | Krev | Avheng av |
|---|--------|------|-----------|
| 1 | AM0: Avklar branch protection-type og nåværende status | `gh auth login` av brukar | — |
| 2 | AM1: Legg `github-actions`-app til bypass-lista for review-krav | GitHub admin-tilgang (via `gh api`) | 1 |
| 3 | AM2: Auto-merge-steg i `release-please.yml` | «Allow auto-merge» aktivert på repoet | 1 |
| 4 | AM3: Dokumenter unntaket i `GOVERNANCE.md`/`CONTRIBUTING.md` | — | 2, 3 |
| 5 | AM4: Verifiser med ein faktisk test-release | — | 2, 3 |

## Avhengigheiter

- **Blokkerande:** Eg kan ikkje utføre AM0-AM2 utan at brukar autentiserer
  `gh` (`! gh auth login`) med ein konto som har admin-tilgang til repoet,
  sidan dette er GitHub-repoinnstillingar, ikkje filer i repoet
- AM2 krev at «Allow auto-merge» er aktivert på repo-nivå (separat frå
  branch protection — sjekkast i AM0)
- AM3 bør gjennomføras **etter** AM1-AM2 er faktisk verifisert i praksis,
  ikkje før, slik at dokumentasjonen reflekterer faktisk oppsett
- Eksplisitt brukarstadfesting krevst før AM1 utføres, sjølv om planen er
  skriven — dette er ei endring i repoet sin sikkerheitspostur, ikkje ein
  ordinær kodefiks

## Utført (2026-06-20)

AM0-AM3 er gjennomførte. **AM4 (verifisering) er utsett** — krev ein faktisk
release-PR gjennom heile løpet, som berre skjer ved neste push til `main`
med ein releasable conventional commit. Ingen syntetisk test vart utført,
sidan det ville krevd å skape ein reell PR/tag.

**Hovudavvik frå plan:**

- **AM1:** Mekanismen i utkastet (legg `github-actions`-appen til
  ruleset sin `bypass_actors`) blei **avvist av GitHub API**
  (422: «Actor GitHub Actions integration must be part of the ruleset
  source or owner organization»). Løyst i staden med ein fine-grained PAT
  (`RELEASE_PLEASE_TOKEN`) frå admin-kontoen, lagra som repo-secret av
  brukar sjølv. Ruleset sin `bypass_actors`-liste er **uendra** —
  ingen GitHub-sikkerheitsinnstilling vart faktisk svekka; i staden brukar
  workflowen ein admin-eigd PAT som allereie har bypass-rett.
- **AM2:** I tillegg til auto-merge-steget vart **token-kilden til
  `release-please-action`-steget sjølv** endra til `RELEASE_PLEASE_TOKEN`
  (ikkje del av opphavleg utkast) — nødvendig fordi GitHub sin
  loop-prevention hindrar `GITHUB_TOKEN`-genererte PR-ar frå å utløyse
  `validate.yml`, som elles ville blokkert auto-merge for alltid (status-
  sjekken ville aldri køyre).
- **Bifunn (fiksa etter avtale med brukar, utanfor opphavleg omfang):**
  `capture-validation`- og `update-dates`-jobbane i `release-please.yml`
  var **allereie brotne** av samme ruleset (direkte push til `main` med
  `GITHUB_TOKEN`, stadfesta via faktisk feilande køyring 27878549460).
  Begge bytt til `RELEASE_PLEASE_TOKEN`.
- **AM3:** Berre `GOVERNANCE.md` oppdatert — `CONTRIBUTING.md` vart vurdert
  og medvite **ikkje** endra (ingen naturleg stad for unntaket der utan
  duplisering, sjå AM3-notatet ovanfor).
