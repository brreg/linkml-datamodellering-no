#!/usr/bin/env python3
"""Automatiske testar for mcp-linkml-modell-utkast converter.

Køyr frå repo-rot:
  make linkml-gen-test-converter

Krev linkml og linkml-runtime (tilgjengeleg i containeren):
  python3 tests/test_mcp_linkml_generator.py -v
"""

import json
import os
import sys
import tempfile
import unittest
import yaml
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src" / "mcp-linkml-modell-utkast"))
from converter import convert, load_policy
from validator import validate_generated
from server import handle


# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------

def _policy() -> dict:
    """Minimal testpolicy — identisk med default.yaml-innhaldet."""
    return {
        "naming": {"class_uri_prefix": "ex", "slot_uri_prefix": "ex"},
        "standard_prefixes": {"linkml": "https://w3id.org/linkml/"},
        "schema_defaults": {
            "default_range": "string",
            "imports": ["linkml:types"],
        },
        "generation": {
            "add_id_slot": True,
            "add_container_class": True,
            "container_class_name": "Containerklasse",
            "container_slot_suffix": "er",
            "add_begrep_annotation": True,
            "begrep_base_uri": "https://data.norge.no/concepts/",
        },
        "subsets": {
            "required_maps_to": "Obligatorisk",
            "non_required_default": "Anbefalt",
        },
        "type_mapping": {
            "string": "string",
            "integer": "integer",
            "number": "float",
            "boolean": "boolean",
        },
        "format_mapping": {
            "uri": "uriorcurie",
            "date": "date",
            "date-time": "datetime",
            "time": "time",
        },
    }


def _convert(json_schema: dict, schema_name: str = "test") -> tuple[dict, list[str]]:
    """Konverterer og returnerer (parsed_schema_dict, warnings)."""
    yaml_str, warnings = convert(
        json_schema,
        _policy(),
        schema_id="https://example.org/test",
        schema_name=schema_name,
    )
    return yaml.safe_load(yaml_str), warnings


# ---------------------------------------------------------------------------
# TestConversion
# ---------------------------------------------------------------------------

class TestConversion(unittest.TestCase):

    def test_required_property_får_obligatorisk_subset(self):
        schema, _ = _convert({
            "$defs": {
                "Person": {
                    "type": "object",
                    "properties": {
                        "namn": {"type": "string"},
                        "alder": {"type": "integer"},
                    },
                    "required": ["namn"],
                }
            }
        })
        su = schema["classes"]["Person"]["slot_usage"]
        self.assertEqual(su["namn"]["in_subset"], ["Obligatorisk"])
        self.assertTrue(su["namn"]["required"])
        self.assertEqual(su["alder"]["in_subset"], ["Anbefalt"])
        self.assertNotIn("required", su["alder"])

    def test_ref_til_definisjon_gir_range(self):
        schema, warnings = _convert({
            "$defs": {
                "Ordre": {
                    "type": "object",
                    "properties": {
                        "kunde": {"$ref": "#/$defs/Kunde"},
                    },
                },
                "Kunde": {
                    "type": "object",
                    "properties": {
                        "namn": {"type": "string"},
                    },
                },
            }
        })
        self.assertEqual(schema["slots"]["kunde"]["range"], "Kunde")
        self.assertEqual([], warnings)

    def test_array_type_gir_multivalued(self):
        schema, _ = _convert({
            "$defs": {
                "Pakke": {
                    "type": "object",
                    "properties": {
                        "taggar": {"type": "array", "items": {"type": "string"}},
                    },
                }
            }
        })
        self.assertTrue(schema["slots"]["taggar"]["multivalued"])
        self.assertEqual(schema["slots"]["taggar"]["range"], "string")

    def test_array_med_ref_gir_multivalued_og_range(self):
        schema, _ = _convert({
            "$defs": {
                "Katalog": {
                    "type": "object",
                    "properties": {
                        "datasett": {"type": "array", "items": {"$ref": "#/$defs/Datasett"}},
                    },
                },
                "Datasett": {
                    "type": "object",
                    "properties": {},
                },
            }
        })
        self.assertTrue(schema["slots"]["datasett"]["multivalued"])
        self.assertEqual(schema["slots"]["datasett"]["range"], "Datasett")

    def test_format_uri_gir_uriorcurie(self):
        schema, _ = _convert({
            "$defs": {
                "Ressurs": {
                    "type": "object",
                    "properties": {
                        "lenke": {"type": "string", "format": "uri"},
                    },
                }
            }
        })
        self.assertEqual(schema["slots"]["lenke"]["range"], "uriorcurie")

    def test_format_date_gir_date(self):
        schema, _ = _convert({
            "$defs": {
                "Hendelse": {
                    "type": "object",
                    "properties": {
                        "dato": {"type": "string", "format": "date"},
                    },
                }
            }
        })
        self.assertEqual(schema["slots"]["dato"]["range"], "date")

    def test_format_datetime_gir_datetime(self):
        schema, _ = _convert({
            "$defs": {
                "Logg": {
                    "type": "object",
                    "properties": {
                        "tidspunkt": {"type": "string", "format": "date-time"},
                    },
                }
            }
        })
        self.assertEqual(schema["slots"]["tidspunkt"]["range"], "datetime")

    def test_containerklasse_vert_generert(self):
        schema, _ = _convert({
            "$defs": {
                "Ting": {
                    "type": "object",
                    "properties": {"namn": {"type": "string"}},
                }
            }
        })
        container = schema["classes"]["Containerklasse"]
        self.assertTrue(container["tree_root"])
        self.assertIn("tinger", container["attributes"])
        attr = container["attributes"]["tinger"]
        self.assertEqual(attr["range"], "Ting")
        self.assertTrue(attr["multivalued"])
        self.assertTrue(attr["inlined"])
        self.assertTrue(attr["inlined_as_list"])

    def test_id_slot_vert_generert(self):
        schema, _ = _convert({
            "$defs": {
                "Ting": {
                    "type": "object",
                    "properties": {},
                }
            }
        })
        self.assertIn("id", schema["slots"])
        self.assertTrue(schema["slots"]["id"]["identifier"])
        self.assertEqual(schema["slots"]["id"]["range"], "uriorcurie")
        self.assertIn("id", schema["classes"]["Ting"]["slots"])

    def test_slot_namns_kollisjon_gir_åtvaring_ikkje_exception(self):
        schema, warnings = _convert({
            "$defs": {
                "A": {
                    "type": "object",
                    "properties": {"verdi": {"type": "string"}},
                },
                "B": {
                    "type": "object",
                    "properties": {"verdi": {"type": "integer"}},
                },
            }
        })
        self.assertTrue(any("verdi" in w for w in warnings))
        self.assertIn("verdi", schema["slots"])

    def test_anyof_med_null_gir_nullable_mønster(self):
        schema, warnings = _convert({
            "$defs": {
                "Ting": {
                    "type": "object",
                    "properties": {
                        "val": {"anyOf": [{"type": "string"}, {"type": "null"}]},
                    },
                }
            }
        })
        self.assertEqual(schema["slots"]["val"]["range"], "string")
        self.assertEqual([], warnings)

    def test_anyof_fleire_ikkje_null_typar_gir_åtvaring(self):
        _, warnings = _convert({
            "$defs": {
                "Ting": {
                    "type": "object",
                    "properties": {
                        "val": {"anyOf": [{"type": "string"}, {"type": "integer"}]},
                    },
                }
            }
        })
        self.assertTrue(any("anyOf" in w for w in warnings))

    def test_schema_utan_defs_bruker_rot_properties(self):
        schema, _ = _convert(
            {
                "type": "object",
                "properties": {
                    "namn": {"type": "string"},
                    "dato": {"type": "string", "format": "date"},
                },
                "required": ["namn"],
            },
            schema_name="MinModell",
        )
        self.assertIn("MinModell", schema["classes"])
        self.assertIn("namn", schema["slots"])
        self.assertIn("dato", schema["slots"])
        su = schema["classes"]["MinModell"]["slot_usage"]
        self.assertEqual(su["namn"]["in_subset"], ["Obligatorisk"])
        self.assertEqual(su["dato"]["in_subset"], ["Anbefalt"])

    def test_tom_properties_gir_klasse_utan_slot_usage(self):
        schema, _ = _convert({
            "$defs": {
                "Tom": {
                    "type": "object",
                    "properties": {},
                }
            }
        })
        self.assertIn("Tom", schema["classes"])
        self.assertNotIn("slot_usage", schema["classes"]["Tom"])

    def test_begrep_annotation_stubb_vert_lagt_til(self):
        schema, _ = _convert({
            "$defs": {
                "Ting": {
                    "type": "object",
                    "properties": {},
                }
            }
        })
        ann = schema["classes"]["Ting"]["annotations"]
        self.assertIn("begrepsidentifikator", ann)
        self.assertIn("data.norge.no/concepts", ann["begrepsidentifikator"])

    def test_class_uri_vert_sett(self):
        schema, _ = _convert({
            "$defs": {
                "Hendelse": {
                    "type": "object",
                    "properties": {},
                }
            }
        })
        self.assertEqual(schema["classes"]["Hendelse"]["class_uri"], "test:Hendelse")

    def test_slot_uri_vert_sett(self):
        schema, _ = _convert({
            "$defs": {
                "Ting": {
                    "type": "object",
                    "properties": {"tittel": {"type": "string"}},
                }
            }
        })
        self.assertEqual(schema["slots"]["tittel"]["slot_uri"], "test:tittel")

    def test_subsets_vert_ikkje_lokalt_definert(self):
        """Subset-namna vert berre referert via in_subset, aldri definert lokalt —
        ei lokal subsets-blokk kolliderer med same namn importert frå
        common-ap-no-schema.yaml (sjå specs/done/fjern-lokale-subsets-new-modell.md)."""
        schema, _ = _convert({"type": "object", "properties": {}}, schema_name="Tom")
        self.assertNotIn("subsets", schema)

    def test_ekstern_ref_gir_åtvaring(self):
        _, warnings = _convert({
            "$defs": {
                "Ting": {
                    "type": "object",
                    "properties": {
                        "relatert": {"$ref": "https://other.example.org/schema#/Foo"},
                    },
                }
            }
        })
        self.assertTrue(any("Ekstern" in w for w in warnings))

    def test_allof_med_ref_gir_is_a_klasse(self):
        """Same mønster som Stedsadresse/GeografiskAdresse i
        src/tmp/bvrstiftelsesdokument_lm_v0.schema.json — allOf som utvidar
        ein foreldretype skal bli ei is_a-klasse, ikkje bli stille droppa."""
        schema, warnings = _convert({
            "$defs": {
                "GeografiskAdresse": {
                    "type": "object",
                    "properties": {},
                },
                "Stedsadresse": {
                    "allOf": [
                        {"$ref": "#/$defs/GeografiskAdresse"},
                        {
                            "type": "object",
                            "required": ["stedsnavn"],
                            "properties": {"stedsnavn": {"type": "string"}},
                        },
                    ]
                },
                "AnnenAdresse": {
                    "type": "object",
                    "properties": {
                        "stedsadresse": {"$ref": "#/$defs/Stedsadresse"},
                    },
                },
            }
        })
        self.assertIn("Stedsadresse", schema["classes"])
        self.assertEqual(schema["classes"]["Stedsadresse"]["is_a"], "GeografiskAdresse")
        self.assertIn("stedsnavn", schema["classes"]["Stedsadresse"]["slots"])
        self.assertNotIn("id", schema["classes"]["Stedsadresse"]["slots"])
        self.assertEqual(schema["slots"]["stedsadresse"]["range"], "Stedsadresse")
        self.assertEqual([], warnings)

    def test_allof_med_fleire_ref_gir_åtvaring(self):
        schema, warnings = _convert({
            "$defs": {
                "A": {"type": "object", "properties": {"a": {"type": "string"}}},
                "B": {"type": "object", "properties": {"b": {"type": "string"}}},
                "C": {
                    "allOf": [
                        {"$ref": "#/$defs/A"},
                        {"$ref": "#/$defs/B"},
                        {"type": "object", "properties": {"c": {"type": "string"}}},
                    ]
                },
            }
        })
        self.assertIn("C", schema["classes"])
        self.assertEqual(schema["classes"]["C"]["is_a"], "A")
        self.assertTrue(any("Fleire $ref-foreldre" in w for w in warnings))
        # B og C sine felt vert flata ut sidan berre A kan bli is_a
        self.assertIn("b", schema["classes"]["C"]["slots"])
        self.assertIn("c", schema["classes"]["C"]["slots"])

    def test_allof_med_ref_til_ikkje_klasse_gir_åtvaring(self):
        schema, warnings = _convert({
            "$defs": {
                "Kode": {"type": "string"},
                "Ting": {
                    "allOf": [
                        {"$ref": "#/$defs/Kode"},
                        {"type": "object", "properties": {"verdi": {"type": "string"}}},
                    ]
                },
            }
        })
        self.assertIn("Ting", schema["classes"])
        self.assertNotIn("is_a", schema["classes"]["Ting"])
        self.assertTrue(any("peikar ikkje til ein klasse" in w for w in warnings))


# ---------------------------------------------------------------------------
# TestGeneratedOutput
# ---------------------------------------------------------------------------

class TestGeneratedOutput(unittest.TestCase):

    def test_output_er_gyldig_yaml(self):
        yaml_str, _ = convert(
            {
                "$defs": {
                    "Ting": {
                        "type": "object",
                        "properties": {"namn": {"type": "string"}},
                    }
                }
            },
            _policy(),
            schema_id="https://example.org/test",
            schema_name="test",
        )
        parsed = yaml.safe_load(yaml_str)
        self.assertIsInstance(parsed, dict)
        self.assertIn("id", parsed)
        self.assertIn("name", parsed)
        self.assertIn("classes", parsed)
        self.assertIn("slots", parsed)

    def test_schema_kan_lastast_av_schemaview(self):
        from linkml_runtime.utils.schemaview import SchemaView
        yaml_str, _ = convert(
            {
                "$defs": {
                    "Person": {
                        "type": "object",
                        "description": "Ein person.",
                        "properties": {
                            "namn":  {"type": "string", "description": "Fullt namn."},
                            "alder": {"type": "integer"},
                        },
                        "required": ["namn"],
                    }
                }
            },
            _policy(),
            schema_id="https://example.org/test",
            schema_name="test",
            schema_title="Testmodell",
        )
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", delete=False, encoding="utf-8"
        ) as f:
            f.write(yaml_str)
            fname = f.name
        try:
            sv = SchemaView(fname)
            self.assertIn("Person", sv.all_classes())
            self.assertIn("namn",   sv.all_slots())
        finally:
            os.unlink(fname)

    def test_load_policy_les_bronze(self):
        p = load_policy("bronze")
        self.assertEqual(p["version"], 1)
        self.assertIn("type_mapping", p)
        self.assertIn("format_mapping", p)
        self.assertIn("generation", p)


# ---------------------------------------------------------------------------
# TestValidation
# ---------------------------------------------------------------------------

class TestValidation(unittest.TestCase):

    def _valid_yaml(self) -> str:
        yaml_str, _ = convert(
            {
                "$defs": {
                    "Ting": {
                        "type": "object",
                        "properties": {
                            "namn": {"type": "string"},
                        },
                        "required": ["namn"],
                    }
                }
            },
            _policy(),
            schema_id="https://example.org/test",
            schema_name="test",
        )
        return yaml_str

    def test_gyldig_yaml_gir_ingen_parse_feil(self):
        result = validate_generated(self._valid_yaml())
        parse_errors = [i for i in result["lint_issues"] if i["rule"] == "parse_error"]
        self.assertEqual([], parse_errors)

    def test_gyldig_yaml_gir_dummy_validering_med_valid_felt(self):
        result = validate_generated(self._valid_yaml())
        dv = result["dummy_validation"]
        self.assertIn("valid", dv, f"dummy_validation manglar 'valid'-felt: {dv}")

    def test_ugyldig_yaml_gir_parse_feil(self):
        result = validate_generated("dette: er: ikkje: gyldig: yaml:\n  - [")
        parse_errors = [i for i in result["lint_issues"] if i["rule"] == "parse_error"]
        self.assertTrue(len(parse_errors) > 0, "Forventa parse-feil for ugyldig YAML")

    def test_ugyldig_yaml_hoppar_over_dummy_validering(self):
        result = validate_generated("dette: er: ikkje: gyldig: yaml:\n  - [")
        self.assertIn("skipped", result["dummy_validation"])

    def test_skjema_utan_containerklasse_gir_skipped(self):
        no_container_yaml = """
id: https://example.org/test
name: test
prefixes:
  linkml: https://w3id.org/linkml/
imports:
  - linkml:types
classes:
  Ting:
    class_uri: ex:Ting
slots: {}
"""
        result = validate_generated(no_container_yaml)
        self.assertIn("skipped", result["dummy_validation"])
        self.assertNotIn("parse_error", [i["rule"] for i in result["lint_issues"]])

    def test_resultat_har_rett_struktur(self):
        result = validate_generated(self._valid_yaml())
        self.assertIn("lint_issues", result)
        self.assertIn("dummy_validation", result)
        self.assertIsInstance(result["lint_issues"], list)
        self.assertIsInstance(result["dummy_validation"], dict)


# ---------------------------------------------------------------------------
# TestMCPProtocol
# ---------------------------------------------------------------------------

def _call(method: str, params: dict = None, msg_id: int = 1) -> dict:
    msg = {"jsonrpc": "2.0", "id": msg_id, "method": method}
    if params is not None:
        msg["params"] = params
    return handle(msg)


class TestMCPProtocol(unittest.TestCase):

    def test_initialize_returnerer_server_info(self):
        resp = _call("initialize")
        self.assertEqual(resp["result"]["serverInfo"]["name"], "mcp-linkml-modell-utkast")
        self.assertIn("capabilities", resp["result"])
        self.assertIn("protocolVersion", resp["result"])

    def test_initialized_returnerer_none(self):
        resp = handle({"jsonrpc": "2.0", "method": "initialized"})
        self.assertIsNone(resp)

    def test_tools_list_inneheld_begge_verktøy(self):
        resp = _call("tools/list")
        names = [t["name"] for t in resp["result"]["tools"]]
        self.assertIn("generate_linkml", names)
        self.assertIn("list_policies", names)

    def test_ukjent_verktøy_gir_32602(self):
        resp = _call("tools/call", {"name": "ikkje_eit_verktøy", "arguments": {}})
        self.assertEqual(resp["error"]["code"], -32602)

    def test_ukjend_metode_gir_32601(self):
        resp = _call("finnes_ikkje")
        self.assertEqual(resp["error"]["code"], -32601)

    def test_generate_json_schema_med_gyldig_input_gir_gyldig_yaml(self):
        json_schema = json.dumps({
            "$defs": {
                "Ting": {
                    "type": "object",
                    "properties": {"namn": {"type": "string"}},
                }
            }
        })
        resp = _call("tools/call", {
            "name": "generate_linkml",
            "arguments": {
                "inputFormat":  "json-schema",
                "inputContent": json_schema,
                "schemaId":     "https://example.org/test",
                "schemaName":   "test",
            },
        })
        result = json.loads(resp["result"]["content"][0]["text"])
        parsed = yaml.safe_load(result["linkmlSchema"])
        self.assertIsInstance(parsed, dict)
        self.assertIn("classes", parsed)

    def test_generate_empty_gir_stub_schema(self):
        resp = _call("tools/call", {
            "name": "generate_linkml",
            "arguments": {
                "inputFormat": "empty",
                "schemaId":    "https://example.org/test",
                "schemaName":  "test",
            },
        })
        result = json.loads(resp["result"]["content"][0]["text"])
        parsed = yaml.safe_load(result["linkmlSchema"])
        self.assertIsInstance(parsed, dict)
        self.assertIn("id", parsed)
        self.assertIn("name", parsed)

    def test_generate_med_validate_false_gir_tome_lint_issues(self):
        resp = _call("tools/call", {
            "name": "generate_linkml",
            "arguments": {
                "inputFormat":  "json-schema",
                "inputContent": json.dumps({"type": "object", "properties": {}}),
                "schemaId":     "https://example.org/test",
                "schemaName":   "test",
                "validate":     False,
            },
        })
        result = json.loads(resp["result"]["content"][0]["text"])
        self.assertEqual([], result["lintIssues"])

    def test_generate_med_ukjend_policy_gir_32602(self):
        resp = _call("tools/call", {
            "name": "generate_linkml",
            "arguments": {
                "inputFormat": "json-schema",
                "inputContent": "{}",
                "schemaId":    "https://example.org/test",
                "schemaName":  "test",
                "policy":      "finnes-ikkje",
            },
        })
        self.assertEqual(resp["error"]["code"], -32602)

    def test_generate_med_ugyldig_json_schema_gir_32602(self):
        resp = _call("tools/call", {
            "name": "generate_linkml",
            "arguments": {
                "inputFormat":  "json-schema",
                "inputContent": "dette er ikkje json",
                "schemaId":     "https://example.org/test",
                "schemaName":   "test",
            },
        })
        self.assertEqual(resp["error"]["code"], -32602)

    def test_generate_med_ugyldig_format_gir_32602(self):
        resp = _call("tools/call", {
            "name": "generate_linkml",
            "arguments": {
                "inputFormat": "ikkje-eit-format",
                "schemaId":    "https://example.org/test",
                "schemaName":  "test",
            },
        })
        self.assertEqual(resp["error"]["code"], -32602)

    def test_ugyldig_json_i_stdin_gir_32700(self):
        import importlib.util
        import subprocess
        spec = importlib.util.find_spec("server")
        server_path = spec.origin if spec else None
        self.assertIsNotNone(server_path, "server.py ikkje funne via importlib")
        proc = subprocess.run(
            [sys.executable, server_path],
            input="dette er ikkje json\n",
            capture_output=True,
            text=True,
            timeout=10,
        )
        responses = [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]
        self.assertTrue(
            any(r.get("error", {}).get("code") == -32700 for r in responses),
            f"Forventa -32700 i respons, fekk: {responses}",
        )

    def test_generate_result_har_rett_nøklar(self):
        resp = _call("tools/call", {
            "name": "generate_linkml",
            "arguments": {
                "inputFormat":  "json-schema",
                "inputContent": json.dumps({"type": "object", "properties": {}}),
                "schemaId":     "https://example.org/test",
                "schemaName":   "test",
                "validate":     False,
            },
        })
        result = json.loads(resp["result"]["content"][0]["text"])
        for key in ("linkmlSchema", "warnings", "lintIssues", "dummyValidation"):
            self.assertIn(key, result)


# ---------------------------------------------------------------------------
# TestListPolicies
# ---------------------------------------------------------------------------

class TestListPolicies(unittest.TestCase):

    def _policies(self) -> list:
        resp = _call("tools/call", {"name": "list_policies", "arguments": {}})
        return json.loads(resp["result"]["content"][0]["text"])

    def test_returnerer_minst_bronze(self):
        names = [p["name"] for p in self._policies()]
        self.assertIn("bronze", names)

    def test_kvar_policy_har_name_og_description(self):
        for p in self._policies():
            self.assertIn("name", p)
            self.assertIn("description", p)

    def test_bronze_har_ikkje_tom_description(self):
        bronze = next(p for p in self._policies() if p["name"] == "bronze")
        self.assertGreater(len(bronze["description"]), 0)


if __name__ == "__main__":
    unittest.main()
