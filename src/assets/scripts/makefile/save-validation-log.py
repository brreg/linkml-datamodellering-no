#!/usr/bin/env python3
"""
Lagrar valideringsresultat frå validate.yml som JSON i validation/logs/.

- Skriv til validation/logs/<domain>/<model>/<version>/<type>.json
- <type> er 'bronze', 'examples', 'data', eller policy-namn frå manifest
- Versjonsnummer henta frå version:-feltet i skjemaet (fallback: 0.0.0-dev)

Ingen eksterne avhengigheiter — berre Python stdlib.

Bruk:
  python3 save-validation-log.py \\
    --schema src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml \\
    --type bronze \\
    --result '{"valid": true, "issues": []}'
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def get_version(schema_path: Path) -> str:
    """Hent versjonsnummer frå version:-feltet i skjemaet."""
    if not schema_path.exists():
        return "0.0.0-dev"
    content = schema_path.read_text(encoding="utf-8")
    m = re.search(r'^version:\s*"([^"]+)"', content, re.MULTILINE)
    return m.group(1) if m else "0.0.0-dev"


def get_domain_model(schema_path: Path) -> tuple[str, str]:
    """Utlei domain og modellnamn frå skjemastien."""
    model = schema_path.parent.name
    domain = schema_path.parent.parent.name
    if domain == "linkml":
        # src/linkml/referanse/referanse-schema.yaml → domain=referanse
        domain = model
    return domain, model


def get_schema_name(schema_path: Path) -> str:
    """Hent skjemanamn utan -schema.yaml-suffiks."""
    return schema_path.stem.removesuffix("-schema")


def save_log(
    schema_path: Path,
    validation_type: str,
    result_json: str,
    output_dir: Path = Path("validation/logs"),
) -> None:
    """
    Lagrar valideringsresultat til validation/logs/<domain>/<model>/<version>/<type>.json.

    Args:
        schema_path: Sti til skjemafila (*.yaml)
        validation_type: Type validering (bronze/examples/data/<policy>)
        result_json: JSON-streng frå flatten-and-validate.bash
        output_dir: Rotmappe for loggar (standard: validation/logs)
    """
    domain, model = get_domain_model(schema_path)
    schema_name = get_schema_name(schema_path)
    version = get_version(schema_path)

    # Parse result-JSON
    try:
        result = json.loads(result_json)
    except json.JSONDecodeError as e:
        print(f"FEIL: Ugyldig JSON i --result: {e}", file=sys.stderr)
        sys.exit(1)

    # Bygg opp logg-objektet
    log_entry = {
        "schema": schema_name,
        "domain": domain,
        "version": version,
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "validation_type": validation_type,
        "result": result,
    }

    # Skriv til validation/logs/<domain>/<model>/<version>/<type>.json
    log_dir = output_dir / domain / model / version
    log_dir.mkdir(parents=True, exist_ok=True)

    # Filnamn basert på validation_type (t.d. bronze.json, examples.json, data.json)
    log_file = log_dir / f"{validation_type}.json"
    log_file.write_text(json.dumps(log_entry, indent=2, ensure_ascii=False) + "\n")

    print(f"✓ Lagra {log_file}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Lagrar valideringsresultat frå validate.yml til validation/logs/"
    )
    parser.add_argument(
        "--schema",
        type=Path,
        required=True,
        help="Sti til skjemafila (t.d. src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml)",
    )
    parser.add_argument(
        "--type",
        required=True,
        help="Valideringstype (bronze/examples/data/<policy>)",
    )
    parser.add_argument(
        "--result",
        required=True,
        help="JSON-resultat frå flatten-and-validate.bash eller linkml validate",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("validation/logs"),
        help="Rotmappe for loggar (standard: validation/logs)",
    )

    args = parser.parse_args()
    save_log(args.schema, args.type, args.result, args.output_dir)


if __name__ == "__main__":
    main()
