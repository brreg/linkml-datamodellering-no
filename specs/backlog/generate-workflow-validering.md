# Generate-workflow: Køyr validering for oppdaterte valideringsresultat i index.md

## Bakgrunn

`mkdocs/publish.sh` genererer `index.md` for kvar modell med ein "Valideringsresultat"-seksjon (via `mkdocs/lib/scripts/generate-validation-md.py`). Denne seksjonen les validerings-JSON frå `src/linkml/<domain>/<schema>/validation/<version>/<policy>.json`.

**Problem:** Når eit skjema vert endra og versjonsnummeret bumpa, finst ikkje valideringsloggar for den nye versjonen enno — dei vert berre oppretta når `validate.yml` køyrer (nattleg kl 02:00 UTC eller via workflow_dispatch). Dette gjer at nye versjonar viser "Valideringsresultat ikkje tilgjengeleg" i dokumentasjonsportalen fram til neste validering.

**Ønskt oppførsel:** `generate.yml` skal køyre validering av kvar modell i `generate`-jobben (per domene) slik at `publish`-jobben alltid har oppdaterte valideringsloggar å inkludere i `index.md`.

## Krav

1. **Ingen PR frå generate-workflow:** `generate.yml` skal **ikkje** committe eller lage PR med valideringsloggar — den skal berre køyre validering i runneren og sørge for at resultata vert inkluderte i `generated/`-artefaktet som `publish`-jobben lastar ned.

2. **Minimal duplikering:** Gjenbruk eksisterande validerings-logikk frå `validate.yml` / `run-validation.sh` / `save-validation-log.py`.

3. **Cache-venleg:** Validering skal berre køyre dersom `cache-generated` missar (same betingelse som `make domain-${{ matrix.domain }}`).

4. **Skalering:** Validering køyrer per domene i parallell (same mønster som generering).

## Design

### Steg 1: Legg til mcp-linkml-validator-image i ensure-images-jobben

`mcp-linkml-validator` er allereie eit bygt image i `validate.yml`, men må leggast til i `ensure-images`-jobben i `generate.yml` for å vere tilgjengeleg for `generate`-jobben.

**Endring:** Utvid `ensure-images.strategy.matrix.image` med:

```yaml
- name: mcp-linkml-validator
  dockerfile: src/mcp-linkml-validator/Dockerfile
  make_target: build-docker-mcp-validator
  hash_files: |
    src/mcp-linkml-validator/Dockerfile
    src/mcp-linkml-validator/requirements.txt
```

### Steg 2: Legg til mcp-linkml-validator i REQUIRED_IMAGES per domene

I `generate`-jobbens "Detekter påkrevde images"-steg (linje ~200), legg til `mcp-linkml-validator` i `REQUIRED_IMAGES`-arrayet (alltid påkrevd, same som `linkml-local`, `python-pytest`, `plantuml`).

**Endring:**

```bash
# Base images som alltid trengs
REQUIRED_IMAGES=("linkml-local" "python-pytest" "plantuml" "mcp-linkml-validator")
```

### Steg 3: Legg til pull-logikk for mcp-linkml-validator

I same steg, i `case "$img" in`-blokka (linje ~260), legg til:

```bash
mcp-linkml-validator)
  pull_image localhost/mcp-linkml-validator:latest \
    "ghcr.io/${{ github.repository_owner }}/mcp-linkml-validator:${{ hashFiles('src/mcp-linkml-validator/Dockerfile', 'src/mcp-linkml-validator/requirements.txt') }}" \
    build-docker-mcp-validator &
  ;;
```

### Steg 4: Køyr validering før generering (nytt steg)

**Før** "Generer alle artefaktar for ${{ matrix.domain }}"-steget (linje ~296), legg til eit nytt steg:

```yaml
- name: Valider alle skjema for ${{ matrix.domain }}
  if: steps.cache-generated.outputs.cache-hit != 'true'
  shell: bash
  run: |
    set -euo pipefail

    echo "=== Validerer skjema for ${{ matrix.domain }} ==="

    # Køyr validering for alle manifest.yaml med generators:-blokk
    for manifest in $(find src/linkml/${{ matrix.domain }} -name manifest.yaml -type f); do
      if grep -q "^generators:" "$manifest"; then
        echo "Validerer skjema frå manifest: $manifest"
        # Bruk same script som validate.yml
        bash src/assets/scripts/ci/run-validation.sh --manifest "$manifest" || {
          echo "::warning::Validering feila for $manifest — held fram"
        }
      fi
    done

    echo "✓ Validering fullført for ${{ matrix.domain }}"
```

**Viktig:** Bruk `|| { echo "::warning::..."; }` i staden for `|| true` for å logge feil utan å stoppe generering.

### Steg 5: Inkluder valideringsloggar i generering

Etter validering (men før generering), treng vi **ikkje** eit separat kopier-steg. I staden skal `make domain-${{ matrix.domain }}` oppdaterast til å automatisk inkludere valideringsloggar frå `src/linkml/<domain>/<schema>/validation/` i `generated/<domain>/<schema>/validation/`.

**Alternativ A (enklare):** Legg til eit kopier-steg **etter** generering:

```yaml
- name: Kopier valideringsloggar til generated/
  if: steps.cache-generated.outputs.cache-hit != 'true'
  run: |
    echo "=== Kopierer valideringsloggar til generated/ ==="

    for schema_dir in src/linkml/${{ matrix.domain }}/*/; do
      if [ ! -d "$schema_dir/validation" ]; then
        continue
      fi

      schema_name=$(basename "$schema_dir")
      target_dir="generated/${{ matrix.domain }}/$schema_name/validation"

      mkdir -p "$target_dir"
      cp -r "$schema_dir/validation"/* "$target_dir/" 2>/dev/null || true

      echo "  ✓ $schema_name: $(find "$target_dir" -name '*.json' | wc -l) validerings-loggar kopierte"
    done
```

**Alternativ (enklare):** Endre `mkdocs/publish.sh` til å lese validerings-loggar frå **både** `src/linkml/<domain>/<schema>/validation/` **og** `generated/<domain>/<schema>/validation/`, med prioritet til `generated/` (nyare).

### Steg 6: Oppdater mkdocs/publish.sh til å prioritere generated/validation/

I `mkdocs/publish.sh` (Steg 5 i heredoc-blokka der `index.md` vert generert), endre logikken for å finne validerings-JSON:

**Før:**
```bash
validation_json="src/linkml/$domain/$schema/validation/$version/$policy.json"
```

**Etter:**
```bash
# Prioriter generated/ (nyare, frå generate-workflow) over src/ (eldre, frå validate-workflow)
if [ -f "generated/$domain/$schema/validation/$version/$policy.json" ]; then
  validation_json="generated/$domain/$schema/validation/$version/$policy.json"
elif [ -f "src/linkml/$domain/$schema/validation/$version/$policy.json" ]; then
  validation_json="src/linkml/$domain/$schema/validation/$version/$policy.json"
else
  validation_json=""
fi
```

Dette sikrar at `publish.sh` alltid brukar den nyaste valideringsloggen — enten frå `generated/` (generert i same workflow-køyring) eller frå `src/` (frå tidlegare `validate.yml`-køyring).

## Konsekvens

Etter denne endringa:

1. **generate-workflow køyrer validering først** (før generering) av alle skjema i parallell (per domene)
2. **Valideringsloggar vert lagra i src/linkml/** (via `save-validation-log.py`)
3. **Valideringsloggar vert kopierte til generated/** etter generering og inkluderte i artefaktet
4. **publish.sh prioriterer generated/validation/** over src/validation/
5. **Nye versjonar får valideringsresultat umiddelbart** i dokumentasjonsportalen (ikkje "Valideringsresultat ikkje tilgjengeleg")
6. **validate-workflow køyrer framleis nattleg** og lagar PR med valideringsloggar til `src/linkml/` (for versjonskontroll)

**Rekkefølgje i generate-jobben:**
1. Last ned source-artefakt (har `src/linkml/` med gamle valideringsloggar)
2. Pull container-images (inkl. `mcp-linkml-validator`)
3. **Køyr validering** (skriv nye loggar til `src/linkml/<domain>/<schema>/validation/`)
4. **Generer artefaktar** (gen-doc, gen-jsonschema osv.)
5. **Kopier valideringsloggar** frå `src/linkml/` til `generated/`
6. Last opp `generated/`-artefakt

## Alternativ vurdert

**Alternativ 1:** Køyr berre validering i `generate`-jobben og fjern valideringsloggar frå `src/linkml/` (ikkje versjonskontrollert).

- **Avvist:** Valideringshistorikk er verdifull for å spoore forbetring over tid. `validate.yml` skal halde fram med å committe loggar til `src/linkml/`.

**Alternativ 2:** Lat `generate`-workflow committe valideringsloggar til `src/linkml/` direkte (utan PR).

- **Avvist:** Dette ville trigge `generate.yml` på nytt i ein loop (via `push`-triggeren).

**Alternativ 3:** Bruk `workflow_run`-trigger for å køyre `validate.yml` etter `generate.yml`.

- **Avvist:** For komplekst, og `publish.sh` vil då måtte vente på at `validate.yml` er ferdig før den kan lese loggane.

## Tiltak

| # | Tiltak | Fil | Prioritet |
|---|---|---|---|
| 1 | Legg til mcp-linkml-validator i ensure-images-jobben | `.github/workflows/generate.yml` | Høg |
| 2 | Legg til mcp-linkml-validator i REQUIRED_IMAGES | `.github/workflows/generate.yml` | Høg |
| 3 | Legg til pull-logikk for mcp-linkml-validator | `.github/workflows/generate.yml` | Høg |
| 4 | Nytt steg: "Valider alle skjema for ${{ matrix.domain }}" | `.github/workflows/generate.yml` | Høg |
| 5 | Nytt steg: "Kopier valideringsloggar til generated/" | `.github/workflows/generate.yml` | Høg |
| 6 | Oppdater mkdocs/publish.sh til å prioritere generated/validation/ | `mkdocs/publish.sh` | Høg |
| 7 | Test lokalt: køyr `make domain-ngr` og sjekk at validation/ vert kopiert | manuell test | Medium |
| 8 | Test i CI: køyr generate-workflow og sjekk at index.md har valideringsresultat | manuell test | Medium |
