#!/usr/bin/env python3
"""Lint og dummy-datasett-validering av genererte LinkML-skjema.

Offentleg API:
  validate_generated(linkml_yaml: str) → dict

Køyrt direkte (python3 validator.py <schema.yaml> [id-prefiks]) skriv modulen
i staden ut eit minimalt dummy-eksempeldatasett for containerklassen i skjemaet,
til bruk som startpunkt for examples/<modell>-eksempel.yaml. Gjenbruker same
_build_dummy_data-logikk som dummy-valideringa over.
"""

import sys
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Placeholder-verdiar per range
# ---------------------------------------------------------------------------

_PLACEHOLDERS: dict = {
    "uriorcurie": "ex:dummy-1",
    "uri":        "https://example.org/dummy",
    "string":     "dummy",
    "integer":    0,
    "int":        0,
    "float":      0.0,
    "double":     0.0,
    "date":       "2024-01-01",
    "datetime":   "2024-01-01T00:00:00",
    "time":       "00:00:00",
    "boolean":    False,
    "bool":       False,
}


def _placeholder(range_str: str) -> object:
    return _PLACEHOLDERS.get(str(range_str).lower(), "dummy")


# ---------------------------------------------------------------------------
# Dummy-datasett-bygging
# ---------------------------------------------------------------------------

def _build_dummy_instance(sv, class_name: str) -> dict:
    """Lagar ein minimal instans av class_name med required-slot fylt ut."""
    instance: dict = {}
    try:
        for slot in sv.class_induced_slots(class_name):
            if slot.required or slot.identifier:
                range_str = str(slot.range or "string")
                # slot.name er ein SlotDefinitionName (linkml_runtime-metamodelltype,
                # ikkje ein rein str) — cast eksplisitt slik at nøklane er trygge å
                # yaml.dump()-e (utan casting fell PyYAML tilbake til
                # !!python/object/new:-serialisering av nøkkelen).
                instance[str(slot.name)] = _placeholder(range_str)
    except Exception as e:
        print(f"ÅTVARING: kunne ikkje byggje dummy-instans for {class_name} — {e}", file=sys.stderr)
    return instance


def _build_dummy_data(sv, container_class: str) -> dict:
    """Lagar dummy-data for containerklassen med éin instans per referert klasse."""
    cls = sv.get_class(container_class)
    data: dict = {}

    for attr_name, attr in (cls.attributes or {}).items():
        range_class = str(attr.range) if attr.range else None
        if not range_class or range_class not in sv.all_classes():
            continue
        instance = _build_dummy_instance(sv, range_class)
        data[attr_name] = [instance] if attr.multivalued else instance

    return data


# ---------------------------------------------------------------------------
# Hovudfunksjon
# ---------------------------------------------------------------------------

def validate_generated(linkml_yaml: str) -> dict:
    """Lint og dummy-validering av eit generert LinkML-skjema.

    Returnerer:
      {
        "lint_issues":      [{"severity": ..., "rule": ..., "message": ...}, ...],
        "dummy_validation": {"valid": bool, "errors": [...], "warnings": [...]}
                            | {"skipped": "<grunn>"}
      }
    """
    lint_issues: list = []

    with tempfile.TemporaryDirectory() as tmp_dir:
        schema_path = str(Path(tmp_dir) / "schema.yaml")
        Path(schema_path).write_text(linkml_yaml, encoding="utf-8")

        # ── Steg A: parse ────────────────────────────────────────────────────
        try:
            from linkml_runtime.utils.schemaview import SchemaView
            sv = SchemaView(schema_path)
        except Exception as exc:
            lint_issues.append({
                "severity": "error",
                "rule": "parse_error",
                "message": str(exc),
            })
            return {
                "lint_issues": lint_issues,
                "dummy_validation": {"skipped": "parse-feil — kan ikkje validere"},
            }

        # ── Steg A: lint ─────────────────────────────────────────────────────
        try:
            from linkml.linter.linter import Linter
            linter = Linter()
            for problem in linter.lint(schema_path):
                level = getattr(problem.level, "value", str(problem.level)).lower()
                lint_issues.append({
                    "severity": level,
                    "rule":     getattr(problem, "rule_name", None) or "linkml_lint",
                    "message":  str(problem.message),
                })
        except Exception as exc:
            lint_issues.append({
                "severity": "error",
                "rule": "linter_error",
                "message": str(exc),
            })

        # ── Steg B: finn containerklasse ─────────────────────────────────────
        container_class = next(
            (n for n, c in sv.all_classes().items() if c.tree_root),
            None,
        )
        if not container_class:
            return {
                "lint_issues": lint_issues,
                "dummy_validation": {
                    "skipped": "Ingen containerklasse (tree_root: true) funne",
                },
            }

        # ── Steg B: bygg og valider dummy-datasett ────────────────────────────
        dummy_data = _build_dummy_data(sv, container_class)

        try:
            from linkml.validator import validate
            report = validate(dummy_data, schema_path, target_class=container_class)
            errors   = [str(r.message) for r in report.results if str(r.severity).endswith("ERROR")]
            warnings = [str(r.message) for r in report.results if str(r.severity).endswith("WARNING")]
            return {
                "lint_issues": lint_issues,
                "dummy_validation": {
                    "valid":    len(errors) == 0,
                    "errors":   errors,
                    "warnings": warnings,
                },
            }
        except Exception as exc:
            return {
                "lint_issues": lint_issues,
                "dummy_validation": {"skipped": f"Valideringsfeil: {exc}"},
            }


# ---------------------------------------------------------------------------
# CLI: skriv ut dummy-eksempeldata for containerklassen i eit LinkML-skjema
# ---------------------------------------------------------------------------

def _main() -> None:
    """Bruk: python3 validator.py <schema.yaml> [id-prefiks]

    Skriv YAML til stdout med éin dummy-instans per containerattributt.
    Med id-prefiks (t.d. 'mittskjema:eksempel') vert identifikator-slot navngjeve
    'id' erstatta med '<prefiks>-<løpenummer>' i staden for den generiske
    placeholder-verdien frå _PLACEHOLDERS — konsistent med
    <navn>:eksempel-N-konvensjonen i examples/<modell>-eksempel.yaml.
    """
    import yaml

    # Skjema med versjonslåst URL-import (t.d. det new-modell.sh set inn for
    # dcat-ap-no) treff BUG-15 (bugs/relativ-import-via-versjonslast-url.md)
    # med mindre denne patchen er brukt før SchemaView vert bygd.
    sys.path.insert(0, "/app/utils")
    try:
        import linkml_relative_import_patch
        linkml_relative_import_patch.apply()
    except ImportError:
        print(
            "ÅTVARING: fann ikkje linkml_relative_import_patch (/app/utils ikkje montert?) — "
            "versjonslåste importar med fleire nivå relative importar kan feile.",
            file=sys.stderr,
        )

    from linkml_runtime.utils.schemaview import SchemaView

    if len(sys.argv) < 2:
        print("Bruk: python3 validator.py <schema.yaml> [id-prefiks]", file=sys.stderr)
        sys.exit(1)

    schema_path = sys.argv[1]
    id_prefix = sys.argv[2] if len(sys.argv) > 2 else None

    sv = SchemaView(schema_path)
    container_class = next(
        (n for n, c in sv.all_classes().items() if c.tree_root),
        None,
    )
    if not container_class:
        print("Feil: fann ikkje containerklasse (tree_root: true) i skjemaet", file=sys.stderr)
        sys.exit(1)

    data = _build_dummy_data(sv, container_class)

    if id_prefix:
        counter = 1
        for value in data.values():
            instances = value if isinstance(value, list) else [value]
            for instance in instances:
                if "id" in instance:
                    instance["id"] = f"{id_prefix}-{counter}"
                    counter += 1

    yaml.dump(data, sys.stdout, allow_unicode=True, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    _main()
