# ==============================================================================
# make/11-generator-targets.mk
#
# Genererte gen-* target basert på make_gen_target-malen.
# ==============================================================================

# ---------------------------------------------------------------------------
# Generisk target-generator for gen-* targets
# ---------------------------------------------------------------------------
# $1=target-navn (t.d. gen-jsonschema)  $2=makro-navn (t.d. run_gen_parallel)  $3=ekstra argument til makroen
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
$(eval $(call make_gen_target,gen-jsonld-context,run_gen_parallel,jsonld-context))
$(eval $(call make_gen_target,gen-shacl,run_gen_shacl_parallel))
$(eval $(call make_gen_target,gen-python,run_gen_parallel,python))
$(eval $(call make_gen_target,gen-jsonschema,run_gen_parallel,json-schema))
$(eval $(call make_gen_target,gen-owl,run_gen_owl_parallel))
$(eval $(call make_gen_target,gen-rdf,run_gen_rdf_parallel))
$(eval $(call make_gen_target,gen-xsd,run_gen_xsd_parallel))
$(eval $(call make_gen_target,gen-asyncapi,run_gen_asyncapi_parallel))
$(eval $(call make_gen_target,gen-openapi,run_gen_openapi_parallel))
$(eval $(call make_gen_target,gen-erdiagram-mermaid,run_gen_erdiagram_parallel))
$(eval $(call make_gen_target,gen-proto,run_gen_parallel,proto))
$(eval $(call make_gen_target,gen-graphql,run_gen_parallel,graphql))
$(eval $(call make_gen_target,gen-java,run_gen_parallel,java))
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
gen-jsonld-context: ## Generer JSON-LD context [DOMAIN=<domene>|SCHEMA=<sti>]
gen-shacl: ## Generer SHACL-shapes [DOMAIN=<domene>|SCHEMA=<sti>]
gen-python: ## Generer Python-klasser [DOMAIN=<domene>|SCHEMA=<sti>]
gen-jsonschema: ## Generer JSON Schema [DOMAIN=<domene>|SCHEMA=<sti>]
gen-owl: ## Generer OWL-ontologi [DOMAIN=<domene>|SCHEMA=<sti>]
gen-rdf: ## Generer RDF/Turtle-skjemaserialisering [DOMAIN=<domene>|SCHEMA=<sti>]
gen-xsd: ## Generer XSD via avrotize, krev gen-jsonschema [DOMAIN=<domene>|SCHEMA=<sti>]
gen-asyncapi: ## Generer og valider AsyncAPI-spec, krev gen-jsonschema [DOMAIN=<domene>|SCHEMA=<sti>]
gen-openapi: ## Generer og valider OpenAPI-spec, krev gen-jsonschema [DOMAIN=<domene>|SCHEMA=<sti>]
gen-erdiagram-mermaid: ## Generer ER-diagram (Mermaid) [DOMAIN=<domene>|SCHEMA=<sti>]
gen-proto: ## Generer Protobuf-schema [DOMAIN=<domene>|SCHEMA=<sti>]
gen-graphql: ## Generer GraphQL-skjema [DOMAIN=<domene>|SCHEMA=<sti>]
gen-java: ## Generer Java-klasser [DOMAIN=<domene>|SCHEMA=<sti>]
gen-plantuml: ## Generer PlantUML-diagram, full og filtrert [DOMAIN=<domene>|SCHEMA=<sti>]

# ---------------------------------------------------------------------------
# gen-schema-docs er spesiell (kallar to makroar)
# ---------------------------------------------------------------------------
.PHONY: gen-schema-docs
gen-schema-docs: ## Generer per-skjema dokumentasjon (gen-doc + ER-diagram) [DOMAIN=<domene>|SCHEMA=<sti>]
ifdef SCHEMA
	$(call print_header,gen-schema-docs,SCHEMA=$(SCHEMA))
else ifdef DOMAIN
	$(call print_header,gen-schema-docs,DOMAIN=$(DOMAIN))
else
	$(call print_header,gen-schema-docs)
endif
	$(call run_gen_doc_parallel,$(call get_target_schemas))
	$(call run_gen_erdiagram_parallel,$(call get_target_schemas))
