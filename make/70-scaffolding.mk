# ==============================================================================
# make/70-scaffolding.mk
#
# Scaffolding-target for å opprette nye modellar, katalogar og begrepssamlingar:
# - new-modell: opprett ny domenemodell via mcp-linkml-modell-utkast
# - new-modellkatalog: opprett ny modellkatalog for ein organisasjon
# - new-begrepssamling: opprett ny begrepssamling i eit domene (gjeldande format,
#   begrep/-katalog med éin fil per begrep — bruk denne for nye katalogar)
# - new-begrepskatalog: legacy scaffolding for det eldre, monolittiske
#   BegrepContainer-skjemaformatet (éin fil, direkte under
#   src/linkml/begrepskatalog/<namn>/). IKKJE ein alias for new-begrepssamling
#   — eige script, eigen skjemastruktur, andre parameter. Halden ved like
#   fordi src/linkml/begrepskatalog/brreg-begrepskatalog framleis nyttar dette
#   formatet.
# - update-valid-scopes: generer .github/valid-scopes.txt frå alle skjema
# ==============================================================================

# Bruk: make new-modell NAME=<namn> DOMAIN=<domene>
new-modell:
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-modell NAME=<namn> DOMAIN=<domene>"; exit 1; }
	@podman image exists $(LINKML_MOD_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-modell-utkast
	bash src/assets/scripts/scaffolding/new-modell.sh "$(NAME)" "$(DOMAIN)"

# Bruk: make new-modellkatalog NAME=<alias>
new-modellkatalog:
	@test -n "$(NAME)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-modellkatalog NAME=<alias>"; exit 1; }
	bash src/assets/scripts/scaffolding/new-modellkatalog.sh "$(NAME)"

# Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>
new-begrepssamling:
	@test -n "$(DOMAIN)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>"; exit 1; }
	@test -n "$(NAME)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-begrepssamling DOMAIN=<domain> NAME=<begrepssamling-namn>"; exit 1; }
	bash src/assets/scripts/scaffolding/new-begrepssamling.sh "$(DOMAIN)" "$(NAME)"

# Legacy: scaffoldar det eldre, monolittiske BegrepContainer-skjemaformatet
# (éi skjemafil under src/linkml/begrepskatalog/<namn>/, i staden for ein
# begrep/-katalog med éin fil per begrep). IKKJE ein alias for
# new-begrepssamling — eige script (new-begrepskatalog.sh), eigen
# skjemastruktur, berre NAME som parameter (ikkje DOMAIN). Bruk
# new-begrepssamling for nye begrepssamlingar; dette targetet held fram
# fordi src/linkml/begrepskatalog/brreg-begrepskatalog alt nyttar formatet.
new-begrepskatalog:
	@test -n "$(NAME)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-begrepskatalog NAME=<katalognavn>"; exit 1; }
	bash src/assets/scripts/scaffolding/new-begrepskatalog.sh "$(NAME)"

# Generer .github/valid-scopes.txt frå alle *-schema.yaml-filer
# Køyrer automatisk ved `make new-modell`, `make new-modellkatalog`, `make new-begrepssamling`
update-valid-scopes:
	@eval "$$LOG_FUNCTIONS"; \
	log_info "Genererer .github/valid-scopes.txt..."; \
	find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
	  | sed 's|.*/||; s|-schema\.yaml$$||' \
	  | sort \
	  > .github/valid-scopes.txt; \
	log_info "Generert $$(wc -l < .github/valid-scopes.txt) scopes"
