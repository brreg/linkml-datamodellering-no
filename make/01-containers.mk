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
PYTHON_RUN := podman run --rm $(WORK_MOUNT) \
	-e PYTHONWARNINGS=ignore \
	$(PYTHON_IMAGE)

# MkDocs container (spesiell mount-konfigurasjon)
# Mountar berre nødvendige delkatalogar for å unngå unødvendig I/O
DOCS_RUN := podman run --rm \
	-v "$(CURDIR)/mkdocs/docs:/docs/docs" \
	-v "$(CURDIR)/mkdocs/mkdocs.yml:/docs/mkdocs.yml" \
	-v "$(CURDIR)/mkdocs/overrides:/docs/overrides" \
	-v "$(CURDIR)/mkdocs/.cache:/docs/.cache" \
	-v "$(CURDIR)/mkdocs/site:/docs/site"
