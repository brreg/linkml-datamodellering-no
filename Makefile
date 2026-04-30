AP_NO_SCHEMAS := dcat-ap-no dqv-ap-no cpsv-ap-no skos-ap-no xkos-ap-no
NGR_SCHEMAS   := ngr-adresse
FINT_SCHEMAS  := fint-administrasjon fint-utdanning fint-okonomi fint-arkiv fint-personvern fint-ressurs
FAIR_SCHEMAS  := fair-metadata
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

.PHONY: all test validate docs gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl gen-rdf convert-rdf clean \
        mcp-build mcp-run mcp-test mcp-smoke


all: test

test:
	bash tests/test_schemas.sh

# Valider skjema mot LinkML-metaskjemaet
validate:
	$(foreach s,$(AP_NO_SCHEMAS),$(PODMAN) gen-linkml --validate $(call ap_no_schema,$(s));)
	$(foreach s,$(NGR_SCHEMAS),$(PODMAN) gen-linkml --validate $(call ngr_schema,$(s));)
	$(foreach s,$(FINT_SCHEMAS),$(PODMAN) gen-linkml --validate $(call fint_schema,$(s));)
	$(foreach s,$(FAIR_SCHEMAS),$(PODMAN) gen-linkml --validate $(call fair_schema,$(s));)

# Generer JSON-LD kontekst
gen-jsonld:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-jsonld-context $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-context.jsonld;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-jsonld-context $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-context.jsonld;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-jsonld-context $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-context.jsonld;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-jsonld-context $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-context.jsonld;)

# Generer SHACL shapes
gen-shacl:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-shacl $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-shapes.ttl;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-shacl $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-shapes.ttl;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-shacl $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-shapes.ttl;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-shacl $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-shapes.ttl;)

# Generer Python dataklasser
gen-python:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-python $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-model.py;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-python $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-model.py;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-python $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-model.py;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-python $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-model.py;)

# Generer JSON Schema
gen-jsonschema:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-json-schema $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-schema.json;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-json-schema $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-schema.json;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-json-schema $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-schema.json;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-json-schema $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-schema.json;)

# Generer OWL/Turtle
gen-owl:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-owl $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-ontology.ttl;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-owl $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-ontology.ttl;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-owl $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-ontology.ttl;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-owl $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-ontology.ttl;)

# Generer RDF/Turtle (skjema som RDF-graf)
gen-rdf:
	$(foreach s,$(AP_NO_SCHEMAS),mkdir -p $(GEN_DIR)/ap-no/$(s) && $(PODMAN) gen-rdf $(call ap_no_schema,$(s)) > $(GEN_DIR)/ap-no/$(s)/$(s)-schema.ttl;)
	$(foreach s,$(NGR_SCHEMAS),mkdir -p $(GEN_DIR)/ngr/$(s) && $(PODMAN) gen-rdf $(call ngr_schema,$(s)) > $(GEN_DIR)/ngr/$(s)/$(s)-schema.ttl;)
	$(foreach s,$(FINT_SCHEMAS),mkdir -p $(GEN_DIR)/fint/$(s) && $(PODMAN) gen-rdf $(call fint_schema,$(s)) > $(GEN_DIR)/fint/$(s)/$(s)-schema.ttl;)
	$(foreach s,$(FAIR_SCHEMAS),mkdir -p $(GEN_DIR)/fair/$(s) && $(PODMAN) gen-rdf $(call fair_schema,$(s)) > $(GEN_DIR)/fair/$(s)/$(s)-schema.ttl;)

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

# Generer HTML-dokumentasjon
docs:
	$(foreach s,$(AP_NO_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/ap-no/$(s)/docs $(call ap_no_schema,$(s));)
	$(foreach s,$(NGR_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/ngr/$(s)/docs $(call ngr_schema,$(s));)
	$(foreach s,$(FINT_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/fint/$(s)/docs $(call fint_schema,$(s));)
	$(foreach s,$(FAIR_SCHEMAS),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(GEN_DIR)/fair/$(s)/docs $(call fair_schema,$(s));)

clean:
	rm -rf $(GEN_DIR)

# ---------------------------------------------------------------------------
# MCP-validator
# ---------------------------------------------------------------------------

# Bygg container-bilete
mcp-build:
	podman build -t $(MCP_IMAGE) $(MCP_DIR)

# Køyr MCP-serveren interaktivt (stdin/stdout)
mcp-run:
	podman run -i --rm $(MCP_IMAGE)

# Køyr unit-testar inne i linkml-imaget
mcp-test:
	$(PODMAN) bash -c "pip install pytest --quiet 2>/dev/null && python -m pytest tests/test_mcp_server.py -v"

# Røyk-test med eksempel-JSON-RPC-meldingar
mcp-smoke: mcp-build
	cat tests/test-mcp-linkml-validator.json | podman run -i --rm $(MCP_IMAGE)
