#!/usr/bin/env bash
set -euo pipefail

IMAGE="docker.io/linkml/linkml:latest"
PODMAN="podman run --rm -v \"$(pwd):/work\" -w /work -e PYTHONWARNINGS=ignore $IMAGE"
SCHEMA_DIR="src/linkml"
FIXTURE_DIR="tests/fixtures"
PASS=0
FAIL=0

# Lint AP-NO-profilskjema (src/linkml/ap-no/<profil>/)
for schema in "$SCHEMA_DIR"/ap-no/*/*-schema.yaml; do
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

# Lint NGR-domenemodellskjema (src/linkml/ngr/<modell>/)
for schema in "$SCHEMA_DIR"/ngr/*/*-schema.yaml; do
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

# Lint FINT-domenemodellskjema (src/linkml/fint/<modell>/)
for schema in "$SCHEMA_DIR"/fint/*/*-schema.yaml; do
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

# Lint FAIR-overbygningsskjema (src/linkml/fair/<modell>/)
for schema in "$SCHEMA_DIR"/fair/*/*-schema.yaml; do
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

# Valider AP-NO-eksempeldata mot fixture-skjema (fixture legg til Container/tree_root)
for example in examples/ap-no/*-eksempel.yaml; do
  profil=$(basename "$example" .yaml | sed 's/-eksempel$//')
  fixture="$FIXTURE_DIR/$profil-fixture.yaml"
  echo -n "Valider $example ... "
  if eval "$PODMAN linkml validate --schema $fixture $example" > /dev/null 2>&1; then
    echo "OK"
    PASS=$((PASS + 1))
  else
    echo "FEIL"
    eval "$PODMAN linkml validate --schema $fixture $example" || true
    FAIL=$((FAIL + 1))
  fi
done

# Valider NGR-eksempeldata direkte mot domenemodellskjema (har eigen tree_root)
for example in examples/ngr/*-eksempel.yaml; do
  profil=$(basename "$example" .yaml | sed 's/-eksempel$//')
  schema="$SCHEMA_DIR/ngr/$profil/$profil-schema.yaml"
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

# Valider FINT-eksempeldata direkte mot domenemodellskjema (har eigen tree_root)
for example in examples/fint/*-eksempel.yaml; do
  [ -f "$example" ] || continue
  profil=$(basename "$example" .yaml | sed 's/-eksempel$//')
  schema="$SCHEMA_DIR/fint/$profil/$profil-schema.yaml"
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

# Valider FAIR-eksempeldata mot fixture-skjema (fixture legg til Container/tree_root)
for example in examples/fair/*-eksempel.yaml; do
  [ -f "$example" ] || continue
  profil=$(basename "$example" .yaml | sed 's/-eksempel$//')
  fixture="$FIXTURE_DIR/$profil-fixture.yaml"
  echo -n "Valider $example ... "
  if eval "$PODMAN linkml validate --schema $fixture $example" > /dev/null 2>&1; then
    echo "OK"
    PASS=$((PASS + 1))
  else
    echo "FEIL"
    eval "$PODMAN linkml validate --schema $fixture $example" || true
    FAIL=$((FAIL + 1))
  fi
done

# Valider OREG-eksempeldata mot skjema direkte (har tree_root)
for example in examples/oreg/*-eksempel.yaml; do
  [ -f "$example" ] || continue
  profil=$(basename "$example" .yaml | sed 's/-eksempel$//')
  schema="$SCHEMA_DIR/oreg/$profil/$profil-schema.yaml"
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
