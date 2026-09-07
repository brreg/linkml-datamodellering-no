#!/usr/bin/env python3
"""MCP-server for LinkML-generering frå ulike inputformat."""

import json
import sys
import yaml
from pathlib import Path

# Delt utils-modul (mcp_jsonrpc_stdio) ligg i src/assets/scripts/utils/ i
# repoet. Ulike invokeringar monterer/kopierer han til ulike kontainarstiar
# — prøv alle kjende kandidatar. Sjå
# src/assets/scripts/utils/mcp_jsonrpc_stdio.py for grunngjeving.
sys.path.insert(0, "/app/utils")
sys.path.insert(0, "/repo/src/assets/scripts/utils")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "assets" / "scripts" / "utils"))

from mcp_jsonrpc_stdio import dispatch, run_stdio_loop  # noqa: E402


# Katalogen heiter framleis "profiles" fysisk på disk — sjå spec
# specs/backlog/erstatt-profil-med-policy.md for grunngjeving/oppfølging.
_POLICIES_DIR = Path(__file__).parent / "profiles"


def _list_policies() -> list:
    policies = []
    for path in sorted(_POLICIES_DIR.glob("*.yaml")):
        try:
            with open(path, encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            policies.append({"name": path.stem, "description": data.get("description", "")})
        except Exception as e:
            print(f"ÅTVARING: kunne ikkje lese policy {path} — {e}", file=sys.stderr)
            policies.append({"name": path.stem, "description": ""})
    return policies


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
                "description": "Kortnavn for skjemaet (name-felt i LinkML).",
                "default": "schema",
            },
            "schemaTitle": {
                "type": "string",
                "description": "Tittel for skjemaet (valfri).",
                "default": "",
            },
            "policy": {
                "type": "string",
                "description": "Konverteringspolicy (default: 'bronze'). Tilgjengelege: 'bronze', 'silver'.",
                "default": "bronze",
            },
            "validate": {
                "type": "boolean",
                "description": "Lint og dummy-valider det genererte skjemaet (default: true).",
                "default": True,
            },
        },
    },
}

TOOL_LIST_POLICIES = {
    "name": "list_policies",
    "description": "Listar tilgjengelege konverteringspolicyar.",
    "inputSchema": {
        "type": "object",
        "properties": {},
    },
}


# ---------------------------------------------------------------------------
# Meldingshandtering
# ---------------------------------------------------------------------------

def _handle_list_policies(msg_id, arguments: dict) -> dict:
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "result": {
            "content": [
                {"type": "text", "text": json.dumps(_list_policies(), ensure_ascii=False)}
            ]
        },
    }


def _handle_generate(msg_id, arguments: dict) -> dict:
    from converter import load_policy, convert
    from validator import validate_generated

    input_format = arguments.get("inputFormat", "")
    input_content = arguments.get("inputContent", "")
    schema_id    = arguments.get("schemaId",    "https://example.org/schema")
    schema_name  = arguments.get("schemaName",  "schema")
    schema_title = arguments.get("schemaTitle", "")
    policy_name  = arguments.get("policy",      "bronze")
    do_validate  = arguments.get("validate",    True)

    valid_formats = {"json-schema", "empty"}
    if input_format not in valid_formats:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ugyldig inputFormat: '{input_format}'. Gyldige: {sorted(valid_formats)}"},
        }

    try:
        policy = load_policy(policy_name)
    except FileNotFoundError:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ukjend policy: '{policy_name}'"},
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
        json_schema, policy,
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


_TOOL_HANDLERS = {
    "list_policies": _handle_list_policies,
    "generate_linkml": _handle_generate,
}


def handle(msg: dict) -> dict | None:
    return dispatch(
        msg,
        tools=[TOOL_GENERATE, TOOL_LIST_POLICIES],
        tool_handlers=_TOOL_HANDLERS,
        server_name="mcp-linkml-modell-utkast",
    )


if __name__ == "__main__":
    run_stdio_loop(handle)
