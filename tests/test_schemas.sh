#!/usr/bin/env bash
set -euo pipefail

IMAGE="docker.io/linkml/linkml:latest"
PODMAN="podman run --rm -v \"$(pwd):/work\" -w /work $IMAGE"
SCHEMA_DIR="src/linkml"
PASS=0
FAIL=0

for schema in "$SCHEMA_DIR"/*/*-schema.yaml; do
  echo -n "Lint $schema ... "
  if eval "$PODMAN linkml lint --ignore-warnings $schema" > /dev/null 2>&1; then
    echo "OK"
    PASS=$((PASS + 1))
  else
    echo "FEIL"
    eval "$PODMAN linkml lint --ignore-warnings $schema" || true
    FAIL=$((FAIL + 1))
  fi
done

for example in examples/*-eksempel.yaml; do
  profil=$(basename "$example" .yaml | sed 's/-eksempel$//')
  schema="$SCHEMA_DIR/$profil/$profil-schema.yaml"
  class=$(grep -m1 '^id:' "$example" | sed 's|.*||' || echo "")
  echo -n "Valider $example ... "
  if eval "$PODMAN linkml validate --schema $schema $example" > /dev/null 2>&1; then
    echo "OK"
    PASS=$((PASS + 1))
  else
    echo "FEIL"
    eval "$PODMAN linkml validate --schema $schema $example" || true
    FAIL=$((FAIL + 1))
  fi
done

echo ""
echo "Resultat: $PASS OK, $FAIL feil"
[ "$FAIL" -eq 0 ]
