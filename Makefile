# ==============================================================================
# Makefile
#
# Hovud-byggefil for linkml-datamodellering-no.
# Modular (settings, containers, generators, osv.) er inkluderte frå make/*.mk.
# ==============================================================================

SHELL       := /bin/bash
.SHELLFLAGS := -o pipefail -c

# Inkluder modular i rett rekkefølgje
include make/00-settings.mk
include make/01-containers.mk
include make/02-schema-discovery.mk

# Inkluder generert konfigurasjon (valgfri)
-include config.mk

# Inkluder generator-makroar
include make/10-generator-macros.mk
include make/11-generator-targets.mk

# Inkluder domain-targets
include make/20-domain-targets.mk

# Inkluder instans-, validerings- og docs-targets
include make/30-instances.mk
include make/40-validation.mk
include make/50-docs.mk

# ---------------------------------------------------------------------------
# Top-level targets
# ---------------------------------------------------------------------------
LINKML_MOD_DIR   := src/mcp-linkml-modell-utkast
LINKML_MOD_IMAGE := mcp-linkml-modell-utkast
LINKML_MOD_RUN   := podman run -i --rm \
  -v "$(CURDIR)/$(LINKML_MOD_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(LINKML_MOD_DIR)/converter.py:/app/converter.py:ro" \
  -v "$(CURDIR)/$(LINKML_MOD_DIR)/validator.py:/app/validator.py:ro" \
  -v "$(CURDIR)/$(LINKML_MOD_DIR)/profiles:/app/profiles:ro"

LINKML_BEGREP_DIR   := src/mcp-linkml-begrep-utkast
LINKML_BEGREP_IMAGE := mcp-linkml-begrep-utkast
LINKML_BEGREP_RUN   := podman run -i --rm \
  -v "$(CURDIR)/$(LINKML_BEGREP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(LINKML_BEGREP_DIR)/generator.py:/app/generator.py:ro" \
  -v "$(CURDIR)/$(LINKML_BEGREP_DIR)/los_tema.py:/app/los_tema.py:ro" \
  -v "$(CURDIR)/$(LINKML_BEGREP_DIR)/profiles:/app/profiles:ro" \
  -v "$(CURDIR):/repo:ro"

PARALLEL ?= 8

.PHONY: test roundtrip validate lint validate-instance clean gen-config \
		gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl gen-rdf gen-erdiagram convert-rdf convert-data gen-docs \
        gen-proto gen-plantuml gen-xsd gen-asyncapi gen-openapi \
        validate-bronze validate-data validate-examples \
        build-docker-linkml build-docker-python build-docker-avrotize build-docker-asyncapi build-docker-mkdocs build-docker-plantuml \
        build-docker-mcp-validator build-docker-mcp-modell-utkast build-docker-mcp-begrep-utkast build-docker-gource \
        mcp-linkml-validate-run mcp-linkml-validate-smoke mcp-linkml-validate-test mcp-linkml-validate \
        mcp-linkml-modell-utkast-run mcp-linkml-modell-utkast-smoke mcp-linkml-modell-utkast-test mcp-linkml-modell-utkast new-model \
        mcp-linkml-begrep-utkast-run mcp-linkml-begrep-utkast-smoke mcp-linkml-begrep-utkast-list-profiles mcp-linkml-begrep-utkast \
		docs-serve docs-build docs-publish \
        check-published-uris check-prereqs \
        update-modellkatalog gen-dqv-measurements gen-modelldcat-elements new-modellkatalog new-begrepskatalog \
        validate-capture \
        build-docker-gource gource-preview gource-video _gource-render

test:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	bash tests/test_make.sh "$(SCHEMA)"

# Bruk: make roundtrip [SCHEMA=<sti-til-skjema>]
roundtrip:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make roundtrip$(if $(SCHEMA),  SCHEMA=$(SCHEMA),  (alle skjema))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	TEST_FILTER=roundtrip bash tests/test_make.sh "$(SCHEMA)"

# Bruk: make roundtrip-json-schema [JSONSCHEMA=<sti-til-json-schema>]
roundtrip-json-schema:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make roundtrip-json-schema$(if $(JSONSCHEMA),  JSONSCHEMA=$(JSONSCHEMA),  (alle JSON Schema i src/tmp))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	TEST_FILTER=roundtrip-json-schema bash tests/test_make.sh "$(JSONSCHEMA)"

# ---------------------------------------------------------------------------
# Generator targets (genererte av make_gen_target) — gamle definisjonar fjerna
# ---------------------------------------------------------------------------

build-docker-linkml:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-linkml$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(LINKML_DOCKERFILE) -t $(LINKML_IMAGE) .

build-docker-python:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-python$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(PYTHON_DOCKERFILE) -t $(PYTHON_IMAGE)

build-docker-avrotize:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-avrotize$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(AVROTIZE_DOCKERFILE) -t $(AVROTIZE_IMAGE)

build-docker-asyncapi:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-asyncapi$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(ASYNCAPI_DOCKERFILE) -t $(ASYNCAPI_IMAGE)

build-docker-plantuml:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-plantuml$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f src/assets/containers/Dockerfile.plantuml -t localhost/plantuml:latest .

# Convert example YAML to RDF/Turtle for all domains.
# AP-NO profiles have no tree_root and use fixture schemas; others use the schema directly.
convert-rdf:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make convert-rdf$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@for example in $$(find $(SCHEMA_DIR) -path '*/examples/*-eksempel.yaml' | sort); do \
		[ -f "$$example" ] || continue; \
		name=$$(basename "$$example" .yaml); \
		profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
		domain=$$(echo "$$example" | awk -F/ '{print $$3}'); \
		manifest=$(SCHEMA_DIR)/$$domain/$$profil/build.yaml; \
		if [ -f "$$manifest" ] && grep -q "^  example_rdf: false" "$$manifest"; then \
			echo "Hoppar over linkml-convert for $$example (example_rdf: false)"; \
			continue; \
		fi; \
		mkdir -p $(GEN_DIR)/$$domain/$$profil; \
		if [ -f tests/fixtures/$$profil-fixture.yaml ]; then \
			schema=tests/fixtures/$$profil-fixture.yaml; \
		else \
			schema=$(SCHEMA_DIR)/$$domain/$$profil/$$profil-schema.yaml; \
		fi; \
		echo "$(CLR_STEP)→ linkml-convert  $$example$(CLR_RST)"; \
		echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate --output $(GEN_DIR)/$$domain/$$profil/$$name.ttl $$example"; \
		$(LINKML_RUN) linkml-convert \
			--schema $$schema \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/$$domain/$$profil/$$name.ttl \
			$$example; \
	done

# Convert data YAML files to RDF/Turtle for all domains.
# Naming convention: src/linkml/<domain>/<model>/data/<catalog>/<catalog>.yaml → generated/<domain>/<catalog>/<catalog>.ttl
# Schema resolved as: src/linkml/<domain>/<model>/<model>-schema.yaml
convert-data:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make convert-data$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@for datadir in $$(find $(SCHEMA_DIR) -mindepth 4 -maxdepth 4 -type d -path '*/data/*' | sort); do \
		domain=$$(echo "$$datadir" | awk -F/ '{print $$3}'); \
		model=$$(echo "$$datadir" | awk -F/ '{print $$4}'); \
		catalog=$$(basename "$$datadir"); \
		manifest="$$datadir/build.yaml"; \
		[ -f "$$manifest" ] || continue; \
		publish_external=$$(grep '^publish_external:' "$$manifest" | awk '{print $$2}'); \
		[ "$$publish_external" = "true" ] || continue; \
		datafile="$$datadir/$$catalog.yaml"; \
		[ -f "$$datafile" ] || continue; \
		schema=$(SCHEMA_DIR)/$$domain/$$model/$$model-schema.yaml; \
		mkdir -p $(GEN_DIR)/$$domain/$$catalog; \
		echo "$(CLR_STEP)→ linkml-convert  $$datafile$(CLR_RST)"; \
		echo "$(LINKML_RUN) linkml-convert --schema $$schema --output-format ttl --no-validate --output $(GEN_DIR)/$$domain/$$catalog/$$catalog.ttl $$datafile"; \
		$(LINKML_RUN) linkml-convert \
			--schema $$schema \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/$$domain/$$catalog/$$catalog.ttl \
			$$datafile; \
	done

clean:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make clean$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	rm -rf $(GEN_DIR)

# Oppdater Informasjonsmodell-innslag i modellkatalogen frå schema.annotations.*.
# Les annotations frå alle skjema med annotations.utgiver og skriv til katalogdatafila.
update-modellkatalog:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make update-modellkatalog$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/update-modellkatalog.py

# Reknar ut DQV-kvalitetsmålingar (fullstendighet/aktualitet) for datafiler med
# data_policy felles-begrepskatalog/felles-datakatalog og skriv dem attende.
gen-dqv-measurements:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-dqv-measurements$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(PYTHON_RUN) python3 src/assets/scripts/makefile/gen-dqv-measurements.py

# Genererer ModelDCAT-AP-NO-modellelement (Objekttype/Attributt/Assosiasjon/
# Kodeliste/Kodeelement) frå LinkML-skjemastruktur og skriv dem inn i riktig
# org sin modellkatalog-datafil. Krev SchemaView, derfor $(LINKML_RUN) (ikkje
# $(PYTHON_RUN)). Bruk: make gen-modelldcat-elements [ORG=alias] [DRYRUN=1]
gen-modelldcat-elements:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-modelldcat-elements$(if $(ORG),  ORG=$(ORG))$(if $(DRYRUN),  DRYRUN=$(DRYRUN))$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_RUN) python3 src/assets/scripts/makefile/gen-modelldcat-elements.py $(if $(ORG),--org $(ORG)) $(if $(DRYRUN),--dry-run)


# ---------------------------------------------------------------------------
# Per-model generator configuration — regenerated when any build.yaml changes.
# ---------------------------------------------------------------------------
config.mk: $(shell find src/linkml -name 'build.yaml')
	bash src/assets/scripts/makefile/gen-config.sh > config.mk

gen-config: config.mk

# ---------------------------------------------------------------------------
# Per-domain targets – generated automatically in make/20-domain-targets.mk
# New domains appear automatically when schemas are added under src/linkml/.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# MCP-validator
# ---------------------------------------------------------------------------
MCP_RUN := podman run -i --rm \
  -v "$(CURDIR)/$(MCP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(MCP_DIR)/policies:/app/policies:ro"

build-docker-mcp-validator:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-validator$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -t $(MCP_IMAGE) $(MCP_DIR)

mcp-linkml-validate-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-validate-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(MCP_RUN) $(MCP_IMAGE)

mcp-linkml-validate-smoke: build-docker-mcp-validator
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-validate-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-validator.json | $(MCP_RUN) $(MCP_IMAGE)

mcp-linkml-validate-test: build-docker-mcp-validator
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-validate-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR):/work:ro" \
		-e PYTHONWARNINGS=ignore \
		$(MCP_IMAGE) \
		python3 /work/tests/test_mcp_policies.py -v

# ---------------------------------------------------------------------------
# mcp-linkml-modell-utkast
# ---------------------------------------------------------------------------
build-docker-mcp-modell-utkast:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-modell-utkast$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -t $(LINKML_MOD_IMAGE) $(LINKML_MOD_DIR)

mcp-linkml-modell-utkast-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-modell-utkast-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-linkml-modell-utkast-smoke: build-docker-mcp-modell-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-modell-utkast-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	cat tests/test-mcp-linkml-generator.json | $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE)

mcp-linkml-modell-utkast-test: build-docker-mcp-modell-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-modell-utkast-test$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman run --rm \
		-v "$(CURDIR)/$(LINKML_MOD_DIR):/app/mcp-linkml-modell-utkast:ro" \
		-v "$(CURDIR)/tests:/app/tests:ro" \
		-w /app/tests \
		-e PYTHONPATH=/app/mcp-linkml-modell-utkast \
		$(LINKML_MOD_IMAGE) \
		python -m pytest test_mcp_linkml_generator.py -v

# Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=bronze]
mcp-linkml-modell-utkast:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-linkml-modell-utkast SCHEMA=<sti> [FORMAT=json-schema] [PROFILE=bronze]"; exit 1)
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-modell-utkast-request.py \
		"$(SCHEMA)" "$(or $(FORMAT),json-schema)" "$(or $(PROFILE),bronze)" \
		| $(LINKML_MOD_RUN) $(LINKML_MOD_IMAGE) \
		| $(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-write-modell-utkast-response.py "$(SCHEMA)"
	@# Automatisk roundtrip-test for JSON Schema
	@if echo "$(SCHEMA)" | grep -qE '\.(json|schema\.json)$$'; then \
		echo "$(CLR_STEP)→ Køyrer roundtrip-test for $(SCHEMA)$(CLR_RST)"; \
		$(MAKE) roundtrip-json-schema JSONSCHEMA="$(SCHEMA)" || \
		(echo "$(CLR_ERR)Roundtrip-test feila — sjå logg for detaljar$(CLR_RST)" && exit 1); \
	fi

# ---------------------------------------------------------------------------
# mcp-linkml-begrep-utkast
# ---------------------------------------------------------------------------
build-docker-mcp-begrep-utkast:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mcp-begrep-utkast$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -t $(LINKML_BEGREP_IMAGE) $(LINKML_BEGREP_DIR)

mcp-linkml-begrep-utkast-run:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-begrep-utkast-run$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

mcp-linkml-begrep-utkast-smoke: build-docker-mcp-begrep-utkast
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make mcp-linkml-begrep-utkast-smoke$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# Bruk: make mcp-linkml-begrep-utkast INPUT=tmp/mitt-begrep.json
mcp-linkml-begrep-utkast:
	@test -n "$(INPUT)" || \
	  (echo "Bruk: make mcp-linkml-begrep-utkast INPUT=<sti-til-json>"; exit 1)
	@test -f "$(INPUT)" || \
	  (echo "Feil: $(INPUT) finst ikkje"; exit 1)
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/mcp-build-begrep-utkast-request.py "$(INPUT)" \
	  | $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# List profiler:
#   make mcp-linkml-begrep-utkast-list-profiles
mcp-linkml-begrep-utkast-list-profiles:
	@podman image exists $(LINKML_BEGREP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-begrep-utkast
	@echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_profiles","arguments":{}}}' \
	| $(LINKML_BEGREP_RUN) $(LINKML_BEGREP_IMAGE)

# Bruk: make new-model NAME=<namn> DOMAIN=<domene>
new-model:
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-model NAME=<namn> DOMAIN=<domene>"; exit 1)
	@podman image exists $(LINKML_MOD_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-modell-utkast
	bash src/assets/scripts/new-model.sh "$(NAME)" "$(DOMAIN)"

# Bruk: make new-modellkatalog NAME=<alias>
new-modellkatalog:
	@test -n "$(NAME)" || (echo "Bruk: make new-modellkatalog NAME=<alias>"; exit 1)
	bash src/assets/scripts/new-modellkatalog.sh "$(NAME)"

# Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>
new-begrepssamling:
	@test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>"; exit 1)
	@test -n "$(NAME)" || \
	  (echo "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>"; exit 1)
	bash src/assets/scripts/new-begrepssamling.sh "$(DOMAIN)" "$(NAME)"

# Deprecated: bruk new-begrepssamling i staden
new-begrepskatalog:
	@echo "Åtvaring: 'make new-begrepskatalog' er deprecated. Bruk 'make new-begrepssamling' i staden." >&2
	@test -n "$(NAME)" || \
	  (echo "Bruk: make new-begrepskatalog NAME=<katalognavn>"; exit 1)
	bash src/assets/scripts/new-begrepskatalog.sh "$(NAME)"

# Generer .github/valid-scopes.txt frå alle *-schema.yaml-filer
# Køyrer automatisk ved `make new-model`, `make new-modellkatalog`, `make new-begrepssamling`
update-valid-scopes:
	@echo "Genererer .github/valid-scopes.txt..."
	@find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
	  | sed 's|.*/||; s|-schema\.yaml$$||' \
	  | sort \
	  > .github/valid-scopes.txt
	@echo "Generert $$(wc -l < .github/valid-scopes.txt) scopes"

check-prereqs:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make check-prereqs$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@bash src/assets/scripts/makefile/check-prereqs.bash

# ---------------------------------------------------------------------------
# Gource – visualisering av git-historikk
# ---------------------------------------------------------------------------
GOURCE_IMAGE      := localhost/gource-local:latest
GOURCE_DOCKERFILE := src/assets/containers/Dockerfile.gource

define GOURCE_RUN
podman run --rm \
  -v "$(CURDIR):/repo:ro" \
  -v "$(CURDIR)/tmp:/out" \
  $(GOURCE_IMAGE) \
  bash -c " \
    git config --global --add safe.directory /repo && \
    xvfb-run -a -s '-screen 0 1920x1080x24' \
      gource /repo \
        --seconds-per-day 1 \
        --auto-skip-seconds 1 \
        --title 'linkml-datamodellering-no' \
        --hide mouse,progress \
        --background-colour 111111 \
        --font-size 18 \
        --output-ppm-stream /out/gource.ppm \
        $(GOURCE_EXTRA_FLAGS) && \
    ffmpeg -y -r $(GOURCE_FPS) \
        -f image2pipe -vcodec ppm \
        -i /out/gource.ppm \
        -an -vcodec libx264 $(GOURCE_FFMPEG_PRESET) \
        -pix_fmt yuv420p -movflags +faststart \
        /out/$(GOURCE_OUTFILE) && \
    rm /out/gource.ppm"
endef

build-docker-gource:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-gource$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(GOURCE_DOCKERFILE) -t $(GOURCE_IMAGE)

gource-preview: build-docker-gource
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gource-preview$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p tmp
	$(MAKE) --no-print-directory _gource-render \
	  GOURCE_OUTFILE=gource-preview.mp4 \
	  GOURCE_EXTRA_FLAGS="--viewport 1280x720" \
	  GOURCE_FPS=30 \
	  GOURCE_FFMPEG_PRESET="-preset ultrafast -crf 28"
	@echo "Preview: tmp/gource-preview.mp4"

gource-video: build-docker-gource
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gource-video$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p tmp
	$(MAKE) --no-print-directory _gource-render \
	  GOURCE_OUTFILE=gource.mp4 \
	  GOURCE_EXTRA_FLAGS="--viewport 1920x1080 --bloom-multiplier 0.5" \
	  GOURCE_FPS=60 \
	  GOURCE_FFMPEG_PRESET="-preset fast -crf 22"
	@echo "Video: tmp/gource.mp4"

_gource-render:
	$(GOURCE_RUN)

# ===========================================================================
# Instans-, validerings-, docs- og MCP-targets er flytta til make/*.mk
# ===========================================================================

