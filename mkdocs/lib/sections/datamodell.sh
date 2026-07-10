#!/usr/bin/env bash
# Generer Datamodell-seksjon med lenke til LinkML-schema

set -euo pipefail

generate_datamodell() {
    local domain="$1"
    local schema="$2"

    cat <<EOF

## Datamodell

Kjelde-datamodell i LinkML-format: [\`$schema-schema.yaml\`](https://github.com/brreg/linkml-datamodellering-no/blob/main/src/linkml/$domain/$schema/$schema-schema.yaml)

EOF
}
