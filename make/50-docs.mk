# ==============================================================================
# make/50-docs.mk
#
# MkDocs-dokumentasjonsportal:
# - build-docker-mkdocs: bygg docs-image med mkdocs-kroki
# - docs-serve: køyr lokal server på :8000
# - docs-build: bygg statisk site til mkdocs/site/
# - docs-publish: kopier generated/ til mkdocs/docs/ og generer mkdocs.yml
# ==============================================================================

# ---------------------------------------------------------------------------
# MkDocs Material
# ---------------------------------------------------------------------------

# Bygg lokal docs-image med mkdocs-kroki (trengst for PlantUML-rendering via Kroki.io).
# Køyr éin gong, eller etter endringar i mkdocs/Dockerfile.
build-docker-mkdocs:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make build-docker-mkdocs$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	podman build --format docker -f $(DOCS_DOCKERFILE) -t $(DOCS_IMAGE)

docs-serve:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-serve$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"
	$(DOCS_RUN) -it -p 8000:8000 $(DOCS_IMAGE) serve --dev-addr=0.0.0.0:8000

docs-build:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-build$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@mkdir -p "$(CURDIR)/mkdocs/.cache" "$(CURDIR)/mkdocs/site"
	$(DOCS_RUN) $(DOCS_IMAGE) build

# Kopier genererte artefakter til mkdocs/docs/ og oppdater mkdocs.yml.
# Føresetnad: relevante make domain-<domain>-targets er køyrde fyrst.
docs-publish:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make docs-publish$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_INFO)Oppdaterer README.md-tabellar...$(CLR_RST)"
	bash src/assets/scripts/makefile/generate-readme-tables.sh README.md
	@echo "$(CLR_INFO)Publiserer mkdocs-portal...$(CLR_RST)"
	bash mkdocs/publish.sh
