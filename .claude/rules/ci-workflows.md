---
name: ci-workflows
description: Actionlint-plikta, CI-YAML sin lægre DRY-terskel (2+), og reusable workflow/composite action-avgrensingar. Lastast automatisk ved arbeid med filer under .github/workflows/ eller .github/actions/.
paths:
  - ".github/workflows/**"
  - ".github/actions/**"
---

## Actionlint etter CI-endring

Etter *kvar* endring i `.github/workflows/*.yml` skal `actionlint` køyrast
mot den endra fila før arbeidet vert rekna som ferdig.

GitHub Actions evaluerer `${{ }}`-uttrykk overalt i eit `run:`-steg — også
inni kommentarar — så eit bokstaveleg tomt `${{ }}` eller anna ugyldig
uttrykk får heile workflowen til å feile ved parse-tid, utan at éin einaste
jobb køyrer (synest som ei 0-sekunds "workflow file issue"-feiling i
Actions-historikken).

Køyr via podman, aldri lokal installasjon:

```bash
podman run --rm -v "$(pwd)":/repo:ro -w /repo docker.io/rhysd/actionlint:latest -color .github/workflows/<fil>.yml
```

**Kva blokkerer:** berre feil av typen `[expression]` (og andre reelle
syntaks-/schemafeil) blokkerer arbeidet. `[shellcheck]`-funn er stilråd og
treng ikkje rettast som del av same endring.

**Gjeld berre `.github/workflows/*.yml`.** `actionlint` tolkar ei
`.github/actions/*/action.yml`-fil som ein workflow (krev `jobs:`/`on:`)
og gir falske "unexpected key"/"section is missing"-feil dersom han
køyrast mot ei composite action-fil. Valider action.yml-filer med rein
YAML-syntakssjekk i staden:

```bash
python3 -c "import yaml; yaml.safe_load(open('.github/actions/<namn>/action.yml')); print('OK')"
```

## DRY-terskel for CI-YAML: 2+, ikkje 3+

CLAUDE.md sin generelle DRY-terskel (tre eller fleire identiske tilfelle)
gjeld **ikkje** for `.github/workflows/**`/`.github/actions/**`. Her er
terskelen **2 eller fleire** stader med same/liknande kode.

**Grunngjeving:** duplisert YAML her har vist seg å drive frå kvarandre
stille, utan at nokon merkar det før noko faktisk feilar i CI. Sjå P3 i
`specs/done/evaluering-gjentakande-monster-backlog.md`: ein
cache-nøkkel-formel meint å vere byte-for-byte identisk i to workflow-
filer dreiv frå kvarandre etter at berre den eine vart fiksa — braut
cross-workflow-cache-delinga umerkt, ingen feilmelding, berre stille
dårlegare yting. Full kartlegging av kva som faktisk vart trekt ut ved
denne terskelen (composite actions + éin intern reusable workflow) står i
`specs/done/evaluering-dry-github-workflows.md`.

## Reusable workflows og composite actions — kva som IKKJE kan delast

### Kallejobba til ein reusable workflow treng eksplisitte permissions

GITHUB_TOKEN sine faktiske permissions i ein kalla reusable workflow
(`uses: ./.github/workflows/X.yml`) er det **mest restriktive** av kva
kallejobben deklarerer OG kva den kalla workflowen sine eigne jobbar
deklarerer. Ei kallejobb utan eksplisitt `permissions:`-block kan difor
stille nedskalere det den kalla workflowen faktisk treng (t.d.
`packages: write` for GHCR-push) — ein feil som verken `actionlint` eller
YAML-syntakssjekk fangar, og som først syner seg ved faktisk CI-køyring.

**Regel:** ei kallejobb til ein intern reusable workflow skal alltid ha
eit eksplisitt `permissions:`-block som minst dekker det den kalla
workflowen sine jobbar treng.

### Reusable workflow-jobbar har fast steg-sekvens

Ein jobb definert inni ein reusable workflow (`on.workflow_call`) kan
**ikkje** ta imot ekstra steg injisert frå kallaren. Før du trekk ut ein
jobb til ein reusable workflow: sjekk om ALLE kallarar faktisk har
identisk steg-sekvens. Kallar-spesifikke ekstra steg må anten
parametriserast (input-styrt `if:` på eit steg INNI den delte jobben,
jf. `prepare-podman` sitt `images != ''`-mønster) eller flyttast til ein
separat jobb hos kvar kallar — dei kan ikkje "setjast inn" i den delte
jobben frå kallaren.

### Composite actions kan ikkje lese kallaren sin steps.*-kontekst

Ein composite action kan gate sine EIGNE interne steg via input-verdiar
(`if: inputs.X != ''`), men kan ikkje lese kallaren sin
`steps.<id>.outputs.*`. Ei cache-hit-vakt må difor liggje på
**kallesteget** (`if: steps.cache-id.outputs.cache-hit != 'true'` på
sjølve `uses: ./.github/actions/X`-linja), ikkje inni actionen.

### To kategoriar reusable workflows — ikkje forveksle

- `reusable-generate.yml`/`reusable-validate.yml` er **public API for
  eksterne repo** (workflow_call med `schema:`-input for validering/
  generering av eitt enkelt skjema) — ikkje interne DRY-verktøy. Endringar
  her er ei API-endring for andre repo.
- `reusable-oppsett.yml` er eit **internt DRY-verktøy** (deler
  `checkout-source`+`ensure-images`), kalla berre av
  `generate.yml`/`lenkje-og-mermaid-sjekk.yml`/`validate.yml` i dette same
  repoet.
