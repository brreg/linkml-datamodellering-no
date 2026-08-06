# Audit — inkonsistensar i make-laget (struktur, script, namngjeving)

## Bakgrunn

Brukaren bad om ein brei gjennomgang av `Makefile`, alle `make/*.mk`-modular
og shellscript/Python-script kalla derifrå, for å finne strukturelle og
kodemessige inkonsistensar — samt ei eksplisitt vurdering av om namngjevinga
på enkelte make-target er inkonsistent seg imellom.

Dette er ein *dokumenterande* audit — ingen rettingar er utførte i denne
omgangen. Kvart funn har eit forslag til retting som kan takast som eigne
tiltak seinare (anten samla eller punktvis).

## Metode

- Las heile `Makefile` og alle 12 filene i `make/*.mk` (00-settings → 90-tools)
  i sin heilheit.
- Kryssjekka kvart script-kall (`bash src/assets/scripts/...`,
  `python3 src/assets/scripts/...`) mot faktisk filplassering med `find`.
- Grep'a etter `make mcp-validate`, `make mcp-begrep-run` og liknande
  kommandonamn på tvers av heile repoet for å finne rest-referansar etter
  tidlegare omdøypingar (jf. `specs/done/mcp-target-navnekonvensjon.md`).
- Samanlikna target-namn på tvers av `make/60-mcp.mk` og `make/70-scaffolding.mk`
  for mønster i verb/substantiv-bruk, språk (norsk/engelsk) og suffiks-sett.
- Samanlikna `## `-hjelpetekst i `make/*.mk` (kjelda for `make help`) mot
  kva som faktisk er dokumentert i `COMMANDS.md`.

## Funn (ranga etter alvorsgrad)

### 1. `log-mcp-validate` / `log-validate-instance` kallar eit script som ikkje finst der (reell bug)

`make/40-validation.mk:184` og `:186` og `:197` kallar
`bash src/assets/scripts/run-validation.sh`. Denne fila finst **ikkje** —
scriptet vart flytta til `src/assets/scripts/ci/run-validation.sh` utan at
kallarane i `make/40-validation.mk` vart oppdaterte. Begge target feilar
difor alltid med "No such file or directory" i dag.

**Retting:** oppdater dei tre kalla i `make/40-validation.mk` til
`src/assets/scripts/ci/run-validation.sh`.

### 2. Stale kommandonamn etter `mcp-validate` → `mcp-linkml-validate`-omdøyping

`specs/done/mcp-target-navnekonvensjon.md` dokumenterer at target vart
omdøypt frå `mcp-validate` til `mcp-linkml-validate`, og at
`mkdocs/docs/`, `README.md` og `CONTRIBUTING.md` vart oppdaterte med sed.
Fleire andre stader vart aldri fanga opp av sveipet, og refererer framleis
til det gamle (ikkje-eksisterande) namnet — eller til `make mcp-begrep-run`,
som heller ikkje finst som target lenger (næraste ekvivalent i dag er
`make mcp-linkml-begrep-utkast-run`):

**Aktive dokument/instruksjonar (ikkje `specs/done/`, som er unntatt DRY-krav):**
- `CLAUDE.md:71` — eiga AI-instruksjon i seksjonen «Valider arbeidet ditt» viser `make mcp-validate ...`
- `bugs/instance-check-walk-skips-lists.md:23`
- `mkdocs/docs/index-md-struktur.md:167,192`
- `mkdocs/docs/ny-begrepsmodell.md:102` (`make mcp-begrep-run`)
- `mkdocs/docs/publisering-oversikt.md:117`
- `mkdocs/lib/sections/kom_i_gang.sh:126` — genererer feil kommando inn i portalsider ved kvar `docs-publish`
- `specs/backlog/dx-prof-linkml-modell.md:262,341` (aktiv backlog-spec, ikkje done)
- `specs/backlog/mcp-begrep-utkast-enkeltfil-generering.md:110` (`make mcp-begrep-run`)

**Script som ekkoar feil kommando til sluttbrukar ved scaffolding (høgast praktisk konsekvens):**
- `src/assets/scripts/scaffolding/new-model.sh:159`
- `src/assets/scripts/scaffolding/new-modellkatalog.sh:248`
- `src/assets/scripts/scaffolding/new-begrepssamling.sh:67,92,97` (inkl. `make mcp-begrep-run`)
- `src/assets/scripts/scaffolding/new-begrepskatalog.sh:124,145` (inkl. `make mcp-begrep-run`)

**README under `src/mcp-linkml-*/`:**
- `src/mcp-linkml-begrep-utkast/README.md:17,214`
- `src/mcp-linkml-modell-utkast/README.md:132,154`
- `src/mcp-linkml-validator/README.md:17-50` (fleire førekomstar)
- `src/mcp-linkml-validator/policies/README.md:42,295,297,301`

`COMMANDS.md` sjølv er korrekt (`mcp-linkml-validate` konsekvent brukt) —
det var altså denne fila sveipet trefte, men ikkje dei over.

**Retting:** sed-sveip `make mcp-validate` → `make mcp-linkml-validate` og
`make mcp-begrep-run` → `make mcp-linkml-begrep-utkast-run` over fillista
over (utanom `specs/done/`, som skal stå urørt).

### 3. `new-begrepskatalog` er ikkje ein alias, trass i dokumentasjonen

`make/70-scaffolding.mk:8` (filoverskrift) og `:32` (kommentar) og
åtvaringsteksten i target sjølv (`:34-35`) hevdar `new-begrepskatalog` er
ein **deprecated alias for `new-begrepssamling`**. I praksis kallar dei to
target heilt ulike script (`new-begrepskatalog.sh` vs
`new-begrepssamling.sh`) med ulikt tal påkravde parameter (`NAME` åleine
mot `DOMAIN`+`NAME`) og genererer strukturelt ulike skjema:
`new-begrepskatalog` lagar éi monolittisk `BegrepContainer`-skjemafil
direkte under `src/linkml/begrepskatalog/<namn>/`, medan
`new-begrepssamling` lagar ein `begrep/`-katalog med éin fil per begrep
under det valde domenet. Dette er to reelt ulike, sjølvstendig vedlikehaldne
implementasjonar — ikkje éin alias som peikar vidare til den andre. Dei to
script-a kan difor drive frå kvarandre over tid (DRY-risiko), og
åtvaringsteksten gjev brukaren eit feilaktig bilete av kva som skjer.

**Retting:** anten (a) oppdater kommentar/åtvaring til å skildre kva
`new-begrepskatalog` faktisk gjer og kvifor begge finst, eller (b) gjer
`new-begrepskatalog` til ein reell tynn alias/wrapper rundt
`new-begrepssamling.sh` slik dokumentasjonen hevdar.

### 4. `print_info`/`print_warning`/`print_error` i `make/03-output.mk` er daud kode

Ingen av dei tre makroane vert kalla nokon stad i `make/*.mk` eller
`Makefile` — einaste treff er sjølve definisjonen og omtale i
`make/README.md`. `print_info` (`:29`) refererer i tillegg `$(CLR_INFO)`,
som **aldri er definert** i `make/00-settings.mk` (som berre definerer
`CLR_SEP/HDR/STEP/OK/ERR/WARN/DBG/RST`) — makroen ville altså produsert
fargelaus output dersom han nokon gong vart kalla. Den faktiske
feil/status-logginga i heile make-laget går via `log_info`/`log_error`/
`log_debug` frå `LOG_FUNCTIONS` (bash-funksjonar, sjå `00-settings.mk`),
ikkje via desse tre Make-makroane. Berre `print_header` og `print_step` er
faktisk i bruk.

**Retting:** fjern `print_info`, `print_warning` og `print_error` frå
`make/03-output.mk` og tilhøyrande omtale i `make/README.md`, sidan
`LOG_FUNCTIONS` allereie dekkjer same behov og er den etablerte
konvensjonen (jf. `specs/done/ingen-stille-feil.md`).

### 5. Stray backup-fil i `make/`

`make/10-generator-macros.mk.bak` (17 KB) er ein etterlaten kopi frå
refaktoreringa dokumentert i `specs/done/forenkle-make-laget.md`. Han vert
ikkje inkludert av `Makefile` (som listar filer eksplisitt, ikkje via
wildcard), så han påverkar ikkje bygget — men han er reint spekulativt
"gammalt" innhald som ligg att i eit katalognamn (`make/`) der alle andre
filer er levande kjeldekode, og ein `grep`/`find make/*.mk` (t.d. i CI eller
tooling) vil plukke han opp med mindre han eksplisitt filtrerast vekk.

**Retting:** slett fila (historikken finst allereie i git).

### 6. Ingen konsekvent plassering for script kalla frå make-laget

Dei aller fleste script kalla frå `make/*.mk` ligg i
`src/assets/scripts/makefile/` (28 filer). To unntak bryt mønsteret utan
forklaring:

- `src/assets/scripts/validate-modelldcat.py` — kalla frå
  `make/30-instances.mk:77`, ligg direkte under `src/assets/scripts/`
  saman med frittståande verktøy (`bump-version.sh`, `list-tool-licenses.py`
  osv.) som ikkje er make-kall.
- `src/assets/scripts/ci/run-validation.sh` — kalla frå
  `make/40-validation.mk` (sjå funn 1), ligg i ein eigen `ci/`-katalog med
  berre denne eine fila.

Ingen dokumentasjon (`make/README.md`, `COMMANDS.md`, CLAUDE.md) forklarer
kva som skil «script i `makefile/`» frå «script utanfor». Det finst i dag
tre ulike plasseringar for make-kalla script (`makefile/`, `ci/`, laus i
`src/assets/scripts/`) med tilsynelatande tilfeldig fordeling.

**Retting:** flytt `validate-modelldcat.py` og `run-validation.sh` inn i
`src/assets/scripts/makefile/`, eller dokumenter eksplisitt kva som skil
kategoriane dersom skiljet er tilsikta (t.d. at `ci/` er meint for script
som også køyrer utanfor `make`, frå GitHub Actions direkte).

### 7. `make help` viser ikkje alle target som er dokumenterte i `COMMANDS.md`

`make help` grep'ar `## `-kommentarar direkte frå kjeldefilene på disk
(sjå `src/assets/scripts/makefile/help.sh`). Følgjande target manglar
`## `-hjelpetekst og er difor usynlege i `make help`, sjølv om dei fleste
av dei er dokumenterte i `COMMANDS.md`:

- `make/30-instances.mk`: `gen-informasjonsmodell-instance`,
  `gen-modellkatalog-instance`, `gen-begrepskatalog-instance`,
  `validate-informasjonsmodell-instance`, `validate-modellkatalog-instance`
- `make/60-mcp.mk`: alle `build-docker-mcp-*`, alle
  `mcp-linkml-{validate,modell-utkast,begrep-utkast}-{run,smoke,test,list-profiles}`
  sub-target, samt `mcp-linkml-modell-utkast` og `mcp-linkml-begrep-utkast`
  sjølve
- `make/70-scaffolding.mk`: `new-model`, `new-modellkatalog`,
  `new-begrepssamling`, `new-begrepskatalog`, `update-valid-scopes`
- `make/40-validation.mk`: `log-mcp-validate`, `log-validate-instance`

Dette gjer `make help` til ei ufullstendig kjelde for «kva kommandoar
finst», og skaper eit gap mot `COMMANDS.md` som *er* fullstendig (jf.
CLAUDE.md-krava om å bruke `COMMANDS.md`-dokumenterte target). Ein brukar
som berre køyrer `make help` vil ikkje oppdage over 20 gyldige target.

**Retting:** legg til `## `-hjelpetekst på target over som er meint for
direkte brukarkall (dei reint interne, t.d. `_mcp-validate-with-header`,
`_gource-render`, kan halde fram utan — dei har alt understrek-prefiks som
signaliserer «internt»).

## Namnekonsistens i make-target

Eksplisitt vurdering av om enkelte make-target-namn er inkonsistente seg
imellom, utover funna over:

1. **`new-model` er engelsk, søsken-target er norske.** `make/70-scaffolding.mk`
   sine fire scaffolding-target er `new-model`, `new-modellkatalog`,
   `new-begrepssamling`, `new-begrepskatalog`. Tre av fire nyttar norske
   domeneord (`modellkatalog`, `begrepssamling`, `begrepskatalog`) — berre
   `new-model` brukar det engelske «model» der «new-modell» eller
   «new-domenemodell» ville følgt mønsteret. (CLAUDE.md sitt krav om
   bokmål gjeld formelt berre YAML-modellering, ikkje make-target-namn —
   men det interne mønsteret i akkurat denne targetgruppa er tydeleg norsk,
   og brytet stikk seg ut.)

2. **`mcp-linkml-validate` (verb) vs. `mcp-linkml-modell-utkast`/
   `mcp-linkml-begrep-utkast` (substantiv-frase).** Dei tre MCP-serverane
   sine hovud-target følgjer ikkje same grammatiske mønster: `-validate` er
   eit verb, medan `-modell-utkast`/`-begrep-utkast` er substantiv. Dette
   heng òg saman med at katalog- og imagenamnet er `mcp-linkml-validator`
   (substantiv) medan make-targetet er `mcp-linkml-validate` (verb) — same
   inkonsekvens internt i namnet på éin og same komponent.

3. **Asymmetriske sub-target-suffiks per MCP-server.** Alle tre serverar
   har `-run` og `-smoke`, men berre `mcp-linkml-validate` og
   `mcp-linkml-modell-utkast` har `-test` (køyrer pytest/unittest);
   `mcp-linkml-begrep-utkast` manglar `-test` heilt, men har i staden ein
   eigen `-list-profiles` som dei to andre ikkje har noko ekvivalent til.
   Dette kan vere reelt (kanskje begrep-utkast ikkje har ei eiga testsuite
   å køyre via make), men er verdt å avklare eksplisitt — anten legg til
   `mcp-linkml-begrep-utkast-test` dersom testar finst men manglar
   make-inngang, eller dokumenter kvifor ho manglar.

4. **`log-mcp-validate`/`log-validate-instance` bryt verb-substantiv-mønsteret.**
   Nesten alle andre target følgjer `<verb>-<substantiv>`
   (`validate-instance`, `validate-data`, `gen-docs`, `gen-erdiagram`).
   `log-mcp-validate` og `log-validate-instance` er derimot
   `<substantiv>-<verb>-<substantiv>` — «log» først. Dei overlappar dessutan
   funksjonelt med `validate-capture` (alle tre skriv valideringsresultat
   til disk/logg), men nyttar tre ulike underliggande script
   (`ci/run-validation.sh` vs. `run-schema-validation.py` +
   `save-validation-log.py`). Verdt å vurdere om dette er tre reelt ulike
   behov, eller om det er modningsrestar frå tre separate iterasjonar av
   same funksjon som burde konsoliderast.

## Ikkje-funn (sjekka, men OK)

- `.PHONY`-dekning er stort sett god: generator- og domain-target
  sjølv-deklarerer `.PHONY` inne i `$(eval $(call ...))`-malen sin
  (`make/11-generator-targets.mk:12`, `make/20-domain-targets.mk:36`), medan
  eldre/manuelt skrivne target samlast i éi stor liste i `Makefile:58-71`.
  To ulike stader for same ting, men begge er fullstendige for sine
  respektive target — ikkje ein reell bug, berre eit strukturelt
  artefakt av at generator-target vart lagt til seinare.
- `check-prereqs.bash` og andre `makefile/`-script sine kall-stiar er
  konsistente elles.
- `CLR_WARN` (tidlegare udefinert, jf. funn 1 i
  `specs/done/logging-inkonsistens-audit.md`) er no retta og eksportert
  korrekt i `make/00-settings.mk`.

## Vedtekne tiltak (utført i denne økta)

Brukaren har vedteke fire konkrete tiltak frå funna over. Resten av funna
(4, 5, 7, namnekonsistens 3-4) står framleis som udokumenterte forslag i
handlingslista under.

1. **Funn 3, alternativ (a):** `new-begrepskatalog` vert **ikkje** gjort om
   til ein ekte alias. I staden vert filoverskrifta og inline-kommentaren/
   åtvaringa i `make/70-scaffolding.mk` oppdatert til å skildre kva
   `new-begrepskatalog` faktisk gjer (sjølvstendig legacy-script, ulik
   skjemastruktur, ulike påkravde parameter) og kvifor begge target held
   fram med å eksistere.
2. **Funn 6:** `validate-modelldcat.py` og `run-validation.sh` vert flytta
   til `src/assets/scripts/makefile/`, saman med alle referansar i
   `make/*.mk` og `.github/workflows/*.yml` (med påfølgjande `actionlint`,
   jf. CLAUDE.md-krav om lint etter CI-endring). Dette løyser samtidig
   funn 1 (den broten stien), sidan den nye stien vert korrekt frå start.
3. **Namnekonsistens 1:** `new-model` → `new-modell` (inkl. scaffolding-
   scriptet `new-model.sh` → `new-modell.sh`), for å følgje det norske
   mønsteret til søsken-targeta.
4. **Namnekonsistens 2:** `mcp-linkml-validate` → `mcp-linkml-valider-modell`,
   inkludert heile sub-target-familien (`-run`, `-smoke`, `-test`) og det
   interne `_mcp-validate-with-header` → `_mcp-valider-modell-with-header`.
   Alle attverande stale `mcp-validate`-referansar frå funn 2 (CLAUDE.md,
   `bugs/`, mkdocs-sider, scaffolding-script, `src/mcp-linkml-*/README.md`
   m.fl.) vert samtidig retta til det nye, korrekte namnet — å la dei
   framleis peike på eit ikkje-eksisterande namn ville vore verre enn før
   endringa. Den separate `mcp-begrep-run`-delen av funn 2 er **ikkje**
   omfatta av dette tiltaket og står att i handlingslista.

## Handlingsliste

- [x] Funn 1: løyst som del av funn 6 (ny sti er korrekt frå start)
- [x] Funn 2: `mcp-validate`-delen løyst av namnekonsistens 2; `mcp-begrep-run`-delen løyst i runde 2, sjå «Utført, runde 2»
- [x] Funn 3: løyst — alternativ (a), sjå «Vedtekne tiltak»
- [x] Funn 4: løyst i runde 2 — daud `print_info`/`print_warning`/`print_error`-kode fjerna
- [x] Funn 5: løyst i runde 2 — `make/10-generator-macros.mk.bak` sletta
- [x] Funn 6: løyst, sjå «Vedtekne tiltak»
- [x] Funn 7: løyst i runde 2 — manglande `## `-hjelpetekst lagt til, pluss ein relatert `help.sh`-bug retta undervegs
- [x] Namnekonsistens 1: løyst — `new-model` → `new-modell`
- [x] Namnekonsistens 2: løyst — `mcp-linkml-validate` → `mcp-linkml-valider-modell`
- [x] Namnekonsistens 3: avklart i runde 2 — inga testsuite finst for begrep-utkast, dokumentert i kode, ingen `-test`-target lagt til
- [x] Namnekonsistens 4: avklart i runde 2 — reelt ulike behov (CI-kritisk vs. manuelt release-verktøy), konsolidering medvite utsett, dokumentert i kode

## Utført

Alle fire vedtekne tiltak er gjennomførte.

**Funn 6 (og dermed funn 1) — flytting av script:**
- `git mv`-ekvivalent (vanleg `mv`, ikkje git-kommando) av
  `src/assets/scripts/validate-modelldcat.py` og
  `src/assets/scripts/ci/run-validation.sh` til
  `src/assets/scripts/makefile/`. Tom `ci/`-katalog sletta.
- Referansar oppdaterte i `make/30-instances.mk`, `make/40-validation.mk`
  (3 kall), `.github/workflows/generate.yml`,
  `.github/workflows/validate.yml`, samt `specs/backlog/validering-badge-inkonsistent.md`.
- `actionlint` køyrt mot begge endra workflow-filer — berre `[shellcheck]`-
  stilråd (ikkje-blokkerande per CLAUDE.md), ingen `[expression]`/syntaksfeil.

**Funn 3, alternativ (a) — `new-begrepskatalog`-dokumentasjon:**
- Filoverskrift og inline-kommentar i `make/70-scaffolding.mk` skriven om
  til å skildre at `new-begrepskatalog` er ein sjølvstendig legacy-
  implementasjon (monolittisk `BegrepContainer`-format, kun `NAME`-parameter),
  ikkje ein alias for `new-begrepssamling`. Verifisert at
  `src/linkml/begrepskatalog/brreg-begrepskatalog` faktisk nyttar dette
  formatet, som grunngjeving for kvifor targetet held fram. Den misvisande
  "deprecated"-åtvaringa i target-oppskrifta er fjerna.

**Namnekonsistens 1 — `new-model` → `new-modell`:**
- Target omdøypt i `make/70-scaffolding.mk`, `.PHONY`-lista i `Makefile`,
  kommentar i `make/60-mcp.mk`.
- Script omdøypt: `src/assets/scripts/scaffolding/new-model.sh` →
  `new-modell.sh`, internt bruk/feilmeldingstekst oppdatert (og ein
  eksisterande stikk-i-strid stipath i toppkommentaren retta i same slag).
- Alle referansar oppdaterte i `COMMANDS.md`, `CONVENTIONS.md`, `README.md`,
  `mkdocs/docs/{build-config,kommandoar,ny-domenemodell,ny-org,readme-tabellgenerering}.md`
  og den aktive `specs/backlog/rename-schema-til-linkml-yaml.md` (som òg
  hadde ein forelda sti utan `scaffolding/`-segmentet, retta i same slag).
- `specs/done/*` ikkje rørt (unntatt frå DRY-krav).

**Namnekonsistens 2 — `mcp-linkml-validate` → `mcp-linkml-valider-modell`:**
- Heile familien omdøypt: hovudtarget, `-run`/`-smoke`/`-test`, og det
  interne `_mcp-validate-with-header` → `_mcp-valider-modell-with-header`
  (`make/40-validation.mk`, `make/60-mcp.mk`, `.PHONY`-lista i `Makefile`,
  `make/README.md`).
- Alle attverande stale `mcp-validate`-referansar (funn 2, `mcp-validate`-
  delen) retta til det nye namnet: `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`,
  `COMMANDS.md`, to filer i `bugs/`, ni sider under `mkdocs/docs/`,
  `mkdocs/lib/sections/kom_i_gang.sh`, fire scaffolding-script,
  fire `src/mcp-linkml-*/README.md`/`policies/README.md`,
  `specs/backlog/dx-prof-linkml-modell.md`, `src/assets/scripts/makefile/run-schema-validation.py`,
  dei tre `referansemodell-{bronze,silver,gold}-schema.yaml`-filene, og
  `src/mcp-linkml-modell-utkast/profiles/{bronze,silver}.yaml`.
- **Kollisjon oppdaga og retta undervegs:** den separate targeten
  `log-mcp-validate` (ulik funksjon, ikkje omfatta av denne omdøypinga)
  vart ved ein feil delvis matcha av det første sed-sveipet i `COMMANDS.md`
  og `mkdocs/docs/kommandoar.md` (`log-mcp-validate` → feilaktig
  `log-mcp-linkml-valider-modell`). Oppdaga ved verifiseringssøk og reversert
  før avslutning.
- `mcp-begrep-run`-delen av funn 2 er **ikkje** rørt (ikkje del av det
  vedtekne tiltaket) — står att i handlingslista over.
- `.claude/settings.local.json` har nokre no-forelda permission-mønster
  (`Bash(make mcp-validate *)`, `Bash(make new-model *)`) — reint lokal
  Claude Code-verktøykonfig, ikkje ein del av kodebasen/make-laget, difor
  ikkje rørt.
- Verifisert: `make -n help`, `make -n mcp-linkml-valider-modell SCHEMA=...`
  og `make -n new-modell` løyser korrekt utan Makefile-parsefeil.

**Ikkje utført etter runde 1 (løyst i runde 2, sjå under):** funn 2
(`mcp-begrep-run`-delen), funn 4, funn 5, funn 7, namnekonsistens 3 og 4.

## Utført, runde 2

Brukaren bad om at alle attverande tiltak i handlingslista skulle
gjennomførast. Alle punkt er no løyste.

**Funn 2, resten (`mcp-begrep-run` → `mcp-linkml-begrep-utkast-run`):**
- Sed-sveip over `mkdocs/docs/ny-begrepsmodell.md`,
  `specs/backlog/mcp-begrep-utkast-enkeltfil-generering.md`,
  `src/assets/scripts/scaffolding/{new-begrepskatalog,new-begrepssamling}.sh`,
  `src/mcp-linkml-begrep-utkast/README.md`. `specs/done/` urørt.

**Funn 4 (daud `print_*`-kode):**
- `print_info`, `print_warning`, `print_error` fjerna frå
  `make/03-output.mk` (berre `print_header`/`print_step` var i reell bruk).
- `make/README.md` oppdatert: fjerna referanse til `print_info` i
  makro-oversikta, og omskrive logging-konvensjonen til å skildre den
  faktiske arbeidsdelinga (`print_header`/`print_step` for overskrifter,
  `LOG_FUNCTIONS` for status/feil).

**Funn 5 (stray backup-fil):**
- `make/10-generator-macros.mk.bak` sletta.

**Funn 7 (manglande `## `-hjelpetekst) + ein relatert `help.sh`-bug:**
- Lagt til `## `-hjelpetekst på alle target lista i funn 7:
  `make/30-instances.mk` (5 target), `make/60-mcp.mk` (11 target, inkl. alle
  `build-docker-mcp-*` og heile `mcp-linkml-{valider-modell,modell-utkast,
  begrep-utkast}`-familien), `make/70-scaffolding.mk` (5 target),
  `make/40-validation.mk` (`log-mcp-validate`, `log-validate-instance`).
  Interne target (`_mcp-valider-modell-with-header`, `_gource-render`)
  framleis utan `## ` som tilsikta.
- **Bug oppdaga og retta i `src/assets/scripts/makefile/help.sh`:** verifisering
  med `make help` etter dei nye `## `-linjene avslørte to eksisterande feil i
  kategoriseringslogikken, begge usynlege før no fordi ingen target med desse
  eigenskapane hadde `## `-tekst tidlegare:
  1. Target med eit Makefile-prerequisite (t.d.
     `mcp-linkml-valider-modell-smoke: build-docker-mcp-validator ## ...`)
     fekk prerequisite-namnet med i namnekolonna i output
     (`mcp-linkml-valider-modell-smoke: build-docker-mcp-validator`) — same
     feilmønster fanst frå før på `gource-preview`/`gource-video`, berre
     ikkje lagt merke til.
  2. Kategori-filtreringa var ikkje gjensidig utelukkande trass i
     toppkommentaren sin påstand om at «første kategori-mønster som matchar
     vinn» — `build-docker-mcp-*`-target matcha både «Container images»
     (`build-docker-`) og «MCP-serverar» (`mcp-`) og vart difor lista dobbelt.
  `help.sh` omskriven til eitt-gjennomlaup med ein `shown`-oppslagstabell som
  faktisk handhevar første-match-vinn, pluss eit sed-steg som strippar
  prerequisite frå namnekolonna før utskrift. Verifisert med full
  `make help`-køyring: ingen duplikat, ingen garbla target-namn, alle nye
  target synlege i korrekt kategori.

**Namnekonsistens 3 (asymmetriske MCP-sub-target):**
- Undersøkt: `tests/` har `test_mcp_linkml_generator.py` (modell-utkast) og
  `test_mcp_policies.py` (validator), men ingen ekvivalent for begrep-utkast.
  Ingen testsuite å knyte ein `-test`-target til. Dokumentert med kommentar i
  `make/60-mcp.mk` i staden for å oppretta eit tomt/uverksamt target.

**Namnekonsistens 4 (`log-mcp-validate`/`log-validate-instance` vs.
`validate-capture`):**
- Undersøkt begge underliggande script (`run-validation.sh`,
  `run-schema-validation.py`). Konklusjon: reelt ulike behov, ikkje
  modningsrestar. `run-validation.sh` er kalla direkte frå
  `.github/workflows/{generate,validate}.yml` — CI-kritisk infrastruktur.
  `run-schema-validation.py`/`validate-capture` er eit manuelt batch-verktøy
  avgrensa til `release-please-config.json` sine "released packages", ikkje
  brukt frå CI. Konsolidering vart difor medvite **ikkje** utført —
  å skrive om CI-kritisk script for DRY åleine krev eksplisitt brukar-
  godkjenning (CLAUDE.md). Konklusjonen er dokumentert som kommentar over
  `validate-capture` i `make/40-validation.mk`.

**Attverande smårettingar oppdaga undervegs:**
- `COMMANDS.md` sin rad for `new-begrepskatalog` sa framleis "Deprecated" —
  inkonsistent med retting frå runde 1 (tiltak 3a). Retta til å skildre
  legacy-status korrekt, i tråd med `make/70-scaffolding.mk`.
- `src/assets/scripts/makefile/run-validation.sh` sin eigen kommentar om
  eigen filplassering ("scriptet ligg i src/assets/scripts/ci/") var forelda
  etter flyttinga i runde 1 (funn 6) — retta til `makefile/`.

**Verifisert:** `make -n help` (ingen parsefeil), full `make help`-køyring
(alle nye target synlege, ingen duplikat/garbling), repo-vidt grep-sveip
for attverande `new-model`/`mcp-validate`/`mcp-linkml-validate`/
`mcp-begrep-run` utanom `specs/done/` — tomt resultat.

**Ikkje rørt (utanfor det brukaren bad om):** `.claude/settings.local.json`
sine forelda permission-mønster (reint lokal verktøykonfig, ikkje del av
make-laget/kodebasen).

Alle funn og namnekonsistens-punkt frå denne auditen er no løyste.
