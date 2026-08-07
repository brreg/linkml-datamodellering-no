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
	$$(call run_gen_parallel,$$(_schemas_$(1)),jsonld-context)
	$$(call run_gen_shacl_parallel,$$(_schemas_$(1)))
	$$(call run_gen_parallel,$$(_schemas_$(1)),python)
	$$(call run_gen_parallel,$$(_schemas_$(1)),json-schema)
	$$(call run_gen_owl_parallel,$$(_schemas_$(1)))
	$$(call run_gen_rdf_parallel,$$(_schemas_$(1)))
	@JOBS_TSV=$$$$(mktemp "$$(GEN_DIR)/.convert-jobs.XXXXXX") && \
	SCHEMA_DIR=$$(SCHEMA_DIR) GEN_DIR=$$(GEN_DIR) bash src/assets/scripts/makefile/convert-examples.sh $(1) > "$$$$JOBS_TSV" && \
	if [ -s "$$$$JOBS_TSV" ]; then \
		$$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator convert --jobs-tsv "$$$$JOBS_TSV"; rc=$$$$?; \
	else \
		rc=0; \
	fi; \
	rm -f "$$$$JOBS_TSV"; exit $$$$rc
	$$(call run_gen_doc_parallel,$$(_schemas_$(1)))
	$$(call run_gen_erdiagram_parallel,$$(_schemas_$(1)))
	$$(call run_gen_parallel,$$(_schemas_$(1)),proto)
	$$(call run_gen_plantuml_parallel,$$(_schemas_$(1)))
	$$(call run_gen_xsd_parallel,$$(_schemas_$(1)))
	$$(call run_gen_openapi_parallel,$$(_schemas_$(1)))
	$$(call run_gen_asyncapi_parallel,$$(_schemas_$(1)))
	$$(call run_gen_informasjonsmodell_instance_parallel,$$(_schemas_$(1)))
endef

# Generer domain-targets for alle domene
$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))
