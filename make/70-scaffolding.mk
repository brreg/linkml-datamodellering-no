# ==============================================================================
# make/70-scaffolding.mk
#
# Scaffolding-target for å opprette nye modellar, katalogar og begrepssamlingar:
# - new-model: opprett ny domenemodell via mcp-linkml-modell-utkast
# - new-modellkatalog: opprett ny modellkatalog for ein organisasjon
# - new-begrepssamling: opprett ny begrepssamling i eit domene
# - new-begrepskatalog: deprecated alias for new-begrepssamling
# - update-valid-scopes: generer .github/valid-scopes.txt frå alle skjema
# ==============================================================================

# Bruk: make new-model NAME=<namn> DOMAIN=<domene>
new-model:
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-model NAME=<namn> DOMAIN=<domene>"; exit 1)
	@podman image exists $(LINKML_MOD_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-modell-utkast
	bash src/assets/scripts/scaffolding/new-model.sh "$(NAME)" "$(DOMAIN)"

# Bruk: make new-modellkatalog NAME=<alias>
new-modellkatalog:
	@test -n "$(NAME)" || (echo "Bruk: make new-modellkatalog NAME=<alias>"; exit 1)
	bash src/assets/scripts/scaffolding/new-modellkatalog.sh "$(NAME)"

# Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>
new-begrepssamling:
	@test -n "$(DOMAIN)" || \
	  (echo "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>"; exit 1)
	@test -n "$(NAME)" || \
	  (echo "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>"; exit 1)
	bash src/assets/scripts/scaffolding/new-begrepssamling.sh "$(DOMAIN)" "$(NAME)"

# Deprecated: bruk new-begrepssamling i staden
new-begrepskatalog:
	@echo "Åtvaring: 'make new-begrepskatalog' er deprecated. Bruk 'make new-begrepssamling' i staden." >&2
	@test -n "$(NAME)" || \
	  (echo "Bruk: make new-begrepskatalog NAME=<katalognavn>"; exit 1)
	bash src/assets/scripts/scaffolding/new-begrepskatalog.sh "$(NAME)"

# Generer .github/valid-scopes.txt frå alle *-schema.yaml-filer
# Køyrer automatisk ved `make new-model`, `make new-modellkatalog`, `make new-begrepssamling`
update-valid-scopes:
	@echo "Genererer .github/valid-scopes.txt..."
	@find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
	  | sed 's|.*/||; s|-schema\.yaml$$||' \
	  | sort \
	  > .github/valid-scopes.txt
	@echo "Generert $$(wc -l < .github/valid-scopes.txt) scopes"
