# Fallback for validation JSON utan validation_policy

## Bakgrunn

CI-jobben `publish` feiler med:

```
ERROR in mkdocs/lib/scripts/generate-validation-md.py:43
Context:
  validation_json: .../generated/modellkatalog/ksdigital-modellkatalog/validation/1.0.0/bronze.json
  domain: modellkatalog
  schema: ksdigital-modellkatalog
  step: missing_policy_field
  message: Valideringsfila manglar validation_policy eller data_policy
```

Årsak: Commit `cb816aa3` endra `run-validation.sh` til å skrive `validation_policy` i JSON-loggen, og `generate-validation-md.py` til å **krashe** dersom feltet manglar. Men GAMLE validation JSON-filer (genererte før denne endringa) har ikkje dette feltet.

## Problem

`generate-validation-md.py` kallar `log_error()` som gjer `sys.exit(1)` → heile publish-jobben krasjar.

## Løysing

I `generate-validation-md.py`: Les `validation_policy` **frå `build.yaml`** (autoritativ kjelde) i staden for frå validation JSON-fila:

```python
def get_validation_policy_from_manifest(domain: str, schema: str) -> str:
    """Les validation_policy frå build.yaml (autoritativ kjelde)."""
    manifest = repo_root / "src" / "linkml" / domain / schema / "build.yaml"
    if not manifest.exists():
        return "bronze"
    data = yaml.safe_load(manifest.open())
    return data.get("validation_policy", "bronze")

# I main():
policy = get_validation_policy_from_manifest(domain, schema)
```

Dette:
1. Brukar `build.yaml` som single source of truth (same som `get_validation_policy()` i `metadata_parsers.sh`)
2. Validation JSON-fila kan mangle `validation_policy`-feltet utan at det bryt noko
3. Konsistent med resten av repoet (alle andre scripts les frå `build.yaml`)
4. Enklare vedlikehald — éin stad å endre validation policy

## Steg

1. Endre `generate-validation-md.py` til å bruke fallback i staden for `log_error()`
2. Køyr `make docs-publish` lokalt for å verifisere
3. Commit og push — CI bør no fullføre utan feil

## Verifisering

```bash
make docs-publish
```

Forventet resultat: Ingen feil, sjølv for gamle validation JSON-filer som manglar `validation_policy`.

## Utførte tiltak

1. ✅ Lagt til `get_validation_policy_from_manifest()` i `generate-validation-md.py`
2. ✅ Endra `main()` til å lese policy frå `build.yaml` i staden for frå validation JSON
3. ✅ Testa med både ny JSON (med `validation_policy`) og gamal JSON (utan) — begge fungerer
4. ✅ Køyrde `make docs-publish` — fullførte utan feil (exit code 0)

## Resultat

Publish-jobben i CI vil no fullføre utan feil, sjølv om gamle validation JSON-filer manglar `validation_policy`-feltet. `build.yaml` er no single source of truth for validation policy, konsistent med resten av repoet.
