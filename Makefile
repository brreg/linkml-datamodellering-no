SHELL           	:= /bin/bash
.SHELLFLAGS     	:= -o pipefail -c
LINKML_IMAGE    	:= localhost/linkml-local:latest
LINKML_DOCKERFILE 	:= src/assets/containers/Dockerfile.linkml
LINKML_RUN     		:= podman run --rm -v "$(CURDIR):/work" -w /work -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root $(LINKML_IMAGE)
GEN_DIR    			:= generated
SCHEMA_DIR 			:= src/linkml
MCP_DIR    			:= src/mcp-linkml-validator
MCP_IMAGE  			:= mcp-linkml-validator
INSTANCE   			?=
DOCS_IMAGE 			:= localhost/mkdocs-local:latest
PLANTUML_IMAGE		:= docker.io/plantuml/plantuml:latest
DOCS_DOCKERFILE 	:= mkdocs/Dockerfile.mkdocs
DOCS_RUN   			:= podman run --rm \
	-v "$(CURDIR)/mkdocs/docs:/docs/docs" \
  	-v "$(CURDIR)/mkdocs/mkdocs.yml:/docs/mkdocs.yml" \
  	-v "$(CURDIR)/mkdocs/overrides:/docs/overrides" \
  	-v "$(CURDIR)/mkdocs/.cache:/docs/.cache" \
  	-v "$(CURDIR)/mkdocs/site:/docs/site"
PYTHON_IMAGE		:= localhost/python-pytest:latest
PYTHON_DOCKERFILE 	:= src/assets/containers/Dockerfile.python
PYTHON_RUN			:= podman run --rm -v "$(CURDIR):/work" -w /work -e PYTHONWARNINGS=ignore $(PYTHON_IMAGE)
SEP        			:= ************************************************************
CLR_SEP    			:= $(shell printf '\033[1;33m')
CLR_HDR    			:= $(shell printf '\033[1;37m')
CLR_STEP   			:= $(shell printf '\033[0;36m')
CLR_RST    			:= $(shell printf '\033[0m')

# ---------------------------------------------------------------------------
# Schema discovery – no manual lists needed.
# Leaf schemas follow the pattern: src/linkml/<domain>/<name>/<name>-schema.yaml
# Schemas with 'common' in the path are shared dependencies, not standalone.
# ---------------------------------------------------------------------------
SCHEMAS := $(shell find $(SCHEMA_DIR) -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
    | grep -v common | sort)

schema_domain = $(word 3,$(subst /, ,$(1)))
schema_name   = $(word 4,$(subst /, ,$(1)))
schema_outdir = $(GEN_DIR)/$(call schema_domain,$(1))/$(call schema_name,$(1))
schema_key    = $(subst -,_,$(call schema_domain,$(1)))_$(subst -,_,$(call schema_name,$(1)))

# Domains are derived automatically from the discovered schemas
DOMAINS := $(sort $(foreach s,$(SCHEMAS),$(call schema_domain,$(s))))

-include config.mk

# ---------------------------------------------------------------------------
# Generator macros
# ---------------------------------------------------------------------------
# $1=schemas  $2=generator  $3=output-file suffix (stdout is redirected)
# @ suppresses make's own echo of the foreach line; each iteration instead
# prints the coloured summary line, then the full podman command, then runs it.
define run_gen
@$(foreach s,$(1),echo "$(CLR_STEP)→ $(2)  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) $(2) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-$(3)" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) $(2) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-$(3);)
endef

# gen-erdiagram: pipe through awk to strip Container classes (entity block + relationships)
# $$  →  $  after make expansion, so shell sees  /^}$/  etc.
define run_gen_erdiagram
@$(foreach s,$(1),echo "$(CLR_STEP)→ gen-erdiagram  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-erdiagram --no-mergeimports $(s) | awk -f src/assets/scripts/filter_container.awk > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-erdiagram --no-mergeimports $(s) \
  | awk -f src/assets/scripts/filter_container.awk \
  > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md && \
  echo "$(PYTHON_RUN) python -u src/assets/scripts/filter_erdiagram.py $(s) $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram.md" && \
  $(PYTHON_RUN) python -u src/assets/scripts/filter_erdiagram.py $(s) $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram.md; \
  )
endef

# gen-doc writes to a directory instead of stdout
define run_gen_doc
@$(foreach s,$(1), \
  echo "$(CLR_STEP)→ gen-docgen-examples  $(s)$(CLR_RST)" && \
  mkdir -p $(call schema_outdir,$(s))/docgen-examples && \
  $(PYTHON_RUN) python3 src/assets/scripts/gen-docgen-examples.py \
    $(s) \
    src/linkml/$(call schema_domain,$(s))/$(call schema_name,$(s))/examples/$(call schema_name,$(s))-eksempel.yaml \
    $(call schema_outdir,$(s))/docgen-examples && \
  echo "$(CLR_STEP)→ gen-doc  $(s)$(CLR_RST)" && \
  echo "$(LINKML_RUN) gen-doc --template-directory src/templates/docgen --no-mergeimports --no-render-imports --no-hierarchical-class-view --diagram-type mermaid_class_diagram --example-directory $(call schema_outdir,$(s))/docgen-examples -d $(call schema_outdir,$(s))/docs $(s)" && \
  mkdir -p $(call schema_outdir,$(s))/docs && \
  $(LINKML_RUN) gen-doc \
    --template-directory src/templates/docgen \
    --no-mergeimports \
    --no-render-imports \
    --no-hierarchical-class-view \
    --diagram-type mermaid_class_diagram \
    --example-directory $(call schema_outdir,$(s))/docgen-examples \
    -d $(call schema_outdir,$(s))/docs $(s) && \
  sed -i '/Container/d' $(call schema_outdir,$(s))/docs/index.md; \
)
endef

define run_gen_plantuml
@$(foreach s,$(1), \
  echo "$(CLR_STEP)→ gen-plantuml  $(s)$(CLR_RST)" && \
  mkdir -p $(call schema_outdir,$(s))/diagrams && \
  $(LINKML_RUN) gen-plantuml $(s) \
    > $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s)).puml && \
  podman run --rm \
    -v "$(CURDIR)/$(call schema_outdir,$(s))/diagrams:/data" \
    $(PLANTUML_IMAGE) -tsvg /data/$(call schema_name,$(s)).puml; \
)
endef

# Per-schema SHACL generator: looks up SHACL_FLAGS_<schema_key> per schema.
define run_gen_shacl
@$(foreach s,$(1),echo "$(CLR_STEP)→ gen-shacl  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-shacl $(SHACL_FLAGS_$(call schema_key,$(s))) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-shapes.ttl" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-shacl $(SHACL_FLAGS_$(call schema_key,$(s))) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-shapes.ttl;)
endef

# Per-schema OWL generator: looks up OWL_FLAGS_<schema_key> per schema.
define run_gen_owl
@$(foreach s,$(1),echo "$(CLR_STEP)→ gen-owl  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-owl $(OWL_FLAGS_$(call schema_key,$(s))) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-ontology.ttl" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-owl $(OWL_FLAGS_$(call schema_key,$(s))) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-ontology.ttl;)
endef

# Per-schema RDF generator: skips schemas with GEN_RDF_SKIP_<schema_key> := true.
define run_gen_rdf
@$(foreach s,$(1),$(if $(filter true,$(GEN_RDF_SKIP_$(call schema_key,$(s)))),echo "Hoppar over gen-rdf for $(call schema_name,$(s)) (GEN_RDF_SKIP_$(call schema_key,$(s)) er sett)";,echo "$(CLR_STEP)→ gen-rdf  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-rdf $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-schema.ttl" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-rdf $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-schema.ttl;))
endef

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

.PHONY: all test validate clean domains gen-config \
		gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl gen-rdf gen-erdiagram convert-rdf convert-data gen-docs \
        linkml-build-docker python-build-docker \
        mcp-val-build mcp-val-run mcp-val-smoke mcp-val-test mcp-validate \
        mcp-mod-build mcp-mod-run mcp-mod-smoke mcp-mod-test mcp-generate new-model \
        mcp-begrep-build mcp-begrep-run mcp-begrep-smoke mcp-begrep-list-profiles \
        mcp-build mcp-run mcp-smoke mcp-test-policies \
        linkml-gen-build linkml-gen-run linkml-gen-smoke linkml-gen-generate linkml-gen-test-converter \
		docs-build-docker docs-serve docs-build docs-build-fast publish \
        $(DOMAINS) \
        domain-gen-linkml domain-gen-context domain-gen-shapes domain-gen-python \
        domain-gen-json-schema domain-gen-owl domain-gen-rdf \
        domain-gen-examples domain-gen-data domain-validate-data domain-gen-doc domain-gen-erdiagram \
        gen-proto gen-plantuml \
        domain-gen-proto domain-gen-plantuml \
        domain-validate-bronze domain-validate-examples \
        schema-gen-linkml schema-gen-context schema-gen-shapes schema-gen-python \
        schema-gen-json-schema schema-gen-owl schema-gen-rdf schema-gen-erdiagram \
        schema-gen-doc schema-gen-proto schema-gen-plantuml schema-gen-examples \
        check-published-uris check-prereqs \
        gource-build gource-preview gource-video _gource-render

all: test

domains: $(DOMAINS)

test:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	bash tests/test_make.sh "$(SCHEMA)"

validate:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make validate$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@$(foreach s,$(SCHEMAS),echo "$(CLR_STEP)→ gen-linkml  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-linkml $(s) > /dev/null" && $(LINKML_RUN) gen-linkml $(s) > /dev/null;)

gen-jsonld:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-jsonld$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMAS),gen-jsonld-context,context.jsonld)

gen-shacl:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-shacl$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_shacl,$(SCHEMAS))

gen-python:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-python$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMAS),gen-python,model.py)

gen-jsonschema:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-jsonschema$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMAS),gen-json-schema,schema.json)

gen-owl:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-owl$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_owl,$(SCHEMAS))

gen-rdf:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-rdf$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_rdf,$(SCHEMAS))


linkml-build-docker:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make linkml-build-docker$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -f $(LINKML_DOCKERFILE) -t $(LINKML_IMAGE)

python-build-docker:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make python-build-docker$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -f $(PYTHON_DOCKERFILE) -t $(PYTHON_IMAGE)



gen-erdiagram:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-erdiagram$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_erdiagram,$(SCHEMAS))

gen-docs:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-docs$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_doc,$(SCHEMAS))
	$(call run_gen_erdiagram,$(SCHEMAS))

gen-proto:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-proto$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMAS),gen-proto,schema.proto)

gen-plantuml:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-plantuml$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_plantuml,$(SCHEMAS))

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
		manifest=$(SCHEMA_DIR)/$$domain/$$profil/manifest.yaml; \
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
	@for datadir in $$(find $(SCHEMA_DIR) -mindepth 4 -maxdepth 4 -type d -path '*/data/*/*' | sort); do \
		domain=$$(echo "$$datadir" | awk -F/ '{print $$3}'); \
		model=$$(echo "$$datadir" | awk -F/ '{print $$4}'); \
		catalog=$$(basename "$$datadir"); \
		manifest="$$datadir/manifest.yaml"; \
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

# Kopier genererte artefakter til mkdocs/docs/ og oppdater mkdocs.yml.
# Føresetnad: relevante make <domain>-targets er køyrde fyrst.
publish:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make publish$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	bash mkdocs/publish.sh

# ---------------------------------------------------------------------------
# Per-model generator configuration — regenerated when any manifest.yaml changes.
# ---------------------------------------------------------------------------
config.mk: $(shell find src/linkml -name 'manifest.yaml')
	bash src/assets/scripts/gen-config.sh > config.mk

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

.PHONY: $(1)
$(1):
	@echo "$(CLR_SEP)$$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make $(1)$(CLR_RST)"
	@echo "$(CLR_SEP)$$(SEP)$(CLR_RST)"
	@$$(foreach s,$$(_schemas_$(1)),echo "$(CLR_STEP)→ gen-linkml  $$(s)$(CLR_RST)" && echo "$$(LINKML_RUN) gen-linkml $$(s) > /dev/null" && $$(LINKML_RUN) gen-linkml $$(s) > /dev/null;)
	$$(call run_gen,$$(_schemas_$(1)),gen-jsonld-context,context.jsonld)
	$$(call run_gen_shacl,$$(_schemas_$(1)))
	$$(call run_gen,$$(_schemas_$(1)),gen-python,model.py)
	$$(call run_gen,$$(_schemas_$(1)),gen-json-schema,schema.json)
	$$(call run_gen_owl,$$(_schemas_$(1)))
	$$(call run_gen_rdf,$$(_schemas_$(1)))
	@for example in $$(find $(SCHEMA_DIR)/$(1) -path '*/examples/*-eksempel.yaml' 2>/dev/null | sort); do \
		[ -f "$$$$example" ] || continue; \
		name=$$$$(basename "$$$$example" .yaml); \
		profil=$$$$(echo "$$$$name" | sed 's/-eksempel$$$$//'); \
		if [ -f $(SCHEMA_DIR)/$(1)/$$$$profil/manifest.yaml ] && grep -q "^  example_rdf: false" $(SCHEMA_DIR)/$(1)/$$$$profil/manifest.yaml; then \
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
	$$(call run_gen_doc,$$(_schemas_$(1)))
	$$(call run_gen_erdiagram,$$(_schemas_$(1)))
	$$(call run_gen,$$(_schemas_$(1)),gen-proto,schema.proto)
	$$(call run_gen_plantuml,$$(_schemas_$(1)))
endef

$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))

# ---------------------------------------------------------------------------
# Per-artifakt-mål for CI – krev DOMAIN=<domenenamn>
# Eksempel: make domain-gen-shapes DOMAIN=oreg
# ---------------------------------------------------------------------------

domain-gen-linkml:
	@$(foreach s,$(_schemas_$(DOMAIN)),echo "$(CLR_STEP)→ gen-linkml  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-linkml $(s) > /dev/null" && $(LINKML_RUN) gen-linkml $(s) > /dev/null;)

domain-gen-context:
	$(call run_gen,$(_schemas_$(DOMAIN)),gen-jsonld-context,context.jsonld)

domain-gen-shapes:
	$(call run_gen_shacl,$(_schemas_$(DOMAIN)))

domain-gen-python:
	$(call run_gen,$(_schemas_$(DOMAIN)),gen-python,model.py)

domain-gen-json-schema:
	$(call run_gen,$(_schemas_$(DOMAIN)),gen-json-schema,schema.json)

domain-gen-owl:
	$(call run_gen_owl,$(_schemas_$(DOMAIN)))

domain-gen-rdf:
	$(call run_gen_rdf,$(_schemas_$(DOMAIN)))

domain-gen-examples:
	@for example in $$(find $(SCHEMA_DIR)/$(DOMAIN) -path '*/examples/*-eksempel.yaml' 2>/dev/null | sort); do \
		[ -f "$$example" ] || continue; \
		name=$$(basename "$$example" .yaml); \
		profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
		if [ -f $(SCHEMA_DIR)/$(DOMAIN)/$$profil/manifest.yaml ] && grep -q "^  example_rdf: false" $(SCHEMA_DIR)/$(DOMAIN)/$$profil/manifest.yaml; then \
			echo "Hoppar over linkml-convert for $$example (example_rdf: false)"; \
			continue; \
		fi; \
		mkdir -p $(GEN_DIR)/$(DOMAIN)/$$profil; \
		if [ -f tests/fixtures/$$profil-fixture.yaml ]; then \
			schema=tests/fixtures/$$profil-fixture.yaml; \
		else \
			schema=$(SCHEMA_DIR)/$(DOMAIN)/$$profil/$$profil-schema.yaml; \
		fi; \
		echo "$(CLR_STEP)→ linkml-convert  $$example$(CLR_RST)"; \
		echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate $$example > $(GEN_DIR)/$(DOMAIN)/$$profil/$$name.ttl"; \
		$(LINKML_RUN) linkml-convert \
			--schema $$schema \
			--output-format ttl \
			--no-validate \
			$$example > $(GEN_DIR)/$(DOMAIN)/$$profil/$$name.ttl; \
	done

domain-gen-data:
	@for datadir in $$(find $(SCHEMA_DIR)/$(DOMAIN) -mindepth 3 -maxdepth 3 -type d -path '*/data/*/*' 2>/dev/null | sort); do \
		model=$$(echo "$$datadir" | awk -F/ '{print $$4}'); \
		catalog=$$(basename "$$datadir"); \
		manifest="$$datadir/manifest.yaml"; \
		[ -f "$$manifest" ] || continue; \
		publish_external=$$(grep '^publish_external:' "$$manifest" | awk '{print $$2}'); \
		[ "$$publish_external" = "true" ] || continue; \
		datafile="$$datadir/$$catalog.yaml"; \
		[ -f "$$datafile" ] || continue; \
		schema=$(SCHEMA_DIR)/$(DOMAIN)/$$model/$$model-schema.yaml; \
		mkdir -p $(GEN_DIR)/$(DOMAIN)/$$catalog; \
		echo "$(CLR_STEP)→ linkml-convert  $$datafile$(CLR_RST)"; \
		echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate $$datafile > $(GEN_DIR)/$(DOMAIN)/$$catalog/$$catalog.ttl"; \
		$(LINKML_RUN) linkml-convert \
			--schema $$schema \
			--output-format ttl \
			--no-validate \
			$$datafile > $(GEN_DIR)/$(DOMAIN)/$$catalog/$$catalog.ttl; \
	done

domain-validate-data:
	@for datadir in $$(find $(SCHEMA_DIR)/$(DOMAIN) -mindepth 3 -maxdepth 3 -type d -path '*/data/*/*' 2>/dev/null | sort); do \
		model=$$(echo "$$datadir" | awk -F/ '{print $$4}'); \
		catalog=$$(basename "$$datadir"); \
		datafile="$$datadir/$$catalog.yaml"; \
		[ -f "$$datafile" ] || continue; \
		schema=$(SCHEMA_DIR)/$(DOMAIN)/$$model/$$model-schema.yaml; \
		manifest="$$datadir/manifest.yaml"; \
		if [ -f "$$manifest" ]; then \
			policy=$$(grep '^data_policy:' "$$manifest" | awk '{print $$2}'); \
		else \
			policy=bronze; \
		fi; \
		[ -n "$$policy" ] || policy=bronze; \
		echo "$(CLR_STEP)→ mcp-validate  $$datafile  (policy: $$policy)$(CLR_RST)"; \
		$(MAKE) --no-print-directory mcp-validate SCHEMA=$$schema POLICY=$$policy INSTANCE=$$datafile; \
	done

check-published-uris:
	@failed=0; \
	for lock in $$(find $(SCHEMA_DIR) -name 'published-uris.lock' 2>/dev/null); do \
		model_dir=$$(dirname "$$lock"); \
		model=$$(basename "$$model_dir"); \
		domain=$$(basename "$$(dirname "$$model_dir")"); \
		data_dir=$(SCHEMA_DIR)/$$domain/$$model/data/$$model; \
		data=$$data_dir/$$model.yaml; \
		[ -f "$$data" ] || { echo "Ingen datafil $$data for $$lock — hoppar over"; continue; }; \
		while IFS= read -r uri; do \
			[ -z "$$uri" ] && continue; \
			printf '%s' "$$uri" | grep -q '^#' && continue; \
			if ! grep -qF "$$uri" "$$data"; then \
				echo "FEIL: Publisert URI manglar frå datafila: $$uri" >&2; \
				failed=1; \
			fi; \
		done < "$$lock"; \
	done; \
	exit $$failed

domain-gen-doc:
	$(call run_gen_doc,$(_schemas_$(DOMAIN)))

domain-gen-erdiagram:
	$(call run_gen_erdiagram,$(_schemas_$(DOMAIN)))

domain-gen-proto:
	$(call run_gen,$(_schemas_$(DOMAIN)),gen-proto,schema.proto)

domain-gen-plantuml:
	$(call run_gen_plantuml,$(_schemas_$(DOMAIN)))

# ---------------------------------------------------------------------------
# Per-skjema-mål for CI — krev SCHEMA=<sti-til-skjema>
# Eksempel: make schema-gen-shapes SCHEMA=src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml
# ---------------------------------------------------------------------------

schema-gen-linkml:
	@echo "$(CLR_STEP)→ gen-linkml  $(SCHEMA)$(CLR_RST)"
	$(LINKML_RUN) gen-linkml $(SCHEMA) > /dev/null

schema-gen-context:
	$(call run_gen,$(SCHEMA),gen-jsonld-context,context.jsonld)

schema-gen-shapes:
	$(call run_gen_shacl,$(SCHEMA))

schema-gen-python:
	$(call run_gen,$(SCHEMA),gen-python,model.py)

schema-gen-json-schema:
	$(call run_gen,$(SCHEMA),gen-json-schema,schema.json)

schema-gen-owl:
	$(call run_gen_owl,$(SCHEMA))

schema-gen-rdf:
	$(call run_gen_rdf,$(SCHEMA))

schema-gen-erdiagram:
	$(call run_gen_erdiagram,$(SCHEMA))

schema-gen-doc:
	$(call run_gen_doc,$(SCHEMA))

schema-gen-proto:
	$(call run_gen,$(SCHEMA),gen-proto,schema.proto)

schema-gen-plantuml:
	$(call run_gen_plantuml,$(SCHEMA))

schema-gen-examples:
	@domain=$(call schema_domain,$(SCHEMA)); \
	name=$(call schema_name,$(SCHEMA)); \
	example=$(SCHEMA_DIR)/$$domain/$$name/examples/$$name-eksempel.yaml; \
	[ -f "$$example" ] || { echo "Ingen eksempelfil: $$example (hoppar over)"; exit 0; }; \
	manifest=$(dir $(SCHEMA))manifest.yaml; \
	if [ -f "$$manifest" ] && grep -q "^  example_rdf: false" "$$manifest"; then \
		echo "Hoppar over linkml-convert for $$example (example_rdf: false)"; exit 0; \
	fi; \
	mkdir -p $(GEN_DIR)/$$domain/$$name; \
	if [ -f tests/fixtures/$$name-fixture.yaml ]; then \
		schema_arg=tests/fixtures/$$name-fixture.yaml; \
	else \
		schema_arg=$(SCHEMA); \
	fi; \
	echo "$(CLR_STEP)→ linkml-convert  $$example$(CLR_RST)"; \
	$(LINKML_RUN) linkml-convert \
		--schema $$schema_arg \
		--output-format ttl \
		--no-validate \
		--output $(GEN_DIR)/$$domain/$$name/$$name-eksempel.ttl \
		$$example

domain-validate-bronze:
	@set +e; \
	FAILED=0; \
	while IFS= read -r schema; do \
		echo "--- $$schema ---"; \
		result=$$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$$schema" bronze 2>/dev/null); \
		echo "$$result"; \
		if ! SCHEMA="$$schema" python3 -c "import json,sys,os;d=json.loads(sys.stdin.read());s=os.environ.get('SCHEMA','');[print('::{} file={}::{}: {}'.format('error' if i.get('severity')=='error' else 'warning',s,i.get('target',''),i.get('message','').replace(chr(10),' '))) for i in d.get('issues',[])];sys.exit(0 if d.get('valid',True) else 1)" <<< "$$result"; then \
			FAILED=$$((FAILED + 1)); \
		fi; \
	done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort); \
	exit $$FAILED

domain-validate-examples:
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
		if echo "$$result" | grep -q "\[ERROR\]"; then \
			echo "$$result" | grep "\[ERROR\]" | while IFS= read -r line; do \
				echo "::error file=$$example::$$(echo "$$line" | sed 's/\[ERROR\] //')"; \
			done; \
			FAILED=$$((FAILED + 1)); \
		fi; \
	done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
		| grep -v common | sort | xargs grep -l "tree_root: true"); \
	exit $$FAILED

# ---------------------------------------------------------------------------
# Dokumentasjonsportal (MkDocs Material)
# ---------------------------------------------------------------------------
# Bygg lokal docs-image med mkdocs-kroki (trengst for PlantUML-rendering via Kroki.io).
# Køyr éin gong, eller etter endringar i mkdocs/Dockerfile.
docs-build-docker:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-docker$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -f $(DOCS_DOCKERFILE) -t $(DOCS_IMAGE)

docs-serve:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-serve$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"
	$(DOCS_RUN) -it -p 8000:8000 $(DOCS_IMAGE) serve --dev-addr=0.0.0.0:8000 --dirtyreload

docs-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"
	$(DOCS_RUN) $(DOCS_IMAGE) build

# Raskare bygg for iterativ utvikling: hoppar over sider utan endringar sidan sist bygg.
# Bruk docs-build for reine produksjonsbyggjer.
docs-build-fast:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-build-fast$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"
	$(DOCS_RUN) $(DOCS_IMAGE) build --dirty

# ---------------------------------------------------------------------------
# MCP-validator
# ---------------------------------------------------------------------------
MCP_RUN := podman run -i --rm \
  -v "$(CURDIR)/$(MCP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(MCP_DIR)/policies:/app/policies:ro"

mcp-val-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-val-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -t $(MCP_IMAGE) $(MCP_DIR)

mcp-val-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-val-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(MCP_RUN) $(MCP_IMAGE)

mcp-val-smoke: mcp-val-build
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-val-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-validator.json | $(MCP_RUN) $(MCP_IMAGE)

mcp-val-test: mcp-val-build
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-val-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR):/work:ro" \
		-e PYTHONWARNINGS=ignore \
		$(MCP_IMAGE) \
		python3 /work/tests/test_mcp_policies.py -v

mcp-build: mcp-val-build
mcp-run: mcp-val-run
mcp-smoke: mcp-val-smoke
mcp-test-policies: mcp-val-test

# ---------------------------------------------------------------------------
# mcp-linkml-modell-utkast
# ---------------------------------------------------------------------------
mcp-mod-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-mod-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -t $(LINKML_MOD_IMAGE) $(LINKML_MOD_DIR)

mcp-mod-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-mod-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-mod-smoke: mcp-mod-build
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-mod-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-generator.json | $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-mod-test: mcp-mod-build
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-mod-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR)/$(LINKML_MOD_DIR):/app/mcp-linkml-modell-utkast:ro" \
		-v "$(CURDIR)/tests:/app/tests:ro" \
		-w /app/tests \
		-e PYTHONPATH=/app/mcp-linkml-modell-utkast \
		$(LINKML_MOD_IMAGE) \
		python -m pytest test_mcp_linkml_generator.py -v

linkml-gen-build: mcp-mod-build
linkml-gen-run: mcp-mod-run
linkml-gen-smoke: mcp-mod-smoke
linkml-gen-test-converter: mcp-mod-test

# Bruk: make mcp-generate SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=default]
mcp-generate:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-generate SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=default]"; exit 1)
	@python3 -c "\
import json; \
content = open('$(SCHEMA)').read(); \
fmt = '$(or $(FORMAT),json-schema)'; \
profile = '$(or $(PROFILE),default)'; \
msgs = [ \
  {'jsonrpc':'2.0','id':1,'method':'initialize','params':{}}, \
  {'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'generate_linkml','arguments':{'inputFormat':fmt,'inputContent':content,'schemaId':'https://example.org/generated','schemaName':'generated','profile':profile}}}, \
]; \
print('\n'.join(json.dumps(m) for m in msgs)) \
" | $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE) \
  | python3 -c "\
import json, sys, pathlib; \
inp = pathlib.Path('$(SCHEMA)'); \
out = inp.parent / (inp.stem + '-schema.yaml'); \
[out.write_text(json.loads(r['result']['content'][0]['text'])['linkmlSchema'], encoding='utf-8') \
 or print('Skriv til:', out) \
 for r in map(json.loads, sys.stdin) if r.get('id') == 2] \
"

linkml-gen-generate: mcp-generate

# ---------------------------------------------------------------------------
# mcp-linkml-begrep-utkast
# ---------------------------------------------------------------------------
mcp-begrep-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-begrep-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -t $(LINKML_BEGREP_IMAGE) $(LINKML_BEGREP_DIR)

mcp-begrep-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-begrep-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

mcp-begrep-smoke: mcp-begrep-build
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-begrep-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# List profiler:
#   make mcp-begrep-list-profiles
mcp-begrep-list-profiles:
	@podman image exists $(LINKML_BEGREP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory mcp-begrep-build
	@echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_profiles","arguments":{}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# Bruk: make new-model NAME=<namn> DOMAIN=<domene>
new-model:
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-model NAME=<namn> DOMAIN=<domene>"; exit 1)
	@podman image exists $(LINKML_MOD_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory mcp-mod-build
	bash src/assets/scripts/new-model.sh "$(NAME)" "$(DOMAIN)"

check-prereqs:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make check-prereqs$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@bash src/assets/scripts/check-prereqs.bash

# Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=gold]
mcp-validate:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=gold]"; exit 1)
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-validate  SCHEMA=$(SCHEMA)  POLICY=$(POLICY)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory mcp-val-build
	bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $(POLICY) $(INSTANCE)

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

gource-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gource-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -f $(GOURCE_DOCKERFILE) -t $(GOURCE_IMAGE)

gource-preview: gource-build
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

gource-video: gource-build
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
