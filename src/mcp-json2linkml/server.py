#!/usr/bin/env python3
"""MCP-server for JSON Schema → LinkML-konvertering."""

import json
import sys
import yaml
from pathlib import Path


_PROFILES_DIR = Path(__file__).parent / "profiles"


def send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _list_profiles() -> list:
    profiles = []
    for path in sorted(_PROFILES_DIR.glob("*.yaml")):
        try:
            with open(path, encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            profiles.append({"name": path.stem, "description": data.get("description", "")})
        except Exception:
            profiles.append({"name": path.stem, "description": ""})
    return profiles


# ---------------------------------------------------------------------------
# Verktøy-definisjonar
# ---------------------------------------------------------------------------

TOOL_GENERATE = {
    "name": "generate_linkml_from_json_schema",
    "description": (
        "Konverterer eit JSON Schema til eit LinkML-skjema (utkast) "
        "basert på ein konfigurerbar profil. Lintast og testvaliderast automatisk."
    ),
    "inputSchema": {
        "type": "object",
        "required": ["jsonSchema", "schemaId", "schemaName"],
        "properties": {
            "jsonSchema": {
                "type": "string",
                "description": "JSON Schema som JSON-streng.",
            },
            "schemaId": {
                "type": "string",
                "description": "URI-identifikator for det genererte LinkML-skjemaet.",
            },
            "schemaName": {
                "type": "string",
                "description": "Kortnamn for skjemaet (name-felt i LinkML).",
            },
            "schemaTitle": {
                "type": "string",
                "description": "Tittel for skjemaet (valfri).",
            },
            "profile": {
                "type": "string",
                "description": "Konverteringsprofil (default: 'ap-no').",
                "default": "ap-no",
            },
            "validate": {
                "type": "boolean",
                "description": "Lint og dummy-valider det genererte skjemaet (default: true).",
                "default": True,
            },
        },
    },
}

TOOL_LIST_PROFILES = {
    "name": "list_profiles",
    "description": "Listar tilgjengelege konverteringsprofiler.",
    "inputSchema": {
        "type": "object",
        "properties": {},
    },
}


# ---------------------------------------------------------------------------
# Meldingshandtering
# ---------------------------------------------------------------------------

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
                "serverInfo": {"name": "mcp-json2linkml", "version": "1.0.0"},
            },
        }

    if method == "initialized":
        return None

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": [TOOL_GENERATE, TOOL_LIST_PROFILES]},
        }

    if method == "tools/call":
        tool_name = (msg.get("params") or {}).get("name")
        arguments = (msg.get("params") or {}).get("arguments") or {}

        if tool_name == "list_profiles":
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(_list_profiles(), ensure_ascii=False)}
                    ]
                },
            }

        if tool_name == "generate_linkml_from_json_schema":
            return _handle_generate(msg_id, arguments)

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


def _handle_generate(msg_id, arguments: dict) -> dict:
    from converter import load_profile, convert
    from validator import validate_generated

    json_schema_str = arguments.get("jsonSchema", "{}")
    schema_id    = arguments.get("schemaId",   "https://example.org/schema")
    schema_name  = arguments.get("schemaName",  "schema")
    schema_title = arguments.get("schemaTitle", "")
    profile_name = arguments.get("profile",     "ap-no")
    do_validate  = arguments.get("validate",    True)

    try:
        json_schema = json.loads(json_schema_str)
    except json.JSONDecodeError as exc:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ugyldig JSON Schema: {exc}"},
        }

    try:
        profile = load_profile(profile_name)
    except FileNotFoundError:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ukjend profil: '{profile_name}'"},
        }

    linkml_yaml, warnings = convert(
        json_schema, profile,
        schema_id=schema_id,
        schema_name=schema_name,
        schema_title=schema_title,
    )

    lint_issues     = []
    dummy_validation = {"skipped": "validate: false"}
    if do_validate:
        val = validate_generated(linkml_yaml)
        lint_issues      = val.get("lint_issues", [])
        dummy_validation = val.get("dummy_validation", {})

    result = {
        "linkmlSchema":   linkml_yaml,
        "warnings":       warnings,
        "lintIssues":     lint_issues,
        "dummyValidation": dummy_validation,
    }
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "content": [
                {"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}
            ]
        },
    }


# ---------------------------------------------------------------------------
# Hovudløkke
# ---------------------------------------------------------------------------

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
