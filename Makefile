SHELL           	:= /bin/bash
.SHELLFLAGS     	:= -o pipefail -c
LINKML_IMAGE    	:= localhost/linkml-local:latest
LINKML_DOCKERFILE 	:= src/assets/containers/Dockerfile.linkml
LINKML_RUN     		:= podman run --rm -v "$(CURDIR):/work" -w /work -e PYTHONWARNINGS=ignore --user $(shell id -u):$(shell id -g) $(LINKML_IMAGE)
GEN_DIR    			:= generated
SCHEMA_DIR 			:= src/linkml
MCP_DIR    			:= src/mcp-linkml-validator
MCP_IMAGE  			:= mcp-linkml-validator
DOCS_IMAGE 			:= localhost/mkdocs-local:latest
DOCS_DOCKERFILE 	:= mkdocs/Dockerfile.mkdocs
DOCS_RUN   			:= podman run --rm \
	-v "$(CURDIR)/mkdocs/docs:/docs/docs" \
  	-v "$(CURDIR)/mkdocs/mkdocs.yml:/docs/mkdocs.yml" \
  	-v "$(CURDIR)/mkdocs/overrides:/docs/overrides" \
  	-v "$(CURDIR)/mkdocs/.cache:/docs/.cache"
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

# Domains are derived automatically from the discovered schemas
DOMAINS := $(sort $(foreach s,$(SCHEMAS),$(call schema_domain,$(s))))

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
  echo "$(CLR_STEP)→ gen-doc  $(s)$(CLR_RST)" && \
  echo "$(LINKML_RUN) gen-doc --template-directory src/templates/docgen --no-mergeimports --no-render-imports --no-hierarchical-class-view --diagram-type mermaid_class_diagram -d $(call schema_outdir,$(s))/docs $(s)" && \
  $(LINKML_RUN) gen-doc \
    --template-directory src/templates/docgen \
    --no-mergeimports \
    --no-render-imports \
    --no-hierarchical-class-view \
    --diagram-type mermaid_class_diagram \
    -d $(call schema_outdir,$(s))/docs $(s) && \
  sed -i '/Container/d' $(call schema_outdir,$(s))/docs/index.md; \
)
endef

# ---------------------------------------------------------------------------
# Top-level targets
# ---------------------------------------------------------------------------
LINKML_GEN_DIR   := src/mcp-linkml-generator
LINKML_GEN_IMAGE := mcp-linkml-generator
LINKML_GEN_RUN   := podman run -i --rm \
  -v "$(CURDIR)/$(LINKML_GEN_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(LINKML_GEN_DIR)/converter.py:/app/converter.py:ro" \
  -v "$(CURDIR)/$(LINKML_GEN_DIR)/validator.py:/app/validator.py:ro" \
  -v "$(CURDIR)/$(LINKML_GEN_DIR)/profiles:/app/profiles:ro"

.PHONY: all test validate clean domains \
		gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl gen-rdf gen-erdiagram convert-rdf gen-docs \
        linkml-build-docker python-build-docker \
        mcp-val-build mcp-val-run mcp-val-smoke mcp-val-test mcp-validate \
        mcp-gen-build mcp-gen-run mcp-gen-smoke mcp-gen-test mcp-generate new-model \
        mcp-build mcp-run mcp-smoke mcp-test-policies \
        linkml-gen-build linkml-gen-run linkml-gen-smoke linkml-gen-generate linkml-gen-test-converter \
		docs-build-docker docs-serve docs-build docs-build-fast publish \
        $(DOMAINS)

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
	$(call run_gen,$(filter-out $(SCHEMA_DIR)/fint/%,$(SCHEMAS)),gen-shacl,shapes.ttl)
	$(call run_gen,$(filter $(SCHEMA_DIR)/fint/%,$(SCHEMAS)),gen-shacl --exclude-imports,shapes.ttl)

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
	$(call run_gen,$(filter-out $(SCHEMA_DIR)/fint/%,$(SCHEMAS)),gen-owl,ontology.ttl)
	$(call run_gen,$(filter $(SCHEMA_DIR)/fint/%,$(SCHEMAS)),gen-owl --log_level ERROR,ontology.ttl)

gen-rdf:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-rdf$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(filter-out $(SCHEMA_DIR)/fint/%,$(SCHEMAS)),gen-rdf,schema.ttl)


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

# Convert example YAML to RDF/Turtle for all domains.
# AP-NO profiles have no tree_root and use fixture schemas; others use the schema directly.
convert-rdf:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make convert-rdf$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@for domain in $$(ls examples/); do \
		for example in examples/$$domain/*-eksempel.yaml; do \
			[ -f "$$example" ] || continue; \
			name=$$(basename "$$example" .yaml); \
			profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
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
		done; \
	done

clean:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make clean$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	rm -rf $(GEN_DIR)

# Kopier genererte artefaktar til mkdocs/docs/ og oppdater mkdocs.yml.
# Føresetnad: relevante make <domain>-targets er køyrde fyrst.
publish:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make publish$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	bash mkdocs/publish.sh

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

# fint schemas use cross-schema class inheritance which triggers a bug in the
# SHACL generator (KeyError on schema_map lookup). --exclude-imports avoids it.
SHACL_FLAGS_fint := --exclude-imports

# gen-owl emits "Ambiguous type" warnings for fint schemas because the same slot
# name (e.g. navn) maps to both DatatypeProperty and ObjectProperty ranges across
# different class contexts – an inherent property of the FINT model design.
OWL_FLAGS_fint := --log_level ERROR

# gen-rdf fails for fint schemas: the JSON-LD generator adds a relative
# ../fint-common/fint-common-schema.context.jsonld context reference, which
# rdflib resolves against the schema base URL (https://schema.fintlabs.no/...)
# and fetches over HTTP → 404. Set GEN_RDF_SKIP_<domain> := true to skip.
GEN_RDF_SKIP_fint := true

# gen-rdf fails for samt schemas: same HTTP-fetch issue as fint (imports dcat-ap-no-schema
# whose JSON-LD context reference is resolved against the schema base URL → 404).
GEN_RDF_SKIP_samt := true

define domain_target
_schemas_$(1) := $(filter $(SCHEMA_DIR)/$(1)/%,$(SCHEMAS))

.PHONY: $(1)
$(1):
	@echo "$(CLR_SEP)$$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make $(1)$(CLR_RST)"
	@echo "$(CLR_SEP)$$(SEP)$(CLR_RST)"
	@$$(foreach s,$$(_schemas_$(1)),echo "$(CLR_STEP)→ gen-linkml  $$(s)$(CLR_RST)" && echo "$$(LINKML_RUN) gen-linkml $$(s) > /dev/null" && $$(LINKML_RUN) gen-linkml $$(s) > /dev/null;)
	$$(call run_gen,$$(_schemas_$(1)),gen-jsonld-context,context.jsonld)
	$$(call run_gen,$$(_schemas_$(1)),gen-shacl $$(SHACL_FLAGS_$(1)),shapes.ttl)
	$$(call run_gen,$$(_schemas_$(1)),gen-python,model.py)
	$$(call run_gen,$$(_schemas_$(1)),gen-json-schema,schema.json)
	$$(call run_gen,$$(_schemas_$(1)),gen-owl $$(OWL_FLAGS_$(1)),ontology.ttl)
	$(if $(GEN_RDF_SKIP_$(1)),,$$(call run_gen,$$(_schemas_$(1)),gen-rdf,schema.ttl))
	@for example in examples/$(1)/*-eksempel.yaml; do \
		[ -f "$$$$example" ] || continue; \
		name=$$$$(basename "$$$$example" .yaml); \
		profil=$$$$(echo "$$$$name" | sed 's/-eksempel$$$$//'); \
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
endef

$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))

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
	@mkdir -p "$(CURDIR)/mkdocs/.cache"
	@echo "Sikra katalog: $(CURDIR)/mkdocs/.cache"
	$(DOCS_RUN) -it -p 8000:8000 $(DOCS_IMAGE) serve --dev-addr=0.0.0.0:8000 --dirtyreload --no-livereload

docs-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(DOCS_RUN) $(DOCS_IMAGE) build

# Raskare bygg for iterativ utvikling: hoppar over sider utan endringar sidan sist bygg.
# Bruk docs-build for reine produksjonsbyggjer.
docs-build-fast:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-build-fast$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
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
# mcp-linkml-generator
# ---------------------------------------------------------------------------
mcp-gen-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-gen-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build -t $(LINKML_GEN_IMAGE) $(LINKML_GEN_DIR)

mcp-gen-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-gen-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_GEN_RUN) $(LINKML_GEN_IMAGE)

mcp-gen-smoke: mcp-gen-build
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-gen-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-generator.json | $(LINKML_GEN_RUN) $(LINKML_GEN_IMAGE)

mcp-gen-test: mcp-gen-build
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-gen-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR)/$(LINKML_GEN_DIR):/app/mcp-linkml-generator:ro" \
		-v "$(CURDIR)/tests:/app/tests:ro" \
		-w /app/tests \
		-e PYTHONPATH=/app/mcp-linkml-generator \
		$(LINKML_GEN_IMAGE) \
		python -m pytest test_mcp_linkml_generator.py -v

linkml-gen-build: mcp-gen-build
linkml-gen-run: mcp-gen-run
linkml-gen-smoke: mcp-gen-smoke
linkml-gen-test-converter: mcp-gen-test

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
" | $(LINKML_GEN_RUN) $(LINKML_GEN_IMAGE) \
  | python3 -c "\
import json, sys, pathlib; \
inp = pathlib.Path('$(SCHEMA)'); \
out = inp.parent / (inp.stem + '-schema.yaml'); \
[out.write_text(json.loads(r['result']['content'][0]['text'])['linkmlSchema'], encoding='utf-8') \
 or print('Skriv til:', out) \
 for r in map(json.loads, sys.stdin) if r.get('id') == 2] \
"

linkml-gen-generate: mcp-generate

# Bruk: make new-model NAME=<namn> DOMAIN=<domene>
new-model:
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-model NAME=<namn> DOMAIN=<domene>"; exit 1)
	@podman image exists $(LINKML_GEN_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory mcp-gen-build
	bash src/assets/scripts/new-model.sh "$(NAME)" "$(DOMAIN)"

# Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=gold]
mcp-validate:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=gold]"; exit 1)
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-validate  SCHEMA=$(SCHEMA)  POLICY=$(POLICY)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory mcp-val-build
	bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $(POLICY)
