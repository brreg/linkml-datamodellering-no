# ==============================================================================
# make/01-containers.mk
#
# Container-wrapperar for alle verktøy.
# Alle wrapperar mountar repoet som /work og køyrer med -w /work.
# ==============================================================================

# Felles mount-konfigurasjon
WORK_MOUNT := -v "$(CURDIR):/work" -w /work

# LinkML container
LINKML_RUN := podman run --rm $(WORK_MOUNT) \
	-e PYTHONWARNINGS=ignore \
	-e HOME=/tmp \
	--user root \
	$(LINKML_IMAGE)

# Avrotize container
AVROTIZE_RUN := podman run --rm \
	-v "$(CURDIR):/work" \
	$(AVROTIZE_IMAGE)

# AsyncAPI CLI container
ASYNCAPI_RUN := podman run --rm $(WORK_MOUNT) \
	-e SUPPRESS_NO_CONFIG_WARNING=true \
	$(ASYNCAPI_IMAGE)

# Python container
# -e GITHUB_REPOSITORY: vidarefører GitHub Actions sin automatisk sette
# owner/repo-variabel inn i containeren (t.d. brukt av
# generate-informasjonsmodell.py for å slå opp raw-URL utan .git/, som
# generate-jobben i generate.yml aldri har — sjå
# specs/done/fiks-git-remote-url-ci-varsel.md). Trygt no-op lokalt der
# variabelen ikkje er sett.
PYTHON_RUN := podman run --rm $(WORK_MOUNT) \
	-e PYTHONWARNINGS=ignore \
	-e GITHUB_REPOSITORY \
	$(PYTHON_IMAGE)

# MkDocs container (spesiell mount-konfigurasjon)
# Mountar berre nødvendige delkatalogar for å unngå unødvendig I/O
DOCS_RUN := podman run --rm \
	-v "$(CURDIR)/mkdocs/docs:/docs/docs" \
	-v "$(CURDIR)/mkdocs/mkdocs.yml:/docs/mkdocs.yml" \
	-v "$(CURDIR)/mkdocs/overrides:/docs/overrides" \
	-v "$(CURDIR)/mkdocs/.cache:/docs/.cache" \
	-v "$(CURDIR)/mkdocs/site:/docs/site"
