# ==============================================================================
# make/50-docs.mk
#
# MkDocs-dokumentasjonsportal:
# - build-docker-mkdocs: bygg docs-image med mkdocs-kroki
# - docs-serve: køyr lokal server på :8000
# - docs-build: bygg statisk site til mkdocs/site/
# - docs-publish: kopier generated/ til mkdocs/docs/ og generer mkdocs.yml
#
# Relaterte script:
# - mkdocs/publish.sh (hovudscript for docs-publish)
# - src/assets/scripts/makefile/generate-readme-tables.sh
# ==============================================================================

# ---------------------------------------------------------------------------
# MkDocs Material
# ---------------------------------------------------------------------------

build-docker-mkdocs: ## Bygg MkDocs container-image
	$(call print_header,build-docker-mkdocs)
	@podman build --format docker -f $(DOCS_DOCKERFILE) -t $(DOCS_IMAGE)

docs-serve: ## Køyr lokal MkDocs-server på :8000
	$(call print_header,docs-serve)
	@mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"
	@$(DOCS_RUN) -it -p 8000:8000 $(DOCS_IMAGE) serve --dev-addr=0.0.0.0:8000

docs-build: ## Bygg statisk MkDocs-site til mkdocs/site/
	$(call print_header,docs-build)
	@eval "$$LOG_FUNCTIONS"; \
	mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"; \
	timed_run "Bygg statisk MkDocs-site" $(DOCS_RUN) $(DOCS_IMAGE) build

docs-publish: ## Publiser generated/ til mkdocs/docs/ og oppdater mkdocs.yml
	$(call print_header,docs-publish)
	@eval "$$LOG_FUNCTIONS"; \
	log_info "$(CLR_STEP)Publiserer mkdocs-portal...$(CLR_RST)"; \
	log_debug "Kommando: mkdocs/publish.sh"; \
	bash mkdocs/publish.sh
