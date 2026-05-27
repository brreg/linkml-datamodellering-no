#!/usr/bin/env bash
# Bootstrap: Legg til LinkML-støtte i eit eksisterande repo.
#
# Bruk:
#   bash bootstrap.sh [ap-no-version]
#   AP_NO_VERSION=v1.0.0 bash bootstrap.sh
#   curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.0.0/bootstrap.sh | bash
#
# Standardversjon er "latest" (alltid siste release).
# For å feste til ein konkret release, send versjonen som argument eller set AP_NO_VERSION.

set -euo pipefail

VERSION="${1:-${AP_NO_VERSION:-latest}}"

# Reusable workflow-ref: @latest er ikkje gyldig i GitHub Actions — bruk @main for flytande versjon
if [ "$VERSION" = "latest" ]; then
    WORKFLOW_REF="main"
else
    WORKFLOW_REF="$VERSION"
fi

echo "→ Bootstrap LinkML (versjon: ${VERSION})"
echo ""

# --- linkml-datamodellering.yaml ---
if [ -f linkml-datamodellering.yaml ]; then
    echo "  linkml-datamodellering.yaml finst allereie — hoppar over."
else
    cat > linkml-datamodellering.yaml << EOF
# Pinnar versjonen av brreg/linkml-datamodellering-no som dette repoet nyttar.
# Oppdater ap-no-version for å oppgradere til ein ny release.
ap-no-version: ${VERSION}
EOF
    echo "  Oppretta linkml-datamodellering.yaml"
fi

# --- .github/workflows/linkml.yml ---
mkdir -p .github/workflows

if [ -f .github/workflows/linkml.yml ]; then
    echo "  .github/workflows/linkml.yml finst allereie — hoppar over."
else
    cat > .github/workflows/linkml.yml << EOF
name: LinkML

on: [push, pull_request]

jobs:
  validate:
    uses: brreg/linkml-datamodellering-no/.github/workflows/reusable-validate.yml@${WORKFLOW_REF}
    with:
      schema: src/linkml/DOMENE/MODELL/MODELL-schema.yaml
      policy: bronze
      # instance: src/linkml/DOMENE/MODELL/examples/MODELL-eksempel.yaml
EOF
    echo "  Oppretta .github/workflows/linkml.yml"
fi

echo ""
echo "Neste steg:"
echo ""
echo "  1. Rediger .github/workflows/linkml.yml:"
echo "     Erstatt 'DOMENE/MODELL/MODELL-schema.yaml' med stien til ditt LinkML-skjema."
echo "     Set policy til bronze/silver/gold etter ønska valideringsnivå."
echo ""
echo "  2. Importer AP-NO-profilene i skjemaet ditt (juster versjon etter behov):"
echo "       imports:"
echo "         - linkml:types"
echo "         - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/${WORKFLOW_REF}/src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema"
echo ""
echo "  3. Commit og push — GitHub Actions køyrer valideringa automatisk."
echo ""
echo "  4. (valfritt) Legg til automatisk oppgradering med Renovate:"
echo "     curl -sSL https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/${WORKFLOW_REF}/renovate.json -o renovate.json"
echo ""
echo "Dokumentasjon: https://linkml.datamodellering.no/ekstern-bruk/"
