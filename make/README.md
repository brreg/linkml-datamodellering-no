# make/

Modularisert Makefile-system for linkml-datamodellering-no.

## Struktur

Makefile er delt i 13 tematiske modular:

| Modul | Føremål |
|---|---|
| `00-settings.mk` | Globale variablar (fargar, katalogar, parallellisering) |
| `01-containers.mk` | Container-image-navn og køyre-kommandoar (LINKML_RUN, PYTHON_RUN, osv.) |
| `02-schema-discovery.mk` | Søk opp alle skjema og domene i `src/linkml/` |
| `03-output.mk` | Logging-makroar (print_header, print_step) |
| `10-generator-macros.mk` | Generelle makroar for å køyre LinkML-generatorar — dei linkml-baserte (merge, jsonld-context, shacl, python, json-schema, owl, rdf, proto, erdiagram, plantuml, doc) batchar N skjema inn i éin kontainar via `batch-generate.py`; python-etterhandsaming (erdiagram-filter, plantuml-filter, docgen-examples, openapi, asyncapi) batchar via `batch-generate-instances.py`; berre gen-xsd og `asyncapi validate` køyrer framleis udelt via `run-parallel-gen.sh` (éin aktivert skjema kvar, ingenting å vinne) |
| `11-generator-targets.mk` | Target for spesifikke generatorar (gen-jsonschema, gen-owl, osv.) |
| `20-domain-targets.mk` | Target per domene (domain-ap-no, domain-fint, osv.) med pre-hooks — sjølve genereringspipelinen er delegert til `run-domain-pipeline.sh`, som fase-parallelliserer dei uavhengige batch-gruppene (rekursive `$(MAKE) DOMAIN=...`-kall) |
| `30-instances.mk` | Generering og validering av instansdata (Informasjonsmodell, modellkatalog) — Informasjonsmodell-generering batchar N skjema inn i éin kontainar via `batch-generate-instances.py` |
| `40-validation.mk` | Validering av skjema, eksempel og data |
| `50-docs.mk` | MkDocs-dokumentasjonsportal (serve, build, publish) |
| `60-mcp.mk` | MCP-serverar (validator, modell-utkast, begrep-utkast) |
| `70-scaffolding.mk` | Scaffolding av nye modellar og katalogar |
| `80-images.mk` | Container-image-bygging (linkml, python, avrotize, osv.) |
| `90-tools.mk` | Verktøy (Gource, prereq-sjekk) |

## Relaterte script

Python og bash-script brukt av make-target ligg i **`src/assets/scripts/makefile/`**.

Viktige script:

| Script | Brukt av | Føremål |
|---|---|---|
| `batch-generate.py` | `gen-shacl`, `gen-owl`, `gen-rdf`, `gen-python`, `gen-jsonschema`, `gen-jsonld-context`, `gen-proto`, `gen-erdiagram`/`gen-plantuml` (rå-generering), `gen-docs` (sjølve gen-doc), `domain_target` (merge) | Batch-generer linkml-baserte artefakt for N skjema i éin kontainar-prosess (Click-API direkte, ikkje CLI-subprosess per skjema) |
| `batch-generate-instances.py` | `gen-informasjonsmodell-instance`, `gen-openapi`, `gen-asyncapi` (generering), `gen-docs` (docgen-examples-fasen), `gen-erdiagram`/`gen-plantuml` (filter-fasen), `domain_target` (linkml-convert) | Batchar dei ikkje-linkml PYTHON_RUN-scripta (under) for N skjema i éin kontainar-prosess |
| `batch-render-plantuml.sh` | `gen-plantuml` (SVG-render-fasen) | Batchar PlantUML SVG-rendering for N skjema sine `.puml`-filer i éitt `podman run`-kall |
| `run-domain-pipeline.sh` | `domain-<domain>` | Fase-parallelliserer dei uavhengige gen-*-gruppene for eit domene (rekursive `$(MAKE)`-kall, PID-array + wait) |
| `generate-informasjonsmodell.py` | `gen-informasjonsmodell-instance` (via `batch-generate-instances.py`) | Generer ModelDCAT-AP-NO-metadata frå schema.annotations |
| `update-modellkatalog.py` | `update-modellkatalog` | Oppdater modellkatalog frå alle skjema |
| `gen-dqv-measurements.py` | `gen-dqv-measurements` | Generer DQV-kvalitetsmålingar for datafiler |
| `collect-concepts.py` | `gen-begrepskatalog-instance` | Samle begrep frå begrepssamlingar til begrepskatalogar |
| `run-schema-validation.py` | `validate-capture` | Køyr MCP-validering parallelt med logging |
| `detect-validation-policy.py` | `mcp-linkml-valider-modell` | Auto-detekter policy frå build.yaml |
| `gen-config.sh` | `gen-config` | Generer config.mk frå build.yaml-filer |
| `check-prereqs.bash` | `check-prereqs` | Sjekk at nødvendige verktøy er installerte |

Sjå `src/assets/scripts/makefile/` for komplette liste.

## Bruk

```bash
# Vis alle tilgjengelege target
make help

# Køyr alle testar
make test

# Generer artefakter for eit domene
make domain-ap-no

# Generer dokumentasjon for eit skjema
make gen-docs SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml

# Valider eit skjema med MCP-validator
make mcp-linkml-valider-modell SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml

# Bygg og publiser dokumentasjonsportal
make docs-publish
```

## Legge til ny modul

1. Opprett `make/XX-navn.mk` med header-kommentar:
   ```makefile
   # ==============================================================================
   # make/XX-navn.mk
   #
   # Føremål:
   #   <Kort skildring>
   #
   # Definerer:
   #   - Variablar: VAR1, VAR2
   #   - Target: target1, target2
   #
   # Avhengigheiter:
   #   - make/00-settings.mk (for CLR_*, SEP)
   # ==============================================================================
   ```

2. Legg til `include make/XX-navn.mk` i `Makefile` (i riktig rekkefølgje)

3. Legg til `##`-kommentarar på offentlege target:
   ```makefile
   my-target: ## Kort skildring av kva target gjer
       $(call print_header,my-target)
       @echo "Gjer noko nyttig"
   ```

4. Prefiks interne target med `_`:
   ```makefile
   _internal-helper:
       @echo "Dette er ikkje meint for direkte bruk"
   ```

## Konvensjonar

- **Target-navn:** Bruk `kebab-case` (gen-docs, validate-instance)
- **Interne target:** Prefiks med `_` (_gource-render, _mcp-valider-modell-with-header)
- **Logging:** Bruk `print_header`/`print_step` frå `03-output.mk` for overskrifter/steg, og
  `log_info`/`log_debug`/`log_error` frå `LOG_FUNCTIONS` (`00-settings.mk`) for status/feil —
  aldri rå `echo`/`printf` (jf. CLAUDE.md § «Ingen stille feil»)
- **Container-køyring:** Bruk `*_RUN`-variablar frå `01-containers.mk` (LINKML_RUN, PYTHON_RUN)
- **Wrapper-target:** target som delegerer til eit anna target via eit rekursivt
  `$(MAKE) <target>`-kall (t.d. `mcp-linkml-valider-modell` → `_mcp-valider-modell-with-header`,
  `gource-preview`/`gource-video` → `_gource-render`) er dokumenterte samla i
  `COMMANDS.md` § «Wrapper-target» — sjå der for full liste og for skilnaden mellom
  det rekursive `$(MAKE)`-mønsteret og det vanlege Make-prerequisite-mønsteret

## Feilsøking

**Problem:** `make domain-ap-no` feiler med "No such file or directory"
- **Løysing:** Køyr `make build-docker-linkml` for å bygge LinkML-container

**Problem:** `make help` viser ikkje mitt nye target
- **Løysing:** Legg til `##`-kommentar etter target-navnet

