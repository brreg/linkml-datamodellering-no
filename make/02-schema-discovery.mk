# ==============================================================================
# make/02-schema-discovery.mk
#
# Automatisk oppdaging av schema og domenar.
#
# Skjema følgjer mønsteret: src/linkml/<domain>/<dir>/<name>-schema.yaml
# Merk: <name> kan vere forskjellig frå <dir> (t.d. dqv-core-schema.yaml i dqv-ap-no/).
# ==============================================================================

# Finn alle skjema automatisk
SCHEMAS := $(shell find $(SCHEMA_DIR) -mindepth 3 -maxdepth 3 -name '*-schema.yaml' | sort)

# Hjelpefunksjonar for å ekstrahere metadata frå skjema-stiar
# $1 = skjema-sti (t.d. src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml)

# Ekstraher domene (3. komponent i stien)
schema_domain = $(word 3,$(subst /, ,$(1)))

# Ekstraher skjemanamn (katalognamn, ikkje filnamn)
schema_name = $(notdir $(patsubst %/,%,$(dir $(1))))

# Generer output-katalog for eit skjema
schema_outdir = $(GEN_DIR)/$(call schema_domain,$(1))/$(call schema_name,$(1))

# Generer unik nøkkel for eit skjema (brukt i config.mk)
schema_key = $(subst -,_,$(call schema_domain,$(1)))_$(subst -,_,$(call schema_name,$(1)))

# Domenar vert automatisk avleidde frå oppdaga skjema
DOMAINS := $(sort $(foreach s,$(SCHEMAS),$(call schema_domain,$(s))))

# Hjelpefunksjon: bestem kva skjema som skal prosesserast basert på DOMAIN eller SCHEMA
# Returnerer liste av skjema-stiar
define get_target_schemas
$(if $(SCHEMA),$(SCHEMA),$(if $(DOMAIN),$(filter src/linkml/$(DOMAIN)/%,$(SCHEMAS)),$(SCHEMAS)))
endef
