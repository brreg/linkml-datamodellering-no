#!/usr/bin/env python3
"""Lint og dummy-datasett-validering av genererte LinkML-skjema.

Offentleg API:
  validate_generated(linkml_yaml: str) → dict
"""

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
                instance[slot.name] = _placeholder(range_str)
    except Exception:
        pass
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
