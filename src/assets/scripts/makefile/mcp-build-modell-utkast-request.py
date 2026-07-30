#!/usr/bin/env python3
"""
Bygg JSON-RPC-request for mcp-linkml-modell-utkast.
Les skjema-fil og emit initialize + generate_linkml-meldingar til stdout.
"""
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Bruk: mcp-build-modell-utkast-request.py <schema> [format] [profile]", file=sys.stderr)
        sys.exit(1)

    schema_path = Path(sys.argv[1])
    fmt = sys.argv[2] if len(sys.argv) > 2 else "json-schema"
    profile = sys.argv[3] if len(sys.argv) > 3 else "bronze"

    if not schema_path.exists():
        print(f"Feil: {schema_path} finst ikkje", file=sys.stderr)
        sys.exit(1)

    content = schema_path.read_text(encoding='utf-8')

    msgs = [
        {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {}},
        {
            'jsonrpc': '2.0',
            'id': 2,
            'method': 'tools/call',
            'params': {
                'name': 'generate_linkml',
                'arguments': {
                    'inputFormat': fmt,
                    'inputContent': content,
                    'schemaId': 'https://example.org/generated',
                    'schemaName': 'generated',
                    'profile': profile,
                }
            }
        }
    ]

    for msg in msgs:
        print(json.dumps(msg))

if __name__ == '__main__':
    main()
