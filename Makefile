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

# Inkluder generert konfigurasjon (valgfri)
-include config.mk

# Inkluder generator-makroar
include make/10-generator-macros.mk
include make/11-generator-targets.mk

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

PARALLEL ?= 8

.PHONY: test roundtrip validate lint validate-instance clean gen-config \
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

test:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	bash tests/test_make.sh "$(SCHEMA)"

# Bruk: make roundtrip [SCHEMA=<sti-til-skjema>]
roundtrip:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make roundtrip$(if $(SCHEMA),  SCHEMA=$(SCHEMA),  (alle skjema))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	TEST_FILTER=roundtrip bash tests/test_make.sh "$(SCHEMA)"

# Bruk: make roundtrip-json-schema [JSONSCHEMA=<sti-til-json-schema>]
roundtrip-json-schema:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make roundtrip-json-schema$(if $(JSONSCHEMA),  JSONSCHEMA=$(JSONSCHEMA),  (alle JSON Schema i src/tmp))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	TEST_FILTER=roundtrip-json-schema bash tests/test_make.sh "$(JSONSCHEMA)"

validate:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make validate$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@$(foreach s,$(SCHEMAS),echo "$(CLR_STEP)→ merge-imports  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-linkml $(s) > /dev/null" && $(LINKML_RUN) gen-linkml $(s) > /dev/null;)

# Bruk: make lint [SCHEMA=<sti-til-skjema>]
lint:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make lint$(if $(SCHEMA),  SCHEMA=$(SCHEMA),  (alle skjema))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@if [ -n "$(SCHEMA)" ]; then \
		$(LINKML_RUN) linkml lint --config src/assets/containers/.linkmllint.yaml "$(SCHEMA)"; \
	else \
		$(foreach s,$(SCHEMAS),$(LINKML_RUN) linkml lint --config src/assets/containers/.linkmllint.yaml "$(s)" &&) true; \
	fi

# Bruk: make validate-instance SCHEMA=<sti-til-skjema> INSTANCE=<sti-til-datafil>
validate-instance:
	@test -n "$(SCHEMA)" || (echo "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@test -n "$(INSTANCE)" || (echo "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make validate-instance  SCHEMA=$(SCHEMA)  INSTANCE=$(INSTANCE)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_RUN) linkml validate --schema "$(SCHEMA)" "$(INSTANCE)"

# ---------------------------------------------------------------------------
# Generator targets (genererte av make_gen_target) — gamle definisjonar fjerna
# ---------------------------------------------------------------------------

build-docker-linkml:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-linkml$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(LINKML_DOCKERFILE) -t $(LINKML_IMAGE) .

build-docker-python:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-python$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(PYTHON_DOCKERFILE) -t $(PYTHON_IMAGE)

build-docker-avrotize:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-avrotize$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(AVROTIZE_DOCKERFILE) -t $(AVROTIZE_IMAGE)

build-docker-asyncapi:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-asyncapi$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(ASYNCAPI_DOCKERFILE) -t $(ASYNCAPI_IMAGE)

build-docker-plantuml:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-plantuml$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f src/assets/containers/Dockerfile.plantuml -t localhost/plantuml:latest .

# Convert example YAML to RDF/Turtle for all domains.
# AP-NO profiles have no tree_root and use fixture schemas; others use the schema directly.
convert-rdf:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make convert-rdf$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@for example in $$(find $(SCHEMA_DIR) -path '*/examples/*-eksempel.yaml' | sort); do \
		[ -f "$$example" ] || continue; \
		name=$$(basename "$$example" .yaml); \
		profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
		domain=$$(echo "$$example" | awk -F/ '{print $$3}'); \
		manifest=$(SCHEMA_DIR)/$$domain/$$profil/build.yaml; \
		if [ -f "$$manifest" ] && grep -q "^  example_rdf: false" "$$manifest"; then \
			echo "Hoppar over linkml-convert for $$example (example_rdf: false)"; \
			continue; \
		fi; \
		mkdir -p $(GEN_DIR)/$$domain/$$profil; \
		if [ -f tests/fixtures/$$profil-fixture.yaml ]; then \
			schema=tests/fixtures/$$profil-fixture.yaml; \
		else \
			schema=$(SCHEMA_DIR)/$$domain/$$profil/$$profil-schema.yaml; \
		fi; \
		echo "$(CLR_STEP)→ linkml-convert  $$example$(CLR_RST)"; \
		echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate --output $(GEN_DIR)/$$domain/$$profil/$$name.ttl $$example"; \
		$(LINKML_RUN) linkml-convert \
			--schema $$schema \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/$$domain/$$profil/$$name.ttl \
			$$example; \
	done

# Convert data YAML files to RDF/Turtle for all domains.
# Naming convention: src/linkml/<domain>/<model>/data/<catalog>/<catalog>.yaml → generated/<domain>/<catalog>/<catalog>.ttl
# Schema resolved as: src/linkml/<domain>/<model>/<model>-schema.yaml
convert-data:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make convert-data$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
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

clean:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make clean$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	rm -rf $(GEN_DIR)

# Oppdater Informasjonsmodell-innslag i modellkatalogen frå schema.annotations.*.
# Les annotations frå alle skjema med annotations.utgiver og skriv til katalogdatafila.
update-modellkatalog:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make update-modellkatalog$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/update-modellkatalog.py

# Reknar ut DQV-kvalitetsmålingar (fullstendighet/aktualitet) for datafiler med
# data_policy felles-begrepskatalog/felles-datakatalog og skriv dem attende.
gen-dqv-measurements:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-dqv-measurements$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-dqv-measurements.py

# Genererer ModelDCAT-AP-NO-modellelement (Objekttype/Attributt/Assosiasjon/
# Kodeliste/Kodeelement) frå LinkML-skjemastruktur og skriv dem inn i riktig
# org sin modellkatalog-datafil. Krev SchemaView, derfor $(LINKML_RUN) (ikkje
# $(PYTHON_RUN)). Bruk: make gen-modelldcat-elements [ORG=alias] [DRYRUN=1]
gen-modelldcat-elements:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-modelldcat-elements$(if $(ORG),  ORG=$(ORG))$(if $(DRYRUN),  DRYRUN=$(DRYRUN))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_RUN) python3 src/assets/scripts/makefile/gen-modelldcat-elements.py $(if $(ORG),--org $(ORG)) $(if $(DRYRUN),--dry-run)

# Kopier genererte artefakter til mkdocs/docs/ og oppdater mkdocs.yml.
# Føresetnad: relevante make domain-<domain>-targets er køyrde fyrst.
docs-publish:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-publish$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_INFO)Oppdaterer README.md-tabellar...$(CLR_RST)"
	bash src/assets/scripts/makefile/generate-readme-tables.sh README.md
	@echo "$(CLR_INFO)Publiserer mkdocs-portal...$(CLR_RST)"
	bash mkdocs/publish.sh

# ---------------------------------------------------------------------------
# Per-model generator configuration — regenerated when any build.yaml changes.
# ---------------------------------------------------------------------------
config.mk: $(shell find src/linkml -name 'build.yaml')
	bash src/assets/scripts/makefile/gen-config.sh > config.mk

gen-config: config.mk

# ---------------------------------------------------------------------------
# Per-domain targets – generated automatically for every domain in DOMAINS.
# `make <domain>` (e.g. make oreg) generates all artefacts for that domain.
# New domains appear automatically when schemas are added under src/linkml/.
#
# Escaping guide for the define block used with $(eval $(call ...)):
#   $(1)          – expanded at call time (parameter substitution)
#   $$(VAR)       – becomes $(VAR) after call; expanded at build time
#   $$$$shell_var – becomes $$shell_var after call; shell receives $shell_var
# ---------------------------------------------------------------------------

define domain_target
_schemas_$(1) := $(filter $(SCHEMA_DIR)/$(1)/%,$(SCHEMAS))

.PHONY: domain-$(1)
domain-$(1):
	@echo "$(CLR_SEP)$$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make domain-$(1)$(if $(filter-out 1,$(PARALLEL)), (PARALLEL=$(PARALLEL)),)$(CLR_RST)"
	@echo "$(CLR_SEP)$$(SEP)$(CLR_RST)"
	$$(call run_gen_linkml_parallel,$$(_schemas_$(1)))
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-jsonld-context,context.jsonld)
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-shacl,shapes.ttl)
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-python,model.py)
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-json-schema,schema.json)
	$$(call run_gen_owl_parallel,$$(_schemas_$(1)))
	$$(call run_gen_rdf_parallel,$$(_schemas_$(1)))
	@for example in $$(find $(SCHEMA_DIR)/$(1) -path '*/examples/*-eksempel.yaml' 2>/dev/null | sort); do \
		[ -f "$$$$example" ] || continue; \
		name=$$$$(basename "$$$$example" .yaml); \
		profil=$$$$(echo "$$$$name" | sed 's/-eksempel$$$$//'); \
		if [ -f $(SCHEMA_DIR)/$(1)/$$$$profil/build.yaml ] && grep -q "^  example_rdf: false" $(SCHEMA_DIR)/$(1)/$$$$profil/build.yaml; then \
			echo "Hoppar over linkml-convert for $$$$example (example_rdf: false)"; \
			continue; \
		fi; \
		mkdir -p $(GEN_DIR)/$(1)/$$$$profil; \
		if [ -f tests/fixtures/$$$$profil-fixture.yaml ]; then \
			schema=tests/fixtures/$$$$profil-fixture.yaml; \
		else \
			schema=$(SCHEMA_DIR)/$(1)/$$$$profil/$$$$profil-schema.yaml; \
		fi; \
		echo "$(CLR_STEP)→ linkml-convert  $$$$example$(CLR_RST)"; \
		echo "$$(LINKML_RUN) linkml-convert --schema $$$$schema --output-format ttl --no-validate $$$$example > $(GEN_DIR)/$(1)/$$$$profil/$$$$name.ttl"; \
		$$(LINKML_RUN) linkml-convert \
			--schema $$$$schema \
			--output-format ttl \
			--no-validate \
			$$$$example > $(GEN_DIR)/$(1)/$$$$profil/$$$$name.ttl; \
	done
	$$(call run_gen_doc_parallel,$$(_schemas_$(1)))
	$$(call run_gen_erdiagram_parallel,$$(_schemas_$(1)))
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-proto,schema.proto)
	$$(call run_gen_plantuml_parallel,$$(_schemas_$(1)))
	$$(call run_gen_xsd,$$(_schemas_$(1)))
	@if [ "$$(PARALLEL)" = "1" ]; then \
		for schema in $$(_schemas_$(1)); do \
			domain=$$$$(echo "$$$$schema" | awk -F/ '{print $$$$3}'); \
			name=$$$$(echo "$$$$schema" | awk -F/ '{print $$$$4}'); \
			manifest=$$$$(dirname "$$$$schema")/build.yaml; \
			if [ ! -f "$$$$manifest" ] || ! grep -q "^  openapi: true" "$$$$manifest"; then \
				continue; \
			fi; \
			jsonschema=$(GEN_DIR)/$$$$domain/$$$$name/$$$$name-schema.json; \
			if [ ! -f "$$$$jsonschema" ]; then \
				echo "ÅTVARING: $$$$jsonschema finst ikkje — hoppar over gen-openapi for $$$$name" >&2; \
				continue; \
			fi; \
			out=$(GEN_DIR)/$$$$domain/$$$$name/$$$$name-openapi.yaml; \
			mkdir -p $(GEN_DIR)/$$$$domain/$$$$name; \
			echo "$(CLR_STEP)→ gen-openapi  $$$$schema$(CLR_RST)"; \
			$$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py \
				/work/$$$$jsonschema /work/$$$$schema --out /work/$$$$out; \
			$$(PYTHON_RUN) openapi-spec-validator /work/$$$$out; \
		done; \
	else \
		$$(call run_gen_openapi_parallel,$$(_schemas_$(1))); \
	fi
	@if [ "$$(PARALLEL)" = "1" ]; then \
		for schema in $$(_schemas_$(1)); do \
			domain=$$$$(echo "$$$$schema" | awk -F/ '{print $$$$3}'); \
			name=$$$$(echo "$$$$schema" | awk -F/ '{print $$$$4}'); \
			manifest=$$$$(dirname "$$$$schema")/build.yaml; \
			if [ ! -f "$$$$manifest" ] || ! grep -q "^  asyncapi: true" "$$$$manifest"; then \
				continue; \
			fi; \
			jsonschema=$(GEN_DIR)/$$$$domain/$$$$name/$$$$name-schema.json; \
			if [ ! -f "$$$$jsonschema" ]; then \
				echo "ÅTVARING: $$$$jsonschema finst ikkje — hoppar over gen-asyncapi for $$$$name" >&2; \
				continue; \
			fi; \
			out=$(GEN_DIR)/$$$$domain/$$$$name/$$$$name-asyncapi.yaml; \
			mkdir -p $(GEN_DIR)/$$$$domain/$$$$name; \
			echo "$(CLR_STEP)→ gen-asyncapi  $$$$schema$(CLR_RST)"; \
			$$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py \
				/work/$$$$jsonschema /work/$$$$schema --out /work/$$$$out; \
			$$(ASYNCAPI_RUN) validate /work/$$$$out; \
		done; \
	else \
		$$(call run_gen_asyncapi_parallel,$$(_schemas_$(1))); \
	fi
	$$(call run_gen_informasjonsmodell_instance,$$(_schemas_$(1)))
endef

# Generer domain-targets for alle domene unntatt begrepskatalog (har eksplisitt override nedanfor)
$(foreach d,$(filter-out begrepskatalog,$(DOMAINS)),$(eval $(call domain_target,$(d))))

# Override domain-begrepskatalog to run gen-begrepskatalog-instance first
.PHONY: domain-begrepskatalog
domain-begrepskatalog: gen-begrepskatalog-instance
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make domain-begrepskatalog$(if $(filter-out 1,$(PARALLEL)), (PARALLEL=$(PARALLEL)),)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_linkml_parallel,$(_schemas_begrepskatalog))
	$(call run_gen_parallel,$(_schemas_begrepskatalog),gen-jsonld-context,context.jsonld)
	$(call run_gen_parallel,$(_schemas_begrepskatalog),gen-shacl,shapes.ttl)
	$(call run_gen_parallel,$(_schemas_begrepskatalog),gen-python,model.py)
	$(call run_gen_parallel,$(_schemas_begrepskatalog),gen-json-schema,schema.json)
	$(call run_gen_owl_parallel,$(_schemas_begrepskatalog))
	$(call run_gen_rdf_parallel,$(_schemas_begrepskatalog))
	@for example in $(shell find $(SCHEMA_DIR)/begrepskatalog -path '*/examples/*-eksempel.yaml' 2>/dev/null | sort); do \
		[ -f "$$example" ] || continue; \
		name=$$(basename "$$example" .yaml); \
		profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
		if [ -f $(SCHEMA_DIR)/begrepskatalog/$$profil/build.yaml ] && grep -q "^  example_rdf: false" $(SCHEMA_DIR)/begrepskatalog/$$profil/build.yaml; then \
			echo "Hoppar over linkml-convert for $$example (example_rdf: false)"; \
			continue; \
		fi; \
		mkdir -p $(GEN_DIR)/begrepskatalog/$$profil; \
		if [ -f tests/fixtures/$$profil-fixture.yaml ]; then \
			schema=tests/fixtures/$$profil-fixture.yaml; \
		else \
			schema=$(SCHEMA_DIR)/begrepskatalog/$$profil/$$profil-schema.yaml; \
		fi; \
		echo "$(CLR_STEP)→ linkml-convert  $$example$(CLR_RST)"; \
		echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate $$example > $(GEN_DIR)/begrepskatalog/$$profil/$$name.ttl"; \
		$(LINKML_RUN) linkml-convert \
			--schema $$schema \
			--output-format ttl \
			--no-validate \
			$$example > $(GEN_DIR)/begrepskatalog/$$profil/$$name.ttl; \
	done
	$(call run_gen_doc_parallel,$(_schemas_begrepskatalog))
	$(call run_gen_erdiagram_parallel,$(_schemas_begrepskatalog))
	$(call run_gen_parallel,$(_schemas_begrepskatalog),gen-proto,schema.proto)
	$(call run_gen_plantuml_parallel,$(_schemas_begrepskatalog))
	$(call run_gen_xsd,$(_schemas_begrepskatalog))
	@if [ "$(PARALLEL)" = "1" ]; then \
		for schema in $(_schemas_begrepskatalog); do \
			domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
			name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
			manifest=$$(dirname "$$schema")/build.yaml; \
			if [ ! -f "$$manifest" ] || ! grep -q "^  openapi: true" "$$manifest"; then \
				continue; \
			fi; \
			jsonschema=$(GEN_DIR)/$$domain/$$name/$$name-schema.json; \
			if [ ! -f "$$jsonschema" ]; then \
				echo "ÅTVARING: $$jsonschema finst ikkje — hoppar over gen-openapi for $$name" >&2; \
				continue; \
			fi; \
			out=$(GEN_DIR)/$$domain/$$name/$$name-openapi.yaml; \
			mkdir -p $(GEN_DIR)/$$domain/$$name; \
			echo "$(CLR_STEP)→ gen-openapi  $$schema$(CLR_RST)"; \
			$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py \
				/work/$$jsonschema /work/$$schema --out /work/$$out; \
			$(PYTHON_RUN) openapi-spec-validator /work/$$out; \
		done; \
	else \
		$(call run_gen_openapi_parallel,$(_schemas_begrepskatalog)); \
	fi
	@if [ "$(PARALLEL)" = "1" ]; then \
		for schema in $(_schemas_begrepskatalog); do \
			domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
			name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
			manifest=$$(dirname "$$schema")/build.yaml; \
			if [ ! -f "$$manifest" ] || ! grep -q "^  asyncapi: true" "$$manifest"; then \
				continue; \
			fi; \
			jsonschema=$(GEN_DIR)/$$domain/$$name/$$name-schema.json; \
			if [ ! -f "$$jsonschema" ]; then \
				echo "ÅTVARING: $$jsonschema finst ikkje — hoppar over gen-asyncapi for $$name" >&2; \
				continue; \
			fi; \
			out=$(GEN_DIR)/$$domain/$$name/$$name-asyncapi.yaml; \
			mkdir -p $(GEN_DIR)/$$domain/$$name; \
			echo "$(CLR_STEP)→ gen-asyncapi  $$schema$(CLR_RST)"; \
			$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py \
				/work/$$jsonschema /work/$$schema --out /work/$$out; \
			$(ASYNCAPI_RUN) validate /work/$$out; \
		done; \
	else \
		$(call run_gen_asyncapi_parallel,$(_schemas_begrepskatalog)); \
	fi
	$(call run_gen_informasjonsmodell_instance,$(_schemas_begrepskatalog))

# ---------------------------------------------------------------------------
# Per-artifakt-mål for CI – krev DOMAIN=<domenenamn>
# Eksempel: make domain-gen-shapes DOMAIN=oreg
# ---------------------------------------------------------------------------


validate-bronze:
ifdef DOMAIN
	@set +e; \
	FAILED=0; \
	while IFS= read -r schema; do \
		echo "--- $$schema ---"; \
		result=$$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$$schema" bronze 2>/dev/null); \
		echo "$$result"; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type bronze --result "$$result" 2>/dev/null || true; \
		if ! SCHEMA="$$schema" $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/emit-github-validation-annotations.py <<< "$$result"; then \
			FAILED=$$((FAILED + 1)); \
		fi; \
	done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort); \
	exit $$FAILED
else
	@echo "FEIL: DOMAIN er påkravd. Bruk: make validate-bronze DOMAIN=<domain>" >&2
	@exit 1
endif

validate-data:
ifdef DOMAIN
	@for datadir in $$(find $(SCHEMA_DIR)/$(DOMAIN) -mindepth 3 -maxdepth 3 -type d -path '*/data/*' 2>/dev/null | sort); do \
		model=$$(echo "$$datadir" | awk -F/ '{print $$4}'); \
		catalog=$$(basename "$$datadir"); \
		datafile="$$datadir/$$catalog.yaml"; \
		[ -f "$$datafile" ] || continue; \
		schema=$(SCHEMA_DIR)/$(DOMAIN)/$$model/$$model-schema.yaml; \
		manifest="$$datadir/build.yaml"; \
		if [ -f "$$manifest" ]; then \
			policy=$$(grep '^validation_policy:' "$$manifest" | awk '{print $$2}'); \
		else \
			policy=bronze; \
		fi; \
		[ -n "$$policy" ] || policy=bronze; \
		echo "$(CLR_STEP)→ mcp-validate  $$datafile  (policy: $$policy)$(CLR_RST)"; \
		result=$$(bash $(MCP_DIR)/flatten-and-validate.bash "$$schema" "$$policy" "$$datafile" 2>/dev/null); \
		echo "$$result"; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type "data-$$catalog" --result "$$result" 2>/dev/null || true; \
	done
else
	@echo "FEIL: DOMAIN er påkravd. Bruk: make validate-data DOMAIN=<domain>" >&2
	@exit 1
endif

validate-examples:
ifdef DOMAIN
	@set +e; \
	FAILED=0; \
	while IFS= read -r schema; do \
		name=$$(basename "$$schema" -schema.yaml); \
		example="$(SCHEMA_DIR)/$(DOMAIN)/$$name/examples/$$name-eksempel.yaml"; \
		if [ ! -f "$$example" ]; then \
			echo "::warning file=$$schema::Ingen eksempelfil funne: $$example"; \
			continue; \
		fi; \
		echo "--- $$schema ---"; \
		result=$$(podman run --rm -v "$$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
			$(LINKML_IMAGE) linkml validate --schema "$$schema" "$$example" 2>&1); \
		echo "$$result"; \
		has_error=false; \
		if echo "$$result" | grep -q "\[ERROR\]"; then \
			has_error=true; \
			echo "$$result" | grep "\[ERROR\]" | while IFS= read -r line; do \
				echo "::error file=$$example::$$(echo "$$line" | sed 's/\[ERROR\] //')"; \
			done; \
			FAILED=$$((FAILED + 1)); \
		fi; \
		if [ "$$has_error" = "true" ]; then \
			result_json='{"valid":false,"error_count":1,"warning_count":0,"issues":[{"severity":"error","target":"examples","message":"Validation failed"}]}'; \
		else \
			result_json='{"valid":true,"error_count":0,"warning_count":0,"issues":[]}'; \
		fi; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type examples --result "$$result_json" 2>/dev/null || true; \
	done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
		| grep -v common | sort | xargs grep -l "tree_root: true"); \
	exit $$FAILED
else
	@echo "FEIL: DOMAIN er påkravd. Bruk: make validate-examples DOMAIN=<domain>" >&2
	@exit 1
endif

# ---------------------------------------------------------------------------
# Dokumentasjonsportal (MkDocs Material)
# ---------------------------------------------------------------------------
# Bygg lokal docs-image med mkdocs-kroki (trengst for PlantUML-rendering via Kroki.io).
# Køyr éin gong, eller etter endringar i mkdocs/Dockerfile.
build-docker-mkdocs:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mkdocs$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(DOCS_DOCKERFILE) -t $(DOCS_IMAGE)

docs-serve:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-serve$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"
	$(DOCS_RUN) -it -p 8000:8000 $(DOCS_IMAGE) serve --dev-addr=0.0.0.0:8000

docs-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"
	$(DOCS_RUN) $(DOCS_IMAGE) build

# ---------------------------------------------------------------------------
# MCP-validator
# ---------------------------------------------------------------------------
MCP_RUN := podman run -i --rm \
  -v "$(CURDIR)/$(MCP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(MCP_DIR)/policies:/app/policies:ro"

build-docker-mcp-validator:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-validator$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -t $(MCP_IMAGE) $(MCP_DIR)

mcp-linkml-validate-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-validate-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(MCP_RUN) $(MCP_IMAGE)

mcp-linkml-validate-smoke: build-docker-mcp-validator
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-validate-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-validator.json | $(MCP_RUN) $(MCP_IMAGE)

mcp-linkml-validate-test: build-docker-mcp-validator
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-validate-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR):/work:ro" \
		-e PYTHONWARNINGS=ignore \
		$(MCP_IMAGE) \
		python3 /work/tests/test_mcp_policies.py -v

# ---------------------------------------------------------------------------
# mcp-linkml-modell-utkast
# ---------------------------------------------------------------------------
build-docker-mcp-modell-utkast:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-modell-utkast$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -t $(LINKML_MOD_IMAGE) $(LINKML_MOD_DIR)

mcp-linkml-modell-utkast-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-modell-utkast-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-linkml-modell-utkast-smoke: build-docker-mcp-modell-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-modell-utkast-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-generator.json | $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-linkml-modell-utkast-test: build-docker-mcp-modell-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-modell-utkast-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR)/$(LINKML_MOD_DIR):/app/mcp-linkml-modell-utkast:ro" \
		-v "$(CURDIR)/tests:/app/tests:ro" \
		-w /app/tests \
		-e PYTHONPATH=/app/mcp-linkml-modell-utkast \
		$(LINKML_MOD_IMAGE) \
		python -m pytest test_mcp_linkml_generator.py -v

# Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=bronze]
mcp-linkml-modell-utkast:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=bronze]"; exit 1)
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-modell-utkast-request.py \
		"$(SCHEMA)" "$(or $(FORMAT),json-schema)" "$(or $(PROFILE),bronze)" \
		| $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE) \
		| $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-write-modell-utkast-response.py "$(SCHEMA)"
	@# Automatisk roundtrip-test for JSON Schema
	@if echo "$(SCHEMA)" | grep -qE '\.(json|schema\.json)$$'; then \
		echo "$(CLR_STEP)→ Køyrer roundtrip-test for $(SCHEMA)$(CLR_RST)"; \
		$(MAKE) roundtrip-json-schema JSONSCHEMA="$(SCHEMA)" || \
		(echo "$(CLR_ERR)Roundtrip-test feila — sjå logg for detaljar$(CLR_RST)" && exit 1); \
	fi

# ---------------------------------------------------------------------------
# mcp-linkml-begrep-utkast
# ---------------------------------------------------------------------------
build-docker-mcp-begrep-utkast:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-begrep-utkast$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -t $(LINKML_BEGREP_IMAGE) $(LINKML_BEGREP_DIR)

mcp-linkml-begrep-utkast-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-begrep-utkast-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

mcp-linkml-begrep-utkast-smoke: build-docker-mcp-begrep-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-begrep-utkast-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# Bruk: make mcp-linkml-begrep-utkast INPUT=tmp/mitt-begrep.json
mcp-linkml-begrep-utkast:
	@test -n "$(INPUT)" || \
	  (echo "Bruk: make mcp-linkml-begrep-utkast INPUT=<sti-til-json>"; exit 1)
	@test -f "$(INPUT)" || \
	  (echo "Feil: $(INPUT) finst ikkje"; exit 1)
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-begrep-utkast-request.py "$(INPUT)" \
	  | $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# List profiler:
#   make mcp-linkml-begrep-utkast-list-profiles
mcp-linkml-begrep-utkast-list-profiles:
	@podman image exists $(LINKML_BEGREP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-begrep-utkast
	@echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_profiles","arguments":{}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# Bruk: make new-model NAME=<namn> DOMAIN=<domene>
new-model:
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-model NAME=<namn> DOMAIN=<domene>"; exit 1)
	@podman image exists $(LINKML_MOD_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-modell-utkast
	bash src/assets/scripts/new-model.sh "$(NAME)" "$(DOMAIN)"

# Bruk: make new-modellkatalog NAME=<alias>
new-modellkatalog:
	@test -n "$(NAME)" || (echo "Bruk: make new-modellkatalog NAME=<alias>"; exit 1)
	bash src/assets/scripts/new-modellkatalog.sh "$(NAME)"

# Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>
new-begrepssamling:
	@test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>"; exit 1)
	@test -n "$(NAME)" || \
	  (echo "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>"; exit 1)
	bash src/assets/scripts/new-begrepssamling.sh "$(DOMAIN)" "$(NAME)"

# Deprecated: bruk new-begrepssamling i staden
new-begrepskatalog:
	@echo "Åtvaring: 'make new-begrepskatalog' er deprecated. Bruk 'make new-begrepssamling' i staden." >&2
	@test -n "$(NAME)" || \
	  (echo "Bruk: make new-begrepskatalog NAME=<katalognavn>"; exit 1)
	bash src/assets/scripts/new-begrepskatalog.sh "$(NAME)"

# Generer .github/valid-scopes.txt frå alle *-schema.yaml-filer
# Køyrer automatisk ved `make new-model`, `make new-modellkatalog`, `make new-begrepssamling`
update-valid-scopes:
	@echo "Genererer .github/valid-scopes.txt..."
	@find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
	  | sed 's|.*/||; s|-schema\.yaml$$||' \
	  | sort \
	  > .github/valid-scopes.txt
	@echo "Generert $$(wc -l < .github/valid-scopes.txt) scopes"

check-prereqs:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make check-prereqs$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@bash src/assets/scripts/makefile/check-prereqs.bash

# Bruk: make mcp-linkml-validate SCHEMA=<sti-til-skjema> [POLICY=gold]
# POLICY vert auto-detektert frå build.yaml dersom ikkje oppgjeven
mcp-linkml-validate:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-linkml-validate SCHEMA=<sti-til-skjema> [POLICY=gold]"; exit 1)
	@DETECTED_POLICY=$$($(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/detect-validation-policy.py "$(SCHEMA)" 2>/dev/null || echo "bronze"); \
	POLICY_TO_USE="$${POLICY:-$$DETECTED_POLICY}"; \
	echo "$(CLR_SEP)$(SEP)$(CLR_RST)"; \
	echo "$(CLR_HDR)*** make mcp-linkml-validate  SCHEMA=$(SCHEMA)  POLICY=$$POLICY_TO_USE$(CLR_RST)"; \
	echo "$(CLR_SEP)$(SEP)$(CLR_RST)"; \
	podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator; \
	bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $$POLICY_TO_USE $(INSTANCE)

# Bruk: make validate-capture [SCHEMA=<sti>] [PARALLEL=8]
# Utan SCHEMA: køyr for alle skjema med parallellisering.
validate-capture:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make validate-capture$(if $(SCHEMA),  SCHEMA=$(SCHEMA),  (alle skjema, $(PARALLEL) workers))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@if [ -n "$(SCHEMA)" ]; then \
	    $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/run-schema-validation.py --schema $(SCHEMA); \
	else \
	    $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/run-schema-validation.py --parallel $(PARALLEL); \
	fi

# Bruk: make log-mcp-validate MANIFEST=<sti> eller SCHEMA=<sti> POLICY=<policy>
# Validerer og skriv logg til src/linkml/<domain>/<modell>/validation/<version>/<policy>.json
log-mcp-validate:
	@if [ -n "$(MANIFEST)" ]; then \
		bash src/assets/scripts/run-validation.sh --manifest $(MANIFEST); \
	elif [ -n "$(SCHEMA)" ] && [ -n "$(POLICY)" ]; then \
		bash src/assets/scripts/run-validation.sh --schema $(SCHEMA) --policy $(POLICY); \
	else \
		echo "Feil: Oppgi anten MANIFEST=<sti> eller både SCHEMA=<sti> og POLICY=<policy>"; \
		exit 1; \
	fi

# Bruk: make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>
# Validerer instans og skriv logg til src/linkml/<domain>/<modell>/validation/<version>/instance-<namn>.json
log-validate-instance:
	@test -n "$(SCHEMA)" || (echo "Bruk: make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@test -n "$(INSTANCE)" || (echo "Bruk: make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@bash src/assets/scripts/run-validation.sh --schema $(SCHEMA) --instance $(INSTANCE)

# ---------------------------------------------------------------------------
# Gource – visualisering av git-historikk
# ---------------------------------------------------------------------------
GOURCE_IMAGE      := localhost/gource-local:latest
GOURCE_DOCKERFILE := src/assets/containers/Dockerfile.gource

define GOURCE_RUN
podman run --rm \
  -v "$(CURDIR):/repo:ro" \
  -v "$(CURDIR)/tmp:/out" \
  $(GOURCE_IMAGE) \
  bash -c " \
    git config --global --add safe.directory /repo && \
    xvfb-run -a -s '-screen 0 1920x1080x24' \
      gource /repo \
        --seconds-per-day 1 \
        --auto-skip-seconds 1 \
        --title 'linkml-datamodellering-no' \
        --hide mouse,progress \
        --background-colour 111111 \
        --font-size 18 \
        --output-ppm-stream /out/gource.ppm \
        $(GOURCE_EXTRA_FLAGS) && \
    ffmpeg -y -r $(GOURCE_FPS) \
        -f image2pipe -vcodec ppm \
        -i /out/gource.ppm \
        -an -vcodec libx264 $(GOURCE_FFMPEG_PRESET) \
        -pix_fmt yuv420p -movflags +faststart \
        /out/$(GOURCE_OUTFILE) && \
    rm /out/gource.ppm"
endef

build-docker-gource:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-gource$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(GOURCE_DOCKERFILE) -t $(GOURCE_IMAGE)

gource-preview: build-docker-gource
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gource-preview$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p tmp
	$(MAKE) --no-print-directory _gource-render \
	  GOURCE_OUTFILE=gource-preview.mp4 \
	  GOURCE_EXTRA_FLAGS="--viewport 1280x720" \
	  GOURCE_FPS=30 \
	  GOURCE_FFMPEG_PRESET="-preset ultrafast -crf 28"
	@echo "Preview: tmp/gource-preview.mp4"

gource-video: build-docker-gource
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gource-video$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p tmp
	$(MAKE) --no-print-directory _gource-render \
	  GOURCE_OUTFILE=gource.mp4 \
	  GOURCE_EXTRA_FLAGS="--viewport 1920x1080 --bloom-multiplier 0.5" \
	  GOURCE_FPS=60 \
	  GOURCE_FFMPEG_PRESET="-preset fast -crf 22"
	@echo "Video: tmp/gource.mp4"

_gource-render:
	$(GOURCE_RUN)

# ===========================================================================
# ModelDCAT-AP-NO Informasjonsmodell-generering (MVP)
# ===========================================================================

# Per-schema Informasjonsmodell-instans generator.
# $1=schemas
define run_gen_informasjonsmodell_instance
@for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	t0=$$(date +%s%3N); \
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-informasjonsmodell.py "$$schema" >/dev/null 2>&1; \
	rc=$$?; \
	elapsed_ms=$$(($$(date +%s%3N) - t0)); \
	printf "$(CLR_STEP)→ gen-informasjonsmodell-instance  %s/%s$(CLR_RST) (%d.%ds)\n" \
		"$$domain" "$$name" \
		$$((elapsed_ms / 1000)) \
		$$((elapsed_ms % 1000 / 100)); \
	if [ $$rc -ne 0 ]; then \
		echo "Warning: Failed to generate Informasjonsmodell for $$schema"; \
	fi; \
done
endef

.PHONY: gen-informasjonsmodell-instance

gen-informasjonsmodell-instance:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-informasjonsmodell-instance SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-informasjonsmodell-instance DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-informasjonsmodell-instance$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_informasjonsmodell_instance,$(call get_target_schemas))

.PHONY: gen-modellkatalog-instance

gen-modellkatalog-instance:
	@echo "$(CLR_HDR)Genererer Modellkatalog-instans$(CLR_RST)"
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-modellkatalog.py

.PHONY: gen-begrepskatalog-instance

gen-begrepskatalog-instance:
	@echo "$(CLR_HDR)Samlar begrep frå begrepssamlingar til begrepskatalogar$(CLR_RST)"
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/collect-concepts.py

.PHONY: validate-informasjonsmodell-instance

validate-informasjonsmodell-instance:
	@if [ -z "$(SCHEMA)" ]; then \
		echo "Error: SCHEMA parameter required"; \
		echo "Usage: make validate-informasjonsmodell-instance SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml"; \
		exit 1; \
	fi
	@echo "$(CLR_HDR)Validerer Informasjonsmodell-instans for $(SCHEMA)$(CLR_RST)"
	@SCHEMA_DIR=$$(dirname "$(SCHEMA)"); \
	MODELLDCAT_YAML="$$SCHEMA_DIR/metadata/modelldcat.yaml"; \
	if [ ! -f "$$MODELLDCAT_YAML" ]; then \
		echo "Error: $$MODELLDCAT_YAML eksisterer ikkje"; \
		echo "Køyr først: make gen-informasjonsmodell-instance SCHEMA=$(SCHEMA)"; \
		exit 1; \
	fi; \
	echo "$(CLR_STEP)Køyrer full LinkML-validering$(CLR_RST)"; \
	$(LINKML_RUN) python3 /work/src/assets/scripts/validate-modelldcat.py \
		"$$MODELLDCAT_YAML" \
		/work/src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml

.PHONY: validate-modellkatalog-instance

validate-modellkatalog-instance:
	@if [ -z "$(ORG)" ]; then \
		echo "Error: ORG parameter required"; \
		echo "Usage: make validate-modellkatalog-instance ORG=<org-slug>"; \
		echo "Eksempel: make validate-modellkatalog-instance ORG=digdir-modellkatalog"; \
		exit 1; \
	fi
	@echo "$(CLR_HDR)Validerer Modellkatalog-instans for $(ORG)$(CLR_RST)"
	@ORG_SCHEMA="src/linkml/modellkatalog/$(ORG)/$(ORG)-schema.yaml"; \
	ORG_DATA="src/linkml/modellkatalog/$(ORG)/data/$(ORG)/$(ORG).yaml"; \
	if [ ! -f "$$ORG_SCHEMA" ]; then \
		echo "Error: $$ORG_SCHEMA eksisterer ikkje"; \
		exit 1; \
	fi; \
	if [ ! -f "$$ORG_DATA" ]; then \
		echo "Error: $$ORG_DATA eksisterer ikkje"; \
		echo "Køyr først: make gen-modellkatalog-instance"; \
		exit 1; \
	fi; \
	echo "$(CLR_STEP)Validerer $$ORG_DATA mot $$ORG_SCHEMA$(CLR_RST)"; \
	$(LINKML_RUN) linkml validate --schema "$$ORG_SCHEMA" "$$ORG_DATA"

