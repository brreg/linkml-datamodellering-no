SHELL           	:= /bin/bash
.SHELLFLAGS     	:= -o pipefail -c
LINKML_IMAGE    	:= localhost/linkml-local:latest
LINKML_DOCKERFILE 	:= src/assets/containers/Dockerfile.linkml
LINKML_RUN     		:= podman run --rm -v "$(CURDIR):/work" -w /work -e PYTHONWARNINGS=ignore -e HOME=/tmp --user root $(LINKML_IMAGE)
AVROTIZE_IMAGE		:= localhost/avrotize-local:latest
AVROTIZE_DOCKERFILE	:= src/assets/containers/Dockerfile.avrotize
AVROTIZE_RUN		:= podman run --rm -v "$(CURDIR):/work" $(AVROTIZE_IMAGE)
ASYNCAPI_IMAGE		:= localhost/asyncapi-cli-local:latest
ASYNCAPI_DOCKERFILE	:= src/assets/containers/Dockerfile.asyncapi-cli
ASYNCAPI_RUN		:= podman run --rm -v "$(CURDIR):/work" -e SUPPRESS_NO_CONFIG_WARNING=true $(ASYNCAPI_IMAGE)
GEN_DIR    			:= generated
SCHEMA_DIR 			:= src/linkml
MCP_DIR    			:= src/mcp-linkml-validator
MCP_IMAGE  			:= mcp-linkml-validator
INSTANCE   			?=
POLICY     			?=
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

# Helper: bestem kva skjema som skal prosesserast basert på DOMAIN eller SCHEMA
# Returnerer liste av skjema-stiar
define get_target_schemas
$(if $(SCHEMA),$(SCHEMA),$(if $(DOMAIN),$(filter src/linkml/$(DOMAIN)/%,$(SCHEMAS)),$(SCHEMAS)))
endef

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
  echo "$(LINKML_RUN) gen-doc --template-directory src/assets/templates/docgen --no-mergeimports --no-render-imports --no-hierarchical-class-view --diagram-type mermaid_class_diagram --example-directory $(call schema_outdir,$(s))/docgen-examples -d $(call schema_outdir,$(s))/docs $(s)" && \
  mkdir -p $(call schema_outdir,$(s))/docs && \
  $(LINKML_RUN) gen-doc \
    --template-directory src/assets/templates/docgen \
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

# Per-schema XSD generator via avrotize: JSON Schema → (fix dates) → XSD.
# Hoppar over skjema der manifest.yaml ikkje har "xsd: true".
# Avheng av at gen-jsonschema er køyrt først.
define run_gen_xsd
@for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	manifest=$$(dirname "$$schema")/manifest.yaml; \
	if [ ! -f "$$manifest" ] || ! grep -q "^  xsd: true" "$$manifest"; then \
		continue; \
	fi; \
	jsonschema=$(GEN_DIR)/$$domain/$$name/$$name-schema.json; \
	if [ ! -f "$$jsonschema" ]; then \
		echo "ÅTVARING: $$jsonschema finst ikkje — hoppar over gen-xsd for $$name" >&2; \
		continue; \
	fi; \
	avsc=$(GEN_DIR)/$$domain/$$name/$$name.avsc; \
	xsd=$(GEN_DIR)/$$domain/$$name/$$name-schema.xsd; \
	namespace=$$(grep '^id:' "$$schema" | head -1 | awk '{print $$2}'); \
	mkdir -p $(GEN_DIR)/$$domain/$$name; \
	echo "$(CLR_STEP)→ gen-xsd  $$schema$(CLR_RST)"; \
	$(AVROTIZE_RUN) j2a /work/$$jsonschema --out /work/$$avsc; \
	$(AVROTIZE_RUN) a2x /work/$$avsc --namespace "$$namespace" --out /work/$$xsd; \
	rm -f "$$avsc"; \
	podman run --rm --entrypoint python3 -v "$(CURDIR):/work" $(AVROTIZE_IMAGE) \
		/work/src/assets/scripts/fix-xsd-dates.py /work/$$xsd /work/$$jsonschema; \
done
endef

# Per-schema AsyncAPI 3.0 generator: JSON Schema → AsyncAPI YAML → validate.
# Hoppar over skjema der manifest.yaml ikkje har "asyncapi: true".
# Avheng av at gen-jsonschema er køyrt først.
define run_gen_asyncapi
@for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	manifest=$$(dirname "$$schema")/manifest.yaml; \
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
	$(PYTHON_RUN) python3 src/assets/scripts/gen-asyncapi.py \
		/work/$$jsonschema /work/$$schema --out /work/$$out; \
	$(ASYNCAPI_RUN) \
		validate /work/$$out; \
done
endef

# Per-schema OpenAPI 3.1 generator: JSON Schema → OpenAPI YAML → validate.
# Hoppar over skjema der manifest.yaml ikkje har "openapi: true".
# Avheng av at gen-jsonschema er køyrt først.
define run_gen_openapi
@for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	manifest=$$(dirname "$$schema")/manifest.yaml; \
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
	$(PYTHON_RUN) python3 src/assets/scripts/gen-openapi.py \
		/work/$$jsonschema /work/$$schema --out /work/$$out; \
	$(PYTHON_RUN) openapi-spec-validator /work/$$out; \
done
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

.PHONY: all test roundtrip validate lint validate-instance clean domains gen-config \
		gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl gen-rdf gen-erdiagram convert-rdf convert-data gen-docs \
        gen-proto gen-plantuml gen-xsd gen-asyncapi gen-openapi \
        validate-bronze validate-data validate-examples \
        build-docker-linkml build-docker-python build-docker-avrotize build-docker-asyncapi build-docker-mkdocs \
        build-docker-mcp-validator build-docker-mcp-modell-utkast build-docker-mcp-begrep-utkast build-docker-gource \
        mcp-validator-run mcp-validator-smoke mcp-validator-test mcp-validate \
        mcp-modell-utkast-run mcp-modell-utkast-smoke mcp-modell-utkast-test mcp-linkml-modell-utkast mcp-generate new-model \
        mcp-begrep-utkast-run mcp-begrep-utkast-smoke mcp-begrep-utkast-list-profiles mcp-linkml-begrep-utkast \
		docs-serve docs-build docs-build-fast publish \
        $(DOMAINS) \
        check-published-uris check-prereqs \
        update-modellkatalog gen-dqv-measurements gen-modelldcat-elements new-org-catalog new-begrepskatalog \
        validate-capture \
        build-docker-gource gource-preview gource-video _gource-render

all: test

domains: $(DOMAINS)

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
	@$(foreach s,$(SCHEMAS),echo "$(CLR_STEP)→ gen-linkml  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-linkml $(s) > /dev/null" && $(LINKML_RUN) gen-linkml $(s) > /dev/null;)

# Bruk: make lint [SCHEMA=<sti-til-skjema>]
lint:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make lint$(if $(SCHEMA),  SCHEMA=$(SCHEMA),  (alle skjema))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@if [ -n "$(SCHEMA)" ]; then \
		$(LINKML_RUN) linkml lint "$(SCHEMA)"; \
	else \
		$(foreach s,$(SCHEMAS),$(LINKML_RUN) linkml lint "$(s)" &&) true; \
	fi

# Bruk: make validate-instance SCHEMA=<sti-til-skjema> INSTANCE=<sti-til-datafil>
validate-instance:
	@test -n "$(SCHEMA)" || (echo "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@test -n "$(INSTANCE)" || (echo "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make validate-instance  SCHEMA=$(SCHEMA)  INSTANCE=$(INSTANCE)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_RUN) linkml validate --schema "$(SCHEMA)" "$(INSTANCE)"

gen-jsonld:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-jsonld SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-jsonld DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-jsonld$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(call get_target_schemas),gen-jsonld-context,context.jsonld)

gen-shacl:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-shacl SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-shacl DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-shacl$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_shacl,$(call get_target_schemas))

gen-python:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-python SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-python DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-python$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(call get_target_schemas),gen-python,model.py)

gen-jsonschema:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-jsonschema SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-jsonschema DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-jsonschema$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(call get_target_schemas),gen-json-schema,schema.json)

gen-owl:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-owl SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-owl DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-owl$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_owl,$(call get_target_schemas))

gen-rdf:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-rdf SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-rdf DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-rdf$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_rdf,$(call get_target_schemas))

gen-xsd:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-xsd SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-xsd DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-xsd$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_xsd,$(call get_target_schemas))

gen-asyncapi:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-asyncapi SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-asyncapi DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-asyncapi$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_asyncapi,$(call get_target_schemas))

gen-openapi:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-openapi SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-openapi DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-openapi$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_openapi,$(call get_target_schemas))

build-docker-linkml:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-linkml$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -f $(LINKML_DOCKERFILE) -t $(LINKML_IMAGE)

build-docker-python:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-python$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -f $(PYTHON_DOCKERFILE) -t $(PYTHON_IMAGE)

build-docker-avrotize:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-avrotize$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -f $(AVROTIZE_DOCKERFILE) -t $(AVROTIZE_IMAGE)

build-docker-asyncapi:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-asyncapi$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -f $(ASYNCAPI_DOCKERFILE) -t $(ASYNCAPI_IMAGE)



gen-erdiagram:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-erdiagram SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-erdiagram DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-erdiagram$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_erdiagram,$(call get_target_schemas))

gen-docs:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-docs SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-docs DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-docs$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_doc,$(call get_target_schemas))
	$(call run_gen_erdiagram,$(call get_target_schemas))

gen-proto:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-proto SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-proto DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-proto$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(call get_target_schemas),gen-proto,schema.proto)

gen-plantuml:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-plantuml SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-plantuml DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-plantuml$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_plantuml,$(call get_target_schemas))

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
	@for datadir in $$(find $(SCHEMA_DIR) -mindepth 4 -maxdepth 4 -type d -path '*/data/*' | sort); do \
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

# Oppdater Informasjonsmodell-innslag i modellkatalogen frå schema.annotations.*.
# Les annotations frå alle skjema med annotations.utgiver og skriv til katalogdatafila.
update-modellkatalog:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make update-modellkatalog$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	python3 src/assets/scripts/update-modellkatalog.py

# Reknar ut DQV-kvalitetsmålingar (fullstendighet/aktualitet) for datafiler med
# data_policy felles-begrepskatalog/felles-datakatalog og skriv dem attende.
gen-dqv-measurements:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-dqv-measurements$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(PYTHON_RUN) python3 src/assets/scripts/gen-dqv-measurements.py

# Genererer ModelDCAT-AP-NO-modellelement (Objekttype/Attributt/Assosiasjon/
# Kodeliste/Kodeelement) frå LinkML-skjemastruktur og skriv dem inn i riktig
# org sin modellkatalog-datafil. Krev SchemaView, derfor $(LINKML_RUN) (ikkje
# $(PYTHON_RUN)). Bruk: make gen-modelldcat-elements [ORG=alias] [DRYRUN=1]
gen-modelldcat-elements:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-modelldcat-elements$(if $(ORG),  ORG=$(ORG))$(if $(DRYRUN),  DRYRUN=$(DRYRUN))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_RUN) python3 src/assets/scripts/gen-modelldcat-elements.py $(if $(ORG),--org $(ORG)) $(if $(DRYRUN),--dry-run)

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
	$$(call run_gen_xsd,$$(_schemas_$(1)))
	$$(call run_gen_openapi,$$(_schemas_$(1)))
	$$(call run_gen_asyncapi,$$(_schemas_$(1)))
endef

$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))

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
		python3 src/assets/scripts/save-validation-log.py \
			--schema "$$schema" --type bronze --result "$$result" 2>/dev/null || true; \
		if ! SCHEMA="$$schema" python3 -c "import json,sys,os;d=json.loads(sys.stdin.read());s=os.environ.get('SCHEMA','');[print('::{} file={}::{}: {}'.format('error' if i.get('severity')=='error' else 'warning',s,i.get('target',''),i.get('message','').replace(chr(10),' '))) for i in d.get('issues',[])];sys.exit(0 if d.get('valid',True) else 1)" <<< "$$result"; then \
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
		manifest="$$datadir/manifest.yaml"; \
		if [ -f "$$manifest" ]; then \
			policy=$$(grep '^validation_policy:' "$$manifest" | awk '{print $$2}'); \
		else \
			policy=bronze; \
		fi; \
		[ -n "$$policy" ] || policy=bronze; \
		echo "$(CLR_STEP)→ mcp-validate  $$datafile  (policy: $$policy)$(CLR_RST)"; \
		result=$$(bash $(MCP_DIR)/flatten-and-validate.bash "$$schema" "$$policy" "$$datafile" 2>/dev/null); \
		echo "$$result"; \
		python3 src/assets/scripts/save-validation-log.py \
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
		python3 src/assets/scripts/save-validation-log.py \
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
	podman build -f $(DOCS_DOCKERFILE) -t $(DOCS_IMAGE)

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

build-docker-mcp-validator:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-validator$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -t $(MCP_IMAGE) $(MCP_DIR)

mcp-validator-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-validator-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(MCP_RUN) $(MCP_IMAGE)

mcp-validator-smoke: build-docker-mcp-validator
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-validator-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-validator.json | $(MCP_RUN) $(MCP_IMAGE)

mcp-validator-test: build-docker-mcp-validator
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-validator-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR):/work:ro" \
		-e PYTHONWARNINGS=ignore \
		$(MCP_IMAGE) \
		python3 /work/tests/test_mcp_policies.py -v

mcp-build: build-docker-mcp-validator
mcp-run: mcp-validator-run
mcp-smoke: mcp-validator-smoke
mcp-test-policies: mcp-validator-test

# ---------------------------------------------------------------------------
# mcp-linkml-modell-utkast
# ---------------------------------------------------------------------------
build-docker-mcp-modell-utkast:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-modell-utkast$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -t $(LINKML_MOD_IMAGE) $(LINKML_MOD_DIR)

mcp-modell-utkast-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-modell-utkast-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-modell-utkast-smoke: build-docker-mcp-modell-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-modell-utkast-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-generator.json | $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-modell-utkast-test: build-docker-mcp-modell-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-modell-utkast-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR)/$(LINKML_MOD_DIR):/app/mcp-linkml-modell-utkast:ro" \
		-v "$(CURDIR)/tests:/app/tests:ro" \
		-w /app/tests \
		-e PYTHONPATH=/app/mcp-linkml-modell-utkast \
		$(LINKML_MOD_IMAGE) \
		python -m pytest test_mcp_linkml_generator.py -v

linkml-gen-build: build-docker-mcp-modell-utkast
linkml-gen-run: mcp-modell-utkast-run
linkml-gen-smoke: mcp-modell-utkast-smoke
linkml-gen-test-converter: mcp-modell-utkast-test

# Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=bronze]
mcp-linkml-modell-utkast:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=bronze]"; exit 1)
	@python3 -c "\
import json; \
content = open('$(SCHEMA)').read(); \
fmt = '$(or $(FORMAT),json-schema)'; \
profile = '$(or $(PROFILE),bronze)'; \
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
	@# Automatisk roundtrip-test for JSON Schema
	@if echo "$(SCHEMA)" | grep -qE '\.(json|schema\.json)$$'; then \
		echo "$(CLR_STEP)→ Køyrer roundtrip-test for $(SCHEMA)$(CLR_RST)"; \
		$(MAKE) roundtrip-json-schema JSONSCHEMA="$(SCHEMA)" || \
		(echo "$(CLR_ERR)Roundtrip-test feila — sjå logg for detaljar$(CLR_RST)" && exit 1); \
	fi

mcp-generate: mcp-linkml-modell-utkast
	@echo "Åtvaring: 'make mcp-generate' er omdøypt til 'make mcp-linkml-modell-utkast'" >&2

linkml-gen-generate: mcp-linkml-modell-utkast

# ---------------------------------------------------------------------------
# mcp-linkml-begrep-utkast
# ---------------------------------------------------------------------------
build-docker-mcp-begrep-utkast:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-begrep-utkast$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -t $(LINKML_BEGREP_IMAGE) $(LINKML_BEGREP_DIR)

mcp-begrep-utkast-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-begrep-utkast-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

mcp-begrep-utkast-smoke: build-docker-mcp-begrep-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-begrep-utkast-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# Bruk: make mcp-linkml-begrep-utkast INPUT=tmp/mitt-begrep.json
mcp-linkml-begrep-utkast:
	@test -n "$(INPUT)" || \
	  (echo "Bruk: make mcp-linkml-begrep-utkast INPUT=<sti-til-json>"; exit 1)
	@test -f "$(INPUT)" || \
	  (echo "Feil: $(INPUT) finst ikkje"; exit 1)
	@printf '%s\n%s\n' \
	  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"make","version":"1"}}}' \
	  "$$(python3 -c "import json; args=json.load(open('$(INPUT)')); print(json.dumps({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'opprett_begrep','arguments':args}}))")" \
	  | $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# List profiler:
#   make mcp-begrep-utkast-list-profiles
mcp-begrep-utkast-list-profiles:
	@podman image exists $(LINKML_BEGREP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-begrep-utkast
	@echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_profiles","arguments":{}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# Bruk: make new-model NAME=<namn> DOMAIN=<domene>
new-model:
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-model NAME=<namn> DOMAIN=<domene>"; exit 1)
	@podman image exists $(LINKML_MOD_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-modell-utkast
	bash src/assets/scripts/new-model.sh "$(NAME)" "$(DOMAIN)"

# Bruk: make new-org-catalog ORG=<alias>
new-org-catalog:
	@test -n "$(ORG)" || (echo "Bruk: make new-org-catalog ORG=<alias>"; exit 1)
	bash src/assets/scripts/new-org-catalog.sh "$(ORG)"

# Bruk: make new-begrepskatalog NAME=<katalognavn>
new-begrepskatalog:
	@test -n "$(NAME)" || \
	  (echo "Bruk: make new-begrepskatalog NAME=<katalognavn>"; exit 1)
	bash src/assets/scripts/new-begrepskatalog.sh "$(NAME)"

check-prereqs:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make check-prereqs$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@bash src/assets/scripts/check-prereqs.bash

# Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=gold]
# POLICY vert auto-detektert frå manifest.yaml dersom ikkje oppgjeven
mcp-validate:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=gold]"; exit 1)
	@DETECTED_POLICY=$$(python3 -c "import yaml, sys; \
	  manifest_path = '$(dir $(SCHEMA))manifest.yaml'; \
	  manifest = yaml.safe_load(open(manifest_path)) if __import__('os').path.isfile(manifest_path) else {}; \
	  print(manifest.get('validation_policy', 'bronze'))" 2>/dev/null || echo "bronze"); \
	POLICY_TO_USE="$${POLICY:-$$DETECTED_POLICY}"; \
	echo "$(CLR_SEP)$(SEP)$(CLR_RST)"; \
	echo "$(CLR_HDR)*** make mcp-validate  SCHEMA=$(SCHEMA)  POLICY=$$POLICY_TO_USE$(CLR_RST)"; \
	echo "$(CLR_SEP)$(SEP)$(CLR_RST)"; \
	podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator; \
	bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $$POLICY_TO_USE $(INSTANCE)

# Bruk: make validate-capture [SCHEMA=<sti>]
# Utan SCHEMA: køyr for alle skjema.
validate-capture:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make validate-capture$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@if [ -n "$(SCHEMA)" ]; then \
	    python3 src/assets/scripts/run-schema-validation.py --schema $(SCHEMA); \
	else \
	    for schema in $(SCHEMAS); do \
	        python3 src/assets/scripts/run-schema-validation.py --schema $$schema; \
	    done \
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
	podman build -f $(GOURCE_DOCKERFILE) -t $(GOURCE_IMAGE)

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

