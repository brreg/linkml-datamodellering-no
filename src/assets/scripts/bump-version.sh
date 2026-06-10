#!/usr/bin/env bash
# Bereknar og oppdaterer version:-feltet i ein schema-YAML basert på conventional commits
# sidan siste versjonstagg for modellen. Lagar ny Git-tagg.
#
# Bruk:
#   ./src/assets/scripts/bump-version.sh <modellnamn>
#   ./src/assets/scripts/bump-version.sh ngr-adresse
#   ./src/assets/scripts/bump-version.sh ngr-adresse --dry-run

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

usage() {
  echo "Bruk: $(basename "$0") <modellnamn> [--dry-run]"
  echo ""
  echo "Eksempel:"
  echo "  $(basename "$0") ngr-adresse"
  echo "  $(basename "$0") dcat-ap-no --dry-run"
  exit 1
}

[[ $# -lt 1 ]] && usage

MODEL="$1"
DRY_RUN=false
[[ "${2:-}" == "--dry-run" ]] && DRY_RUN=true

# Finn schema-fil
SCHEMA_FILE=$(find "$REPO_ROOT/src/linkml" -name "${MODEL}-schema.yaml" | head -1)
if [[ -z "$SCHEMA_FILE" ]]; then
  echo "Feil: fann ingen schema-fil for '$MODEL'" >&2
  exit 1
fi

# Les noverande versjon
CURRENT_VERSION=$(grep "^version:" "$SCHEMA_FILE" | head -1 | awk '{print $2}' | tr -d '"')
if [[ -z "$CURRENT_VERSION" ]]; then
  echo "Feil: '$SCHEMA_FILE' manglar version:-felt" >&2
  exit 1
fi

# Normaliser til x.y.z
IFS='.' read -r -a PARTS <<< "$CURRENT_VERSION"
MAJOR="${PARTS[0]:-0}"
MINOR="${PARTS[1]:-0}"
PATCH="${PARTS[2]:-0}"

# Finn siste tagg for denne modellen
LAST_TAG=$(git -C "$REPO_ROOT" tag --list "${MODEL}/v*" --sort=-version:refname | head -1)

if [[ -z "$LAST_TAG" ]]; then
  echo "Ingen tidlegare tagg funne for '$MODEL' — brukar alle commits"
  GIT_RANGE="HEAD"
else
  echo "Siste tagg: $LAST_TAG"
  GIT_RANGE="${LAST_TAG}..HEAD"
fi

# Les commits og bestem bump-nivå
BUMP="none"
while IFS= read -r msg; do
  # BREAKING CHANGE i footer eller !-suffix
  if echo "$msg" | grep -qE "^(feat|fix|refactor|docs|chore)(\([^)]+\))?!:" || \
     echo "$msg" | grep -qE "^BREAKING CHANGE:"; then
    BUMP="major"
    break
  fi
  # feat → minor (viss ikkje allereie major)
  if echo "$msg" | grep -qE "^feat(\([^)]+\))?:" && [[ "$BUMP" != "major" ]]; then
    BUMP="minor"
  fi
  # fix/refactor → patch (viss ikkje allereie minor eller major)
  if echo "$msg" | grep -qE "^(fix|refactor)(\([^)]+\))?:" && [[ "$BUMP" == "none" ]]; then
    BUMP="patch"
  fi
done < <(git -C "$REPO_ROOT" log --pretty=format:"%s" $GIT_RANGE -- \
  "$(dirname "$SCHEMA_FILE")" 2>/dev/null || true)

if [[ "$BUMP" == "none" ]]; then
  echo "Ingen relevante commits funne — ingen versjonsbump nødvendig"
  exit 0
fi

# Berekn ny versjon
case "$BUMP" in
  major) MAJOR=$((MAJOR + 1)); MINOR=0; PATCH=0 ;;
  minor) MINOR=$((MINOR + 1)); PATCH=0 ;;
  patch) PATCH=$((PATCH + 1)) ;;
esac

NEW_VERSION="${MAJOR}.${MINOR}.${PATCH}"
NEW_TAG="${MODEL}/v${NEW_VERSION}"

echo "Bump: $BUMP"
echo "Versjon: $CURRENT_VERSION → $NEW_VERSION"
echo "Tagg: $NEW_TAG"

if $DRY_RUN; then
  echo "(dry-run — ingen endringar gjort)"
  exit 0
fi

# Oppdater version:-felt i schema-YAML
sed -i "s/^version: .*/version: \"${NEW_VERSION}\"/" "$SCHEMA_FILE"
echo "Oppdatert: $SCHEMA_FILE"

# Lag Git-tagg
git -C "$REPO_ROOT" tag "$NEW_TAG"
echo "Tagg oppretta: $NEW_TAG"
