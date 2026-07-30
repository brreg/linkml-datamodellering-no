#!/usr/bin/env python3
"""
Skriv MCP-response til LinkML-skjemafil.
Les JSON-RPC-responsar frå stdin, ekstraher generert LinkML og skriv til fil.
"""
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Bruk: mcp-write-modell-utkast-response.py <schema>", file=sys.stderr)
        sys.exit(1)

    schema_path = Path(sys.argv[1])
    out_path = schema_path.parent / (schema_path.stem + '-schema.yaml')

    # Les JSON-RPC-responsar frå stdin
    for line in sys.stdin:
        response = json.loads(line)

        # Hopp over meldingar som ikkje er frå generate_linkml-kallet
        if response.get('id') != 2:
            continue

        # Ekstraher generert LinkML-skjema
        result = response.get('result', {})
        content = result.get('content', [])
        if not content:
            print("Feil: Ingen content i response", file=sys.stderr)
            sys.exit(1)

        text = content[0].get('text', '')
        if not text:
            print("Feil: Tom text i response", file=sys.stderr)
            sys.exit(1)

        linkml_schema = json.loads(text).get('linkmlSchema', '')
        if not linkml_schema:
            print("Feil: Ingen linkmlSchema i response", file=sys.stderr)
            sys.exit(1)

        # Skriv til fil
        out_path.write_text(linkml_schema, encoding='utf-8')
        print(f"Skriv til: {out_path}")

if __name__ == '__main__':
    main()
