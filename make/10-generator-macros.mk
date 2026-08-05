# ==============================================================================
# make/10-generator-macros.mk
#
# Generiske generator-makroar for å byggje LinkML-artefaktar.
# ==============================================================================

# ---------------------------------------------------------------------------
# Serial generator-makro — brukt av dei frittståande gen-*-targeta i
# make/11-generator-targets.mk (t.d. make gen-jsonld-context SCHEMA=...),
# ikkje som PARALLEL=1-fallback (den mekanismen er fjerna, sjå
# src/assets/scripts/makefile/run-parallel-gen.sh)
# ---------------------------------------------------------------------------
# $1=schemas  $2=generator  $3=output-file suffix
define run_gen
@$(foreach s,$(1), \
	eval "$$LOG_FUNCTIONS"; \
	log_info "$(CLR_STEP)→ $(2)  $(s)$(CLR_RST)"; \
	log_debug "Kommando: $(LINKML_RUN) $(2) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-$(3)"; \
	mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) $(2) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-$(3);)
endef

# Parallell versjon av run_gen med timer — gata mot build.yaml sitt
# generators:-flagg (same mønster som run_gen_plantuml_parallel)
# $1=schemas  $2=generator  $3=output-file suffix  $4=build.yaml generator-flagg
define run_gen_parallel
@GEN_CMD='mkdir -p "$$outdir" && $(LINKML_RUN) $(2) "$$s" > "$$outdir/$$name-$(3)"' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator $(2) $(if $(4),--flag $(4)) -- $(1)
endef

# ---------------------------------------------------------------------------
# LinkML merge-imports (gen-linkml)
# ---------------------------------------------------------------------------
# Ingen frittståande gen-linkml-target finst (merge-imports er berre eit
# steg i domain_target-pipelinen), difor finst det heller ingen serial
# variant å halde ved like — berre denne.
define run_gen_linkml_parallel
@GEN_CMD='$(LINKML_RUN) gen-linkml "$$s" > /dev/null' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator merge-imports -- $(1)
endef

# ---------------------------------------------------------------------------
# SHACL-generering med per-schema flagg-override
# ---------------------------------------------------------------------------
SHACL_DEFAULT_FLAGS :=
define run_gen_shacl
@$(foreach s,$(1), \
	eval "$$LOG_FUNCTIONS"; \
	log_info "$(CLR_STEP)→ gen-shacl  $(s)$(CLR_RST)"; \
	log_debug "Kommando: $(LINKML_RUN) gen-shacl $(if $(SHACL_FLAGS_$(call schema_key,$(s))),$(SHACL_FLAGS_$(call schema_key,$(s))),$(SHACL_DEFAULT_FLAGS)) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-shapes.ttl"; \
	mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-shacl $(if $(SHACL_FLAGS_$(call schema_key,$(s))),$(SHACL_FLAGS_$(call schema_key,$(s))),$(SHACL_DEFAULT_FLAGS)) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-shapes.ttl;)
endef

# ---------------------------------------------------------------------------
# OWL-generering med per-schema flagg-override
# ---------------------------------------------------------------------------
OWL_DEFAULT_FLAGS := --skip-vacuous-local-range-axioms --skip-vacuous-min-zero-cardinality-axioms --consolidate-cardinality-axioms
define run_gen_owl
@$(foreach s,$(1), \
	eval "$$LOG_FUNCTIONS"; \
	log_info "$(CLR_STEP)→ gen-owl  $(s)$(CLR_RST)"; \
	log_debug "Kommando: $(LINKML_RUN) gen-owl $(if $(OWL_FLAGS_$(call schema_key,$(s))),$(OWL_FLAGS_$(call schema_key,$(s))),$(OWL_DEFAULT_FLAGS)) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-ontology.ttl"; \
	mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-owl $(if $(OWL_FLAGS_$(call schema_key,$(s))),$(OWL_FLAGS_$(call schema_key,$(s))),$(OWL_DEFAULT_FLAGS)) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-ontology.ttl;)
endef

# Parallell versjon av gen-owl — gata mot build.yaml (owl: true)
# Merk: brukar OWL_DEFAULT_FLAGS i parallell-modus (config.mk overrides vert ikkje propagerte til xargs)
define run_gen_owl_parallel
@GEN_CMD='mkdir -p "$$outdir" && $(LINKML_RUN) gen-owl $(OWL_DEFAULT_FLAGS) "$$s" > "$$outdir/$$name-ontology.ttl"' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-owl --flag owl -- $(1)
endef

# ---------------------------------------------------------------------------
# RDF-generering med per-schema skip-flagg
# ---------------------------------------------------------------------------
define run_gen_rdf
@$(foreach s,$(1), \
	eval "$$LOG_FUNCTIONS"; \
	$(if $(filter true,$(GEN_RDF_SKIP_$(call schema_key,$(s)))), \
		log_info "Hoppar over gen-rdf for $(call schema_name,$(s)) (GEN_RDF_SKIP_$(call schema_key,$(s)) er sett)";, \
		log_info "$(CLR_STEP)→ gen-rdf  $(s)$(CLR_RST)"; \
		log_debug "Kommando: $(LINKML_RUN) gen-rdf $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-schema.ttl"; \
		mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-rdf $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-schema.ttl;))
endef

# Parallell versjon av gen-rdf — gata mot build.yaml (rdf: true)
define run_gen_rdf_parallel
@GEN_CMD='mkdir -p "$$outdir" && $(LINKML_RUN) gen-rdf "$$s" > "$$outdir/$$name-schema.ttl"' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-rdf --flag rdf -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-doc (genererer dokumentasjon til katalog i staden for stdout)
# ---------------------------------------------------------------------------
define run_gen_doc
@$(foreach s,$(1), \
  eval "$$LOG_FUNCTIONS"; \
  log_info "$(CLR_STEP)→ gen-docgen-examples  $(s)$(CLR_RST)"; \
  log_debug "Kommando: python3 src/assets/scripts/makefile/gen-docgen-examples.py $(s) ..."; \
  mkdir -p $(call schema_outdir,$(s))/docgen-examples && \
  $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-docgen-examples.py \
    $(s) \
    src/linkml/$(call schema_domain,$(s))/$(call schema_name,$(s))/examples/$(call schema_name,$(s))-eksempel.yaml \
    $(call schema_outdir,$(s))/docgen-examples && \
  log_info "$(CLR_STEP)→ gen-doc  $(s)$(CLR_RST)"; \
  log_debug "Kommando: $(LINKML_RUN) gen-doc --template-directory src/assets/templates/docgen ... -d $(call schema_outdir,$(s))/docs $(s)"; \
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

# Parallell versjon av gen-doc — gata mot build.yaml (docs: true)
define run_gen_doc_parallel
@GEN_CMD='mkdir -p "$$outdir/docgen-examples" "$$outdir/docs" && \
run_logged "gen-docgen-examples $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-docgen-examples.py \
	"$$s" \
	"src/linkml/$$domain/$$name/examples/$$name-eksempel.yaml" \
	"$$outdir/docgen-examples" && \
run_logged "gen-doc $$domain/$$name" $(LINKML_RUN) gen-doc \
	--template-directory src/assets/templates/docgen \
	--no-mergeimports \
	--no-render-imports \
	--no-hierarchical-class-view \
	--diagram-type mermaid_class_diagram \
	--example-directory "$$outdir/docgen-examples" \
	-d "$$outdir/docs" "$$s" && \
sed -i "/Container/d" "$$outdir/docs/index.md"' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator "gen-docgen-examples + gen-doc" --flag docs -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-erdiagram (pipar gjennom awk for å stripa Container-klassar)
# ---------------------------------------------------------------------------
define run_gen_erdiagram
@$(foreach s,$(1), \
  eval "$$LOG_FUNCTIONS"; \
  log_info "$(CLR_STEP)→ gen-erdiagram  $(s)$(CLR_RST)"; \
  log_debug "Kommando: $(LINKML_RUN) gen-erdiagram --no-mergeimports $(s) | awk -f src/assets/scripts/makefile/filter_container.awk > ..."; \
  mkdir -p $(call schema_outdir,$(s)) && $(LINKML_RUN) gen-erdiagram --no-mergeimports $(s) \
  | awk -f src/assets/scripts/makefile/filter_container.awk \
  > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md && \
  log_debug "Kommando: python -u src/assets/scripts/makefile/filter_erdiagram.py $(s) ..."; \
  $(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_erdiagram.py $(s) $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram-unfiltered.md > $(call schema_outdir,$(s))/$(call schema_name,$(s))-erdiagram.md; \
  )
endef

# Parallell versjon av gen-erdiagram — gata mot build.yaml (erdiagram: true)
define run_gen_erdiagram_parallel
@GEN_CMD='mkdir -p "$$outdir" && \
$(LINKML_RUN) gen-erdiagram --no-mergeimports "$$s" \
	| awk -f src/assets/scripts/makefile/filter_container.awk \
	> "$$outdir/$$name-erdiagram-unfiltered.md" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_erdiagram.py \
	"$$s" \
	"$$outdir/$$name-erdiagram-unfiltered.md" \
	> "$$outdir/$$name-erdiagram.md"' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-erdiagram --flag erdiagram -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-plantuml (genererer PlantUML-diagram med filtrering)
# ---------------------------------------------------------------------------
define run_gen_plantuml
@$(foreach s,$(1), \
  eval "$$LOG_FUNCTIONS"; \
  log_info "$(CLR_STEP)→ gen-plantuml  $(s)$(CLR_RST)"; \
  log_debug "Kommando: $(LINKML_RUN) gen-plantuml $(s) > diagrams/$(call schema_name,$(s))-raw.puml"; \
  mkdir -p $(call schema_outdir,$(s))/diagrams && \
  $(LINKML_RUN) gen-plantuml $(s) \
    > $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-raw.puml && \
  log_info "$(CLR_STEP)→ filter-plantuml (filtered)  $(s)$(CLR_RST)"; \
  $(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py $(s) $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-raw.puml filtered \
    > $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-filtered.puml && \
  log_info "$(CLR_STEP)→ filter-plantuml (full)  $(s)$(CLR_RST)"; \
  $(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py $(s) $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s))-raw.puml full \
    > $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s)).puml && \
  log_debug "Kommando: podman run plantuml -tsvg ..."; \
  podman run --rm \
    -v "$(CURDIR)/$(call schema_outdir,$(s))/diagrams:/data" \
    $(PLANTUML_IMAGE) -tsvg /data/$(call schema_name,$(s)).puml && \
  podman run --rm \
    -v "$(CURDIR)/$(call schema_outdir,$(s))/diagrams:/data" \
    $(PLANTUML_IMAGE) -tsvg /data/$(call schema_name,$(s))-filtered.puml; \
)
endef

# Parallell versjon av gen-plantuml — hoppar over skjema utan `plantuml: true` i
# build.yaml, sidan images.json sitt required_if_generator_flag: "plantuml"
# føreset at biletet faktisk ikkje vert bruka for slike skjema
define run_gen_plantuml_parallel
@GEN_CMD='mkdir -p "$$outdir/diagrams" && \
$(LINKML_RUN) gen-plantuml "$$s" > "$$outdir/diagrams/$$name-raw.puml" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py \
	"$$s" "$$outdir/diagrams/$$name-raw.puml" filtered \
	> "$$outdir/diagrams/$$name-filtered.puml" && \
$(PYTHON_RUN) python -u src/assets/scripts/makefile/filter_plantuml.py \
	"$$s" "$$outdir/diagrams/$$name-raw.puml" full \
	> "$$outdir/diagrams/$$name.puml" && \
podman run --rm -v "$(CURDIR)/$$outdir/diagrams:/data" $(PLANTUML_IMAGE) -tsvg /data/$$name.puml > /dev/null && \
podman run --rm -v "$(CURDIR)/$$outdir/diagrams:/data" $(PLANTUML_IMAGE) -tsvg /data/$$name-filtered.puml > /dev/null' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-plantuml --flag plantuml -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-xsd (JSON Schema → Avro → XSD via avrotize)
# ---------------------------------------------------------------------------
define run_gen_xsd
@eval "$$LOG_FUNCTIONS"; \
has_error=0; \
for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	manifest=$$(dirname "$$schema")/build.yaml; \
	if [ ! -f "$$manifest" ] || ! grep -q "^  xsd: true" "$$manifest"; then \
		continue; \
	fi; \
	jsonschema=$(GEN_DIR)/$$domain/$$name/$$name-schema.json; \
	if [ ! -f "$$jsonschema" ]; then \
		log_info "$(CLR_WARN)ÅTVARING: $$jsonschema finst ikkje — hoppar over gen-xsd for $$name$(CLR_RST)"; \
		continue; \
	fi; \
	avsc=$(GEN_DIR)/$$domain/$$name/$$name.avsc; \
	xsd=$(GEN_DIR)/$$domain/$$name/$$name-schema.xsd; \
	namespace=$$(grep '^id:' "$$schema" | head -1 | awk '{print $$2}'); \
	mkdir -p $(GEN_DIR)/$$domain/$$name; \
	log_debug "[$$domain/$$name] Startar gen-xsd: $$schema → $$xsd"; \
	t0=$$(date +%s%3N); \
	if run_logged "gen-xsd/j2a $$domain/$$name" $(AVROTIZE_RUN) j2a /work/$$jsonschema --out /work/$$avsc \
		&& run_logged "gen-xsd/a2x $$domain/$$name" $(AVROTIZE_RUN) a2x /work/$$avsc --namespace "$$namespace" --out /work/$$xsd \
		&& run_logged "gen-xsd/fix-xsd-dates $$domain/$$name" podman run --rm --entrypoint python3 -v "$(CURDIR):/work" $(AVROTIZE_IMAGE) /work/src/assets/scripts/makefile/fix-xsd-dates.py /work/$$xsd /work/$$jsonschema; \
	then \
		elapsed_ms=$$(($$( date +%s%3N) - t0)); \
		log_info "$$(printf '$(CLR_STEP)→ gen-xsd  %s/%s$(CLR_RST) (%d.%ds)' \
			"$$domain" "$$name" \
			$$((elapsed_ms / 1000)) \
			$$((elapsed_ms % 1000 / 100)))"; \
	else \
		has_error=1; \
	fi; \
	rm -f "$$avsc"; \
done; \
[ "$$has_error" -eq 0 ]
endef

# ---------------------------------------------------------------------------
# gen-asyncapi (JSON Schema → AsyncAPI YAML → validate)
# ---------------------------------------------------------------------------
define run_gen_asyncapi
@eval "$$LOG_FUNCTIONS"; \
for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	manifest=$$(dirname "$$schema")/build.yaml; \
	if [ ! -f "$$manifest" ] || ! grep -q "^  asyncapi: true" "$$manifest"; then \
		continue; \
	fi; \
	jsonschema=$(GEN_DIR)/$$domain/$$name/$$name-schema.json; \
	if [ ! -f "$$jsonschema" ]; then \
		log_info "$(CLR_WARN)ÅTVARING: $$jsonschema finst ikkje — hoppar over gen-asyncapi for $$name$(CLR_RST)"; \
		continue; \
	fi; \
	out=$(GEN_DIR)/$$domain/$$name/$$name-asyncapi.yaml; \
	mkdir -p $(GEN_DIR)/$$domain/$$name; \
	log_info "$(CLR_STEP)→ gen-asyncapi  $$schema$(CLR_RST)"; \
	log_debug "[$$domain/$$name] Kommando: gen-asyncapi.py /work/$$jsonschema → /work/$$out"; \
	t0=$$(date +%s%3N); \
	$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py \
		/work/$$jsonschema /work/$$schema --out /work/$$out; \
	$(ASYNCAPI_RUN) \
		validate /work/$$out; \
	elapsed_ms=$$(($$( date +%s%3N) - t0)); \
	log_info "$$(printf '  Ferdig (%d.%ds)' \
		$$((elapsed_ms / 1000)) \
		$$((elapsed_ms % 1000 / 100)))"; \
done
endef

# Parallell versjon av gen-asyncapi
define run_gen_asyncapi_parallel
@GEN_CMD='run_logged "gen-asyncapi $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py /work/$$input /work/$$s --out /work/$$out && run_logged "asyncapi-validate $$domain/$$name" $(ASYNCAPI_RUN) validate /work/$$out' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-asyncapi --flag asyncapi --check-suffix schema.json --out-suffix asyncapi.yaml -- $(1)
endef

# ---------------------------------------------------------------------------
# gen-openapi (JSON Schema → OpenAPI YAML → validate)
# ---------------------------------------------------------------------------
define run_gen_openapi
@eval "$$LOG_FUNCTIONS"; \
for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	manifest=$$(dirname "$$schema")/build.yaml; \
	if [ ! -f "$$manifest" ] || ! grep -q "^  openapi: true" "$$manifest"; then \
		continue; \
	fi; \
	jsonschema=$(GEN_DIR)/$$domain/$$name/$$name-schema.json; \
	if [ ! -f "$$jsonschema" ]; then \
		log_info "$(CLR_WARN)ÅTVARING: $$jsonschema finst ikkje — hoppar over gen-openapi for $$name$(CLR_RST)"; \
		continue; \
	fi; \
	out=$(GEN_DIR)/$$domain/$$name/$$name-openapi.yaml; \
	mkdir -p $(GEN_DIR)/$$domain/$$name; \
	log_info "$(CLR_STEP)→ gen-openapi  $$schema$(CLR_RST)"; \
	log_debug "[$$domain/$$name] Kommando: gen-openapi.py /work/$$jsonschema → /work/$$out"; \
	t0=$$(date +%s%3N); \
	$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py \
		/work/$$jsonschema /work/$$schema --out /work/$$out; \
	$(PYTHON_RUN) openapi-spec-validator /work/$$out; \
	elapsed_ms=$$(($$( date +%s%3N) - t0)); \
	log_info "$$(printf '  Ferdig (%d.%ds)' \
		$$((elapsed_ms / 1000)) \
		$$((elapsed_ms % 1000 / 100)))"; \
done
endef

# Parallell versjon av gen-openapi
define run_gen_openapi_parallel
@GEN_CMD='run_logged "gen-openapi $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py /work/$$input /work/$$s --out /work/$$out && run_logged "openapi-spec-validator $$domain/$$name" $(PYTHON_RUN) openapi-spec-validator /work/$$out' \
	src/assets/scripts/makefile/run-parallel-gen.sh --generator gen-openapi --flag openapi --check-suffix schema.json --out-suffix openapi.yaml -- $(1)
endef
