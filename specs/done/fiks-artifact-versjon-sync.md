# Fiks artifact-versjon-synk i GitHub Actions workflows

## Bakgrunn

CI-jobben `generate / begrepskatalog` feiler med:

```
python3: can't open file '/home/runner/work/linkml-datamodellering-no/linkml-datamodellering-no/.github/scripts/collect-concepts.py': [Errno 2] No such file or directory
make: *** [Makefile:1322: gen-begrepskatalog-instance] Error 2
```

Fila `.github/scripts/collect-concepts.py` finst i repoet og er inkludert i `checkout-source`-steget sitt `upload-artifact@v7`-kall (linje 41 i `generate.yml` inkluderer `.github/`).

**Rotårsak:** `download-artifact@v8` i `generate`-jobben (linje 122) mangla eksplisitt `path: .`-parameter. Utan denne vert artefakten ekstrahert til eit undermappe-namn (basert på artefaktnamn), ikkje til gjeldande katalog. Dette gjer at `.github/scripts/collect-concepts.py` endar opp i feil katalog når `make domain-begrepskatalog` prøver å kjøyre fila.

## Løysing

Legg til `path: .` i `download-artifact@v8`-steget i `generate`-jobben for å sikre at artefakten vert ekstrahert til gjeldande katalog (ikkje undermappe).

## Tiltak

- [x] 1. Legg til `path: .` i `download-artifact@v8` i `generate`-jobben (linje 122-125)

## Utført

Lagt til `path: .` i `download-artifact@v8`-steget i `generate`-jobben (linje 124).

**Endra fil:**
- `.github/workflows/generate.yml`: linje 122-125

**Forklaring:** Utan eksplisitt `path`-parameter ekstraherer `download-artifact@v8` artefakten til ein undermappe med same namn som artefakten (t.d. `source/`), ikkje til gjeldande katalog. Dette gjer at `.github/scripts/collect-concepts.py` endar opp i `source/.github/scripts/` i staden for `.github/scripts/`, og Makefile finn ikkje fila. Med `path: .` vert filstrukturen ekstrahert direkte til gjeldande katalog.
