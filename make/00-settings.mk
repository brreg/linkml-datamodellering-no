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
PLANTUML_DOCKERFILE := src/assets/containers/Dockerfile.plantuml

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
CLR_WARN   := $(shell printf '\033[0;33m')
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
# run_logged "<label>" <kommando> [args...] — fangar stdout+stderr frå kommandoen.
# Ved feil: loggar heile den fanga teksten via log_error (synleg på LOGLVL=ERROR)
# saman med exit code og kommandolinja, og returnerer kommandoen sin exit code.
# Ved suksess: fanga output går berre til log_debug (stille som før på INFO/ERROR).
# Finst for å unngå at "cmd > /dev/null 2>&1"-mønsteret kastar vekk stderr, og
# for å unngå at feil midt i ei &&-kjede går forbi ein trap ERR usett (bash sin
# set -e ignorerer feil i alle ledd av ei &&/||-liste utanom det siste — sjå
# specs/done/ingen-stille-feil.md).
run_logged() {
  local label="$$1"; shift
  local output rc
  if output=$$("$$@" 2>&1); then
    rc=0
  else
    rc=$$?
  fi
  if [ $$rc -ne 0 ]; then
    log_error "$$label feila (exit code $$rc) — kommando: $$*"
    [ -n "$$output" ] && log_error "$$output"
    return $$rc
  fi
  # linkml sine gen-*-CLI-kommandoar skriv stundom bokstaveleg "None" til
  # stdout ved suksess (CLI-en sin returverdi frå serialize()) — filtrer
  # vekk denne kjende støykjelda, og hopp over tom output, frå debug-logginga
  if [ -n "$$output" ] && [ "$$output" != "None" ]; then
    log_debug "$$output"
  fi
  return 0
}
endef
export LOG_FUNCTIONS

# Eksportert for src/assets/scripts/makefile/run-parallel-gen.sh (delt
# orkestrering for parallell generering — sjå make/10-generator-macros.mk)
export GEN_DIR
export PARALLEL
export CLR_STEP
export CLR_RST

# Eksportert for frittståande script som ikkje får fargane via Make sin
# tekstsubstitusjon i sjølve recipe-linja (t.d. mkdocs/publish.sh, kalla
# som eit eige script frå make/50-docs.mk, ikkje som embedda $(CLR_*)
# i ei recipe-linje) — unngår at slike script må redeklarere same
# fargeverdiar lokalt
export SEP
export CLR_SEP
export CLR_HDR
export CLR_OK
export CLR_ERR
export CLR_WARN
export CLR_DBG
