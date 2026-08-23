# ==============================================================================
# make/91-modell-analyse.mk
#
# Analyse på tvers av skjema: liknande klasse-/slotnavn og
# IRI-dereferering (IRI resolution).
# Brukt av .github/workflows/modell-analyse.yml (vekentleg, ikkje CI-
# blokkerande — rapportane er informative, ikkje ein valideringspolicy).
#
# Header-linja vert send til stderr (1>&2) slik at stdout frå målet kan
# omdirigerast rett til ein rapportfil (t.d. `make <target> > rapport.md`)
# utan å blande inn header-teksten.
#
# Relaterte script:
# - src/assets/scripts/makefile/find-similar-names.py
# - src/assets/scripts/makefile/check-iri-resolution.py
# - src/assets/scripts/makefile/summarise-modell-analyse.py
# ==============================================================================

SIMILARITY_THRESHOLD ?= 0.8

.PHONY: analyse-similar-classes-domain analyse-similar-classes-all \
        analyse-similar-slots-domain analyse-similar-slots-all \
        analyse-similar-types-domain analyse-similar-types-all \
        analyse-iri-dereferering analyse-innhaldsforhandling analyse-sammendrag

analyse-similar-classes-domain: ## Finn klasser med liknande navn innanfor same domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-classes-domain) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind class --scope domain --threshold $(SIMILARITY_THRESHOLD) $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))

analyse-similar-classes-all: ## Finn klasser med liknande navn på tvers av alle domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-classes-all) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind class --scope all --threshold $(SIMILARITY_THRESHOLD) $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))

analyse-similar-slots-domain: ## Finn slots med liknande navn innanfor same domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-slots-domain) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind slot --scope domain --threshold $(SIMILARITY_THRESHOLD) $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))

analyse-similar-slots-all: ## Finn slots med liknande navn på tvers av alle domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-slots-all) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind slot --scope all --threshold $(SIMILARITY_THRESHOLD) $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))

analyse-similar-types-domain: ## Finn typar (types:) med liknande navn innanfor same domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-types-domain) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind types --scope domain --threshold $(SIMILARITY_THRESHOLD) $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))

analyse-similar-types-all: ## Finn typar (types:) med liknande navn på tvers av alle domene [DOMAIN=<domene>] [NAME=<modell>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-types-all) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --kind types --scope all --threshold $(SIMILARITY_THRESHOLD) $(if $(DOMAIN),--domain $(DOMAIN)) $(if $(NAME),--name $(NAME))

analyse-iri-dereferering: ## Testar at alle IRI-ar (id/default_prefix/prefixes) i skjema let seg derefere over HTTP(S) [DOMAIN=<domene>]
	$(call print_header,analyse-iri-dereferering) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/check-iri-resolution.py --check dereferering $(if $(DOMAIN),--domain $(DOMAIN))

analyse-innhaldsforhandling: ## Testar innhaldsforhandling (Accept-header for format/språk) for id/default_prefix-IRI-ar repoet eig [DOMAIN=<domene>]
	$(call print_header,analyse-innhaldsforhandling) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/check-iri-resolution.py --check innhaldsforhandling $(if $(DOMAIN),--domain $(DOMAIN))

analyse-sammendrag: ## Les dei seks analyse-*-rapportfilene og skriv ein konsolidert sammendrag-tabell
	$(call print_header,analyse-sammendrag) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/summarise-modell-analyse.py
