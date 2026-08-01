# Validation-katalogstruktur opprydding

## Bakgrunn

PR #47 introduserte validering i generate-workflow, men valideringsloggane vert lagra i feil katalogstruktur. `run-validation.sh` genererer `domain` og `model` frå schema-stien med `basename`, som feiltolkar einivå-stiar (`src/linkml/<modell>`) og tolkar `linkml` som domenenivået.

**Faktisk situasjon:**
- `src/linkml/register-over-aksjeeiere/validation` (gammal struktur — utan domenenivå)
- `src/linkml/oreg/register-over-aksjeeiere/validation` (riktig struktur — med domenenivå)

**Problem:**
1. `run-validation.sh` linje 99-103 brukar `basename "$(dirname "$schema_dir")"` for å finne domain — dette fungerer berre for todelte stiar (`linkml/<domain>/<modell>`), ikkje éindelte (`linkml/<modell>`)
2. Alle skjema under `src/linkml/<modell>` (utan domene-nivå) får `domain=linkml`, som er feil
3. Duplikate validation-katalogar ligg att frå tidlegare generate-køyringar

## Mål

1. Fjern alle duplikate validation-katalogar direkte under `src/linkml/<modell>/`
2. Fiks `run-validation.sh` til å tolke schema-stien riktig (sjekk om stien er `linkml/<domain>/<modell>` eller `linkml/<modell>`, og tolk deretter)
3. Verifiser at generate-workflow genererer loggane i riktig katalog

## Steg

### 1. Fjern duplikate validation-katalogar

Alle validation-katalogar direkte under `src/linkml/<modell>/` skal fjernast — desse er duplikat av loggane i `src/linkml/<domain>/<modell>/validation`:

```bash
# Finn alle validation-katalogar direkte under linkml (maxdepth 2)
find src/linkml -maxdepth 2 -type d -name validation

# Slett desse — dei skal no liggje under src/linkml/<domain>/<modell>/validation
```

**Liste over katalogar som skal fjernast:**
- `src/linkml/brreg-begrepskatalog/validation` → finst i `src/linkml/begrepskatalog/brreg-begrepskatalog/validation`
- `src/linkml/brreg-modellkatalog/validation` → finst i `src/linkml/modellkatalog/brreg-modellkatalog/validation`
- `src/linkml/cpsv-ap-no/validation` → finst i `src/linkml/ap-no/cpsv-ap-no/validation`
- `src/linkml/dcat-ap-no/validation` → finst i `src/linkml/ap-no/dcat-ap-no/validation`
- `src/linkml/digdir-modellkatalog/validation` → finst i `src/linkml/modellkatalog/digdir-modellkatalog/validation`
- `src/linkml/dqv-ap-no/validation` → finst i `src/linkml/ap-no/dqv-ap-no/validation`
- `src/linkml/enhetsregisteret-bvrinn/validation` → finst i `src/linkml/oreg/enhetsregisteret-bvrinn/validation`
- `src/linkml/fair-metadata/validation` → finst i `src/linkml/fair/fair-metadata/validation`
- `src/linkml/fint-administrasjon/validation` → finst i `src/linkml/fint/fint-administrasjon/validation`
- `src/linkml/fint-arkiv/validation` → finst i `src/linkml/fint/fint-arkiv/validation`
- `src/linkml/fint-okonomi/validation` → finst i `src/linkml/fint/fint-okonomi/validation`
- `src/linkml/fint-personvern/validation` → finst i `src/linkml/fint/fint-personvern/validation`
- `src/linkml/fint-ressurs/validation` → finst i `src/linkml/fint/fint-ressurs/validation`
- `src/linkml/fint-utdanning/validation` → finst i `src/linkml/fint/fint-utdanning/validation`
- `src/linkml/kartverket-modellkatalog/validation` → finst i `src/linkml/modellkatalog/kartverket-modellkatalog/validation`
- `src/linkml/ksdigital-modellkatalog/validation` → finst i `src/linkml/modellkatalog/ksdigital-modellkatalog/validation`
- `src/linkml/modelldcat-ap-no/validation` → finst i `src/linkml/ap-no/modelldcat-ap-no/validation`
- `src/linkml/ngr-adresse/validation` → finst i `src/linkml/ngr/ngr-adresse/validation`
- `src/linkml/ngr-eiendom/validation` → finst i `src/linkml/ngr/ngr-eiendom/validation`
- `src/linkml/ngr-person/validation` → finst i `src/linkml/ngr/ngr-person/validation`
- `src/linkml/ngr-virksomhet/validation` → finst i `src/linkml/ngr/ngr-virksomhet/validation`
- `src/linkml/novari-modellkatalog/validation` → finst i `src/linkml/modellkatalog/novari-modellkatalog/validation`
- `src/linkml/register-over-aksjeeiere/validation` → finst i `src/linkml/oreg/register-over-aksjeeiere/validation`
- `src/linkml/samt-bu/validation` → finst i `src/linkml/samt/samt-bu/validation`
- `src/linkml/skatteetaten-modellkatalog/validation` → finst i `src/linkml/modellkatalog/skatteetaten-modellkatalog/validation`
- `src/linkml/skos-ap-no/validation` → finst i `src/linkml/ap-no/skos-ap-no/validation`
- `src/linkml/xkos-ap-no/validation` → finst i `src/linkml/ap-no/xkos-ap-no/validation`

### 2. Fiks `run-validation.sh`

Endre linje 99-106 i `src/assets/scripts/ci/run-validation.sh`:

```bash
# Finn domain og modell frå schema-sti
# Eksempel:
#   src/linkml/samt/samt-bu/samt-bu-schema.yaml → domain=samt, model=samt-bu
#   src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml → domain=ngr, model=ngr-adresse
schema_dir=$(dirname "$SCHEMA")
model=$(basename "$schema_dir")

# Sjekk om schema_dir har tre nivå (linkml/<domain>/<modell>) eller to (linkml/<modell>)
parent_dir=$(dirname "$schema_dir")
parent_name=$(basename "$parent_dir")

if [ "$parent_name" = "linkml" ]; then
  # To-nivå-struktur: linkml/<modell> (skal ikkje skje lenger, men handter det)
  echo "Åtvaring: Schema ligg direkte under linkml/ utan domenenivå: $SCHEMA" >&2
  domain="$model"  # Bruk modellnamn som domain (fallback)
else
  # Tre-nivå-struktur: linkml/<domain>/<modell>
  domain="$parent_name"
fi

# Rekn ut loggsti (co-location)
log_path="$schema_dir/validation/$VERSION/$POLICY.json"

echo "→ Validerer $domain/$model (v$VERSION) med policy: $POLICY" >&2
```

### 3. Verifiser at generate-workflow fungerer

Køyr generate-workflow for eit domene (t.d. `oreg`) og verifiser at loggane hamnar i riktig katalog:

```bash
# Køyr generate-workflow for oreg (lokalt, dersom mogleg)
# Eller vent på neste CI-køyring og sjekk:
ls -la src/linkml/oreg/register-over-aksjeeiere/validation/
ls -la generated/oreg/register-over-aksjeeiere/validation/

# Sjekk at det IKKJE finst logg i gamal struktur:
ls -la src/linkml/register-over-aksjeeiere/validation/ 2>/dev/null && echo "FEIL: Gamal struktur finst framleis!"
```

## Handlingsliste

- [x] Fjern alle duplikate validation-katalogar direkte under `src/linkml/<modell>/`
- [x] Fiks `run-validation.sh` til å tolke schema-stien riktig
- [ ] Verifiser at generate-workflow genererer loggane i riktig katalog (køyrer i CI)

## Utført

**Steg 1: Fjern duplikate validation-katalogar**
- Fjerna alle 27 duplikate validation-katalogar direkte under `src/linkml/<modell>/`
- Bekrefta at alle validation-katalogar no ligg i riktig tre-nivå-struktur: `src/linkml/<domain>/<modell>/validation`

**Steg 2: Fiks `run-validation.sh`**
- Endra linje 99-106 i `src/assets/scripts/ci/run-validation.sh` til å tolke schema-stien riktig:
  - Sjekkar om `parent_name` er `linkml` (to-nivå-struktur) eller eit domenenamn (tre-nivå-struktur)
  - Sett `domain` til `parent_name` dersom tre-nivå-struktur, elles fallback til `model`
- Verifisert med `bash src/assets/scripts/ci/run-validation.sh --manifest src/linkml/oreg/register-over-aksjeeiere/build.yaml`:
  - Output viser `→ Validerer oreg/register-over-aksjeeiere (v1.6.0) med policy: bronze` — riktig domain/model-tolking

**Steg 3: Verifiser generate-workflow**
- Neste CI-køyring vil verifisere at generate-workflow genererer loggane i riktig katalog
- Kopierings-steget i `.github/workflows/generate.yml` (linje 332-344) er uendra — det kopierer frå `src/linkml/${{ matrix.domain }}/*/validation` til `generated/${{ matrix.domain }}/$schema_name/validation`, som er riktig
