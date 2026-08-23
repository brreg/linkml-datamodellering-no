# ==============================================================================
# make/40-validation.mk
#
# Validering av skjema, eksempelfiler og datafiler:
# - LinkML-validering (validate, lint, validate-instance)
# - Policy-validering (validate-data, validate-examples)
# - MCP-validering (mcp-linkml-valider-modell, validate-capture)
# - Logging av valideringsresultat (validate-policy-logg, validate-instance-logg)
#
# Relaterte script:
# - src/assets/scripts/makefile/detect-validation-policy.py
# - src/assets/scripts/makefile/run-schema-validation.py
# - src/assets/scripts/makefile/save-validation-log.py
# - src/assets/scripts/makefile/run-validation.sh
# ==============================================================================

# ---------------------------------------------------------------------------
# LinkML-validering
# ---------------------------------------------------------------------------

validate: ## Valider alle skjema (merge-imports, fail-fast, ingen fil skriven) [DOMAIN=<domene>|SCHEMA=<sti>]
ifdef SCHEMA
	$(call print_header,validate,SCHEMA=$(SCHEMA))
else ifdef DOMAIN
	$(call print_header,validate,DOMAIN=$(DOMAIN))
else
	$(call print_header,validate)
endif
	$(call run_gen_linkml_parallel,$(call get_target_schemas))

lint: ## Køyr linkml lint [SCHEMA=<sti>]
	$(call print_header,lint,$(if $(SCHEMA),SCHEMA=$(SCHEMA),(alle skjema)))
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-lint.py \
		--config src/assets/containers/.linkmllint.yaml -- $(if $(SCHEMA),$(SCHEMA),$(SCHEMAS))

validate-instance: ## Valider instansfil mot skjema (SCHEMA=<sti> INSTANCE=<sti>)
	@test -n "$(SCHEMA)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1; }
	@test -n "$(INSTANCE)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make validate-instance SCHEMA=<sti> INSTANCE=<sti>"; exit 1; }
	$(call print_header,validate-instance,SCHEMA=$(SCHEMA)  INSTANCE=$(INSTANCE))
	$(LINKML_RUN) linkml validate --schema "$(SCHEMA)" "$(INSTANCE)"

# ---------------------------------------------------------------------------
# Policy-validering (bronze/silver/gold/felles-*)
# ---------------------------------------------------------------------------

validate-data: ## Valider datafiler (data/*/*.yaml) med MCP-validator (DOMAIN=<domene>)
ifdef DOMAIN
	@eval "$$LOG_FUNCTIONS"; \
	set +e; \
	FAILED=0; \
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
	run_logged "batch-flatten-and-validate/data $(DOMAIN)" python3 src/mcp-linkml-validator/batch-flatten-and-validate.py --jobs-tsv "$$JOBS_TSV" \
		--output-dir "$$BATCH_DIR"; \
	t1=$$(date +%s%3N); \
	ms=$$(( t1 - t0 )); \
	log_info "$$(printf '$(CLR_STEP)→ validate-data  %s  (%d datafiler, batcha)$(CLR_RST) (%s)' "$(DOMAIN)" "$$COUNT" "$$(fmt_elapsed_ms $$ms)")"; \
	i=0; \
	while IFS=$$'\t' read -r schema policy datafile; do \
		catalog=$$(basename "$$datafile" .yaml); \
		result=$$(cat "$$BATCH_DIR/$$i.json" 2>/dev/null || echo '{"valid":false,"errorCount":1,"warningCount":0,"issues":[{"severity":"error","code":"missing_batch_result","target":"schema","message":"Batch-resultat manglar"}]}'); \
		log_debug "$$result"; \
		if echo "$$result" | grep -Eq '"valid"[[:space:]]*:[[:space:]]*false'; then \
			FAILED=$$((FAILED + 1)); \
			log_error "::error file=$$datafile::Validering feila ($$catalog): $$result"; \
		fi; \
		run_logged "save-validation-log/data $$catalog" $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type "data-$$catalog" --result "$$result" < /dev/null; \
		i=$$((i + 1)); \
	done < "$$JOBS_TSV"; \
	exit $$FAILED
else
	@log_error "FEIL: DOMAIN er påkravd. Bruk: make validate-data DOMAIN=<domene>"
	@exit 1
endif

validate-examples: ## Valider eksempelfiler mot skjema (DOMAIN=<domene>)
ifdef DOMAIN
	@eval "$$LOG_FUNCTIONS"; \
	set +e; \
	JOBS_TSV=$$(mktemp "$(GEN_DIR)/.validate-examples-jobs.XXXXXX"); \
	trap 'rm -f "$$JOBS_TSV"' EXIT; \
	SCHEMA_LIST=$$(find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort); \
	if [ -z "$$SCHEMA_LIST" ]; then \
		log_info "Ingen skjema funne for DOMAIN=$(DOMAIN)"; \
		exit 0; \
	fi; \
	while IFS= read -r schema; do \
		name=$$(basename "$$schema" -schema.yaml); \
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
		printf '%s\t%s\t%s\n' "$$schema" "$$validate_schema" "$$example" >> "$$JOBS_TSV"; \
	done <<< "$$SCHEMA_LIST"; \
	if [ ! -s "$$JOBS_TSV" ]; then \
		log_info "Ingen eksempelfiler å validere for DOMAIN=$(DOMAIN)"; \
		exit 0; \
	fi; \
	COUNT=$$(wc -l < "$$JOBS_TSV"); \
	log_debug "Kommando: batch-linkml-validate.py --jobs-tsv ($$COUNT eksempelfiler, domain $(DOMAIN))"; \
	t0=$$(date +%s%3N); \
	if ! $(LINKML_RUN) python3 src/assets/scripts/makefile/batch-linkml-validate.py --jobs-tsv "$$JOBS_TSV"; then \
		FAILED=1; \
	else \
		FAILED=0; \
	fi; \
	t1=$$(date +%s%3N); \
	ms=$$(( t1 - t0 )); \
	log_info "$$(printf '$(CLR_STEP)→ validate-examples  %s  (%d eksempelfiler, batcha)$(CLR_RST) (%s)' "$(DOMAIN)" "$$COUNT" "$$(fmt_elapsed_ms $$ms)")"; \
	i=0; \
	while IFS=$$'\t' read -r schema validate_schema example; do \
		name=$$(basename "$$schema" -schema.yaml); \
		if [ $$FAILED -eq 0 ]; then \
			result_json='{"valid":true,"error_count":0,"warning_count":0,"issues":[]}'; \
		else \
			result_json='{"valid":false,"error_count":1,"warning_count":0,"issues":[{"severity":"error","target":"examples","message":"Validation failed"}]}'; \
		fi; \
		run_logged "save-validation-log/examples $(DOMAIN)/$$name" $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/save-validation-log.py \
			--schema "$$schema" --type examples --result "$$result_json" < /dev/null; \
		i=$$((i + 1)); \
	done < "$$JOBS_TSV"; \
	exit $$FAILED
else
	@log_error "FEIL: DOMAIN er påkravd. Bruk: make validate-examples DOMAIN=<domene>"
	@exit 1
endif

# ---------------------------------------------------------------------------
# MCP-validering
# ---------------------------------------------------------------------------

mcp-linkml-valider-modell: ## MCP-validator for skjema (SCHEMA=<sti> [POLICY=<policy>])
	@test -n "$(SCHEMA)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make mcp-linkml-valider-modell SCHEMA=<sti> [POLICY=gold]"; exit 1; }
	@DETECTED_POLICY=$$($(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/detect-validation-policy.py "$(SCHEMA)" || echo "bronze"); \
	POLICY_TO_USE="$${POLICY:-$$DETECTED_POLICY}"; \
	$(MAKE) --no-print-directory _mcp-valider-modell-with-header SCHEMA=$(SCHEMA) POLICY=$$POLICY_TO_USE

_mcp-valider-modell-with-header:
	$(call print_header,mcp-linkml-valider-modell,SCHEMA=$(SCHEMA)  POLICY=$(POLICY))
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@eval "$$LOG_FUNCTIONS"; \
	LOG_PATH=$$(bash src/assets/scripts/makefile/run-validation.sh \
	    --schema "$(SCHEMA)" --policy "$(POLICY)" \
	    $(if $(INSTANCE),--instance "$(INSTANCE)") --quiet); \
	EXIT_CODE=$$?; \
	cat "$$LOG_PATH"; \
	GEN_PATH=$$(echo "$$LOG_PATH" | sed 's#^src/linkml/#generated/#'); \
	mkdir -p "$$(dirname "$$GEN_PATH")"; \
	cp "$$LOG_PATH" "$$GEN_PATH"; \
	log_info "Skrive til: $$LOG_PATH (og kopiert til $$GEN_PATH for lokal portalvising)"; \
	exit $$EXIT_CODE

# Merk namnekonsistens/overlapp med validate-policy-logg/validate-instance-logg
# under: begge skriv til same output-format (validation/<versjon>/<policy>.json),
# men er ikkje duplikat i praksis. validate-capture (run-schema-validation.py)
# er eit manuelt batch-verktøy avgrensa til release-please-config.json sine
# "released packages" — ikkje brukt frå CI. validate-policy-logg/validate-
# instance-logg (run-validation.sh) er derimot kalla direkte frå
# .github/workflows/{generate,validate}.yml for kvart einskild skjema/manifest
# — CI-kritisk infrastruktur. Konsolidering vart difor vurdert (jf.
# specs/backlog/make-kommando-inkonsistens-audit.md, namnekonsistens 4) og
# medvite utsett: å skrive om eit CI-kritisk script utan eksplisitt brukar-
# godkjenning bryt CLAUDE.md sitt DRY-unntak for risikofylte omskrivingar.
# (Namna sjølve vart omdøypte 2026-08-20, jf.
# specs/done/make-target-namn-vs-funksjon.md, Funn 7 — funksjonen og
# CI-kritikaliteten er uendra.)
validate-capture: ## MCP-validering med logging til validation/ [SCHEMA=<sti>]
	$(call print_header,validate-capture,$(if $(SCHEMA),SCHEMA=$(SCHEMA),(alle skjema$(COMMA) batcha)))
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-validator
	@if [ -n "$(SCHEMA)" ]; then \
	    $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/run-schema-validation.py --schema $(SCHEMA); \
	else \
	    $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/run-schema-validation.py; \
	fi

# ---------------------------------------------------------------------------
# Logging av valideringsresultat
# ---------------------------------------------------------------------------

# Validerer og skriv logg til src/linkml/<domain>/<modell>/validation/<version>/<policy>.json
validate-policy-logg: ## Policy-validering med full JSON-logg (BUILDYAML=<sti>|SCHEMA=<sti> POLICY=<policy>)
	@eval "$$LOG_FUNCTIONS"; \
	if [ -n "$(BUILDYAML)" ]; then \
		bash src/assets/scripts/makefile/run-validation.sh --manifest $(BUILDYAML); \
	elif [ -n "$(SCHEMA)" ] && [ -n "$(POLICY)" ]; then \
		bash src/assets/scripts/makefile/run-validation.sh --schema $(SCHEMA) --policy $(POLICY); \
	else \
		log_error "Oppgi anten BUILDYAML=<sti> eller både SCHEMA=<sti> og POLICY=<policy>"; \
		exit 1; \
	fi

# Validerer instans og skriv logg til src/linkml/<domain>/<modell>/validation/<version>/instance-<namn>.json
validate-instance-logg: ## Instansvalidering med full JSON-logg (SCHEMA=<sti> INSTANCE=<sti>)
	@test -n "$(SCHEMA)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make validate-instance-logg SCHEMA=<sti> INSTANCE=<sti>"; exit 1; }
	@test -n "$(INSTANCE)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make validate-instance-logg SCHEMA=<sti> INSTANCE=<sti>"; exit 1; }
	@bash src/assets/scripts/makefile/run-validation.sh --schema $(SCHEMA) --instance $(INSTANCE)
