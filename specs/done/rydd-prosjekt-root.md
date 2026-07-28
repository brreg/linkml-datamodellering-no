# Rydd prosjekt-root

## Bakgrunn

Prosjekt-root inneheld fleire lowercase-filer som kan flyttast til meir passande katalogar for å redusere rot. Filer med uppercase-namn (t.d. `README.md`, `CLAUDE.md`, `LICENSE`) skal bli liggande på root per konvensjon.

## Kandidatar for flytting

| Fil | Type | Funksjon | Foreslått plassering |
|-----|------|----------|----------------------|
| `bootstrap.sh` | Bash-script | Bootstrap-script for eksterne repo | `src/assets/scripts/` |
| `config.mk` | Generert Make-konfig | Autogenerert frå `build.yaml`-filer | `generated/` (eller behald på root) |
| `release-please-config.json` | JSON-konfig | Release Please-konfigurasjon | `.github/` |
| `renovate.json` | JSON-konfig | Renovate-konfigurasjon | `.github/` |
| `validation-test.json` | JSON test-output | Testdata for validering | `tests/fixtures/` eller slett dersom utdatert |
| `validation-test-v2.json` | JSON test-output | Testdata for validering (v2) | `tests/fixtures/` eller slett dersom utdatert |

## Analyse per fil

### `bootstrap.sh`
- **Funksjon:** Bootstrap-script som eksterne repo kan køyre for å leggje til LinkML-støtte
- **Referert frå:** `README.md` (curl-kommando)
- **Vurdering:** Kan flyttast til `src/assets/scripts/bootstrap.sh`, men krev oppdatering av curl-URL i README og potensielt i ekstern dokumentasjon. **Risiko:** breaking change for brukarar som har hardkoda URL-en.
- **Anbefaling:** **Behald på root** — URL-stabilitet er viktigare enn opprydding.

### `config.mk`
- **Funksjon:** Autogenerert Make-konfig som Makefile inkluderer (`-include config.mk`)
- **Generert av:** `src/assets/scripts/makefile/gen-config.sh`
- **Referert frå:** `Makefile` (linje 1)
- **Vurdering:** Generert artefakt, men Makefile forventar den på root. Kan flyttast til `generated/config.mk`, men krev endring i Makefile.
- **Anbefaling:** **Behald på root** — enklare enn å endre Makefile-logikk.

### `release-please-config.json`
- **Funksjon:** Konfigurasjon for Release Please GitHub Action
- **Referert frå:** `.github/workflows/release-please.yml`
- **Vurdering:** Kan flyttast til `.github/release-please-config.json` og oppdatere workflow-referansen.
- **Anbefaling:** **Flytt til `.github/`** — logisk plassering saman med andre GitHub-konfigurasjonar.

### `renovate.json`
- **Funksjon:** Konfigurasjon for Renovate bot
- **Referert frå:** Renovate leitar etter fila i root per konvensjon
- **Vurdering:** Renovate støttar `.github/renovate.json`, men root er meir standard.
- **Anbefaling:** **Kan flyttast til `.github/`** dersom ønskt, men ikkje kritisk.

### `validation-test.json` og `validation-test-v2.json`
- **Funksjon:** JSON-filer med valideringsresultat (testdata)
- **Referert frå:** Ingen funne referansar i Makefile, CI eller dokumentasjon
- **Vurdering:** Ser ut til å vere gamle testfiler eller manuelt genererte valideringsoutput. Kan flyttast til `tests/fixtures/` eller slettast dersom dei ikkje er i bruk.
- **Anbefaling:** **Slett** dersom dei ikkje er refererte i testar — eller **flytt til `tests/fixtures/`** dersom dei har verdi som testdata.

## Tiltak

1. **Flytt `release-please-config.json` til `.github/`**
   - [x] Flytt `release-please-config.json` → `.github/release-please-config.json`
   - [x] Oppdater `.github/workflows/release-please.yml`: `config-file: release-please-config.json` → `config-file: .github/release-please-config.json`

2. **Vurder flytting av `renovate.json` til `.github/`** (valfritt)
   - [x] Flytt `renovate.json` → `.github/renovate.json`
   - [x] Verifiser at Renovate finn ny plassering (Renovate søker i både root og `.github/`)

3. **Slett eller flytt `validation-test*.json`**
   - [x] Sjekk om `validation-test.json` og `validation-test-v2.json` er refererte i testar
   - [x] Dersom **ikkje i bruk**: slett begge filene
   - ~~Dersom **i bruk**: flytt til `tests/fixtures/validation-test.json` og `tests/fixtures/validation-test-v2.json`~~
   - **Resultat:** Ingen referansar funne — begge filene sletta

4. **Behald `bootstrap.sh` og `config.mk` på root**
   - Ingen handling — desse blir liggande av grunnar gitt over

## Forventa resultat

Etter gjennomføring:
- Færre filer på root (2-4 færre lowercase-filer)
- GitHub-konfigurasjonar samla i `.github/`
- Ingen breaking changes for eksterne brukarar av `bootstrap.sh`
- Makefile fungerer som før

## Utført

Alle tre tiltak er gjennomførte, pluss ei ekstra fil:

1. ✅ `release-please-config.json` flytta til `.github/` med oppdatert workflow-referanse
2. ✅ `renovate.json` flytta til `.github/`
3. ✅ `validation-test.json` og `validation-test-v2.json` sletta (ingen referansar funne)
4. ✅ `.release-please-manifest.json` flytta til `.github/` (same kategori som config-fila, 3 referansar i workflow oppdaterte)

**Resultat:** Prosjekt-root har no 5 færre filer (4 lowercase + 1 dotfil). Gjenverande lowercase-filer på root:
- `bootstrap.sh` (må bli liggande — URL-stabilitet)
- `config.mk` (må bli liggande — Makefile-avhengigheit)
- `bugs/`, `generated/`, `mkdocs/`, `specs/`, `src/`, `tests/` (katalogar)
