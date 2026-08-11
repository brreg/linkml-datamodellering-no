# Fiks validate-workflow-feil for brreg-begrepskatalog

## Bakgrunn

`make validate-data DOMAIN=begrepskatalog` feila i CI (validate.yml) med to
blokkerande feil og tre åtvaringar for `brreg-begrepskatalog`:

```
error   schema_declares_standard_prefix   Ingen standard vokabularprefiks deklarert (skos)
error   schema_declares_standard_prefix   Ingen standard vokabularprefiks deklarert (dct)
warning missing_recommended_metadata      class:BegrepContainer manglar description
warning instance_begrep_missing_language_definisjon  aksjeklasser manglar nn
warning instance_begrep_missing_language_definisjon  foretaksnavn manglar nn
```

I tillegg feila loggen med ein separat, urelatert infrastrukturfeil etter
sjølve valideringsfeilen: `save-validation-log.py` (køyrt i
python-pytest-kontaineren via `PYTHON_RUN`) prøvde å pulle
`localhost/python-pytest:latest` som eit ekte registry og feila med
`connection refused`.

### Årsaksanalyse

1. **Prefiks-feilen**: `_check_schema_declares_standard_prefix` i
   `src/mcp-linkml-validator/server.py` sjekka berre `sv.schema.prefixes`
   — prefiks deklarert lokalt i skjemaet sin eigen `prefixes:`-blokk.
   Prefiks som kjem inn transitivt via eit importert skjema (her:
   `skos:`/`dct:` frå `skos-ap-no-schema`) vart ikkje talde med, sjølv om
   dei reelt sett er tilgjengelege og brukt. Bruvarslinja spesifiserte at
   dette skulle rettast i sjølve sjekken (ikkje ved å duplisere
   prefiks-deklarasjonar lokalt i kvart skjema som importerer).
2. **nn-åtvaringane**: `instance_begrep_definisjon_language_coverage`
   krev at `har_definisjon`-lista har minst éin URI med `-nb`- og éin med
   `-nn`-suffiks (reint ID-suffiks-basert sjekk, ingen faktisk
   `Definisjon`-objekt vert dereferert). `aksjeklasser` og `foretaksnavn`
   (kjelde: `src/linkml/oreg/begrepssamling-foretaksregisteret/begrep/`)
   hadde berre `-nb`. `nestleder.yaml` har alt `-nb`/`-nn`/`-en` og er
   malen for korrekt struktur.
3. **python-pytest-biletfeilen**: `.github/workflows/validate.yml` sitt
   `checkout-source`-steg bygde `images`-outputen frå ei hardkoda liste
   `["linkml-local","mcp-linkml-validator"]`, i staden for å slå opp
   `always_required: true` i `src/assets/containers/images.json`
   (autoritativ kjelde — jf. `generate.yml` sitt tilsvarande steg, som
   allereie gjer dette rett). `python-pytest` er `always_required: true`
   i manifestet (`save-validation-log.py` køyrer i denne kontaineren via
   `PYTHON_RUN` frå `validate-bronze`/`validate-data`/`validate-examples`),
   men vart aldri pulla i validate.yml — difor prøvde podman å pulle han
   frå eit ekte registry og feila.

## Steg

1. **`src/mcp-linkml-validator/server.py`**: Endra
   `_check_schema_declares_standard_prefix` til å kalle
   `sv.imports_closure()` og sjekke `sv.namespaces()` (merga prefiks frå
   heile import-treet) i staden for `schema.prefixes` (berre lokalt
   skjema).
2. **`tests/test_mcp_policies.py`**: Ny test
   `test_fair_i2_transitivt_importert_standard_prefiks_godtatt` som
   verifiserer at eit skjema som importerer `linkml:types` (og dermed får
   `xsd:`-prefikset transitivt) ikkje lenger utløyser `fair_i2`.
3. **`src/linkml/oreg/begrepssamling-foretaksregisteret/begrep/{aksjeklasser,foretaksnavn}.yaml`**:
   La til `-nn`-suffiksert URI i `har_definisjon`, same mønster som
   `nestleder.yaml`.
4. **`src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml`**:
   Regenerert via `make gen-begrepskatalog-instance` (fila er
   CI-generert, skal ikkje redigerast manuelt).
5. **`src/linkml/begrepskatalog/brreg-begrepskatalog/brreg-begrepskatalog-schema.yaml`**:
   La til `description` på `BegrepContainer` (fjerna siste åtvaringa,
   trivielt).
6. **`.github/workflows/validate.yml`**: `checkout-source` sitt
   "Bygg image-liste og tag-oppslag for validering"-steg slår no opp
   `always_required`-images dynamisk frå `images.json` (som
   `generate.yml`) i staden for å hardkode dei to. La til
   `python-pytest`-oppføring i `image_tags`-JSON-en, med same
   `hashFiles()`-input som `generate.yml` brukar (for at GHCR-taggen skal
   matche mellom dei to workflowane og unngå unødvendig rebuild).

## Verifisering

- `make mcp-linkml-valider-modell-test`: alle testar grøne bortsett frå
  ei allereie eksisterande, urelatert feiling
  (`TestGold.test_gyldig_skjema_har_ingen_feil` — `_GOLD_PASS`-fixturen
  manglar slots for `dct:accessRights`/`dcatap:applicableLegislation` som
  gold-policyen no krev; reproduserer identisk på uendra `main`, ikkje
  route av dette arbeidet).
- `make validate-data DOMAIN=begrepskatalog`: `{"valid": true,
  "errorCount": 0, "warningCount": 0, "issues": []}`.
- `make lint SCHEMA=.../brreg-begrepskatalog-schema.yaml`: 9 pre-eksisterande
  åtvaringar (manglande `description` på containerattributt) — urelatert
  til denne feilen, ikkje del av oppgåva.
- `make validate-examples DOMAIN=begrepskatalog`: OK.
- `actionlint` på `validate.yml`: berre `[shellcheck]`-funn (stilråd,
  ingen `[expression]`-feil).

## Kjent, urelatert feil (ikkje retta her)

`TestGold.test_gyldig_skjema_har_ingen_feil` i `tests/test_mcp_policies.py`
feilar alt på uendra `main` (`_GOLD_PASS`-fixturen manglar
`dct:accessRights`/`dcatap:applicableLegislation`-slots for `Datasett`
som gold-policyen krev). Utanfor scope for denne spesifikasjonen.

## Utført

Alle steg gjennomførte og verifiserte som skildra ovanfor. Sjå Verifisering-
seksjonen for testresultat.
