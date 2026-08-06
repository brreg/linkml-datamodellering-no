# Logging-støy i `make domain-<domain>` — doble linjer og ugata rådata

## Bakgrunn

Brukaren limte inn CI-loggen frå `make domain-samt` (GitHub Actions-runner,
`/home/runner/work/...`) og observerte to ting:

1. **To linjer for kvar generator**, t.d.:
   ```
   → gen-jsonld-context: samt/samt-bu
   → gen-jsonld-context  samt/samt-bu (3.5s)
   ```
2. **Ekstralinjer som ser uventa/ugata ut**, t.d. ein rå `podman run`-kommandolinje
   midt i loggen, og fleire `[DEBUG]`-linjer og verktøy-eigne meldingar
   (avrotize, asyncapi-validate, openapi-spec-validator, generate-informasjonsmodell.py).

Analysen under skil dei to fenomena, sidan dei har heilt ulik rotårsak.

## Funn 1 — to linjer per generator er tilsikta design, ikkje ein feil

`src/assets/scripts/makefile/run-parallel-gen.sh` (delt av alle
`run_gen_*_parallel`-makroane i `make/10-generator-macros.mk`) skriv:

- **Éi deloverskrift** før xargs-parallelliseringa startar (linje 78):
  `log_info "→ ${generator}: ${names}"` — lister alle skjema som er
  *aktiverte* for denne generatoren (filtrert mot `build.yaml`-flagget).
- **Éi fullført-linje per skjema** inne i kvar xargs-arbeidar (linje 121):
  `log_info "→ ${generator}  ${domain}/${name} (Ns)"` — med køyretid.

Dette er det tilsikta resultatet av
`specs/done/kompakt-generator-logging.md` (steg 1: "Skriv éi deloverskrift
via `log_info`… Skriv éi samla `log_debug`-linje for dei som vert hoppa
over"). Deloverskrifta finst for å gje oversikt over *kva som køyrer* før
parallelliseringa spreier output over fleire xargs-arbeidarar (nyttig når
eit domene har mange skjema, t.d. ap-no med 9). Fullført-linja gjev
individuell køyretid per skjema.

**Kvifor det ser dobla ut for `samt`:** domenet har berre **eitt** skjema
(`samt-bu`). Då degenererer mønsteret til to nesten identiske linjer —
`"→ X: samt/samt-bu"` og `"→ X  samt/samt-bu (Ns)"` — utan at
deloverskrifta tilfører ny informasjon utover det fullført-linja alt viser.
For domene med fleire skjema tilfører deloverskrifta reell verdi (kva som
er aktivert vs. hoppa over, samla på éin stad, før interfoldia parallelt
output).

**Vurdering:** ikkje ein bug i logikken, men eit ergonomisk problem —
deloverskrifta bør truleg visast på `LOGLVL=DEBUG` (som skip-samandraget på
linje 83), eller berre skrivast når `${#enabled[@]} > 1`. Sjå forslag i
steg 1.

## Funn 2 — dei fleste "uventa" ekstralinjene kjem frå `LOGLVL=DEBUG` i CI (tilsikta)

`.github/workflows/generate.yml` set `LOGLVL: DEBUG` eksplisitt for stega
"Generer alle artefaktar" (linje 330) og "Publiser og bygg
dokumentasjonsportal" (linje 434), i tråd med
`specs/done/logging-framework-makefile.md` sin uttalte grunngjeving:
"CI-loggar vert lagra i GitHub Actions og er essensielle for feilsøking."

Med `LOGLVL=DEBUG` vert **all** fanga stdout/stderr frå `run_logged`-kall
skrive ut via `log_debug` (`make/00-settings.mk` linje 104-106), t.d.:

- `[DEBUG] Executing Convert JSON schema to Avrotize schema…` og
  `WARNING: Unable to resolve circular dependency…` — avrotize sin eigen
  output, fanga av `run_logged "gen-xsd/j2a …"` i `run_gen_xsd_parallel`
- `[DEBUG] fix-xsd-dates: 12 datofelt fiksa…` — frå `fix-xsd-dates.py`
- `[DEBUG] …samt-bu-openapi.yaml: OK` — frå `gen-openapi.py`
- `[DEBUG] Validation diagnostics: …` og "File … is valid but has
  warnings." — frå `asyncapi validate`
- `✓ Generert: …samt-bu-manifest.yaml` — frå `generate-informasjonsmodell.py`

Alt dette er **forventa** oppførsel gitt at CI køyrer med `LOGLVL=DEBUG` —
det er nettopp det denne logg-arkitekturen skal gjere. Det er ikkje ein
feil, men det betyr at *alle* CI-køyringar av `make domain-*` er like
verbose som ein lokal `LOGLVL=DEBUG`-køyring, uavhengig av om det oppstod
eit problem å feilsøkje.

## Funn 3 — éin reell inkonsistens: `linkml-convert`-løkka omgår heile logg-rammeverket

`make/20-domain-targets.mk` (linje 46-56, `domain_target`) og dei to
tilsvarande løkkene i `Makefile` (`convert-rdf` linje 98-110 og
`convert-data` linje 112-134) skriv:

```make
echo "$(CLR_STEP)→ linkml-convert  $$example$(CLR_RST)"; \
echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate --output $$out $$example"; \
$(LINKML_RUN) linkml-convert ...
```

Den andre `echo`-linja skriv ut heile den rå `podman run …
linkml-convert …`-kommandolinja **ubetinga**, via eit bart `echo` — ikkje
via `log_debug`/`log_info` frå `LOG_FUNCTIONS`. Det er nøyaktig den typen
kommandolinje-dump `logging-framework-makefile.md` (linje 244-248,
DEBUG-nivå-eksempelet) seier skal vere `log_debug`-gata og dermed usynleg
på `LOGLVL=INFO`/`ERROR`. Alle andre 12 generator-makroar i
`make/10-generator-macros.mk` følgjer dette (kommandoen sjølv vert aldri
`echo`-a rått; einaste unntaket er sjølve stdout/stderr frå kommandoen,
som anten går til fila den skal, eller vert fanga av `run_logged` og
`log_debug`-gata).

**Konsekvens:** denne eine `podman run --rm -v …`-linja (med full
absolutt sti, image-namn, alle flagg) vert skrive ut **uansett
`LOGLVL`** — også på `LOGLVL=ERROR`, der ingenting anna skal visast ved
suksess. Dette er den einaste staden i heile `make/`-laget som bryt
`log_debug`-konvensjonen på denne måten, og er truleg ein rest frå før
`LOG_FUNCTIONS` vart innført (`convert-examples.sh` og
`linkml-convert`-løkka er ikkje nemnde i handlingslista i
`logging-framework-makefile.md` eller `kompakt-generator-logging.md`).

## Relevante filer

- `src/assets/scripts/makefile/run-parallel-gen.sh` — deloverskrift (linje 78) + fullført-linje (linje 121)
- `make/00-settings.mk` — `LOG_FUNCTIONS`, `LOGLVL`-styring
- `make/20-domain-targets.mk` — `linkml-convert`-løkka (linje 46-56)
- `Makefile` — `convert-rdf` (linje 98-110), `convert-data` (linje 112-134)
- `.github/workflows/generate.yml` — `LOGLVL: DEBUG` (linje 330, 434)

## Steg

1. **Avklar med brukar** kva som skal rettast (sjå spørsmål i chat):
   - Deloverskrifta i `run-parallel-gen.sh` (Funn 1): la stå, gate til
     `LOGLVL=DEBUG`, eller berre skriv ho når meir enn eitt skjema er
     aktivert?
   - `LOGLVL=DEBUG` i CI (Funn 2): behalde som i dag (tilsikta,
     dokumentert), eller er det noko brukaren vil endre?
2. Rett `linkml-convert`-løkka (Funn 3, uavhengig av avklaringa over —
   dette er den eintydige inkonsistensen): fjern den ubetinga
   `echo "$(LINKML_RUN) linkml-convert …"`-linja, eller gate ho via
   `log_debug` (krev `eval "$$LOG_FUNCTIONS"` i løkka, som ikkje er sett
   opp i dag sidan løkka brukar rein `echo`/`$(CLR_STEP)` i staden for
   `LOG_FUNCTIONS`). Same retting i alle tre stadene (`20-domain-targets.mk`,
   `Makefile` × 2) — unngå å innføre eit fjerde duplikat, vurder om
   `convert-examples.sh` bør ta over sjølve `echo`-a i staden (DRY, jf.
   CLAUDE.md-regelen om tre eller fleire identiske tilfelle).
3. Test: `make domain-samt LOGLVL=ERROR` skal ikkje lenger vise
   `podman run …`-linja ved suksess; `make domain-samt LOGLVL=DEBUG` skal
   framleis vise ho.
4. Oppdater denne specen med "Utført"-seksjon og flytt til `specs/done/`.

## Handlingsliste

- [x] Avklar med brukar: gate deloverskrift i `run-parallel-gen.sh` til `LOGLVL=DEBUG` (Funn 1)
- [x] Avklar med brukar: behalde `LOGLVL=DEBUG` i CI som i dag (Funn 2) — ingen endring
- [x] Rett `linkml-convert`-løkka til å gate kommandolinje-dumpen via `log_debug` (Funn 3)
- [x] Test med `LOGLVL=ERROR`/default og `LOGLVL=DEBUG`
- [x] Commit-melding

## Utført

**Funn 1 — deloverskrift gata til DEBUG, omforma:**

`src/assets/scripts/makefile/run-parallel-gen.sh` linje 78: `log_info "→
${generator}: ${names}"` → `log_debug "${generator} for schemas:
${names}"`. Brukaren valde å i tillegg fjerne den innleiande pila og
skrive om teksten (`X for schemas: Y` i staden for `X: Y`) slik at ho
skil seg tydeleg frå fullført-linja (`→ X  Y (Ns)`) same om ho skulle bli
synleg. Toppkommentaren i scriptet oppdatert til å forklare kvifor
deloverskrifta er DEBUG-only (unngår to nesten identiske INFO-linjer for
batchar med berre eitt skjema, utan å miste oversikta for domene med
mange skjema på `LOGLVL=DEBUG`).

**Funn 2 — ingen endring:** `LOGLVL=DEBUG` i CI (`generate.yml` linje 330,
434) er tilsikta og godt dokumentert (`logging-framework-makefile.md`) —
brukaren stadfesta at dette skal halde fram som i dag.

**Funn 3 — `linkml-convert`-løkka gata via `LOG_FUNCTIONS`:**

Alle tre stadene (`make/20-domain-targets.mk` sin `domain_target`,
`Makefile` sine `convert-rdf` og `convert-data`) fekk `eval
"$LOG_FUNCTIONS"` (høvesvis `$$$$LOG_FUNCTIONS` i `domain_target`-makroen
pga. dobbel `$(call)`/`$(eval)`-utpakking) og bytte av dei to `echo`-linjene
til `log_info` (steg-linja, som før synleg på INFO) og `log_debug`
(kommandolinja, no berre synleg på `LOGLVL=DEBUG`, med same
`"Kommando: …"`-prefiks som resten av kodebasen).

**Verifisert:**
- `make -n domain-fair`, `make -n convert-rdf`, `make -n convert-data` —
  korrekt make-escaping (shell ser `$LOG_FUNCTIONS`/`$schema` osv., ikkje
  literalar)
- `make domain-samt` (default `LOGLVL=INFO`): éi linje per generator, ingen
  rå `podman run …`-linje for `linkml-convert`
- `make domain-samt LOGLVL=DEBUG`: deloverskrifta (`X for schemas: Y`) og
  `linkml-convert`-kommandolinja er begge synlege att

**Følgje opp — `generate-informasjonsmodell.py` sine eigne progress-prints:**

Brukaren peika ut endå ei støylinje frå same CI-logg, køyrt gjennom
`generate-informasjonsmodell.py` (kalla av
`run_gen_informasjonsmodell_instance_parallel`, `make/30-instances.mk`):

```
[DEBUG] Genererer Informasjonsmodell-instans for src/linkml/samt/samt-bu/samt-bu-schema.yaml
✓ Generert: src/linkml/samt/samt-bu/metadata/samt-bu-manifest.yaml
```

Same rotårsak som Funn 2 (`run_logged` fangar stdout og sender det til
`log_debug` ved suksess), men her er sjølve *innhaldet* òg reint
overflødig: `run-parallel-gen.sh` sin xargs-arbeidar loggar allereie éi
`log_info`-fullført-linje med køyretid (`→
gen-informasjonsmodell-instance samt/samt-bu (Ns)`) etter kvart vellukka
kall, så scriptet sine eigne `print(f"Genererer …")` og `print(f"✓
Generert: …")` (linje 377 og 392) dupliserer informasjon som allereie
finst, og finst berre i skriptet fordi det historisk vart køyrt
frittståande før `run_logged`/`run-parallel-gen.sh` vart innført. Fjerna
begge `print()`-kalla — feilhandteringa (`log_error(...)` i
`except`-blokka, uendra) dekkjer framleis kravet om ingen stille feil.

Verifisert med `make gen-informasjonsmodell-instance
SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml LOGLVL=DEBUG`: berre
deloverskrifta og fullført-linja vert vist, ingen duplikat frå scriptet.

**Følgje opp 2 — `Kommando: podman run …`-debuglinja i `linkml-convert`-løkka fjerna heilt:**

Brukaren peika ut at `log_debug "Kommando: $(LINKML_RUN) linkml-convert
…"` (lagt til i Funn 3 over, som DEBUG-gata erstatning for den gamle
ubetinga `echo`) framleis er unødvendig støy, sjølv på `LOGLVL=DEBUG`.
Samanlikna med dei 12 andre generator-makroane i
`make/10-generator-macros.mk`: ingen av dei loggar sin eigen
`podman run`-kommandolinje på noko loggnivå — kommandoen (gitt via
`GEN_CMD`) køyrer stille, og `run-parallel-gen.sh` sin
start-/fullført-logg dekkjer kva som skjer og kor lang tid det tok.
`Kommando: …`-linja var dermed overflødig ceremoni frå omskrivinga, ikkje
eit reelt behov. Fjerna heilt (ikkje berre DEBUG-gata) frå alle tre
stadene (`make/20-domain-targets.mk`, `Makefile` sine `convert-rdf` og
`convert-data`) — `log_info "→ linkml-convert  <fil>"` står att som einaste
loggnivå for dette steget, uendra.

Verifisert med `make domain-samt LOGLVL=DEBUG`: `Kommando: …`-linja er
borte, `→ linkml-convert  <fil>`-linja er framleis synleg.

**Følgje opp 3 — CI-preflight-header og `Hoppar over linkml-convert`-linjer (frå `make domain-ap-no`-logg):**

Brukaren limte inn CI-loggen frå `make domain-ap-no` (10 skjema, fleire
`example_rdf: false`) og peika ut to nye ting:

1. Header-teksten `.github/workflows/generate.yml` skriv før
   `make domain-<domain>` startar (`echo "=== Skjema som skal genererast
   for ${{ matrix.domain }} ==="`, linje 335) skulle endrast til `"===
   ${{ matrix.domain }} skjema for artefakt generering ==="`. Reint
   tekstbyte, gjort direkte. `actionlint` køyrd mot `generate.yml` etter
   endringa — berre pre-eksisterande `[shellcheck]`-funn (stilråd, ikkje
   blokkerande), ingen `[expression]`-feil.
2. `Hoppar over linkml-convert for <full sti> (example_rdf: false)` —
   éi linje per hoppa-over eksempelfil, skrive **ubetinga** til stderr av
   `convert-examples.sh` (linje 35, rein `echo`, ikkje gata av `LOGLVL`).
   Bryt konvensjonen etablert av `run-parallel-gen.sh` (og handheva i
   `specs/done/kompakt-generator-logging.md`): skip-meldingar skal
   samlast til **éi** kombinert linje per steg, via `log_debug` (synleg
   berre på `LOGLVL=DEBUG`) — jf. `hoppar over (<flag>: false):
   domain/skjema1, domain/skjema2` frå dei parallelle generator-makroane.
   `convert-examples.sh` hadde derimot éin `echo` per fil, ubetinga
   synleg på alle loggnivå, med full filsti i staden for korte
   `domain/skjema`-namn.

**Retting:** `convert-examples.sh` (`src/assets/scripts/makefile/`) fekk
`eval "$LOG_FUNCTIONS"` (miljøvariabelen er allereie eksportert av
`make/00-settings.mk`, ingen ny kallar-endring nødvendig sidan Make
eksporterer ho til alle recipe-shell), eit `skipped=()`-array som samlar
`domain/profil` for kvart hoppa-over eksempel undervegs i løkka, og éi
`log_debug "  hoppar over linkml-convert (example_rdf: false):
${skipped_list}"` etter løkka — same mønster (leiande to mellomrom,
kommaseparert liste, prosentfjerning av trailing komma) som
`run-parallel-gen.sh` sin skip-logg.

**Verifisert:**
- `make domain-ap-no` (default `LOGLVL=INFO`): ingen `hoppar over`-treff
- `make domain-ap-no LOGLVL=DEBUG`: éi samla linje —
  `hoppar over linkml-convert (example_rdf: false): ap-no/cpsv-ap-no,
  ap-no/dcat-ap-no, ap-no/dqv-ap-no, ap-no/modelldcat-ap-no,
  ap-no/skos-ap-no, ap-no/xkos-ap-no` — i staden for 6 separate ubetinga
  linjer

**Følgje opp 4 — `→ linkml-convert  <fil>` er ei start-linje forkledd som
fullført-linje:**

Brukaren la merke til at `→ linkml-convert  <fil>` dukkar opp **rett
etter** `→ gen-rdf  samt/samt-bu (6.0s)` i loggen, og vart usikker på kva
tidsrom linja gjaldt. Rotårsaka: denne linja vert skrive **før**
`linkml-convert`-kallet køyrer (`log_info "→ linkml-convert  $example"`,
utan `(Ns)`-tidsstempel), medan **alle** dei 12 andre generator-stega
(via `run-parallel-gen.sh`) berre loggar éi `log_info`-linje **etter**
vellukka køyring, med køyretid — `→ <generator>  <domain>/<namn>
(N.Ns)`. Same `→`-prefiks og fargekode vert dermed brukt til å bety to
ulike ting (start vs. fullført) avhengig av kva steg det gjeld, utan at
lesaren kan sjå forskjellen.

**Retting:** `linkml-convert`-løkka (alle tre stadene: `domain_target` i
`make/20-domain-targets.mk`, `convert-rdf` og `convert-data` i
`Makefile`) målar no køyretid rundt sjølve `linkml-convert`-kallet
(`t0=$(date +%s%3N)` … `t1=$(date +%s%3N)`) og loggar `→ linkml-convert
<fil> (N.Ns)` **etter** vellukka konvertering — same format og
tidspunkt-semantikk (fullført, med køyretid) som alle andre
generator-steg.

**Verifisert:** `make domain-samt` — linja er no `→ linkml-convert
src/linkml/samt/samt-bu/examples/samt-bu-eksempel.yaml (11.2s)`, plassert
etter `→ gen-rdf … (14.7s)` som før, men no eintydig eit
fullført-med-køyretid-steg, ikkje eit ambiguøst startvarsel.
`make -n domain-fair`/`convert-rdf`/`convert-data` — korrekt
make-escaping stadfesta (shell ser `$(date …)`, `$(( … ))` og
`$example`/`$datafile`, ikkje literalar eller feiltolka make-referansar).

**Følgje opp 5 — deloverskrifta inkluderer no generator-flagget:**

Brukaren peika på at generator-kommandonamn (`gen-shacl`, `gen-proto`,
`gen-json-schema` …) ikkje alltid matchar `build.yaml`-flaggnamnet
(`shacl`, `protobuf`, `json_schema` …), noko som skaper forvirring når ein
skal slå opp kva flagg som styrer eit steg. `run-parallel-gen.sh` (linje
81) skriv no `"${generator} (${flag}: true) for schemas: ${names}"` når
eit flagg finst, elles same tekst som før (for `merge-imports` og
`gen-informasjonsmodell-instance`, som ikkje er flagg-styrte).

Verifisert med `make domain-samt LOGLVL=DEBUG`: t.d. `gen-shacl (shacl:
true) for schemas: samt/samt-bu`, `gen-json-schema (json_schema: true)
for schemas: samt/samt-bu`, `gen-proto (protobuf: true) for schemas:
samt/samt-bu` — flagget vist tydeleg saman med generator-namnet, medan
`merge-imports for schemas: samt/samt-bu` (ingen flagg) er uendra.
