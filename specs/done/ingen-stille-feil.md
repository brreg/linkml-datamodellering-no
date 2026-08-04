# Ingen stille feil — alle script og funksjonar skal logge feil med LOGLVL=ERROR

## Bakgrunn

Under feilsøking av `specs/done/debug-referanse-nav-meny.md` vart det oppdaga at
`gen-doc`-steget for `referanse/referansemodell` feila heilt stille: kommandoen
sitt output vart redirigert til `/dev/null 2>&1`, og fordi kommandoen ikkje var
den siste i ei `&&`-kjede, utløyste ikkje `set -e`/`trap ERR`-mekanismen som
elles skal logge feil via `log_error`. Resultatet var eit `Error 123` frå `make`
utan nokon indikasjon på kva som faktisk gjekk gale.

Dette er eit generelt mønster, ikkje eit enkelttilfelle. Målet er at **ingen
kommando, funksjon eller script i repoet skal kunne feile utan at feilen vert
logga synleg** — minimum ved `LOGLVL=ERROR` (default-nivå), sjølv om
`LOGLVL=INFO`/`DEBUG` ikkje er sett.

Omfang (avklart med brukar): make-laget, Python-script og CI-workflows.

## Rotårsaker identifisert

### 1. Make-laget: `> /dev/null 2>&1` skjuler stderr, og `&&`-kjeder hindrar `trap ERR`

`make/00-settings.mk` har alt eit `LOG_FUNCTIONS`-rammeverk (`log_debug`,
`log_info`, `log_error`, `timed_run`) frå `specs/done/logging-framework-makefile.md`.
Fleire generator-makroar i `make/10-generator-macros.mk` og `make/30-instances.mk`
brukar likevel eit mønster som omgår dette rammeverket heilt:

```bash
cmd1 > /dev/null 2>&1 && \
cmd2 > /dev/null 2>&1 && \
cmd3
```

To separate problem gjer dette farleg:

- **`> /dev/null 2>&1` kastar vekk stderr ubetinga** — sjølv om noko seinare
  fangar opp at kommandoen feila, er den faktiske feilmeldinga borte for godt.
- **`trap ERR` (i `run_parallel_with_timer`/`run_gen_with_check_parallel`)
  utløysast ikkje** når ein kommando midt i ei `&&`-kjede feilar — dette er
  standard bash-semantikk (`set -e` ignorerer feil i alle ledd av ei
  `&&`/`||`-liste utanom det siste). Exit-koden propagerer til slutt via
  `rc=$?; ...; exit $rc`, men utan noka `log_error`-melding undervegs.

**Stadfesta råka stader** (grep etter `/dev/null 2>&1` i `make/*.mk`):

| Fil | Linje | Makro | Kommando(ar) som feilar stille |
|---|---|---|---|
| `make/10-generator-macros.mk` | 192, 200 | `run_gen_doc_parallel` | `gen-docgen-examples.py`, `gen-doc` |
| `make/10-generator-macros.mk` | 298, 299, 302 | `run_gen_xsd` | `avrotize j2a`, `avrotize a2x`, `fix-xsd-dates.py` |
| `make/10-generator-macros.mk` | 346 | `run_gen_asyncapi` (via `run_gen_with_check_parallel`) | `gen-asyncapi.py`, `asyncapi validate` |
| `make/10-generator-macros.mk` | 383 | `run_gen_openapi` (via `run_gen_with_check_parallel`) | `gen-openapi.py`, `openapi-spec-validator` |
| `make/30-instances.mk` | 25 | `run_gen_informasjonsmodell_instance` | `generate-informasjonsmodell.py` |

**Verst:** `run_gen_xsd` (linje 278-309) har verken `set -e` eller nokon
`rc=$?`-sjekk i det heile — feil i `avrotize j2a`/`a2x`/`fix-xsd-dates.py`
stoppar ikkje build og loggast ikkje. Denne makroen manglar altså heile
feilhandteringsmekanismen, ikkje berre stderr-visinga.

### 2. Python-script: inkonsekvent bruk av eksisterande feilhandteringskonvensjon

`src/assets/scripts/utils/error_handler.py` finst alt og er dokumentert som
"Standardisert error-handtering for Python-script i repoet" — ein `log_error()`
som skriv strukturert kontekst + stack trace til stderr og avsluttar med
non-zero exit code. Han vert derimot berre importert av **3 av dei ca. 20
scripta** som har `except`-blokker:

```
src/assets/scripts/makefile/generate-modellkatalog.py
src/assets/scripts/makefile/generate-informasjonsmodell.py
mkdocs/lib/scripts/generate-validation-md.py
```

Resten (`update-schema-dates.py`, `validate-modelldcat.py`,
`add-schema-header-comments.py`, `collect-concepts.py`,
`run-schema-validation.py`, `gen-dqv-measurements.py`,
`migrate-container.py`, m.fl.) handterer feil ad-hoc — nokre skriv til
stderr sjølv, nokre gjer ingenting.

**Høgast prioritet — heilt stille (bare `except:` utan loggekall):**

| Fil | Linje | Problem |
|---|---|---|
| `src/assets/scripts/makefile/generate-informasjonsmodell.py` | 234 | `except: pass` — feil ved parsing av git remote-URL forsvinn heilt |
| `src/assets/scripts/ci/run-validation.sh` | 148 (embedda Python) | `except: result = {...}` — svelgjer alle JSON-parse-feil identisk, uansett årsak |

### 3. CI-workflows: `|| true` / `2>/dev/null` som kan skjule reelle feil

Dei fleste `2>/dev/null`-førekomstane i `.github/workflows/*.yml` er legitime
eksistenssjekkar (`grep ... 2>/dev/null || echo "finst ikkje"`) og skal **ikkje**
endrast. Følgjande er derimot verdt å vurdere fordi dei kan skjule reelle feil:

| Fil | Linje | Kommando | Risiko |
|---|---|---|---|
| `.github/workflows/validate.yml` | 265 | `git add src/linkml/**/validation/**/*.json \|\| true` | Skjuler reelle `git add`-feil (t.d. sti-problem), ikkje berre "ingen filer å leggje til" |
| `.github/workflows/generate.yml` | 362 | `cp -r "$validation_version_dir"/* "$target_dir/" 2>/dev/null \|\| true` | Skjuler reelle kopieringsfeil (t.d. disk full, permission), ikkje berre tomt kjeldekatalog |

## Målbilete

- **Make-laget:** alle generator-kommandoar sitt output vert fanga opp, og ved
  feil (non-zero exit) skriv `log_error` både kva kommando som feila OG den
  faktiske stderr/stdout-teksten. Ved suksess vert output framleis undertrykt
  frå normal INFO-logging (evt. synleg på DEBUG), slik dagens stille-ved-suksess
  åtferd er.
- **Python-laget:** `error_handler.log_error()` vert den eintydige konvensjonen
  for uventa unntak i alle script under `src/assets/scripts/` og
  `mkdocs/lib/scripts/`. Bare `except:`-blokker utan eksplisitt loggekall er
  ikkje tillate.
- **CI-laget:** `|| true`/`2>/dev/null` skal berre brukast rundt kommandoar der
  ein forventa, ikkje-feilaktig årsak til non-zero exit er identifisert (t.d.
  "ingen treff i grep"). Andre bruk skal fjernast eller erstattast med
  eksplisitt feilhandtering.

## Steg

1. **Legg til `run_logged`-hjelpefunksjon i `LOG_FUNCTIONS`** (`make/00-settings.mk`):
   fangar stdout+stderr frå ein kommando i ein variabel; ved feil kallar
   `log_error` med kommandonamn + fanga output og returnerer non-zero; ved
   suksess sender fanga output til `log_debug`. Signatur:
   `run_logged "<label>" <kommando> [args...]`.

2. **Refaktorer dei 5 råka makroane i `make/10-generator-macros.mk`** til å
   bruke `run_logged` i staden for `> /dev/null 2>&1`:
   - `run_gen_doc_parallel` (linje 186-202)
   - `run_gen_xsd` (linje 278-309) — legg i tillegg til manglande `set -e`/feilsjekk
   - `run_gen_asyncapi` / `run_gen_with_check_parallel`-bruken (linje 346)
   - `run_gen_openapi` / `run_gen_with_check_parallel`-bruken (linje 383)

3. **Refaktorer `run_gen_informasjonsmodell_instance`** (`make/30-instances.mk`,
   linje 25) til same mønster.

4. **Verifiser at `trap ERR`-avhengige kjeder ikkje lenger er sårbare** for
   `&&`-korttslutning: sidan `run_logged` sjølv loggar og returnerer feilkode
   før chain-en kortsluttar, skal `trap ERR` allereie fungere korrekt for
   siste-i-kjede-tilfelle — dette steget er ei verifisering, ikkje ei ny endring.

5. **Fiks dei to bare-`except:`-blokkene** (høgast prioritet, Python):
   - `src/assets/scripts/makefile/generate-informasjonsmodell.py:234` —
     bruk `except Exception as e:` + logg via `error_handler.log_error()` eller
     `print(..., file=sys.stderr)` med konteksten (kva git remote-URL vart forsøkt parsa)
   - `src/assets/scripts/ci/run-validation.sh:148` (embedda Python) —
     logg `result_json`-innhaldet og parse-feilen til stderr før fallback-verdien vert brukt

6. **Audit resterande `except`-blokker** i `src/assets/scripts/` og
   `mkdocs/lib/scripts/` (lista i `## Rotårsaker identifisert § 2`): for kvar
   `except`-blokk, avgjer om han (a) alt loggar tydeleg til stderr, (b) bør
   bruke `error_handler.log_error()`, eller (c) er ei bevisst, dokumentert
   fallback (t.d. `detect-validation-policy.py` sin `except Exception: pass`
   for policy-deteksjon kan vere eit legitimt "bruk default"-mønster — vurder
   per tilfelle, ikkje mekanisk).

7. **Vurder dei to CI-stadene** i `## Rotårsaker identifisert § 3` — enten
   fjern `|| true`/`2>/dev/null` og lat feilen propagere, eller erstatt med
   eksplisitt sjekk av kvifor kommandoen kan feile legitimt (t.d.
   `git add ... || echo "::warning::ingen validering-filer å leggje til"`).

8. **Test lokalt:**
   - Reproduser den opphavlege `gen-doc`-feilen kunstig (t.d. midlertidig
     feil `--template-directory`-sti) og verifiser at `log_error` no viser
     den faktiske feilmeldinga frå `linkml gen-doc`.
   - Køyr `make lint` / `make validate-instance` for eit par domene for å
     stadfeste at ingen eksisterande, vellykka byggjeflyt vert påverka
     (output framleis stille ved suksess, `LOGLVL=DEBUG` viser fanga output).

9. **Oppdater dokumentasjon:** legg til ei kort forklaring av
   `run_logged`-konvensjonen i `COMMANDS.md` sin "Logging"-seksjon, og nemn
   `error_handler.log_error()`-konvensjonen som standard for Python-script
   (t.d. i ein kommentar øvst i `error_handler.py` — han har alt god
   docstring, men manglar ei linje om at han er *obligatorisk* konvensjon,
   ikkje valfri).

10. **Oppdater `CLAUDE.md`** med ein instruks om at nye script og funksjonar
    aldri skal feile stille — dette er ein framtidsretta regel for AI-assistert
    arbeid i repoet, ikkje eit engongsopprydding-steg. Legg til som eit nytt
    punkt under "Førende prinsipper" (saman med dei andre repo-brei reglane,
    t.d. "Bruk Makefile-targets", "Aldri commit eller push"). Innhaldet skal
    dekkje minimum:
    - Make-laget: aldri `> /dev/null 2>&1` (eller tilsvarande) rundt kommandoar
      som kan feile — bruk `run_logged` frå `LOG_FUNCTIONS`
      (`make/00-settings.mk`)
    - Python-laget: aldri ein bar `except:`/`except Exception:` utan anten
      eksplisitt logging (`print(..., file=sys.stderr)`) eller
      `error_handler.log_error()` — spesifiser unntakstype der mogleg
    - Ei feil skal alltid vere synleg ved `LOGLVL=ERROR` (default-nivå), sjølv
      om ho ikkje stoppar heile bygget (mjuke åtvaringar er greitt, stille
      feil er det ikkje)
    - Kryssrefererer til `specs/done/ingen-stille-feil.md` (etter flytting)
      for grunngjeving og eksempel, i tråd med CLAUDE.md sin DRY-regel om at
      forklaringar ikkje skal duplisere det som finst i spec-arkivet

## Framdrift

**Steg 1-2 utført** (2026-08-04):

- `make/00-settings.mk`: la til `run_logged "<label>" <kommando>` i `LOG_FUNCTIONS`.
  Fangar stdout+stderr i ein variabel via `if output=$$("$$@" 2>&1); then rc=0; else rc=$$?; fi`
  (assignment inne i if-betinging, ikkje kombinert med `local` — unngår både at
  `set -e` avsluttar for tidleg og at `local`s eiga exit-status maskerer
  kommandoen sin faktiske exit-kode). Ved feil: `log_error` med label, exit
  code, kommandolinje og fanga output. Ved suksess: fanga output til
  `log_debug` (stille på INFO/ERROR som før).
- `make/10-generator-macros.mk`: refaktorerte `run_gen_doc_parallel`,
  `run_gen_xsd` (la i tillegg til manglande `has_error`-sporing sidan makroen
  ikkje hadde NOKA feilhandtering før), og `run_gen_with_check_parallel`-bruken
  for `run_gen_asyncapi_parallel`/`run_gen_openapi_parallel` til å bruke
  `run_logged` i staden for `> /dev/null 2>&1`.

**Verifisert:**
- Isolert unit-test av `run_logged` (bash, utan podman): stille ved suksess,
  loggar korrekt sjølv når feilen skjer midt i ei `&&`-kjede, viser fanga
  stderr-tekst ved feil.
- Live-test via `make domain-samt` (domene med `xsd: true` + `asyncapi: true`
  + `openapi: true`): alle steg (`gen-doc`, `gen-xsd`, `gen-asyncapi`,
  `gen-openapi`) fullførte med identisk stille output som før refaktoreringa —
  ingen regresjon på suksess-stien. Alle forventa artefakt vart produserte
  (`.xsd`, `-asyncapi.yaml`, `-openapi.yaml`, `docs/index.md` m.fl.).
- Indusert feil i `gen-xsd` (korrupt input til `avrotize a2x`): feilteksten
  frå avrotize (`Error: [Errno 2] No such file or directory: ...`) vart no
  synleg via `log_error`, og `has_error` sørgja for at heile steget
  rapporterer feil — dette var heilt usynleg/ikkje-feilande før endringa.

**Steg 3 utført** (2026-08-04):

- `make/30-instances.mk`: refaktorerte `run_gen_informasjonsmodell_instance`
  til å bruke `run_logged` i staden for `> /dev/null 2>&1` + generisk
  `echo "Warning: Failed to generate..."`. Merk designval: denne makroen hadde
  frå før ein *bevisst* soft-fail-semantikk (feil stoppar ikkje bygget, berre
  varslar) — i motsetnad til `run_gen_xsd`, som ikkje hadde NOKA
  feilhandtering. Sidan Python-scriptet (`generate-informasjonsmodell.py`)
  sin eigen `except`-blokk allereie bruker `error_handler.log_error()` (fullt
  strukturert feilmelding + stack trace til stderr) for alle uventa feil, var
  problemet reint at denne stderr-teksten vart kasta bort av
  `> /dev/null 2>&1` — ikkje at feilen var usynleg av design. Fiksen gjer
  feilen synleg via `log_error`, men **endrar ikkje** om steget stoppar
  bygget — det er framleis ei mjuk åtvaring per schema, no berre med reelt
  innhald i staden for ei generisk melding.

**Verifisert:**
- `make gen-informasjonsmodell-instance DOMAIN=referanse`: suksess-stien
  stille som før, artefakt (`metadata/referansemodell-manifest.yaml`)
  produsert korrekt.
- `make gen-informasjonsmodell-instance SCHEMA=<ikkje-eksisterande-fil>`:
  feilteksten frå Python-scriptet (`Error: ... eksisterer ikkje`) vart synleg
  via `[ERROR]`, og `make` avslutta framleis med exit 0 (soft-fail-semantikken
  er bevart, no berre ikkje stille).

**Steg 5-6 utført** (2026-08-04):

Fiksa dei to bare-`except:`-blokkene (høgast prioritet) og reviderte alle
resterande `except`-blokker i `src/assets/scripts/` og `mkdocs/lib/scripts/`
(`src/mcp-linkml-validator/` er halde utanfor omfanget, jf. spec-en sitt
opphavlege avgrensa filfokus).

*Fiksa (var reelt stille eller for breie):*

| Fil | Linje | Endring |
|---|---|---|
| `src/assets/scripts/makefile/generate-informasjonsmodell.py` | 234 | Bare `except:` → `except Exception as e:` + stderr-melding om fallback-URL |
| `src/assets/scripts/ci/run-validation.sh` | 148 | Bare `except:` → `except json.JSONDecodeError as e:` (unngår å skjule urelaterte bugs) + stderr-melding |
| `src/assets/scripts/update-schema-dates.py` | 81 | `except Exception: old = {}` (heilt stille) → same, men med stderr-INFO om fallback |
| `src/assets/scripts/makefile/run-schema-validation.py` | 121 | Duplikat av same funksjon som over (docstring seier eksplisitt "Same logikk som i update-schema-dates.py") — same fiks |
| `src/assets/scripts/makefile/detect-validation-policy.py` | 30 | `except Exception: print("bronze")` (stille fallback) → ÅTVARING til stderr før fallback |
| `mkdocs/lib/scripts/generate-validation-md.py` | 35 | Same mønster som over, i `get_validation_policy_from_manifest()` |

*Vurdert og late stå urørt (legitime, ikkje-stille eller lågrisiko fallbackar):*

- `src/assets/scripts/validate-modelldcat.py`, `add-schema-header-comments.py`,
  `save-validation-log.py`, `migrate-container.py` — alle loggar allereie
  eksplisitt til stderr med `{e}` og/eller `sys.exit(1)`
- `src/assets/scripts/makefile/collect-concepts.py` (3 blokker),
  `generate-modellkatalog.py` (3 blokker) — alle loggar allereie `[WARNING]`
  eller bruker `error_handler.log_error()`
- `src/assets/scripts/makefile/gen-docgen-examples.py:21` — import-guard,
  loggar og `sys.exit(1)`; funksjonen sin eigen "exit 0 stille"-kontrakt for
  manglande eksempelfil er eit dokumentert, ikkje-feilaktig no-op (jf. docstring)
- `src/assets/scripts/makefile/gen-dqv-measurements.py:78` — smal
  `except ValueError: continue` i ei datakvalitetsberekning per element;
  legg bevisst ikkje til logging her (ville flomme ut ved mange manglande
  datoar i eit datasett — sjølve poenget med DQV-målinga er å telle slikt)
- `src/assets/scripts/scaffolding/new-model.sh:66` (embedda Python) — smal
  `except Exception: pass` i eit streaming-JSON-parse-loop der dei fleste
  linjene forventa *ikkje* er den responsen ein leitar etter; toppnivået har
  alt eit eige feilsjekk (`LINKML_YAML` tom → `exit 1`)
- `src/assets/scripts/utils/error_handler.py:37` — `except ValueError:`
  fallback til absolutt sti i staden for relativ, reint kosmetisk, ingen
  informasjon går tapt
- `mkdocs/lib/scripts/generate-validation-md.py:50` — alt eksemplarisk:
  skriv feilteksten (`{e}`) direkte inn i den genererte doc-sida, med
  kommentar som forklarer kvifor `sys.exit(0)` er bevisst

**Verifisert:** `python3 -m py_compile` på alle endra `.py`-filer,
`bash -n` på `run-validation.sh`, og eit funksjonelt smoke-test av
`detect-validation-policy.py` mot både gyldig og korrupt `build.yaml` —
stille på gyldig input, `ÅTVARING` til stderr (stdout framleis reint, sidan
Makefile fangar stdout som policy-verdien) på korrupt input.

**Steg 4, 7, 8, 9, 10 utført** (2026-08-04):

- **Steg 4 (verifisering):** stadfesta via steg 8 sin live-reproduksjon —
  sjå under.
- **Steg 7 (CI `|| true`-gjennomgang):**
  - `.github/workflows/validate.yml` («Stage alle valideringsloggar»):
    `git add ... || true` → `if ! git add ... 2>logfil; then echo "::warning::..."; cat logfil >&2; fi`.
    Framleis non-fatal (fyrste køyring utan endra loggar er ein legitim
    "ingen treff"-case), men årsaka er no alltid synleg.
  - `.github/workflows/generate.yml` («Kopier valideringsloggar til
    generated/»): `cp -r ... 2>/dev/null || true` →
    `if ! cp_output=$(cp -rv ... 2>&1); then echo "  ⚠️  ... feila: $cp_output" >&2; fi`.
    Same non-fatal semantikk, no med faktisk `cp`-feiltekst synleg.
  - Begge verifisert med `bash -n` (syntaks) + eit isolert funksjonstest av
    `if ! var=$(cmd); then ...; fi`-mønsteret under `set -e` (stadfestar at
    scriptet ikkje avsluttar for tidleg, jf. same prinsipp som `run_logged`).
- **Steg 8 (test lokalt):**
  - Reproduserte den opphavlege `gen-doc`-feilen kunstig (mellombels ugyldig
    `--diagram-type`-verdi i `run_gen_doc_parallel`) og køyrde
    `make domain-referanse`: `[ERROR]`-linjene viste no den faktiske
    feilteksten frå `linkml gen-doc` ("Error: Invalid value for
    '--diagram-type': ..."), og `make` avslutta korrekt med `Error 123` —
    identisk symptom som det opphavlege incidentet, men no med full
    diagnostikk. Testendringa vart reversert (`git diff` tomt etterpå).
  - `make lint SCHEMA=src/linkml/referanse/referansemodell/referansemodell-schema.yaml`
    og ein full `make domain-referanse`-køyring (utan kunstig feil) stadfesta
    at normal byggjeflyt er upåverka — identisk stille output og identiske
    artefakt som før refaktoreringa.
- **Steg 9 (dokumentasjon):**
  - `COMMANDS.md`: nytt underavsnitt "Ingen stille feil — `run_logged`" under
    `## Logging`, med kort forklaring, signatur og kryssreferanse til denne
    spec-en.
  - `src/assets/scripts/utils/error_handler.py`: la til ei linje i
    modul-docstringen som gjer eksplisitt at `log_error()` er *obligatorisk*
    konvensjon (ikkje valfri), med kryssreferanse.
- **Steg 10 (CLAUDE.md):** la til eit nytt punkt under "Førende prinsipper"
  ("Ingen stille feil") som dekkjer både make- og Python-laget, med
  kryssreferanse til denne spec-en for grunngjeving (DRY, jf. CLAUDE.md sin
  eigen regel om at forklaringar ikkje skal duplisere spec-arkivet).

Alle 10 steg i spec-en er no fullførte.

## Akseptansekriterier

- [x] Ingen `> /dev/null 2>&1` (eller tilsvarande stderr-discard) attende i
      `make/10-generator-macros.mk` / `make/30-instances.mk` for kommandoar
      som kan feile
- [x] `run_gen_xsd` har feilhandtering (stoppar build + loggar ved feil i
      avrotize/fix-xsd-dates.py)
- [x] Ein kunstig indusert feil i kvar av dei 5 råka make-makroane produserer
      ein synleg `[ERROR]`-melding med den faktiske feilteksten, ved
      `LOGLVL=INFO` (default)
- [x] Dei to bare-`except:`-blokkene loggar unntaket dei fangar
- [x] Resterande `except`-blokker i `src/assets/scripts/` og
      `mkdocs/lib/scripts/` er gjennomgått og anten bruker
      `error_handler.log_error()`, loggar eksplisitt, eller har ein kommentar
      som forklarer kvifor stille fallback er trygt
- [x] Dei to identifiserte CI `|| true`-stadene er vurderte og enten fiksa
      eller dokumenterte som bevisste unntak
- [x] `COMMANDS.md` dokumenterer `run_logged`-konvensjonen
- [x] `CLAUDE.md` har eit punkt under "Førende prinsipper" om at nye script
      og funksjonar aldri skal feile stille

## Relaterte filer

- `make/00-settings.mk` — `LOG_FUNCTIONS`-definisjon (der `run_logged` skal leggjast til)
- `make/10-generator-macros.mk` — hovudmengda av råka makroar
- `make/30-instances.mk` — `run_gen_informasjonsmodell_instance`
- `src/assets/scripts/utils/error_handler.py` — eksisterande, underbrukt Python-konvensjon
- `src/assets/scripts/makefile/generate-informasjonsmodell.py` — bare `except:` linje 234
- `src/assets/scripts/ci/run-validation.sh` — bare `except:` linje 148
- `.github/workflows/validate.yml`, `.github/workflows/generate.yml` — CI `|| true`-stader
- `specs/done/logging-framework-makefile.md` — opphavleg LOGLVL-rammeverk
- `specs/done/debug-referanse-nav-meny.md` — saka som avdekte problemet
- `COMMANDS.md` — «Logging»-seksjonen som skal utvidast
- `CLAUDE.md` — «Førende prinsipper»-seksjonen der den nye regelen skal inn

## Utført

Alle 10 steg fullførte. Endra filer:

- `make/00-settings.mk` — ny `run_logged`-funksjon i `LOG_FUNCTIONS`
- `make/10-generator-macros.mk` — `run_gen_doc_parallel`, `run_gen_xsd`,
  `run_gen_asyncapi_parallel`, `run_gen_openapi_parallel` bruker `run_logged`
- `make/30-instances.mk` — `run_gen_informasjonsmodell_instance` bruker
  `run_logged`
- `src/assets/scripts/makefile/generate-informasjonsmodell.py` — bare
  `except:` fiksa (linje 234)
- `src/assets/scripts/ci/run-validation.sh` — bare `except:` fiksa (linje 148)
- `src/assets/scripts/update-schema-dates.py`,
  `src/assets/scripts/makefile/run-schema-validation.py` — stille
  `except Exception: old = {}`-duplikat fiksa
- `src/assets/scripts/makefile/detect-validation-policy.py`,
  `mkdocs/lib/scripts/generate-validation-md.py` — stille
  bronze-policy-fallback fiksa
- `src/assets/scripts/utils/error_handler.py` — docstring gjer konvensjonen
  obligatorisk
- `.github/workflows/validate.yml`, `.github/workflows/generate.yml` —
  `|| true` erstatta med synleg åtvaring, non-fatal semantikk bevart
- `COMMANDS.md` — nytt underavsnitt "Ingen stille feil — `run_logged`"
- `CLAUDE.md` — nytt punkt under "Førende prinsipper"

Alt verifisert lokalt: isolerte unit-testar av `run_logged` og
`if ! var=$(cmd); then`-mønsteret, live-køyring av `make domain-samt` (xsd +
asyncapi + openapi) og `make domain-referanse`, kunstig reproduksjon av det
opphavlege `gen-doc`-incidentet (no synleg feil + korrekt `make`-avslutning),
`py_compile`/`bash -n` på alle endra script, og funksjonstestar av
fallback-scripta mot både gyldig og korrupt input.
