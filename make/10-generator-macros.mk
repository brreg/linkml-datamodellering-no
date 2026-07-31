# ==============================================================================
# make/10-generator-macros.mk
#
# Generiske generator-makroar for å byggje LinkML-artefaktar.
# ==============================================================================

# ---------------------------------------------------------------------------
# Generisk parallell generator-makro med timer
# ---------------------------------------------------------------------------
# $1=schemas  $2=generator-namn (for logging)  $3=serial-fallback-makro  $4=parallel-kommando
define run_parallel_with_timer
@if [ "$(PARALLEL)" = "1" ]; then \
	$(call $(3),$(1)) \
else \
	printf '%s\n' $(1) | xargs -P $(PARALLEL) -I {} bash -c ' \
		set -euo pipefail; \
		trap '\''echo "ERROR in Makefile parallel job for $$domain/$$name at line $$LINENO — command: $$BASH_COMMAND" >&2; exit 1'\'' ERR; \
		s="{}"; \
		name=$$(basename "$$s" -schema.yaml | sed "s/-schema$$//"); \
		domain=$$(echo "$$s" | cut -d/ -f3); \
		outdir=$(GEN_DIR)/$$domain/$$name; \
		t0=$$(date +%s%3N); \
		$(4); \
		rc=$$?; \
		t1=$$(date +%s%3N); \
		elapsed_ms=$$((t1 - t0)); \
		printf "$(CLR_STEP)→ $(2)  %s/%s$(CLR_RST) (%d.%ds)\n" \
			"$$domain" "$$name" \
			$$((elapsed_ms / 1000)) \
			$$((elapsed_ms % 1000 / 100)); \
		exit $$rc'; \
fi
endef

# ---------------------------------------------------------------------------
# Generisk parallell generator-makro med pre-check (for OpenAPI/AsyncAPI)
# ---------------------------------------------------------------------------
# $1=schemas  $2=generator-namn  $3=manifest-flagg (t.d. "openapi")  $4=input-suffix (t.d. "schema.json")  $5=output-suffix  $6=kommandoar
define run_gen_with_check_parallel
printf '%s\n' $(1) | xargs -P $(PARALLEL) -I {} bash -c ' \
	s="{}"; \
	name=$$(basename "$$s" -schema.yaml | sed "s/-schema$$//"); \
	domain=$$(echo "$$s" | cut -d/ -f3); \
	manifest=$$(dirname "$$s")/build.yaml; \
	if [ ! -f "$$manifest" ] || ! grep -q "^  $(3): true" "$$manifest"; then \
		exit 0; \
	fi; \
	outdir=$(GEN_DIR)/$$domain/$$name; \
	input="$$outdir/$$name-$(4)"; \
	if [ ! -f "$$input" ]; then \
		echo "ÅTVARING: $$input finst ikkje — hoppar over $(2) for $$name" >&2; \
		exit 0; \
	fi; \
	out="$$outdir/$$name-$(5)"; \
	t0=$$(date +%s%3N); \
	mkdir -p "$$outdir"; \
	$(6); \
	rc=$$?; \
	elapsed_ms=$$(($$( date +%s%3N) - t0)); \
	printf "$(CLR_STEP)→ $(2)  %s/%s$(CLR_RST) (%d.%ds)\n" \
		"$$domain" "$$name" \
		$$((elapsed_ms / 1000)) \
		$$((elapsed_ms % 1000 / 100)); \
	exit $$rc'
endef

# ---------------------------------------------------------------------------
# Serial generator-makro (fallback for run_gen når PARALLEL=1)
# ---------------------------------------------------------------------------
# $1=schemas  $2=generator  $3=output-file suffix
define run_gen
@$(foreach s,$(1),echo "$(CLR_STEP)→ $(2)  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) $(2) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-$(3)" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) $(2) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-$(3);)
endef

# Parallell versjon av run_gen med timer
# $1=schemas  $2=generator  $3=output-file suffix
define run_gen_parallel
$(call run_parallel_with_timer,$(1),$(2),run_gen,mkdir -p "$$outdir" && $(LINKML_RUN) $(2) "$$s" > "$$outdir/$$name-$(3)")
endef

# ---------------------------------------------------------------------------
# LinkML merge-imports (gen-linkml)
# ---------------------------------------------------------------------------
# Serial fallback
define run_gen_linkml_serial
@$(foreach s,$(1),echo "$(CLR_STEP)→ merge-imports  $(s)$(CLR_RST)" && $(LINKML_RUN) gen-linkml $(s) > /dev/null;)
endef

# Parallell versjon
define run_gen_linkml_parallel
$(call run_parallel_with_timer,$(1),merge-imports,run_gen_linkml_serial,$(LINKML_RUN) gen-linkml "$$s" > /dev/null)
endef

# ---------------------------------------------------------------------------
# SHACL-generering med per-schema flagg-override
# ---------------------------------------------------------------------------
SHACL_DEFAULT_FLAGS :=
define run_gen_shacl
@$(foreach s,$(1),echo "$(CLR_STEP)→ gen-shacl  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-shacl $(if $(SHACL_FLAGS_$(call schema_key,$(s))),$(SHACL_FLAGS_$(call schema_key,$(s))),$(SHACL_DEFAULT_FLAGS)) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-shapes.ttl" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-shacl $(if $(SHACL_FLAGS_$(call schema_key,$(s))),$(SHACL_FLAGS_$(call schema_key,$(s))),$(SHACL_DEFAULT_FLAGS)) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-shapes.ttl;)
endef

# ---------------------------------------------------------------------------
# OWL-generering med per-schema flagg-override
# ---------------------------------------------------------------------------
OWL_DEFAULT_FLAGS := --skip-vacuous-local-range-axioms --skip-vacuous-min-zero-cardinality-axioms --consolidate-cardinality-axioms
define run_gen_owl
@$(foreach s,$(1),echo "$(CLR_STEP)→ gen-owl  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-owl $(if $(OWL_FLAGS_$(call schema_key,$(s))),$(OWL_FLAGS_$(call schema_key,$(s))),$(OWL_DEFAULT_FLAGS)) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-ontology.ttl" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-owl $(if $(OWL_FLAGS_$(call schema_key,$(s))),$(OWL_FLAGS_$(call schema_key,$(s))),$(OWL_DEFAULT_FLAGS)) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-ontology.ttl;)
endef

# Parallell versjon av gen-owl
# Merk: brukar OWL_DEFAULT_FLAGS i parallell-modus (config.mk overrides vert ikkje propagerte til xargs)
define run_gen_owl_parallel
$(call run_parallel_with_timer,$(1),gen-owl,run_gen_owl,mkdir -p "$$outdir" && $(LINKML_RUN) gen-owl $(OWL_DEFAULT_FLAGS) "$$s" > "$$outdir/$$name-ontology.ttl")
endef

# ---------------------------------------------------------------------------
# RDF-generering med per-schema skip-flagg
# ---------------------------------------------------------------------------
define run_gen_rdf
@$(foreach s,$(1),$(if $(filter true,$(GEN_RDF_SKIP_$(call schema_key,$(s)))),echo "Hoppar over gen-rdf for $(call schema_name,$(s)) (GEN_RDF_SKIP_$(call schema_key,$(s)) er sett)";,echo "$(CLR_STEP)→ gen-rdf  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-rdf $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-schema.ttl" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-rdf $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-schema.ttl;))
endef

# Parallell versjon av gen-rdf
define run_gen_rdf_parallel
$(call run_parallel_with_timer,$(1),gen-rdf,run_gen_rdf,mkdir -p "$$outdir" && $(LINKML_RUN) gen-rdf "$$s" > "$$outdir/$$name-schema.ttl")
endef

# ---------------------------------------------------------------------------
# gen-doc (genererer dokumentasjon til katalog i staden for stdout)
# ---------------------------------------------------------------------------
define run_gen_doc
@$(foreach s,$(1), \
  echo "$(CLR_STEP)→ gen-docgen-examples  $(s)$(CLR_RST)" && \
  mkdir -p $(call schema_outdir,$(s))/docgen-examples && \
  $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-docgen-examples.py \
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

# Parallell versjon av gen-doc
define run_gen_doc_parallel
$(call run_parallel_with_timer,$(1),gen-docgen-examples + gen-doc,run_gen_doc,\
mkdir -p "$$outdir/docgen-examples" "$$outdir/docs" && \
$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-docgen-examples.py \
	"$$s" \
	"src/linkml/$$domain/$$name/examples/$$name-eksempel.yaml" \
	"$$outdir/docgen-examples" > /dev/null 2>&1 && \
$(LINKML_RUN) gen-doc \
	--template-directory src/assets/templates/docgen \
	--no-mergeimports \
	--no-render-imports \
	--no-hierarchical-class-view \
	--diagram-type mermaid_class_diagram \
	--example-directory "$$outdir/docgen-examples" \
	-d "$$outdir/docs" "$$s" > /dev/null 2>&1 && \
sed -i "/Container/d" "$$outdir/docs/index.md")
endef

# ---------------------------------------------------------------------------
# gen-erdiagram (pipar gjennom awk for å stripa Container-klassar)
# ---------------------------------------------------------------------------
define run_gen_erdiagram
@$(foreach s,$(1),echo "$(CLR_STEP)→ gen-erdiagram  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-erdiagram --no-mergeimports $(s) | awk -f src/assets/scripts/makefile/filter_container.awk > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md" && mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-erdiagram --no-mergeimports $(s) \
  | awk -f src/assets/scripts/makefile/filter_container.awk \
  > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md && \
  echo "$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_erdiagram.py $(s) $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram.md" && \
  $(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_erdiagram.py $(s) $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram.md; \
  )
endef

# Parallell versjon av gen-erdiagram
define run_gen_erdiagram_parallel
$(call run_parallel_with_timer,$(1),gen-erdiagram,run_gen_erdiagram,\
mkdir -p "$$outdir" && \
$(LINKML_RUN) gen-erdiagram --no-mergeimports "$$s" \
	| awk -f src/assets/scripts/makefile/filter_container.awk \
	> "$$outdir/$$name-erdiagram-unfiltered.md" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_erdiagram.py \
	"$$s" \
	"$$outdir/$$name-erdiagram-unfiltered.md" \
	> "$$outdir/$$name-erdiagram.md")
endef

# ---------------------------------------------------------------------------
# gen-plantuml (genererer PlantUML-diagram med filtrering)
# ---------------------------------------------------------------------------
define run_gen_plantuml
@$(foreach s,$(1), \
  echo "$(CLR_STEP)→ gen-plantuml  $(s)$(CLR_RST)" && \
  mkdir -p $(call schema_outdir,$(s))/diagrams && \
  $(LINKML_RUN) gen-plantuml $(s) \
    > $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-raw.puml && \
  echo "$(CLR_STEP)→ filter-plantuml (filtered)  $(s)$(CLR_RST)" && \
  $(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py $(s) $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-raw.puml filtered \
    > $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-filtered.puml && \
  echo "$(CLR_STEP)→ filter-plantuml (full)  $(s)$(CLR_RST)" && \
  $(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py $(s) $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-raw.puml full \
    > $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s)).puml && \
  podman run --rm \
    -v "$(CURDIR)/$(call schema_outdir,$(s))/diagrams:/data" \
    $(PLANTUML_IMAGE) -tsvg /data/$(call schema_name,$(s)).puml && \
  podman run --rm \
    -v "$(CURDIR)/$(call schema_outdir,$(s))/diagrams:/data" \
    $(PLANTUML_IMAGE) -tsvg /data/$(call schema_name,$(s))-filtered.puml; \
)
endef

# Parallell versjon av gen-plantuml
define run_gen_plantuml_parallel
$(call run_parallel_with_timer,$(1),gen-plantuml,run_gen_plantuml,\
mkdir -p "$$outdir/diagrams" && \
$(LINKML_RUN) gen-plantuml "$$s" > "$$outdir/diagrams/$$name-raw.puml" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py \
	"$$s" "$$outdir/diagrams/$$name-raw.puml" filtered \
	> "$$outdir/diagrams/$$name-filtered.puml" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py \
	"$$s" "$$outdir/diagrams/$$name-raw.puml" full \
	> "$$outdir/diagrams/$$name.puml" && \
podman run --rm -v "$(CURDIR)/$$outdir/diagrams:/data" $(PLANTUML_IMAGE) -tsvg /data/$$name.puml > /dev/null && \
podman run --rm -v "$(CURDIR)/$$outdir/diagrams:/data" $(PLANTUML_IMAGE) -tsvg /data/$$name-filtered.puml > /dev/null)
endef

# ---------------------------------------------------------------------------
# gen-xsd (JSON Schema → Avro → XSD via avrotize)
# ---------------------------------------------------------------------------
define run_gen_xsd
@for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	manifest=$$(dirname "$$schema")/build.yaml; \
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
	t0=$$(date +%s%3N); \
	$(AVROTIZE_RUN) j2a /work/$$jsonschema --out /work/$$avsc >/dev/null 2>&1; \
	$(AVROTIZE_RUN) a2x /work/$$avsc --namespace "$$namespace" --out /work/$$xsd >/dev/null 2>&1; \
	rm -f "$$avsc"; \
	podman run --rm --entrypoint python3 -v "$(CURDIR):/work" $(AVROTIZE_IMAGE) \
		/work/src/assets/scripts/makefile/fix-xsd-dates.py /work/$$xsd /work/$$jsonschema >/dev/null 2>&1; \
	elapsed_ms=$$(($$( date +%s%3N) - t0)); \
	printf "$(CLR_STEP)→ gen-xsd  %s/%s$(CLR_RST) (%d.%ds)\n" \
		"$$domain" "$$name" \
		$$((elapsed_ms / 1000)) \
		$$((elapsed_ms % 1000 / 100)); \
done
endef

# ---------------------------------------------------------------------------
# gen-asyncapi (JSON Schema → AsyncAPI YAML → validate)
# ---------------------------------------------------------------------------
define run_gen_asyncapi
@for schema in $(1); do \
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
	$(ASYNCAPI_RUN) \
		validate /work/$$out; \
done
endef

# Parallell versjon av gen-asyncapi
define run_gen_asyncapi_parallel
$(call run_gen_with_check_parallel,$(1),gen-asyncapi,asyncapi,schema.json,asyncapi.yaml,$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py /work/$$input /work/$$s --out /work/$$out > /dev/null 2>&1; $(ASYNCAPI_RUN) validate /work/$$out > /dev/null 2>&1)
endef

# ---------------------------------------------------------------------------
# gen-openapi (JSON Schema → OpenAPI YAML → validate)
# ---------------------------------------------------------------------------
define run_gen_openapi
@for schema in $(1); do \
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
done
endef

# Parallell versjon av gen-openapi
define run_gen_openapi_parallel
$(call run_gen_with_check_parallel,$(1),gen-openapi,openapi,schema.json,openapi.yaml,$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py /work/$$input /work/$$s --out /work/$$out > /dev/null 2>&1; $(PYTHON_RUN) openapi-spec-validator /work/$$out > /dev/null 2>&1)
endef
