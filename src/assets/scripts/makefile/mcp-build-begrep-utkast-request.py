#!/usr/bin/env python3
"""
Bygg JSON-RPC-request for mcp-linkml-begrep-utkast.
Les JSON-argumentfil og emit initialize + opprett_begrep-meldingar til stdout.
"""
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Bruk: mcp-build-begrep-utkast-request.py <input-json>", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Feil: {input_path} finst ikkje", file=sys.stderr)
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        args = json.load(f)

    msgs = [
        {
            'jsonrpc': '2.0',
            'id': 1,
            'method': 'initialize',
            'params': {
                'protocolVersion': '2024-11-05',
                'capabilities': {},
                'clientInfo': {'name': 'make', 'version': '1'}
            }
        },
        {
            'jsonrpc': '2.0',
            'id': 2,
            'method': 'tools/call',
            'params': {
                'name': 'opprett_begrep',
                'arguments': args
            }
        }
    ]

    for msg in msgs:
        print(json.dumps(msg))

if __name__ == '__main__':
    main()
