# CI-workflow-optimalisering — fjern dobbeltarbeid, unødvendig arbeid og reduser køyretid

## Bakgrunn

Full gjennomgang av alle 8 workflow-filer i `.github/workflows/`
(`generate.yml`, `validate.yml`, `release.yml`, `release-please.yml`,
`reusable-generate.yml`, `reusable-validate.yml`, `trivy.yml`,
`auto-approve-release-please.yml`), kryssjekka mot dei `make`-måla dei
kallar (`make/20-domain-targets.mk`, `make/40-validation.mk`,
`make/80-images.mk`) og `src/assets/containers/images.json`.

`specs/done/dry-opprydding.md` gjorde alt eitt gjennombrot her (A1/A2):
domenelista og image-metadata i `generate.yml` vart gjort datadrivne
(`make print-domains`, `images.json`). Den spec-en flagga eksplisitt éi
attståande oppfølging: *"`validate.yml` har ei mindre, analog duplisering
... krev ein delt composite action ... naturleg oppfølging"*. Denne
spec-en tek opp den tråden, og utvidar gjennomgangen til køyretid og
reint unødvendig arbeid — ikkje berre kodeduplikasjon.

**Mål:** Redusere talet på gonger identisk arbeid (validering,
image-bygging, container-oppsett) vert utført for same commit/endring,
fjerne CI-arbeid som køyrer breiare/oftare enn naudsynt, og leggje til dei
kansellerings-/cache-mekanismane som manglar — utan å svekkje
robustheita workflowane har i dag (retries, `fail-fast: false`,
GHCR-cache).

## Metode

Kvart funn under er verifisert ved å lese heile kjeldefila (ikkje berre
grep-treff) og kryssjekke mot faktisk `make`-åtferd (t.d. stadfesta at
`make domain-<x>` ikkje sjølv validerer, sidan `20-domain-targets.mk` sin
`domain_target`-makro berre inneheld generator-kall). `grep -rn
"concurrency" .github/workflows/*.yml` stadfesta null treff i heile
repoet.

## Funn

### A. Ekte dobbeltarbeid (identisk berekning utført to gonger for same endring)

| # | Stad | Problem | Kostnad |
|---|---|---|---|
| A1 | **Alle 8 workflow-filer** | Ingen bruker `concurrency:`. `generate.yml` sin eigen toppkommentar dokumenterer alt eit kjent race mot `release-please.yml` sin versjons-oppdateringsjobb: *"denne workflowen kan derfor køyre to gonger per release (éin gong på data frå før update-dates, éin gong korrigert)"* — heile generate+build+publish-pipelinen (7 image, N domene, docs-bygg, Pages-deploy) køyrer to gonger for éin logisk release. Same problem gjeld `validate.yml`: kvar ny push til ein open PR startar ein heilt ny full valideringspipeline (image-bygg + N domene-matrise) utan å kansellere den føregåande, sjølv om berre siste push er relevant for merge-avgjerda. | **Størst funn i denne gjennomgangen** — kan doble total CI-tid ved rask iterasjon på ein PR, og garantert doblar han for kvar release |
| A2 | `generate.yml` steget *"Valider alle skjema for ${{ matrix.domain }}"* (linje ~290-308) | **Revidert etter diskusjon (sjå under):** Dette er **ikkje** reint dobbeltarbeid. `release-please.yml` sitt steg *"Oppdater schema-versjonar i release-PR"* skriv `version`/`endringsdato`/`utgivelsesdato` direkte inn i skjemaet og pushar denne endringa til PR-branchen med `[skip ci]` — det inneber at **denne konkrete, endra skjema-tilstanden vert aldri validert av `validate.yml` før merge**. `generate.yml` sitt valideringssteg er difor den einaste kontrollen som nokon gong køyrer mot det faktiske innhaldet som vert publisert. Det reelle problemet er at steget **svelgjer feilkoden** (`\|\| { echo "::warning::...held fram" }`) — det validerer, men gatar ingenting, sjølv om det er siste forsvarslinje mot version-bump-gapet | Steget kostar validerings-runtime som i dag, men gjev **null vern** mot feil i det versjonsoppdaterte innhaldet, sidan feil berre vert logga som åtvaring |
| A3 | `release.yml`, jobbane `mcp-linkml-validator`, `mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast` | Byggjer imaget **frå scratch** med `podman build` utan først å sjekke om det hash-tagga imaget alt finst i GHCR. `mcp-linkml-validator` er derimot alt bygd og pusha (hash-tagga) av **både** `generate.yml` og `validate.yml` sine `ensure-images`-jobbar for same commit. `linkml-local`-jobben i **same fil** har alt riktig mønster (`podman pull HASH_TAG \|\| podman build`) — dei tre andre jobbane manglar berre kopien av det mønsteret | Full `podman build` (inkl. `pip install` av `requirements.txt`) for eit image som statistisk sett alt eksisterer i GHCR |

### B. Duplisert YAML/logikk (vedlikehaldsrisiko / drift, jf. CLAUDE.md sin DRY-regel)

| # | Stad | Duplisert | Merknad |
|---|---|---|---|
| B1 | `generate.yml` (×3: `ensure-images`, `generate`, `publish`), `validate.yml` (×2: `commitlint`, `ensure-images`), `release.yml` (×4: éin per jobb) | *"Oppgrader crun til støtte for OCI v1-image"* — identisk 6-linjers `wget`+`chmod`+`mv`-blokk, kopiert **9 gonger** på tvers av 3 filer | Rein vedlikehaldsduplikasjon i dag (same versjon `1.18.2` alle stader), men risikoen er den same klassen feil som `avro`/`xsd`-bugen i `dry-opprydding.md`: neste versjonsoppdatering må råke alle 9 kopiane, elles driv dei frå kvarandre umerkt |
| B2 | `generate.yml` og `validate.yml` sine `checkout-source`-jobbar | Nesten identisk domeneoppdaging (`make print-domains` → JSON + space-separert liste → `upload-artifact`) | Alt flagga i `dry-opprydding.md` som attståande — "krev full samanslåing ein delt composite action ... naturleg oppfølging" |
| B3 | `generate.yml` og `validate.yml` sine `ensure-images`-jobbar | Identisk GHCR-eksistenssjekk-mønster (`skopeo inspect --format='exists'`) og bygg/push-steg, skrive ut for hand i begge filer | Same rotårsak som B2 |
| B4 | `validate.yml` sin `ensure-images`-matrise (linje 117-127) | **Framleis hardkoda** (2 image, `name`/`dockerfile`/`make_target`/`hash_files` skrive direkte i YAML), i motsetnad til `generate.yml` som vart gjort datadriven via `images.json` i `dry-opprydding.md` steg A2 | Stadfesta drift-risiko: eit nytt image lagt til `images.json` for valideringsflyten ville ikkje automatisk dukke opp her — nøyaktig same feilklasse som `avrotize`/`xsd`-bugen som alt vart funne og fiksa i `generate.yml` |
| B5 | `reusable-generate.yml` (for eksterne repo som kallar denne workflowen) | Reimplementerer generator-kommandoane (`gen-jsonld-context`, `gen-shacl`, `gen-owl`, osv.) direkte med `podman run linkml-local:latest <cmd>`, i staden for å kalle dei same `make gen-*`-måla som `make/11-generator-targets.mk` alt definerer for lokal bruk og intern CI | To separate implementasjonar av "korleis generere artefakt X" — driv frå kvarandre viss t.d. `OWL_DEFAULT_FLAGS` endrar seg internt utan at `reusable-generate.yml` vert oppdatert tilsvarande |

### C. Unødvendig arbeid (køyrer breiare/oftare enn naudsynt)

| # | Stad | Problem |
|---|---|---|
| C1 | `trivy.yml`, `on: push: branches: [main]` | **Ingen `paths:`-filter.** Kvar einaste push til main (README, `specs/`, `mkdocs/docs/`, CI-YAML — alt) utløyser 4 separate Trivy-fs-scans + 1 full SBOM-scan, sjølv om ingen av dei skanna filene (`Dockerfile*`, `requirements*.txt`) endra seg. Den vekevise cronen (`0 6 * * 2`) dekkjer alt periodisk skanning uavhengig av push-innhald |
| C2 | `trivy.yml`, jobben `scan-requirements` | 4 separate `aquasecurity/trivy-action`-steg, eitt per `requirements.txt`-fil, kvar med eiga sårbarheits-DB-oppslag/oppdatering. `generate-sbom`-jobben i **same fil** viser alt at éin `scan-ref: .`-skanning dekkjer heile repoet i eitt steg |
| C3 | `generate.yml`, jobben `generate`, steget *"Oppgrader crun"* (linje 197-204) | Manglar `if: steps.cache-generated.outputs.cache-hit != 'true'` som resten av jobben sine steg har (t.d. GHCR-innlogging rett under, linje 213-215). Køyrer alltid — også når heile resten av jobben hoppar over pga. cache-treff |

## Målbilete

- **Kansellering av supersedde køyringar** (`concurrency:` + `cancel-in-progress: true`) på `validate.yml` (pull_request) og `generate.yml` (push), slik at berre siste relevante commit sin pipeline fullfører. `release-please.yml` og `release.yml` får ei kø-basert `concurrency:`-gruppe **utan** kansellering (dei gjer mutasjonar — git-tags, releases — som ikkje er trygge å avbryte midtvegs).
- **`validate.yml` og `generate.yml` sine valideringssteg skal begge stå ved lag**, sidan dei dekkjer ulikt innhald: `validate.yml` gatar det som vert føreslått merga; `generate.yml` er einaste kontrollen mot innhaldet **etter** release-please sin `[skip ci]`-versjonsbump. `generate.yml` sitt steg skal derimot gjerast om til eit **ekte gate** (feile bygget ved reell valideringsfeil) i staden for å svelgje feilkoden og berre logge ei åtvaring.
- **Alle image-bygg i `release.yml` følgjer same "pull-by-hash, fallback-to-build"-mønster** som `linkml-local`-jobben alt har.
- **Éin autoritativ kjelde for crun-versjon, domeneoppdaging og GHCR-biletlogikk** — via composite actions i `.github/actions/`, brukt av alle 3 filer som treng dei.
- **`validate.yml` sin image-matrise hentar frå `images.json`**, ikkje hardkoda inline.
- **Trivy køyrer berre når relevante filer endrar seg** (push-trigger), pluss uendra vekentleg full-scan som sikkerheitsnett.
- **Ingen regresjon**: `fail-fast: false`, GHCR-cache-nøklar, og eksisterande retry-logikk (Pages-deploy) skal fungere identisk som før.

## Steg

1. **Legg til `concurrency:` på `validate.yml`** (høgast verdi, lågast risiko):
   ```yaml
   concurrency:
     group: validate-${{ github.event.pull_request.number || github.ref }}
     cancel-in-progress: true
   ```
   Verifiser at `create-pr-with-validation-logs`-jobben (som berre køyrer på
   `schedule`/`workflow_dispatch`, ikkje `pull_request`) ikkje vert kansellert
   utilsikta av ein samstundes PR-validering — bruk ulik `group`-nøkkel per
   event-type om naudsynt (t.d. inkluder `github.event_name` i gruppa).

2. **Legg til `concurrency:` på `generate.yml`**:
   ```yaml
   concurrency:
     group: generate-${{ github.ref }}
     cancel-in-progress: true
   ```
   Dette løyser direkte race-vilkåret dokumentert i fila sin eigen
   toppkommentar (linje 3-5) — når release-please sin versjonsbump-merge
   trigger eit nytt `generate.yml`-løp rett etter utviklaren sitt opphavlege
   push, vert det fyrste (utdaterte) løpet kansellert automatisk i staden
   for å fullføre unødvendig. **Oppdater toppkommentaren** til å skildre den
   nye åtferda i staden for å beskrive han som "kjent, akseptert".

3. **Legg til `concurrency:` (utan kansellering) på `release-please.yml`**
   for å hindre at to samstundes-triggerte køyringar (t.d. manuell
   `workflow_dispatch` midt i eit automatisk push-triggera løp) skriv til
   same manifest-fil samstundes:
   ```yaml
   concurrency:
     group: release-please
   ```

4. **Gjer valideringssteget i `generate.yml` til eit ekte gate** (revidert
   etter avklaring — steget skal **ikkje** fjernast, sidan det er einaste
   kontrollen mot skjema-innhaldet etter release-please sin
   `[skip ci]`-versjonsbump, som `validate.yml` aldri validerer):
   - Fjern feilsvelginga: steget *"Valider alle skjema for
     ${{ matrix.domain }}"* (linje ~290-308) skal la
     `run-validation.sh --manifest`-feil **stoppe bygget**, ikkje berre
     logge `::warning::`. Fjern `\|\| { echo "::warning::...held fram" }`-
     mønsteret og la exit-koden forplante seg (`set -euo pipefail` er alt
     sett i steget).
   - Vurder samstundes om `generate.yml` sin `publish`-jobb (Pages-deploy)
     bør ha ein eksplisitt `needs`-kjede-sjekk som gjer det tydeleg at
     publisering stoppar dersom valideringssteget feilar for **eitt**
     domene i matrisa (`fail-fast: false` gjer at andre domene framleis
     fullfører — avklar om det er ønska åtferd, eller om éin feila
     domene-validering bør stoppe heile `publish`-jobben).
   - **Behald** *"Kopier valideringsloggar til generated/"*-steget uendra
     (kopierer allereie eksisterande committa loggar for docs-visning —
     urelatert til dette gate-spørsmålet).
   - Legg gjerne til ein kommentar i steget som forklarer **kvifor** det
     framleis køyrer sjølv om `validate.yml` alt validerte same PR
     (peik til release-please sitt `[skip ci]`-versjonsbump-steg), slik at
     ein framtidig lesar ikkje mistolkar det som ubrukt dobbeltarbeid og
     fjernar det utan denne konteksten.

5. **Fiks `release.yml` sine 3 image-jobbar (A3)** til å følgje
   `linkml-local`-jobben sitt mønster:
   ```bash
   HASH_TAG="ghcr.io/${{ github.repository_owner }}/mcp-linkml-validator:${{ hashFiles('src/mcp-linkml-validator/Dockerfile', 'src/mcp-linkml-validator/requirements.txt') }}"
   if ! podman pull "$HASH_TAG" 2>/dev/null; then
     podman build -t localhost/mcp-linkml-validator:latest src/mcp-linkml-validator
     podman tag localhost/mcp-linkml-validator:latest "$HASH_TAG"
     podman push "$HASH_TAG"
   fi
   podman tag "$HASH_TAG" "ghcr.io/${{ github.repository_owner }}/mcp-linkml-validator:${{ github.ref_name }}"
   # osv. same som linkml-local
   ```
   Gjeld berre `mcp-linkml-validator` (finst i `images.json`, bygd av CI
   alt). `mcp-linkml-modell-utkast` og `mcp-linkml-begrep-utkast` er
   **ikkje** i `images.json` og vert aldri bygd før release — for desse er
   det ingen dobbeltarbeid å fjerne, la dei stå som i dag.

6. **Opprett composite action `.github/actions/upgrade-crun/action.yml`**
   (B1) som kapslar inn dei 9 identiske crun-oppgraderingsblokkene.
   Erstatt alle 9 kallstadene med `- uses: ./.github/actions/upgrade-crun`.
   Éin `CRUN_VERSION`-konstant framover.

7. **Opprett composite action `.github/actions/discover-domains/action.yml`**
   (B2) som kapslar inn `make print-domains` → JSON + space-separert
   output. Bruk han i begge `checkout-source`-jobbane i `generate.yml` og
   `validate.yml`.

8. **Opprett composite action `.github/actions/ensure-image/action.yml`**
   (B3+B4) som tek `name`/`dockerfile`/`make_target`/`hash_files` som
   input og kapslar inn: GHCR-eksistenssjekk (skopeo) → bygg om
   manglande → push. Bruk han frå:
   - `generate.yml` sin `ensure-images`-matrise (les framleis frå
     `images.json`)
   - `validate.yml` sin `ensure-images`-matrise — **og** migrer samstundes
     matrisa til å lese frå `images.json` i staden for hardkoda YAML
     (løyser B4 heilt, fullfører oppfølginga frå `dry-opprydding.md`)

9. **Legg til `if: steps.cache-generated.outputs.cache-hit != 'true'`** på
   *"Oppgrader crun"*-steget i `generate.yml` sin `generate`-jobb (C3) —
   éin linje, ingen åtferdsendring utanom å hoppe over ved cache-treff.

10. **Legg til `paths:`-filter på `trivy.yml` sin push-trigger** (C1):
    ```yaml
    on:
      push:
        branches: [main]
        paths:
          - 'src/**/Dockerfile*'
          - 'src/**/requirements*.txt'
          - 'src/assets/containers/**'
      schedule:
        - cron: '0 6 * * 2'
    ```
    Juster mønstra til faktisk å dekkje alle 4 skanna filer pluss
    Dockerfile-endringar som kan påverke SBOM-et.

11. **Konsolider `trivy.yml` sin `scan-requirements`-jobb til éin
    `scan-ref: .`-skanning** (C2), same mønster som `generate-sbom`-jobben
    alt bruker. Bruk `category:`-feltet på éin samla SARIF-upload i staden
    for 4 separate, eller behald 4 kategoriar men generer dei frå éin
    skanning viss `trivy-action` støttar det (undersøk om `--list-all-pkgs`
    + filtrering kan splitte resultatet post-hoc utan å tape granularitet —
    elles aksepter éin samla kategori som god nok).

12. **Vurder `reusable-generate.yml` sitt drift-potensial (B5)** — dette er
    ei eksternt kallande grensesnitt-fil (andre repo brukar han via
    `workflow_call`), så endring har breiare konsekvens. Foreslå (ikkje
    utfør utan eksplisitt godkjenning): la `reusable-generate.yml` kalle
    `make gen-<x> SCHEMA=...`-måla via `linkml-local`-containeren i staden
    for å reimplementere `podman run <cmd>` for kvar generator. Krev at
    `Makefile`/`make/` vert `git checkout`-a saman med skjemaet i det
    kallande repoet (sparse-checkout av `Makefile`, `make/`,
    `src/assets/scripts/`), analogt med korleis `reusable-validate.yml`
    alt gjer sparse-checkout av validator-komponentar frå dette repoet.

13. **Test og verifiser kvart steg isolert**, ikkje samla til slutt:
    - Steg 6-9 (composite actions, gating): valider YAML-syntaks lokalt
      (`python3 -c "import yaml; ..."`), test `ensure-image`-actionen
      manuelt mot minst to image (eitt eksisterande i GHCR, eitt som må
      byggjast) via `workflow_dispatch` på ein testgrein.
    - Steg 1-3 (`concurrency`): kan berre verifiserast reelt i GitHub
      Actions (push to fungerande PR/testgrein raskt etter kvarandre og
      stadfest at det fyrste løpet vert markert "Cancelled").
    - Steg 4 (ekte gate i generate.yml): på ein testgrein, introduser eit
      medvite ugyldig skjema (t.d. brot på ein bronze-policy-regel) og
      stadfest at `generate`-jobben faktisk feilar og `publish`-jobben
      ikkje køyrer for det domenet — deretter køyr ein normal
      PR→merge-syklus og stadfest at `generated/<domain>/validation/`
      framleis vert fylt korrekt for docs-visning når alt er gyldig
    - Steg 5 (release.yml): test med ein pre-release-tag (t.d.
      `v0.0.0-test`) på ein fork/testgrein, IKKJE på ekte
      `v*.*.*`-mønster mot hovudrepoet, for å unngå utilsikta ekte release.
    - Steg 10-11 (trivy): stadfest at SARIF-opplasting til Security-fana
      framleis fungerer med redusert steg-tal.

14. **Oppdater `specs/done/dry-opprydding.md`** med ei kort tilvising til
    denne spec-en når steg 7-8 er fullførte (dei fullfører den attståande
    oppfølginga fila alt peika på), i tråd med CLAUDE.md sin DRY-regel om
    kryssreferansar framfor duplisert forklaring.

15. **Når alle steg er fullførte:** generer commit-melding, legg til
    `## Utført`-seksjon, flytt denne spec-en til `specs/done/`.

## Rekkjefølgje og prioritet

Anbefalt rekkjefølgje etter verdi/risiko-forhold, ikkje etter
avhengigheit (stega er stort sett uavhengige):

1. **Høgast verdi, lågast risiko — gjer først:**
   - Steg 1-2 (`concurrency` på `validate.yml`/`generate.yml`) — løyser
     det klart største funnet, éin linje endring per fil, reint additivt
   - Steg 9 (crun-gating på cache-hit) — trivielt, null risiko
   - Steg 10 (trivy paths-filter) — trivielt, reduserer unødvendige
     køyringar direkte
   - Steg 5 (release.yml image-reuse) — mønsteret finst alt i same fil å
     kopiere frå
   - Steg 4 (gjer valideringssteget i generate.yml til eit ekte gate) —
     avklart med brukaren (sjå revidert steg 4), enkel fiks (fjern
     feilsvelging), men **valider åtferd nøye** før merge sidan det no
     kan stoppe publisering som før alltid gjekk gjennom
2. **Middels verdi, krev meir testing:**
   - Steg 3 (release-please concurrency)
   - Steg 11 (trivy-konsolidering) — krev å stadfeste at
     kategori-granularitet ikkje går tapt
   - Steg 6 (crun composite action) — rein refaktorering, låg risiko, men
     rører 3 filer
3. **Høgare kompleksitet, fleire jobbar involvert:**
   - Steg 7-8 (composite actions for domeneoppdaging/image-handtering) —
     fullfører `dry-opprydding.md` sin attståande A2-oppfølging, men
     involverer fleire jobbar/filer samstundes
4. **Utgreiande, ikkje nødvendigvis fiks no:**
   - Steg 12 (reusable-generate.yml) — ekstern grensesnitt-fil, foreslå
     berre, ikkje utfør utan eksplisitt godkjenning

## Akseptansekriterium

- [ ] `validate.yml` og `generate.yml` har `concurrency:`-blokker med
      `cancel-in-progress: true`; ein rask dobbel-push til same PR/branch
      kansellerer det fyrste løpet synleg i Actions-historikken
- [ ] `release-please.yml` har ei `concurrency:`-gruppe utan kansellering
- [ ] Valideringssteget i `generate.yml` er eit ekte gate (feilar bygget
      ved reell valideringsfeil), ikkje ei svelgd åtvaring — verifisert
      med eit medvite ugyldig testskjema på ein testgrein
      - [ ] Steget har ein kommentar som forklarer kvifor det framleis
            trengst sjølv om `validate.yml` alt validerte same PR
            (release-please sitt `[skip ci]`-versjonsbump-gap)
- [ ] Alle 4 image-byggjobbar i `release.yml` følgjer
      pull-by-hash-fallback-to-build-mønsteret der eit hash-tagga
      image alt kan finnast i GHCR (`linkml-local`, `mcp-linkml-validator`)
- [ ] Crun-oppgraderingslogikk finst berre éin stad
      (`.github/actions/upgrade-crun/`), brukt frå alle tidlegare 9 kallstader
- [ ] Domeneoppdagingslogikk finst berre éin stad, brukt av begge
      `checkout-source`-jobbane
- [ ] `validate.yml` sin `ensure-images`-matrise hentar frå `images.json`,
      ikkje hardkoda YAML
- [ ] `trivy.yml` sin push-trigger har `paths:`-filter; vekecronen er uendra
- [ ] `trivy.yml` sin `scan-requirements`-jobb har redusert talet på
      separate Trivy-invokasjonar (frå 4, helst til 1)
- [ ] Ingen regresjon: `fail-fast: false` på alle matriser er uendra,
      GHCR-cache-nøklar er identiske som før (ingen unødvendig
      cache-invalidering innført), Pages-deploy-retry fungerer som før
- [ ] Alle endra workflow-filer er `actionlint`-reine (CLAUDE.md-krav
      etter kvar CI-endring)

## Framdrift

**Steg 1, 2, 5, 9, 10 utført** (2026-08-04):

- **Steg 1 — `concurrency` på `validate.yml`:** Gruppe
  `validate-${{ github.event.pull_request.number || github.ref }}-${{ github.event_name }}`
  med `cancel-in-progress: true`. `github.event_name` er med i gruppa
  slik at nattleg schedule-køyring og PR-validering aldri kan kansellere
  kvarandre.
- **Steg 2 — `concurrency` på `generate.yml`:** Gruppe
  `generate-${{ github.ref }}` med `cancel-in-progress: true`.
  Toppkommentaren (linje 3-5) er oppdatert frå "kjent, akseptert race" til
  å skildre at `concurrency`-blokka no løyser det.
- **Steg 5 — `release.yml` sin `mcp-linkml-validator`-jobb:** Bytt frå
  ubetinga `podman build` til pull-by-hash-fallback-to-build, identisk
  mønster som `linkml-local`-jobben i same fil. `mcp-linkml-modell-utkast`
  og `mcp-linkml-begrep-utkast` er urørte (ikkje i `images.json`, ingen
  duplikat å fjerne — jf. spec-teksten over).
- **Steg 9 — crun-gating i `generate.yml`:** `"Cache genererte
  artefaktar"`-steget vart flytta **før** `"Oppgrader crun"`-steget (var
  omvendt rekkjefølgje før — `cache-generated`-outputen fanst ikkje endå
  då crun-steget køyrde), deretter fekk crun-steget
  `if: steps.cache-generated.outputs.cache-hit != 'true'`. Reint
  rekkjefølgje-bytte, ingen annan åtferdsendring.
- **Steg 10 — `trivy.yml` paths-filter:** Lagt til `paths:` på
  push-triggeren (`**/Dockerfile*`, `**/requirements*.txt`,
  `src/assets/containers/**`). Vekecronen (`0 6 * * 2`) er uendra og
  dekkjer framleis periodisk full skanning uavhengig av push-innhald.

**Verifisert:**
- Alle 4 endra filer parsar korrekt (`python3 -c "import yaml; ..."`)
- `actionlint` (via podman, `docker.io/rhysd/actionlint:latest`) køyrd mot
  alle 4 filer: **ingen** `[expression]`- eller schema-feil. Dei einaste
  funna er pre-eksisterande `[shellcheck]`-stilråd (SC2044/SC2086/SC2076/
  SC2199/SC2155/SC2162) på linjer som ikkje er del av denne økta sine
  endringar (stadfesta ved å lese linjenumra opp mot faktisk endra
  seksjonar) — desse er stilråd og treng ikkje rettast som del av denne
  endringa, jf. CLAUDE.md.
- **Ikkje verifisert:** faktisk køyring i GitHub Actions (kan ikkje
  testast lokalt). `concurrency`-kansellering (steg 1-2) og
  cache-hit-gating (steg 9) bør overvakast ved neste par pushar til main
  og neste par PR-oppdateringar for å stadfeste forventa åtferd (kansellert
  utdatert løp synleg i Actions-historikken, crun-steget hoppa over ved
  cache-treff).

**Attståande:** steg 3, 4, 6, 7, 8, 11, 12 (sjå "Rekkjefølgje og
prioritet" for tilrådd vidare rekkjefølgje).

## Relaterte filer

- `.github/workflows/generate.yml` — A1, A2, A3 (via `release.yml`), B1,
  B2, B3, C3
- `.github/workflows/validate.yml` — A1, B1, B2, B3, B4
- `.github/workflows/release.yml` — A3
- `.github/workflows/release-please.yml` — A1 (concurrency)
- `.github/workflows/trivy.yml` — C1, C2
- `.github/workflows/reusable-generate.yml` — B5
- `src/assets/containers/images.json` — kjelde for B4-fiksen
- `make/40-validation.mk` — stadfesta at `make domain-<x>` ikkje sjølv
  validerer (grunnlag for A2-analysen)
- `make/20-domain-targets.mk` — stadfesta domain_target-pipelinen sitt
  faktiske innhald (ingen validering inkludert)
- `specs/done/dry-opprydding.md` — opphavet til B2/B4-funna (attståande
  oppfølging derifrå), mønster-referanse for korleis A1/A2 der vart løyst
