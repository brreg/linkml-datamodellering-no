# ==============================================================================
# make/60-mcp.mk
#
# MCP-serverar (Model Context Protocol):
# - mcp-linkml-validator: validator-server (build, run, smoke, test)
# - mcp-linkml-modell-utkast: modellgenerator-server (build, run, smoke, test, new-model)
# - mcp-linkml-begrep-utkast: begrepsgenerator-server (build, run, smoke, list-profiles)
# ==============================================================================

# ---------------------------------------------------------------------------
# MCP-validator
# ---------------------------------------------------------------------------

MCP_RUN := podman run -i --rm \
  -v "$(CURDIR)/$(MCP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(MCP_DIR)/policies:/app/policies:ro"

build-docker-mcp-validator:
	$(call print_header,build-docker-mcp-validator)
	@podman build --format docker -f src/assets/containers/Dockerfile.mcp-linkml --target validator -t $(MCP_IMAGE) .

mcp-linkml-validate-run:
	$(call print_header,mcp-linkml-validate-run)
	@$(MCP_RUN) $(MCP_IMAGE)

mcp-linkml-validate-smoke: build-docker-mcp-validator
	$(call print_header,mcp-linkml-validate-smoke)
	@cat tests/test-mcp-linkml-validator.json | $(MCP_RUN) $(MCP_IMAGE)

mcp-linkml-validate-test: build-docker-mcp-validator
	$(call print_header,mcp-linkml-validate-test)
	@podman run --rm \
		-v "$(CURDIR):/work:ro" \
		-e PYTHONWARNINGS=ignore \
		$(MCP_IMAGE) \
		python3 /work/tests/test_mcp_policies.py -v

# ---------------------------------------------------------------------------
# mcp-linkml-modell-utkast
# ---------------------------------------------------------------------------

build-docker-mcp-modell-utkast:
	$(call print_header,build-docker-mcp-modell-utkast)
	@podman build --format docker -f src/assets/containers/Dockerfile.mcp-linkml --target modell-utkast -t $(LINKML_MOD_IMAGE) .

mcp-linkml-modell-utkast-run:
	$(call print_header,mcp-linkml-modell-utkast-run)
	@$(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-linkml-modell-utkast-smoke: build-docker-mcp-modell-utkast
	$(call print_header,mcp-linkml-modell-utkast-smoke)
	@cat tests/test-mcp-linkml-generator.json | $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-linkml-modell-utkast-test: build-docker-mcp-modell-utkast
	$(call print_header,mcp-linkml-modell-utkast-test)
	@podman run --rm \
		-v "$(CURDIR)/$(LINKML_MOD_DIR):/app/mcp-linkml-modell-utkast:ro" \
		-v "$(CURDIR)/tests:/app/tests:ro" \
		-w /app/tests \
		-e PYTHONPATH=/app/mcp-linkml-modell-utkast \
		$(LINKML_MOD_IMAGE) \
		python -m pytest test_mcp_linkml_generator.py -v

# Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=bronze]
mcp-linkml-modell-utkast:
	@test -n "$(SCHEMA)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=bronze]"; exit 1; }
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-modell-utkast-request.py \
		"$(SCHEMA)" "$(or $(FORMAT),json-schema)" "$(or $(PROFILE),bronze)" \
		| $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE) \
		| $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-write-modell-utkast-response.py "$(SCHEMA)"
	@# Automatisk roundtrip-test for JSON Schema
	@eval "$$LOG_FUNCTIONS"; \
	if echo "$(SCHEMA)" | grep -qE '\.(json|schema\.json)$$'; then \
		log_info "$(CLR_STEP)→ Køyrer roundtrip-test for $(SCHEMA)$(CLR_RST)"; \
		$(MAKE) roundtrip-json-schema JSONSCHEMA="$(SCHEMA)" || \
		(log_error "Roundtrip-test feila — sjå logg for detaljar" && exit 1); \
	fi

# ---------------------------------------------------------------------------
# mcp-linkml-begrep-utkast
# ---------------------------------------------------------------------------

build-docker-mcp-begrep-utkast:
	$(call print_header,build-docker-mcp-begrep-utkast)
	@podman build --format docker -f src/assets/containers/Dockerfile.mcp-linkml --target begrep-utkast -t $(LINKML_BEGREP_IMAGE) .

mcp-linkml-begrep-utkast-run:
	$(call print_header,mcp-linkml-begrep-utkast-run)
	@$(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

mcp-linkml-begrep-utkast-smoke: build-docker-mcp-begrep-utkast
	$(call print_header,mcp-linkml-begrep-utkast-smoke)
	@echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# Bruk: make mcp-linkml-begrep-utkast INPUT=tmp/mitt-begrep.json
mcp-linkml-begrep-utkast:
	@test -n "$(INPUT)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make mcp-linkml-begrep-utkast INPUT=<sti-til-json>"; exit 1; }
	@test -f "$(INPUT)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "$(INPUT) finst ikkje"; exit 1; }
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-begrep-utkast-request.py "$(INPUT)" \
	  | $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# List profiler:
#   make mcp-linkml-begrep-utkast-list-profiles
mcp-linkml-begrep-utkast-list-profiles:
	@podman image exists $(LINKML_BEGREP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-begrep-utkast
	@echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_profiles","arguments":{}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)
