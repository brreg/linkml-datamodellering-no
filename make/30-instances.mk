# ==============================================================================
# make/30-instances.mk
#
# Target for generering og validering av instansdata:
# - Informasjonsmodell-instansar (ModelDCAT-AP-NO metadata)
# - Modellkatalog-instansar (aggregering av alle Informasjonsmodellar)
# - Begrepskatalog-instansar (aggregering av begrepssamlingar)
#
# Relaterte script:
# - src/assets/scripts/makefile/generate-informasjonsmodell.py
# - src/assets/scripts/makefile/generate-modellkatalog.py
# - src/assets/scripts/makefile/collect-concepts.py
# - src/assets/scripts/makefile/validate-modelldcat.py
# ==============================================================================

# ---------------------------------------------------------------------------
# run_gen_informasjonsmodell_instance_parallel — batchar Informasjonsmodell-
# generering for ALLE skjema til ÉIN kontainar (reint Python, ingen
# linkml-import) — sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md (Tiltak 3).
# Ingen build.yaml-generatorflagg gatar dette steget i dag. Brukt av både
# domain_target (make/20-domain-targets.mk) og det frittståande
# gen-informasjonsmodell-instance-targetet under.
# ---------------------------------------------------------------------------
define run_gen_informasjonsmodell_instance_parallel
@$(PYTHON_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator informasjonsmodell -- $(1)
endef

# ---------------------------------------------------------------------------
# Generering av instansdata
# ---------------------------------------------------------------------------

.PHONY: gen-informasjonsmodell-instance

gen-informasjonsmodell-instance: ## Generer ModelDCAT-metadata for skjema [SCHEMA=<sti>|DOMAIN=<domain>]
ifdef SCHEMA
	$(call print_header,gen-informasjonsmodell-instance,SCHEMA=$(SCHEMA))
else ifdef DOMAIN
	$(call print_header,gen-informasjonsmodell-instance,DOMAIN=$(DOMAIN))
else
	$(call print_header,gen-informasjonsmodell-instance)
endif
	$(call run_gen_informasjonsmodell_instance_parallel,$(call get_target_schemas))

.PHONY: gen-modellkatalog-instance

gen-modellkatalog-instance: ## Generer per-org modellkatalogar frå alle Informasjonsmodell-instansar
	$(call print_step,Genererer Modellkatalog-instans)
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-modellkatalog.py

.PHONY: gen-begrepskatalog-instance

gen-begrepskatalog-instance: ## Samle begrep frå begrepssamlingar til begrepskatalogar per organisasjon
	$(call print_step,Samlar begrep frå begrepssamlingar til begrepskatalogar)
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/collect-concepts.py

# ---------------------------------------------------------------------------
# Validering av instansdata
# ---------------------------------------------------------------------------

.PHONY: validate-informasjonsmodell-instance

validate-informasjonsmodell-instance: ## Valider generert ModelDCAT-metadata mot modelldcat-katalog-schema (SCHEMA=<sti>)
	@eval "$$LOG_FUNCTIONS"; \
	if [ -z "$(SCHEMA)" ]; then \
		log_error "SCHEMA parameter required. Bruk: make validate-informasjonsmodell-instance SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml"; \
		exit 1; \
	fi
	$(call print_step,Validerer Informasjonsmodell-instans for $(SCHEMA))
	@eval "$$LOG_FUNCTIONS"; \
	SCHEMA_DIR=$$(dirname "$(SCHEMA)"); \
	MODELL_NAME=$$(basename "$(SCHEMA)" -schema.yaml); \
	MODELLDCAT_YAML="$$SCHEMA_DIR/metadata/$$MODELL_NAME-manifest.yaml"; \
	if [ ! -f "$$MODELLDCAT_YAML" ]; then \
		log_error "$$MODELLDCAT_YAML eksisterer ikkje. Køyr først: make gen-informasjonsmodell-instance SCHEMA=$(SCHEMA)"; \
		exit 1; \
	fi; \
	log_info "$(CLR_STEP)Køyrer full LinkML-validering$(CLR_RST)"; \
	$(LINKML_RUN) python3 /work/src/assets/scripts/makefile/validate-modelldcat.py \
		"$$MODELLDCAT_YAML" \
		/work/src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml

.PHONY: validate-modellkatalog-instance

validate-modellkatalog-instance: ## Valider generert modellkatalog-datafil mot org-skjema (ORG=<org-slug>)
	@eval "$$LOG_FUNCTIONS"; \
	if [ -z "$(ORG)" ]; then \
		log_error "ORG parameter required. Bruk: make validate-modellkatalog-instance ORG=<org-slug> (eksempel: ORG=digdir-modellkatalog)"; \
		exit 1; \
	fi
	$(call print_step,Validerer Modellkatalog-instans for $(ORG))
	@eval "$$LOG_FUNCTIONS"; \
	ORG_SCHEMA="src/linkml/modellkatalog/$(ORG)/$(ORG)-schema.yaml"; \
	ORG_DATA="src/linkml/modellkatalog/$(ORG)/data/$(ORG)/$(ORG).yaml"; \
	if [ ! -f "$$ORG_SCHEMA" ]; then \
		log_error "$$ORG_SCHEMA eksisterer ikkje"; \
		exit 1; \
	fi; \
	if [ ! -f "$$ORG_DATA" ]; then \
		log_error "$$ORG_DATA eksisterer ikkje. Køyr først: make gen-modellkatalog-instance"; \
		exit 1; \
	fi; \
	log_info "$(CLR_STEP)Validerer $$ORG_DATA mot $$ORG_SCHEMA$(CLR_RST)"; \
	$(LINKML_RUN) linkml validate --schema "$$ORG_SCHEMA" "$$ORG_DATA"
