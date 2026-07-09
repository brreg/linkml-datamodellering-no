#!/usr/bin/env bash
# Generer Datamodell-seksjon med lenke til LinkML-schema

set -euo pipefail

generate_datamodell() {
    local domain="$1"
    local schema="$2"

    cat <<EOF

## Datamodell

Kjelde-datamodell i LinkML-format: [\`$schema-schema.yaml\`](../../../src/linkml/$domain/$schema/$schema-schema.yaml)

EOF
}
