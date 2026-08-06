# Audit — inkonsistensar i logging i make-target og tilhøyrande shellscript

## Bakgrunn

Etter fleire punktvise rettingar i `specs/done/logging-stoy-domenebygg.md`
(deloverskrifter, `linkml-convert`-timing, skip-samandrag, generator-flagg
i deloverskrift), bad brukaren om ein brei gjennomgang av **all** logging
i `make/*.mk`, `Makefile` og shellscript kalla derifrå, for å finne
attverande inkonsistensar — ikkje berre i `domain_target`-pipelinen som
har fått mest merksemd til no.

**Referanse-konvensjonen** (etablert i `specs/done/logging-framework-makefile.md`
og handheva gjennom heile `logging-stoy-domenebygg.md`):
- `LOGLVL=ERROR` (default i lokal bruk er `INFO`, CI brukar eksplisitt
  `DEBUG`) skal vise **berre feil**
- `LOGLVL=INFO` (default) skal vise status/framgang, ikkje kommandolinjer
  eller verktøy-eigne diagnosticar
- `LOGLVL=DEBUG` skal vise alt — kommandoar, deloverskrifter, skip-samandrag
- All logging skal gå via `log_info`/`log_debug`/`log_error` (frå
  `LOG_FUNCTIONS`, `make/00-settings.mk`) eller `print_header`/`print_step`/
  `print_info`/`print_warning`/`print_error` (`make/03-output.mk`) — aldri
  rå `echo`/`printf` for status/framgang-meldingar
- Fullført-linjer skal ha køyretid (`(N.Ns)`), skrivast **etter** vellukka
  køyring, aldri før

Metode: grep etter `echo`/`printf`/`$(CLR_*)`/`print(` i alle `make/*.mk`,
`Makefile`, og alle shellscript i `src/assets/scripts/makefile/` +
`mkdocs/publish.sh`, kryssjekka mot om `eval "$LOG_FUNCTIONS"` er i bruk i
same kontekst.

## Funn (ranga etter alvorsgrad)

### 1. `CLR_WARN` er referert, men aldri definert (reell bug)

`make/03-output.mk:38` (`print_warning`) og `make/40-validation.mk:106`
(manglande-eksempelfil-åtvaring i `validate-examples`) brukar
`$(CLR_WARN)`, men **ingen `CLR_WARN := ...` finst nokon stad** i
`make/00-settings.mk` (som definerer `CLR_SEP`, `CLR_HDR`, `CLR_STEP`,
`CLR_OK`, `CLR_ERR`, `CLR_DBG`, `CLR_RST` — men ikkje `CLR_WARN`).
`$(CLR_WARN)` ekspanderer difor til tom streng, så **`print_warning` og
åtvaringa i `validate-examples` har aldri hatt farge** sidan dei vart
skrivne. Stille funksjonsfeil, ikkje berre stilbrot.

**Retting:** legg til `CLR_WARN := $(shell printf '\033[0;33m')` (gult,
konsistent med `CLR_ERR`/`CLR_OK`-mønsteret) i `make/00-settings.mk`.

### 2. `→ …`-stega med fargekode som omgår `LOG_FUNCTIONS` heilt

Fire stader brukar nøyaktig same visuelle språk som `log_info`/`log_error`
(`$(CLR_STEP)→ …$(CLR_RST)`, `$(CLR_ERR)…$(CLR_RST)`) via **rå `echo`**,
ikkje via funksjonane sjølve — dei er dermed usynlege for `LOGLVL`-styring
(vises alltid, også på `LOGLVL=ERROR`, i strid med kontrakten "berre feil"):

- `make/30-instances.mk:76` — `echo "$(CLR_STEP)Køyrer full LinkML-validering$(CLR_RST)"` (`validate-informasjonsmodell-instance`)
- `make/30-instances.mk:102` — `echo "$(CLR_STEP)Validerer $$ORG_DATA mot $$ORG_SCHEMA$(CLR_RST)"` (`validate-modellkatalog-instance`)
- `make/60-mcp.mk:73` — `echo "$(CLR_STEP)→ Køyrer roundtrip-test for $(SCHEMA)$(CLR_RST)"` (`mcp-linkml-modell-utkast`)
- `make/60-mcp.mk:75` — `echo "$(CLR_ERR)Roundtrip-test feila — sjå logg for detaljar$(CLR_RST)"` (same target — burde vore `log_error`, som òg ville gjeve `[ERROR]`-prefiks)

**Retting:** legg til `eval "$$LOG_FUNCTIONS"; \` og byt til
`log_info`/`log_error`, same mønster som brukt i `make/40-validation.mk`
og alt retta i `make/20-domain-targets.mk`/`Makefile` for `linkml-convert`.

### 3. Same "start-linje utan fullføring/køyretid"-mønster som `linkml-convert` hadde, funne i tre til

Før dagens rettingar hadde `linkml-convert` ei `→ …`-linje skriven **før**
kommandoen køyrde, utan køyretid — brukaren peika på at dette var
tvitydig samanlikna med alle andre steg (som loggar **etter**, med
`(N.Ns)`). Same mønster finst uretta i `make/40-validation.mk`:

- Linje 52 (`validate-bronze`): `log_info "→ validate-bronze  $$domain/$$name"` — før `flatten-and-validate.bash`-kallet, ingen fullført-linje/køyretid etterpå
- Linje 84 (`validate-data`): `log_info "→ mcp-validate  $$datafile  (policy: $$policy)"` — same mønster
- Linje 109 (`validate-examples`): `log_info "→ validate-examples  $$domain/$$name"` — same mønster

Desse går ikkje via `run-parallel-gen.sh` (heilt anna kodepath, eigne
`while`/`for`-løkker), så dei manglar òg den DEBUG-gata
`(<flag>: true) for schemas: …`-deloverskrifta domain_target-steget har.
Sidan dei brukar identisk `→`-prefiks, kan ein lesar ikkje sjå frå loggen
åleine at dette er ein heilt annan (eldre, ad hoc) logg-konstruksjon enn
`run-parallel-gen.sh`-pipelinen.

**Retting (same mønster som `linkml-convert`):** mål `t0`/`t1` rundt
`flatten-and-validate.bash`/`podman run … linkml validate`-kallet i kvar
løkke, flytt `log_info`-linja til **etter** kallet med `(N.Ns)`.

### 4. `echo "$$result"` — full valideringsutdata skriven ubetinga, uansett `LOGLVL`

I `validate-bronze` (linje 55), `validate-data` (linje 87) og
`validate-examples` (linje 114) vert heile valideringsresultatet (JSON
eller rå LinkML-validate-tekst, potensielt langt) skrive til stdout via
rein `echo`, **for kvart skjema, uavhengig av `LOGLVL` og uavhengig av om
valideringa var vellukka**. På `LOGLVL=ERROR` (som `generate.yml`/
`validate.yml` brukar via `DEBUG` — men merk: `validate-bronze`/
`validate-data`/`validate-examples` vert kalla frå andre stader, sjekk om
nokon køyrer dei med `LOGLVL=ERROR`) ville dette bryte "berre feil"
-kontrakten for vellukka skjema.

**Dette kan vere bevisst** — valideringsresultatet er kanskje sjølve
*payload*-en brukaren køyrer kommandoen for å sjå (parallelt med korleis
`make lint` sin output ikkje er "logging" men det faktiske resultatet),
ikkje støy. **Avklaring naudsynt før retting** — sjå spørsmål i chat.

### 5. `generate-readme-tables.sh` brukar emoji i staden for den etablerte fargekode-/prefikskonvensjonen

Kalla frå `docs-publish` (`make/50-docs.mk:38`). Scriptet nyttar ikkje
`LOG_FUNCTIONS` i det heile, og har tre ubetinga statuslinjer med emoji i
staden for ANSI-fargar/`[NIVÅ]`-prefiks (einaste staden i heile
`src/assets/scripts/makefile/` som gjer dette):

- Linje 12: `echo "❌ Feil: $README finst ikkje"`
- Linje 16: `echo "🔧 Genererer auto-genererte tabellar for $README..."`
- Linje 219: `echo "✅ $README er oppdatert med auto-genererte tabellar"`

CLAUDE.md sin generelle regel ("emoji berre når eksplisitt bede om det")
gjeld primært LLM-generert output, men same argument gjeld her for
konsistens: resten av kodebasen signaliserer feil/suksess med
`CLR_ERR`/`[ERROR]`/`log_info`, ikkje emoji.

**Retting:** krev `LOG_FUNCTIONS` i miljøet (som `convert-examples.sh`
alt gjer), byt dei tre linjene til `log_error`/`log_info`/`log_info`.

### 6. `mkdocs/publish.sh` implementerer sitt eige, parallelle logging-oppsett — null `LOGLVL`-medvit

Det klart største scriptet kalla frå `make` (572 linjer, `docs-publish`).
Redefinerer `SEP`, `CLR_SEP`, `CLR_HDR`, `CLR_STEP`, `CLR_OK`, `CLR_ERR`,
`CLR_RST` **lokalt** (linje 12-18) med identiske fargeverdiar som
`make/00-settings.mk`, i staden for å attbruke dei — driftsrisiko (dei to
stadene kan skilje lag over tid). Har **ingen** `LOGLVL`-gating i det
heile — alle ~40 statuslinjene (`echo "${CLR_STEP}→ …"` osv.) vert vist
uavhengig av nivå, sjølv om `50-docs.mk` sin `docs-publish`-target
allereie brukar `log_info`/`log_debug` konsekvent for steget rett før
(`generate-readme-tables.sh`).

**Vurdering:** dette er eit strukturelt, større arbeid (heile scriptet
må gå via `eval "$LOG_FUNCTIONS"` og skiljast mellom `log_info`/`log_debug`
linje for linje) — ikkje ei rask punktretting som resten av funna over.
Flagga for merksemd, ikkje foreslått løyst i same omgang.

### 7. Mindre funn (lågare prioritet)

- **`Bruk:`/`Feil:`/`Error:`-meldingar før `exit 1`** brukar rein `echo`
  i staden for `log_error` fleire stader (`30-instances.mk`, `60-mcp.mk`,
  `70-scaffolding.mk`, `40-validation.mk:178`). Sidan desse alltid skal
  visast (brukarfeil), er den praktiske konsekvensen låg — men dei mistar
  `[ERROR]`-prefiks/raud farge som elles er konsekvent brukt for feil.
- **`70-scaffolding.mk` sin `update-valid-scopes`** (linje 42, 47) brukar
  ustylt `echo` for start-/fullført-melding — ingen farge, ingen
  `log_info`, ingen køyretid. Lite trafikkert utviklarverktøy, låg
  prioritet.
- **`check-prereqs.bash`** har sitt eige sjølvstendige ✓/⚠/✗-rapportformat
  — dette er **ikkje** eit funn, output **er** sjølve leveransen (som
  `make lint`), ikkje logg-støy. Nemnt for å unngå at det vert forveksla
  med eit overse tt tilfelle ved seinare gjennomgang.

## Steg (dersom brukar ønskjer retting)

1. Avklar Funn 4 (`echo "$$result"`) — skal valideringsresultat framleis
   vere ubetinga synleg, eller DEBUG/ERROR-gata som resten av loggen?
2. Rett Funn 1 (`CLR_WARN` manglar) — trivielt, éin linje i `00-settings.mk`
3. Rett Funn 2 (fire `echo`→`log_info`/`log_error`-bytte)
4. Rett Funn 3 (timing rundt `flatten-and-validate.bash`/`linkml validate`
   i `validate-bronze`/`validate-data`/`validate-examples`, same mønster
   som `linkml-convert`)
5. Rett Funn 5 (`generate-readme-tables.sh` → `LOG_FUNCTIONS`)
6. Vurder Funn 6 (`mkdocs/publish.sh`) som eige, større spec-arbeid —
   ikkje del av denne runden
7. Vurder Funn 7 (mindre funn) — låg prioritet, kan takast samla med Funn 2

## Handlingsliste

- [x] Avklar Funn 4 med brukar — svar: valideringsresultat skal vere DEBUG-gata som resten av loggen
- [x] Funn 1 — legg til `CLR_WARN` i `make/00-settings.mk`
- [x] Funn 2 — `30-instances.mk` + `60-mcp.mk`: byt rå `echo` til `log_info`/`log_error`
- [x] Funn 3 — timing i `validate-bronze`/`validate-data`/`validate-examples`
- [x] Funn 4 — `echo "$$result"` → `log_debug "$$result"` i alle tre (gjort saman med Funn 3)
- [x] Funn 5 — `generate-readme-tables.sh` → `LOG_FUNCTIONS`
- [x] `PYTHON_RUN` manglar `-i` (urelatert bug oppdaga under verifisering av Funn 3/4, retta på brukar sin førespurnad)
- [x] Funn 6 (`mkdocs/publish.sh`) — retta på brukar sin førespurnad
- [x] Funn 7 (mindre funn: usage/error-echo utan `log_error`, `update-valid-scopes`) — retta på brukar sin førespurnad
- [x] Test med `LOGLVL=ERROR`/`INFO`/`DEBUG` etter kvar retting
- [x] Commit-melding

## Utført

**Funn 1** — `CLR_WARN := $(shell printf '\033[0;33m')` lagt til i
`make/00-settings.mk` (gult, same mønster som `CLR_ERR`/`CLR_OK`).
`print_warning` og `validate-examples` sin manglande-eksempelfil-åtvaring
har no faktisk farge.

**Funn 2** — `make/30-instances.mk` (`validate-informasjonsmodell-instance`,
`validate-modellkatalog-instance`) og `make/60-mcp.mk`
(`mcp-linkml-modell-utkast`) fekk `eval "$$LOG_FUNCTIONS"` lagt til, og dei
fire `echo "$(CLR_STEP)/$(CLR_ERR)…"`-linjene bytt til `log_info`/`log_error`.

**Funn 3 + 4** — `validate-bronze`, `validate-data`, `validate-examples`
(`make/40-validation.mk`) målar no `t0`/`t1` rundt sjølve
valideringskallet (`flatten-and-validate.bash`/`linkml validate`) og
loggar `→ <steg>  <mål> (N.Ns)` **etter** vellukka køyring — same mønster
som `linkml-convert`-fiksen frå tidlegare i dag. `echo "$$result"` bytt
til `log_debug "$$result"` i alle tre: valideringsresultatet er no
DEBUG-gata som resten av loggen, i tråd med brukaren sitt svar på
avklaringsspørsmålet. Feil vert framleis alltid synlege uavhengig av
`LOGLVL` — `validate-bronze`/`validate-examples` sine eksisterande
`log_error "::error file=…"`-kall (og GitHub-annotasjonane frå
`emit-github-validation-annotations.py`) er urørte.

**Funn 5** — `generate-readme-tables.sh` krev no `LOG_FUNCTIONS` i
miljøet (`: "${LOG_FUNCTIONS:?…}"` + `eval`), og dei tre emoji-linjene
(`❌`/`🔧`/`✅`) er bytte til `log_error`/`log_info`/`log_info`.

**Verifisert:**
- `make -n validate-bronze DOMAIN=fair`/`validate-data DOMAIN=fair` —
  korrekt make-escaping (single-expansion-kontekst, same mønster som
  resten av `40-validation.mk`)
- `make validate-data DOMAIN=modellkatalog` (6 datafiler, default
  `LOGLVL=INFO`) — éi tidsett `→ mcp-validate … (N.Ns)`-linje per
  datafil, ingen rå resultat-dump
- `make validate-examples DOMAIN=samt` — `→ validate-examples
  samt/samt-bu (11.7s)` på default nivå; `LOGLVL=DEBUG` viser i tillegg
  kommando + fullt resultat (`No issues found`); `LOGLVL=ERROR` er heilt
  stille ved suksess
- `make validate-bronze DOMAIN=fair LOGLVL=DEBUG` — stadfesta at
  `t0`/`t1`/timing og `log_debug "$$result"` fungerer korrekt (fullt
  gyldig JSON vist), og at `→ validate-bronze fair/fair-metadata
  (15.7s)`-linja no kjem **etter** valideringskallet, ikkje før
- `make docs-publish` (avbrote etter README-steget, sidan
  `mkdocs/publish.sh` er Funn 6/utanfor scope) —
  `generate-readme-tables.sh` sine tre linjer går no via `log_info`/
  `log_error`, ingen emoji att

**Ny, urelatert bug oppdaga under verifisering, retta på brukar sin
førespurnad (`make/01-containers.mk`):** `make validate-bronze
DOMAIN=<domain>` krasja alltid i `emit-github-validation-annotations.py`
med `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char
0)`. Rotårsak: `PYTHON_RUN` (`make/01-containers.mk`) mangla `-i` på
`podman run`, så `<<< "$$result"`-heredocen i `validate-bronze`
(`make/40-validation.mk`) aldri nådde containeren sin stdin — scriptet
las tom streng. Stadfesta med eit isolert `podman run --rm` vs.
`podman run --rm -i`-forsøk (utan `-i`: 0 byte lesne på stdin).

**Retting:** la til `-i` på `PYTHON_RUN` (`podman run -i --rm ...`),
same mønster som `MCP_RUN` (`make/60-mcp.mk`) og `LINKML_MOD_RUN`
(`Makefile`) allereie brukar for containerar som mottek pipa/heredoc-a
stdin. To kjende kallstader var råka: `emit-github-validation-
annotations.py <<< "$$result"` (`validate-bronze`) og
`mcp-write-modell-utkast-response.py` (`mcp-linkml-modell-utkast`, motteke
via pipe frå LinkML-modell-utkast-serveren).

**Verifisert:**
- `make validate-bronze DOMAIN=fair` — fullfører no med exit 0 (berre
  åtvaringar), ingen `JSONDecodeError`; GitHub-annotasjonane
  (`::warning file=...`) vert korrekt emitterte
- `make validate-bronze DOMAIN=fair LOGLVL=ERROR` — framleis synlege
  åtvaringar (som forventa, sidan GH-annotasjonar alltid skal visast),
  ingen anna støy
- `make gen-informasjonsmodell-instance SCHEMA=...` (ingen stdin-piping,
  éin av dei mange andre `PYTHON_RUN`-kallstadene) — uendra åtferd,
  stadfestar at `-i` ikkje har biverknader for ikkje-piping-bruk
- `make -n mcp-linkml-modell-utkast SCHEMA=...` — stadfesta at alle tre
  `podman run`-ledd i pipelinen (inkl. dei to `PYTHON_RUN`-kalla) no har
  `-i`

**Funn 7** — alle `Bruk:`/`Usage:`/`Error:`/`Feil:`-meldingar før `exit 1`
i `make/30-instances.mk`, `make/40-validation.mk`, `make/60-mcp.mk` og
`make/70-scaffolding.mk` bytt frå rå `echo` til `log_error` (med
`eval "$$LOG_FUNCTIONS"` lagt til der det mangla). Fleirlinje-meldingar
(t.d. `Error: X` + `Usage: Y`) slått saman til éin `log_error`-kall, same
mønster som `validate-bronze`/`validate-data`/`validate-examples` sine
eksisterande `DOMAIN`-guard-klausular. `70-scaffolding.mk` sin
deprecation-åtvaring (`new-begrepskatalog`) bytt til `log_info` med
`$(CLR_WARN)` (no definert, jf. Funn 1) — same mønster som den
eksisterande `example_rdf`-åtvaringa i `validate-examples`.
`update-valid-scopes` fekk `eval "$$LOG_FUNCTIONS"` og sine to
statuslinjer bytt til `log_info`.

**Verifisert:** alle guard-klausular testa direkte (manglande
SCHEMA/INSTANCE/ORG/NAME/DOMAIN/INPUT-parameter) — kvar viser no
`[ERROR]`-prefiks med raud farge, korrekt exit code. Fann og rydda opp
i to utilsikta biverknader frå testinga: (1) eit avbrote `make
docs-publish`-forsøk hadde delvis rive ned `mkdocs/docs/referanse/`
(gjenoppretta med `git checkout`), og (2) ein forureina `NAME`-
miljøvariabel (sett til maskinen sitt hostname av WSL2-miljøet) fekk
`new-modellkatalog`/`new-begrepskatalog` til å faktisk køyre i staden
for å treffe guard-klausulen ved første forsøk — oppdaga og retta ved å
tvinge `NAME=` tom eksplisitt i test-kallet, og dei uynskte
scaffolding-filene som vart oppretta (`src/src/linkml/begrepskatalog/…`)
vart sletta. `update-valid-scopes` sin faktiske content-oppdatering av
`.github/valid-scopes.txt` (avdekte at fila alt var forelda før denne
økta) vart reverta — utanfor scope for denne retteomgangen.

**Funn 6** — `mkdocs/publish.sh` (572 linjer, kalla frå `docs-publish`,
`make/50-docs.mk`) retta:

1. **`make/00-settings.mk`**: `CLR_STEP`/`CLR_RST` var alt eksporterte
   (for `run-parallel-gen.sh`). La til eksport av `SEP`, `CLR_SEP`,
   `CLR_HDR`, `CLR_OK`, `CLR_ERR`, `CLR_WARN`, `CLR_DBG` — same grunngjeving:
   frittståande script (ikkje embedda `$(CLR_*)`-tekstsubstitusjon i ei
   Make-recipe-linje) treng fargane som miljøvariablar. Fjernar
   naudsynet for kvart slikt script å redeklarere identiske
   ANSI-fargekodar lokalt.
2. **`mkdocs/publish.sh`**: fjerna den lokale `SEP`/`CLR_*`-blokka (linje
   12-18, duplikat av `00-settings.mk` sine verdiar) og bytt til å
   `eval "$LOG_FUNCTIONS"` (arva via eksport, same mønster som
   `convert-examples.sh` og `generate-readme-tables.sh`). Alle
   status-/steg-/feil-meldingar (~20 stader — steg-fullført-linjer med
   køyretid, per-skjema-fullført inne i `process_schema()` som køyrer i
   parallelle bakgrunnsjobbar, feilrapportering frå parallelle jobbar,
   `generate_validation_docs()` sine to linjer, sluttoppsummeringa) bytt
   frå rå `echo`/`printf` til `log_info`/`log_error`. Den ubetinga
   `ÅTVARING: … stale artefakter`-linja bytt frå `CLR_ERR` til `CLR_WARN`
   (ikkje fatal, same mønster som andre åtvaringar i denne runden).
   Fleire feilmeldingar som før var spreidde over 4-7 separate
   `echo`-linjer (per-jobb-feil, sluttoppsummering) slått saman til éin
   `log_error`-kall kvar, i tråd med den etablerte eittlinjes
   feil-konvensjonen elles i kodebasen. `log_step()` (banner-funksjonen,
   tilsvarande `print_header`) er **framleis alltid synleg** uavhengig av
   `LOGLVL` — same kontrakt som `print_header` i `make/03-output.mk`.
   Reine innhaldsgenererande funksjonar (`get_contact_info()`,
   domene-`index.md`-tabellar, `mkdocs.yml`-nav) er urørte — desse sine
   `echo`-kall er sjølve *payload*-en (fil-innhald), ikkje logging.

**Verifisert:**
- `bash -n mkdocs/publish.sh` — syntaktisk gyldig
- Isolert test av den eksporterte `LOG_FUNCTIONS` + nye fargevariablane
  via eit minimalt scratch-Makefile: stadfesta at `log_info` er skjult på
  `LOGLVL=ERROR`, synleg på `INFO`/`DEBUG`; `log_debug` berre synleg på
  `DEBUG`; `log_error` og rå `echo`-banner alltid synlege — nøyaktig den
  same kontrakten som resten av kodebasen
- **Full, uavbroten køyring av `make docs-publish`** (~170s, 37
  skjema-jobbar i parallell over 9 domene) — fullførte med exit 0, alle
  stega (1-4) viste korrekt farga/tidsett `log_info`-output, ingen feil
  - `git status` etter køyringa: **ingen endringar i `mkdocs/docs/` eller
    `README.md`** — stadfestar at det genererte *innhaldet* er
    byte-for-byte identisk med før refaktoreringa, berre logginga endra
    seg
