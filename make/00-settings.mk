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

ASYNCAPI_IMAGE     := localhost/asyncapi-cli-local:latest
ASYNCAPI_DOCKERFILE := src/assets/containers/Dockerfile.asyncapi-cli

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

# Fargar for logging
CLR_SEP    := $(shell printf '\033[1;33m')
CLR_HDR    := $(shell printf '\033[1;37m')
CLR_STEP   := $(shell printf '\033[0;36m')
CLR_RST    := $(shell printf '\033[0m')

# Separatorlinje
SEP := ************************************************************
