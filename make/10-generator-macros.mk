# ==============================================================================
# make/10-generator-macros.mk
#
# Generiske generator-makroar for å byggje LinkML-artefaktar.
# ==============================================================================

# ---------------------------------------------------------------------------
# Generisk parallell generator-makro med timer
# ---------------------------------------------------------------------------
# $1=schemas  $2=generator-namn (for logging)  $3=parallel-kommando
#
# Køyrer alltid via xargs -P $(PARALLEL) — også når PARALLEL=1 (då køyrer
# xargs éin job om gongen, funksjonelt identisk med ein serialisert løkke).
# Hadde tidlegare ei eiga "PARALLEL=1 → køyr serial-fallback-makro direkte"-
# grein, men den var reelt øydelagd: serial-makroane sin eigen leiande "@"
# hamna midt i ei bash-linje når han vart substituert inn i denne makroen
# sitt if/else, og feila med "bash: @: command not found" for kvart einaste
# steg. Stadfesta empirisk (før/etter, med make -n og reelle domain-byggjer)
# at xargs -P 1 gir identisk, korrekt output — sjå specs/done/dry-opprydding.md.
define run_parallel_with_timer
@printf '%s\n' $(1) | xargs -P $(PARALLEL) -I {} bash -c ' \
		set -euo pipefail; \
		eval "$$LOG_FUNCTIONS"; \
		s="{}"; \
		name=$$(basename "$$s" -schema.yaml | sed "s/-schema$$//"); \
		domain=$$(echo "$$s" | cut -d/ -f3); \
		trap "log_error \"::error file=$$s::$(2) feila for $$domain/$$name (linje \$$LINENO) — kommando: \$$BASH_COMMAND\"; exit 1" ERR; \
		outdir=$(GEN_DIR)/$$domain/$$name; \
		log_debug "[$$domain/$$name] Startar $(2): $$s"; \
		t0=$$(date +%s%3N); \
		$(3); \
		rc=$$?; \
		t1=$$(date +%s%3N); \
		elapsed_ms=$$((t1 - t0)); \
		log_info "$$(printf "$(CLR_STEP)→ $(2)  %s/%s$(CLR_RST) (%d.%ds)" \
			"$$domain" "$$name" \
			$$((elapsed_ms / 1000)) \
			$$((elapsed_ms % 1000 / 100)))"; \
		exit $$rc'
endef

# ---------------------------------------------------------------------------
# Generisk parallell generator-makro med pre-check (for OpenAPI/AsyncAPI)
# ---------------------------------------------------------------------------
# $1=schemas  $2=generator-namn  $3=manifest-flagg (t.d. "openapi")  $4=input-suffix (t.d. "schema.json")  $5=output-suffix  $6=kommandoar
define run_gen_with_check_parallel
printf '%s\n' $(1) | xargs -P $(PARALLEL) -I {} bash -c ' \
	set -euo pipefail; \
	eval "$$LOG_FUNCTIONS"; \
	s="{}"; \
	name=$$(basename "$$s" -schema.yaml | sed "s/-schema$$//"); \
	domain=$$(echo "$$s" | cut -d/ -f3); \
	trap "log_error \"::error file=$$s::$(2) feila for $$domain/$$name (linje \$$LINENO) — kommando: \$$BASH_COMMAND\"; exit 1" ERR; \
	manifest=$$(dirname "$$s")/build.yaml; \
	if [ ! -f "$$manifest" ] || ! grep -q "^  $(3): true" "$$manifest"; then \
		log_debug "[$$domain/$$name] Hoppar over $(2) ($(3) ikkje aktivert i build.yaml)"; \
		exit 0; \
	fi; \
	outdir=$(GEN_DIR)/$$domain/$$name; \
	input="$$outdir/$$name-$(4)"; \
	if [ ! -f "$$input" ]; then \
		log_error "ÅTVARING: $$input finst ikkje — hoppar over $(2) for $$name"; \
		exit 0; \
	fi; \
	out="$$outdir/$$name-$(5)"; \
	log_debug "[$$domain/$$name] Startar $(2): $$input → $$out"; \
	t0=$$(date +%s%3N); \
	mkdir -p "$$outdir"; \
	$(6); \
	rc=$$?; \
	elapsed_ms=$$(($$( date +%s%3N) - t0)); \
	log_info "$$(printf "$(CLR_STEP)→ $(2)  %s/%s$(CLR_RST) (%d.%ds)" \
		"$$domain" "$$name" \
		$$((elapsed_ms / 1000)) \
		$$((elapsed_ms % 1000 / 100)))"; \
	exit $$rc'
endef

# ---------------------------------------------------------------------------
# Serial generator-makro — brukt av dei frittståande gen-*-targeta i
# make/11-generator-targets.mk (t.d. make gen-jsonld-context SCHEMA=...),
# ikkje som PARALLEL=1-fallback (den mekanismen er fjerna, sjå
# run_parallel_with_timer over)
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
$(call run_parallel_with_timer,$(1),$(2),\
if [ ! -f "$$(dirname "$$s")/build.yaml" ] || ! grep -q "^  $(4): true" "$$(dirname "$$s")/build.yaml"; then \
	log_debug "[$$domain/$$name] Hoppar over $(2) ($(4): true ikkje sett i build.yaml)"; \
	exit 0; \
fi; \
mkdir -p "$$outdir" && $(LINKML_RUN) $(2) "$$s" > "$$outdir/$$name-$(3)")
endef

# ---------------------------------------------------------------------------
# LinkML merge-imports (gen-linkml)
# ---------------------------------------------------------------------------
# Ingen frittståande gen-linkml-target finst (merge-imports er berre eit
# steg i domain_target-pipelinen), difor finst det heller ingen serial
# variant å halde ved like — berre denne, brukt via run_parallel_with_timer.
define run_gen_linkml_parallel
$(call run_parallel_with_timer,$(1),merge-imports,$(LINKML_RUN) gen-linkml "$$s" > /dev/null)
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
$(call run_parallel_with_timer,$(1),gen-owl,\
if [ ! -f "$$(dirname "$$s")/build.yaml" ] || ! grep -q "^  owl: true" "$$(dirname "$$s")/build.yaml"; then \
	log_debug "[$$domain/$$name] Hoppar over gen-owl (owl: true ikkje sett i build.yaml)"; \
	exit 0; \
fi; \
mkdir -p "$$outdir" && $(LINKML_RUN) gen-owl $(OWL_DEFAULT_FLAGS) "$$s" > "$$outdir/$$name-ontology.ttl")
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
$(call run_parallel_with_timer,$(1),gen-rdf,\
if [ ! -f "$$(dirname "$$s")/build.yaml" ] || ! grep -q "^  rdf: true" "$$(dirname "$$s")/build.yaml"; then \
	log_debug "[$$domain/$$name] Hoppar over gen-rdf (rdf: true ikkje sett i build.yaml)"; \
	exit 0; \
fi; \
mkdir -p "$$outdir" && $(LINKML_RUN) gen-rdf "$$s" > "$$outdir/$$name-schema.ttl")
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
$(call run_parallel_with_timer,$(1),gen-docgen-examples + gen-doc,\
if [ ! -f "$$(dirname "$$s")/build.yaml" ] || ! grep -q "^  docs: true" "$$(dirname "$$s")/build.yaml"; then \
	log_debug "[$$domain/$$name] Hoppar over gen-doc (docs: true ikkje sett i build.yaml)"; \
	exit 0; \
fi; \
mkdir -p "$$outdir/docgen-examples" "$$outdir/docs" && \
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
sed -i "/Container/d" "$$outdir/docs/index.md")
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
$(call run_parallel_with_timer,$(1),gen-erdiagram,\
if [ ! -f "$$(dirname "$$s")/build.yaml" ] || ! grep -q "^  erdiagram: true" "$$(dirname "$$s")/build.yaml"; then \
	log_debug "[$$domain/$$name] Hoppar over gen-erdiagram (erdiagram: true ikkje sett i build.yaml)"; \
	exit 0; \
fi; \
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
# build.yaml (same mønster som run_gen_with_check_parallel for openapi/asyncapi),
# sidan images.json sitt required_if_generator_flag: "plantuml" føreset at biletet
# faktisk ikkje vert bruka for slike skjema
define run_gen_plantuml_parallel
$(call run_parallel_with_timer,$(1),gen-plantuml,\
if [ ! -f "$$(dirname "$$s")/build.yaml" ] || ! grep -q "^  plantuml: true" "$$(dirname "$$s")/build.yaml"; then \
	log_debug "[$$domain/$$name] Hoppar over gen-plantuml (plantuml: true ikkje sett i build.yaml)"; \
	exit 0; \
fi; \
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
$(call run_gen_with_check_parallel,$(1),gen-asyncapi,asyncapi,schema.json,asyncapi.yaml,run_logged "gen-asyncapi $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py /work/$$input /work/$$s --out /work/$$out && run_logged "asyncapi-validate $$domain/$$name" $(ASYNCAPI_RUN) validate /work/$$out)
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
$(call run_gen_with_check_parallel,$(1),gen-openapi,openapi,schema.json,openapi.yaml,run_logged "gen-openapi $$domain/$$name" $(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-openapi.py /work/$$input /work/$$s --out /work/$$out && run_logged "openapi-spec-validator $$domain/$$name" $(PYTHON_RUN) openapi-spec-validator /work/$$out)
endef
