# ==============================================================================
# make/70-scaffolding.mk
#
# Scaffolding-target for å opprette nye modellar, katalogar og begrepssamlingar:
# - new-modell: opprett ny domenemodell via mcp-linkml-modell-utkast
# - remove-modell: fjern ein domenemodell etter tryggleikssjekkar (submodels-/
#   imports-referansar, publish_external) — sjå specs/backlog/remove-modell.md
# - new-modellkatalog: opprett ny modellkatalog for ein organisasjon
# - new-begrepssamling: opprett ny begrepssamling i eit domene (gjeldande format,
#   begrep/-katalog med éin fil per begrep — bruk denne for nye katalogar)
# - gen-valid-scopes: generer .github/valid-scopes.txt frå alle skjema
#
# Merk: `new-begrepskatalog` (legacy scaffolding for det eldre, monolittiske
# BegrepContainer-skjemaformatet) er fjerna, jf.
# specs/done/make-target-namn-vs-funksjon.md, Funn 9.
# src/linkml/begrepskatalog/brreg-begrepskatalog nyttar framleis det gamle
# formatet, men kan ikkje lenger scaffoldast på nytt via make — bruk han som
# mal manuelt dersom eit nytt monolittisk skjema nokon gong trengst.
# ==============================================================================

new-modell: ## Opprett katalogstruktur og boilerplate for ny domenemodell (DOMAIN=<domene> NAME=<modell> [JSON_SCHEMA=<sti til json-schema>])
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-modell DOMAIN=<domene> NAME=<modell> [JSON_SCHEMA=<sti>]"; exit 1; }
	$(call print_header,new-modell,DOMAIN=$(DOMAIN)  NAME=$(NAME)$(if $(JSON_SCHEMA),  JSON_SCHEMA=$(JSON_SCHEMA)))
	@podman image exists $(LINKML_MOD_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory build-docker-mcp-modell-utkast
	bash src/assets/scripts/scaffolding/new-modell.sh "$(NAME)" "$(DOMAIN)" "$(JSON_SCHEMA)"

remove-modell: ## Fjern ein domenemodell etter tryggleikssjekkar (DOMAIN=<domene> NAME=<modell>) [CONFIRM=1]
	@test -n "$(NAME)" && test -n "$(DOMAIN)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make remove-modell DOMAIN=<domene> NAME=<modell> [CONFIRM=1]"; exit 1; }
	$(call print_header,remove-modell,DOMAIN=$(DOMAIN)  NAME=$(NAME))
	bash src/assets/scripts/scaffolding/remove-modell.sh "$(NAME)" "$(DOMAIN)" $(if $(CONFIRM),--confirm)

new-modellkatalog: ## Opprett katalogstruktur og boilerplate for ny organisasjonskatalog (ORG=<alias>)
	@test -n "$(ORG)" || { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-modellkatalog ORG=<alias>"; exit 1; }
	$(call print_header,new-modellkatalog,ORG=$(ORG))
	bash src/assets/scripts/scaffolding/new-modellkatalog.sh "$(ORG)"

new-begrepssamling: ## Opprett katalogstruktur for ny begrepssamling (DOMAIN=<domene> NAME=<begrepssamling>)
	@test -n "$(DOMAIN)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-begrepssamling DOMAIN=<domene> NAME=<begrepssamling>"; exit 1; }
	@test -n "$(NAME)" || \
	  { eval "$$LOG_FUNCTIONS"; log_error "Bruk: make new-begrepssamling DOMAIN=<domene> NAME=<begrepssamling>"; exit 1; }
	$(call print_header,new-begrepssamling,DOMAIN=$(DOMAIN)  NAME=$(NAME))
	bash src/assets/scripts/scaffolding/new-begrepssamling.sh "$(DOMAIN)" "$(NAME)"

# Køyrer automatisk ved `make new-modell`, `make new-modellkatalog`, `make new-begrepssamling`
gen-valid-scopes: ## Generer .github/valid-scopes.txt frå alle *-schema.yaml-filer
	@eval "$$LOG_FUNCTIONS"; \
	log_info "Genererer .github/valid-scopes.txt..."; \
	find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
	  | sed 's|.*/||; s|-schema\.yaml$$||' \
	  | sort \
	  > .github/valid-scopes.txt; \
	log_info "Generert $$(wc -l < .github/valid-scopes.txt) scopes"
