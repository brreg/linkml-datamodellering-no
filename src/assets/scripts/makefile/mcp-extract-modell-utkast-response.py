#!/usr/bin/env python3
"""
Les JSON-RPC-responsar frå stdin, ekstraher generert LinkML-skjema frå
generate_linkml-svaret, og skriv til stdout.

Filskriving er kallaren sitt ansvar (Makefile-oppskrifter omdirigerer
stdout til fil, new-modell.sh fangar opp resultatet i ein variabel for
vidare post-prosessering).
"""
import json
import sys


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        response = json.loads(line)

        # Hopp over meldingar som ikkje er frå generate_linkml-kallet
        if response.get('id') != 2:
            continue

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

        sys.stdout.write(linkml_schema)
        return

    print("Feil: Ingen svar med id=2 funne i responsen", file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    main()
