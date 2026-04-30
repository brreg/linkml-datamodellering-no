"""
Unit-testar for mcp-linkml-validator.

Importerer server.py direkte — krev linkml (ikkje podman).

Køyr via:
    bash src/mcp-linkml-validator/pt-mcp-linkml-validator.bash
"""

import json
import sys
import os

# Finn server.py uavhengig av CWD
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "mcp-linkml-validator"))

from server import validate_schema, handle  # noqa: E402

# ---------------------------------------------------------------------------
# Testskjema
# ---------------------------------------------------------------------------

VALID_SCHEMA = """\
id: https://example.org/test
name: test
description: Testskjema
prefixes:
  linkml: https://w3id.org/linkml/
  ex: https://example.org/
default_prefix: ex
imports:
  - linkml:types
classes:
  Person:
    description: Ein person
    class_uri: ex:Person
    tree_root: true
    attributes:
      namn:
        description: Personens namn
        range: string
"""

SCHEMA_NO_ID = """\
name: utan-id
prefixes:
  linkml: https://w3id.org/linkml/
  ex: https://example.org/
default_prefix: ex
imports:
  - linkml:types
classes:
  Ting:
    description: Ei ting
"""

SCHEMA_NO_DESCRIPTION = """\
id: https://example.org/test
name: test
prefixes:
  linkml: https://w3id.org/linkml/
  ex: https://example.org/
default_prefix: ex
imports:
  - linkml:types
classes:
  Person:
    class_uri: ex:Person
    attributes:
      namn:
        range: string
"""

INVALID_YAML = "dette er ikkje gyldig yaml: {["


# ---------------------------------------------------------------------------
# Testar: MCP-protokoll (handle-funksjonen, ingen linkml nødvendig)
# ---------------------------------------------------------------------------

class TestMCPProtocol:
    def test_initialize_returns_server_info(self):
        r = handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        assert r["result"]["serverInfo"]["name"] == "mcp-linkml-validator"

    def test_initialize_protocol_version(self):
        r = handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        assert r["result"]["protocolVersion"] == "2024-11-05"

    def test_initialize_advertises_tools_capability(self):
        r = handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        assert "tools" in r["result"]["capabilities"]

    def test_initialized_notification_returns_none(self):
        r = handle({"jsonrpc": "2.0", "method": "initialized"})
        assert r is None

    def test_tools_list_contains_validate_tool(self):
        r = handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
        names = [t["name"] for t in r["result"]["tools"]]
        assert "validate_linkml_schema" in names

    def test_tools_list_tool_has_input_schema(self):
        r = handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
        tool = next(t for t in r["result"]["tools"] if t["name"] == "validate_linkml_schema")
        assert "schemaText" in tool["inputSchema"]["properties"]
        assert "schemaText" in tool["inputSchema"]["required"]

    def test_unknown_method_returns_error_code(self):
        r = handle({"jsonrpc": "2.0", "id": 9, "method": "ukjent/metode", "params": {}})
        assert "error" in r
        assert r["error"]["code"] == -32601

    def test_unknown_tool_returns_error(self):
        r = handle({
            "jsonrpc": "2.0", "id": 5, "method": "tools/call",
            "params": {"name": "finst_ikkje", "arguments": {}},
        })
        assert "error" in r
        assert r["error"]["code"] == -32602

    def test_tools_call_response_uses_content_format(self):
        r = handle({
            "jsonrpc": "2.0", "id": 3, "method": "tools/call",
            "params": {"name": "validate_linkml_schema", "arguments": {"schemaText": VALID_SCHEMA}},
        })
        content = r["result"]["content"]
        assert content[0]["type"] == "text"
        json.loads(content[0]["text"])  # skal vere gyldig JSON


# ---------------------------------------------------------------------------
# Testar: validate_schema (krev linkml)
# ---------------------------------------------------------------------------

class TestValidation:
    def test_valid_schema_is_valid(self):
        result = validate_schema(VALID_SCHEMA)
        assert result["valid"] is True
        assert result["errorCount"] == 0

    def test_result_has_required_keys(self):
        result = validate_schema(VALID_SCHEMA)
        assert "valid" in result
        assert "errorCount" in result
        assert "warningCount" in result
        assert "issues" in result

    def test_issue_has_required_keys(self):
        result = validate_schema(SCHEMA_NO_DESCRIPTION)
        for issue in result["issues"]:
            assert "severity" in issue
            assert "code" in issue
            assert "target" in issue
            assert "message" in issue

    def test_invalid_yaml_is_not_valid(self):
        result = validate_schema(INVALID_YAML)
        assert result["valid"] is False
        assert result["errorCount"] >= 1

    def test_invalid_yaml_issue_is_parse_error(self):
        result = validate_schema(INVALID_YAML)
        codes = [i["code"] for i in result["issues"]]
        assert "parse_error" in codes

    def test_schema_without_id_fails_policy(self):
        result = validate_schema(SCHEMA_NO_ID)
        errors = [i for i in result["issues"] if i["severity"] == "error"]
        id_errors = [e for e in errors if "id" in e["message"]]
        assert len(id_errors) >= 1

    def test_schema_without_class_description_gets_warning(self):
        result = validate_schema(SCHEMA_NO_DESCRIPTION)
        warnings = [i for i in result["issues"] if i["severity"] == "warning"]
        desc_warnings = [w for w in warnings if "description" in w["message"]]
        assert len(desc_warnings) >= 1

    def test_no_errors_for_valid_schema(self):
        result = validate_schema(VALID_SCHEMA)
        errors = [i for i in result["issues"] if i["severity"] == "error"]
        assert errors == []

    def test_error_count_matches_issues(self):
        result = validate_schema(SCHEMA_NO_ID)
        actual_errors = sum(1 for i in result["issues"] if i["severity"] == "error")
        assert result["errorCount"] == actual_errors

    def test_warning_count_matches_issues(self):
        result = validate_schema(SCHEMA_NO_DESCRIPTION)
        actual_warnings = sum(1 for i in result["issues"] if i["severity"] == "warning")
        assert result["warningCount"] == actual_warnings
