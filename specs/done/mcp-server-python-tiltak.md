# Tiltak: rett alle funn frå `.claude/rules/mcp-server-python.md` i dei tre MCP-serverane

## Bakgrunn

`.claude/rules/mcp-server-python.md` (jf. `specs/done/mcp-server-kodepraksis-rule.md`)
dokumenterer fire kodepraksis-funn for `src/mcp-*/**`. Denne specen kartlegg
**konkret status per funn i kvar av dei tre serverane** — kva som alt er
retta, og kva som framleis må endrast — som grunnlag for eit avgrensa
implementeringstiltak.

### Status per funn (verifisert direkte mot kjeldekoden denne økta)

| # | Funn i rula | `mcp-linkml-validator` | `mcp-linkml-modell-utkast` | `mcp-linkml-begrep-utkast` |
|---|---|---|---|---|
| 1 | Feil-før-resultat ved JSON-RPC-parsing | ✅ Alt retta (`flatten-and-validate.bash`, `batch-flatten-and-validate.py`, `batch-validate-instances.py` sjekkar alle `"error" in resp` før `result`-indeksering) | — (ingen JSON-RPC-*konsument* i denne mappa, berre *produsent*) | — (same) |
| 2 | Identifikatorsanering på alle utleiingsstader | — (ikkje relevant, ingen identifikator-utleiing her) | ✅ Alt retta (`_sanitize_identifier()` brukt i `_collect_types`, `_resolve_ref`, `_collect_enums`, `_collect_classes`) | — (ikkje relevant) |
| 3 | Namnekonvensjon `mcp-linkml-<funksjon>` | ✅ README konsistent | ❌ **README stale** — 4× `make mcp-generate` + 1× ugyldig `POLICY=default` | ❌ **README stale** — `make mcp-begrep-build` (1×) + `make mcp-begrep-list-profiles` (2×) |
| 4 | Triplisert JSON-RPC-dispatch-boilerplate | ❌ Del av triplikatet | ❌ Del av triplikatet | ❌ Del av triplikatet |

Funn 1 og 2 er altså **allereie i samsvar** med rula i alle tre serverane —
ingen kodeendring trengst for desse. Funn 3 og 4 har konkrete, verifiserte
avvik og er scope for tiltaka under.

### Nytt funn denne økta: crash-isolasjon manglar i to av tre `main()`-løkker

Ved gjennomlesing av alle tre `main()`-funksjonane for å planleggje
konsolideringa av funn 4, vart eit femte, ikkje tidlegare dokumentert avvik
oppdaga: **berre** `src/mcp-linkml-validator/server.py` sin `main()` (linje
1376-1385) pakkar `handle(msg)`-kallet i eit `try/except Exception`, med
kommentar om at éin uventa exception i handteringa av éi melding elles ville
drepe heile prosessen og miste resultatet for *alle* attverande jobbar i ein
batch. `mcp-linkml-modell-utkast/server.py` (linje 245) og
`mcp-linkml-begrep-utkast/server.py` (tilsvarande linje) manglar denne
vakta — ein uventa exception i éin tool-handler (t.d. ein ikkje-fanga feil i
`converter.py` eller `concept_search.py`) ville i dag terminere heile
stdio-sesjonen for desse to serverane, i staden for å returnere ein
JSON-RPC-feilrespons for berre den eine meldinga.

Dette er relevant for konsolideringa av funn 4: når `main()`-løkka vert
flytta til eit delt modul, skal **alle tre** serverane arve
crash-isolasjonen som i dag berre finst i éin av dei.

## Tiltak

### A — Rett stale namnekonvensjon i README (funn 3)

**`src/mcp-linkml-modell-utkast/README.md`:**
- Linje 9, 12, 100, 125: `make mcp-generate` → `make mcp-linkml-modell-utkast`
- Linje 12: `POLICY=default` er ikkje ein gyldig verdi (policyane er
  `bronze`/`silver`, jf. `profiles/*.yaml`) — byt til eit gyldig eksempel
  (t.d. `POLICY=silver`, som alt er dokumentert lenger ned i same fil)

**`src/mcp-linkml-begrep-utkast/README.md`:**
- Linje 11: `make mcp-begrep-build` → `make mcp-linkml-begrep-utkast`
- Linje 14, 291: `make mcp-begrep-list-profiles` → `make mcp-linkml-begrep-utkast-list-profiles`

Reint dokumentasjonstiltak — ingen kodeendring, ingen risiko.

### B — Konsolider triplisert JSON-RPC-dispatch-boilerplate (funn 4 + crash-isolasjon)

**Ny delt fil:** `src/assets/scripts/utils/mcp_jsonrpc_stdio.py` (same
katalog som `linkml_relative_import_patch.py`, som alt er delt på tvers av
fleire `src/mcp-*/`- og `src/assets/scripts/makefile/`-kallestader — same
mønster for deling).

Inneheld:

1. `send(obj: dict) -> None` — uendra frå alle tre servarane i dag.
2. `dispatch(msg, *, tools, tool_handlers, server_name, server_version) -> dict | None`
   — handterer `initialize` (bygger `serverInfo` frå `server_name`/
   `server_version`), `initialized` (returnerer `None`), `tools/list`
   (returnerer `tools`-lista uendra), `tools/call` (slår opp
   `tool_handlers[tool_name]` — ein `dict[str, Callable[[Any, dict], dict]]`
   kvar server byggjer sjølv — og kallar han med `(msg_id, arguments)`;
   ukjent verktøy → `-32602`-feil), og metode-ikkje-funnen (`-32601`-feil).
   Denne funksjonen kapslar nøyaktig den koden som i dag er duplisert
   linje-for-linje i alle tre `handle()`-funksjonane, **utanom** sjølve
   tool-spesifikk forretningslogikk (som framleis bur i kvar server sin
   eigen `_handle_*`-funksjon).
3. `run_stdio_loop(dispatch_fn: Callable[[dict], dict | None]) -> None`
   — les linje for linje frå `sys.stdin`, handterer JSON-parse-feil
   (`-32700`), kallar `dispatch_fn(msg)` **innanfor** eit
   `try/except Exception` (crash-isolasjon — henta frå
   `mcp-linkml-validator` sin eksisterande vakt, no brukt av alle tre), og
   sender responsen via `send()` dersom han ikkje er `None`.

**Endring i kvar av dei tre `server.py`-filene:**

- Fjern lokal `send()`, `main()`, og den generiske delen av `handle()`
  (initialize/initialized/tools-list/ukjent-verktøy/metode-ikkje-funnen).
- Behald `handle()`-namnet, men la han byggje `tool_handlers`-dicten (namn
  → funksjon) og delegere til `dispatch()` frå det delte modulet.
- `mcp-linkml-validator/server.py` sin eksisterande `try/except` i `main()`
  fjernast (flytta til det delte modulet) — ingen funksjonell endring for
  denne serveren, berre flytting.
- `mcp-linkml-modell-utkast` og `mcp-linkml-begrep-utkast` sine `main()`
  får crash-isolasjon dei manglar i dag — **funksjonell endring** (må
  nemnast i commit-melding og verifiserast eksplisitt, sidan det endrar
  feilåtferd, ikkje berre flyttar kode).

**Uendra, urørt:**
- Alle `TOOL_*`-konstantane (verktøydefinisjonar/JSON Schema for kvart
  verktøy)
- Alle `_handle_*`-funksjonane (forretningslogikk per verktøy)
- Feilkodane (`-32700`, `-32601`, `-32602`, `-32000`) og meldingsformatet

## Handlingsliste

- [x] A1: `src/mcp-linkml-modell-utkast/README.md` — rett 4× `mcp-generate` + `POLICY=default`
- [x] A2: `src/mcp-linkml-begrep-utkast/README.md` — rett `mcp-begrep-build` + 2× `mcp-begrep-list-profiles`
- [x] B1: Opprett `src/assets/scripts/utils/mcp_jsonrpc_stdio.py` (`send`, `dispatch`, `run_stdio_loop`)
- [x] B2: Refaktorer `src/mcp-linkml-validator/server.py` til å bruke det delte modulet
- [x] B3: Refaktorer `src/mcp-linkml-modell-utkast/server.py` til å bruke det delte modulet
- [x] B4: Refaktorer `src/mcp-linkml-begrep-utkast/server.py` til å bruke det delte modulet
- [x] B5: Verifiser uendra åtferd:
      `make mcp-linkml-valider-modell-smoke`, `make mcp-linkml-valider-modell-test`,
      `make mcp-linkml-modell-utkast-smoke`, `make mcp-linkml-modell-utkast-test`,
      `make mcp-linkml-begrep-utkast-smoke`
- [x] B6: Verifiser crash-isolasjon i alle tre (t.d. midlertidig injisert
      exception i ein tool-handler → forvent JSON-RPC-feilrespons for éi
      melding, ikkje krasja prosess) for `mcp-linkml-modell-utkast` og
      `mcp-linkml-begrep-utkast` spesifikt, sidan dette er ny åtferd der
- [x] B7 (oppdaga under utføring, ikkje i opphavleg plan): oppdater alle
      podman-monteringar av dei tre serverane til å gjere
      `mcp_jsonrpc_stdio.py` tilgjengeleg i kontainaren — sjå Avgjerder

## Avgrensing

- Funn 1 og 2 i rula krev **ingen** endring — alt verifisert i samsvar.
- Sjølve request-/respons-parsing-scripta under
  `src/assets/scripts/makefile/` (t.d. `mcp-extract-modell-utkast-response.py`)
  er **utanfor scope** — dei ligg utanfor `src/mcp-*/**` og høyrer til
  `make-conventions.md`-rula sitt scope, ikkje `mcp-server-python.md`.
- Verktøynamnet `generate_linkml` (nemnd som valfri omdøyping i
  `specs/done/mcp-server-namngjeving.md`) vert **ikkje** endra — det er
  utanfor scope for denne specen.

## Avgjerder

- **`src/mcp-linkml-begrep-utkast/README.md` linje 11 vart retta til
  `make build-docker-mcp-begrep-utkast`, ikkje `make mcp-linkml-begrep-utkast`
  slik opphavleg plan (A i denne specen) sa.** Grunngjeving: sjekk mot
  faktisk `make/60-mcp.mk` viste at kommentaren over kommandoen sa "Bygg
  containeren (éin gong)" — det korrekte biletbygging-targetet er
  `build-docker-mcp-begrep-utkast`. `mcp-linkml-begrep-utkast` er eit heilt
  anna target (genererer eit begrep frå ein JSON-fil, krev `INPUT=`).
  Å følgje det opphavlege planutkastet ordrett ville gjeve brukaren ein
  reelt feil README-kommando. Avdekt og retta før commit.
- **Konsolideringa av funn 4 (steg B) kravde eit vesentleg større
  omfang enn opphavleg spec skildra: alle podman-monteringar av dei tre
  serverane måtte oppdaterast** for at det nye, delte modulet
  (`mcp_jsonrpc_stdio.py`) i det heile skal vere importerbart inne i
  kontainarane — sidan modulet er ein **hard** avhengigheit for at
  `server.py` skal starte (ikkje ein valfri bug-workaround med mjuk
  fallback, slik `linkml_relative_import_patch.py` er). Kartla alle
  invokeringsstader via grep og retta kvar av dei:
  - `Makefile`: `LINKML_MOD_RUN`, `LINKML_BEGREP_RUN` — la til
    `-v .../src/assets/scripts/utils:/app/utils:ro`
  - `make/60-mcp.mk`: `MCP_RUN` (validator) og
    `mcp-linkml-modell-utkast-test`-oppskrifta — same mount
  - `src/assets/scripts/scaffolding/new-modell.sh`: generate_linkml-kallet
    (linje ~70-76) — same mount
  - `tests/test_make.sh`: `test_roundtrip_json_schema()` sitt direkte
    podman-kall til modell-utkast — same mount
  - `mcp-linkml-valider-modell-test` (heile repoet montert på `/work`) og
    batch-scripta (`batch-flatten-and-validate.py`,
    `batch-validate-instances.py`, `flatten-and-validate.bash`, alle
    monterer `/repo`) trong **ingen** endring — dekt automatisk av
    `server.py` sin repo-relative sys.path-kandidat
    (`Path(__file__).resolve().parent.parent / "assets/scripts/utils"`)
  - `server.py` i alle tre prøver tre kandidatstiar (`/app/utils`,
    `/repo/src/assets/scripts/utils`, repo-relativ sti) — same mønster
    som `linkml_relative_import_patch.py` sin kandidatsøk, men utan mjuk
    fallback (import-feil skal krasje høgt, ikkje logge ei åtvaring og
    halde fram — modulet er *påkravd* for at serveren skal fungere)
  - `.github/workflows/generate.yml` og `.github/workflows/validate.yml`
    sine cache-nøklar (som eksplisitt listar `server.py` som
    cache-avhengigheit) fekk `mcp_jsonrpc_stdio.py` lagt til, elles ville
    ei framtidig endring i det delte modulet gjeve eit stille cache-hit
    i CI i staden for reell re-køyring
  Alle desse endringane vart verifisert empirisk (sjå Utført), ikkje berre
  resonnert fram.
- **Dockerfile.mcp-linkml vart *ikkje* endra** (ingen `COPY` av
  `mcp_jsonrpc_stdio.py` inn i sjølve biletet). Grunngjeving: repoet sin
  eigen dokumentasjon (`mkdocs/docs/arkitektur/ekstern-bruk.md`) stadfestar
  at dei publiserte GHCR-bileta alt **ikkje** er sjølvforsynte — brukarar
  som køyrer `ghcr.io/brreg/mcp-linkml-validator` må alt hente og montere
  støttefiler (`flatten-and-validate.bash`, `policies/`) frå repoet separat.
  Å krevje at `src/assets/scripts/utils/` òg monterast er konsistent med
  eit etablert mønster, ikkje ei ny byrde. Berre `mcp-linkml-modell-utkast`
  og `mcp-linkml-begrep-utkast` manglar tilsvarande dokumentert
  ekstern-bruk-instruks i dag — utanfor scope her.
- **`_ok()`/`_param_error()`-hjelparane i `mcp-linkml-begrep-utkast/server.py`
  vart ikkje rørte/konsoliderte inn i det delte modulet**, sjølv om dei
  liknar `send()`/feilbygging-mønsteret. Grunngjeving: dei er
  fil-spesifikke envelope-hjelparar for denne serveren sine eigne
  `_handle_*`-funksjonar (ikkje del av den generiske JSON-RPC-dispatch-
  mekanikken triplisert på tvers av alle tre), og rula/specen sitt scope
  var uttrykkjeleg avgrensa til send/dispatch/main-løkka.

## Utført

**A — README-rettingar** (`src/mcp-linkml-modell-utkast/README.md`,
`src/mcp-linkml-begrep-utkast/README.md`): alle stale kommandoreferansar
retta til faktiske make-target, jf. Avgjerder over for begrep-utkast sitt
avvik frå opphavleg plan.

**B — Delt `mcp_jsonrpc_stdio.py` + refaktorering av alle tre `server.py`:**

- Nytt modul `src/assets/scripts/utils/mcp_jsonrpc_stdio.py`:
  `send()`, `error_response()`, `dispatch()`, `run_stdio_loop()`
  (crash-isolasjon inkludert).
- `src/mcp-linkml-validator/server.py`: `handle()` bygger no
  `_TOOL_HANDLERS` (`validate_linkml_schema`→`_handle_validate_schema`,
  `validate_linkml_instance`→`_handle_validate_instance`, begge nye,
  ekstraherte frå den gamle inline `tools/call`-blokka) og delegerer til
  `dispatch()`. Lokal `send()`/`main()` fjerna.
- `src/mcp-linkml-modell-utkast/server.py`: same mønster,
  `_TOOL_HANDLERS` = `{list_policies, generate_linkml}`
  (`_handle_list_policies` ny, ekstrahert frå inline-blokk).
- `src/mcp-linkml-begrep-utkast/server.py`: same mønster,
  `_TOOL_HANDLERS` med alle seks verktøy (`list_profiles` ekstrahert til
  ny `_handle_list_profiles`; `list_los_tema` wrappa i ein liten lambda
  sidan `_handle_list_los_tema` har ein annan signatur, `(msg_id)` utan
  `arguments`).
- Alle tre får no crash-isolasjon i hovudløkka (tidlegare berre
  validator) — stadfesta med eit direkte, isolert unit-forsøk mot
  `run_stdio_loop()` (ei melding som kastar ein uventa exception vert
  konvertert til ein `-32000`-feilrespons, påfølgjande meldingar vert
  framleis prosesserte).
- Montering av det nye modulet lagt til seks stader (Makefile ×2,
  make/60-mcp.mk ×2, new-modell.sh, tests/test_make.sh) — sjå Avgjerder.
- CI-cache-nøklar i `generate.yml`/`validate.yml` oppdaterte med den nye
  fila som avhengigheit.
- `actionlint` køyrt mot begge endra workflow-filer — berre
  føreeksisterande, urelaterte shellcheck-åtvaringar (linje 37/265 i
  `validate.yml`, ikkje i nærleiken av mi endring på linje 138).

**Verifisert empirisk** (ikkje berre lint/kompilering):
- `make mcp-linkml-valider-modell-smoke` — OK
- `make mcp-linkml-valider-modell-test` — 47/47 testar OK
- `pytest tests/test_mcp_server.py -k TestMCPProtocol` (ikkje kopla til
  noko make-target, køyrt manuelt for ekstra dekning) — 8/9 OK, 1
  føreeksisterande, urelatert feil (manglande `required`-felt i
  `TOOL_DEF`, uendra av denne refaktoreringa)
- `make mcp-linkml-modell-utkast-smoke` — OK, inkl. full `generate_linkml`
  med lint+dummy-validering
- `make mcp-linkml-modell-utkast-test` — 51/51 testar OK
- `make mcp-linkml-begrep-utkast-smoke` + manuelt utvida test av
  `list_profiles`, `opprett_begrep`, `sok_begrepskatalog`, `list_los_tema`
  — alle korrekte JSON-RPC-svar
- `make new-modell DOMAIN=oreg NAME=test-mcp-refaktor-tmp` (fullt
  scaffolding-løp via den endra `new-modell.sh`) — OK, testartefakt rydda
  opp etterpå
- `make roundtrip-json-schema JSONSCHEMA=<test-fixture>` (via den endra
  `tests/test_make.sh`) — OK, testartefakt rydda opp etterpå
- `batch-flatten-and-validate.py` køyrt direkte mot eit reelt skjema
  (`/repo`-monteringsvegen) — OK
- `make mcp-linkml-valider-modell SCHEMA=... POLICY=silver` (single-schema
  `flatten-and-validate.bash`-vegen) — OK, genererte valideringslogg rydda
  opp etterpå (biverknad av verifiseringa, ikkje ei tilsikta endring)

Ingen regresjonar funne. Alle testartefakt og genererte biverknader frå
verifiseringa er fjerna — `git status` syner berre dei tilsikta
kjeldeendringane.

**Rule-evaluering ved avslutning (jf. CLAUDE.md § Arbeidsflyt, steg 5a):**
brukaren stadfesta at kartlegginga av alle seks monteringsstader for det
nye påkravde delte modulet er eit konkret, generaliserbart mønster verdt å
fange som rule. `.claude/rules/container-images.md` utvida med ny seksjon
"Ein ny påkravd delt modul krev full kartlegging av alle monteringsstader"
+ `paths:` utvida til `make/60-mcp.mk`, `Makefile` og
`src/assets/scripts/scaffolding/**` (elles ville seksjonen ikkje lasta
automatisk ved arbeid med nettopp dei filene som var kjeldene til funnet).
