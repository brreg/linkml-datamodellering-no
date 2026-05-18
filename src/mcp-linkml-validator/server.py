#!/usr/bin/env python3
"""MCP-server for LinkML-skjemavalidering med konfigurerbar policy."""

import json
import sys
import tempfile
import yaml
from pathlib import Path


# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------

def issue(severity: str, code: str, target: str, message: str) -> dict:
    return {"severity": severity, "code": code, "target": target, "message": message}


_POLICY_DIR = Path(__file__).parent / "policies"


def load_policy(name: str = "default") -> dict:
    try:
        with open(_POLICY_DIR / f"{name}.yaml", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}


def send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# FAIR-sjekkar
# ---------------------------------------------------------------------------

def _all_slot_uris(schema) -> set:
    """Samlar alle slot_uri-verdiar frå globale slots og class-attributtar."""
    uris = set()
    for slot in (schema.slots or {}).values():
        if slot.slot_uri:
            uris.add(str(slot.slot_uri))
    for cls in (schema.classes or {}).values():
        for attr in (cls.attributes or {}).values():
            uri = getattr(attr, "slot_uri", None)
            if uri:
                uris.add(str(uri))
    return uris


def _fair_code(config: dict) -> str:
    return "fair_" + config["principle"].lower().replace(".", "")


def _check_schema_id_is_http_uri(sv, schema, config, issues):
    sid = str(schema.id or "")
    if not (sid.startswith("http://") or sid.startswith("https://")):
        issues.append(issue(
            config["severity"], _fair_code(config), "schema",
            f"FAIR {config['principle']}: schema.id er ikkje ein HTTP(S)-URI — persistent identifikator manglar",
        ))


def _check_schema_field_present(sv, schema, config, issues):
    field = config["field"]
    if not getattr(schema, field, None):
        issues.append(issue(
            config["severity"], _fair_code(config), "schema",
            f"FAIR {config['principle']}: schema.{field} manglar",
        ))


def _check_all_classes_have_class_uri(sv, schema, config, issues):
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            continue
        if not cls.class_uri:
            issues.append(issue(
                config["severity"], _fair_code(config), f"class:{cname}",
                f"FAIR {config['principle']}: Klasse '{cname}' manglar class_uri (formal ressursbeskrivelse)",
            ))


def _check_all_slots_have_slot_uri(sv, schema, config, issues):
    for sname, slot in (schema.slots or {}).items():
        if not slot.slot_uri:
            issues.append(issue(
                config["severity"], _fair_code(config), f"slot:{sname}",
                f"FAIR {config['principle']}: Slot '{sname}' manglar slot_uri — formell RDF-semantikk er ikkje definert",
            ))


def _check_schema_declares_standard_prefix(sv, schema, config, issues):
    standard_prefixes = set(config.get("standard_prefixes", []))
    declared = set(schema.prefixes.keys()) if schema.prefixes else set()
    if not (declared & standard_prefixes):
        issues.append(issue(
            config["severity"], _fair_code(config), "schema",
            f"FAIR {config['principle']}: Ingen standard vokabularprefiks deklarert "
            f"({', '.join(sorted(standard_prefixes))})",
        ))


def _check_schema_has_slot_with_uri(sv, schema, config, issues):
    match_uris = set(config.get("match_any_uri", []))
    if not (_all_slot_uris(schema) & match_uris):
        curie_forms = sorted(u for u in match_uris if "://" not in u)
        issues.append(issue(
            config["severity"], _fair_code(config), "schema",
            f"FAIR {config['principle']}: Ingen slot med {' / '.join(curie_forms)} funnen",
        ))


_FAIR_CHECK_HANDLERS = {
    "schema_id_is_http_uri":           _check_schema_id_is_http_uri,
    "schema_field_present":            _check_schema_field_present,
    "all_classes_have_class_uri":      _check_all_classes_have_class_uri,
    "all_slots_have_slot_uri":         _check_all_slots_have_slot_uri,
    "schema_declares_standard_prefix": _check_schema_declares_standard_prefix,
    "schema_has_slot_with_uri":        _check_schema_has_slot_with_uri,
}


def _check_class_slots(sv, schema, policy: dict, issues: list) -> None:
    """Sjekkar at spesifiserte klasser har slots med kravde slot_uri-ar."""
    must_include = policy.get("class_slots", {}).get("must_include", [])
    if not must_include:
        return

    own_class_names = set(schema.classes.keys()) if schema.classes else set()

    for entry in must_include:
        cname = entry.get("class")
        required_uri = entry.get("slot_uri")
        label = entry.get("label", required_uri)

        if cname not in own_class_names:
            continue

        slot_uris = set()
        visited: set = set()
        queue = [cname]
        while queue:
            name = queue.pop()
            if name in visited:
                continue
            visited.add(name)
            cls = sv.get_class(name)
            if cls is None:
                continue
            for sname in (cls.slots or []):
                slot = sv.get_slot(sname)
                if slot and slot.slot_uri:
                    slot_uris.add(str(slot.slot_uri))
            for attr in (cls.attributes or {}).values():
                if attr.slot_uri:
                    slot_uris.add(str(attr.slot_uri))
            if cls.is_a:
                queue.append(cls.is_a)
            for mixin in (cls.mixins or []):
                queue.append(mixin)

        if required_uri not in slot_uris:
            issues.append(issue(
                "error", "class_missing_required_slot", f"class:{cname}",
                f"Klasse '{cname}' manglar obligatorisk slot '{label}' ({required_uri})",
            ))


def _check_container_classes(schema, policy: dict, issues: list) -> None:
    """Sjekkar at tree_root-klassen har attributtar med range for spesifiserte klasser.

    Policy-nøklar:
      container_classes.must_include   – manglar → error
      container_classes.should_include – manglar → warning
    """
    must_include   = policy.get("container_classes", {}).get("must_include", [])
    should_include = policy.get("container_classes", {}).get("should_include", [])
    if not must_include and not should_include:
        return

    # Finn tree_root-klassen i dette skjemaet (ikkje importerte klasser)
    container_cls  = None
    container_name = None
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            container_cls  = cls
            container_name = cname
            break

    if container_cls is None:
        issues.append(issue(
            "error", "no_container_class", "schema",
            "Ingen tree_root-klasse funnen — kan ikkje sjekke container-klasse-krav",
        ))
        return

    # Samle range-verdiar frå attributtane til container-klassen
    container_ranges = {
        str(attr.range)
        for attr in (container_cls.attributes or {}).values()
        if attr.range
    }

    for cls_name in must_include:
        if cls_name not in container_ranges:
            issues.append(issue(
                "error", "container_missing_required_class",
                f"class:{container_name}",
                f"Container '{container_name}' manglar obligatorisk attributt med range '{cls_name}'",
            ))

    for cls_name in should_include:
        if cls_name not in container_ranges:
            issues.append(issue(
                "warning", "container_missing_recommended_class",
                f"class:{container_name}",
                f"Container '{container_name}' manglar anbefalt attributt med range '{cls_name}'",
            ))


def _run_fair_checks(sv, schema, policy: dict, issues: list) -> None:
    for config in policy.get("fair_checks", {}).values():
        handler = _FAIR_CHECK_HANDLERS.get(config.get("check"))
        if handler:
            handler(sv, schema, config, issues)


# ---------------------------------------------------------------------------
# Validering
# ---------------------------------------------------------------------------

def validate_schema(schema_text: str, policy_name: str = "default") -> dict:
    policy = load_policy(policy_name)
    issues = []

    with tempfile.TemporaryDirectory() as tmp_dir:
        schema_path = str(Path(tmp_dir) / "schema.yaml")
        Path(schema_path).write_text(schema_text, encoding="utf-8")

        # 1) Parse — gir parse-feil som error
        try:
            from linkml_runtime.utils.schemaview import SchemaView
            sv = SchemaView(schema_path)
        except Exception as exc:
            return {
                "valid": False,
                "errorCount": 1,
                "warningCount": 0,
                "issues": [issue("error", "parse_error", "schema", str(exc))],
            }

        # 2) LinkML linter — sender filstien (str), ikkje SchemaView
        try:
            from linkml.linter.linter import Linter
            linter = Linter()
            for problem in linter.lint(schema_path):
                level = getattr(problem.level, "value", str(problem.level)).lower()
                rule = getattr(problem, "rule_name", None) or "linkml_lint"
                target = str(getattr(problem, "source", None) or "schema")
                issues.append(issue(level, rule, target, str(problem.message)))
        except Exception as exc:
            issues.append(issue("error", "linter_error", "schema", str(exc)))

        schema = sv.schema

        # 3) Policy-felt-sjekkar
        def _check(obj, obj_label: str, required_fields: list, recommended_fields: list):
            for field in required_fields:
                if not getattr(obj, field, None):
                    issues.append(issue(
                        "error", "missing_required_metadata", obj_label,
                        f"Manglar obligatorisk metadata: {field}",
                    ))
            for field in recommended_fields:
                if not getattr(obj, field, None):
                    issues.append(issue(
                        "warning", "missing_recommended_metadata", obj_label,
                        f"Manglar anbefalt metadata: {field}",
                    ))

        _check(
            schema,
            f"schema:{schema.name or 'ukjent'}",
            policy.get("required", {}).get("schema", []),
            policy.get("recommended", {}).get("schema", []),
        )
        for cname, cls in (schema.classes or {}).items():
            _check(
                cls, f"class:{cname}",
                policy.get("required", {}).get("class", []),
                policy.get("recommended", {}).get("class", []),
            )
        for sname, slot in (schema.slots or {}).items():
            _check(
                slot, f"slot:{sname}",
                policy.get("required", {}).get("slot", []),
                policy.get("recommended", {}).get("slot", []),
            )

        # Påkravde fellesklasser
        must_use = policy.get("common_classes", {}).get("must_use", [])
        all_class_names = set(sv.all_classes().keys())
        for cc in must_use:
            if cc not in all_class_names:
                issues.append(issue(
                    "error", "missing_common_class", f"class:{cc}",
                    f"Påkravd fellesklasse manglar: {cc}",
                ))

        # Container-klasse-sjekkar
        _check_container_classes(schema, policy, issues)

        # AP-NO obligatoriske slot-sjekkar
        _check_class_slots(sv, schema, policy, issues)

        # 4) FAIR-strukturelle sjekkar (berre for policyer som definerer fair_checks)
        _run_fair_checks(sv, schema, policy, issues)

    errors = [i for i in issues if i["severity"] == "error"]
    warnings = [i for i in issues if i["severity"] == "warning"]
    return {
        "valid": len(errors) == 0,
        "errorCount": len(errors),
        "warningCount": len(warnings),
        "issues": issues,
    }


# ---------------------------------------------------------------------------
# MCP-protokoll
# ---------------------------------------------------------------------------

TOOL_DEF = {
    "name": "validate_linkml_schema",
    "description": (
        "Validerer eit LinkML-skjema med standard LinkML-linting og "
        "konfigurerbare policy-reglar. Støttar fleire policyer: "
        "'default' (basis) og 'fair' (FAIR-prinsippa F1–R1.3)."
    ),
    "inputSchema": {
        "type": "object",
        "required": ["schemaText"],
        "properties": {
            "schemaText": {
                "type": "string",
                "description": "LinkML-skjema i YAML-format.",
            },
            "policy": {
                "type": "string",
                "description": "Policy-namn (default: 'default'). Tilgjengelege: 'default', 'fair'.",
                "default": "default",
            },
        },
    },
}


def handle(msg: dict) -> dict | None:
    method = msg.get("method", "")
    msg_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "mcp-linkml-validator", "version": "1.0.0"},
            },
        }

    if method == "initialized":
        return None  # notifikasjon — ingen respons

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": [TOOL_DEF]},
        }

    if method == "tools/call":
        tool_name = msg.get("params", {}).get("name")
        arguments = msg.get("params", {}).get("arguments", {})

        if tool_name == "validate_linkml_schema":
            policy_name = arguments.get("policy", "default")
            result = validate_schema(arguments.get("schemaText", ""), policy_name)
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}
                    ]
                },
            }

        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ukjent verktøy: {tool_name}"},
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Metode ikkje funnen: {method}"},
    }


def main():
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError as exc:
            send({"jsonrpc": "2.0", "id": None,
                  "error": {"code": -32700, "message": f"Parse-feil: {exc}"}})
            continue

        response = handle(msg)
        if response is not None:
            send(response)


if __name__ == "__main__":
    main()
