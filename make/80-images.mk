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
#
# Targeta er skrivne ut kvar for seg (ikkje generert via $(eval $(call ...)),
# slik domain_target i make/20-domain-targets.mk gjer) fordi `make help`
# oppdagar ##-hjelpetekst ved å grep'e KJELDEFILA på disk (sjå help-targetet
# i Makefile) — target/kommentar-linjer generert av $(eval ...) finst berre
# i Make sin minnetilstand, aldri på disk, og ville difor vorte usynlege i
# `make help`. Sjølve podman build-oppskrifta (den delen som faktisk var
# duplisert) er derimot delt via docker_build-makroen.
# ==============================================================================

# ---------------------------------------------------------------------------
# docker_build — delt oppskrift for "podman build -f <dockerfile> -t <tag> <kontekst>"
# ---------------------------------------------------------------------------
# $1 = Dockerfile-sti  $2 = image-tag  $3 = build-kontekst (t.d. "." eller tomt)
# ---------------------------------------------------------------------------
define docker_build
@podman build --format docker -f $(1) -t $(2) $(3)
endef

build-docker-linkml: ## Bygg LinkML container-image
	$(call print_header,build-docker-linkml)
	$(call docker_build,$(LINKML_DOCKERFILE),$(LINKML_IMAGE),.)

build-docker-python: ## Bygg Python container-image
	$(call print_header,build-docker-python)
	$(call docker_build,$(PYTHON_DOCKERFILE),$(PYTHON_IMAGE),)

build-docker-avrotize: ## Bygg Avrotize container-image
	$(call print_header,build-docker-avrotize)
	$(call docker_build,$(AVROTIZE_DOCKERFILE),$(AVROTIZE_IMAGE),)

build-docker-asyncapi: ## Bygg AsyncAPI CLI container-image
	$(call print_header,build-docker-asyncapi)
	$(call docker_build,$(ASYNCAPI_DOCKERFILE),$(ASYNCAPI_IMAGE),.)

build-docker-plantuml: ## Bygg PlantUML container-image
	$(call print_header,build-docker-plantuml)
	$(call docker_build,$(PLANTUML_DOCKERFILE),$(PLANTUML_IMAGE),.)

build-docker-gource: ## Bygg Gource container-image
	$(call print_header,build-docker-gource)
	$(call docker_build,$(GOURCE_DOCKERFILE),$(GOURCE_IMAGE),)
