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
# - src/assets/scripts/makefile/find-unused-local-definitions.py
# - src/assets/scripts/makefile/check-iri-resolution.py
# - src/assets/scripts/makefile/check-ap-no-reuse.py
# - src/assets/scripts/makefile/check-model-relationships.py
# - src/assets/scripts/makefile/summarise-modell-analyse.py
# ==============================================================================

SIMILARITY_THRESHOLD ?= 0.8

.PHONY: analyse-similar-classes-domain analyse-similar-classes-all \
        analyse-similar-slots-domain analyse-similar-slots-all \
        analyse-similar-types-domain analyse-similar-types-all \
        analyse-similar-domene-batch analyse-similar-alle-domene-batch \
        analyse-ubrukte-slots analyse-ubrukte-enums \
        analyse-ubrukte-types analyse-ubrukte-subsets \
        analyse-isolerte-klasser analyse-ikkje-tilkopla-container \
        analyse-lokal-modellanalyse-domene \
        analyse-iri-dereferering analyse-innhaldsforhandling \
        analyse-ap-no-gjenbruk analyse-modell-sammenhenger analyse-sammendrag

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

analyse-similar-domene-batch: ## Skriv similar-classes/-slots/-types-domain-report.md for alle skjema i domenet, éin kontainar (sjå specs/done/effektiviser-modellanalyse-koyretid.md) [DOMAIN=<domene>] [OUT_DIR=generated] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-domene-batch,DOMAIN=$(DOMAIN)) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --domain $(DOMAIN) --out-dir $(if $(OUT_DIR),$(OUT_DIR),generated) --threshold $(SIMILARITY_THRESHOLD)

analyse-similar-alle-domene-batch: ## Skriv dei tre kombinerte similar-*-all-report.md-filene (--scope all), éin kontainar [OUT_DIR=<sti>] [SIMILARITY_THRESHOLD=0.8]
	$(call print_header,analyse-similar-alle-domene-batch,OUT_DIR=$(OUT_DIR)) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/find-similar-names.py \
	  --out-dir $(OUT_DIR) --threshold $(SIMILARITY_THRESHOLD)

analyse-ubrukte-slots: ## Finn lokalt definerte slots som ikkje er brukt av nokon lokal klasse [SCHEMA=<sti>]
	$(call print_header,analyse-ubrukte-slots,SCHEMA=$(SCHEMA)) 1>&2
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/find-unused-local-definitions.py \
	  --kind slot --schema $(SCHEMA)

analyse-ubrukte-enums: ## Finn lokalt definerte enums som ikkje er brukt av nokon lokal klasse [SCHEMA=<sti>]
	$(call print_header,analyse-ubrukte-enums,SCHEMA=$(SCHEMA)) 1>&2
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/find-unused-local-definitions.py \
	  --kind enum --schema $(SCHEMA)

analyse-ubrukte-types: ## Finn lokalt definerte typar (types:) som ikkje er brukt av nokon lokal klasse [SCHEMA=<sti>]
	$(call print_header,analyse-ubrukte-types,SCHEMA=$(SCHEMA)) 1>&2
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/find-unused-local-definitions.py \
	  --kind type --schema $(SCHEMA)

analyse-ubrukte-subsets: ## Finn lokalt definerte subsets som ikkje er brukt av nokon lokal klasse [SCHEMA=<sti>]
	$(call print_header,analyse-ubrukte-subsets,SCHEMA=$(SCHEMA)) 1>&2
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/find-unused-local-definitions.py \
	  --kind subset --schema $(SCHEMA)

analyse-isolerte-klasser: ## Finn lokale klasser utan referansar til/frå noka anna lokal klasse [SCHEMA=<sti>]
	$(call print_header,analyse-isolerte-klasser,SCHEMA=$(SCHEMA)) 1>&2
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/find-unused-local-definitions.py \
	  --kind class --schema $(SCHEMA)

analyse-ikkje-tilkopla-container: ## Finn lokale klasser som ikkje er nåbare frå containerklassen (tree_root), sjølv om dei er kopla til kvarandre [SCHEMA=<sti>]
	$(call print_header,analyse-ikkje-tilkopla-container,SCHEMA=$(SCHEMA)) 1>&2
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/find-unused-local-definitions.py \
	  --kind unreachable --schema $(SCHEMA)

analyse-lokal-modellanalyse-domene: ## Skriv alle seks ubrukt-lokalt/isolerte-klasser/ikkje-tilkopla-container-rapportane for alle skjema i domenet, éin kontainar (sjå specs/done/effektiviser-modellanalyse-koyretid.md) [DOMAIN=<domene>] [OUT_DIR=generated]
	$(call print_header,analyse-lokal-modellanalyse-domene,DOMAIN=$(DOMAIN)) 1>&2
	@$(LINKML_RUN) python3 src/assets/scripts/makefile/find-unused-local-definitions.py \
	  --domain $(DOMAIN) --out-dir $(if $(OUT_DIR),$(OUT_DIR),generated)

analyse-iri-dereferering: ## Testar at alle IRI-ar (id/default_prefix/prefixes) i skjema let seg derefere over HTTP(S) [DOMAIN=<domene>]
	$(call print_header,analyse-iri-dereferering) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/check-iri-resolution.py --check dereferering $(if $(DOMAIN),--domain $(DOMAIN))

analyse-innhaldsforhandling: ## Testar innhaldsforhandling (Accept-header for format/språk) for id/default_prefix-IRI-ar repoet eig [DOMAIN=<domene>]
	$(call print_header,analyse-innhaldsforhandling) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/check-iri-resolution.py --check innhaldsforhandling $(if $(DOMAIN),--domain $(DOMAIN))

analyse-ap-no-gjenbruk: ## Sjekk at ap-no/*-skjema importerer common-ap-no-schema, og at ingen skjema utanfor ap-no/* importerer det direkte (Digdir-regel 14)
	$(call print_header,analyse-ap-no-gjenbruk) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/check-ap-no-reuse.py

analyse-modell-sammenhenger: ## Kryssreferer importgraf mot modellkatalogen sine har_del/er_i_samsvar_med/er_profil_av/erstatter-annotasjonar (Digdir-regel 12)
	$(call print_header,analyse-modell-sammenhenger) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/check-model-relationships.py

analyse-sammendrag: ## Les analyse-*-rapportfilene og skriv ein konsolidert sammendrag-tabell
	$(call print_header,analyse-sammendrag) 1>&2
	@$(PYTHON_RUN) python3 /work/src/assets/scripts/makefile/summarise-modell-analyse.py
