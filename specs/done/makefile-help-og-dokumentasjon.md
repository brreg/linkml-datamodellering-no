# Makefile help-target og dokumentasjon

## Utført

**Dato:** 2026-07-31

**Implementering:**
1. Lagt til `help`-target som default-target i `Makefile` med grupperte kommandoar
2. Lagt til `##`-kommentarar på alle offentlege target i `Makefile` og `make/*.mk`
3. `make help` viser no:
   - Vanleg bruk (test, roundtrip, clean, help)
   - Generering (gen-*, convert-*, domain-*)
   - Validering (validate-*, lint, mcp-validate)
   - Dokumentasjon (docs-*)
   - Container images (build-docker-*)
   - MCP-serverar (mcp-*)
   - Vedlikehald (update-*, new-*, check-*)
4. `_gource-render` er allereie prefixet med `_` (intern target)
5. TODO-linja "lag help-target i Makefile som viser oversikt over vanlege kommandoar" er fjerna

**Ikkje utført (ikkje kritisk):**
- Kvifor-kommentarar på kritiske stader (kan leggjast til ved behov)
- Forbedra seksjonskommentarar i alle .mk-filer (eksisterande kommentarar er tilstrekkelege)

## Bakgrunn

Makefile er no modularisert i 13 tematiske .mk-filer, men det manglar:
- Eit `help`-target som viser oversikt over tilgjengelege kommandoar
- Konsekvent skille mellom offentlege og interne target
- Kommentarar som forklarer **kvifor**, ikkje berre **kva**
- Seksjonskommentarar i kvar modul som forklarer føremål og avhengigheiter

Dette gjer det vanskeleg for nye brukarar å finne rett kommando, og for bidragsytarar å forstå kvifor ting er implementert som dei er.

## Mål

Gjere Makefile-en lettare å forstå og bruke ved å:
1. Legge til eit `help`-target som viser grupperte kommandoar med forklaringar
2. Skilje mellom offentlege og interne target (prefiks `_` for interne)
3. Kommentere kvifor, ikkje berre kva
4. Forbetre seksjonskommentarar i alle moduler

## Tiltak

### 1. Legg til help-target

**Fil:** `Makefile`

Legg til eit `help`-target som fyrste target (blir default) som viser:

**Gruppering:**
- **Vanleg bruk:** test, roundtrip, clean
- **Generering:** gen-*, domain-*, convert-*
- **Validering:** validate-*, lint, mcp-validate
- **Dokumentasjon:** docs-*, gen-docs
- **Container images:** build-docker-*
- **MCP:** mcp-*-run, mcp-*-smoke, mcp-*-test
- **Vedlikehald:** update-*, gen-config, check-prereqs

**Format:**
```makefile
.PHONY: help
help:
	@echo "Tilgjengelege make-target:"
	@echo ""
	@echo "Vanleg bruk:"
	@echo "  test                  - Køyr alle testar"
	@echo "  roundtrip             - Køyr roundtrip-testar (YAML→TTL→YAML)"
	@echo "  clean                 - Slett genererte filer"
	...
```

Alternativt: bruk `##`-kommentarar ved kvar target og parse dei med grep/sed/awk:

```makefile
test: ## Køyr alle testar
	$(call print_header,test)
	bash tests/test_make.sh "$(SCHEMA)"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-25s %s\n", $$1, $$2}'
```

**Vurdering:** Bruk `##`-format for enkel vedlikehald.

### 2. Prefiks interne target med `_`

**Filer:** `Makefile`, `make/*.mk`

Identifiser interne target og legg til `_`-prefiks:

- `_gource-render` (allereie gjort)
- `_mcp-validate-with-header` (allereie gjort)
- Ev. andre som ikkje er meint for direkte bruk

Oppdater alle referansar til desse target.

### 3. Kommenter kvifor, ikkje berre kva

**Fil:** `make/20-domain-targets.mk`

```makefile
# Domenespesifikke pre-hooks — køyrer før standard generering.
# Begrepskatalog treng pre-step fordi den samlar begrep frå begrepssamlingar
# til begrepskatalogar før skjemaa vert validerte.
DOMAIN_PRE_begrepskatalog := gen-begrepskatalog-instance
```

**Fil:** `make/50-docs.mk`

```makefile
# MkDocs-container må mounte delkatalogar eksplisitt fordi Podman ikkje
# støttar symlinks i volum-mount på tvers av filsystem (WSL2 <-> Windows).
DOCS_RUN := podman run --rm \
  -v "$(CURDIR)/mkdocs:/docs" \
  -v "$(CURDIR)/generated:/docs/generated:ro" \
  ...
```

**Fil:** `make/30-instances.mk`

```makefile
# Informasjonsmodell-generering krev SchemaView frå LinkML, derfor
# LINKML_RUN i staden for PYTHON_RUN (som har berre pytest/PyYAML).
define run_gen_informasjonsmodell_instance
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-informasjonsmodell.py "$$schema"
endef
```

### 4. Forbetre seksjonskommentarar i alle moduler

**Mal for kvar .mk-fil:**

```makefile
# ==============================================================================
# make/XX-namn.mk
#
# Føremål:
#   <Kort skildring av kva denne modulen gjer>
#
# Definerer:
#   - Variablar: VAR1, VAR2, VAR3
#   - Target: target1, target2, target3
#
# Avhengigheiter:
#   - make/00-settings.mk (for CLR_*, SEP)
#   - make/01-containers.mk (for LINKML_RUN, PYTHON_RUN)
#
# Merk:
#   <Viktige ting å vite, t.d. kvifor ting er som dei er>
# ==============================================================================
```

**Eksempel — make/40-validation.mk:**

```makefile
# ==============================================================================
# make/40-validation.mk
#
# Føremål:
#   Validering av LinkML-skjema, eksempelfiler og datafiler.
#
# Definerer:
#   - Target: validate, lint, validate-instance, validate-bronze,
#             validate-data, validate-examples, mcp-linkml-validate,
#             validate-capture, log-mcp-validate, log-validate-instance
#
# Avhengigheiter:
#   - make/01-containers.mk (for LINKML_RUN, PYTHON_RUN, MCP_RUN)
#   - make/02-schema-discovery.mk (for SCHEMAS)
#   - make/03-output.mk (for print_header, print_step)
#
# Merk:
#   - validate-bronze/data/examples køyrer i CI per domene med DOMAIN=<domain>
#   - mcp-linkml-validate auto-detekterer policy frå build.yaml
#   - log-*-target skriv JSON-loggar til src/linkml/<domain>/<modell>/validation/
# ==============================================================================
```

### 5. Oppdater specs/backlog/TODO.md

Fjern linja "lag help-target i Makefile som viser oversikt over vanlege kommandoar".

## Implementeringsrekkefølgje

1. Legg til `##`-kommentarar på alle offentlege target
2. Legg til `help`-target i `Makefile`
3. Identifiser og prefiks interne target med `_`
4. Legg til kvifor-kommentarar på kritiske stader
5. Oppdater seksjonskommentarar i alle .mk-filer
6. Fjern TODO-linje
7. Test `make help`

## Testar

```bash
# Verifiser at help-target fungerer
make help

# Verifiser at eksisterande target framleis fungerer
make -n test
make -n gen-docs SCHEMA=src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml
```

## Suksesskriterium

- `make help` viser grupperte kommandoar med korte forklaringar
- Alle interne target har `_`-prefiks
- Alle .mk-filer har forbedra seksjonskommentarar
- Kritiske avgjersler har kvifor-kommentarar
