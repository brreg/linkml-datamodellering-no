#!/usr/bin/env python3
"""MCP-server for LinkML-generering frå ulike inputformat."""

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
    "name": "generate_linkml",
    "description": (
        "Genererer eit LinkML-skjema (utkast) frå ulike inputformat. "
        "Støtta format: 'json-schema' (JSON Schema som streng), 'empty' (tomt skjema med stub-klasse). "
        "Lintast og testvaliderast automatisk."
    ),
    "inputSchema": {
        "type": "object",
        "required": ["inputFormat"],
        "properties": {
            "inputFormat": {
                "type": "string",
                "description": "Inputformat: 'json-schema' eller 'empty'.",
                "enum": ["json-schema", "empty"],
            },
            "inputContent": {
                "type": "string",
                "description": "Innhaldet som skal konverterast (JSON Schema som streng). Ikkje påkravd for 'empty'.",
                "default": "",
            },
            "schemaId": {
                "type": "string",
                "description": "URI-identifikator for det genererte LinkML-skjemaet.",
                "default": "https://example.org/schema",
            },
            "schemaName": {
                "type": "string",
                "description": "Kortnamn for skjemaet (name-felt i LinkML).",
                "default": "schema",
            },
            "schemaTitle": {
                "type": "string",
                "description": "Tittel for skjemaet (valfri).",
                "default": "",
            },
            "profile": {
                "type": "string",
                "description": "Konverteringsprofil (default: 'default').",
                "default": "default",
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
                "serverInfo": {"name": "mcp-linkml-modell-utkast", "version": "1.0.0"},
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

        if tool_name == "generate_linkml":
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

    input_format = arguments.get("inputFormat", "")
    input_content = arguments.get("inputContent", "")
    schema_id    = arguments.get("schemaId",    "https://example.org/schema")
    schema_name  = arguments.get("schemaName",  "schema")
    schema_title = arguments.get("schemaTitle", "")
    profile_name = arguments.get("profile",     "default")
    do_validate  = arguments.get("validate",    True)

    valid_formats = {"json-schema", "empty"}
    if input_format not in valid_formats:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ugyldig inputFormat: '{input_format}'. Gyldige: {sorted(valid_formats)}"},
        }

    try:
        profile = load_profile(profile_name)
    except FileNotFoundError:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ukjend profil: '{profile_name}'"},
        }

    if input_format == "json-schema":
        try:
            json_schema = json.loads(input_content or "{}")
        except json.JSONDecodeError as exc:
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32602, "message": f"Ugyldig JSON Schema: {exc}"},
            }
    elif input_format == "empty":
        json_schema = {"type": "object", "properties": {}}

    linkml_yaml, warnings = convert(
        json_schema, profile,
        schema_id=schema_id,
        schema_name=schema_name,
        schema_title=schema_title,
    )

    lint_issues      = []
    dummy_validation = {"skipped": "validate: false"}
    if do_validate:
        val = validate_generated(linkml_yaml)
        lint_issues      = val.get("lint_issues", [])
        dummy_validation = val.get("dummy_validation", {})

    result = {
        "linkmlSchema":    linkml_yaml,
        "warnings":        warnings,
        "lintIssues":      lint_issues,
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
