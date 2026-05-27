#!/usr/bin/env python3
import json, sys

schema = sys.argv[1]
result = json.loads(sys.stdin.read())
issues = result.get('issues', [])
for i in issues:
    sev = 'error' if i.get('severity') == 'error' else 'warning'
    msg = i.get('message', '').replace('\n', ' ')
    target = i.get('target', '')
    print(f'::{sev} file={schema}::{target} – {msg}')
sys.exit(0 if result.get('valid', True) else 1)
