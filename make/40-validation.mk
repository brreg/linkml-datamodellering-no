# ==============================================================================
# make/40-validation.mk
#
# Validering av skjema, eksempelfiler og datafiler:
# - LinkML-validering (validate, lint, validate-instance)
# - Bronze/policy-validering (validate-bronze, validate-data, validate-examples)
# - MCP-validering (mcp-linkml-validate, validate-capture)
# - Logging av valideringsresultat (log-mcp-validate, log-validate-instance)
#
# Relaterte script:
# - src/assets/scripts/makefile/detect-validation-policy.py
# - src/assets/scripts/makefile/run-schema-validation.py
# - src/assets/scripts/makefile/save-validation-log.py
# - src/assets/scripts/makefile/emit-github-validation-annotations.py
# ==============================================================================

# ---------------------------------------------------------------------------
# LinkML-validering
# ---------------------------------------------------------------------------

validate: ## Valider alle skjema (merge-imports)
	$(call print_header,validate)
	@$(foreach s,$(SCHEMAS),echo "$(CLR_STEP)→ merge-imports  $(s)$(CLR_RST)" && echo "$(LINKML_RUN) gen-linkml $(s) > /dev/null" && $(LINKML_RUN) gen-linkml $(s) > /dev/null;)

lint: ## Køyr linkml lint [SCHEMA=<sti>]
	$(call print_header,lint,$(if $(SCHEMA),SCHEMA=$(SCHEMA),(alle skjema)))
	@if [ -n "$(SCHEMA)" ]; then \
		$(LINKML_RUN) linkml lint --config src/assets/containers/.linkmllint.yaml "$(SCHEMA)"; \
	else \
		$(foreach s,$(SCHEMAS),$(LINKML_RUN) linkml lint --config src/assets/containers/.linkmllint.yaml "$(s)" &&) true; \
	fi

validate-instance: ## Valider instansfil mot skjema (SCHEMA=<sti> INSTANCE=<sti>)
	@test -n "$(SCHEMA)" || (echo "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@test -n "$(INSTANCE)" || (echo "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	$(call print_header,validate-instance,SCHEMA=$(SCHEMA)  INSTANCE=$(INSTANCE))
	$(LINKML_RUN) linkml validate --schema "$(SCHEMA)" "$(INSTANCE)"

# ---------------------------------------------------------------------------
# Policy-validering (bronze/silver/gold/felles-*)
# ---------------------------------------------------------------------------

validate-bronze: ## Valider skjema med bronze-policy (DOMAIN=<domain>)
ifdef DOMAIN
	@set +e; \
	FAILED=0; \
	while IFS= read -r schema; do \
		echo "--- $$schema ---"; \
		result=$$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$$schema" bronze 2>/dev/null); \
		echo "$$result"; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type bronze --result "$$result" 2>/dev/null || true; \
		if ! SCHEMA="$$schema" $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/emit-github-validation-annotations.py <<< "$$result"; then \
			FAILED=$$((FAILED + 1)); \
		fi; \
	done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort); \
	exit $$FAILED
else
	@echo "FEIL: DOMAIN er påkravd. Bruk: make validate-bronze DOMAIN=<domain>" >&2
	@exit 1
endif

validate-data: ## Valider datafiler (data/*/*.yaml) med MCP-validator (DOMAIN=<domain>)
ifdef DOMAIN
	@for datadir in $$(find $(SCHEMA_DIR)/$(DOMAIN) -mindepth 3 -maxdepth 3 -type d -path '*/data/*' 2>/dev/null | sort); do \
		model=$$(echo "$$datadir" | awk -F/ '{print $$4}'); \
		catalog=$$(basename "$$datadir"); \
		datafile="$$datadir/$$catalog.yaml"; \
		[ -f "$$datafile" ] || continue; \
		schema=$(SCHEMA_DIR)/$(DOMAIN)/$$model/$$model-schema.yaml; \
		manifest="$$datadir/build.yaml"; \
		if [ -f "$$manifest" ]; then \
			policy=$$(grep '^validation_policy:' "$$manifest" | awk '{print $$2}'); \
		else \
			policy=bronze; \
		fi; \
		[ -n "$$policy" ] || policy=bronze; \
		echo "$(CLR_STEP)→ mcp-validate  $$datafile  (policy: $$policy)$(CLR_RST)"; \
		result=$$(bash $(MCP_DIR)/flatten-and-validate.bash "$$schema" "$$policy" "$$datafile" 2>/dev/null); \
		echo "$$result"; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type "data-$$catalog" --result "$$result" 2>/dev/null || true; \
	done
else
	@echo "FEIL: DOMAIN er påkravd. Bruk: make validate-data DOMAIN=<domain>" >&2
	@exit 1
endif

validate-examples: ## Valider eksempelfiler mot skjema (DOMAIN=<domain>)
ifdef DOMAIN
	@set +e; \
	FAILED=0; \
	while IFS= read -r schema; do \
		name=$$(basename "$$schema" -schema.yaml); \
		example="$(SCHEMA_DIR)/$(DOMAIN)/$$name/examples/$$name-eksempel.yaml"; \
		if [ ! -f "$$example" ]; then \
			echo "::warning file=$$schema::Ingen eksempelfil funne: $$example"; \
			continue; \
		fi; \
		echo "--- $$schema ---"; \
		result=$$(podman run --rm -v "$$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
			$(LINKML_IMAGE) linkml validate --schema "$$schema" "$$example" 2>&1); \
		echo "$$result"; \
		has_error=false; \
		if echo "$$result" | grep -q "\[ERROR\]"; then \
			has_error=true; \
			echo "$$result" | grep "\[ERROR\]" | while IFS= read -r line; do \
				echo "::error file=$$example::$$(echo "$$line" | sed 's/\[ERROR\] //')"; \
			done; \
			FAILED=$$((FAILED + 1)); \
		fi; \
		if [ "$$has_error" = "true" ]; then \
			result_json='{"valid":false,"error_count":1,"warning_count":0,"issues":[{"severity":"error","target":"examples","message":"Validation failed"}]}'; \
		else \
			result_json='{"valid":true,"error_count":0,"warning_count":0,"issues":[]}'; \
		fi; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type examples --result "$$result_json" 2>/dev/null || true; \
	done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
		| grep -v common | sort | xargs grep -l "tree_root: true"); \
	exit $$FAILED
else
	@echo "FEIL: DOMAIN er påkravd. Bruk: make validate-examples DOMAIN=<domain>" >&2
	@exit 1
endif

# ---------------------------------------------------------------------------
# MCP-validering
# ---------------------------------------------------------------------------

mcp-linkml-validate: ## MCP-validator for skjema (SCHEMA=<sti> [POLICY=<bronze|silver|gold>])
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-linkml-validate SCHEMA=<sti-til-skjema> [POLICY=gold]"; exit 1)
	@DETECTED_POLICY=$$($(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/detect-validation-policy.py "$(SCHEMA)" 2>/dev/null || echo "bronze"); \
	POLICY_TO_USE="$${POLICY:-$$DETECTED_POLICY}"; \
	$(MAKE) --no-print-directory _mcp-validate-with-header SCHEMA=$(SCHEMA) POLICY=$$POLICY_TO_USE

_mcp-validate-with-header:
	$(call print_header,mcp-linkml-validate,SCHEMA=$(SCHEMA)  POLICY=$(POLICY))
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $(POLICY) $(INSTANCE)

validate-capture: ## MCP-validering med logging til validation/ [SCHEMA=<sti>] [PARALLEL=8]
	$(call print_header,validate-capture,$(if $(SCHEMA),SCHEMA=$(SCHEMA),(alle skjema$(COMMA) $(PARALLEL) workers)))
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@if [ -n "$(SCHEMA)" ]; then \
	    $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/run-schema-validation.py --schema $(SCHEMA); \
	else \
	    $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/run-schema-validation.py --parallel $(PARALLEL); \
	fi

# ---------------------------------------------------------------------------
# Logging av valideringsresultat
# ---------------------------------------------------------------------------

# Bruk: make log-mcp-validate MANIFEST=<sti> eller SCHEMA=<sti> POLICY=<policy>
# Validerer og skriv logg til src/linkml/<domain>/<modell>/validation/<version>/<policy>.json
log-mcp-validate:
	@if [ -n "$(MANIFEST)" ]; then \
		bash src/assets/scripts/run-validation.sh --manifest $(MANIFEST); \
	elif [ -n "$(SCHEMA)" ] && [ -n "$(POLICY)" ]; then \
		bash src/assets/scripts/run-validation.sh --schema $(SCHEMA) --policy $(POLICY); \
	else \
		echo "Feil: Oppgi anten MANIFEST=<sti> eller både SCHEMA=<sti> og POLICY=<policy>"; \
		exit 1; \
	fi

# Bruk: make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>
# Validerer instans og skriv logg til src/linkml/<domain>/<modell>/validation/<version>/instance-<namn>.json
log-validate-instance:
	@test -n "$(SCHEMA)" || (echo "Bruk: make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@test -n "$(INSTANCE)" || (echo "Bruk: make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1)
	@bash src/assets/scripts/run-validation.sh --schema $(SCHEMA) --instance $(INSTANCE)
