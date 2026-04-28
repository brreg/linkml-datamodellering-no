#!/usr/bin/env bash
set -euo pipefail

IMAGE="docker.io/linkml/linkml:latest"
PODMAN="podman run --rm -v \"$(pwd):/work\" -w /work -e PYTHONWARNINGS=ignore $IMAGE"
SCHEMA_DIR="src/linkml"
FIXTURE_DIR="tests/fixtures"
PASS=0
FAIL=0

# Lint alle skjema (AP-NO-profiler og domenemodeller)
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

# Valider eksempeldata.
# AP-NO-profiler (utan tree_root) brukar fixture-skjema.
# Domenemodeller (med tree_root) brukar skjemaet direkte.
for example in examples/*-eksempel.yaml; do
  profil=$(basename "$example" .yaml | sed 's/-eksempel$//')
  fixture="$FIXTURE_DIR/$profil-fixture.yaml"
  schema="$SCHEMA_DIR/$profil/$profil-schema.yaml"

  if [ -f "$fixture" ]; then
    valider_schema="$fixture"
  else
    valider_schema="$schema"
  fi

  echo -n "Valider $example ... "
  if eval "$PODMAN linkml validate --schema $valider_schema $example" > /dev/null 2>&1; then
    echo "OK"
    PASS=$((PASS + 1))
  else
    echo "FEIL"
    eval "$PODMAN linkml validate --schema $valider_schema $example" || true
    FAIL=$((FAIL + 1))
  fi
done

echo ""
echo "Resultat: $PASS OK, $FAIL feil"
[ "$FAIL" -eq 0 ]
