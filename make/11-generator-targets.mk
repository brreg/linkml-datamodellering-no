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
$(eval $(call make_gen_target,gen-linkml-merge,run_gen_linkml_parallel))
$(eval $(call make_gen_target,gen-jsonld-context,run_gen_parallel,jsonld-context))
$(eval $(call make_gen_target,gen-shacl,run_gen_shacl_parallel))
$(eval $(call make_gen_target,gen-python,run_gen_parallel,python))
$(eval $(call make_gen_target,gen-jsonschema,run_gen_parallel,json-schema))
$(eval $(call make_gen_target,gen-owl,run_gen_owl_parallel))
$(eval $(call make_gen_target,gen-rdf,run_gen_rdf_parallel))
$(eval $(call make_gen_target,gen-xsd,run_gen_xsd_parallel))
$(eval $(call make_gen_target,gen-asyncapi,run_gen_asyncapi_parallel))
$(eval $(call make_gen_target,gen-openapi,run_gen_openapi_parallel))
$(eval $(call make_gen_target,gen-erdiagram,run_gen_erdiagram_parallel))
$(eval $(call make_gen_target,gen-proto,run_gen_parallel,proto))
$(eval $(call make_gen_target,gen-plantuml,run_gen_plantuml_parallel))

# ---------------------------------------------------------------------------
# Hjelpetekst for gen-*-targeta over. Target/kommentar-linjer generert av
# $(eval $(call make_gen_target,...)) ovanfor finst berre i Make sin
# minnetilstand, aldri på disk, og er difor usynlege for `make help` sin
# grep av $(MAKEFILE_LIST) (same fallgruve som make/80-images.mk sin
# toppkommentar åtvarar mot for build-docker-*). Desse reint deklarative
# linjene (utan oppskrift) legg til hjelpeteksten utan å duplisere sjølve
# genererings-logikken — Make tillèt fleire reglar for same target så lenge
# berre éi av dei har ei oppskrift. Sjå specs/done/forenkle-make-laget.md.
# ---------------------------------------------------------------------------
gen-linkml-merge: ## Valider skjema (gen-linkml, fail-fast, ingen fil skriven) [SCHEMA=<sti>|DOMAIN=<domain>]
gen-jsonld-context: ## Generer JSON-LD context [SCHEMA=<sti>|DOMAIN=<domain>]
gen-shacl: ## Generer SHACL-shapes [SCHEMA=<sti>|DOMAIN=<domain>]
gen-python: ## Generer Python-klassar [SCHEMA=<sti>|DOMAIN=<domain>]
gen-jsonschema: ## Generer JSON Schema [SCHEMA=<sti>|DOMAIN=<domain>]
gen-owl: ## Generer OWL-ontologi [SCHEMA=<sti>|DOMAIN=<domain>]
gen-rdf: ## Generer RDF/Turtle-skjemaserialisering [SCHEMA=<sti>|DOMAIN=<domain>]
gen-xsd: ## Generer XSD via avrotize, krev gen-jsonschema [SCHEMA=<sti>|DOMAIN=<domain>]
gen-asyncapi: ## Generer og valider AsyncAPI-spec, krev gen-jsonschema [SCHEMA=<sti>|DOMAIN=<domain>]
gen-openapi: ## Generer og valider OpenAPI-spec, krev gen-jsonschema [SCHEMA=<sti>|DOMAIN=<domain>]
gen-erdiagram: ## Generer ER-diagram (Mermaid) [SCHEMA=<sti>|DOMAIN=<domain>]
gen-proto: ## Generer Protobuf-schema [SCHEMA=<sti>|DOMAIN=<domain>]
gen-plantuml: ## Generer PlantUML-diagram, full og filtrert [SCHEMA=<sti>|DOMAIN=<domain>]

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
	$(call run_gen_doc_parallel,$(call get_target_schemas))
	$(call run_gen_erdiagram_parallel,$(call get_target_schemas))
