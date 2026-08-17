#!/usr/bin/env bash
# Generer Datamodell-seksjon med lenke til LinkML-schema

set -euo pipefail
trap 'echo "ERROR in ${BASH_SOURCE[0]}:${LINENO} — command: ${BASH_COMMAND}" >&2; exit 1' ERR

generate_datamodell() {
    local domain="$1"
    local schema="$2"
    # Delmodell-skjema (t.d. dqv-core, modelldcat-katalog) ligg fysisk i
    # FORELDRE-skjemaet sin katalog, ikkje i ein katalog oppkalla etter seg
    # sjølv — PARENT_MODEL er eksportert av publish.sh for slike skjema.
    local source_dir="${PARENT_MODEL:-$schema}"

    cat <<EOF

## Datamodell

> Dette er den autoritative kjelda for modellen. Alle tabellar, diagram og artefakt på denne sida er genererte frå dette skjemaet.

Kjelde-datamodell i LinkML-format: [\`$schema-schema.yaml\`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/$domain/$source_dir/$schema-schema.yaml)

EOF
}
