#!/usr/bin/env python3
"""
Detekter validation_policy frå build.yaml.
Les build.yaml frå same katalog som skjemaet og emit policy til stdout.
Returnerer 'bronze' som default dersom build.yaml ikkje finst eller manglar policy.
"""
import sys
import yaml
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Bruk: detect-validation-policy.py <schema>", file=sys.stderr)
        sys.exit(1)

    schema_path = Path(sys.argv[1])
    manifest_path = schema_path.parent / "build.yaml"

    if not manifest_path.exists():
        print("bronze")
        return

    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = yaml.safe_load(f)

        policy = manifest.get('validation_policy', 'bronze')
        print(policy)

    except Exception:
        print("bronze")

if __name__ == '__main__':
    main()
