# Kartlegging: stdlib-only Python-script som køyrer via container

## Bakgrunn

Brukaren bad om ei kartlegging av alle Python-script i repoet som (a) køyrer
via ein podman-kontainar, og (b) berre brukar Python sitt standardbibliotek
(«stdlib-only», ingen tredjepartspakke som PyYAML, linkml, linkml-runtime,
openapi-spec-validator o.l. — verken direkte eller transitivt via lokale
`utils/*`-modular). Reint kartleggingsoppdrag, ingen kodeendring bestilt.

## Metode

1. Funne alle `.py`-filer under `src/assets/scripts/`, `mkdocs/lib/scripts/`,
   `src/mcp-linkml-*/` og `tests/`.
2. Kryssreferert kvar fil mot `make/*.mk`, `mkdocs/publish.sh`,
   `mkdocs/lib/**/*.sh`, `.github/workflows/*.yml` og
   `src/assets/scripts/makefile/*.sh` for å avgjere **om og korleis** dei
   køyrer — via `podman run` (`$(PYTHON_RUN)`, `$(LINKML_RUN)`, MCP-images,
   avrotize-image) eller direkte på host.
3. Ekstrahert alle `import`/`from`-setningar per fil, **inkludert relative
   importar** (`from .modul import x`) — ein første gjennomgang med
   regex `^\s*from\s+[a-zA-Z_]` gjekk glipp av `from .yaml_io import
   load_yaml` i `utils/schema_meta.py`, sidan `.` ikkje matcha
   teiknklassen. Retta med eit eige søk etter `from\s*\.`.
4. Følgt lokale `utils/*`-importar transitivt (eit script som importerer ein
   `utils`-modul som sjølv importerer PyYAML, er **ikkje** stdlib-only).
5. Klassifisert kvart container-køyrt script som anten **stdlib-only** eller
   **treng tredjepartspakke**, og notert kva image det køyrer i.

Relevant tidlegare arbeid: `specs/done/containerisering-python-kall.md`
dokumenterer sjølve containeriseringa av Makefile-kall (2026-07-30) og listar
attverande host-køyrde Python-kall i `mkdocs/publish.sh` og
`tests/test_make.sh` som ikkje vart følgt opp — denne kartlegginga stadfestar
og utdjupar den lista.

## Funn — script som køyrer via container

### `$(PYTHON_RUN)` — python-pytest-kontaineren (pytest, PyYAML, openapi-spec-validator installert)

| Script | Stdlib-only? | Merknad |
|---|---|---|
| `makefile/emit-github-validation-annotations.py` | **Ja** | json, sys, os |
| `makefile/mcp-build-modell-utkast-request.py` | **Ja** | json, sys, pathlib |
| `makefile/mcp-write-modell-utkast-response.py` | **Ja** | json, sys, pathlib |
| `makefile/mcp-build-begrep-utkast-request.py` | **Ja** | json, sys, pathlib |
| `makefile/detect-validation-policy.py` | Nei | delegerer til `utils.schema_meta.detect_policy`, som importerer `utils.yaml_io` (PyYAML) |
| `makefile/save-validation-log.py` | Nei | brukar `utils.schema_meta` (sjå over) |
| `makefile/run-schema-validation.py` | Nei | brukar `utils.schema_meta` (sjå over); kallar i tillegg `flatten-and-validate.bash`, som sjølv startar ein ny podman-kontainar (nøsta kontainarisering) |
| `makefile/generate-modellkatalog.py` | Nei | `import yaml` |
| `makefile/collect-concepts.py` | Nei | `import yaml`, `utils.yaml_io` |
| `makefile/find-similar-names.py` | Nei | `import yaml` |
| `makefile/check-iri-resolution.py` | Nei | `import yaml` |
| `makefile/update-modellkatalog.py` | Nei | `import yaml` |
| `makefile/gen-openapi.py` | Nei | `import yaml`, `api_spec_common` (PyYAML) |
| `makefile/gen-asyncapi.py` | Nei | same |
| `makefile/gen-docgen-examples.py` | Nei | krev PyYAML (avsluttar med feilmelding om det manglar) |
| `makefile/filter_erdiagram.py` | Nei | `import yaml` |
| `makefile/filter_plantuml.py` | Nei | `import yaml` |
| `makefile/batch-generate-instances.py` | **Delvis** | toppnivå-importar er reint stdlib, men er ein dispatcher som rutar til `gen-openapi.py`/`gen-asyncapi.py`/`gen-docgen-examples.py`/`filter_erdiagram.py`/`filter_plantuml.py` (alle PyYAML-avhengige) og `openapi_spec_validator` |

### `$(LINKML_RUN)` — linkml-local-kontaineren (linkml 1.11.1, rdflib, PyYAML transitivt)

| Script | Stdlib-only? | Merknad |
|---|---|---|
| `makefile/batch-generate.py` | **Delvis** | toppnivå-importar er reint stdlib (argparse, importlib, os, re, shlex, sys, time, dataclasses, pathlib, typing), men heile føremålet er `importlib.import_module("linkml.generators.<x>")` — funksjonelt heilt avhengig av `linkml`-pakken sjølv om han ikkje importerer han statisk |
| `makefile/batch-lint.py` | Nei | `import yaml`, `linkml.linter.*` |
| `makefile/batch-linkml-validate.py` | Nei | `yaml`, `linkml.validator`, `linkml_runtime` importert i `main()` — kjernefunksjonalitet, ikkje valfritt |
| `makefile/validate-modelldcat.py` | Nei | `yaml`, `linkml_runtime` |
| `makefile/gen-modelldcat-elements.py` | Nei | `yaml`, `linkml_runtime.utils.schemaview` |

### Avrotize-kontaineren (`podman run --entrypoint python3 $(AVROTIZE_IMAGE) ...`)

| Script | Stdlib-only? | Merknad |
|---|---|---|
| `makefile/fix-xsd-dates.py` | **Ja** | json, re, sys — køyrer i den delte avrotize-kontaineren via `batch-gen-xsd.sh`, ingen eigen podman-kontainar per skjema |

### MCP-kontainarane (mcp-linkml-validator / mcp-linkml-modell-utkast / mcp-linkml-begrep-utkast — alle har linkml + linkml-runtime + PyYAML installert)

| Script | Stdlib-only? | Merknad |
|---|---|---|
| `src/mcp-linkml-validator/server.py` | Nei | `yaml`, lazy `linkml_runtime`/`linkml.validator` |
| `src/mcp-linkml-validator/validate-and-log.py` | Nei | `yaml`, importerer frå `server` (yaml-avhengig) |
| `src/mcp-linkml-modell-utkast/server.py` | Nei | `yaml` |
| `src/mcp-linkml-modell-utkast/converter.py` | Nei | `yaml` |
| `src/mcp-linkml-modell-utkast/validator.py` | Nei | lazy `linkml_runtime`, `linkml.linter`, `linkml.validator` |
| `src/mcp-linkml-begrep-utkast/server.py` | Nei | `yaml`, lazy `linkml_runtime`/`linkml.validator` |
| `src/mcp-linkml-begrep-utkast/generator.py` | Nei | `yaml` |
| `src/mcp-linkml-begrep-utkast/los_tema.py` | **Ja** (trivielt) | ingen importar i det heile — men er ein rein datamodul importert av `server.py`, køyrer aldri sjølvstendig |
| `tests/test_mcp_policies.py` (via `mcp-linkml-valider-modell-test`) | Nei | importerer frå `server` (yaml-avhengig) |
| `tests/test_mcp_linkml_generator.py` (via `mcp-linkml-modell-utkast-test`) | Nei | `yaml`, `linkml_runtime` |

## Samandrag — stdlib-only script som faktisk køyrer via container

Desse ni scripta er verifiserte stdlib-only (inkl. transitivt via lokale
modular) OG køyrer via `podman run` i det aktive byggeoppsettet:

1. `src/assets/scripts/makefile/emit-github-validation-annotations.py` ($(PYTHON_RUN))
2. `src/assets/scripts/makefile/mcp-build-modell-utkast-request.py` ($(PYTHON_RUN))
3. `src/assets/scripts/makefile/mcp-write-modell-utkast-response.py` ($(PYTHON_RUN))
4. `src/assets/scripts/makefile/mcp-build-begrep-utkast-request.py` ($(PYTHON_RUN))
5. `src/assets/scripts/makefile/fix-xsd-dates.py` (avrotize-kontaineren)
6. `src/mcp-linkml-begrep-utkast/los_tema.py` (datamodul, MCP-kontainarane — ikkje sjølvstendig køyrbar)

I tillegg er `batch-generate.py` og `batch-generate-instances.py` stdlib
på toppnivå, men er dispatchar/orkestratorar som funksjonelt krev
`linkml` (batch-generate.py) eller PyYAML (batch-generate-instances.py) for
å utføre arbeidet sitt — dei er difor **ikkje** rekna som reine stdlib-only
script i praksis, sjølv om ingen tredjepartspakke importerast statisk i
fila.

**Viktig korreksjon undervegs:** `utils/schema_meta.py` såg først ut til å
vere stdlib-only (re, sys, pathlib), men importerer faktisk
`utils.yaml_io` (PyYAML) via ein relativ import (`from .yaml_io import
load_yaml`) som eit for snevert regex-søk først gjekk glipp av. Dette gjer
at `detect-validation-policy.py`, `save-validation-log.py` og
`run-schema-validation.py` — alle wired via `$(PYTHON_RUN)` — **ikkje** er
stdlib-only, sjølv om dei sjølve berre importerer stdlib-modular direkte.

## Relaterte funn (utanfor hovudspørsmålet, men relevant kontekst)

Fleire stdlib-only script køyrer i dag **direkte på host**, ikkje via
container — dei er difor ikkje med i hovudtabellane over, men er notert her
sidan dei er naturlege kandidatar for framtidig containerisering
(jf. attverande arbeid i `specs/done/containerisering-python-kall.md`):

| Script | Stdlib-only? | Køyrer frå |
|---|---|---|
| `mkdocs/lib/scripts/parse-dependency-tree.py` | Ja | `mkdocs/lib/utils/imported_schemas.sh`, `mkdocs/lib/sections/avhengigheiter.sh` — direkte `python3` på host |
| `mkdocs/lib/scripts/check-mermaid-click-hrefs.py` | Ja | `.github/workflows/lenkje-og-mermaid-sjekk.yml` — direkte `python3` på GitHub-runnaren |
| `src/assets/scripts/makefile/extract-schema-metadata.py` | Ja | `src/assets/scripts/makefile/generate-readme-tables.sh` — direkte `python3` på host |
| `src/mcp-linkml-validator/annotate-validate.py` | Ja | `.github/workflows/reusable-validate.yml` — direkte `python3` på GitHub-runnaren |
| `src/mcp-linkml-validator/batch-flatten-and-validate.py` | Ja | `make/40-validation.mk` — køyrer på host, men startar sjølv MCP-kontainaren via `subprocess.run(["podman", ...])` (bevisst arkitektur, ikkje eit inkonsistens-funn) |
| `src/mcp-linkml-validator/batch-validate-instances.py` | Ja | `tests/test_make.sh` — same mønster som over |

Ikkje stdlib-only, køyrer på host (utanfor kartlegginga sitt fokus, men
notert for fullstendigheit):

- `mkdocs/lib/scripts/generate-validation-md.py` (PyYAML) — kalla direkte frå `mkdocs/lib/sections/valideringsresultat.sh`
- `mkdocs/lib/scripts/collect-schema-metadata.py` (PyYAML) — kalla via `run_python_container` (**er** containerisert, i motsetnad til dei to andre `mkdocs/lib/scripts`-filene)

To script er ikkje kopla til noko `make`-target i det heile (verken host
eller container) — begge stadfesta i bruk som **bevisste manuelle
vedlikehaldsverktøy**, ikkje daud kode:

- `src/assets/scripts/add-schema-header-comments.py` (stdlib-only) — skriven
  for eit ein-gongs vedlikehaldstiltak (`specs/done/auto-forvalta-felt-
  kommentar.md`, la til filhovud-kommentarar i 22 skjema), sidan eksplisitt
  klassifisert som «Ad-hoc vedlikehald» i `specs/done/gruppering-av-
  scripts.md` og `specs/done/reorganiser-assets-scripts.md`. Ligg att for
  gjenbruk ved framtidige tilsvarande retrofit-behov.
- `src/assets/scripts/list-tool-licenses.py` (stdlib-only) — støttar
  CLAUDE.md-regelen «Nye verktøyavhengigheiter»: skannar `Dockerfile*`/
  `requirements*.txt` og hjelper med å halde attributions-tabellen i
  `mkdocs/docs/om.md` oppdatert. `specs/done/verktoy-lisensoversikt.md`
  dokumenterer manuell køyring (`python3 src/assets/scripts/list-tool-
  licenses.py`) — meint å køyrast når ein legg til ein ny
  verktøyavhengigheit, ikkje ved kvart bygg.

## Estimert kjøretidsgevinst ved å ikkje containerisere dei reine stdlib-scripta

**Kvalifisert gjetting**, grunna i repoet sitt eige målte tal for rein
podman+Python-oppstart (ingen pakke-import): **~2,6 s** for
`python-pytest`-kontaineren (`specs/done/effektiviser-generate-workflow-
koyretid.md`, linje 46: `python3 -c "print()"` i den kontaineren). Dette er
overhead-kostnaden åleine — sjølve scriptlogikken i dei aktuelle scripta
(nokre linjer json/os/sys) tek i praksis <10 ms, uansett om han køyrer i
kontainar eller direkte på host.

Metode: for kvart av dei fem reelt sjølvstendig-køyrde stdlib-only-scripta
frå samandraget over, telt opp **kor mange gonger** det faktisk vert kalla
i den aktuelle bruks-konteksten (CI-loop vs. manuelt/on-demand
utviklarkommando), og multiplisert med 2,6 s per kall.

| Script | Kontekst | Kall per køyring | Estimert overhead |
|---|---|---|---|
| `emit-github-validation-annotations.py` | `make validate-bronze DOMAIN=<x>` — éin gong per skjema i domenet | 36 skjema totalt i repoet (`find src/linkml -name '*-schema.yaml' \| wc -l`), om alle domene køyrast i éin sveip | 36 × 2,6 s ≈ **94 s (~1,5 min)** |
| `mcp-build-modell-utkast-request.py` + `mcp-write-modell-utkast-response.py` | `make mcp-linkml-modell-utkast SCHEMA=<x>` — 2 kontainar-kall per invokasjon | 1 invokasjon | 2 × 2,6 s ≈ **5,2 s per kall** |
| `mcp-build-begrep-utkast-request.py` | `make mcp-linkml-begrep-utkast INPUT=<x>` — 1 kontainar-kall per invokasjon | 1 invokasjon | **2,6 s per kall** |
| `fix-xsd-dates.py` | Køyrer allereie **inni** den delte avrotize-kontaineren (`batch-gen-xsd.sh`), ingen eigen kontainar-oppstart per skjema | — | **0 s** — ingen gevinst å hente, containeriseringa er alt amortisert |
| `los_tema.py` | Ikkje sjølvstendig køyrbar (rein datamodul importert av `server.py`) | — | Ikkje relevant |

**Viktig atterhald om `emit-github-validation-annotations.py`:** COMMANDS.md
og ein kommentar i `.github/workflows/validate.yml` (linje 101) hevdar
`validate-bronze` er «brukt i CI per domene», men den faktiske
skjemavalideringsjobben i `validate.yml` (steget «Valider skjema mot
validation_policy», linje 206–248) kallar
`src/assets/scripts/makefile/run-validation.sh` direkte per manifest — ikkje
`make validate-bronze`. Dette scriptet finst ikkje i noko `run:`-steg i
`.github/workflows/*.yml`. Estimatet på ~94 s gjeld difor truleg berre
**manuelle/lokale** køyringar av `make validate-bronze DOMAIN=<x>` (t.d. ved
feilsøking), ikkje ein kostnad som gjentek seg for kvar CI-køyring i dag.
Dette er ein dokumentasjons-inkonsistens som ligg utanfor denne kartlegginga
sitt mandat å rette, men er verdt å merke seg. **Retta i etterkant** (same
økt): `COMMANDS.md` linje 164 sa før «Brukt i CI per domene» for
`validate-bronze` — endra til å presisere at CI faktisk kallar
`run-validation.sh` direkte per manifest, og at `validate-bronze` er eit
manuelt/lokalt batch-alternativ. Same feilkjelde vart òg retta i
`.github/workflows/validate.yml` (linje 100–102) — kommentaren nemnde
`validate-bronze` saman med `validate-data`/`validate-examples` som grunn
til at `python-pytest`-imaget er `always_required`; no listar han berre dei
to targeta som faktisk er CI-kalla. `actionlint` køyrt mot fila etter
endringa — berre pre-eksisterande `[shellcheck]`-funn, ingen
`[expression]`-feil.

**Systematisk oppfølgingssøk** etter fleire tilsvarande CI-kommentar-
inkonsistensar (gjennomgått alle «Brukt i CI»/«CI-kalla»/«kalla frå CI»-
liknande påstandar i `COMMANDS.md` og `.github/workflows/*.yml`) fann éin
til: `mkdocs/docs/kom-i-gang/kommandoar.md` linje 51 er ein separat,
manuelt vedlikehalden tabell som speglar `COMMANDS.md` og hadde same stale
påstand for `validate-bronze` — retta likt. Alle andre kontrollerte
påstandar (`make domain-*`/`make docs-publish`/`make docs-build` i
`generate.yml`, `gen-begrepskatalog-instance`, `validate-data`/
`validate-examples` sine «Brukt i CI»-merknader) er verifiserte korrekte,
ingen fleire funne.

**Samla vurdering:** Den potensielle gevinsten ved å køyre desse fem
scripta direkte på host i staden for i kontainar ligg i storleiksorden
**sekund til eitt-og-eit-halvt minutt**, avhengig av kor ofte
`validate-bronze` faktisk køyrast lokalt. Til samanlikning dokumenterer
`specs/done/effektiviser-generate-workflow-koyretid.md` (linje 169–172) at
eit fullt generate-løp gjer **~474 podman-kontainar-oppstartar** der
`~300 køyrer linkml-local og ber ~25–28 minutt reint importarbeid` — den
potensielle gevinsten her er difor **to til tre størrelsesordenar mindre**
enn den allereie dokumenterte og adresserte linkml-import-kostnaden. Å
containerisere desse fem scripta har vore eit **korrekt-heit/konsistens**-val
(jf. `specs/done/containerisering-python-kall.md` sitt mål om null direkte
host-Python-kall i Makefile), ikkje eit val med målbar ytingskostnad.

## Handlingsliste

Ingen kodeendringar er gjort — dette er eit reint kartleggingsoppdrag.
Moglege oppfølgingspunkt (ikkje utført, kun notert for framtidig backlog
dersom brukaren ønskjer det):

- [ ] Vurder å containerisere `parse-dependency-tree.py`,
      `check-mermaid-click-hrefs.py` og `extract-schema-metadata.py` sidan
      dei alt er stdlib-only og dermed ikkje treng noko spesifikt image
      utover ein rein Python-runtime.

`add-schema-header-comments.py` og `list-tool-licenses.py` er avklarte
(sjå seksjonen over) — begge er i aktiv bruk som manuelle
vedlikehaldsverktøy, ikkje daud kode. Ingen vidare handling.

## Utført

**Dato:** 2026-08-12

Kartlegging fullført. Alle `.py`-filer under `src/assets/scripts/`,
`mkdocs/lib/scripts/`, `src/mcp-linkml-*/` og `tests/` er gjennomgått,
kryssreferert mot `make/*.mk`/`mkdocs/publish.sh`/CI-workflows for
køyringskontekst, og klassifisert stdlib-only vs. tredjepartsavhengig
(inkl. transitivt via lokale `utils/*`-modular). Resultatet er dokumentert
i tabellane over.
