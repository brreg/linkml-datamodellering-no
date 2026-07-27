# Fiks quickstart.sh til å bruke skjema-spesifikke git-taggar

## Bakgrunn

`mkdocs/lib/sections/quickstart.sh` genererer importdøme i `index.md` for kvar skjema. For AP-NO-skjema brukar den `$version_path` (t.d. `v1.7.0`), men dei korrekte git-taggane er skjema-spesifikke (t.d. `cpsv-ap-no-v1.7.0`, `dcat-ap-no-v2.8.0`).

**Problem:**
```yaml
# Generert (feil)
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/v1.7.0/src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml

# Korrekt
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/cpsv-ap-no-v1.7.0/src/linkml/ap-no/cpsv-ap-no/cpsv-ap-no-schema.yaml
```

**Rotårsak:** `quickstart.sh` linje 24-25 genererer `$version_path` frå `version:`-feltet i skjemaet (`v1.7.0`), men git-taggane følgjer formatet `<schema>-v<version>` (sjå `specs/done/git-tag-validering-schema-versjonar.md`).

## Løysing

Endre `quickstart.sh` til å konstruere skjema-spesifikk tagg når `version`-feltet finst:

```bash
# Før
local version_tag="${version:+v$version}"
local version_path="${version_tag:-main}"

# Etter
local version_tag="${version:+${schema}-v$version}"
local version_path="${version_tag:-main}"
```

Dette gir:
- `cpsv-ap-no` + versjon `1.7.0` → `cpsv-ap-no-v1.7.0`
- `dcat-ap-no` + versjon `2.8.0` → `dcat-ap-no-v2.8.0`
- Skjema utan `version`-felt → `main` (uendra)

## Steg

1. ✅ Endre `mkdocs/lib/sections/quickstart.sh` linje 24
2. ✅ Regenerer dokumentasjon (`make docs-publish`)
3. ✅ Verifiser at `mkdocs/docs/ap-no/cpsv-ap-no/index.md` har korrekt tagg
4. ✅ Verifiser at `mkdocs/docs/ap-no/dcat-ap-no/index.md` har korrekt tagg

## Utført

Endringa er implementert og verifisert:

**Endra fil:**
- `mkdocs/lib/sections/quickstart.sh:24` — endra `local version_tag="${version:+v$version}"` til `local version_tag="${version:+${schema}-v$version}"`

**Verifiserte importdøme:**
- `cpsv-ap-no` → `cpsv-ap-no-v1.8.0` ✅
- `dcat-ap-no` → `dcat-ap-no-v2.11.0` ✅
- `dqv-ap-no` → `dqv-ap-no-v1.13.0` ✅

Alle AP-NO-skjema brukar no skjema-spesifikke git-taggar i importdøma.

## Påverka filer

- `mkdocs/lib/sections/quickstart.sh` — endre `version_tag`-konstruksjon
- `mkdocs/docs/ap-no/*/index.md` — regenerert med korrekte taggar
