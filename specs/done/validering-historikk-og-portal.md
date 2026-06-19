# Valideringshistorikk og portal-integrering

## Bakgrunn

`make mcp-validate` produserer strukturert JSON til stdout men resultat vert
aldri lagra — kvar CI-køyring startar blankt. To ting manglar:

1. **Historikk**: ingen kan sjå valideringsresultata for ein tidlegare versjon
   av ein modell.
2. **Portal-synlegheit**: ein som les skjemadokumentasjonen i mkdocs-portalen
   veit ikkje om modellen passerer bronze/silver/gold.

Begge problema løysast med same mekanisme: lagra valideringsresultat som JSON
i `validation/` i repoet (ein commit per release), og la `make publish` lese
desse JSON-filene og generere ein Markdown-seksjon i kvar skjema sin `index.md`.

---

## Design

### Katalogstruktur

```
validation/
  <domain>/
    <model>/
      <version>.json   ← éin fil per release, inneheld alle policyresultat
      latest.json      ← kopi av siste versjon (alltid oppdatert)
```

Td: `validation/ngr/ngr-adresse/1.2.0.json` og `validation/ngr/ngr-adresse/latest.json`.

`generated/` er unntatt — valideringshistorikk er **kjeldekode**, ikkje byggoutput.
`make clean` skal ikkje slette `validation/`.

### JSON-format

```json
{
  "schema": "ngr-adresse",
  "domain": "ngr",
  "version": "1.2.0",
  "validated_at": "2026-06-19",
  "data_policy": "silver",
  "result": {
    "valid": true,
    "error_count": 0,
    "warning_count": 3,
    "issues": [
      {"severity": "warning", "code": "all_classes_have_concept_ref",
       "target": "OffisiellAdresse", "message": "..."}
    ]
  }
}
```

`data_policy` speglar `manifest.yaml`-feltet og fortel kva policy som vart
køyrt. `result` kjem direkte frå MCP-serverens JSON-respons
(`result.content[0].text` → `{"valid": ..., "issues": [...]}`).

### Policy-utval per skjema

Scriptet les `data_policy`-feltet frå `manifest.yaml` i same katalog som
skjemaet og køyrer **éin** validering med nøyaktig det policy-namnet:

| `data_policy` i `manifest.yaml` | Policy som vert køyrt |
|---|---|
| (ingen manifest) | `bronze` |
| `bronze` | `bronze` |
| `silver` | `silver` |
| `gold` | `gold` |
| `felles-datakatalog` | `felles-datakatalog` |
| `felles-begrepskatalog` | `felles-begrepskatalog` |

Bronze køyrer ikkje separat for silver/gold-skjema: kvar policy arvar
lågare nivå via `extends:` i policyfila og dekker dermed alle lågare
krav i éin køyring.

`referanse`-skjemaet har ingen `manifest.yaml` → `bronze`.

### Mkdocs-display

`make publish` genererer ein `## Valideringsresultat`-seksjon i kvar skjema
sin `index.md`:

```markdown
## Valideringsresultat

*Siste validering: 2026-06-19 — v1.2.0 — policy: silver*

| Status | Feil | Åtvaringar |
|---|---|---|
| ✅ Godkjent | 0 | 3 |
```

Skjema utan `latest.json` (endå ikkje releasja) viser ei meldinga
«Valideringsresultat ikkje tilgjengeleg — ingen release enno».

---

## CI-flyt

Valideringa køyrer som ein **eigen jobb** (`capture-validation`) i
`release-please.yml`, parallelt med `update-dates`. Begge jobbane
`needs: release-please` og triggar uavhengig av kvarandre.

`capture-validation`-jobben:

1. Hent `mcp-linkml-validator`-image frå GHCR
   (image vert alltid pusha av `validate.yml` før ein release kan oppstå)
2. Køyr `run-schema-validation.py --config release-please-config.json`
   (finn releasja pakkar via manifest-diff, same logikk som `update-dates`)
3. Skriv `validation/<domain>/<model>/<version>.json` og `latest.json`
4. Commit: `chore(*): oppdater valideringsresultat etter release [skip ci]`

Viss ingenting er endra (alle resultat identiske med forrige versjon) → ingen commit.

Alternativ som vart vurdert og forkasta:
- **Steg i `update-dates`**: blandar ansvar — datooppdatering og validering
  er uavhengige operasjonar som bør kunne feile og rekøyrast kvar for seg.
- **Validering på kvar push**: for tung; `validate.yml` dekkjer allereie
  pass/fail for CI. Historikk er mest nyttig per release.
- **GitHub Actions Artifacts**: ikkje persistert lenger enn 90 dagar,
  ikkje tilgjengeleg for mkdocs-generering utan API-kall.

---

## Avhengigheiter

- `release-please.yml` — `update-dates`-jobben (tiltak 3 nedarver frå
  `auto-datoannotasjonar-release.md`)
- `mkdocs/publish.sh` — utvida med validering-seksjon (tiltak 4)
- `flatten-and-validate.bash` — leverandør av JSON-resultata (urørt)

---

## Tiltak

| # | Tiltak | Omfang | Prioritet | Status |
|---|---|---|---|---|
| 1 | Lag `src/assets/scripts/run-schema-validation.py` | 1 script | Høg | ✓ Skrive; les `data_policy` frå manifest via regex, stdlib-only |
| 2 | Legg til `make validate-capture` i `Makefile` | 1 target | Høg | ✓ Lagt til etter `mcp-validate`; auto-build av image; SCHEMA-override |
| 3 | Ny jobb `capture-validation` i `release-please.yml` | 1 workflow-jobb | Høg | ✓ Parallelt med `update-dates`; pull frå GHCR; commit til `validation/` |
| 4 | Lag `src/assets/scripts/generate-validation-md.py` | 1 script | Medium | ✓ Skrive; `<details>`-blokk for feil; stdlib-only |
| 5 | Utvid `mkdocs/publish.sh` | 1 publish.sh-seksjon | Medium | ✓ Kall per skjema i `process_schema()`; fallback-melding ved manglande JSON |

## Utført

- **Tiltak 1**: `run-schema-validation.py` — hentar policy frå `manifest.yaml` via regex (`^data_policy:`), same manifest-diff-logikk som `update-schema-dates.py`, skriv `validation/<domain>/<model>/<version>.json` og `latest.json`.
- **Tiltak 2**: `validate-capture`-target i Makefile — auto-build av `mcp-linkml-validator`-image; støttar `SCHEMA=`-override for enkeltskjema.
- **Tiltak 3**: Ny jobb `capture-validation` i `release-please.yml` — parallelt med `update-dates`, `needs: release-please`, pull image frå GHCR, commit til `validation/` med `[skip ci]`.
- **Tiltak 4**: `generate-validation-md.py` — genererer tabell + kollapsa `<details>`-blokk for feil; åtvaringar berre talt; `<details>` utelaten ved 0 feil.
- **Tiltak 5**: `mkdocs/publish.sh` `process_schema()` — kallar `generate-validation-md.py` per skjema; viser «ikkje tilgjengeleg»-melding for skjema utan `latest.json`.

### Implementeringsnotat for tiltak 1

`run-schema-validation.py` gjenbrukar `find_released_packages()`-mønsteret
frå `update-schema-dates.py` for å finne skjemafiler frå `release-please-config.json`.

Kallsekvens per skjema og policy:

```python
result = subprocess.run(
    ["bash", "src/mcp-linkml-validator/flatten-and-validate.bash",
     str(schema_path), policy],
    capture_output=True, text=True
)
policy_result = json.loads(result.stdout)
```

Scriptet les `data_policy`-feltet frå `manifest.yaml` i same katalog som
skjemaet. Manglande manifest, eller manifest utan `data_policy`-felt → `bronze`.

```python
def get_policy(schema_path: Path) -> str:
    manifest = schema_path.parent / "manifest.yaml"
    if manifest.exists():
        m = yaml.safe_load(manifest.read_text())
        return m.get("data_policy", "bronze")
    return "bronze"
```

CLI-grensesnitt:

```
python3 run-schema-validation.py --config release-please-config.json
python3 run-schema-validation.py --schema src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml
python3 run-schema-validation.py --dry-run
```

### Implementeringsnotat for tiltak 2

```makefile
validate-capture:
    @test -n "$(SCHEMA)" && \
        python3 src/assets/scripts/run-schema-validation.py --schema $(SCHEMA) || \
        python3 src/assets/scripts/run-schema-validation.py --config release-please-config.json
```

### Implementeringsnotat for tiltak 3

Ny jobb `capture-validation` i `release-please.yml`, parallelt med `update-dates`:

```yaml
capture-validation:
  needs: release-please
  if: ${{ needs.release-please.outputs.releases_created == 'true' }}
  runs-on: ubuntu-22.04
  permissions:
    contents: write
  steps:
    - uses: actions/checkout@v6
      with:
        ref: main
        fetch-depth: 2
        token: ${{ secrets.GITHUB_TOKEN }}

    - name: Hent mcp-validator-image frå GHCR
      run: |
        IMAGE=ghcr.io/${{ github.repository_owner }}/mcp-linkml-validator:${{
          hashFiles('src/mcp-linkml-validator/Dockerfile',
                    'src/mcp-linkml-validator/requirements.txt') }}
        podman pull "$IMAGE"
        podman tag "$IMAGE" mcp-linkml-validator

    - name: Fang valideringsresultat
      run: python3 src/assets/scripts/run-schema-validation.py \
             --config release-please-config.json

    - name: Commit og push valideringsresultat
      run: |
        git config user.name "github-actions[bot]"
        git config user.email "github-actions[bot]@users.noreply.github.com"
        if ! git diff --quiet; then
          git add validation/
          git commit -m "chore(*): oppdater valideringsresultat etter release [skip ci]"
          git push
        else
          echo "Ingen endringar å committe"
        fi
```

`update-dates`-jobben er urørt.

### Implementeringsnotat for tiltak 4

`generate-validation-md.py <latest.json>` → Markdown til stdout.

Tabellen viser ✅/❌ basert på `valid`-feltet, antal feil og åtvaringar.
Issues med `severity: error` listast i ein kollapsa `<details>`-blokk under
tabellen — same mønster som «LinkML Source»-seksjonen i portalen:

```markdown
## Valideringsresultat

*Siste validering: 2026-06-19 — v1.2.0 — policy: silver*

| Status | Feil | Åtvaringar |
|---|---|---|
| ❌ Ikkje godkjent | 2 | 1 |

<details>
<summary>Feil (2)</summary>

```
schema_has_annotation_utgiver: schema — schema.annotations.utgiver manglar
schema_has_annotation_status: schema — schema.annotations.status manglar
```

</details>
```

Kvar feil-linje har forma `<code>: <target> — <message>`, henta direkte frå
`issue`-objekta i JSON-resultatet. Åtvaringar vert ikkje lista ut — berre
talt i tabellen. Dersom det ikkje er nokon feil, vert `<details>`-blokka utelaten.

### Implementeringsnotat for tiltak 5

I `publish.sh`, etter at artefaktlista er generert for kvart skjema:

```bash
VALIDATION_JSON="validation/${domain}/${model}/latest.json"
if [ -f "$VALIDATION_JSON" ]; then
    python3 src/assets/scripts/generate-validation-md.py "$VALIDATION_JSON" \
        >> "mkdocs/docs/${domain}/${model}/index.md"
fi
```
