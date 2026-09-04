# Evaluering: DRY-kandidatar i GitHub workflow-filer

## Bakgrunn

Brukaren bad om ei evaluering av om det framleis finst kode i
`.github/workflows/*.yml` som er gode kandidatar for å trekkjast ut i
felles/gjenbrukbare GitHub Actions (`.github/actions/`). **Eksplisitt
sett terskel for denne evalueringa:** kode eller liknande kode brukt på
**2 eller fleire stader** — lågare enn CLAUDE.md sin vanlege DRY-terskel
på 3+ identiske tilfelle, som elles gjeld generelt i repoet.

## Metode

Alle `.github/workflows/*.yml`-filer og alle eksisterande
`.github/actions/*/action.yml` er lesne i sin heilskap (ikkje berre
grep-treff) for å samanlikne faktisk steginnhald, og for å unngå å
føreslå ekstraksjon av noko som alt er ein delt action. Éin
leietråd frå tidlegare arbeid denne økta (P3 i
`specs/done/evaluering-gjentakande-monster-backlog.md` — cache-nøkkel-
duplisering mellom `generate.yml` og `lenkje-og-mermaid-sjekk.yml`) vart
brukt som utgangspunkt, ikkje som einaste søkjeområde.

## Funn — reelle kandidatar (identisk/nesten identisk, trygt å trekkje ut)

### K1 — `modell-analyse.yml`: 11 jobbar deler same 4-stegs skjelett, OG byggjer image frå botnen kvar gong (høgast verdi, flest førekomstar) — revidert etter utdjupande utgreiing

**Stad:** `similar-classes-domain` (14-39), `similar-classes-all` (42-67),
`similar-slots-domain` (70-95), `similar-slots-all` (98-123),
`similar-types-domain` (126-151), `similar-types-all` (154-179),
`iri-dereferering` (182-207), `innhaldsforhandling` (210-235),
`ap-no-gjenbruk` (238-263), `modell-sammenhenger` (266-291),
`sammendrag` (293-330).

**Duplikasjon (steg-skjelett):** Alle 11 har verbatim `actions/checkout@v7`
+ `make build-docker-python`. 10 av 11 (alle unnateke `sammendrag`) har i
tillegg identisk mønster: `make analyse-X > X-report.md` →
`{ echo "## <tittel>"; cat X-report.md; } >> "$GITHUB_STEP_SUMMARY"` →
`actions/upload-artifact@v7` med `name: X-report`, `path: X-report.md`,
`retention-days: 30`. Einaste variasjonen: make-target, filnamn,
STEP_SUMMARY-tittel, artefaktnamn.

**Ekstra funn ved utdjupande utgreiing — biletbygging, ikkje berre
steg-duplikasjon:** `run: make build-docker-python` byggjer
`python-pytest`-biletet **frå botnen** i kvar av dei 11 jobbane (full
Alpine-pull + `apk add git` + `pip install`), i staden for å nytte
ensure-images/pull-images-mønsteret `generate.yml`/
`lenkje-og-mermaid-sjekk.yml`/`validate.yml` alt brukar (bygg+push berre
ved cache-miss via `ensure-image`, seinare jobbar **hentar** via
`pull-images`). Stadfesta: alle 11 jobbar brukar **berre**
`python-pytest` (ingen brukar `LINKML_RUN`/andre image) — éin einaste
image-type å handtere.

**Revidert forslag (kombinerer det opphavlege steg-skjelettet OG
biletbygginga — utgreiinga konkluderte at dette **bør kombinerast, ikkje
handterast separat**, sidan composite actions ikkje kan uttrykkje
`needs:` på jobb-nivå):**

1. **Ny, ikkje-matrise jobb `ensure-images`** i `modell-analyse.yml`
   (trivielt forenkla variant av mønsteret i dei tre andre filene, sidan
   berre éin image trengst): `checkout` → `compute-image-tags` →
   `upgrade-crun` → `ghcr-login` → `ensure-image` (target:
   `build-docker-python`).
2. **`.github/actions/run-modell-analyse`** (ny composite action) tek imot
   `make-target`, `report-name`, `summary-title`, og gjer internt:
   `upgrade-crun` → `ghcr-login` → `pull-images` (fast, hardkoda for
   `python-pytest` — treng ikkje vere eit input, sidan alle 11 jobbar har
   same biletbehov) → køyr make-target → skriv `$GITHUB_STEP_SUMMARY` →
   last opp artefakt.
3. Kvar av dei 11 jobbane vert då: `checkout` + `needs: ensure-images` +
   éin composite-kall — same linjetal-reduksjon som opphavleg (**~150
   linjer YAML → ~40 linjer**, pluss éin ny ~35-40-linjers action), pluss
   biletgevinsten.

**Estimert gevinst:** `modell-analyse.yml` køyrer sjeldan
(`schedule: cron '0 7 * * 1'`, kvar måndag — pluss `workflow_dispatch`),
så den akkumulerte gevinsten over tid er **liten samanlikna med K1-K3 sin
opphavlege steg-duplikasjon** (som gjeld workflowar som køyrer på kvar
push). Grovt estimert 2-5 minutt total compute-tid spart **per køyring**
(11 × eit par-fem-og-tjue sekund), men berre éin køyring i veka.
Hovudverdien er difor meir prinsipiell enn økonomisk: fjernar det einaste
attverande "bygg frå botnen kvar gong"-mønsteret i repoet, og gjer
`modell-analyse.yml` konsistent med korleis alle andre workflowar
handterer image. Sidan `python-pytest` sin image-tag er ein deterministisk
hash av `Dockerfile.python`+`requirements-python-test.txt`, og
`generate.yml` alt held biletet oppdatert i GHCR på kvar push til main,
vil `ensure-images` i praksis nesten alltid berre gjere eit raskt
`skopeo inspect`-treff (bygg+push-grenene køyrer sjeldan).

**Risiko/kompleksitet:** Låg — mønsteret er alt etablert og verifisert i
tre andre workflow-filer, ingen ny logikk. Einaste nye: `ensure-images`
som **ikkje-matrise**-jobb (dei tre eksisterande brukar matrise over
fleire image) — ei trivielt forenkla variant, ingen kjend fallgruve.

### K2 — `release.yml`: rå `podman login`-duplikasjon, trass i at `ghcr-login`-actionen alt finst

**Stad:** linje 21, 48, 75, 103 — alle fire jobbar (`linkml-local`,
`mcp-linkml-validator`, `mcp-linkml-modell-utkast`,
`mcp-linkml-begrep-utkast`). Verifisert direkte:

```
21:        run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin
48:        run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin
75:        run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin
103:        run: echo "${{ secrets.GITHUB_TOKEN }}" | podman login ghcr.io -u ${{ github.actor }} --password-stdin
```

**Duplikasjon:** Eksakt same eittlinjeskommando som
`.github/actions/ghcr-login/action.yml` alt kapslar inn — og som **alt er
korrekt brukt 10 andre stader i repoet** (`ghcr-login`-actionen sin eigen
kommentar seier han vart trekt ut nettopp for å hindre denne kommandoen
frå å drive frå kvarandre mellom workflow-filer). `release.yml` brukar alt
`upgrade-crun`-actionen rett før i alle fire jobbar, men har tydelegvis
gløymt å byte til `ghcr-login` for login-steget.

**Forslag:** Trivielt, mekanisk: byt alle fire `run:`-steg ut med
`uses: ./.github/actions/ghcr-login` + `with: github-token:
${{ secrets.GITHUB_TOKEN }}`. **Ingen ny kode — actionen finst alt.**
Lågast risiko, høgast tillit av alle funna her.

### K3 — `upgrade-crun` + `ghcr-login` som par, gjenteke 8 gonger på tvers av 3 filer

**Stad (adjacente par, same rekkjefølgje kvar gong):** `generate.yml`
112-118, 168-176, 273-281, 521-529, 621-629 (5 stader i éi fil, dei fire
siste med `if: steps.<cache-id>.outputs.cache-hit != 'true'`-vakt på
begge steg). `lenkje-og-mermaid-sjekk.yml` 71-77, 132-140 (sistnemnde med
vakt). `validate.yml` 150-154.

**Forslag:** Ny composite `.github/actions/prepare-podman` (namn ope for
diskusjon) som kombinerer dei to. **Merk:** composite actions støttar
ikkje ein eigen `if:` for indre steg via input, så vakta må framleis liggje
på **kallesteget**, ikkje inni actionen — det avgrensar gevinsten noko for
dei 5 vaktbeskytta tilfella, men fjernar likevel duplikasjonen av sjølve
kall-linjene. Estimert moderat verdi (~4 linjer spart × 8 = ~32 linjer),
men reduserer talet på stader "kva versjon av denne parkoplinga" må
haldast i synk.

**Utviding funnen ved den nye reusable-workflow-kartlegginga:** det breiare
"cache-gata podman-oppsett"-mønsteret (`actions/cache@v6`-treff →
`if: cache-hit != 'true'`-vakt → `upgrade-crun` + `ghcr-login` +
`pull-images`, tre steg samla) går att i **5** jobbar — `generate`-jobben
i både `generate.yml` og `lenkje-og-mermaid-sjekk.yml`,
`valider-og-analyser`, `modellanalyse-tvers-domene`, og `validate`-jobben
i `validate.yml`. Kvar har ulik "gjer arbeidet"-hale etterpå, men
prefikset (crun+ghcr-login+pull-images) kunne foldast til éin
composite-kall med eit `images:`-input, på tvers av alle 5 — ei naturleg
utviding av same K3-forslag (inkluder `pull-images` i
`prepare-podman`-actionen for desse 5 "forbrukar"-jobbane, ikkje berre
crun+ghcr-login-paret), ikkje eit eige punkt.

## Funn — kandidatar for nye reusable workflows (utdjupa gjennomførbarleiksvurdering)

Repoet har alt to `reusable-*.yml`-filer (`reusable-generate.yml`,
`reusable-validate.yml`), men dei er **ikkje** interne DRY-verktøy — dei
er public-facing API meint for eksterne repo som skal
generere/validere eitt enkelt skjema (`workflow_call` med
`schema:`-input), urelatert til denne kartlegginga.

### G1+G2 — `checkout-source` + `ensure-images`-jobbane, nesten identiske i 3 filer — **teknisk gjennomførbare, mindre risikabelt enn opphavleg vurdert**

**Stad:** `checkout-source`: `generate.yml` 47-76,
`lenkje-og-mermaid-sjekk.yml` 9-45, `validate.yml` 81-130.
`ensure-images` (matrise over image): same tre filer, tilsvarande
jobbar (checkout → download source → upgrade-crun → ghcr-login →
ensure-image).

**Gjennomførbarleik, verifisert ved utdjupande utgreiing (ingen reell
GitHub Actions-avgrensing funnen):**
- **Outputs:** `on.workflow_call.outputs:` mappar rett til
  `jobs.<job>.outputs.X` internt, og eksponerast til kallaren som
  `needs.<call-job-id>.outputs.X` — akkurat same syntaks som i dag. Fullt
  støtta.
- **Matrise nedstraums:** ein jobb i den kallande workflowen kan bruke
  `needs.<workflow_call-jobb>.outputs.X` til `strategy: matrix:` —
  GitHub handsamar ein `uses: ./.github/workflows/x.yml`-jobb identisk
  med ein vanleg jobb for `needs:`/`outputs:`-føremål. Ingen avgrensing.
- **`secrets: inherit`:** standard, trygt mønster for GHCR-login-steget
  inni G2.
- **Artefaktar over grensa:** `workflow_call` køyrer som jobbar i **same**
  workflow-run (ikkje ein separat run) — `upload-`/`download-artifact`
  fungerer identisk som i dag, ingen spesialhandtering nødvendig.
- **Reelle skilnader mellom filene, alle trivielt parametriserbare:**
  `validate.yml` sin `checkout-source` har to ekstra steg (eit
  `images`-filter til `always_required`-image, og oppslag av gamle
  valideringsloggar) — løysast med eit ekstra `always_required_images`-
  output pluss eit `clean-validation-logs: true/false`-input. Artefakt-
  sti-lista skil seg (`validate.yml` ekskluderer `mkdocs/`, `README.md`,
  `CODEOWNERS.md`) — løysast med eit `artifact-paths`-input. Ekstra
  enkeltsteg (debug-logg i `generate.yml`, "trekk inn lychee" i
  `lenkje-og-mermaid-sjekk.yml`) **bør ikkje** proppast inn i den delte
  workflowen — behald dei som separate steg i kvar kallar, held den delte
  kjernen minimal.

**Forslag:** slå saman G1+G2 til éin ny, **intern** reusable workflow
(t.d. `.github/workflows/reusable-oppsett.yml` — ikkje forveksle med dei
to eksisterande, eksterne `reusable-*.yml`). Estimert: ~225 linjer
duplisert jobbkode (3 × ~75 linjer) → éin ~90-linjers reusable workflow +
3 × ~10-linjers kallblokker ≈ **165+ linjer spart**, same storleiksorden
som K1.

**Revidert tilråding:** teknisk gjennomførbart og **ikkje lenger avvist
som "for komplekst"** — men blast radius er reelt (ein wiring-feil ville
råke `generate`/`validate`/`lenkje-og-mermaid-sjekk` samstundes). Bør
gjerast **isolert og testast grundig**, og krev framleis eksplisitt
brukargodkjenning før implementering — status endra frå "ikkje teke
vidare" til "gjennomførbart, avventar prioritering".

**Ingen nye heil-jobb-kandidatar funne** utover G1/G2 (2+-terskelen
brukt): `publish`-jobben i `generate.yml` er unik, ingen tvilling.
`create-pull-request`-mønsteret finst berre éin stad (`validate.yml`,
linje 325) — under terskelen. `release-please.yml` sine
`actions/checkout@v7`-kall er isolerte enkeltlinjer utan delt kontekst
med resten — same kategori som G3 under.

### G3 — `actions/download-artifact@v8` for "source"-artefakten, 11 stader

Kvar førekomst er berre 3 linjer, 100 % standard bruk utan eigen logikk.
Terskelen (2+) er langt overskride, men **truleg ikkje verdt
kompleksiteten** — éin ekstra indireksjonslag for eit alt trivielt,
sjølvforklarande steg. Nemnt for fullstendigheit, lågast verdi av alle
funna.

## Alt korrekt trekt ut (vurdert, ingen endring naudsynt)

`upgrade-crun`, `compute-image-tags`, `detect-required-images`,
`discover-domains`, `ensure-image`, `generate-domain`, `ghcr-login`,
`merge-generated-artifacts`, `pull-images` — alle ni er veldefinerte,
einsidige composite actions med klar grunngjeving i eigne kommentarar
(fleire refererer eksplisitt til kva spec dei vart trekt ut frå). Ingen
intern duplikasjon funne i sjølve action.yml-filene.

## Anbefaling

Prioritert etter risiko/verdi-forhold:

1. **K2** — gjer først. Null ny kode, mekanisk bytte, høgast tillit.
   Rettar eit reelt avvik der ein alt-etablert action ikkje vart brukt.
2. **K1** (revidert, no òg med ensure-images/pull-images for
   `modell-analyse.yml`) — høgast strukturell verdi, moderat innsats (éin
   ny `ensure-images`-jobb + éin ny composite action + 11 kallestader
   oppdatert). Ytingsgevinsten er liten (workflowen køyrer berre vekentleg),
   men verdien er prinsipiell: siste attverande "bygg-frå-botnen"-mønster
   i repoet.
3. **K3** (utvida med pull-images-prefikset for dei 5 "forbrukar"-jobbane)
   — moderat verdi.
4. **G1/G2** — **teknisk gjennomførbart** (revidert frå "ikkje teke
   vidare" etter utdjupande gjennomførbarleiksvurdering: ingen reell
   GitHub Actions-avgrensing funnen), men bør gjerast **isolert og testast
   grundig** gitt blast radius (råkar `generate`/`validate`/
   `lenkje-og-mermaid-sjekk` samstundes). Krev framleis eksplisitt
   brukargodkjenning før implementering — høgast potensiell linjegevinst
   (165+ linjer) av alle kandidatane, men òg høgast risiko ved feil.
5. **G3** — ikkje anbefalt. Kompleksiteten ved indireksjon oppveg ikkje
   den vesle gevinsten for eit sjølvforklarande 3-linjers steg.

## Avgjerder

- **Slo saman den opphavlege K1 (steg-skjelett) med
  ensure-images/pull-images-optimaliseringa for `modell-analyse.yml`, i
  staden for å halde dei som to separate punkt (K1 + eit nytt K4).**
  Grunngjeving: utgreiinga fann at composite actions ikkje kan uttrykkje
  `needs:` på jobb-nivå, så den nye `ensure-images`-jobben må uansett
  leggjast til i same YAML-endring som composite-action-ekstraksjonen —
  å handtere dei som separate tiltak ville berre tvinge fram at K1 vart
  implementert to gonger.
- **Behandla G1 og G2 samla (ikkje separate punkt), og oppgraderte statusen
  deira frå "ikkje teke vidare" til "gjennomførbart, avventar
  prioritering".** Grunngjeving: den utdjupande gjennomførbarleiks-
  vurderinga fann ingen reell teknisk avgrensing (outputs, matrise,
  secrets og artefaktar fungerer alle identisk over ein
  `workflow_call`-grense) — den opphavlege "høgare risiko/kompleksitet"-
  vurderinga var for konservativ. Behaldt likevel kravet om eksplisitt
  brukargodkjenning før implementering, sidan blast radius framleis er
  reelt (tre kritiske workflow-filer råka samstundes ved ein wiring-feil).
- **Utvida K3 i staden for å opprette eit nytt punkt** for
  "cache-gata podman-oppsett i 5 jobbar"-funnet. Grunngjeving: det er
  same underliggjande duplikasjon (crun+ghcr-login-paret) sett frå ein
  breiare vinkel (no òg med pull-images inkludert for forbrukar-jobbane)
  — ikkje eit nytt, uavhengig mønster.

## Opent spørsmål

Kva for kandidatar (K1 revidert, K2, K3 utvida) ønskjer du å realisere, og
i kva rekkjefølgje? Og skal G1/G2 (intern reusable workflow for
`checkout-source`/`ensure-images`, no vurdert teknisk gjennomførbart)
prioriterast som eige, isolert tiltak, eller leggjast til side inntil
vidare?

## Utført

Brukaren stadfesta K1, K2 og K3 (G1/G2 attstår, ikkje implementert).

**K2:** `release.yml` sine fire raske `podman login`-linjer bytt ut med
`uses: ./.github/actions/ghcr-login`. Actionlint reint.

**K1 (revidert):** `modell-analyse.yml` fekk ein ny, ikkje-matrise
`ensure-images`-jobb (sikrar `python-pytest` i GHCR, bygg+push berre ved
cache-miss). Ny composite action
`.github/actions/run-modell-analyse` kapslar inn det 4-stegs skjelettet
(hent bilete → køyr make-target → skriv `$GITHUB_STEP_SUMMARY` → last opp
artefakt) — brukt av alle 10 rapport-jobbane, kvar redusert til
`checkout` + `needs: ensure-images` + éin composite-kall.
`sammendrag`-jobben (annan struktur — lastar ned artefaktar, ikkje opp)
fekk `needs: ensure-images` lagt til og biletbygginga bytt ut med
tilsvarande hent-frå-GHCR-steg. Alle jobbar fekk `packages: read`
(`ensure-images` fekk `packages: write`).

**K3 (utvida):** Ny composite action `.github/actions/prepare-podman`
(crun + GHCR-login + valfri `pull-images`, sidan composite actions ikkje
kan uttrykkje `if:` for indre steg via input — cache-hit-vakta ligg
framleis på kallesteget). Brukt på **15 kallestader**: dei opphavleg
kartlagde 8 (`generate.yml` ×5, `lenkje-og-mermaid-sjekk.yml` ×2,
`validate.yml` ×1), pluss **4 nye i `release.yml`** (synlege først etter
K2-fiksen — dei brukte no `ghcr-login`-actionen og matcha dermed
crun+ghcr-login-mønsteret), pluss **2 nye i `modell-analyse.yml`** (frå
K1), pluss **1 internt i `run-modell-analyse`-actionen sjølv** (i staden
for å duplisere dei same tre stega der òg). Jobbar med genuint avvikande
struktur (`validate.yml` sin `commitlint`-jobb: crun utan ghcr-login;
`validate.yml` sin `validate`-jobb: ghcr-login utan crun) vart **medvite
ikkje** rørte, sidan dei ikkje matchar paret.

**Verifisert:** `actionlint` (ingen `[expression]`-feil, berre pre-
eksisterande `[shellcheck]`-råd) på alle fem endra workflow-filer,
YAML-syntakssjekk (Python) på alle workflow- og action-filer, og manuell
gjennomgang av alle 15 `prepare-podman`-kallestader mot faktisk før-
struktur (statisk `images`-liste vs. dynamisk `detect-required-images`-
mellomsteg — sistnemnde jobbar fekk berre crun+ghcr-login samla, pull-
images-steget urørt som eige steg etterpå).

**G1+G2 (etter oppfølgingsbestilling):** Ny intern reusable workflow
`.github/workflows/reusable-oppsett.yml` (`on.workflow_call`), med to
jobbar (`checkout-source` → `ensure-images`, lenka internt via `needs:` —
begge INNI same fil, ikkje over ein `workflow_call`-grense, sidan berre
`ensure-images` treng `checkout-source` sine outputs). Parametrisert for
skilnadene mellom dei tre kallarane:
- `always-required-only` (boolean, default `false`) — validate.yml sitt
  behov for å filtrere `images`-outputen til berre `always_required`.
  Løyst med eit reint bash-basert steg (`if [ "${{ inputs.X }}" = "true"
  ]`) i staden for eit GH-uttrykk-ternær (`cond && a || b`), for å unngå
  uverifisert uttrykkssyntaks i noko med så stor blast radius.
- `clean-validation-logs` (boolean, default `false`) — validate.yml sitt
  ekstra oppryddingssteg før artifact-opplasting.
- `artifact-paths` (multi-line string, default dekker
  generate.yml/lenkje-og-mermaid-sjekk.yml sitt identiske behov) —
  validate.yml overstyrer med ei innsnevra liste.

`generate.yml`, `lenkje-og-mermaid-sjekk.yml` og `validate.yml` fekk kvar
sin `checkout-source`+`ensure-images`-jobb erstatta med éin
`oppsett:`-jobb (`uses: ./.github/workflows/reusable-oppsett.yml`, med
eksplisitt `permissions: contents: read, packages: write` — GITHUB_TOKEN
sine faktiske permissions i ein kalla reusable workflow er det MEST
restriktive av kva kallejobben OG kva den kalla workflowen sjølv
deklarerer, så dette måtte setjast på kallejobben, ikkje berre inni
`reusable-oppsett.yml`). Alle nedstraums-jobbar (11 stader på tvers av dei
tre filene) fekk `needs: [...]` og `needs.checkout-source.outputs.X` →
`needs.oppsett.outputs.X` oppdatert.

**Avvik frå opphavleg plan, med grunngjeving:** to per-kallar-ekstrasteg
kunne IKKJE bli verande inni den delte `ensure-images`-jobben, sidan ein
reusable workflow sine jobbar er faste — kallaren kan ikkje injisere
ekstra steg midt inni. `generate.yml` sitt reint diagnostiske
"Logg artifact-innhald og miljøinfo"-steg (disk/versjon-info, ingen
nedstraums-forbrukar) vart **fjerna heilt** — informasjonen er uansett
synleg i kvart podman/skopeo-kommandokall sin eigen output.
`lenkje-og-mermaid-sjekk.yml` sitt "Trekk inn lychee"-steg vart **flytta**
til ein ny, liten, uavhengig jobb (`trekk-inn-lychee`) — biletet sitt
eige kommentar stadfesta alt at steget ikkje overfører til
lenkjesjekk-jobben sin eigen runner uansett (kvar jobb har eigen runner),
så flyttinga endrar ikkje funksjonell åtferd, og gir i tillegg ein liten
biverknad: han køyrer no éin gong (eigen jobb) i staden for éin gong per
image i den tidlegare matrisa (marginal effektiviseringsgevinst, ikkje
sjølve føremålet med flyttinga).

**Verifisert:** `actionlint` (ingen `[expression]`-feil — inkluderer
GitHub sin eigen validering av at `needs:`-jobbnamn og
`needs.X.outputs.Y`-referansar faktisk finst, kritisk for akkurat denne
endringa sin risikoprofil) og YAML-syntakssjekk på alle fem endra
workflow-filer og den nye `reusable-oppsett.yml`.

Alle kandidatar frå denne evalueringa (K1, K2, K3, G1, G2) er no
realiserte.
