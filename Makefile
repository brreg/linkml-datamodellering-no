# ==============================================================================
# Makefile
#
# Hovud-byggefil for linkml-datamodellering-no.
# Modular (settings, containers, generators, osv.) er inkluderte frå make/*.mk.
# ==============================================================================

SHELL       := /bin/bash
.SHELLFLAGS := -o pipefail -c

# Inkluder modular i rett rekkefølgje
include make/00-settings.mk
include make/01-containers.mk
include make/02-schema-discovery.mk
include make/03-output.mk

# Inkluder generert konfigurasjon (valgfri)
-include config.mk

# Inkluder generator-makroar
include make/10-generator-macros.mk
include make/11-generator-targets.mk

# Inkluder domain-targets
include make/20-domain-targets.mk

# Inkluder instans-, validerings- og docs-targets
include make/30-instances.mk
include make/40-validation.mk
include make/50-docs.mk

# Inkluder MCP, scaffolding, images og tools
include make/60-mcp.mk
include make/70-scaffolding.mk
include make/80-images.mk
include make/90-tools.mk

# ---------------------------------------------------------------------------
# Top-level targets
# ---------------------------------------------------------------------------
LINKML_MOD_DIR   := src/mcp-linkml-modell-utkast
LINKML_MOD_IMAGE := mcp-linkml-modell-utkast
LINKML_MOD_RUN   := podman run -i --rm \
  -v "$(CURDIR)/$(LINKML_MOD_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(LINKML_MOD_DIR)/converter.py:/app/converter.py:ro" \
  -v "$(CURDIR)/$(LINKML_MOD_DIR)/validator.py:/app/validator.py:ro" \
  -v "$(CURDIR)/$(LINKML_MOD_DIR)/profiles:/app/profiles:ro"

LINKML_BEGREP_DIR   := src/mcp-linkml-begrep-utkast
LINKML_BEGREP_IMAGE := mcp-linkml-begrep-utkast
LINKML_BEGREP_RUN   := podman run -i --rm \
  -v "$(CURDIR)/$(LINKML_BEGREP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(LINKML_BEGREP_DIR)/generator.py:/app/generator.py:ro" \
  -v "$(CURDIR)/$(LINKML_BEGREP_DIR)/los_tema.py:/app/los_tema.py:ro" \
  -v "$(CURDIR)/$(LINKML_BEGREP_DIR)/profiles:/app/profiles:ro" \
  -v "$(CURDIR):/repo:ro"

.PHONY: help test roundtrip validate lint validate-instance clean gen-config \
		gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl gen-rdf gen-erdiagram convert-rdf convert-data gen-docs \
        gen-proto gen-plantuml gen-xsd gen-asyncapi gen-openapi \
        validate-bronze validate-data validate-examples \
        build-docker-linkml build-docker-python build-docker-avrotize build-docker-asyncapi build-docker-mkdocs build-docker-plantuml \
        build-docker-mcp-validator build-docker-mcp-modell-utkast build-docker-mcp-begrep-utkast build-docker-gource \
        mcp-linkml-validate-run mcp-linkml-validate-smoke mcp-linkml-validate-test mcp-linkml-validate \
        mcp-linkml-modell-utkast-run mcp-linkml-modell-utkast-smoke mcp-linkml-modell-utkast-test mcp-linkml-modell-utkast new-model \
        mcp-linkml-begrep-utkast-run mcp-linkml-begrep-utkast-smoke mcp-linkml-begrep-utkast-list-profiles mcp-linkml-begrep-utkast \
		docs-serve docs-build docs-publish \
        check-published-uris check-prereqs \
        update-modellkatalog gen-dqv-measurements gen-modelldcat-elements new-modellkatalog new-begrepskatalog \
        validate-capture \
        build-docker-gource gource-preview gource-video _gource-render

.DEFAULT_GOAL := help

help: ## Vis oversikt over tilgjengelege make-target
	@echo "$(CLR_HDR)Tilgjengelege make-target:$(CLR_RST)"
	@echo ""
	@bash src/assets/scripts/makefile/help.sh $(MAKEFILE_LIST)

test: ## Køyr alle testar
	$(call print_header,test)
	bash tests/test_make.sh "$(SCHEMA)"

roundtrip: ## Køyr roundtrip-testar (YAML→TTL→YAML) [SCHEMA=<sti>]
	$(call print_header,roundtrip,$(if $(SCHEMA),SCHEMA=$(SCHEMA),(alle skjema)))
	TEST_FILTER=roundtrip bash tests/test_make.sh "$(SCHEMA)"

roundtrip-json-schema: ## Køyr JSON Schema roundtrip-testar [JSONSCHEMA=<sti>]
	$(call print_header,roundtrip-json-schema,$(if $(JSONSCHEMA),JSONSCHEMA=$(JSONSCHEMA),(alle JSON Schema i src/tmp)))
	TEST_FILTER=roundtrip-json-schema bash tests/test_make.sh "$(JSONSCHEMA)"

# ---------------------------------------------------------------------------
# Generator targets (genererte av make_gen_target) — gamle definisjonar fjerna
# ---------------------------------------------------------------------------
# Image-bygging, MCP, scaffolding og verktøy flytta til make/*.mk
# ---------------------------------------------------------------------------

convert-rdf: ## Konverter eksempelfiler frå YAML til RDF/Turtle
	$(call print_header,convert-rdf)
	@SCHEMA_DIR=$(SCHEMA_DIR) GEN_DIR=$(GEN_DIR) bash src/assets/scripts/makefile/convert-examples.sh | \
	while IFS=$$'\t' read -r schema example out; do \
		echo "$(CLR_STEP)→ linkml-convert  $$example$(CLR_RST)"; \
		echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate --output $$out $$example"; \
		$(LINKML_RUN) linkml-convert \
			--schema $$schema \
			--output-format ttl \
			--no-validate \
			--output $$out \
			$$example; \
	done

convert-data: ## Konverter datafiler (data/*/*.yaml) frå YAML til RDF/Turtle
	$(call print_header,convert-data)
	@for datadir in $$(find $(SCHEMA_DIR) -mindepth 4 -maxdepth 4 -type d -path '*/data/*' | sort); do \
		domain=$$(echo "$$datadir" | awk -F/ '{print $$3}'); \
		model=$$(echo "$$datadir" | awk -F/ '{print $$4}'); \
		catalog=$$(basename "$$datadir"); \
		manifest="$$datadir/build.yaml"; \
		[ -f "$$manifest" ] || continue; \
		publish_external=$$(grep '^publish_external:' "$$manifest" | awk '{print $$2}'); \
		[ "$$publish_external" = "true" ] || continue; \
		datafile="$$datadir/$$catalog.yaml"; \
		[ -f "$$datafile" ] || continue; \
		schema=$(SCHEMA_DIR)/$$domain/$$model/$$model-schema.yaml; \
		mkdir -p $(GEN_DIR)/$$domain/$$catalog; \
		echo "$(CLR_STEP)→ linkml-convert  $$datafile$(CLR_RST)"; \
		echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate --output $(GEN_DIR)/$$domain/$$catalog/$$catalog.ttl $$datafile"; \
		$(LINKML_RUN) linkml-convert \
			--schema $$schema \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/$$domain/$$catalog/$$catalog.ttl \
			$$datafile; \
	done

clean: ## Slett alle genererte filer (generated/)
	$(call print_header,clean)
	rm -rf $(GEN_DIR)

update-modellkatalog: ## Oppdater modellkatalog frå schema.annotations.*
	$(call print_header,update-modellkatalog)
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/update-modellkatalog.py

gen-dqv-measurements: ## Generer DQV-kvalitetsmålingar for datafiler
	$(call print_header,gen-dqv-measurements)
	$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-dqv-measurements.py

gen-modelldcat-elements: ## Generer ModelDCAT-AP-NO-modellelement [ORG=<alias>] [DRYRUN=1]
	$(call print_header,gen-modelldcat-elements,$(if $(ORG),ORG=$(ORG))$(if $(DRYRUN), DRYRUN=$(DRYRUN)))
	$(LINKML_RUN) python3 src/assets/scripts/makefile/gen-modelldcat-elements.py $(if $(ORG),--org $(ORG)) $(if $(DRYRUN),--dry-run)


# ---------------------------------------------------------------------------
# Per-model generator configuration — regenerated when any build.yaml changes.
# ---------------------------------------------------------------------------
config.mk: $(shell find src/linkml -name 'build.yaml')
	@bash src/assets/scripts/makefile/gen-config.sh > config.mk

gen-config: config.mk

# ---------------------------------------------------------------------------
# Per-domain targets – generated automatically in make/20-domain-targets.mk
# New domains appear automatically when schemas are added under src/linkml/.
# ---------------------------------------------------------------------------


# ===========================================================================
# MCP, scaffolding, images og verktøy flytta til make/*.mk
# ===========================================================================

