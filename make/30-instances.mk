# ==============================================================================
# make/30-instances.mk
#
# Target for generering og validering av instansdata:
# - Informasjonsmodell-instansar (ModelDCAT-AP-NO metadata)
# - Modellkatalog-instansar (aggregering av alle Informasjonsmodellar)
# - Begrepskatalog-instansar (aggregering av begrepssamlingar)
# ==============================================================================

# ---------------------------------------------------------------------------
# run_gen_informasjonsmodell_instance — makro for å generere Informasjonsmodell
# ---------------------------------------------------------------------------
# Per-schema Informasjonsmodell-instans generator.
# $1=schemas
define run_gen_informasjonsmodell_instance
@for schema in $(1); do \
	domain=$$(echo "$$schema" | awk -F/ '{print $$3}'); \
	name=$$(echo "$$schema" | awk -F/ '{print $$4}'); \
	t0=$$(date +%s%3N); \
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-informasjonsmodell.py "$$schema" >/dev/null 2>&1; \
	rc=$$?; \
	elapsed_ms=$$(($$(date +%s%3N) - t0)); \
	printf "$(CLR_STEP)→ gen-informasjonsmodell-instance  %s/%s$(CLR_RST) (%d.%ds)\n" \
		"$$domain" "$$name" \
		$$((elapsed_ms / 1000)) \
		$$((elapsed_ms % 1000 / 100)); \
	if [ $$rc -ne 0 ]; then \
		echo "Warning: Failed to generate Informasjonsmodell for $$schema"; \
	fi; \
done
endef

# ---------------------------------------------------------------------------
# Generering av instansdata
# ---------------------------------------------------------------------------

.PHONY: gen-informasjonsmodell-instance

gen-informasjonsmodell-instance:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-informasjonsmodell-instance SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-informasjonsmodell-instance DOMAIN=$(DOMAIN)$(CLR_RST)"
else
	@echo "$(CLR_HDR)*** make gen-informasjonsmodell-instance$(CLR_RST)"
endif
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_informasjonsmodell_instance,$(call get_target_schemas))

.PHONY: gen-modellkatalog-instance

gen-modellkatalog-instance:
	@echo "$(CLR_HDR)Genererer Modellkatalog-instans$(CLR_RST)"
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/generate-modellkatalog.py

.PHONY: gen-begrepskatalog-instance

gen-begrepskatalog-instance:
	@echo "$(CLR_HDR)Samlar begrep frå begrepssamlingar til begrepskatalogar$(CLR_RST)"
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/collect-concepts.py

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
	@echo "$(CLR_HDR)Validerer Informasjonsmodell-instans for $(SCHEMA)$(CLR_RST)"
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
	@echo "$(CLR_HDR)Validerer Modellkatalog-instans for $(ORG)$(CLR_RST)"
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
