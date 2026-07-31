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

build-docker-gource:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-gource$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(GOURCE_DOCKERFILE) -t $(GOURCE_IMAGE)
