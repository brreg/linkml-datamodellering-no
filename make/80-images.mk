# ==============================================================================
# make/80-images.mk
#
# Container-image-bygging for alle verktøy:
# - build-docker-linkml: LinkML-container (gen-linkml, gen-doc, gen-owl, osv.)
# - build-docker-python: Python-container (pytest, validering, script)
# - build-docker-avrotize: Avrotize-container (JSON Schema → Avro → XSD)
# - build-docker-asyncapi: AsyncAPI CLI-container (validering av AsyncAPI-spec)
# - build-docker-plantuml: PlantUML-container (generering av diagram)
# - build-docker-gource: Gource-container (git-historikk-visualisering)
# ==============================================================================

build-docker-linkml: ## Bygg LinkML container-image
	$(call print_header,build-docker-linkml)
	@podman build --format docker -f $(LINKML_DOCKERFILE) -t $(LINKML_IMAGE) .

build-docker-python: ## Bygg Python container-image
	$(call print_header,build-docker-python)
	@podman build --format docker -f $(PYTHON_DOCKERFILE) -t $(PYTHON_IMAGE)

build-docker-avrotize: ## Bygg Avrotize container-image
	$(call print_header,build-docker-avrotize)
	@podman build --format docker -f $(AVROTIZE_DOCKERFILE) -t $(AVROTIZE_IMAGE)

build-docker-asyncapi: ## Bygg AsyncAPI CLI container-image
	$(call print_header,build-docker-asyncapi)
	@podman build --format docker -f $(ASYNCAPI_DOCKERFILE) -t $(ASYNCAPI_IMAGE)

build-docker-plantuml: ## Bygg PlantUML container-image
	$(call print_header,build-docker-plantuml)
	@podman build --format docker -f src/assets/containers/Dockerfile.plantuml -t localhost/plantuml:latest .

build-docker-gource: ## Bygg Gource container-image
	$(call print_header,build-docker-gource)
	@podman build --format docker -f $(GOURCE_DOCKERFILE) -t $(GOURCE_IMAGE)
