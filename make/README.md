# make/

Modularisert Makefile-system for linkml-datamodellering-no.

## Struktur

Makefile er delt i 13 tematiske modular:

| Modul | Føremål |
|---|---|
| `00-settings.mk` | Globale variablar (fargar, katalogar, parallellisering) |
| `01-containers.mk` | Container-image-namn og køyre-kommandoar (LINKML_RUN, PYTHON_RUN, osv.) |
| `02-schema-discovery.mk` | Søk opp alle skjema og domene i `src/linkml/` |
| `03-output.mk` | Logging-makroar (print_header, print_step) |
| `10-generator-macros.mk` | Generelle makroar for å køyre LinkML-generatorar parallelt |
| `11-generator-targets.mk` | Target for spesifikke generatorar (gen-jsonschema, gen-owl, osv.) |
| `20-domain-targets.mk` | Target per domene (domain-ap-no, domain-fint, osv.) med pre-hooks |
| `30-instances.mk` | Generering og validering av instansdata (Informasjonsmodell, modellkatalog) |
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
| `generate-informasjonsmodell.py` | `gen-informasjonsmodell-instance` | Generer ModelDCAT-AP-NO-metadata frå schema.annotations |
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

# Generer artefaktar for eit domene
make domain-ap-no

# Generer dokumentasjon for eit skjema
make gen-docs SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml

# Valider eit skjema med MCP-validator
make mcp-linkml-valider-modell SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml

# Bygg og publiser dokumentasjonsportal
make docs-publish
```

## Legge til ny modul

1. Opprett `make/XX-namn.mk` med header-kommentar:
   ```makefile
   # ==============================================================================
   # make/XX-namn.mk
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

2. Legg til `include make/XX-namn.mk` i `Makefile` (i riktig rekkefølgje)

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

- **Target-namn:** Bruk `kebab-case` (gen-docs, validate-instance)
- **Interne target:** Prefiks med `_` (_gource-render, _mcp-valider-modell-with-header)
- **Logging:** Bruk `print_header`/`print_step` frå `03-output.mk` for overskrifter/steg, og
  `log_info`/`log_debug`/`log_error` frå `LOG_FUNCTIONS` (`00-settings.mk`) for status/feil —
  aldri rå `echo`/`printf` (jf. CLAUDE.md § «Ingen stille feil»)
- **Parallellisering:** Bruk `$(PARALLEL)` frå `00-settings.mk` (default 8)
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
- **Løysing:** Legg til `##`-kommentar etter target-namnet

**Problem:** Parallellisering feiler på Windows/WSL2
- **Løysing:** Reduser `PARALLEL`: `make domain-ap-no PARALLEL=2`
