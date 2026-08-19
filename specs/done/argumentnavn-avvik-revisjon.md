# Plan: Avvikande argumentnamn i COMMANDS.md/make help

## Bakgrunn

Brukaren peika på at `make validate` sitt argument `SCHEMAS` (fleirtal)
avvik frå `SCHEMA` (eintal) brukt elles, og bad om eit søk etter tilsvarande
avvik i heile `COMMANDS.md` og kjeldegrunnlaget for `make help`
(`make/*.mk`, `Makefile`, lest via `src/assets/scripts/makefile/help.sh`).

Metode: samanlikna argumentnamn i alle `## `-kommentarar (kjelda til
`make help`) mot tilsvarande rader i `COMMANDS.md`, og verifiserte kvart
avvik mot den faktiske oppskrifta (`ifdef`/`$(if $(VAR),...)`) for å
avgjere om avviket er reelt (feil dokumentasjon) eller berre kosmetisk.

## Funn

### A — COMMANDS.md dokumenterer feil variabelnamn (kommandoen ville ikkje fungert som vist)

| Target | `make help`-kjelde (korrekt) | `COMMANDS.md` (feil) | Verifisert mot oppskrift |
|---|---|---|---|
| `roundtrip-json-schema` | `[JSONSCHEMA=<sti>]` (`Makefile:110`) | `SCHEMA=<sti>` (linje 157) | Oppskrifta les `$(JSONSCHEMA)` — `SCHEMA=` gjer ingenting |
| `log-mcp-validate` | `(MANIFEST=<sti> eller SCHEMA=<sti> POLICY=<policy>)` (`make/40-validation.mk:237`) | berre `SCHEMA=<sti>` (linje 167) | Oppskrifta krev `POLICY` saman med `SCHEMA` (elles `log_error`-feil) — `MANIFEST` som alternativ er heilt utelate |

### B — Same omgrep, ulikt variabelnamn (brukaren sitt opphavlege eksempel + analogt tilfelle)

| Omgrep | Variabelnamn brukt | Stader |
|---|---|---|
| Skjema-sti(ar) | `SCHEMA` (eintal, dei aller fleste target) vs. `SCHEMAS` (fleirtal, berre `validate`) | `make/40-validation.mk:22` — `SCHEMAS` er faktisk **same globale variabel** som auto-oppdaga skjemaliste frå `make/02-schema-discovery.mk`, attgjenbrukt/overstyrbar som brukarargument. `lint` fell òg tilbake til `$(SCHEMAS)` internt (`make/40-validation.mk:28`) utan at det er dokumentert i `## `-kommentaren |
| Organisasjons-alias | `NAME=<alias>` (`new-modellkatalog`) vs. `ORG=<alias>`/`ORG=<org-slug>` (`gen-modelldcat-elements`, `validate-modellkatalog-instance`) | `make/70-scaffolding.mk:31`, `Makefile:154`, `make/30-instances.mk:85` — alle tre referer til same identifikator (t.d. `digdir-modellkatalog`), men `new-modellkatalog` kallar han `NAME`, dei to andre kallar han `ORG` |

### C — COMMANDS.md viser feil/urelaterte argument (ikkje berre feil namn, heile argumentlista feil)

3 rader i «Enkeltartefakter»-tabellen (linje 222-238) fekk tydelegvis
malen `[DOMAIN=...] [SCHEMA=...]` kopiert inn frå dei 14 andre `gen-*`-radene
utan å sjekke om det stemmer for desse tre spesifikt:

| Target | `COMMANDS.md` seier (feil) | Faktisk oppskrift |
|---|---|---|
| `gen-config` (linje 236) | `[DOMAIN=...] [SCHEMA=...]` | Ingen argument i det heile — `config.mk`-avhengig target, `Makefile:169` |
| `gen-dqv-measurements` (linje 237) | `[DOMAIN=...] [SCHEMA=...]` | Ingen argument i det heile — `Makefile:150-152` |
| `gen-modelldcat-elements` (linje 238) | `[DOMAIN=...] [SCHEMA=...]` | `[ORG=<alias>] [DRYRUN=1]` — `Makefile:154` |

### D — Manglar heilt i COMMANDS.md

| Target | Har argument i `## `-kommentar |
|---|---|
| `gen-linkml-merge` | `[DOMAIN=<domain>\|SCHEMA=<sti>]` — ingen rad i COMMANDS.md i det heile |
| `remove-modell` | `(DOMAIN=<domene> NAME=<namn>) [CONFIRM=1]` — ingen rad i COMMANDS.md (funne under tidlegare arbeid, [[domain-name-argumentrekkjefolge]]) |
| `make validate` sitt `SCHEMAS=<sti ...>`-argument | Raden for `make validate` (linje 160) viser ingen argument i det heile, sjølv om `## `-kommentaren i `make/40-validation.mk:22` viser `[SCHEMAS=<sti ...>]` |

### E — Dokumentasjon av fjerna funksjonalitet

`COMMANDS.md` (linje 63, 182-186) skildrar `PARALLEL=N` som ein parameter
alle `domain-*`-target støttar («default: 8 jobbar»). Søk i heile
kjeldekoden (unntatt `specs/done/` og `generated/`) finn **ingen**
`PARALLEL`-referanse i `make/*.mk`, `Makefile` eller
`run-domain-pipeline.sh` — berre i `tests/test_make.sh` (urelatert
kontekst). `run-domain-pipeline.sh` sin eigen toppkommentar skildrar i
staden ei fastlagd fase-basert parallellisering (Fase 1/2/3, ikkje eit
brukarstyrt jobb-tal). Mest sannsynleg vart `PARALLEL` fjerna i eit
tidlegare refactor (jf. `run-domain-pipeline.sh`) utan at COMMANDS.md vart
oppdatert.

## Vurdering

Funn A og C er reelle feil — ein brukar som følgjer COMMANDS.md ordrett
ville fått ein kommando som anten ikkje gjer det dokumentert, eller feilar.
Funn D er reine dekningshol. Funn E krev anten fjerning av prosaen eller
(dersom det finst eit gjeldande motstykke) omskriving til å skildre
fase-parallelliseringa i staden. Funn B (NAME/ORG, SCHEMA/SCHEMAS) krev eit
brukarval: **rett dokumentasjonen til å skildre dagens namn** (minimal,
ingen åtferdsendring) eller **rename sjølve `make`-variabelen** for
konsistens (brekk moglegvis eksisterande brukarvanar/skript som alt brukar
`NAME=` for `new-modellkatalog`).

## Brukarval

Brukaren valde: **rett alt, inkl. B — harmoniser sjølve variabelnamna**
(ikkje berre dokumentasjonen).

## Handlingsliste

1. [x] A: Retta `roundtrip-json-schema`- og `log-mcp-validate`-radene i
   COMMANDS.md til faktisk variabelnamn
2. [x] C: Retta `gen-config`-, `gen-dqv-measurements`- og
   `gen-modelldcat-elements`-radene til faktiske argument/output
3. [x] D: Lagt til manglande rader (`gen-linkml-merge`, `remove-modell`,
   `SCHEMA`-argument på `validate`-raden)
4. [x] E: Fjerna/korrigert stale `PARALLEL=N`-dokumentasjon
5. [x] B: Harmonisert variabelnamn i koden (ikkje berre dokumentasjonen)

## Utført

**B — variabel-rename (koda):**
- `make/40-validation.mk`: `validate` sitt argument endra frå
  `[SCHEMAS=<sti ...>]` til `[SCHEMA=<sti>]`, med same
  `$(if $(SCHEMA),$(SCHEMA),$(SCHEMAS))`-fallback-mønster som `lint` alt
  brukte (`SCHEMAS`-den globale auto-oppdaga lista er urørt — framleis
  brukt internt av `run_gen_linkml_parallel`/testsuite-batching via
  `tests/test_make.sh` sine `SCHEMAS=`-kall, som framleis fungerer uendra
  sidan fallback-rekkjefølgja er identisk)
- `make/70-scaffolding.mk`, `src/assets/scripts/scaffolding/new-modellkatalog.sh`:
  `new-modellkatalog` sitt argument endra frå `NAME=<alias>` til
  `ORG=<alias>`, konsistent med `gen-modelldcat-elements`/
  `validate-modellkatalog-instance` som alt brukte `ORG` for same
  organisasjons-alias-omgrep
- Oppdatert alle referansar: `COMMANDS.md`, `CODEOWNERS.md`,
  `mkdocs/docs/kom-i-gang/kommandoar.md`, `mkdocs/docs/kom-i-gang/ny-org.md`

**A/C/D — COMMANDS.md-rettingar:**
- `roundtrip-json-schema`: `SCHEMA=<sti>` → `JSONSCHEMA=<sti>`
- `log-mcp-validate`: no viser både `POLICY=<policy>` (kravd saman med
  SCHEMA) og `MANIFEST=<sti>`-alternativet i prosa
- `gen-config`/`gen-dqv-measurements`: retta til «ingen argument» +
  korrekt output-sti (høvesvis `config.mk` og in-place oppdaterte
  `build.yaml`-datamanifest, ikkje `generated/.../*.ttl` som før)
- `gen-modelldcat-elements`: retta til faktiske `[ORG=<alias>] [DRYRUN=1]`
  + korrekt output-sti (modellkatalog-datafil, ikkje `.ttl`)
- Nye rader: `gen-linkml-merge` (Validering-tabellen), `remove-modell`
  (scaffolding-tabellen)
- `validate`-raden viser no `[SCHEMA=<sti>]`

**E — PARALLEL fjerna frå levande dokumentasjon** (funksjonen sjølv vart
fjerna tidlegare, jf. `specs/done/evaluer-parallel-flag-etter-batching.md`
— berre dokumentasjonen hadde ikkje følgt etter):
- `COMMANDS.md`: to stader (kryssreferanse + eigen «Parallellisering»-bolk)
- `make/README.md`: fjerna konvensjonspunkt + feilsøkingsråd som
  refererte ein ikkje-eksisterande variabel
- `mkdocs/docs/kom-i-gang/kommandoar.md`: same bolk som COMMANDS.md
- `mkdocs/docs/automasjon/modellmanifest-generering.md`: tre
  `PARALLEL=N`-kodeeksempel fjerna/omskrivne

**Verifisert:** `make help` viser no alle retta argument korrekt
(`validate [SCHEMA=<sti>]`, `new-modellkatalog (ORG=<alias>)`,
`roundtrip-json-schema [JSONSCHEMA=<sti>]` osv.). `make -n gen-config` og
`make validate SCHEMA=<sti>` (reell køyring) verifisert å fungere.
`tests/test_make.sh` sine `SCHEMAS=`-baserte kall til `validate`
uendra/kompatible sidan fallback-rekkjefølgja er identisk med før.
