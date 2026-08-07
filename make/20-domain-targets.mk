# ==============================================================================
# make/20-domain-targets.mk
#
# Genererer domain-<domain> targets for kvart domene funne i schema discovery.
# Støttar domenespesifikke pre-hooks via DOMAIN_PRE_<domain>.
# ==============================================================================

# Domenespesifikke pre-hooks — køyrer før standard generering
DOMAIN_PRE_begrepskatalog := gen-begrepskatalog-instance

# ---------------------------------------------------------------------------
# gen-linkml-convert (eksempel → RDF/Turtle) — batchar via jobs-TSV frå
# convert-examples.sh (sjå Tiltak 4). Frittståande target, slik at
# domain_target kan starte han som ein uavhengig, parallell rekursiv
# $(MAKE)-jobb (sjå run-domain-pipeline.sh, Tiltak «Parallellisering etter
# batching») i staden for å inline logikken direkte i domain_target.
# ---------------------------------------------------------------------------
.PHONY: gen-linkml-convert
gen-linkml-convert: ## Konverter eksempelfiler til RDF/Turtle [DOMAIN=<domain>]
	$(call print_header,gen-linkml-convert,DOMAIN=$(DOMAIN))
	@JOBS_TSV=$$(mktemp "$(GEN_DIR)/.convert-jobs.XXXXXX") && \
	SCHEMA_DIR=$(SCHEMA_DIR) GEN_DIR=$(GEN_DIR) bash src/assets/scripts/makefile/convert-examples.sh $(DOMAIN) > "$$JOBS_TSV" && \
	if [ -s "$$JOBS_TSV" ]; then \
		$(LINKML_RUN) python3 src/assets/scripts/makefile/batch-generate-instances.py --generator convert --jobs-tsv "$$JOBS_TSV"; rc=$$?; \
	else \
		rc=0; \
	fi; \
	rm -f "$$JOBS_TSV"; exit $$rc

# ---------------------------------------------------------------------------
# domain_target — generisk mal for domain-<domain> targets
# ---------------------------------------------------------------------------
# $1 = domain-namn (t.d. ap-no, begrepskatalog, oreg, ...)
#
# Sjølve genereringspipelinen er delegert til
# src/assets/scripts/makefile/run-domain-pipeline.sh, som fase-parallelliserer
# dei uavhengige batch-gruppene (sjå
# specs/backlog/effektiviser-generate-workflow-koyretid.md,
# «Parallellisering etter batching»):
#
#   Fase 1 (samstundes): gen-linkml-merge, gen-jsonld-context, gen-shacl,
#     gen-python, gen-jsonschema, gen-owl, gen-rdf, gen-proto,
#     gen-linkml-convert, gen-docs (doc+erdiagram), gen-plantuml
#   Fase 2 (samstundes, ventar på gen-jsonschema): gen-xsd, gen-openapi,
#     gen-asyncapi (alle les <name>-schema.json)
#   Fase 3 (ventar på ALT): gen-informasjonsmodell-instance (les heile
#     generated/<domain>/<name>/* for finnes_i_format-lista)
#
# Kvart steg er ein rekursiv $(MAKE) <target> DOMAIN=$(1)-kall til eit alt
# eksisterande, sjølvstendig verifisert gen-*-target — scriptet
# reimplementerer ingen podman-/genereringslogikk sjølv, berre
# fase-rekkjefølgje og feilsamling (PID-array + wait, same mønster som
# parallelliser-domene-validering.md).
# ---------------------------------------------------------------------------

define domain_target
_domain_pre_$(1) := $$(DOMAIN_PRE_$(1))

.PHONY: domain-$(1)
domain-$(1): $$(_domain_pre_$(1))
	$$(call print_header,domain-$(1),$$(if $$(filter-out 1,$$(PARALLEL)),(PARALLEL=$$(PARALLEL))))
	@MAKE="$$(MAKE)" GEN_DIR=$$(GEN_DIR) bash src/assets/scripts/makefile/run-domain-pipeline.sh $(1)
endef

# Generer domain-targets for alle domene
$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))
