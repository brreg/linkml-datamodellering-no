# ==============================================================================
# make/20-domain-targets.mk
#
# Genererer domain-<domain> targets for kvart domene funne i schema discovery.
# Støttar domenespesifikke pre-hooks via DOMAIN_PRE_<domain>.
# ==============================================================================

# Domenespesifikke pre-hooks — køyrer før standard generering
DOMAIN_PRE_begrepskatalog := gen-begrepskatalog-instance

# ---------------------------------------------------------------------------
# domain_target — generisk mal for domain-<domain> targets
# ---------------------------------------------------------------------------
# $1 = domain-namn (t.d. ap-no, begrepskatalog, oreg, ...)
#
# Genereringsrekkefølgje:
#   1. DOMAIN_PRE_$(1) — domenespesifikk førebuing (t.d. gen-begrepskatalog-instance)
#   2. gen-linkml (merge imports)
#   3. gen-jsonld-context, gen-shacl, gen-python, gen-json-schema
#   4. gen-owl, gen-rdf
#   5. linkml-convert for eksempelfiler
#   6. gen-doc, gen-erdiagram, gen-proto, gen-plantuml, gen-xsd
#   7. gen-openapi, gen-asyncapi (berre dersom flagga i manifest)
#   8. gen-informasjonsmodell-instance
#
# Escaping guide for $(eval $(call ...)):
#   $(1)          – expanded at call time (parameter substitution)
#   $$(VAR)       – becomes $(VAR) after call; expanded at build time
#   $$$$shell_var – becomes $$shell_var after call; shell receives $shell_var
# ---------------------------------------------------------------------------

define domain_target
_schemas_$(1) := $$(filter $$(SCHEMA_DIR)/$(1)/%,$$(SCHEMAS))
_domain_pre_$(1) := $$(DOMAIN_PRE_$(1))

.PHONY: domain-$(1)
domain-$(1): $$(_domain_pre_$(1))
	$$(call print_header,domain-$(1),$$(if $$(filter-out 1,$$(PARALLEL)),(PARALLEL=$$(PARALLEL))))
	$$(call run_gen_linkml_parallel,$$(_schemas_$(1)))
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-jsonld-context,context.jsonld)
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-shacl,shapes.ttl)
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-python,model.py)
	$$(call run_gen_parallel,$$(_schemas_$(1)),gen-json-schema,schema.json)
	$$(call run_gen_owl_parallel,$$(_schemas_$(1)))
	$$(call run_gen_rdf_parallel,$$(_schemas_$(1)))
	@for example in $$(find $$(SCHEMA_DIR)/$(1) -path '*/examples/*-eksempel.yaml' 2>/dev/null | sort); do \
		[ -f "$$$$example" ] || continue; \
		name=$$$$(basename "$$$$example" .yaml); \
		profil=$$$$(echo "$$$$name" | sed 's/-eksempel$$$$//'); \
		if [ -f $$(SCHEMA_DIR)/$(1)/$$$$profil/build.yaml ] && grep -q "^  example_rdf: false" $$(SCHEMA_DIR)/$(1)/$$$$profil/build.yaml; then \
			echo "Hoppar over linkml-convert for $$$$example (example_rdf: false)"; \
			continue; \
		fi; \
		mkdir -p $$(GEN_DIR)/$(1)/$$$$profil; \
		if [ -f tests/fixtures/$$$$profil-fixture.yaml ]; then \
			schema=tests/fixtures/$$$$profil-fixture.yaml; \
		else \
			schema=$$(SCHEMA_DIR)/$(1)/$$$$profil/$$$$profil-schema.yaml; \
		fi; \
		echo "$$(CLR_STEP)→ linkml-convert  $$$$example$$(CLR_RST)"; \
		echo "$$(LINKML_RUN) linkml-convert --schema $$$$schema --output-format ttl --no-validate $$$$example > $$(GEN_DIR)/$(1)/$$$$profil/$$$$name.ttl"; \
		$$(LINKML_RUN) linkml-convert \
			--schema $$$$schema \
			--output-format ttl \
			--no-validate \
			$$$$example > $$(GEN_DIR)/$(1)/$$$$profil/$$$$name.ttl; \
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
			jsonschema=$$(GEN_DIR)/$$$$domain/$$$$name/$$$$name-schema.json; \
			if [ ! -f "$$$$jsonschema" ]; then \
				echo "ÅTVARING: $$$$jsonschema finst ikkje — hoppar over gen-openapi for $$$$name" >&2; \
				continue; \
			fi; \
			out=$$(GEN_DIR)/$$$$domain/$$$$name/$$$$name-openapi.yaml; \
			mkdir -p $$(GEN_DIR)/$$$$domain/$$$$name; \
			echo "$$(CLR_STEP)→ gen-openapi  $$$$schema$$(CLR_RST)"; \
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
			jsonschema=$$(GEN_DIR)/$$$$domain/$$$$name/$$$$name-schema.json; \
			if [ ! -f "$$$$jsonschema" ]; then \
				echo "ÅTVARING: $$$$jsonschema finst ikkje — hoppar over gen-asyncapi for $$$$name" >&2; \
				continue; \
			fi; \
			out=$$(GEN_DIR)/$$$$domain/$$$$name/$$$$name-asyncapi.yaml; \
			mkdir -p $$(GEN_DIR)/$$$$domain/$$$$name; \
			echo "$$(CLR_STEP)→ gen-asyncapi  $$$$schema$$(CLR_RST)"; \
			$$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-asyncapi.py \
				/work/$$$$jsonschema /work/$$$$schema --out /work/$$$$out; \
			$$(ASYNCAPI_RUN) validate /work/$$$$out; \
		done; \
	else \
		$$(call run_gen_asyncapi_parallel,$$(_schemas_$(1))); \
	fi
	$$(call run_gen_informasjonsmodell_instance,$$(_schemas_$(1)))
endef

# Generer domain-targets for alle domene
$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))
