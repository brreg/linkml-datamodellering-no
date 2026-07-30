# Stabile anker-ID-ar for index.md-seksjoner

**Status:** Utført

## Bakgrunn

Brukar rapporterte at lenkjer til seksjoner frå andre skjema sluttar å fungere når teljinga i overskriftene endrar seg (t.d. `## Enumerations (0)` → `## Enumerations (3)`, `## Avhengigheiter (3)` → `## Avhengigheiter (5)`). MkDocs genererer anker-ID frå heile overskriftsteksten inkludert teljinga, så `#enumerations-0` blir `#enumerations-3` når ein enum vert lagt til.

## Løysing

Bruk Markdown-syntaks `{#custom-id}` (frå `attr_list`-extension) for å legge til stabile anker-ID-ar som er uavhengige av teljing:

```markdown
## Classes (5) {#classes}
## Slots (16) {#slots}
## Enumerations (0) {#enumerations}
## Types (4) {#types}
## Subsets (2) {#subsets}
## Avhengigheiter (3) {#avhengigheiter}
## Generated artifacts (11) {#generated-artifacts}
```

Lenkjer frå andre skjema kan no bruke stabile anker som `#classes`, `#slots`, `#avhengigheiter`, `#generated-artifacts` osv., som fungerer uavhengig av teljing.

## Tiltak

- [x] Aktiver `attr_list`-extension i `mkdocs.yml`
- [x] Oppdater `mkdocs/publish.sh` til å inkludere `attr_list` i generert `mkdocs.yml` (Steg 4)
- [x] Oppdater `mkdocs/lib/sections/classes.sh` til å legge til `{#classes}`, `{#slots}`, `{#enumerations}`, `{#types}`, `{#subsets}`
- [x] Oppdater `mkdocs/lib/sections/avhengigheiter.sh` til å legge til `{#avhengigheiter}`
- [x] Oppdater `mkdocs/lib/sections/generated_artifacts.sh` til å legge til `{#generated-artifacts}`
- [x] Regenerer alle domene med `bash mkdocs/publish.sh`
- [x] Verifiser at lenkjer frå importerte skjema fungerer korrekt

**NB:** `publish.sh` overskriver `mkdocs.yml` i Steg 4, så endringar må gjerast i `publish.sh` sin heredoc-blokk, ikkje direkte i `mkdocs.yml`.

## Verifikasjon

Sjekka at overskrifter har stabile anker i fleire modellar:

```bash
$ grep "^## Classes\|^## Slots" mkdocs/docs/samt/samt-bu/index.md
## Classes (10) {#classes}
## Slots (13) {#slots}

$ grep "Importerte klasser:" mkdocs/docs/samt/samt-bu/index.md
*Importerte klasser: [common-ap-no](../../ap-no/common-ap-no/#classes), [dcat-ap-no](../../ap-no/dcat-ap-no/#classes), [dqv-core](../../ap-no/dqv-core/#classes)*
```

Lenkjer frå `samt-bu` til importerte skjema brukar `#classes`, som no matcher anker-ID i `common-ap-no/index.md` osv.

## Filer endra

- `mkdocs/mkdocs.yml`: lagt til `attr_list` i `markdown_extensions` (regenerert av publish.sh)
- `mkdocs/publish.sh`: lagt til `attr_list` i heredoc-blokk som genererer `mkdocs.yml`
- `mkdocs/lib/sections/classes.sh`: lagt til `{#classes}`, `{#slots}`, `{#enumerations}`, `{#types}`, `{#subsets}`
- `mkdocs/lib/sections/avhengigheiter.sh`: lagt til `{#avhengigheiter}`
- `mkdocs/lib/sections/generated_artifacts.sh`: lagt til `{#generated-artifacts}`

## Testing

```bash
# Test at overskrifter får stabile anker
bash -c '
source mkdocs/lib/sections/classes.sh
export CURRENT_DOMAIN=fint CURRENT_SCHEMA=fint-personvern REPO_ROOT=$(pwd)
generate_classes_section "mkdocs/docs/fint/fint-personvern/klasser/index.md" | grep "^## "
'

# Forventa output:
# ## Classes (5) {#classes}
# ## Slots (16) {#slots}
# ## Enumerations (0) {#enumerations}
# ## Types (4) {#types}
# ## Subsets (2) {#subsets}
```

## Resultat

Med stabile anker-ID-ar vil lenkjer som:
- `[fint-common](../fint-common/#classes)` fungere uavhengig av om `fint-common` har 5 eller 50 klasser
- `[dcat-ap-no](../../ap-no/dcat-ap-no/#avhengigheiter)` fungere uavhengig av om `dcat-ap-no` har 3 eller 10 avhengigheiter
- `[samt-bu](../samt-bu/#generated-artifacts)` fungere uavhengig av antal artefaktar

## Utført

Alle hovudoverskrifter i index.md har no stabile anker-ID-ar:

```bash
$ grep "^## " mkdocs/docs/samt/samt-bu/index.md | grep "{"
## Avhengigheiter (5) {#avhengigheiter}
## Classes (10) {#classes}
## Slots (13) {#slots}
## Enumerations (0) {#enumerations}
## Types (2) {#types}
## Subsets (3) {#subsets}

$ grep "^## Generated artifacts" mkdocs/docs/fint/fint-personvern/index.md
## Generated artifacts (9) {#generated-artifacts}
```

Lenkjer frå andre skjema (t.d. `[common-ap-no](../../ap-no/common-ap-no/#classes)`) fungerer no uavhengig av teljing.

## Utkast til commit-melding

```
feat(mkdocs): legg til stabile anker-ID-ar for hovudoverskrifter i index.md

  - mkdocs/publish.sh: aktiver attr_list-extension i generert mkdocs.yml
  - mkdocs/lib/sections/classes.sh: {#classes}, {#slots}, {#enumerations}, {#types}, {#subsets}
  - mkdocs/lib/sections/avhengigheiter.sh: {#avhengigheiter}
  - mkdocs/lib/sections/generated_artifacts.sh: {#generated-artifacts}
  - mkdocs/mkdocs.yml: regenerert med attr_list
  - Lenkjer frå andre skjema fungerer no uavhengig av teljing i parentesen
```
