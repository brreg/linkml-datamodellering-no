# Valideringsbadge viser inkonsistent versjon og policy

## Bakgrunn

**Problem:** Etter siste køyring av generate-workflow viser valideringsbadgen "silver 16 feil", men modellen er bumpa til v1.9.0 og valideringsresultatet seier "siste validering: - v.1.8.0 - policy:bronze".

**Observasjonar:**
- `samt-bu-schema.yaml` har `version: "1.9.0"`
- `src/linkml/samt/samt-bu/validation/` har berre `1.0.0/`, `1.0.5/` og `1.8.0/` — ingen `1.9.0/`
- `generated/samt/samt-bu/validation/` finst **ikkje** i det lokale repoet
- Generate-workflow brukte cache for `generated/samt/` (cache-hit)
- Valideringssteg køyrde (linje 307-325) og skreiv til `src/linkml/samt/samt-bu/validation/1.9.0/silver.json`
- Steget "Kopier valideringsloggar til generated/" (linje 327-365) vart **hoppa over** fordi cache-hit var true

**Rotårsak:**

Steget "Kopier valideringsloggar til generated/" (linje 327) har `if: steps.cache-generated.outputs.cache-hit != 'true'`, som tyder at det **berre køyrer dersom cache ikkje vart brukt**. Dette er feil fordi:

1. Valideringssteg køyrer **alltid** (uavhengig av cache) og skriv til `src/linkml/<domain>/<modell>/validation/<version>/<policy>.json`
2. Valideringsloggar ligg i `src/` (ikkje i `generated/`) og er **ikkje** ein del av cache-nykkelen
3. Når cache-hit skjer, vert gamle valideringsloggar (frå cache) brukt i staden for dei nye frå valideringssteget
4. Dokumentasjonsportalen (`mkdocs/publish.sh`) les valideringsloggar frå `generated/<domain>/<modell>/validation/<version>/<policy>.json`
5. Dersom denne katalogen ikkje finst eller inneheld gamle data, viser portalen feil versjon/policy

## Relevante filer

- `.github/workflows/generate.yml` — workflow for generering og publisering
- `src/assets/scripts/makefile/run-validation.sh` — validering-script som skriv til `src/linkml/`
- `mkdocs/publish.sh` — les valideringsloggar frå `generated/` og genererer `index.md`
- `mkdocs/lib/scripts/generate-validation-md.py` — genererer Markdown frå valideringsloggar

## Steg

### 1. Endre `get_validation_json_path()` til å lese frå `generated/` i staden for `src/linkml/`

**Rotårsak (oppdatert):**

`get_validation_json_path()` i `mkdocs/lib/utils/metadata_parsers.sh` les valideringsloggar frå `src/linkml/${domain}/${schema}/validation/${latest_version}/${policy}.json`.

Men i CI:
1. Validering køyrer og skriv til `src/linkml/samt/samt-bu/validation/1.9.0/silver.json` (i CI-runner)
2. Kopiering kopierer til `generated/samt/samt-bu/validation/1.9.0/silver.json`
3. `generated/samt/` vert lasta opp som artifact og slått saman i publish-jobben
4. **`src/linkml/samt/samt-bu/validation/1.9.0/` vert IKKJE commita tilbake til repoet**
5. Publish-jobben køyrer `mkdocs/publish.sh` som les frå `src/linkml/` (som ikkje har v1.9.0)
6. Portalen finn berre den siste versjonen i `src/linkml/`: `1.8.0/bronze.json`

**Løysing:**

Endre `get_validation_json_path()` til å lese frå `generated/` i staden for `src/linkml/`:

**Før:**
```bash
get_validation_json_path() {
    local domain="$1"
    local schema="$2"
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/build.yaml"
    local policy=$(get_validation_policy "$manifest")

    # Bruk alltid src/linkml/.../validation/ som kjelde — både validate.yml
    # og generate.yml lagrar valideringsloggar der
    local src_validation_dir="$REPO_ROOT/src/linkml/${domain}/${schema}/validation"

    local latest_version=$(get_latest_validation_version "$src_validation_dir")
    [ -z "$latest_version" ] && return
    echo "$src_validation_dir/$latest_version/${policy}.json"
}
```

**Etter:**
```bash
get_validation_json_path() {
    local domain="$1"
    local schema="$2"
    local manifest="$REPO_ROOT/src/linkml/${domain}/${schema}/build.yaml"
    local policy=$(get_validation_policy "$manifest")

    # Bruk alltid generated/.../validation/ som kjelde — validate.yml kopierer
    # dit, og generate.yml kopierer dit frå src/linkml/
    local gen_validation_dir="$REPO_ROOT/generated/${domain}/${schema}/validation"

    local latest_version=$(get_latest_validation_version "$gen_validation_dir")
    [ -z "$latest_version" ] && return
    echo "$gen_validation_dir/$latest_version/${policy}.json"
}
```

### 2. Verifiser at valideringsloggar vert kopierte etter cache-hit

Køyr workflow manuelt og sjekk at:
1. Valideringsloggar vert kopierte til `generated/<domain>/<modell>/validation/<version>/` sjølv om cache-hit skjer
2. Dokumentasjonsportalen viser korrekt versjon og policy i valideringsresultat

### 3. Test med samt-bu v1.9.0

```bash
# Trigge workflow manuelt
gh workflow run generate.yml

# Sjekk at valideringsloggar vart kopierte
gh run list --workflow=generate.yml --limit 1
gh run view <run-id> --log | grep "Kopier valideringsloggar"

# Sjekk at generated/samt/samt-bu/validation/1.9.0/ finst i artifact
# (dette kan ikkje testast lokalt — må sjå på publisert portal)
```

## Handlingsliste

- [x] Endre `get_validation_json_path()` til å lese frå `generated/` i staden for `src/linkml/`
- [ ] Test lokalt at portalen finn rett valideringslogg
- [ ] Push endring og trigge workflow manuelt
- [ ] Sjekk publisert portal at versjon og policy stemmer

## Utkast til commit-melding

```
fix(mkdocs): les valideringsloggar frå generated/ i staden for src/
  - mkdocs/lib/utils/metadata_parsers.sh: endre get_validation_json_path() til å lese frå generated/
  - specs/backlog/validering-badge-inkonsistent.md: dokumenter problem, analyse og løysing
```
