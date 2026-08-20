#!/usr/bin/env bash
# Fjernar ein domenemodell etter tryggleikssjekkar. Motstykke til new-modell.sh.
# Sjekkar (i rekkjefølgje): submodels-referansar i andre build.yaml (blokkerande),
# imports-referansar frå andre skjema (blokkerande), publish_external/
# published-uris.lock (åtvaring). Utan --confirm gjer scriptet berre ei
# dry-run-oversikt over kva som ville blitt sletta.
# Bruk: bash src/assets/scripts/scaffolding/remove-modell.sh <name> <domain> [--confirm]
set -euo pipefail

NAME="${1:-}"
DOMAIN="${2:-}"
CONFIRM_FLAG="${3:-}"

if [[ -z "$NAME" || -z "$DOMAIN" ]]; then
    echo "Feil: NAME og DOMAIN er påkravde." >&2
    echo "Bruk: make remove-modell DOMAIN=<domene> NAME=<namn> [CONFIRM=1]" >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
SCHEMA_DIR="$REPO_ROOT/src/linkml/$DOMAIN/$NAME"
BUILD_FILE="$SCHEMA_DIR/build.yaml"

if [[ ! -d "$SCHEMA_DIR" ]]; then
    echo "Feil: katalogen $SCHEMA_DIR finst ikkje." >&2
    exit 1
fi

BLOCKING=0

echo "Sjekkar submodels-referansar..."
SUBMODEL_HITS=$(python3 -c "
import glob, yaml
name = '$NAME'
hits = []
for path in glob.glob('$REPO_ROOT/src/linkml/*/*/build.yaml'):
    try:
        with open(path) as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        continue
    if name in (data.get('submodels') or []):
        hits.append(path)
print('\n'.join(hits))
")
if [[ -n "$SUBMODEL_HITS" ]]; then
    echo "  BLOKKERANDE: '$NAME' er lista under submodels: i:" >&2
    echo "$SUBMODEL_HITS" | sed 's/^/    /' >&2
    BLOCKING=1
fi

echo "Sjekkar imports-referansar..."
IMPORT_HITS=$(grep -rlE "${DOMAIN}/${NAME}/${NAME}-schema" \
    --include='*-schema.yaml' "$REPO_ROOT/src/linkml" 2>/dev/null \
    | grep -v "^${SCHEMA_DIR}/" || true)
if [[ -n "$IMPORT_HITS" ]]; then
    echo "  BLOKKERANDE: '$NAME'-schema vert importert av:" >&2
    echo "$IMPORT_HITS" | sed 's/^/    /' >&2
    BLOCKING=1
fi

PUBLISH_WARNING=0
if [[ -f "$BUILD_FILE" ]] && grep -qE '^publish_external:[[:space:]]*true' "$BUILD_FILE"; then
    PUBLISH_WARNING=1
fi
if [[ -f "$SCHEMA_DIR/published-uris.lock" ]]; then
    PUBLISH_WARNING=1
fi
if [[ "$PUBLISH_WARNING" -eq 1 ]]; then
    echo "  ÅTVARING: modellen har publish_external: true og/eller published-uris.lock." >&2
    echo "  Eksterne katalogoppføringar (Felles Datakatalog/Begrepskatalog) vert IKKJE" >&2
    echo "  automatisk fjerna — repoet pushar aldri til eksterne system. Vurder å" >&2
    echo "  deprekere i staden, sjå mkdocs/docs/publisering/publisering-begrep.md" >&2
    echo "  § «Deprekere eit begrep»." >&2
fi

echo ""
echo "Filer som vil bli sletta:"
find "$SCHEMA_DIR" -type f | sort | sed 's/^/  /'

if [[ "$BLOCKING" -eq 1 ]]; then
    echo "" >&2
    echo "Feil: blokkerande referansar funne — rett desse først (sjå over)." >&2
    exit 1
fi

if [[ "$CONFIRM_FLAG" != "--confirm" ]]; then
    echo ""
    echo "Dette var ei førehandsvising (dry-run). Ingen filer er sletta."
    echo "Køyr med CONFIRM=1 for å faktisk slette: make remove-modell DOMAIN=$DOMAIN NAME=$NAME CONFIRM=1"
    exit 0
fi

rm -rf "$SCHEMA_DIR"
echo ""
echo "Sletta: $SCHEMA_DIR"

echo ""
echo "Oppdaterer .github/valid-scopes.txt..."
cd "$REPO_ROOT"
make --no-print-directory gen-valid-scopes
