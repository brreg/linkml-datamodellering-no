#!/usr/bin/env python3
"""
Emit GitHub Actions annotations (error/warning) frå MCP-valideringsresultat.
Les JSON frå stdin og skriv annotations til stdout.
Returnerer exitkode 0 ved valid=true, 1 elles.
"""
import json
import sys
import os

def main():
    # Les JSON-resultat frå stdin
    result = json.loads(sys.stdin.read())

    # Hent schema frå miljøvariabel
    schema = os.environ.get('SCHEMA', '')

    # Emit annotasjonar for kvart issue
    for issue in result.get('issues', []):
        severity = 'error' if issue.get('severity') == 'error' else 'warning'
        target = issue.get('target', '')
        message = issue.get('message', '').replace('\n', ' ')
        print(f'::{severity} file={schema}::{target}: {message}')

    # Returner exitkode basert på valid-flagg
    sys.exit(0 if result.get('valid', True) else 1)

if __name__ == '__main__':
    main()
