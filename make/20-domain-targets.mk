# ==============================================================================
# make/20-domain-targets.mk
#
# Genererer domain-<domain> targets for kvart domene funne i schema discovery.
# Støttar domenespesifikke pre-hooks via DOMAIN_PRE_<domain>.
# ==============================================================================

# Domenespesifikke pre-hooks — køyrer før standard generering
DOMAIN_PRE_begrepskatalog := gen-begrepskatalog-instance

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
#   Fase 1 (samstundes): validate, gen-jsonld-context, gen-shacl,
#     gen-python, gen-jsonschema, gen-owl, gen-rdf, gen-proto,
#     convert-instance-rdf, gen-schema-docs (doc+erdiagram), gen-plantuml
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
	$$(call print_header,domain-$(1))
	@MAKE="$$(MAKE)" GEN_DIR=$$(GEN_DIR) bash src/assets/scripts/makefile/run-domain-pipeline.sh $(1)
endef

# Generer domain-targets for alle domene
$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))
