# Evaluering: treng `.claude/rules/ci-workflows.md` tillegg etter workflow-refaktoreringa?

## Bakgrunn

Brukaren bad om ei evaluering av om dei omfattande endringane i
`.github/workflows/*.yml`/`.github/actions/*/action.yml` denne økta
(`specs/done/evaluering-dry-github-workflows.md`, K1-K3 + G1/G2 — to nye
composite actions, éin ny intern reusable workflow, 15+ kallestader
konsolidert) skaper behov for tillegg i eksisterande
`.claude/rules/ci-workflows.md`. Dette er ei evaluering, ikkje eit
utføringsoppdrag.

## Metode

Las gjeldande `.claude/rules/ci-workflows.md` fullt ut (28 linjer, scopa
til `.github/workflows/**`, dekker i dag berre actionlint-plikta). Gjekk
gjennom dei konkrete, ikkje-opplagte lærdomane frå dagens
workflow-refaktorering — kvar av dei er verifisert mot faktisk hendt
åtferd i denne økta, ikkje spekulative "beste praksisar" (jf. metoden i
`.claude/skills/ny-rule/SKILL.md` steg 1).

## Funn — konkrete kandidatar for tillegg

### F1 — Scope-hòl: rula dekker ikkje `.github/actions/**`

**Bevis:** `paths:` er i dag `[".github/workflows/**"]` åleine. Denne
økta oppretta/endra fleire filer under `.github/actions/**`
(`prepare-podman/action.yml`, `run-modell-analyse/action.yml`) utan at
rula lasta automatisk. Sidan composite actions og reusable workflows er
tett samankopla (workflow-filene kallar dei, dei kallar kvarandre), er
dette eit reelt blindsone.

**Forslag:** Utvid `paths:` til å òg dekke `.github/actions/**`.

### F2 — `actionlint` validerer IKKJE `.github/actions/*/action.yml`

**Bevis:** Verifisert direkte denne økta —
`podman run ... actionlint ... .github/actions/run-modell-analyse/action.yml`
gav fem falske "unexpected key"/"section is missing"-feil, sidan
actionlint tolkar fila som ein workflow (som krev `jobs:`/`on:`), ikkje
som ein composite action. Dagens rule seier "Køyr via podman" utan å
presisere at dette berre gjeld `.github/workflows/*.yml` — nokon som
følgjer rula bokstaveleg på ei `action.yml`-fil ville få misvisande
feilmeldingar og kunne tru fila er øydelagd.

**Forslag:** Presiser eksplisitt at actionlint-plikta gjeld
`.github/workflows/*.yml`, IKKJE `.github/actions/*/action.yml`. For
sistnemnde: YAML-syntakssjekk (`python3 -c "import yaml; yaml.safe_load(...)"`)
er det som faktisk validerer dei.

### F3 — Reusable workflow-kallejobbar treng eksplisitte `permissions:`

**Bevis:** Oppdaga direkte denne økta under G1/G2-implementeringa:
GITHUB_TOKEN sine faktiske permissions i ein kalla reusable workflow
(`uses: ./.github/workflows/X.yml`) er det **mest restriktive** av kva
kallejobben deklarerer OG kva den kalla workflowen sine eigne jobbar
deklarerer. Utan eksplisitt `permissions:` på sjølve kallejobben
(ikkje berre inni den kalla fila) kunne `ensure-images` sitt
`packages: write`-behov (GHCR-push) blitt stille nedskalert — ein feil
som **ikkje** ville synast før ein faktisk CI-køyring (verken
`actionlint` eller YAML-syntakssjekk fangar dette).

**Forslag:** Legg til som eksplisitt regel: ei kallejobb til ein intern
reusable workflow (`uses: ./.github/workflows/*.yml`) skal alltid ha eit
eksplisitt `permissions:`-block som minst dekker det den kalla workflowen
sine jobbar treng.

### F4 — Reusable workflow-jobbar kan ikkje ta imot kallar-spesifikke ekstra steg

**Bevis:** Under G1/G2 vart `generate.yml` sitt diagnostiske
"Logg artifact-innhald og miljøinfo"-steg og
`lenkje-og-mermaid-sjekk.yml` sitt "Trekk inn lychee"-steg **fjerna**
(fyrstnemnde) og **flytta til ein separat jobb** (sistnemnde), fordi
begge var kallar-spesifikke tillegg til ein jobb som no er delt via
`workflow_call` — reusable workflow-jobbar har ein fast steg-sekvens,
kallaren kan ikkje injisere eit steg midt inni.

**Forslag:** Legg til som ei vurderingsrettleiing: før ein trekk ut ein
jobb til ein reusable workflow, sjekk om ALLE kallarar faktisk har
identisk steg-sekvens. Kallar-spesifikke ekstra steg må anten
parametriserast (input-styrt `if:` på steg INNI den delte jobben, jf.
`prepare-podman` sitt `images != ''`-mønster) eller flyttast til ein
separat jobb hos kvar kallar — dei kan ikkje "setjast inn" i den delte
jobben frå kallaren.

### F5 — Composite actions kan ikkje lese kallaren sin `steps.*`-kontekst

**Bevis:** `prepare-podman`-actionen kan gate sine EIGNE interne steg via
input-verdiar (`if: inputs.images != ''`), men kan ikkje lese kallaren sin
`steps.<cache-id>.outputs.cache-hit` — cache-hit-vakta må difor liggje på
**kallesteget** (`if: steps.cache-id.outputs.cache-hit != 'true'` på sjølve
`uses: ./.github/actions/prepare-podman`-linja), ikkje inni actionen.
Dette avgrensar kor mykje ein composite action kan absorbere av
duplikasjon når kallarar har ulike cache-vakter.

**Forslag:** Legg til som ei kort presisering ved sida av F4, sidan begge
handlar om kva som IKKJE kan delast/parametriserast i høvesvis composite
actions og reusable workflows.

### F6 — To kategoriar reusable workflows i repoet — ikkje forveksle

**Bevis:** `reusable-generate.yml`/`reusable-validate.yml` er **public
API for eksterne repo** (workflow_call med `schema:`-input). Den nye
`reusable-oppsett.yml` (denne økta) er eit **internt DRY-verktøy**, kalla
berre av dei tre workflow-filene i dette same repoet. Lett å forveksle
sidan begge ligg i same katalog med same namneprefiks.

**Forslag:** Kort presisering i rula om skiljet, med tilvising til begge
kategoriane.

## Vurdert, men ikkje anbefalt som eiga rule-tillegg

**Lågare DRY-terskel (2+ i staden for 3+) for CI-workflow-YAML
spesifikt.** Brukaren sette dette eksplisitt for éin konkret
evalueringsoppgåve tidlegare denne økta ("Terskelen for DRY skal være at
koden eller liknande kode er brukt 2 stader"). Usikkert om dette var meint
som ein varig repo-policy for all framtidig CI-arbeid, eller ei
avgrensa presisering for nettopp den eine kartlegginga. Grunngjeving for
IKKJE å inkludere det no utan vidare avklaring: å permanent skrive inn ein
talfesta terskel som avvik frå CLAUDE.md sin elles gjeldande 3+-regel er
ei ikkje-triviell policy-avgjerd som fortener eksplisitt stadfesting, ikkje
utleiast frå ein enkelt økt-spesifikk instruks (jf. steg 1 i
`.claude/skills/ny-rule/SKILL.md` — krev konkret grunngjeving, men unngår
å overtolke omfanget av eit einskild, oppgåve-avgrensa brukarval).

## Anbefaling

F1-F6 er alle konkrete, verifiserte, ikkje-spekulative — realiser som eitt
samla tillegg til `.claude/rules/ci-workflows.md`:
- F1: utvid `paths:` til å inkludere `.github/actions/**`
- F2: presiser actionlint-scope (berre `.github/workflows/*.yml`)
- F3+F4+F5: ny seksjon om reusable workflow/composite action-avgrensingar
  (permissions, faste steg, avgrensa kontekst-tilgang)
- F6: kort presisering av dei to reusable-workflow-kategoriane

DRY-terskel-spørsmålet (vurdert-men-ikkje-anbefalt over) bør avklarast
eksplisitt med brukaren dersom det skal takast vidare, ikkje inkluderast
stilltiande.

## Opent spørsmål

Skal eg realisere F1-F6 som tillegg til `.claude/rules/ci-workflows.md`?
Og ønskjer du at den lægre DRY-terskelen (2+) for CI-YAML skal
formaliserast som ein varig regel, eller skal han halde fram som
ei økt-spesifikk avgjerd?

**Svart av brukar:** Realiser F1-F6, og formaliser DRY-terskelen (2+) som
ein varig regel.

## Avgjerder

- **Formaliserte 2+-terskelen som eit eksplisitt CI-YAML-unntak i BÅDE
  CLAUDE.md (éin kryssreferanselinje) og `.claude/rules/ci-workflows.md`
  (full grunngjeving), i staden for berre den eine staden.** Grunngjeving:
  CLAUDE.md sitt DRY-avsnitt er der 3+-hovudregelen står — utan ei
  tilvising der ville nokon som berre les CLAUDE.md (utan å opne rula)
  aldri oppdage at CI-YAML har eit unntak. Sjølve grunngjevinga/dømet høyrer
  heime i rula (kortare CLAUDE.md, detaljar der dei faktisk trengst — same
  mønster som resten av CLAUDE.md sine rule-tilvisingar).
- **Alle F1-F6 realisert i éin samla omskriving av `ci-workflows.md`,
  ikkje som separate tillegg.** Grunngjeving: dei heng tett saman
  (permissions/faste-steg/kontekst-avgrensingar er tre fasettar av same
  "kva kan delast i CI-YAML"-spørsmål) — ei samla, omorganisert fil er
  meir lesbar enn seks spreidde stikkord-tillegg til den opphavlege
  28-linjers strukturen.

## Utført

- `.claude/rules/ci-workflows.md`: fullstendig omskriven — `paths:` utvida
  til `.github/actions/**` (F1), actionlint-scope presisert (F2), ny
  seksjon "DRY-terskel for CI-YAML: 2+, ikkje 3+" (formalisert per
  brukarstadfesting), ny seksjon "Reusable workflows og composite actions
  — kva som IKKJE kan delast" (F3, F4, F5, F6).
- `CLAUDE.md`: DRY-avsnittet fekk ei kort tilvising til CI-YAML-unntaket.
