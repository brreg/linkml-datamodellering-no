# ==============================================================================
# make/11-generator-targets.mk
#
# Genererte gen-* target basert på make_gen_target-malen.
# ==============================================================================

# ---------------------------------------------------------------------------
# Generisk target-generator for gen-* targets
# ---------------------------------------------------------------------------
# $1=target-namn (t.d. gen-jsonschema)  $2=makro-namn (t.d. run_gen_parallel)  $3=ekstra argument til makroen
define make_gen_target
.PHONY: $(1)
$(1):
ifdef SCHEMA
	$$(call print_header,$(1),SCHEMA=$$(SCHEMA))
else ifdef DOMAIN
	$$(call print_header,$(1),DOMAIN=$$(DOMAIN))
else
	$$(call print_header,$(1))
endif
	$$(call $(2),$$(call get_target_schemas)$(if $(3),$(COMMA)$(3)))
endef

COMMA := ,

# ---------------------------------------------------------------------------
# Standard gen-* targets (genererte via make_gen_target)
# ---------------------------------------------------------------------------
$(eval $(call make_gen_target,gen-jsonld-context,run_gen,gen-jsonld-context$(COMMA)context.jsonld))
$(eval $(call make_gen_target,gen-shacl,run_gen_shacl))
$(eval $(call make_gen_target,gen-python,run_gen,gen-python$(COMMA)model.py))
$(eval $(call make_gen_target,gen-jsonschema,run_gen,gen-json-schema$(COMMA)schema.json))
$(eval $(call make_gen_target,gen-owl,run_gen_owl))
$(eval $(call make_gen_target,gen-rdf,run_gen_rdf))
$(eval $(call make_gen_target,gen-xsd,run_gen_xsd))
$(eval $(call make_gen_target,gen-asyncapi,run_gen_asyncapi))
$(eval $(call make_gen_target,gen-openapi,run_gen_openapi))
$(eval $(call make_gen_target,gen-erdiagram,run_gen_erdiagram))
$(eval $(call make_gen_target,gen-proto,run_gen,gen-proto$(COMMA)schema.proto))
$(eval $(call make_gen_target,gen-plantuml,run_gen_plantuml))

# ---------------------------------------------------------------------------
# gen-docs er spesiell (kallar to makroar)
# ---------------------------------------------------------------------------
.PHONY: gen-docs
gen-docs: ## Generer dokumentasjon (gen-doc + gen-erdiagram) [SCHEMA=<sti>|DOMAIN=<domain>]
ifdef SCHEMA
	$(call print_header,gen-docs,SCHEMA=$(SCHEMA))
else ifdef DOMAIN
	$(call print_header,gen-docs,DOMAIN=$(DOMAIN))
else
	$(call print_header,gen-docs)
endif
	$(call run_gen_doc,$(call get_target_schemas))
	$(call run_gen_erdiagram,$(call get_target_schemas))
