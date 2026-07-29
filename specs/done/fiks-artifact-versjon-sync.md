# Fiks artifact-versjon-synk i GitHub Actions workflows

## Bakgrunn

CI-jobben `generate / begrepskatalog` feiler med:

```
python3: can't open file '/home/runner/work/linkml-datamodellering-no/linkml-datamodellering-no/.github/scripts/collect-concepts.py': [Errno 2] No such file or directory
make: *** [Makefile:1322: gen-begrepskatalog-instance] Error 2
```

Fila `.github/scripts/collect-concepts.py` finst i repoet og er inkludert i `checkout-source`-steget sitt `upload-artifact@v7`-kall (linje 41 i `generate.yml` inkluderer `.github/`).

**Rotårsak:** `generate.yml` og `validate.yml` brukar `upload-artifact@v7` men `download-artifact@v8`. Desse versjonane kan ha ulik filstruktur-handtering, særleg rundt `merge-multiple`-parameteren som endra standardoppførsel i v4.4+.

## Løysing

Oppgrader `upload-artifact` frå `@v7` til `@v8` i alle workflows for å sikre konsistent versjon med `download-artifact@v8`.

## Tiltak

- [x] 1. Oppdater `upload-artifact@v7` → `@v8` i `.github/workflows/generate.yml` (2 stader)
- [x] 2. Oppdater `upload-artifact@v7` → `@v8` i `.github/workflows/validate.yml` (2 stader)
- [x] 3. Oppdater `upload-artifact@v7` → `@v8` i `.github/workflows/trivy.yml` (1 stad)
- [x] 4. Oppdater `upload-artifact@v7` → `@v8` i `.github/workflows/reusable-generate.yml` (1 stad)

## Utført

Alle `upload-artifact@v7`-referansar i `.github/workflows/` er oppdaterte til `@v8` for konsistent versjonering med `download-artifact@v8`. Dette sikrar at filstrukturen vert bevart korrekt når artefaktar vert lasta ned i andre jobbar.

**Endra filer:**
- `.github/workflows/generate.yml`: 2 oppdateringar (checkout-source og generate-artefaktar)
- `.github/workflows/validate.yml`: 2 oppdateringar (checkout-source og validation-logs)
- `.github/workflows/trivy.yml`: 1 oppdatering (SBOM-artefakt)
- `.github/workflows/reusable-generate.yml`: 1 oppdatering (linkml-generated)

**Forklaring:** `actions/upload-artifact@v7` og `actions/download-artifact@v8` kan ha inkompatibilitet rundt filstruktur-handtering (særleg `merge-multiple`-parameteren som endra standardoppførsel i v4.4+). Ved å oppgradere upload til same major-versjon som download, sikrar me at GitHub Actions handterer filstrukturen konsekvent.
