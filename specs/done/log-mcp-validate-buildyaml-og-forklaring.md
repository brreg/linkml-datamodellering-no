# Plan: `log-mcp-validate` — `MANIFEST` → `BUILDYAML` + forklarande skildring

## Bakgrunn

Oppfølging av [[log-mcp-validate-alternasjon-notasjon]]. Brukaren forstod
ikkje skilnaden mellom `MANIFEST=`/`SCHEMA=`+`POLICY=` for
`make log-mcp-validate`. Etter forklaring bad brukaren om to tiltak:

1. Legg forklaringa til i `COMMANDS.md` sin skildringstekst
2. Byt om `MANIFEST`-argumentet til `BUILDYAML`, sidan det peikar direkte
   på filnamnet (`build.yaml`) i staden for det meir abstrakte
   «manifest»-omgrepet

**Den faktiske skilnaden** (verifisert mot
`src/assets/scripts/makefile/run-validation.sh`):

| | `SCHEMA=<sti> POLICY=<policy>` | `BUILDYAML=<sti>` (i dag: `MANIFEST`) |
|---|---|---|
| Du oppgir | Sti til `*-schema.yaml` + policy eksplisitt | Berre sti til `build.yaml` |
| Policy | Det du skreiv på kommandolinja — **overstyrer** `build.yaml` | Lest automatisk frå `validation_policy:`-feltet i `build.yaml` |
| Schema-sti | Det du skreiv | Utleia automatisk frå katalognamn (`<katalog>/build.yaml` → `<katalog>/<katalog>-schema.yaml`) |
| Bruk når | Du vil teste mot ein **annan** policy enn den konfigurerte | Du vil validere modellen **slik han faktisk er konfigurert** — same som CI ville brukt |

## Plan

### 1 — Rename `MANIFEST` → `BUILDYAML` (berre make-nivå-argumentet)

`MANIFEST` er berre brukt som make-argument på **éin** stad
(`log-mcp-validate` i `make/40-validation.mk`). Renamen er difor trygt
avgrensa til den eine oppskrifta:

- `## `-kommentar: `MANIFEST=<sti>` → `BUILDYAML=<sti>`
- `if [ -n "$(MANIFEST)" ]` → `if [ -n "$(BUILDYAML)" ]`
- `--manifest $(MANIFEST)` → `--manifest $(BUILDYAML)` (sjølve
  `run-validation.sh` sitt `--manifest`-flagg vert **ikkje** endra — det
  er eit internt skript-flagg, ikkje eksponert direkte som eit
  `make ARG=`-namn, og brukt av fleire CI-kall (`generate.yml`,
  `validate.yml`) utanfor denne targeten sitt omfang)
- `log_error`-meldinga: `MANIFEST=<sti>` → `BUILDYAML=<sti>`

**Utanfor omfang:** CI-workflowane sine eigne, interne bash-variablar
(`MANIFEST`/`MANIFESTS` i `generate.yml`/`validate.yml`) og
`run-validation.sh` sitt `--manifest`-flagg. Desse er implementasjonsdetaljar
på eit anna nivå enn `make`-brukargrensesnittet, og heiter noko anna av
gode grunnar der (skriptet sitt eige, stabile CLI-kontrakt).

### 2 — Utvid skildringa i `COMMANDS.md`

Legg til ei kort forklaring av skilnaden i skildringscella for
`log-mcp-validate`-raden, basert på tabellen over.

## Filer som vert påverka

- `make/40-validation.mk`
- `COMMANDS.md`

## Handlingsliste

1. [x] Rename `MANIFEST` → `BUILDYAML` i `log-mcp-validate` (## kommentar,
   `if`-sjekk, `--manifest`-kall, `log_error`)
2. [x] Utvid `COMMANDS.md` sin skildringstekst med forklaringa
3. [x] Verifiser med `make help` og ein reell køyring
   (`make log-mcp-validate BUILDYAML=<sti-til-build.yaml>`)

## Utført

`make/40-validation.mk`: `MANIFEST` → `BUILDYAML` i `log-mcp-validate`
(## kommentar, `if`-sjekk, `log_error`) — `run-validation.sh` sitt eige
`--manifest`-flagg er urørt (internt skript-kontrakt, brukt av
`generate.yml`/`validate.yml` òg, utanfor denne renamen sitt omfang).

`COMMANDS.md`: skildringa for `log-mcp-validate` utvida med forklaring av
dei to kallmåtane (`SCHEMA=`+`POLICY=` = eksplisitt/overstyrande,
`BUILDYAML=` = automatisk utleia frå `build.yaml`, same som CI).

**Verifisert:** `make help` viser `(BUILDYAML=<sti>|SCHEMA=<sti> POLICY=<policy>)`.
Reell køyring `make log-mcp-validate BUILDYAML=src/linkml/samt/samt-bu/build.yaml`
validerte korrekt — slo automatisk opp `silver`-policyen frå `build.yaml`
og skreiv `validation/1.10.0/silver.json`.
