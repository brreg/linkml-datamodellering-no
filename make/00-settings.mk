# ==============================================================================
# make/00-settings.mk
#
# Statiske variablar og overordna konfigurasjon for byggesystemet.
# ==============================================================================

# Katalogar
GEN_DIR    := generated
SCHEMA_DIR := src/linkml
MCP_DIR    := src/mcp-linkml-validator

# Docker/Podman image-namn og Dockerfile-stiar
LINKML_IMAGE       := localhost/linkml-local:latest
LINKML_DOCKERFILE  := src/assets/containers/Dockerfile.linkml

AVROTIZE_IMAGE     := localhost/avrotize-local:latest
AVROTIZE_DOCKERFILE := src/assets/containers/Dockerfile.avrotize

ASYNCAPI_IMAGE     := localhost/asyncapi-cli-minimal:latest
ASYNCAPI_DOCKERFILE := src/assets/containers/Dockerfile.asyncapi-cli-minimal

DOCS_IMAGE         := localhost/mkdocs-local:latest
DOCS_DOCKERFILE    := src/assets/containers/Dockerfile.mkdocs

PLANTUML_IMAGE     := localhost/plantuml:latest

PYTHON_IMAGE       := localhost/python-pytest:latest
PYTHON_DOCKERFILE  := src/assets/containers/Dockerfile.python

MCP_IMAGE          := mcp-linkml-validator

# Parallellitet
PARALLEL ?= 16

# Valfrie parameter (kan overstyrast frå kommandolinje)
INSTANCE ?=
POLICY   ?=

# Logging
LOGLVL ?= INFO

# Fargar for logging
CLR_SEP    := $(shell printf '\033[1;33m')
CLR_HDR    := $(shell printf '\033[1;37m')
CLR_STEP   := $(shell printf '\033[0;36m')
CLR_OK     := $(shell printf '\033[0;32m')
CLR_ERR    := $(shell printf '\033[0;31m')
CLR_DBG    := $(shell printf '\033[2m')
CLR_RST    := $(shell printf '\033[0m')

# Separatorlinje
SEP := ************************************************************

# Logging-hjelpefunksjonar (bash-snippet som kan sourcas i makroar)
define LOG_FUNCTIONS
log_debug() {
  [[ "$(LOGLVL)" == "DEBUG" ]] && printf "$(CLR_DBG)[DEBUG]$(CLR_RST) %s\n" "$$*" >&2 || true
}
log_info() {
  [[ "$(LOGLVL)" != "ERROR" ]] && printf "%s\n" "$$*" >&2 || true
}
log_error() {
  printf "$(CLR_ERR)[ERROR]$(CLR_RST) %s\n" "$$*" >&2
}
timed_run() {
  local label="$$1"; shift
  local start=$$(date +%s%3N)
  log_debug "→ $$label: $$*"
  "$$@"
  local exit_code=$$?
  local elapsed=$$(( $$(date +%s%3N) - start ))
  if [ $$exit_code -eq 0 ]; then
    log_info "$$(printf '$(CLR_STEP)→ %s$(CLR_RST) (%d.%ds)' "$$label" $$((elapsed / 1000)) $$((elapsed % 1000 / 100)))"
  else
    log_error "$$(printf '%s feila etter %d.%ds (exit code %d)' "$$label" $$((elapsed / 1000)) $$((elapsed % 1000 / 100)) $$exit_code)"
  fi
  return $$exit_code
}
endef
export LOG_FUNCTIONS
