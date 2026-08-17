# CodeQL — fiks for 23 opne varsel

## Bakgrunn

`gh api repos/brreg/linkml-datamodellering-no/code-scanning/alerts` viser 23 opne
CodeQL-varsel (alert #33–#61, alle oppdaga 2026-08-13). Varsla fordeler seg på
9 reglar, dominert av "dødt Python-kodemønster" (ubrukte importar/variablar) og
GitHub Actions-hardening (unpinned actions / usikker checkout). Denne specen
grupperer varsla per regel, med éin konkret fiks per gruppe, slik at kvar
gruppe kan rettast i éin liten, gjennomsiktig commit.

Ingen av varsla er `security_severity_level != null` bortsett frå dei 6
Actions-varsla (alle `medium`). Resten er `note`/kvalitet
(`useless-code`, `maintainability`).

## Grupperingar og fiks

### 1. Ubrukte importar (Python) — `py/unused-import` (7 varsel: #51–#56, #59)

| # | Fil | Linje | Fiern |
|---|---|---|---|
| 59 | `src/assets/scripts/makefile/collect-concepts.py` | 20 | `import yaml` |
| 56 | `src/mcp-linkml-validator/validate-and-log.py` | 19 | `validate_instance` frå `from server import validate_schema, validate_instance` (behald `validate_schema`) |
| 55 | `src/mcp-linkml-begrep-utkast/server.py` | 6 | `import tempfile` |
| 54 | `mkdocs/lib/scripts/parse-dependency-tree.py` | 23 | `Optional` frå `from typing import Dict, List, Set, Optional` |
| 53 | `mkdocs/lib/scripts/generate-validation-md.py` | 12–14 | heile blokka (`sys.path.insert`-kommentar + linje + `from utils.error_handler import log_error`) — `log_error` vert aldri kalla i fila, som alt har eiga inline stderr-handtering |
| 52 | `src/assets/scripts/makefile/generate-modellkatalog.py` | 15 | `Optional` frå `from typing import Dict, List, Optional` |
| 51 | `src/assets/scripts/makefile/generate-informasjonsmodell.py` | 21 | `import glob` (koden brukar `Path.glob()`-metoden, ikkje `glob`-modulet) |

Verifisert med `grep` at ingen av desse namna vert brukt andre stader i respektive fil.

### 2. Ubrukte lokale variablar (Python) — `py/unused-local-variable` (4 varsel: #46–#49)

**`src/assets/scripts/makefile/validate-modelldcat.py`:**
- Linje 30: `schema_view = SchemaView(str(schema_path))` → fjern tildelinga, behald kallet
  (`SchemaView(str(schema_path))`) sidan konstruktøren validerer at skjemaet
  lastar korrekt — sjølve objektet vert aldri lese seinare.
- Linje 34: `loader = YAMLLoader()` → fjern heile linja. Kommentaren på linje
  49–50 stadfestar at `yaml_loader` bevisst er forlate til fordel for manuell
  strukturvalidering, så instansieringa er reint daud kode. Fjern då òg
  importen `from linkml_runtime.loaders.yaml_loader import YAMLLoader` (linje
  25) — han vert ubrukt etter denne endringa og ville elles utløyst eit nytt
  `py/unused-import`-varsel.

**`src/mcp-linkml-validator/validate-and-log.py`:**
- Linje 33 og 36: begge `model = ...`-tildelingane i `extract_metadata()`
  (`model = path_parts[3]` / `model = schema_name`) → fjern begge. Stadfesta
  mot delt referanseimplementasjon `src/assets/scripts/utils/validation_log.py`
  (BUG-12, same feltnamn-krav) at logg-objektet berre skal ha
  `schema`/`domain`/`version` — `model` er ikkje eit forventa felt, og
  returverdien i `extract_metadata()` inkluderer han heller ikkje i dag.

### 3. Ubrukt global variabel — `py/unused-global-variable` (1 varsel: #61)

`src/assets/scripts/utils/linkml_relative_import_patch.py`, funksjonen `apply()`
(linje 206–214): idempotens-mønsteret (`global _patched; if _patched: return; …; _patched = True`)
er eit vanleg CodeQL-falsk-positiv for denne regelen — verdien **vert** lesen
(linje 209), men berre på eit *seinare* kall, noko CodeQL sin per-funksjon
kontrollflyt-analyse ikkje fangar opp som "bruk" av skrivinga på linje 214.

Fiks — erstatt det manuelle flagget med `functools.lru_cache(maxsize=1)`, som
gir same idempotens utan eit modulnivå-flagg CodeQL kan mistolke:

```python
import functools

@functools.lru_cache(maxsize=1)
def apply() -> None:
    """Installer begge patchane. Trygt å kalle fleire gonger (cacha via lru_cache)."""
    _apply_schemaview_patch()
    _apply_mergeutils_patch()
```

Fjern `_patched = False` (linje 60) og `global _patched`-logikken heilt.

### 4. Ubrukte lokale variablar (JavaScript) — `js/unused-local-variable` (2 varsel: #57, #58)

`src/assets/scripts/container/asyncapi-validate.js`:
- Linje 9: `const doc = yaml.load(content);` → `yaml.load(content);` (behald
  kallet for tidleg YAML-syntaksvalidering, dropp den ubrukte bindinga).
- Linje 12: `const { document, diagnostics } = await parser.parse(content);`
  → `const { diagnostics } = await parser.parse(content);` (`document` vert
  aldri lese).

### 5. Print-setning ved import — `py/print-during-import` (1 varsel: #60)

`src/mcp-linkml-validator/server.py`, linje 15–23: `print(..., file=sys.stderr)`
køyrer som sideeffekt når modulet vert importert (t.d. frå
`validate-and-log.py` sin `from server import validate_schema, validate_instance`),
noko CodeQL flaggar som eit anti-mønster uavhengig av straum. Fiks — bruk
`sys.stderr.write(...)` i staden for `print()` (identisk observerbar åtferd,
ingen `print`-kall ved importtidspunkt):

```python
except ImportError:
    sys.stderr.write(
        "ÅTVARING: fann ikkje linkml_relative_import_patch (/repo ikkje montert?) — "
        "versjonslåste importar med fleire nivå relative importar kan feile.\n"
    )
```

### 6. Returverdi frå prosedyre utan returverdi vert brukt — `py/procedure-return-value-used` (1 varsel: #45)

`src/assets/scripts/list-tool-licenses.py`, linje 109–110: `main()` har ingen
`return`-setning (alltid `None`), men vert kalla som `sys.exit(main())`. Fiks
— fjern `sys.exit(...)`-innpakninga sidan skriptet uansett avsluttar med
exitkode 0 ved normal køyring:

```python
if __name__ == "__main__":
    main()
```

### 7. Unøyaktig assert i test — `py/imprecise-assert` (1 varsel: #44)

`tests/test_mcp_linkml_generator.py`, linje 672:

```python
self.assertTrue(len(bronze["description"]) > 0)
```

→

```python
self.assertGreater(len(bronze["description"]), 0)
```

### 8. Usikker checkout i reusable workflows — `actions/untrusted-checkout/medium` (2 varsel: #37, #38)

Flagga steg: "Hent validator-komponenter …" (`reusable-validate.yml`, linje
42) og "Hent make-verktøy …" (`reusable-generate.yml`, linje 61) — begge
sjekkar ut **dette** repoet (`brreg/linkml-datamodellering-no`) på ein
`ref` utleia frå `steps.config.outputs.version`, som igjen kjem frå
`inputs.version` og/eller `linkml-datamodellering.yaml` i det **kallande**
(potensielt lågare-tillit) repoet.

**Reell lakune:** `reusable-generate.yml` har alt eit regex-vakt
(`^(latest|v[0-9]+\.[0-9]+\.[0-9]+)$`, linje 46–50) som avviser ugyldige
versjonsstrengar — men `reusable-validate.yml` manglar tilsvarande vakt heilt
(linje 33–40 skriv `version`-output direkte utan validering). Fiks del A:
speil valideringsblokka frå `reusable-generate.yml` inn i
`reusable-validate.yml`:

```yaml
      - name: Les versjon frå linkml-datamodellering.yaml
        id: config
        run: |
          VERSION="${{ inputs.version }}"
          if [ -z "$VERSION" ] && [ -f linkml-datamodellering.yaml ]; then
            VERSION=$(grep '^ap-no-version:' linkml-datamodellering.yaml | awk '{print $2}')
          fi
          VERSION="${VERSION:-latest}"

          # Tryggleik: avgrens checkout-ref til forventa, stabile verdiar.
          # Tillat berre "latest" eller semver-taggar på forma vMAJOR.MINOR.PATCH.
          if ! echo "$VERSION" | grep -Eq '^(latest|v[0-9]+\.[0-9]+\.[0-9]+)$'; then
            echo "::error::Ugyldig versjon '$VERSION'. Tillatne verdiar er 'latest' eller semver-tag på forma vX.Y.Z."
            exit 1
          fi

          echo "version=$VERSION" >> "$GITHUB_OUTPUT"
```

Fiks del B (begge filer, begge flagga checkout-steg): legg til
`persist-credentials: false`, sidan dei etterfølgjande stega køyrer
scripts/Makefile-mål frå det utsjekka innhaldet og ikkje treng
push-akkreditiv liggjande att i lokal git-konfig:

```yaml
      - name: Hent validator-komponenter frå brreg/linkml-datamodellering-no
        uses: actions/checkout@v7
        with:
          repository: brreg/linkml-datamodellering-no
          ref: ${{ steps.config.outputs.version }}
          persist-credentials: false
          sparse-checkout: |
            …
```

(tilsvarande for `reusable-generate.yml` sitt "Hent make-verktøy"-steg).

**Merk:** `actionlint` skal køyrast mot begge filene etter endringa, jf.
CLAUDE.md § "Actionlint etter CI-endring".

### 9. Ikkje-pinna Action-referansar — `actions/unpinned-tag` (4 varsel: #33–#36)

Berre 3.-parts (ikkje-GitHub-eigde) Actions er flagga — `actions/checkout@v7`
er unnateke sidan det er ein immutable, GitHub-verifisert Action. Fiks: pin
kvar til den dereferensierte commit-SHA-en tag-en peikar til per no, med
versjonsnummer som kommentar (verifisert via `git ls-remote` mot upstream):

| Fil | Linje | Frå | Til |
|---|---|---|---|
| `.github/workflows/validate.yml` | 325 | `peter-evans/create-pull-request@v8` | `peter-evans/create-pull-request@5f6978faf089d4d20b00c7766989d076bb2fc7f1 # v8` |
| `.github/workflows/trivy.yml` | 33 | `aquasecurity/trivy-action@v0.36.0` | `aquasecurity/trivy-action@ed142fd0673e97e23eac54620cfb913e5ce36c25 # v0.36.0` |
| `.github/workflows/trivy.yml` | 56 | `aquasecurity/trivy-action@v0.36.0` | `aquasecurity/trivy-action@ed142fd0673e97e23eac54620cfb913e5ce36c25 # v0.36.0` |
| `.github/workflows/release-please.yml` | 104 | `googleapis/release-please-action@v5` | `googleapis/release-please-action@45996ed1f6d02564a971a2fa1b5860e934307cf7 # v5` |

**Merk:** `actionlint` skal køyrast mot alle tre filene etter endringa, jf.
CLAUDE.md § "Actionlint etter CI-endring". Framtidige Dependabot/Renovate-
oppdateringar av desse tre Actions må oppdatere både SHA **og**
versjonskommentar saman.

## Handlingsliste

- [x] Gruppe 1 — fjern 7 ubrukte Python-importar (sjå tabell over)
- [x] Gruppe 2 — fjern 4 ubrukte lokale variablar i `validate-modelldcat.py`
      og `validate-and-log.py` (inkl. følgje-opprydding av no-ubrukt
      `YAMLLoader`-import)
- [x] Gruppe 3 — erstatt `_patched`-globalflagg med
      `functools.lru_cache(maxsize=1)` i `linkml_relative_import_patch.py`
- [x] Gruppe 4 — fjern 2 ubrukte lokale variablar i `asyncapi-validate.js`
- [x] Gruppe 5 — byt `print()` → `sys.stderr.write()` i `server.py`
- [x] Gruppe 6 — fjern `sys.exit(...)`-innpakning rundt `main()` i
      `list-tool-licenses.py`
- [x] Gruppe 7 — byt `assertTrue(a > b)` → `assertGreater(a, b)` i
      `test_mcp_linkml_generator.py`
- [x] Gruppe 8 — legg til versjonsvakt i `reusable-validate.yml` +
      `persist-credentials: false` på begge flagga checkout-steg; køyr
      `actionlint` mot begge filene
- [x] Gruppe 9 — pin 3 tredjeparts Actions til commit-SHA i `validate.yml`,
      `trivy.yml` (x2) og `release-please.yml`; køyr `actionlint` mot alle tre
- [x] Verifiser at ingen av endringane utløyser nye CodeQL-varsel (spesielt
      gruppe 2 og 5, der fjerning kan gjere andre importar/variablar ubrukte)
      — fann og fiksa eitt følgjefunn: `import sys` vart ubrukt i
      `list-tool-licenses.py` etter gruppe 6-fiksen
- [x] Generer commit-melding og flytt spec til `specs/done/`

## Utført

Alle 9 grupperingar (23 CodeQL-varsel) er retta. Python/JS-syntaks verifisert
med `python3 -m py_compile` og `node --check` for gruppe 1-7. `actionlint`
køyrd mot alle 5 endra workflow-filer for gruppe 8-9 — berre pre-eksisterande
`[shellcheck]`-stilråd att, ingen `[expression]`/syntaksfeil.
