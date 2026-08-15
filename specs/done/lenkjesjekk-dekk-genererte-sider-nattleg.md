# Lenkjesjekk skal dekkje genererte docs-sider og køyre nattleg

## Bakgrunn

`.github/workflows/lenkje-og-mermaid-sjekk.yml` sin `lenkjesjekk`-jobb køyrer
`lychee` mot `**/*.md` rett etter ein rein `actions/checkout` — han byggjer
**ikkje** `mkdocs/docs/` fyrst (ingen `make docs-publish`/`make docs-build`).
Sidan alle genererte per-domene-dokumentasjonssider
(`mkdocs/docs/ap-no/`, `referanse/`, `fint/`, `ngr/`, `oreg/`, `fair/`,
`samt/`, `modellkatalog/`, `begrepskatalog/`, samt `index.md` og
`arkitektur/valideringsregler.md`) står i `.gitignore`, finst dei ikkje i
den utsjekka arbeidskatalogen — `lychee` ser dei aldri. Jobben dekkjer i
praksis berre dei ~20 statisk versjonskontrollerte rettleiingssidene i
`mkdocs/docs/` pluss repo-rot-dokument (README.md, CONVENTIONS.md osv.).
Fleirtalet av det publiserte sidetreet (alle domene-/skjemasider,
klassedokumentasjon generert av gen-doc) har difor **null** ekstern
lenkjesjekk-dekning i dag.

Same gap gjeld motsett veg: `mkdocs` sin eigen build-tids
`validation.links` (i `mkdocs/mkdocs.yml`, køyrt via `make docs-build`)
fangar interne, brotne relative lenkjer i genererte sider (jf.
`specs/done/fiks-brotne-relative-lenkjer-mkdocs.md`), men sjekkar aldri om
**eksterne** URL-ar (data.norge.no, digdir.no, W3C-vokabular osv.) faktisk
svarar — det gjer berre `lychee`. Dei to mekanismane har difor
komplementær, men i dag begge ufullstendig anvendt, dekning.

I tillegg køyrer heile `lenkje-og-mermaid-sjekk.yml` i dag berre vekentleg
(`cron: '0 6 * * 1'`, kvar måndag), ikkje nattleg.

## Vedtak (avklart med brukar)

**1. Genereringskjelde:** Den nattlege jobben skal skaffe seg
`generated/`-innhaldet sitt via **full generering inline** — ikkje eit
kall til ein delt reusable *workflow*, og ikkje gjenbruk av artefakt frå
siste `generate.yml`-køyring. Grunngjeving: enklast å implementere, null
risiko for å påverke `generate.yml`, og unngår skjørleiken ved at
`generate.yml` berre triggerar på push til `main` (ikkje eige schedule)
kombinert med `retention-days: 1` på artefakta hans — ein stille natt utan
push ville elles gjort den nattlege jobben feile.

**2. Unngå drift (denne revisjonen):** Sjølve *steg-logikken* for
domenegenerering skal **ikkje** kopierast inn i
`lenkje-og-mermaid-sjekk.yml` som rå YAML-duplikat av `generate.yml`. I
staden vert dei delane som begge workflowane treng identisk trekte ut til
nye composite actions under `.github/actions/`, som begge workflowane
kallar. Dette hindrar at dei to workflowane driv frå kvarandre over tid
(t.d. at nokon rettar ein retry-bug eller legg til eit nytt
generator-flagg i `generate.yml` sitt inline steg, utan å oppdage at
`lenkje-og-mermaid-sjekk.yml` har ein separat, no utdatert kopi).

Som konkret føre-var-funn under denne vurderinga: `validate.yml` har **alt
i dag** ein nesten-identisk kopi av `generate.yml` sitt
image-tags-utrekningssteg (same `hashFiles()`-formlar for
linkml-local/python-pytest/mcp-linkml-validator, subtilt ulik filtrering av
`images`-output) — eit reelt, eksisterande driftseksempel av nett den typen
denne spesifikasjonen skal unngå å leggje til ein tredje kopi av.

## Nye composite actions

Alle under `.github/actions/<namn>/action.yml`, same struktur/stil som
eksisterande `discover-domains`, `pull-images`, `ensure-image`,
`upgrade-crun`.

| Action | Input | Output | Kjelde (eksisterande steg som vert flytta ut) |
|---|---|---|---|
| `ghcr-login` | `github-token` (required) | — | Duplisert 3× i `generate.yml`, 2× i `validate.yml` i dag (`echo "$TOKEN" \| podman login ghcr.io ...`) |
| `compute-image-tags` | — | `images` (full `images.json`-passthrough), `image_tags` (JSON-map, ALLE image sine hash-taggar) | `generate.yml` linje 58-81 ("Bygg image-tag-oppslag") |
| `detect-required-images` | `domain` (required) | `images` (JSON-array `{name, make_target}`, always_required ∪ `build.yaml`-flaggutløyste) | `generate.yml` linje 198-236 ("Detekter påkrevde images for domain") |
| `generate-domain` | `domain` (required) | — (sideeffekt: fyller `generated/<domain>/`) | `generate.yml` linje 358-393 (pre-flight-logg + retry×2-wrappa `make domain-<domain>`) |
| `merge-generated-artifacts` | `domain_list` (space-separert) | — (sideeffekt: fyller `generated/`) | `generate.yml` linje 433-446 ("Last ned alle genererte artefakter" + samanslåing) |

`compute-image-tags` sitt `image_tags`-output er ein **superset** —
inneheld alle 7 image, ikkje berre dei ein spesifikk kallar treng.
Kallarar som treng eit filtrert `images`-utval (t.d. `validate.yml` sitt
"berre always_required") gjer framleis sin eigen `jq`-filtrering av
`images`-outputen lokalt — det er eit ekte, ulikt behov per workflow, ikkje
duplisert logikk. Det som faktisk var i risiko for å drifte
(`hashFiles()`-formelen per image) er no éin kjelde.

`detect-required-images` og `generate-domain` er **ikkje** aktuelle å
gjenbruke i `validate.yml`, sidan validate-jobben aldri køyrer full
`make domain-X`-artefaktgenerering (berre skjema-/eksempel-/data-validering
— ein heilt annan operasjon).

## Steg

1. **Opprett composite actions** (sjå tabell over). Kvar action skal
   dokumentere formålet sitt i toppkommentaren, same stil som eksisterande
   actions.

2. **Refaktorer `generate.yml`** til å bruke dei nye actionane i staden
   for dei tilsvarande inline-stega:
   - `checkout-source`: `image-tags`-steget → `uses:
     ./.github/actions/compute-image-tags`
   - `ensure-images`- og `generate`-jobbane sine "Logg inn på GHCR"-steg →
     `uses: ./.github/actions/ghcr-login` med `github-token:
     ${{ secrets.GITHUB_TOKEN }}`
   - `generate`-jobben sitt "Detekter påkrevde images"-steg → `uses:
     ./.github/actions/detect-required-images` med `domain: ${{
     matrix.domain }}`
   - `generate`-jobben sitt "Generer alle artefakter"-steg → `uses:
     ./.github/actions/generate-domain` med `domain: ${{ matrix.domain }}`
   - `publish`-jobben sitt "Logg inn på GHCR" → `ghcr-login`-actionen;
     "Last ned alle genererte artefakter" + samanslåing → `uses:
     ./.github/actions/merge-generated-artifacts` med `domain_list: ${{
     needs.checkout-source.outputs.domain_list }}`
   - Åtferda skal vere **uendra** etter refaktoreringa (reint
     flytte-steg, ingen logikkendring) — verifiser med ei
     `workflow_dispatch`-køyring at `generate.yml` framleis fullfører og
     produserer identisk `generated/`-innhald.

3. **Endra schedule til nattleg** i `lenkje-og-mermaid-sjekk.yml` —
   `cron: '0 6 * * 1'` → `cron: '0 6 * * *'` (heile workflowen, alle tre
   jobbane køyrer på same trigger som i dag).

4. **Nye jobbar for domenegenerering** i `lenkje-og-mermaid-sjekk.yml`,
   no bygde utelukkande av dei delte actionane (ikkje kopiert YAML):
   - `checkout-source`: `./.github/actions/discover-domains` +
     `./.github/actions/compute-image-tags`. Last opp `source`-artefakt
     (`src/`, `mkdocs/`, `.github/`, `Makefile`, `make/`, `README.md`,
     `CODEOWNERS.md`, `retention-days: 1`).
   - `generate` (matrise over `needs.checkout-source.outputs.domains`):
     last ned `source`-artefakt, `./.github/actions/upgrade-crun`,
     `./.github/actions/ghcr-login`, `./.github/actions/detect-required-images`
     → `./.github/actions/pull-images` (fell automatisk tilbake til lokalt
     `make <target>`-bygg dersom GHCR-pull feilar — inga eiga
     `ensure-images`/push-til-GHCR-jobb trengst, sidan denne jobben berre
     les/genererer, aldri publiserer image), `./.github/actions/generate-domain`,
     last opp `generated-${{ matrix.domain }}`-artefakt
     (`retention-days: 1`).
   - **Ikkje** ta med `generate.yml` sitt "Valider alle skjema"-steg eller
     `actions/cache`-steget — dette er ei fokusert, engongs nattleg
     køyring for lenkjesjekk, ikkje ein publiseringspipeline;
     skjemavalidering er alt dekt av `validate.yml` ved kvar PR, og cache
     gjev mindre gevinst for ein jobb som køyrer éin gong i døgnet
     uansett.

5. **Utvid `lenkjesjekk`-jobben** til å byggje portalen før lenkjesjekken:
   - `needs: [checkout-source, generate]`
   - `./.github/actions/merge-generated-artifacts` med `domain_list: ${{
     needs.checkout-source.outputs.domain_list }}`.
   - `./.github/actions/ghcr-login`, deretter pull `mkdocs-local` +
     `python-pytest` via `./.github/actions/pull-images` (identisk mønster
     som nyleg innført i `generate.yml` sin `publish`-jobb, sjå
     `specs/done/parallell-image-pull-publish-jobb.md`).
   - Køyr `make docs-publish` (populerer `mkdocs/docs/**` — også
     `arkitektur/valideringsregler.md` som i dag manglar heilt frå
     lenkjesjekken sitt synsfelt) og deretter `make docs-build`. Fang
     `WARNING`/`ERROR`-linjer frå `make docs-build` sin output og skriv dei
     til `$GITHUB_STEP_SUMMARY` (ny synlegheit — i dag vert desse berre
     sett dersom nokon køyrer `make docs-build` lokalt eller les rålogg
     frå `generate.yml`).
   - Behald eksisterande `lychee`-steg **uendra** — det treng ikkje
     omskrivast: `'**/*.md'`-globen og `exclude_path` i `.github/lychee.toml`
     (`generated`, `mkdocs/site`) fangar automatisk opp dei no
     materialiserte `mkdocs/docs/**/*.md`-filene, sidan dei fysisk finst på
     disk i denne jobben sitt arbeidsområde etter `make docs-publish`.

6. **Permissions:** den nye `checkout-source`/`generate`-jobbrekkja treng
   berre `contents: read` (ingen `packages: write` — jobben pushar aldri
   nye image til GHCR, berre les/fell tilbake til lokalt bygg).

7. **Verifiser:**
   - `actionlint` mot alle endra/nye filer (CLAUDE.md-krav etter kvar
     workflow-endring): `podman run --rm -v "$(pwd)":/repo:ro -w /repo
     docker.io/rhysd/actionlint:latest -color .github/workflows/*.yml
     .github/actions/*/action.yml`
   - Manuell `workflow_dispatch`-køyring av **både** `generate.yml`
     (stadfest uendra åtferd etter refaktorering) **og**
     `lenkje-og-mermaid-sjekk.yml` (stadfest at heile kjeda — generering →
     docs-publish → docs-build → lychee — fullfører, og at rapporten i
     `$GITHUB_STEP_SUMMARY` no viser treff/ikkje-treff mot genererte
     sider; t.d. reproduser CONVENTIONS.md-typen feil mellombels for å
     stadfeste at lychee no faktisk ville fanga han).

## Valfritt, utvida scope (ikkje del av kjerneleveransen)

`validate.yml` sitt eksisterande, nesten-identiske `image-tags`-steg
(linje 96-125) kan også byggjast om til å bruke
`./.github/actions/compute-image-tags` (med lokal `jq`-filtrering av
`images`-outputen til `always_required` etterpå, sidan validate.yml sitt
behov der er reelt ulikt). Dette løyser den eksisterande
drift-situasjonen mellom `generate.yml` og `validate.yml` fullt ut, ikkje
berre mellom `generate.yml` og `lenkje-og-mermaid-sjekk.yml`. Låg risiko
(rein uttrekk-og-referer, ingen semantikkendring), men rører ein tredje,
i dag fungerande workflow som ikkje var del av den opphavelege
førespurnaden — teke med her som eit forslag, ikkje ei handling, inntil
brukar stadfestar.

## Ikkje i scope

- `mermaid-render`-jobben brukar alt `git ls-files -z -- '*.md'` (kun
  versjonskontrollerte filer) — uendra, sidan mermaid-blokker i praksis
  berre finst i statiske rettleiingssider (ER-diagram i genererte sider
  brukar PlantUML SVG, ikkje mermaid, jf. CLAUDE.md § PlantUML-diagram).
  Ingen kjend dekningsgap her.
- `mermaid-click-href-sjekk`-jobben crawlar alt den *publiserte*
  GitHub Pages-portalen direkte (løyser same
  generert-innhald-problemstilling på ein annan måte). Kan i prinsippet
  forenklast til å bruke den no lokalt bygde `mkdocs/site/` i staden for å
  crawle live-sida, men det er ei separat vurdering — ikkje del av denne
  spesifikasjonen.
- Ingen endring i `.github/lychee.toml` (eksisterande `exclude_path` er
  alt korrekt for den nye jobbstrukturen).
- `release.yml` sine 4 GHCR-login-førekomstar vert ikkje rørte — anna
  formål (releasepublisering), ikkje del av
  generate/validate/lenkjesjekk-familien denne spesifikasjonen gjeld.

## Handlingsliste

- [x] `.github/actions/ghcr-login/action.yml`: ny
- [x] `.github/actions/compute-image-tags/action.yml`: ny
- [x] `.github/actions/detect-required-images/action.yml`: ny
- [x] `.github/actions/generate-domain/action.yml`: ny
- [x] `.github/actions/merge-generated-artifacts/action.yml`: ny
- [x] `.github/workflows/generate.yml`: refaktorert til å bruke dei nye
      actionane (uendra åtferd)
- [x] `.github/workflows/lenkje-og-mermaid-sjekk.yml`: `cron` → nattleg
      (`0 6 * * *`); nye `checkout-source`/`generate`-jobbar bygde av dei
      delte actionane; `lenkjesjekk`-jobb utvida med
      merge-generated-artifacts → pull mkdocs-local/python-pytest →
      `make docs-publish` + `make docs-build` (WARNING/ERROR til step
      summary) før eksisterande lychee-steg
- [x] `actionlint` køyrt mot alle endra/nye workflow-filer, ingen
      `[expression]`-/schemafeil
- [ ] Manuell `workflow_dispatch`-verifisering av både `generate.yml` og
      `lenkje-og-mermaid-sjekk.yml` — **ikkje utført** (LLM har ikkje
      løyve til å pushe/triggre CI, sjå Utført-seksjonen)
- [x] Avklart med brukar om `validate.yml`-konsolideringa (sjå "Valfritt,
      utvida scope") skal takast med → ja, teken med (sjå Utført-seksjonen)

## Utført

- 5 nye composite actions oppretta under `.github/actions/`, kvar med
  toppkommentar som forklarer kva den erstattar og kvifor.
- `generate.yml` refaktorert: `checkout-source` sitt image-tags-steg,
  begge `ensure-images`/`generate`-jobbane sine GHCR-login-steg,
  `generate`-jobben sitt "Detekter påkrevde images"- og "Generer alle
  artefakter"-steg, og `publish`-jobben sitt GHCR-login +
  artefakt-samanslåingssteg peikar no alle til dei delte actionane. Rein
  flytte-refaktorering — ingen logikkendring.
- `validate.yml` refaktorert (brukar stadfesta å ta med det valfrie
  steget): `checkout-source` sitt image-tags-steg bruker no
  `compute-image-tags` + eit nytt, lite filtreringssteg
  (`image-tags-filtered`) som avgrensar til `always_required`-images
  lokalt via `jq` (job-outputen `images` peikar no til det filtrerte
  steget, `image_tags` til superset-steget). Begge GHCR-login-steg
  (`ensure-images`- og `validate`-jobben) peikar no til `ghcr-login`.
- `lenkje-og-mermaid-sjekk.yml`: `cron` endra til `0 6 * * *` (nattleg).
  To nye jobbar (`checkout-source`, `generate`) byggjer heile
  `generated/`-treet via dei delte actionane, sjølvstendig frå
  `generate.yml`. `lenkjesjekk`-jobben beheld sin **fulle**
  `actions/checkout` (ikkje `source`-artefakten frå `checkout-source`,
  som er avgrensa til domenegenererings-filsettet og ville mista
  lychee-dekning av `specs/`, `CONVENTIONS.md`, `GOVERNANCE.md` m.fl.),
  slår saman generert-artefakt, pullar `mkdocs-local`/`python-pytest`,
  køyrer `make docs-publish` + `make docs-build` med eksplisitt
  exit-code-handtering (skil mellom `docs-publish`-feil og
  `docs-build`-feil, skriv WARNING/ERROR-linjer til `$GITHUB_STEP_SUMMARY`
  uavhengig av utfall) — deretter uendra `lychee`-steg.
- **Verifisert:** alle 8 nye/endra filer er gyldig YAML (`python3 -c
  yaml.safe_load`). `actionlint` køyrt mot dei tre endra workflow-filene
  (`generate.yml`, `validate.yml`, `lenkje-og-mermaid-sjekk.yml`) — ingen
  `[expression]`-/schemafeil, berre `[shellcheck]`-stilråd (éin i ny kode
  retta: `exit $build_rc` → `exit "$build_rc"`, resten pre-eksisterande og
  urelaterte til denne endringa). Merk: `actionlint` lintar ikkje
  composite `action.yml`-filer direkte i dette repoet sitt oppsett (verken
  som CLI-argument eller via auto-discovery frå kallande workflow) — dei
  nye actionane er verifisert via manuell gjennomlesing + YAML-parse i
  staden.
- **Ikkje verifisert:** faktisk `workflow_dispatch`-køyring av nokon av dei
  tre workflowane. LLM har ikkje løyve til å committe/pushe (CLAUDE.md),
  og GitHub Actions krev at endringane er pusha til repoet før dei kan
  triggast. Brukar bør køyre `workflow_dispatch` på både `generate.yml`
  og `lenkje-og-mermaid-sjekk.yml` etter push, og stadfeste at
  `generate.yml` framleis produserer identisk `generated/`-innhald og at
  `lenkje-og-mermaid-sjekk.yml` fullfører heile kjeda (generering →
  docs-publish → docs-build → lychee).
