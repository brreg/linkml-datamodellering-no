#!/usr/bin/env bash
# Generer publiseringsinfo-boks (seksjon 8 i index.md)
set -euo pipefail

generate_publishing_info() {
    local domain="$1"
    local schema="$2"
    local lock_file="$REPO_ROOT/src/linkml/$domain/$schema/published-uris.lock"

    [ ! -f "$lock_file" ] && return 0

    local ttl_url="https://brreg.github.io/linkml-datamodellering-no/$domain/$schema/$schema.ttl"
    echo ""
    echo "---"
    echo ""
    echo "!!! info \"Publisert til Felles Begrepskatalog\""
    echo "    Denne katalogen er publisert til [data.norge.no/concepts](https://data.norge.no/concepts)"
    echo "    via høstingsendepunkt. Turtle-fila er tilgjengeleg på:"
    echo ""
    echo "    \`${ttl_url}\`"
    echo ""
    echo "    Sjå [Publiser til Felles Begrepskatalog](../../publisering-begrep.md) for rettleiing"
    echo "    om arbeidsflyt, URI-stabilitet og oppsett for nye katalogar."
    echo ""
}
