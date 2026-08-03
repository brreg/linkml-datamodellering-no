# Fiks validering-cache-invalidering i generate.yml

## Bakgrunn

`make docs-publish` feiler i CI med følgjande feil for 21 skjema:

```
ERROR in mkdocs/lib/scripts/generate-validation-md.py:43
Context:
  validation_json: .../fair/fair-metadata/validation/1.6.0/gold.json
  domain: fair
  schema: fair-metadata
  step: missing_policy_field
  message: Valideringsfila manglar validation_policy eller data_policy
```

**Rotårsak:**

GitHub Actions cachar `generated/<domain>/`-katalogane basert på ein cache-nøkkel som inkluderer:
1. `src/linkml/<domain>/**` — alle skjemafiler
2. `src/assets/containers/Dockerfile.*`, `src/assets/templates/**`, `Makefile` — infrastruktur

Men `src/assets/scripts/ci/run-validation.sh` er **ikkje** inkludert i cache-nøkkelen. Så når `run-validation.sh` endra seg i commit `cb816aa3` (for å skrive `validation_policy`-felt i JSON-loggen), vart ikkje cachen invalidert. CI-en gjenbruker derfor gamle validation JSON-filer frå før `cb816aa3`, som manglar `validation_policy`-feltet.

**Problem:** `generate-validation-md.py` (gamal versjon frå `cb816aa3`) kastar feil dersom `validation_policy`-feltet manglar. Sjølv om `f5073ed7` endra `generate-validation-md.py` til å lese policy frå `build.yaml` i staden, er validation JSON-filene framleis gamle fordi cachen ikkje vart invalidert.

## Løysing

1. **Legg til `src/assets/scripts/**` i cache-nøkkelen** — sikrar at endringar i valideringsskript invaliderer cachen
2. **Bump cache-versjon frå `v3` til `v4`** — tving re-generering av alle artefaktar for alle domene
3. **Gjer `generate-validation-md.py` meir robust** — håndter feil utan å kaste exception dersom JSON-fila manglar felt

## Handlingsliste

- [x] Oppdater `.github/workflows/generate.yml` (linje 200):
  - Legg til `src/assets/scripts/**` i `infra-${{ hashFiles(...) }}`
  - Bump `v3-generated-` til `v4-generated-`
- [x] Oppdater `mkdocs/lib/scripts/generate-validation-md.py`:
  - Bruk `try`/`except` rundt `json.loads()` med betre feilhandtering
  - Skriv ein fallback-seksjon dersom JSON-fila er ugyldig
- [ ] Test lokalt: `make docs-publish` skal fullføre utan feil
- [ ] Push og verifiser at CI køyrer validering på nytt og regenererer validation JSON-filer med `validation_policy`

## Utført

### Endringar

1. `.github/workflows/generate.yml:200`:
   - Cache-versjon bumpa frå `v3` til `v4`
   - `src/assets/scripts/**` lagt til i `infra-${{ hashFiles(...) }}`
   - Sikrar at endringar i `run-validation.sh` invaliderer cachen

2. `mkdocs/lib/scripts/generate-validation-md.py:48-56`:
   - Ny `try`/`except`-blokk med fallback-seksjon dersom JSON-fila er ugyldig
   - Exit utan feil (`sys.exit(0)`) for å ikkje stoppe publish-prosessen
   - Skriv feilmelding til Markdown-output for synlegheit

### Forklaring

**Problem:** GitHub Actions cachar `generated/<domain>/` basert på hashen av `src/linkml/<domain>/**` og infrastruktur-filer, men `src/assets/scripts/ci/run-validation.sh` var **ikkje** inkludert. Så når `run-validation.sh` endra seg (commit `cb816aa3`) for å skrive `validation_policy`-felt i JSON-loggen, vart ikkje cachen invalidert. CI-en gjenbrukte derfor gamle validation JSON-filer som mangla `validation_policy`, og `generate-validation-md.py` (gamal versjon) kasta feil.

**Løysing:** Legg til `src/assets/scripts/**` i cache-nøkkelen og bump versjonen til `v4`. Dette tvingar re-generering av alle validation JSON-filer med det nye formatet.

### Kriteria for fullføring

- [x] Cache-nøkkelen inkluderer `src/assets/scripts/**`
- [x] Cache-versjon bumpa til `v4`
- [x] `generate-validation-md.py` handterer ugyldige JSON-filer utan å kaste feil
- [ ] CI-jobben `generate / <domain>` regenererer alle validation JSON-filer (ikkje cache-treff)
- [ ] `make docs-publish` fullførar utan `ERROR in generate-validation-md.py`
- [ ] Alle skjema har valideringsresultat-seksjon i `mkdocs/docs/<domain>/<schema>/index.md`
