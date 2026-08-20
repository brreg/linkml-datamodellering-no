#!/usr/bin/env python3
"""
Bygg JSON-RPC-request for mcp-linkml-modell-utkast sitt generate_linkml-verktøy.
Emitter initialize + tools/call-meldingar til stdout.

Delt av make mcp-linkml-modell-utkast (--input-format json-schema, les ei
eksisterande fil) og new-modell.sh (--input-format empty, ingen input-fil).
"""
import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-format", required=True, choices=["json-schema", "empty"])
    parser.add_argument("--input-file", help="Sti til fil som skal konverterast (kravd for json-schema)")
    parser.add_argument("--schema-id", default="https://example.org/generated")
    parser.add_argument("--schema-name", default="generated")
    parser.add_argument("--schema-title", default="")
    parser.add_argument("--policy", default="bronze")
    parser.add_argument("--no-validate", action="store_true", help="Slå av lint/dummy-validering (default: på)")
    args = parser.parse_args()

    input_content = ""
    if args.input_format == "json-schema":
        if not args.input_file:
            print("Feil: --input-file er kravd for --input-format json-schema", file=sys.stderr)
            sys.exit(1)
        input_path = Path(args.input_file)
        if not input_path.exists():
            print(f"Feil: {input_path} finst ikkje", file=sys.stderr)
            sys.exit(1)
        input_content = input_path.read_text(encoding="utf-8")

    msgs = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "generate_linkml",
                "arguments": {
                    "inputFormat": args.input_format,
                    "inputContent": input_content,
                    "schemaId": args.schema_id,
                    "schemaName": args.schema_name,
                    "schemaTitle": args.schema_title,
                    "policy": args.policy,
                    "validate": not args.no_validate,
                },
            },
        },
    ]

    for msg in msgs:
        print(json.dumps(msg))


if __name__ == "__main__":
    main()
