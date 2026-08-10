#!/usr/bin/env python3
"""
Detekter validation_policy frå build.yaml.
Les build.yaml frå same katalog som skjemaet og emit policy til stdout.
Returnerer 'bronze' som default dersom build.yaml ikkje finst eller manglar policy.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src" / "assets" / "scripts"))
from utils.schema_meta import detect_policy  # noqa: E402


def main():
    if len(sys.argv) < 2:
        print("Bruk: detect-validation-policy.py <schema>", file=sys.stderr)
        sys.exit(1)

    print(detect_policy(Path(sys.argv[1])))


if __name__ == '__main__':
    main()
