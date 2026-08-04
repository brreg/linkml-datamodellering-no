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
# ==============================================================================

# ---------------------------------------------------------------------------
# run_gen_informasjonsmodell_instance — makro for å generere Informasjonsmodell
# ---------------------------------------------------------------------------
# Per-schema Informasjonsmodell-instans generator.
# $1=schemas
define run_gen_informasjonsmodell_instance
@eval "$$LOG_FUNCTIONS"; \
for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	t0=$$(date +%s%3N); \
	if run_logged "gen-informasjonsmodell-instance $$domain/$$name" $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-informasjonsmodell.py "$$schema"; then \
		elapsed_ms=$$(($$(date +%s%3N) - t0)); \
		log_info "$$(printf '$(CLR_STEP)→ gen-informasjonsmodell-instance  %s/%s$(CLR_RST) (%d.%ds)' \
			"$$domain" "$$name" \
			$$((elapsed_ms / 1000)) \
			$$((elapsed_ms % 1000 / 100)))"; \
	fi; \
done
endef

# ---------------------------------------------------------------------------
# Generering av instansdata
# ---------------------------------------------------------------------------

.PHONY: gen-informasjonsmodell-instance

gen-informasjonsmodell-instance:
ifdef SCHEMA
	$(call print_header,gen-informasjonsmodell-instance,SCHEMA=$(SCHEMA))
else ifdef DOMAIN
	$(call print_header,gen-informasjonsmodell-instance,DOMAIN=$(DOMAIN))
else
	$(call print_header,gen-informasjonsmodell-instance)
endif
	$(call run_gen_informasjonsmodell_instance,$(call get_target_schemas))

.PHONY: gen-modellkatalog-instance

gen-modellkatalog-instance:
	$(call print_step,Genererer Modellkatalog-instans)
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-modellkatalog.py

.PHONY: gen-begrepskatalog-instance

gen-begrepskatalog-instance:
	$(call print_step,Samlar begrep frå begrepssamlingar til begrepskatalogar)
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/collect-concepts.py

# ---------------------------------------------------------------------------
# Validering av instansdata
# ---------------------------------------------------------------------------

.PHONY: validate-informasjonsmodell-instance

validate-informasjonsmodell-instance:
	@if [ -z "$(SCHEMA)" ]; then \
		echo "Error: SCHEMA parameter required"; \
		echo "Usage: make validate-informasjonsmodell-instance SCHEMA=src/linkml/<domain>/<modell>/<modell>-schema.yaml"; \
		exit 1; \
	fi
	$(call print_step,Validerer Informasjonsmodell-instans for $(SCHEMA))
	@SCHEMA_DIR=$$(dirname "$(SCHEMA)"); \
	MODELLDCAT_YAML="$$SCHEMA_DIR/metadata/modelldcat.yaml"; \
	if [ ! -f "$$MODELLDCAT_YAML" ]; then \
		echo "Error: $$MODELLDCAT_YAML eksisterer ikkje"; \
		echo "Køyr først: make gen-informasjonsmodell-instance SCHEMA=$(SCHEMA)"; \
		exit 1; \
	fi; \
	echo "$(CLR_STEP)Køyrer full LinkML-validering$(CLR_RST)"; \
	$(LINKML_RUN) python3 /work/src/assets/scripts/validate-modelldcat.py \
		"$$MODELLDCAT_YAML" \
		/work/src/linkml/ap-no/modelldcat-ap-no/modelldcat-katalog-schema.yaml

.PHONY: validate-modellkatalog-instance

validate-modellkatalog-instance:
	@if [ -z "$(ORG)" ]; then \
		echo "Error: ORG parameter required"; \
		echo "Usage: make validate-modellkatalog-instance ORG=<org-slug>"; \
		echo "Eksempel: make validate-modellkatalog-instance ORG=digdir-modellkatalog"; \
		exit 1; \
	fi
	$(call print_step,Validerer Modellkatalog-instans for $(ORG))
	@ORG_SCHEMA="src/linkml/modellkatalog/$(ORG)/$(ORG)-schema.yaml"; \
	ORG_DATA="src/linkml/modellkatalog/$(ORG)/data/$(ORG)/$(ORG).yaml"; \
	if [ ! -f "$$ORG_SCHEMA" ]; then \
		echo "Error: $$ORG_SCHEMA eksisterer ikkje"; \
		exit 1; \
	fi; \
	if [ ! -f "$$ORG_DATA" ]; then \
		echo "Error: $$ORG_DATA eksisterer ikkje"; \
		echo "Køyr først: make gen-modellkatalog-instance"; \
		exit 1; \
	fi; \
	echo "$(CLR_STEP)Validerer $$ORG_DATA mot $$ORG_SCHEMA$(CLR_RST)"; \
	$(LINKML_RUN) linkml validate --schema "$$ORG_SCHEMA" "$$ORG_DATA"
