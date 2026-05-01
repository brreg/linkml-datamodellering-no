AP_NO_SCHEMAS := dcat-ap-no dqv-ap-no cpsv-ap-no skos-ap-no xkos-ap-no modelldcat-ap-no
NGR_SCHEMAS   := ngr-adresse ngr-eiendom ngr-person ngr-virksomhet
FINT_SCHEMAS  := fint-administrasjon fint-utdanning fint-okonomi fint-arkiv fint-personvern fint-ressurs
FAIR_SCHEMAS  := fair-metadata
OREG_SCHEMAS  := register-over-aksjeeiere
SCHEMA_DIR    := src/linkml
MCP_DIR       := src/mcp-linkml-validator
MCP_IMAGE     := mcp-linkml-validator
GEN_DIR       := generated
IMAGE         := docker.io/linkml/linkml:latest
PODMAN        := podman run --rm -v "$(CURDIR):/work" -w /work -e PYTHONWARNINGS=ignore $(IMAGE)

# Skjemafil-makroar
ap_no_schema  = $(SCHEMA_DIR)/ap-no/$(1)/$(1)-schema.yaml
ngr_schema    = $(SCHEMA_DIR)/ngr/$(1)/$(1)-schema.yaml
fint_schema   = $(SCHEMA_DIR)/fint/$(1)/$(1)-schema.yaml
fair_schema   = $(SCHEMA_DIR)/fair/$(1)/$(1)-schema.yaml
oreg_schema   = $(SCHEMA_DIR)/oreg/$(1)/$(1)-schema.yaml

DOCS_IMAGE  := docker.io/squidfunk/mkdocs-material
DOCS_RUN    := podman run --rm -v "$(CURDIR):/docs"

.PHONY: all test validate docs gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl gen-rdf convert-rdf clean \
        mcp-build mcp-run mcp-test mcp-smoke mcp-validate \
        docs-serve docs-build \
        $(addprefix validate-,$(OREG_SCHEMAS))


all: test

test:
	bash tests/test_schemas.sh

# Valider skjema mot LinkML-metaskjemaet
validate:
	$(foreach s,$(AP_NO_SCHEMAS),$(PODMAN) gen-linkml --validate $(call ap_no_schema,$(s));)
	$(foreach s,$(NGR_SCHEMAS),$(PODMAN) gen-linkml --validate $(call ngr_schema,$(s));)
	$(foreach s,$(FINT_SCHEMAS),$(PODMAN) gen-linkml --validate $(call fint_schema,$(s));)
	$(foreach s,$(FAIR_SCHEMAS),$(PODMAN) gen-linkml --validate $(call fair_schema,$(s));)
	$(foreach s,$(OREG_SCHEMAS),$(PODMAN) gen-linkml --validate $(call oreg_schema,$(s));)

# Generer JSON-LD kontekst
gen-jsonld:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-jsonld-context $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-context.jsonld;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-jsonld-context $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-context.jsonld;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-jsonld-context $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-context.jsonld;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-jsonld-context $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-context.jsonld;)
	$(foreach s,$(OREG_SCHEMAS),mkdir -p $(GEN_DIR)/oreg/$(s) && $(PODMAN) gen-jsonld-context $(call oreg_schema,$(s)) > $(GEN_DIR)/oreg/$(s)/$(s)-context.jsonld;)

# Generer SHACL shapes
gen-shacl:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-shacl $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-shapes.ttl;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-shacl $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-shapes.ttl;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-shacl $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-shapes.ttl;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-shacl $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-shapes.ttl;)
	$(foreach s,$(OREG_SCHEMAS),mkdir -p $(GEN_DIR)/oreg/$(s) && $(PODMAN) gen-shacl $(call oreg_schema,$(s)) > $(GEN_DIR)/oreg/$(s)/$(s)-shapes.ttl;)

# Generer Python dataklasser
gen-python:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-python $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-model.py;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-python $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-model.py;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-python $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-model.py;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-python $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-model.py;)
	$(foreach s,$(OREG_SCHEMAS),mkdir -p $(GEN_DIR)/oreg/$(s) && $(PODMAN) gen-python $(call oreg_schema,$(s)) > $(GEN_DIR)/oreg/$(s)/$(s)-model.py;)

# Generer JSON Schema
gen-jsonschema:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-json-schema $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-schema.json;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-json-schema $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-schema.json;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-json-schema $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-schema.json;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-json-schema $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-schema.json;)
	$(foreach s,$(OREG_SCHEMAS),mkdir -p $(GEN_DIR)/oreg/$(s) && $(PODMAN) gen-json-schema $(call oreg_schema,$(s)) > $(GEN_DIR)/oreg/$(s)/$(s)-schema.json;)

# Generer OWL/Turtle
gen-owl:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-owl $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-ontology.ttl;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-owl $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-ontology.ttl;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-owl $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-ontology.ttl;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-owl $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-ontology.ttl;)
	$(foreach s,$(OREG_SCHEMAS),mkdir -p $(GEN_DIR)/oreg/$(s) && $(PODMAN) gen-owl $(call oreg_schema,$(s)) > $(GEN_DIR)/oreg/$(s)/$(s)-ontology.ttl;)

# Generer RDF/Turtle (skjema som RDF-graf)
gen-rdf:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-rdf $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-schema.ttl;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-rdf $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-schema.ttl;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-rdf $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-schema.ttl;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-rdf $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-schema.ttl;)
	$(foreach s,$(OREG_SCHEMAS),mkdir -p $(GEN_DIR)/oreg/$(s) && $(PODMAN) gen-rdf $(call oreg_schema,$(s)) > $(GEN_DIR)/oreg/$(s)/$(s)-schema.ttl;)

# Konverter eksempeldata (YAML) til RDF/Turtle
# AP-NO-profiler (utan tree_root) brukar fixture-skjema
# NGR-domenemodeller (med tree_root) brukar skjemaet direkte
convert-rdf:
	for example in examples/ap-no/*-eksempel.yaml; do \
		name=$$(basename "$$example" .yaml); \
		profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
		mkdir -p $(GEN_DIR)/ap-no/$$profil; \
		$(PODMAN) linkml-convert \
			--schema tests/fixtures/$$profil-fixture.yaml \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/ap-no/$$profil/$$name.ttl \
			$$example; \
	done
	for example in examples/ngr/*-eksempel.yaml; do \
		name=$$(basename "$$example" .yaml); \
		profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
		mkdir -p $(GEN_DIR)/ngr/$$profil; \
		$(PODMAN) linkml-convert \
			--schema $(SCHEMA_DIR)/ngr/$$profil/$$profil-schema.yaml \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/ngr/$$profil/$$name.ttl \
			$$example; \
	done
	for example in examples/fint/*-eksempel.yaml; do \
		name=$$(basename "$$example" .yaml); \
		profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
		mkdir -p $(GEN_DIR)/fint/$$profil; \
		$(PODMAN) linkml-convert \
			--schema $(SCHEMA_DIR)/fint/$$profil/$$profil-schema.yaml \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/fint/$$profil/$$name.ttl \
			$$example; \
	done
	for example in examples/oreg/*-eksempel.yaml; do \
		name=$$(basename "$$example" .yaml); \
		profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
		mkdir -p $(GEN_DIR)/oreg/$$profil; \
		$(PODMAN) linkml-convert \
			--schema $(SCHEMA_DIR)/oreg/$$profil/$$profil-schema.yaml \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/oreg/$$profil/$$name.ttl \
			$$example; \
	done

# Generer HTML-dokumentasjon
docs:
	$(foreach s,$(AP_NO_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/ap-no/$(s)/docs $(call ap_no_schema,$(s));)
	$(foreach s,$(NGR_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/ngr/$(s)/docs $(call ngr_schema,$(s));)
	$(foreach s,$(FINT_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/fint/$(s)/docs $(call fint_schema,$(s));)
	$(foreach s,$(FAIR_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/fair/$(s)/docs $(call fair_schema,$(s));)
	$(foreach s,$(OREG_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/oreg/$(s)/docs $(call oreg_schema,$(s));)

clean:
	rm -rf $(GEN_DIR)

# ---------------------------------------------------------------------------
# Dokumentasjonsportal (MkDocs Material)
# ---------------------------------------------------------------------------

# Køyr lokal dev-server med live-reload på http://localhost:8000
docs-serve:
	$(DOCS_RUN) -it -p 8000:8000 $(DOCS_IMAGE) serve --dev-addr=0.0.0.0:8000

# Bygg statisk HTML til site/
docs-build:
	$(DOCS_RUN) $(DOCS_IMAGE) build

# ---------------------------------------------------------------------------
# MCP-validator
# ---------------------------------------------------------------------------

# server.py og policies/ er ikkje bakt inn i image — dei vert montert
# inn ved køyring slik at endringar tek effekt utan rebuild.
MCP_RUN := podman run -i --rm \
  -v "$(CURDIR)/$(MCP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(MCP_DIR)/policies:/app/policies:ro"

# Bygg container-bilete (trengst berre når server.py, requirements.txt
# eller Dockerfile er endra)
mcp-build:
	podman build -t $(MCP_IMAGE) $(MCP_DIR)

# Køyr MCP-serveren interaktivt (stdin/stdout)
mcp-run:
	$(MCP_RUN) $(MCP_IMAGE)

# Køyr unit-testar inne i linkml-imaget
mcp-test:
	$(PODMAN) bash -c "pip install pytest --quiet 2>/dev/null && python -m pytest tests/test_mcp_server.py -v"

# Røyk-test med eksempel-JSON-RPC-meldingar
mcp-smoke: mcp-build
	cat tests/test-mcp-linkml-validator.json | $(MCP_RUN) $(MCP_IMAGE)

# Valider eit skjema med alle importar flatta ut (støttar relative importar).
# Bygger image automatisk viss det ikkje finst, men ikkje på nytt kvar gong.
# Bruk: make mcp-validate SCHEMA=<sti> [POLICY=fair]
mcp-validate:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=fair]"; exit 1)
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory mcp-build
	bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $(POLICY)
