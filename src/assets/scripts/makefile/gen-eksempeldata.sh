#!/usr/bin/env bash
# Genererer eit rikt syntetisk eksempeldatasett frå eit LinkML-skjema, via
# same validator.py::_build_example_data-generator som new-modell.sh brukar
# internt for examples/<modell>-eksempel.yaml. Sjå specs/done/
# gen-eksempeldata-fra-skjema.md.
#
# Bruk: gen-eksempeldata.sh <schema.yaml> [out-fil] [id-prefiks] [overwrite]
#   <schema.yaml>  påkravd — sti til *-schema.yaml
#   [out-fil]      valfri — skriv til fil i staden for stdout
#   [id-prefiks]   valfri — jf. <navn>:eksempel-N-konvensjonen
#   [overwrite]    valfri — "1" for å tillate overskriving av eksisterande out-fil
#
# Miljøvariablar:
#   SCHEMA_REPO_ROOT  valfri — repoet skjemaet ligg i, monterast read-only for
#                     å løyse relative importar. Default: næraste git-rot for
#                     skjemafila (fungerer difor også for eit skjema i eit
#                     anna, t.d. eksternt, repo — ikkje berre dette repoet).
#   LINKML_GEN_IMAGE  valfri — image-namn/-tag for mcp-linkml-modell-utkast.
#                     Default: lokalbygd "mcp-linkml-modell-utkast".
set -euo pipefail

SCHEMA_PATH="${1:-}"
OUT_FILE="${2:-}"
ID_PREFIX="${3:-}"
OVERWRITE="${4:-}"

if [[ -z "$SCHEMA_PATH" ]]; then
    echo "Feil: SCHEMA er påkravd." >&2
    echo "Bruk: make gen-eksempeldata SCHEMA=<sti> [OUT=<sti>] [ID_PREFIX=<prefiks>] [OVERWRITE=1]" >&2
    exit 1
fi

if [[ ! -f "$SCHEMA_PATH" ]]; then
    echo "Feil: fann ikkje skjemafil $SCHEMA_PATH" >&2
    exit 1
fi

if [[ -n "$OUT_FILE" && -f "$OUT_FILE" && "$OVERWRITE" != "1" ]]; then
    echo "Feil: $OUT_FILE finst allereie — set OVERWRITE=1 for å overskrive." >&2
    exit 1
fi

# TOOL_REPO_ROOT: kor sjølve mcp-linkml-modell-utkast-verktøyet (kjeldekode
# og/eller lokalbygd image) bur — alltid dette repoet, uavhengig av kvar
# skjemaet ligg.
TOOL_REPO_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
LINKML_GEN_DIR="$TOOL_REPO_ROOT/src/mcp-linkml-modell-utkast"
LINKML_GEN_IMAGE="${LINKML_GEN_IMAGE:-mcp-linkml-modell-utkast}"
SCHEMA_ABS="$(cd "$(dirname "$SCHEMA_PATH")" && pwd)/$(basename "$SCHEMA_PATH")"

# SCHEMA_REPO_ROOT: repoet skjemaet sjølv ligg i — monterast read-only slik
# at relative importar til søskenskjema løysest (t.d. dqv-ap-no frå
# dcat-ap-no). Treng IKKJE vere dette repoet: default er næraste git-rot for
# skjemafila, slik at scriptet også kan peikast mot eit skjema i eit anna
# (t.d. eksternt) repo — set SCHEMA_REPO_ROOT eksplisitt for å overstyre.
SCHEMA_REPO_ROOT="${SCHEMA_REPO_ROOT:-$(cd "$(dirname "$SCHEMA_ABS")" && git rev-parse --show-toplevel 2>/dev/null || true)}"
if [[ -z "$SCHEMA_REPO_ROOT" ]]; then
    echo "Feil: fann ikkje noko git-repo for $SCHEMA_PATH, og SCHEMA_REPO_ROOT er ikkje sett eksplisitt." >&2
    exit 1
fi

case "$SCHEMA_ABS" in
    "$SCHEMA_REPO_ROOT"/*) SCHEMA_REL="${SCHEMA_ABS#"$SCHEMA_REPO_ROOT"/}" ;;
    *)
        echo "Feil: $SCHEMA_PATH ligg utanfor SCHEMA_REPO_ROOT ($SCHEMA_REPO_ROOT) — kan ikkje monterast." >&2
        exit 1
        ;;
esac

# Monterer heile repoet (skrivebeskytta), ikkje berre éi skjemafil — skjema
# med relative importar til søskendomene (t.d. dqv-ap-no frå dcat-ap-no) kan
# elles ikkje løyse importane sine. Same mønster som LINKML_RUN/WORK_MOUNT
# (make/01-containers.mk) brukar for validate-instance.
#
# Monterer src/assets/scripts/utils/ slik at validator.py kan bruke
# linkml_relative_import_patch (BUG-15/bugs/relativ-import-via-versjonslast-url.md)
# — utan den feilar SchemaView på versjonslåste importar (t.d. dcat-ap-no).
EXAMPLE_DATA=$(podman run -i --rm \
      -v "$LINKML_GEN_DIR/server.py:/app/server.py:ro" \
      -v "$LINKML_GEN_DIR/converter.py:/app/converter.py:ro" \
      -v "$LINKML_GEN_DIR/validator.py:/app/validator.py:ro" \
      -v "$LINKML_GEN_DIR/profiles:/app/profiles:ro" \
      -v "$TOOL_REPO_ROOT/src/assets/scripts/utils:/app/utils:ro" \
      -v "$SCHEMA_REPO_ROOT:/work:ro" \
      "$LINKML_GEN_IMAGE" \
      python3 /app/validator.py "/work/$SCHEMA_REL" "$ID_PREFIX") || {
    echo "Feil: eksempelgenerering feila for $SCHEMA_PATH" >&2
    exit 1
}

if [[ -z "$EXAMPLE_DATA" ]]; then
    echo "Feil: eksempelgenerering returnerte tomt resultat for $SCHEMA_PATH" >&2
    exit 1
fi

if [[ -n "$OUT_FILE" ]]; then
    printf '%s\n' "$EXAMPLE_DATA" > "$OUT_FILE"
    echo "Skrive til: $OUT_FILE"
else
    printf '%s\n' "$EXAMPLE_DATA"
fi
