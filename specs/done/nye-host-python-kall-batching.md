# Nye direkte python3-kall på host (batching- og loggkopi-regresjon)

## Bakgrunn

`specs/done/containerisering-python-kall.md` (lukka 2026-07-30) fjerna alle
direkte `python3`/`python -c`-kall på hosten frå `Makefile` (den gongen éin
samla fil, seinare delt i `make/*.mk`). Sluttresultatet var dokumentert som
**"Gjennverande direkte host-Python-kall i Makefile: Ingen"** — alle
make-targets brukte `$(PYTHON_RUN)` eller `$(LINKML_RUN)`. To lågprioriterte,
eksplisitt aksepterte unntak stod att: `mkdocs/publish.sh` (og `mkdocs/lib/`,
som var ein del av same publiseringsskript-familie før og etter spec-en) og
`tests/test_make.sh`, båe grunngjevne med at dei køyrer sjeldan/aldri i CI.

Denne spec-en dokumenterer funn frå ein etterfølgjande gjennomgang
(2026-08-09) av heile repoet for å avdekkje om det har kome **nye** direkte
host-`python3`-kall sidan den spec-en vart lukka — dvs. kall introdusert av
seinare arbeid som ikkje har vore gjennom same containeriserings-vurdering.
Undersøkinga vart gjort ved å grep etter `python3 ` repo-breitt og
kryssjekke kvart treff mot `git log -S`/`git log --diff-filter=A` for å
skilje reelt nye kall frå filomorganiseringar/omdøypingar (som t.d.
`src/assets/scripts/scaffolding/new-modell.sh`, som berre vart flytta/omdøypt
2026-08-06, ikkje endra i innhald).

**Scope-korrigering (2026-08-09, etter tilbakemelding frå brukar):**
`mkdocs/publish.sh` og `mkdocs/lib/` vart først handsama som "allereie
aksepterte unntak, ikkje del av denne spec-en sitt omfang" (jf. den no
fjerna seksjonen under). Dette var feil av to grunnar:

1. **Brukar har eksplisitt bede om at desse takast inn i omfanget** for denne
   spec-en, uavhengig av om kalla er "nye" eller ikkje.
2. **Grunngjevinga for det opphavlege unntaket held ikkje ved nærare ettersyn:**
   containeriserings-spec-en (2026-07-30) skreiv at `mkdocs/publish.sh`
   "køyrer berre ved manuell publisering (ikkje i CI)". Dette var **alt feil
   då det vart skrive** — `make docs-publish` (då `make publish`) har vore
   kalla frå `.github/workflows/generate.yml` sidan det aller første
   CI-oppsettet (commit `5e9d088c`, 2026-05-19), lenge før containeriserings-
   spec-en vart skriven. `mkdocs/publish.sh`/`mkdocs/lib/` sine `python3`-kall
   køyrer difor på **kvar einaste** `generate.yml`-køyring, akkurat som funn 2
   under — dei høyrer ikkje heime i "køyrer sjeldan/aldri i CI"-kategorien
   saman med `tests/test_make.sh`.

Sjå funn 3 under for full katalogisering av `mkdocs/publish.sh`/`mkdocs/lib/`
sine `python3`-kall.

Tre reelt relevante, ikkje-containeriserte host-`python3`-kall-grupper vart
stadfesta:

## Funn

### 1. `make/40-validation.mk` — `batch-flatten-and-validate.py` kalla bart på host

**Introdusert:** commit `29fd231c` (2026-08-07,
"perf(mcp-linkml-validator): batch skjemavalidering til éin kontainar per
domene" — same batching-arbeid som `specs/done/stille-feil-batching-regresjon.md`
allereie har fiksa logging-sida av).

**Stader:** `make/40-validation.mk:56` (`validate-bronze`) og `:110`
(`validate-data`):

```make
run_logged "batch-flatten-and-validate/bronze $(DOMAIN)" python3 src/mcp-linkml-validator/batch-flatten-and-validate.py --policy bronze \
	--output-dir "$$BATCH_DIR" $$SCHEMA_LIST; \
```

(`run_logged`-innpakninga vart lagt til av `stille-feil-batching-regresjon.md`
— sjølve `python3`-kallet var bart før og etter den fiksen, sidan det spec-en
løyste var manglande feillogging, ikkje manglande containerisering.)

**Problem:** `batch-flatten-and-validate.py` gjer `import yaml` og
`import subprocess` på toppnivå og les/parsar skjema-YAML direkte på hosten
(m.a. `schema_has_tree_root()`, som brukar `yaml.safe_load` på skjemafila) før
han til slutt kallar `subprocess.run(["podman", "run", ...])` for sjølve
valideringa. Dette krev at hosten har `python3` + `PyYAML` installert — nett
den typen lokale avhengigheit CLAUDE.md sitt førande prinsipp ("Ingen
avhengigheter skal installeres lokalt... Alt skal kjøres som containere med
podman i WSL2") og den lukka containeriserings-spec-en eksplisitt fjerna frå
`make/40-validation.mk`.

**Kontekst — ikkje eit heilt nytt arkitekturmønster:** før batching-endringa
kalla dei same to targeta `bash src/mcp-linkml-validator/flatten-and-validate.bash`
bart på host — også eit ikkje-containerisert orkestreringskall, men eit reint
bash-script utan Python-avhengigheiter (det kalla berre vidare til
`podman run` for validatoren). Batching-omskrivinga bytte dette ut med eit
Python-script som **sjølv** treng eit host-Python-miljø med `PyYAML` for å
gjere YAML-parsinga si eiga logikk (tree_root-sjekk, jobs-parsing) — dette er
den reelle regresjonen: ikkje at orkestrering skjer på host (det gjorde det
òg før), men at orkestreringsscriptet no har ein eigen, ny host-Python-
avhengigheit (`PyYAML`) som ikkje fanst i `flatten-and-validate.bash`.

### 2. `.github/workflows/generate.yml:308` — bart `python3 -c` på GitHub-runner

**Introdusert:** commit `9bccd191` (2026-08-01, "fix(ci): valider alle skjema
i nattleg jobb og kopier kun siste versjon av loggar") — **éin dag etter** at
containeriserings-spec-en vart lukka.

```bash
version=$(python3 -c "import yaml; print(yaml.safe_load(open('$schema_file')).get('version', ''))" 2>/dev/null || echo "")
```

**Problem:** Dette er nøyaktig det containeriserings-spec-en sitt
opphavlege føremål retta seg mot — sitatet frå spec-en: "Målet er å fjerne
direkte kall til `python3` og `python` frå **GitHub-runneren**/hosten." Steget
("Kopier valideringsloggar til generated/") køyrer på **kvar einaste**
`generate.yml`-køyring (ikkje betinga av `if: cache-hit != 'true'`-unntaket
åleine — det gjeld når cache IKKJE traff, som er normalfallet for endra
skjema), i motsetnad til `tests/test_make.sh`, som eksplisitt vart akseptert
som unntak fordi det "køyrer sjeldan i CI". Det finst ingen `setup-python`-
steg i `generate.yml`, så kallet er avhengig av kva `python3`/`PyYAML`-versjon
som tilfeldigvis følgjer med GitHub sitt `ubuntu-latest`-runnerbilete — usett
og upinna, nøyaktig risikoen spec-en åtvara mot ("Meir deterministisk CI —
same Python-image lokalt og i CI").

### 3. `mkdocs/publish.sh` + `mkdocs/lib/` — heile dokumentasjonspipelinen

**Ikkje nytt i tid** (kalla fanst alt før `mkdocs/lib/`-katalogen vart
oppretta 2026-07-06, altså før containeriserings-spec-en vart lukka), men
**feilaktig ekskludert** frå det opphavlege unntaket sin grunngjeving (sjå
scope-korrigeringa i `## Bakgrunn`) — teke inn i omfanget for denne spec-en
på eksplisitt førespurnad frå brukar. `make docs-publish` køyrer via
`.github/workflows/generate.yml:438` (med `trap ERR` — ein feil her stoppar
CI-bygget) på kvar einaste `generate`-køyring, ikkje berre ved manuell
publisering.

**Full katalogisering** (17 kallstader i 9 filer). Delt i to grupper etter
avhengigheit:

**Gruppe A — krev `PyYAML` på hosten (13 kallstader, høgast prioritet):**

| Fil:linje | Føremål |
|---|---|
| `mkdocs/publish.sh:55` | Heredoc — parse CODEOWNERS.md YAML-frontmatter, match `schema_path` mot `path_patterns` for utgjevar-org |
| `mkdocs/publish.sh:254` | Les `submodels`-liste frå eit skjema sin `build.yaml` |
| `mkdocs/lib/sections/kontakt.sh:29` | Heredoc — same CODEOWNERS-YAML-parsing som publish.sh:55, utvida med `catalog_slug`-matching |
| `mkdocs/lib/sections/badges.sh:26` | Heredoc — same CODEOWNERS-YAML-parsing igjen, tredje variant (direkte `org_uri`-match) |
| `mkdocs/lib/sections/delmodellar.sh:37` | Les `title`/`name` frå hovudmodellen sitt skjema |
| `mkdocs/lib/sections/delmodellar.sh:70` | Les `title`/`name` frå ein delmodell sitt skjema |
| `mkdocs/lib/sections/delmodellar.sh:73` | Les `description` frå ein delmodell sitt skjema |
| `mkdocs/lib/sections/kom_i_gang.sh:19` | Les `version`-felt frå skjema |
| `mkdocs/lib/sections/kom_i_gang.sh:31` | Heredoc — les skjema + `build.yaml`, ekstraherer eksempel-klasse/-variabel/policy |
| `mkdocs/lib/utils/metadata_parsers.sh:24` (`load_manifest_cache`) | Les `validation_policy`/`external_spec_url`/`external_spec_label` frå `build.yaml` i éin kombinert prosess |
| `mkdocs/lib/utils/metadata_parsers.sh:55` (`get_validation_policy`) | Fallback-kall når cache ikkje er lasta |
| `mkdocs/lib/utils/metadata_parsers.sh:76` (`get_external_spec_url`) | Same fallback-mønster |
| `mkdocs/lib/utils/metadata_parsers.sh:86` (`get_external_spec_label`) | Same fallback-mønster |

**Merk — DRY-observasjon:** dei tre CODEOWNERS-YAML-parsing-heredocane
(`publish.sh:55`, `kontakt.sh:29`, `badges.sh:26`) er ~80 % identisk kode
(les frontmatter, `re.search`-ekstraksjon, `yaml.safe_load`, loop over
`organizations`) med små variasjonar i matching-logikk. Dette møter CLAUDE.md
sin DRY-terskel ("tre eller fleire identiske tilfelle") og er verdt å
konsolidere til eitt delt script uavhengig av containeriserings-spørsmålet —
sjå steg 7.

**Gruppe B — berre standardbibliotek (`json`/`re`/`pathlib`), ingen `PyYAML`
(4 kallstader, lågare prioritet):**

| Fil:linje | Føremål |
|---|---|
| `mkdocs/lib/sections/badges.sh:58` | Les `errorCount` frå validerings-JSON (berre `json`-modulen) |
| `mkdocs/lib/sections/avhengigheiter.sh:107` | Kallar `mkdocs/lib/scripts/parse-dependency-tree.py` (stdlib-only) |
| `mkdocs/lib/utils/imported_schemas.sh:57` | Same script, `--format flat` |
| `mkdocs/lib/sections/valideringsresultat.sh:19` | Kallar `mkdocs/lib/scripts/generate-validation-md.py` (stdlib `json` + lokal `utils.error_handler`-modul) |

Gruppe B krev ikkje tredjeparts-pakkar (berre Python 3 sjølv), så desse er
mindre risikable enn gruppe A, men er framleis bare host-kall utan
containerinnpakking, i strid med CLAUDE.md sitt førande prinsipp.

## Vurdert og stadfesta ikkje nytt (falske positivar frå grep)

Fylgjande vart òg funne ved grep, men stadfesta via `git log --diff-filter=A`/
`--follow` å vere anten filomorganiseringar (ikkje nytt innhald) eller allereie
eksplisitt aksepterte unntak (og framleis rimeleg å halde utanfor, i motsetnad
til `mkdocs/publish.sh`/`mkdocs/lib/` over, sidan grunngjevinga for desse
faktisk held):

- `tests/test_make.sh` — alle bare python3-kall (inkl. dei nye
  `batch-lint.py`/`batch-convert.py`/`batch-linkml-validate.py`/
  `batch-validate-instances.py`-kalla frå batching-arbeidet) fell inn under
  det same, allereie aksepterte "køyrer sjeldan i CI"-unntaket.
- `src/assets/scripts/scaffolding/new-modell.sh`,
  `src/assets/scripts/migreringsscript/migrate-schema-metadata.sh`,
  `src/assets/scripts/scaffolding/new-modellkatalog.sh` — nyare
  filstidsstempel (2026-07-31/08-06) skuldast reine omdøypings-/
  reorganiseringscommits (`refactor(scripts): organiser script i logiske
  underkatalogar`, `omdøyp new-model`), stadfesta via `git log --follow` at
  dei bare python3-kalla i desse fanst frå før (opphav heilt attende til
  2026-05).
- `make/60-mcp.mk:36` (`python3 /work/tests/test_mcp_policies.py -v`) — dette
  er sjølve *entrypoint-kommandoen* inne i eit `podman run --rm ... $(MCP_IMAGE)
  python3 ...`-kall, ikkje eit host-kall — feilaktig grep-treff.
- `.github/workflows/reusable-validate.yml:73`
  (`python3 _linkml-tools/.../annotate-validate.py`) — bart GitHub-runner-kall,
  men stadfesta å vere frå 2026-05-27 (commit `5d799eb6`), altså lenge før
  containeriserings-spec-en og ikkje del av kva den spec-en gjekk gjennom
  (spec-en fokuserte eksplisitt på `Makefile`). Same kategori av avvik som
  funn 2, men **ikkje nytt** — nemnt her for fullstendigheit, ikkje som eit
  nytt funn.

## Målbilete

- `make/40-validation.mk` sine to `batch-flatten-and-validate.py`-kall køyrer
  via ein container (t.d. `$(PYTHON_RUN)` eller `$(LINKML_RUN)`, avhengig av
  om scriptet treng LinkML-spesifikke bibliotek utover `PyYAML`), slik
  containeriserings-spec-en sitt sluttmål ("Makefile-en skal ikkje innehalde
  direkte python3 ... som køyrer på hosten") framleis held.
- `.github/workflows/generate.yml` sitt versjonsoppslag brukar anten eit
  eksisterande containerisert mønster (t.d. via `$(PYTHON_RUN)` om
  `generate.yml` alt har podman/make-tilgang på det punktet) eller eit
  reint shell/`grep`/`sed`-basert oppslag av `version:`-feltet som ikkje
  krev `PyYAML` i det heile (skjemaet sitt YAML-format for `version:`-feltet
  er enkelt nok til at det kan vurderast).
- `mkdocs/publish.sh`/`mkdocs/lib/` sine 13 `PyYAML`-avhengige kallstader
  (gruppe A) køyrer via container, eller — dersom full containerisering av
  heile dokumentasjonspipelinen viser seg upraktisk i éin runde — er
  eksplisitt re-vurdert med korrekt CI-kritikalitet lagt til grunn (ikkje
  lenger handsama som "køyrer sjeldan i CI"). Dei tre nesten-identiske
  CODEOWNERS-YAML-parsing-heredocane er konsoliderte til eitt script.
  Gruppe B (stdlib-only) kan handterast som eige, lågare prioritert steg.

## Steg

1. **Avklar med brukar** kva containerstrategi som er ønskt for
   `batch-flatten-and-validate.py`: scriptet gjer både YAML-parsing (krev
   `PyYAML`) og `subprocess.run(["podman", "run", ...])` internt — å køyre
   *sjølve orkestreringsscriptet* inne i ein container krev at containeren
   har tilgang til podman-socket/CLI for å kunne starte
   mcp-linkml-validator-kontaineren nedanfrå (docker-in-docker/podman-in-
   podman-problematikk). Moglege retningar:
   - a) Køyr orkestreringsscriptet via `$(PYTHON_RUN)` med podman-socket
     mounta inn (krev endring i `PYTHON_RUN`-definisjonen og tryggleiks-
     vurdering av socket-tilgang frå containeren).
   - b) Fjern `PyYAML`-avhengigheita frå `schema_has_tree_root()` (t.d. bruk
     ein enkel regex/grep-basert sjekk av `tree_root: true`-linja i staden
     for full YAML-parsing), og aksepter at resten av scriptet (rein
     stdin/stdout-JSON-orkestrering) ikkje treng noko utover standardbiblioteket.
   - c) Eksplisitt dokumenter dette som eit nytt, akseptert unntak (som
     `mkdocs/publish.sh`/`tests/test_make.sh`), med grunngjeving om kvifor
     full containerisering ikkje er praktisk her.
2. **Implementer vald løysing** frå steg 1.
3. **Fiks `.github/workflows/generate.yml:308`:** vurder om
   `version=$(grep -m1 '^version:' "$schema_file" | sed ...)` (reint
   shell/grep, ingen Python/YAML-avhengigheit) kan erstatte
   `python3 -c "import yaml; ..."` utan å miste korrektheit — YAML-verdiar
   for `version:` i dette repoet er alltid enkle sitat-strengar (t.d.
   `version: "1.0.0"`), så eit grep/sed-mønster bør vere trygt. Alternativt,
   dersom `generate.yml` alt har eit steg med containerisert Python
   tilgjengeleg på det punktet i workflowen, bruk det i staden.
4. **Actionlint** (jf. CLAUDE.md) på `.github/workflows/generate.yml` etter
   endringa.
5. **Test lokalt/i CI:**
   - `make validate-bronze DOMAIN=<lite domene>` og
     `make validate-data DOMAIN=<domene med data/>` etter containeriserings-
     fiksen — stadfest identisk output og exit-kode-åtferd som før (jf.
     `specs/done/stille-feil-batching-regresjon.md` sine testar av desse
     same targeta).
   - Reproduser `generate.yml` sitt versjonsoppslag lokalt (t.d. via `act`
     eller eit isolert shell-testskript) mot fleire `*-schema.yaml`-filer for
     å stadfeste at det nye oppslaget gjev identisk versjon som
     `python3 -c "import yaml; ..."` gjorde.
6. **Oppdater `specs/done/containerisering-python-kall.md`** (eller legg til
   ei kort tilleggsnotis der) om at desse to nye kalla vart oppdaga og fiksa,
   slik framtidige revisjonar av same type kan finne presedens. Same notis
   bør rette opp den faktiske feilen i den spec-en sitt opphavlege utsegn om
   at `mkdocs/publish.sh` "køyrer berre ved manuell publisering (ikkje i CI)".
7. **Avklar med brukar prioritering og strategi for `mkdocs/publish.sh`/
   `mkdocs/lib/` (funn 3):**
   - a) Full containerisering av gruppe A (13 kallstader) — same
     podman-socket-i-container-problematikk som steg 1, sidan
     `mkdocs/lib/scripts/parse-dependency-tree.py`/`generate-validation-md.py`
     (gruppe B) alt køyrer reint (ingen podman-kall inni), men gruppe A sine
     `python3 -c`/heredoc-kall ikkje treng podman-tilgang i det heile — dei
     er reine YAML-lesingar. Containerisering her er difor enklare enn for
     `batch-flatten-and-validate.py` (ingen docker-in-docker-problematikk),
     men inneber truleg eit nytt, lettvekts `$(YAML_RUN)`-liknande
     container-kall for kvar av dei mange kallstadene — vurder ytingskostnad
     (kvart `podman run`-kall har oppstartskostnad, og publish.sh har opptil
     fleire slike kall **per skjema**, jf. kommentaren i
     `mkdocs/lib/generate_index.sh:31-37` om at nettopp dette var motivasjonen
     for `load_manifest_cache()` sin eksisterande batching-optimalisering).
   - b) Konsolider dei tre CODEOWNERS-heredocane til eitt delt script (uansett
     om det køyrer i container eller ikkje) — reduserer talet på kallstader
     som må containeriserast frå 13 til 11 i gruppe A.
   - c) Eksplisitt dokumenter gruppe A/B som eit medvite, avgrensa unntak med
     korrekt grunngjeving (i motsetnad til den feilaktige "køyrer sjeldan i
     CI"-grunngjevinga), dersom brukar vurderer full containerisering som
     ikkje verdt kostnaden for dette pipeline-laget.
8. **Implementer vald løysing** frå steg 7, og oppdater `mkdocs/publish.sh`/
   `mkdocs/lib/*.sh` sine call sites tilsvarande.
9. **Test lokalt:** `make docs-publish` (eller `docs-build`) for eit par
   domene, stadfest identisk generert `mkdocs/docs/`-innhald (`git diff`
   tomt for genererte sider utanom forventa endringar) før og etter
   endringa.

## Akseptansekriterier

- [x] `make/40-validation.mk` sitt `batch-flatten-and-validate.py`-kall krev
      ikkje lenger `PyYAML` på hosten (PyYAML-avhengigheita fjerna frå
      scriptet sjølv, jf. avklaring — kallet er framleis eit bart `python3`-
      kall, men treng no berre standardbiblioteket)
- [x] `.github/workflows/generate.yml` sitt versjonsoppslag krev ikkje
      `PyYAML` på GitHub-runneren
- [x] `actionlint` køyrt mot `.github/workflows/generate.yml` utan
      `[expression]`-feil
- [x] `make validate-bronze`/`make validate-data` for eit testdomene gjev
      identisk resultat (output, exit-kode, lagra valideringsloggar) før og
      etter endringa
- [x] Versjonsoppslaget i `generate.yml` gjev identisk versjonsverdi som før
      endringa, testa mot minst tre ulike `*-schema.yaml`-filer
- [x] `mkdocs/publish.sh`/`mkdocs/lib/` sine 13 Gruppe A-kallstader (funn 3)
      er anten containeriserte eller fjerna som daud kode (Gruppe B, 4
      kallstader, framleis eksplisitt utanfor omfang per avklaring)
- [x] `make docs-publish` gjev identisk generert `mkdocs/docs/`-innhald før
      og etter endringa (verifisert for alle 9 domene, ikkje berre eit par)

## Relaterte filer

- `make/40-validation.mk` — `validate-bronze`, `validate-data`
- `src/mcp-linkml-validator/batch-flatten-and-validate.py` — orkestrerings-
  scriptet med `PyYAML`-avhengigheit
- `.github/workflows/generate.yml` — "Kopier valideringsloggar til
  generated/"-steget
- `make/01-containers.mk` — `PYTHON_RUN`/`LINKML_RUN`-definisjonar
- `specs/done/containerisering-python-kall.md` — opphavleg audit og fiks,
  presedens for kva mønster som er akseptable unntak
- `specs/done/stille-feil-batching-regresjon.md` — same batching-arbeid
  (commit `29fd231c`) sin logging-regresjon, allereie fiksa; denne spec-en
  dekkjer containeriserings-sida av same underliggande endring
- `mkdocs/publish.sh` — CODEOWNERS-oppslag (linje 55), submodels-oppslag
  (linje 254)
- `mkdocs/lib/sections/kontakt.sh`, `badges.sh`, `delmodellar.sh`,
  `kom_i_gang.sh`, `avhengigheiter.sh` — sjå funn 3 for fullstendig linjeliste
- `mkdocs/lib/utils/metadata_parsers.sh`, `imported_schemas.sh`
- `mkdocs/lib/scripts/parse-dependency-tree.py`,
  `generate-validation-md.py` — gruppe B, stdlib-only
- `mkdocs/lib/generate_index.sh` — kommentar (linje 31-37) som forklarer
  motivasjonen bak `load_manifest_cache()`, relevant for ytingsvurderinga i
  steg 7a
- `.github/workflows/generate.yml:438` — `make docs-publish`-kallet som
  stadfestar at `mkdocs/publish.sh` køyrer i CI

## Utført

Avklaringar med brukar før implementering:
- **Finn 1:** fjern `PyYAML`-avhengigheita frå `batch-flatten-and-validate.py`
  i staden for å containerisere heile orkestreringsscriptet (unngår docker-
  in-docker-problematikk heilt).
- **Finn 2:** grep/sed-basert versjonsoppslag i `generate.yml` i staden for
  å behalde `python3 -c`.
- **Finn 3:** full containerisering av Gruppe A (13 kallstader), sjølv med
  akseptert ytingskostnad.

**Finn 1 — `src/mcp-linkml-validator/batch-flatten-and-validate.py`:**
`schema_has_tree_root()` brukte `yaml.safe_load()` til éin ting: sjekke om
skjemaet har ein lokal `tree_root: true`-klasse. Erstatta med eit regex-søk
(`re.compile(r"^\s+tree_root:\s*true\s*$", re.MULTILINE)`) på råteksten.
`import yaml` fjerna heilt — scriptet brukar no berre standardbiblioteket
(`argparse`, `json`, `os`, `re`, `subprocess`, `sys`, `pathlib`). Kallet i
`make/40-validation.mk` er framleis eit bart `python3`-kall (uendra), men
krev ikkje lenger nokon tredjeparts-pakke på hosten.

**Finn 2 — `.github/workflows/generate.yml:308`:** erstatta
`python3 -c "import yaml; ..."` med
`grep -m1 '^version:' "$schema_file" | sed -E 's/^version:[[:space:]]*"?([^"]*)"?[[:space:]]*$/\1/' || echo ""`.
Handterer både siterte (`version: "1.6.0"`) og usiterte (`version: 2.13.0`)
skjemaformat. `|| echo ""` bevarer fallback-semantikken under GitHub Actions
sin implisitte `set -eo pipefail` for `run:`-steg.

**Finn 3 — `mkdocs/publish.sh`/`mkdocs/lib/`:**
- Ny delt fil `mkdocs/lib/utils/python_container.sh` med
  `run_python_container()` (podman-wrapper mot `localhost/python-pytest:latest`,
  som alt har PyYAML installert via `requirements-python-test.txt`) og
  `to_container_path()` (konverterer `$REPO_ROOT/...`-stiar til `/work/...`
  for mount-en `-v "$REPO_ROOT:/work:ro"`).
- **12 kallstader containeriserte:** `metadata_parsers.sh` (4),
  `delmodellar.sh` (3), `kom_i_gang.sh` (2), `badges.sh` (1), `kontakt.sh` (1),
  `publish.sh` (1, submodels-oppslag).
- **1 kallstad fjerna som daud kode:** `publish.sh` sin `get_contact_info()`
  (CODEOWNERS-oppslag, linje 55 i det opphavlege funnet) var eksplisitt merkt
  `# DEPRECATED ... Behald stub for bakoverkompatibilitet`, erstatta av
  `generate_contact_info()` i `kontakt.sh`, og aldri kalla nokon stad i
  kodebasen (stadfesta med `grep -rn "get_contact_info"`). Sletta heilt i
  staden for å containerisere ubrukt kode, jf. CLAUDE.md.
- **Biverknad:** sletting av `get_contact_info()` fjerna éin av dei tre
  nesten-identiske CODEOWNERS-YAML-parsing-heredocane som vart flagga som eit
  DRY-avvik i Funn 3 — berre to att (`badges.sh`/`kontakt.sh`), under
  CLAUDE.md sin treterskel for påkravd konsolidering. Ingen ytterlegare
  konsolidering naudsynt.
- **Gruppe B (4 kallstader, stdlib-only)** — `badges.sh:59`,
  `avhengigheiter.sh`, `imported_schemas.sh`, `valideringsresultat.sh` —
  ikkje containeriserte, i tråd med avklaringa (spørsmålet gjaldt
  eksplisitt Gruppe A).

**Verifisert:**
- `bash -n` på alle sju endra shell-filer og den nye `python_container.sh`.
- `python3 -m py_compile` på `batch-flatten-and-validate.py`.
- `schema_has_tree_root()`: samanlikna gammal (yaml-basert) og ny
  (regex-basert) implementasjon mot alle 36 `*-schema.yaml`-filer i repoet —
  0 avvik.
- Versjonsoppslaget i `generate.yml`: samanlikna gammal (python3/yaml) og ny
  (grep/sed) implementasjon mot alle 36 skjema — 0 avvik, inkludert
  det eine skjemaet med usitert versjonsverdi (`dcat-ap-no-schema.yaml`).
- `actionlint` mot `generate.yml`: ingen `[expression]`-feil (berre
  pre-eksisterande `[shellcheck]`-stilråd på urelaterte linjer 177/339).
- `make validate-bronze DOMAIN=fair`: identisk output/exit-kode som før
  PyYAML-fjerninga.
- Kvar containerisert funksjon i `mkdocs/lib/` testa isolert (kjeldd
  direkte, kalla med reelle skjema/manifest frå repoet): `load_manifest_cache`/
  `get_validation_policy`/`get_external_spec_url`/`get_external_spec_label`
  (inkl. manglande og korrupt manifest — ÅTVARING-fallback verifisert),
  `generate_badges` (utgjevar-oppslag), `generate_submodel_box`/
  `generate_submodels_section` (begge retningar, ekte delmodell-relasjon frå
  `ap-no/modelldcat-ap-no`), `generate_quickstart` (versjon + auto-detektert
  klasse/variabel/policy), `generate_contact_info` (både `path_patterns`- og
  `catalog_slug`-matching).
- **Full `make docs-publish`-køyring** (alle 9 domene, ikkje berre eit par):
  exit 0, ~5m27s (mot tidlegare ukjend basistid — aldri målt før
  containerisering, sidan dette er første gong heile pipelinen er
  fullstendig containerisert). `git diff` mot `mkdocs/docs/` etter køyringa
  synte **éin** avvikande fil (`referanse/referansemodell/index.md`,
  badge-*rekkjefølgje*), stadfesta å vere ei pre-eksisterande staleness i det
  committa dokumentet (matcha ikkje `badges.sh` sin *allereie eksisterande,
  urørte* echo-rekkjefølgje frå før dagens endringar) — reversert med
  `git checkout --` sidan det er urelatert til denne spec-en. Ingen andre
  avvik i nokon av dei ni domena.

**Oppfølging (2026-08-09, etter første CI-køyring):** `make docs-publish`
feila i `.github/workflows/generate.yml` sin `publish`-jobb med gjentekne
`ÅTVARING: kunne ikkje lese submodels ... (... pinging container registry
localhost: dial tcp [::1]:443: connect: connection refused)`. Rotårsak: lokal
testing skjedde med `localhost/python-pytest:latest` alt bygd i podman sitt
image-lager, men **kvar CI-jobb køyrer på ein separat, tom runner-VM** —
podman sitt image-lager delast ikkje mellom jobbar. `publish`-jobben
(`needs: [generate, checkout-source]`) har sin eigen, avgrensa
image-innlastingslogikk (berre eit "Last mkdocs-local image frå GHCR"-steg,
sidan det historisk var einaste image `docs-publish`/`docs-build` trong) —
i motsetnad til `generate`-jobben, som brukar ein generell
"detect-images"/pull-images-composite-action og alt korrekt lastar
`python-pytest` (`always_required: true` i `images.json`, difor uavhengig av
domene). Fiksen containeriserte kall som no krev `python-pytest` i
`publish`-jobben, men jobben fekk aldri eit tilsvarande pull-steg.

**Fiks:** la til eit "Last python-pytest image frå GHCR"-steg i
`publish`-jobben (`.github/workflows/generate.yml`, rett etter det
eksisterande mkdocs-local-steget), med identisk mønster
(`podman pull` + `podman tag ... localhost/python-pytest:latest`) og
identisk GHCR-tag-utrekning (`hashFiles('src/assets/containers/Dockerfile.python',
'src/assets/containers/requirements-python-test.txt')`) som `checkout-source`
sitt `image-tags`-steg alt brukar for same image. `actionlint` køyrt på nytt
mot `generate.yml` — ingen nye `[expression]`-feil (same to
pre-eksisterande `[shellcheck]`-funn som før, urelaterte linjer 177/339).
Kunne ikkje fullt ut reproduserast lokalt (krev faktisk GHCR-autentisering
og separate, tomme runner-VM-ar), men tag-mønsteret er verifisert identisk
med det alt fungerande `mkdocs-local`-steget og med `ensure-images`-jobben
sin biletbygging — same `always_required: true`-image, same
hash-input-kombinasjon.

Alle steg i spec-en er fullførte (steg 1-9), inkludert oppfølgingsfiksen for
CI-image-tilgjenge. Ingen ytterlegare oppfølging i `bugs/` naudsynt utover
denne spec-en sin eigen dokumentasjon av funnet.
