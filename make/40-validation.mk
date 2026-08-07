# ==============================================================================
# make/40-validation.mk
#
# Validering av skjema, eksempelfiler og datafiler:
# - LinkML-validering (validate, lint, validate-instance)
# - Bronze/policy-validering (validate-bronze, validate-data, validate-examples)
# - MCP-validering (mcp-linkml-valider-modell, validate-capture)
# - Logging av valideringsresultat (log-mcp-validate, log-validate-instance)
#
# Relaterte script:
# - src/assets/scripts/makefile/detect-validation-policy.py
# - src/assets/scripts/makefile/run-schema-validation.py
# - src/assets/scripts/makefile/save-validation-log.py
# - src/assets/scripts/makefile/emit-github-validation-annotations.py
# - src/assets/scripts/makefile/run-validation.sh
# ==============================================================================

# ---------------------------------------------------------------------------
# LinkML-validering
# ---------------------------------------------------------------------------

validate: ## Valider alle skjema (merge-imports)
	$(call print_header,validate)
	@eval "$$LOG_FUNCTIONS"; \
	$(foreach s,$(SCHEMAS),log_info "$(CLR_STEP)→ merge-imports  $(s)$(CLR_RST)" && log_debug "Kommando: $(LINKML_RUN) gen-linkml $(s)" && $(LINKML_RUN) gen-linkml $(s) > /dev/null;)

lint: ## Køyr linkml lint [SCHEMA=<sti>]
	$(call print_header,lint,$(if $(SCHEMA),SCHEMA=$(SCHEMA),(alle skjema)))
	@if [ -n "$(SCHEMA)" ]; then \
		$(LINKML_RUN) linkml lint --config src/assets/containers/.linkmllint.yaml "$(SCHEMA)"; \
	else \
		$(foreach s,$(SCHEMAS),$(LINKML_RUN) linkml lint --config src/assets/containers/.linkmllint.yaml "$(s)" &&) true; \
	fi

validate-instance: ## Valider instansfil mot skjema (SCHEMA=<sti> INSTANCE=<sti>)
	@test -n "$(SCHEMA)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1; }
	@test -n "$(INSTANCE)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1; }
	$(call print_header,validate-instance,SCHEMA=$(SCHEMA)  INSTANCE=$(INSTANCE))
	$(LINKML_RUN) linkml validate --schema "$(SCHEMA)" "$(INSTANCE)"

# ---------------------------------------------------------------------------
# Policy-validering (bronze/silver/gold/felles-*)
# ---------------------------------------------------------------------------

validate-bronze: ## Valider skjema med bronze-policy (DOMAIN=<domain>)
ifdef DOMAIN
	@eval "$$LOG_FUNCTIONS"; \
	set +e; \
	FAILED=0; \
	SCHEMA_LIST=$$(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort); \
	if [ -z "$$SCHEMA_LIST" ]; then \
		log_info "Ingen skjema funne for DOMAIN=$(DOMAIN)"; \
		exit 0; \
	fi; \
	COUNT=$$(echo "$$SCHEMA_LIST" | wc -l); \
	BATCH_DIR=$$(mktemp -d); \
	trap 'rm -rf "$$BATCH_DIR"' EXIT; \
	log_debug "Kommando: batch-flatten-and-validate.py --policy bronze ($$COUNT skjema, domain $(DOMAIN))"; \
	t0=$$(date +%s%3N); \
	python3 src/mcp-linkml-validator/batch-flatten-and-validate.py --policy bronze \
		--output-dir "$$BATCH_DIR" $$SCHEMA_LIST 2>/dev/null; \
	t1=$$(date +%s%3N); \
	ms=$$(( t1 - t0 )); \
	log_info "$$(printf '$(CLR_STEP)→ validate-bronze  %s  (%d skjema, batcha)$(CLR_RST) (%d.%ds)' "$(DOMAIN)" "$$COUNT" $$(( ms / 1000 )) $$(( ms % 1000 / 100 )))"; \
	i=0; \
	while IFS= read -r schema; do \
		result=$$(cat "$$BATCH_DIR/$$i.json" 2>/dev/null || echo '{"valid":false,"errorCount":1,"warningCount":0,"issues":[{"severity":"error","code":"missing_batch_result","target":"schema","message":"Batch-resultat manglar"}]}'); \
		log_debug "$$result"; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type bronze --result "$$result" < /dev/null 2>/dev/null || true; \
		if ! SCHEMA="$$schema" $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/emit-github-validation-annotations.py <<< "$$result"; then \
			FAILED=$$((FAILED + 1)); \
		fi; \
		i=$$((i + 1)); \
	done <<< "$$SCHEMA_LIST"; \
	exit $$FAILED
else
	@log_error "FEIL: DOMAIN er påkravd. Bruk: make validate-bronze DOMAIN=<domain>"
	@exit 1
endif

validate-data: ## Valider datafiler (data/*/*.yaml) med MCP-validator (DOMAIN=<domain>)
ifdef DOMAIN
	@eval "$$LOG_FUNCTIONS"; \
	DATADIRS=$$(find $(SCHEMA_DIR)/$(DOMAIN) -mindepth 3 -maxdepth 3 -type d -path '*/data/*' 2>/dev/null | sort); \
	if [ -z "$$DATADIRS" ]; then \
		log_info "Ingen datafiler funne for DOMAIN=$(DOMAIN)"; \
		exit 0; \
	fi; \
	BATCH_DIR=$$(mktemp -d); \
	trap 'rm -rf "$$BATCH_DIR"' EXIT; \
	JOBS_TSV="$$BATCH_DIR/jobs.tsv"; \
	: > "$$JOBS_TSV"; \
	for datadir in $$DATADIRS; do \
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
		printf '%s\t%s\t%s\n' "$$schema" "$$policy" "$$datafile" >> "$$JOBS_TSV"; \
	done; \
	COUNT=$$(wc -l < "$$JOBS_TSV"); \
	log_debug "Kommando: batch-flatten-and-validate.py --jobs-tsv ($$COUNT datafiler, domain $(DOMAIN))"; \
	t0=$$(date +%s%3N); \
	python3 src/mcp-linkml-validator/batch-flatten-and-validate.py --jobs-tsv "$$JOBS_TSV" \
		--output-dir "$$BATCH_DIR" 2>/dev/null; \
	t1=$$(date +%s%3N); \
	ms=$$(( t1 - t0 )); \
	log_info "$$(printf '$(CLR_STEP)→ validate-data  %s  (%d datafiler, batcha)$(CLR_RST) (%d.%ds)' "$(DOMAIN)" "$$COUNT" $$(( ms / 1000 )) $$(( ms % 1000 / 100 )))"; \
	i=0; \
	while IFS=$$'\t' read -r schema policy datafile; do \
		catalog=$$(basename "$$datafile" .yaml); \
		result=$$(cat "$$BATCH_DIR/$$i.json" 2>/dev/null || echo '{"valid":false,"errorCount":1,"warningCount":0,"issues":[{"severity":"error","code":"missing_batch_result","target":"schema","message":"Batch-resultat manglar"}]}'); \
		log_debug "$$result"; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type "data-$$catalog" --result "$$result" 2>/dev/null || true; \
		i=$$((i + 1)); \
	done < "$$JOBS_TSV"
else
	@log_error "FEIL: DOMAIN er påkravd. Bruk: make validate-data DOMAIN=<domain>"
	@exit 1
endif

validate-examples: ## Valider eksempelfiler mot skjema (DOMAIN=<domain>)
ifdef DOMAIN
	@eval "$$LOG_FUNCTIONS"; \
	set +e; \
	FAILED=0; \
	while IFS= read -r schema; do \
		name=$$(basename "$$schema" -schema.yaml); \
		domain=$$(echo "$$schema" | cut -d/ -f3); \
		example="$(SCHEMA_DIR)/$(DOMAIN)/$$name/examples/$$name-eksempel.yaml"; \
		if [ ! -f "$$example" ]; then \
			log_info "$(CLR_WARN)::warning file=$$schema::Ingen eksempelfil funne: $$example$(CLR_RST)"; \
			continue; \
		fi; \
		validate_schema="$$schema"; \
		if ! grep -q "tree_root: true" "$$schema"; then \
			fixture="tests/fixtures/$$name-fixture.yaml"; \
			if [ -f "$$fixture" ]; then \
				validate_schema="$$fixture"; \
			else \
				log_info "$(CLR_WARN)::warning file=$$schema::Ingen tree_root og ingen fixture funne ($$fixture) — hoppar over$(CLR_RST)"; \
				continue; \
			fi; \
		fi; \
		log_debug "[$$domain/$$name] Kommando: linkml validate --schema $$validate_schema $$example"; \
		t0=$$(date +%s%3N); \
		result=$$(podman run --rm -v "$$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
			$(LINKML_IMAGE) linkml validate --schema "$$validate_schema" "$$example" 2>&1); \
		exit_code=$$?; \
		t1=$$(date +%s%3N); \
		ms=$$(( t1 - t0 )); \
		log_debug "$$result"; \
		log_info "$$(printf '$(CLR_STEP)→ validate-examples  %s/%s$(CLR_RST) (%d.%ds)' "$$domain" "$$name" $$(( ms / 1000 )) $$(( ms % 1000 / 100 )))"; \
		has_error=false; \
		if [ $$exit_code -ne 0 ]; then \
			has_error=true; \
			if echo "$$result" | grep -q "\[ERROR\]"; then \
				echo "$$result" | grep "\[ERROR\]" | while IFS= read -r line; do \
					log_error "::error file=$$example::$$(echo "$$line" | sed 's/\[ERROR\] //')"; \
				done; \
			else \
				log_error "::error file=$$example::Validering feila (exit code $$exit_code)"; \
			fi; \
			FAILED=$$((FAILED + 1)); \
		fi; \
		if [ "$$has_error" = "true" ]; then \
			result_json='{"valid":false,"error_count":1,"warning_count":0,"issues":[{"severity":"error","target":"examples","message":"Validation failed"}]}'; \
		else \
			result_json='{"valid":true,"error_count":0,"warning_count":0,"issues":[]}'; \
		fi; \
		$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type examples --result "$$result_json" < /dev/null 2>/dev/null || true; \
	done < <(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
		| grep -v common | sort); \
	exit $$FAILED
else
	@log_error "FEIL: DOMAIN er påkravd. Bruk: make validate-examples DOMAIN=<domain>"
	@exit 1
endif

# ---------------------------------------------------------------------------
# MCP-validering
# ---------------------------------------------------------------------------

mcp-linkml-valider-modell: ## MCP-validator for skjema (SCHEMA=<sti> [POLICY=<bronze|silver|gold>])
	@test -n "$(SCHEMA)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make mcp-linkml-valider-modell SCHEMA=<sti-til-skjema> [POLICY=gold]"; exit 1; }
	@DETECTED_POLICY=$$($(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/detect-validation-policy.py "$(SCHEMA)" 2>/dev/null || echo "bronze"); \
	POLICY_TO_USE="$${POLICY:-$$DETECTED_POLICY}"; \
	$(MAKE) --no-print-directory _mcp-valider-modell-with-header SCHEMA=$(SCHEMA) POLICY=$$POLICY_TO_USE

_mcp-valider-modell-with-header:
	$(call print_header,mcp-linkml-valider-modell,SCHEMA=$(SCHEMA)  POLICY=$(POLICY))
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $(POLICY) $(INSTANCE)

# Merk namnekonsistens/overlapp med log-mcp-validate/log-validate-instance
# under: begge skriv til same output-format (validation/<versjon>/<policy>.json),
# men er ikkje duplikat i praksis. validate-capture (run-schema-validation.py)
# er eit manuelt batch-verktøy avgrensa til release-please-config.json sine
# "released packages" — ikkje brukt frå CI. log-mcp-validate/log-validate-
# instance (run-validation.sh) er derimot kalla direkte frå
# .github/workflows/{generate,validate}.yml for kvart einskild skjema/manifest
# — CI-kritisk infrastruktur. Konsolidering vart difor vurdert (jf.
# specs/backlog/make-kommando-inkonsistens-audit.md, namnekonsistens 4) og
# medvite utsett: å skrive om eit CI-kritisk script utan eksplisitt brukar-
# godkjenning bryt CLAUDE.md sitt DRY-unntak for risikofylte omskrivingar.
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

# Validerer og skriv logg til src/linkml/<domain>/<modell>/validation/<version>/<policy>.json
log-mcp-validate: ## Policy-validering med full JSON-logg (MANIFEST=<sti> eller SCHEMA=<sti> POLICY=<policy>)
	@eval "$$LOG_FUNCTIONS"; \
	if [ -n "$(MANIFEST)" ]; then \
		bash src/assets/scripts/makefile/run-validation.sh --manifest $(MANIFEST); \
	elif [ -n "$(SCHEMA)" ] && [ -n "$(POLICY)" ]; then \
		bash src/assets/scripts/makefile/run-validation.sh --schema $(SCHEMA) --policy $(POLICY); \
	else \
		log_error "Oppgi anten MANIFEST=<sti> eller både SCHEMA=<sti> og POLICY=<policy>"; \
		exit 1; \
	fi

# Validerer instans og skriv logg til src/linkml/<domain>/<modell>/validation/<version>/instance-<namn>.json
log-validate-instance: ## Instansvalidering med full JSON-logg (SCHEMA=<sti> INSTANCE=<sti>)
	@test -n "$(SCHEMA)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1; }
	@test -n "$(INSTANCE)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make log-validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1; }
	@bash src/assets/scripts/makefile/run-validation.sh --schema $(SCHEMA) --instance $(INSTANCE)
