# Parallelisering av validate.yml

## Situasjon

19 skjema vert validerte sekvensielt. Kvart skjema køyrer to Podman-kontainerinstansar:
1. `docker.io/linkml/linkml:latest` — flattar ut importar (`gen-linkml --mergeimports`)
2. `mcp-linkml-validator` — køyrer policy-sjekk

Wall-time i dag ≈ 19 × (tid per skjema). Dei er heilt uavhengige av kvarandre.

---

## Forslag: to-lags jobb-graf

```
build-validator

validate-ap-no ┐
validate-fair  │
validate-fint  │  ← alle needs: build-validator
validate-ngr   │
validate-oreg  │
validate-samt  ┘
```

Kvar domenejobb validerer sine skjema sekvensielt internt — parallelismen er på jobb-nivå.

`mcp-linkml-validator`-imaget vert bygt éin gong og delt via workflow-artefakt.  
`docker.io/linkml/linkml:latest` vert henta direkte frå Docker Hub i kvar jobb (ingen byggesteg).

---

## Implementasjon

Gjentakne steg er trekte ut til ein composite action:

```
.github/actions/validate-domain/action.yml   ← éin gong
.github/workflows/validate.yml               ← kaller action med domain-input
```

### `.github/workflows/validate.yml`

```yaml
name: Validate

on:
  push:
    branches: [main]
  pull_request:

jobs:

  build-validator:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - name: Bygg mcp-linkml-validator
        run: make mcp-val-build
      - name: Lagre image som artefakt
        run: podman save mcp-linkml-validator | gzip > mcp-linkml-validator.tar.gz
      - uses: actions/upload-artifact@v4
        with:
          name: mcp-linkml-validator-image
          path: mcp-linkml-validator.tar.gz
          retention-days: 1

  validate-ap-no:
    needs: build-validator
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: ./.github/actions/validate-domain
        with:
          domain: ap-no

  validate-fair:
    needs: build-validator
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: ./.github/actions/validate-domain
        with:
          domain: fair

  # … same mønster for fint, ngr, oreg, samt
```

### `.github/actions/validate-domain/action.yml`

Tek `domain` som input og køyrer:
1. Last ned og load validator-image
2. Valider alle skjema i domenet mot bronze-policy
3. Valider eksempelfiler mot skjema (berre skjema med `tree_root: true`)

---

## Tidlegare forslag (for referanse)

```yaml
  validate-ap-no:
    needs: build-validator
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: mcp-linkml-validator-image
      - name: Last inn validator-image
        run: podman load < <(gunzip -c mcp-linkml-validator.tar.gz)
      - name: Valider ap-no mot bronze-policy
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            echo "--- $schema ---"
            result=$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$schema" bronze 2>/dev/null)
            echo "$result"
            if ! SCHEMA="$schema" python3 -c "import json,sys,os;d=json.loads(sys.stdin.read());s=os.environ.get('SCHEMA','');[print('::{} file={}::{}: {}'.format('error' if i.get('severity')=='error' else 'warning',s,i.get('target',''),i.get('message','').replace(chr(10),' '))) for i in d.get('issues',[])];sys.exit(0 if d.get('valid',True) else 1)" <<< "$result"; then
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/ap-no -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort)
          exit $FAILED
      - name: Valider eksempelfiler mot skjema
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            name=$(basename "$schema" -schema.yaml)
            example="examples/ap-no/$name-eksempel.yaml"
            if [ ! -f "$example" ]; then
              echo "::warning file=$schema::Ingen eksempelfil funne: $example"
              continue
            fi
            echo "--- $schema ---"
            result=$(podman run --rm -v "$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
              docker.io/linkml/linkml:latest linkml validate --schema "$schema" "$example" 2>&1)
            echo "$result"
            if echo "$result" | grep -q "\[ERROR\]"; then
              echo "$result" | grep "\[ERROR\]" | while IFS= read -r line; do
                echo "::error file=$example::$(echo "$line" | sed 's/\[ERROR\] //')"
              done
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/ap-no -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
            | grep -v common | sort | xargs grep -l "tree_root: true")
          exit $FAILED

  validate-fair:
    needs: build-validator
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: mcp-linkml-validator-image
      - name: Last inn validator-image
        run: podman load < <(gunzip -c mcp-linkml-validator.tar.gz)
      - name: Valider fair mot bronze-policy
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            echo "--- $schema ---"
            result=$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$schema" bronze 2>/dev/null)
            echo "$result"
            if ! SCHEMA="$schema" python3 -c "import json,sys,os;d=json.loads(sys.stdin.read());s=os.environ.get('SCHEMA','');[print('::{} file={}::{}: {}'.format('error' if i.get('severity')=='error' else 'warning',s,i.get('target',''),i.get('message','').replace(chr(10),' '))) for i in d.get('issues',[])];sys.exit(0 if d.get('valid',True) else 1)" <<< "$result"; then
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/fair -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort)
          exit $FAILED
      - name: Valider eksempelfiler mot skjema
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            name=$(basename "$schema" -schema.yaml)
            example="examples/fair/$name-eksempel.yaml"
            if [ ! -f "$example" ]; then
              echo "::warning file=$schema::Ingen eksempelfil funne: $example"
              continue
            fi
            echo "--- $schema ---"
            result=$(podman run --rm -v "$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
              docker.io/linkml/linkml:latest linkml validate --schema "$schema" "$example" 2>&1)
            echo "$result"
            if echo "$result" | grep -q "\[ERROR\]"; then
              echo "$result" | grep "\[ERROR\]" | while IFS= read -r line; do
                echo "::error file=$example::$(echo "$line" | sed 's/\[ERROR\] //')"
              done
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/fair -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
            | grep -v common | sort | xargs grep -l "tree_root: true")
          exit $FAILED

  validate-fint:
    needs: build-validator
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: mcp-linkml-validator-image
      - name: Last inn validator-image
        run: podman load < <(gunzip -c mcp-linkml-validator.tar.gz)
      - name: Valider fint mot bronze-policy
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            echo "--- $schema ---"
            result=$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$schema" bronze 2>/dev/null)
            echo "$result"
            if ! SCHEMA="$schema" python3 -c "import json,sys,os;d=json.loads(sys.stdin.read());s=os.environ.get('SCHEMA','');[print('::{} file={}::{}: {}'.format('error' if i.get('severity')=='error' else 'warning',s,i.get('target',''),i.get('message','').replace(chr(10),' '))) for i in d.get('issues',[])];sys.exit(0 if d.get('valid',True) else 1)" <<< "$result"; then
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/fint -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort)
          exit $FAILED
      - name: Valider eksempelfiler mot skjema
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            name=$(basename "$schema" -schema.yaml)
            example="examples/fint/$name-eksempel.yaml"
            if [ ! -f "$example" ]; then
              echo "::warning file=$schema::Ingen eksempelfil funne: $example"
              continue
            fi
            echo "--- $schema ---"
            result=$(podman run --rm -v "$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
              docker.io/linkml/linkml:latest linkml validate --schema "$schema" "$example" 2>&1)
            echo "$result"
            if echo "$result" | grep -q "\[ERROR\]"; then
              echo "$result" | grep "\[ERROR\]" | while IFS= read -r line; do
                echo "::error file=$example::$(echo "$line" | sed 's/\[ERROR\] //')"
              done
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/fint -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
            | grep -v common | sort | xargs grep -l "tree_root: true")
          exit $FAILED

  validate-ngr:
    needs: build-validator
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: mcp-linkml-validator-image
      - name: Last inn validator-image
        run: podman load < <(gunzip -c mcp-linkml-validator.tar.gz)
      - name: Valider ngr mot bronze-policy
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            echo "--- $schema ---"
            result=$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$schema" bronze 2>/dev/null)
            echo "$result"
            if ! SCHEMA="$schema" python3 -c "import json,sys,os;d=json.loads(sys.stdin.read());s=os.environ.get('SCHEMA','');[print('::{} file={}::{}: {}'.format('error' if i.get('severity')=='error' else 'warning',s,i.get('target',''),i.get('message','').replace(chr(10),' '))) for i in d.get('issues',[])];sys.exit(0 if d.get('valid',True) else 1)" <<< "$result"; then
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/ngr -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort)
          exit $FAILED
      - name: Valider eksempelfiler mot skjema
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            name=$(basename "$schema" -schema.yaml)
            example="examples/ngr/$name-eksempel.yaml"
            if [ ! -f "$example" ]; then
              echo "::warning file=$schema::Ingen eksempelfil funne: $example"
              continue
            fi
            echo "--- $schema ---"
            result=$(podman run --rm -v "$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
              docker.io/linkml/linkml:latest linkml validate --schema "$schema" "$example" 2>&1)
            echo "$result"
            if echo "$result" | grep -q "\[ERROR\]"; then
              echo "$result" | grep "\[ERROR\]" | while IFS= read -r line; do
                echo "::error file=$example::$(echo "$line" | sed 's/\[ERROR\] //')"
              done
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/ngr -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
            | grep -v common | sort | xargs grep -l "tree_root: true")
          exit $FAILED

  validate-oreg:
    needs: build-validator
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: mcp-linkml-validator-image
      - name: Last inn validator-image
        run: podman load < <(gunzip -c mcp-linkml-validator.tar.gz)
      - name: Valider oreg mot bronze-policy
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            echo "--- $schema ---"
            result=$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$schema" bronze 2>/dev/null)
            echo "$result"
            if ! SCHEMA="$schema" python3 -c "import json,sys,os;d=json.loads(sys.stdin.read());s=os.environ.get('SCHEMA','');[print('::{} file={}::{}: {}'.format('error' if i.get('severity')=='error' else 'warning',s,i.get('target',''),i.get('message','').replace(chr(10),' '))) for i in d.get('issues',[])];sys.exit(0 if d.get('valid',True) else 1)" <<< "$result"; then
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/oreg -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort)
          exit $FAILED
      - name: Valider eksempelfiler mot skjema
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            name=$(basename "$schema" -schema.yaml)
            example="examples/oreg/$name-eksempel.yaml"
            if [ ! -f "$example" ]; then
              echo "::warning file=$schema::Ingen eksempelfil funne: $example"
              continue
            fi
            echo "--- $schema ---"
            result=$(podman run --rm -v "$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
              docker.io/linkml/linkml:latest linkml validate --schema "$schema" "$example" 2>&1)
            echo "$result"
            if echo "$result" | grep -q "\[ERROR\]"; then
              echo "$result" | grep "\[ERROR\]" | while IFS= read -r line; do
                echo "::error file=$example::$(echo "$line" | sed 's/\[ERROR\] //')"
              done
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/oreg -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
            | grep -v common | sort | xargs grep -l "tree_root: true")
          exit $FAILED

  validate-samt:
    needs: build-validator
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: mcp-linkml-validator-image
      - name: Last inn validator-image
        run: podman load < <(gunzip -c mcp-linkml-validator.tar.gz)
      - name: Valider samt mot bronze-policy
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            echo "--- $schema ---"
            result=$(bash src/mcp-linkml-validator/flatten-and-validate.bash "$schema" bronze 2>/dev/null)
            echo "$result"
            if ! SCHEMA="$schema" python3 -c "import json,sys,os;d=json.loads(sys.stdin.read());s=os.environ.get('SCHEMA','');[print('::{} file={}::{}: {}'.format('error' if i.get('severity')=='error' else 'warning',s,i.get('target',''),i.get('message','').replace(chr(10),' '))) for i in d.get('issues',[])];sys.exit(0 if d.get('valid',True) else 1)" <<< "$result"; then
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/samt -mindepth 2 -maxdepth 2 -name '*-schema.yaml' | grep -v common | sort)
          exit $FAILED
      - name: Valider eksempelfiler mot skjema
        run: |
          set +e
          FAILED=0
          while IFS= read -r schema; do
            name=$(basename "$schema" -schema.yaml)
            example="examples/samt/$name-eksempel.yaml"
            if [ ! -f "$example" ]; then
              echo "::warning file=$schema::Ingen eksempelfil funne: $example"
              continue
            fi
            echo "--- $schema ---"
            result=$(podman run --rm -v "$PWD:/work" -w /work -e PYTHONWARNINGS=ignore \
              docker.io/linkml/linkml:latest linkml validate --schema "$schema" "$example" 2>&1)
            echo "$result"
            if echo "$result" | grep -q "\[ERROR\]"; then
              echo "$result" | grep "\[ERROR\]" | while IFS= read -r line; do
                echo "::error file=$example::$(echo "$line" | sed 's/\[ERROR\] //')"
              done
              FAILED=$((FAILED + 1))
            fi
          done < <(find src/linkml/samt -mindepth 2 -maxdepth 2 -name '*-schema.yaml' \
            | grep -v common | sort | xargs grep -l "tree_root: true")
          exit $FAILED
```

---

## Merknadar

**`find src/linkml/<domain> -mindepth 2 -maxdepth 2`** — kvar jobb søkjer berre i sitt eige domene i staden for heile `src/linkml/`.

**`docker.io/linkml/linkml:latest`** vert henta direkte frå Docker Hub i kvar jobb — imaget vert ikkje bygt og treng ikkje delast som artefakt.

**`fail-fast`** er ikkje relevant her sidan jobbane er eksplisitt definerte — alle køyrer alltid til endes uavhengig av kvarandre.

**Ny domene** krev å kopiere ein `validate-<domene>`-jobb og byte domenenamnet.
