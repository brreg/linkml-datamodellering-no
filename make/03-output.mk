# ==============================================================================
# make/03-output.mk
#
# Logging-makroar for konsistent output frå make-target.
# ==============================================================================

# ---------------------------------------------------------------------------
# print_header — skriv separator, header og separator
# ---------------------------------------------------------------------------
# $1=target-namn  $2=valfri tilleggsinfo (t.d. SCHEMA=...)
define print_header
@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
@echo "$(CLR_HDR)*** make $(1)$(if $(2),  $(2))$(CLR_RST)"
@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
endef

# ---------------------------------------------------------------------------
# print_step — skriv steg-melding med farge
# ---------------------------------------------------------------------------
# $1=melding (t.d. "→ gen-jsonschema  ap-no/dcat-ap-no")
define print_step
@echo "$(CLR_STEP)$(1)$(CLR_RST)"
endef
