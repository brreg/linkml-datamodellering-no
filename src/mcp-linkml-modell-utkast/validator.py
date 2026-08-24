#!/usr/bin/env python3
"""Lint og dummy-datasett-validering av genererte LinkML-skjema.

Offentleg API:
  validate_generated(linkml_yaml: str) → dict

Køyrt direkte (python3 validator.py <schema.yaml> [id-prefiks]) skriv modulen
i staden ut eit rikt syntetisk eksempeldatasett for containerklassen i
skjemaet (alle slots, ikkje berre required/identifier — sjå
_build_example_data), til bruk som startpunkt for
examples/<modell>-eksempel.yaml eller direkte via `make gen-eksempeldata`.

`validate_generated()` (MCP-serveren sin interne sjølvsjekk under
skjemagenerering) brukar framleis den minimale `_build_dummy_data`/
`_build_dummy_instance`-logikken (kun required/identifier) — å fylle ut alle
valfrie slots ville auka sjansen for at generiske placeholders bryt
pattern-/verdiavgrensingar på eit skjema under aktiv utarbeiding, noko som
ville gje falske negative i eit etablert, testa steg. Sjå
specs/done/gen-eksempeldata-fra-skjema.md.
"""

import re
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
    "datetime":   "2024-01-01T00:00:00Z",
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
# Rike eksempeldata (alle slots, kryssreferansar) — for examples/<modell>-
# eksempel.yaml og `make gen-eksempeldata`. Held seg unna _build_dummy_*
# over, som validate_generated() framleis brukar uendra — sjå moduldocstring.
# ---------------------------------------------------------------------------

def _kebab(name: str) -> str:
    """PascalCase → kebab-case (t.d. 'KontaktPunkt' → 'kontakt-punkt')."""
    return re.sub(r"(?<!^)(?=[A-Z])", "-", str(name)).lower()


def _enum_placeholder(sv, range_str: str):
    """Returnerer første permissible_values-nøkkel for eit enum-range, eller
    None dersom range_str ikkje er eit lokalt/importert enum-navn."""
    try:
        enum_def = sv.get_enum(range_str)
    except Exception:
        return None
    if enum_def is None or not enum_def.permissible_values:
        return None
    return str(next(iter(enum_def.permissible_values)))


def _type_base(sv, range_str: str):
    """Returnerer `base`-verdien (t.d. 'int', 'float', 'str') for ein
    eigendefinert `types:`-oppføring (t.d. NonNegativeInteger → 'int'), eller
    None dersom range_str ikkje er eit typenavn eller ikkje har ein base."""
    try:
        type_def = sv.get_type(range_str)
    except Exception:
        return None
    if type_def is None or not type_def.base:
        return None
    return str(type_def.base)


def _example_placeholder(sv, range_str: str, slot_name: str) -> object:
    """Som _placeholder(), men med to utvidingar:
    - eigendefinerte `types:`-oppføringar med numerisk/bool base (t.d.
      NonNegativeInteger → base 'int') vert løyst til rett primitiv
      placeholder via _type_base, ikkje generisk tekst — elles ville t.d.
      eit heiltalsfelt fått ein ugyldig strengverdi.
    - fallback for range utan kjend primitiv/base-match er ein skildrande
      placeholder utleidd frå slotnamnet, ikkje generisk 'dummy' — gjer
      eksempelfila sjølvforklarande utan å innføre ei ny biblioteksavhengigheit
      (t.d. faker)."""
    key = str(range_str).lower()
    if key in _PLACEHOLDERS:
        return _PLACEHOLDERS[key]
    base = _type_base(sv, range_str)
    if base is not None:
        base_key = str(base).lower()
        if base_key in _PLACEHOLDERS:
            return _PLACEHOLDERS[base_key]
    return f"Eksempelverdi for {slot_name}"


def _class_reference_placeholder(range_class: str) -> str:
    """Generisk syntetisk URI-referanse for eit klasse-range-slot der
    target-klassen ikkje er ein containerattributt-klasse (dvs. inga fysisk
    instans er generert nokon stad i fila) — same mønster som eksterne
    foaf:Agent-referansar i handskrivne eksempel (t.d. dcat-ap-no)."""
    return f"ex:{_kebab(range_class)}-1"


def _build_example_instance(sv, class_name: str, class_id_map: dict, own_id: str | None = None) -> dict:
    """Lagar ein rik eksempelinstans av class_name: **alle** slots vert fylte
    (ikkje berre required/identifier), multivalued-slot vert lister,
    enum-range vel første permissible_values, og klasse-range-slot vert
    lenka til den genererte instansen sin id via class_id_map dersom
    target-klassen sjølv er ein containerattributt-klasse — elles ein
    generisk placeholder-URI (sjå _class_reference_placeholder).

    `own_id` er denne konkrete instansen sin eigen tildelte id (sett av
    _build_example_data) — brukast for identifier-slotet i staden for
    class_id_map[class_name], sidan fleire containerattributt kan dele same
    range_class (t.d. to ulike aktørroller typa som same klasse); utan
    dette ville alle slike instansar fått identisk id og innhald."""
    instance: dict = {}
    try:
        for slot in sv.class_induced_slots(class_name):
            slot_name = str(slot.name)
            range_str = str(slot.range or "string")

            if slot.identifier:
                value = own_id or class_id_map.get(class_name) or _example_placeholder(sv, range_str, slot_name)
            elif range_str in sv.all_classes():
                value = class_id_map.get(range_str) or _class_reference_placeholder(range_str)
            else:
                enum_value = _enum_placeholder(sv, range_str)
                value = enum_value if enum_value is not None else _example_placeholder(sv, range_str, slot_name)

            instance[slot_name] = [value] if slot.multivalued else value
    except Exception as e:
        print(f"ÅTVARING: kunne ikkje byggje eksempelinstans for {class_name} — {e}", file=sys.stderr)
    return instance


def _build_example_data(sv, container_class: str, id_prefix: str | None = None) -> dict:
    """Lagar rike eksempeldata for containerklassen med éin instans per
    containerattributt. To pass: (1) tildel éin unik id per
    containerattributt (sekvensielt, '<prefiks>-N' — same konvensjon som
    dagens <navn>:eksempel-N) og fyll class_id_map med den *første* id-en
    tildelt kvar range_class (brukt av andre instansar sine kryssreferansar
    — fleire containerattributt kan dele same range_class, t.d. to ulike
    aktørroller typa som same klasse, men skal likevel få kvar sin unike
    eigen-id, ikkje dele éin), (2) bygg instansane med id-kartet
    tilgjengeleg for kryssreferanse-oppslag i _build_example_instance.
    """
    cls = sv.get_class(container_class)
    prefix = id_prefix or str(sv.schema.name or "eksempel")

    attr_classes: dict = {}
    attr_ids: dict = {}
    class_id_map: dict = {}
    counter = 1
    for attr_name, attr in (cls.attributes or {}).items():
        range_class = str(attr.range) if attr.range else None
        if not range_class or range_class not in sv.all_classes():
            continue
        attr_classes[attr_name] = range_class
        assigned_id = f"{prefix}-{counter}"
        attr_ids[attr_name] = assigned_id
        class_id_map.setdefault(range_class, assigned_id)
        counter += 1

    data: dict = {}
    for attr_name, range_class in attr_classes.items():
        attr = cls.attributes[attr_name]
        instance = _build_example_instance(sv, range_class, class_id_map, attr_ids[attr_name])
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
# CLI: skriv ut rike eksempeldata for containerklassen i eit LinkML-skjema
# ---------------------------------------------------------------------------

def _main() -> None:
    """Bruk: python3 validator.py <schema.yaml> [id-prefiks]

    Skriv YAML til stdout med éin rik eksempelinstans per containerattributt
    (alle slots fylte, ikkje berre required/identifier — sjå
    _build_example_data). Med id-prefiks (t.d. 'mittskjema:eksempel') vert
    genererte id-ar '<prefiks>-<løpenummer>' i staden for
    '<skjemanavn>-<løpenummer>' — konsistent med <navn>:eksempel-N-
    konvensjonen i examples/<modell>-eksempel.yaml.
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

    data = _build_example_data(sv, container_class, id_prefix)

    yaml.dump(data, sys.stdout, allow_unicode=True, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    _main()
