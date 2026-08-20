# ==============================================================================
# make/60-mcp.mk
#
# MCP-serverar (Model Context Protocol):
# - mcp-linkml-validator: validator-server (build, run, smoke, test)
# - mcp-linkml-modell-utkast: modellgenerator-server (build, run, smoke, test, new-modell)
# - mcp-linkml-begrep-utkast: begrepsgenerator-server (build, run, smoke, list-profiles)
# ==============================================================================

# ---------------------------------------------------------------------------
# MCP-validator
# ---------------------------------------------------------------------------

MCP_RUN := podman run -i --rm \
  -v "$(CURDIR)/$(MCP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(MCP_DIR)/policies:/app/policies:ro"

build-docker-mcp-validator: ## Bygg container-image for validator MCP-serveren
	$(call print_header,build-docker-mcp-validator)
	@podman build --format docker -f src/assets/containers/Dockerfile.mcp-linkml --target validator -t $(MCP_IMAGE) .

mcp-linkml-valider-modell-run: ## Start validator MCP-serveren interaktivt (JSON-RPC på stdin/stdout)
	$(call print_header,mcp-linkml-valider-modell-run)
	@$(MCP_RUN) $(MCP_IMAGE)

mcp-linkml-valider-modell-smoke: build-docker-mcp-validator ## Røyktest validator MCP-serveren med eksempel-meldingar
	$(call print_header,mcp-linkml-valider-modell-smoke)
	@cat tests/test-mcp-linkml-validator.json | $(MCP_RUN) $(MCP_IMAGE)

mcp-linkml-valider-modell-test: build-docker-mcp-validator ## Køyr alle policy-testar for validator MCP-serveren
	$(call print_header,mcp-linkml-valider-modell-test)
	@podman run --rm \
		-v "$(CURDIR):/work:ro" \
		-e PYTHONWARNINGS=ignore \
		$(MCP_IMAGE) \
		python3 /work/tests/test_mcp_policies.py -v

# ---------------------------------------------------------------------------
# mcp-linkml-modell-utkast
# ---------------------------------------------------------------------------

build-docker-mcp-modell-utkast: ## Bygg container-image for modell-utkast MCP-serveren
	$(call print_header,build-docker-mcp-modell-utkast)
	@podman build --format docker -f src/assets/containers/Dockerfile.mcp-linkml --target modell-utkast -t $(LINKML_MOD_IMAGE) .

mcp-linkml-modell-utkast-run: ## Start modell-utkast MCP-serveren interaktivt (JSON-RPC på stdin/stdout)
	$(call print_header,mcp-linkml-modell-utkast-run)
	@$(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-linkml-modell-utkast-smoke: build-docker-mcp-modell-utkast ## Røyktest modell-utkast MCP-serveren med eksempel-meldingar
	$(call print_header,mcp-linkml-modell-utkast-smoke)
	@cat tests/test-mcp-linkml-generator.json | $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-linkml-modell-utkast-test: build-docker-mcp-modell-utkast ## Køyr alle unit-testar for modell-utkast MCP-serveren
	$(call print_header,mcp-linkml-modell-utkast-test)
	@podman run --rm \
		-v "$(CURDIR)/$(LINKML_MOD_DIR):/app/mcp-linkml-modell-utkast:ro" \
		-v "$(CURDIR)/tests:/app/tests:ro" \
		-w /app/tests \
		-e PYTHONPATH=/app/mcp-linkml-modell-utkast \
		$(LINKML_MOD_IMAGE) \
		python -m pytest test_mcp_linkml_generator.py -v

mcp-linkml-modell-utkast: ## Generer LinkML-skjemautkast frå JSON Schema (SCHEMA=<sti> [FORMAT=json-schema] [POLICY=bronze])
	@test -n "$(SCHEMA)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [POLICY=bronze]"; exit 1; }
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-modell-utkast-request.py \
		--input-format "$(or $(FORMAT),json-schema)" --input-file "$(SCHEMA)" \
		--policy "$(or $(POLICY),bronze)" \
		| $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE) \
		| $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-extract-modell-utkast-response.py \
		> "$(basename $(SCHEMA))-schema.yaml"
	@echo "Skriv til: $(basename $(SCHEMA))-schema.yaml"
	@# Automatisk roundtrip-test for JSON Schema
	@eval "$$LOG_FUNCTIONS"; \
	if echo "$(SCHEMA)" | grep -qE '\.(json|schema\.json)$$'; then \
		log_info "$(CLR_STEP)→ Køyrer roundtrip-test for $(SCHEMA)$(CLR_RST)"; \
		$(MAKE) roundtrip-json-schema JSONSCHEMA="$(SCHEMA)" || \
		(log_error "Roundtrip-test feila — sjå logg for detaljar" && exit 1); \
	fi

# ---------------------------------------------------------------------------
# mcp-linkml-begrep-utkast
#
# Ingen -test-target her (til skilnad frå mcp-linkml-valider-modell-test og
# mcp-linkml-modell-utkast-test): det finst ingen pytest/unittest-suite for
# denne serveren i tests/ i dag (jf. tests/test_mcp_linkml_generator.py for
# modell-utkast). Legg til mcp-linkml-begrep-utkast-test her dersom ei slik
# testsuite vert oppretta.
# ---------------------------------------------------------------------------

build-docker-mcp-begrep-utkast: ## Bygg container-image for begrep-utkast MCP-serveren
	$(call print_header,build-docker-mcp-begrep-utkast)
	@podman build --format docker -f src/assets/containers/Dockerfile.mcp-linkml --target begrep-utkast -t $(LINKML_BEGREP_IMAGE) .

mcp-linkml-begrep-utkast-run: ## Start begrep-utkast MCP-serveren interaktivt (JSON-RPC på stdin/stdout)
	$(call print_header,mcp-linkml-begrep-utkast-run)
	@$(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

mcp-linkml-begrep-utkast-smoke: build-docker-mcp-begrep-utkast ## Røyktest begrep-utkast MCP-serveren med eksempel-meldingar
	$(call print_header,mcp-linkml-begrep-utkast-smoke)
	@echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

mcp-linkml-begrep-utkast: ## Generer YAML-utkast til begrep frå JSON-fil (INPUT=<sti-til-json>)
	@test -n "$(INPUT)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make mcp-linkml-begrep-utkast INPUT=<sti-til-json>"; exit 1; }
	@test -f "$(INPUT)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "$(INPUT) finst ikkje"; exit 1; }
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-begrep-utkast-request.py "$(INPUT)" \
	  | $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

mcp-linkml-begrep-utkast-list-profiles: ## List alle tilgjengelege organisasjonsprofiler for begrepsoppretting
	@podman image exists $(LINKML_BEGREP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-begrep-utkast
	@echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_profiles","arguments":{}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)
