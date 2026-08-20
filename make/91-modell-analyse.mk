# ==============================================================================
# make/91-modell-analyse.mk
#
# Analyse på tvers av skjema: liknande klasse-/slotnavn og IRI-resolusjon.
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
        analyse-iri-resolution analyse-sammendrag

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

analyse-iri-resolution: ## Testar at alle IRI-ar (id/default_prefix/prefixes) i skjema resolverer over HTTP(S) [DOMAIN=<domene>]
	$(call print_header,analyse-iri-resolution) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/check-iri-resolution.py $(if $(DOMAIN),--domain $(DOMAIN))

analyse-sammendrag: ## Les dei fem analyse-*-rapportfilene og skriv ein konsolidert sammendrag-tabell
	$(call print_header,analyse-sammendrag) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/summarise-modell-analyse.py
