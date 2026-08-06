#!/usr/bin/env python3
"""
Lagrar valideringsresultat frå validate.yml som JSON i src/linkml/<domain>/<model>/validation/.

- Skriv til src/linkml/<domain>/<model>/validation/<version>/<type>.json
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
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src" / "assets" / "scripts"))
from utils.schema_meta import get_domain_model, get_version  # noqa: E402
from utils.validation_log import build_validation_log_entry, write_validation_log  # noqa: E402


def get_schema_name(schema_path: Path) -> str:
    """Hent skjemanamn utan -schema.yaml-suffiks."""
    return schema_path.stem.removesuffix("-schema")


def save_log(
    schema_path: Path,
    validation_type: str,
    result_json: str,
    output_dir: Path = Path("src/linkml"),
) -> None:
    """
    Lagrar valideringsresultat til src/linkml/<domain>/<model>/validation/<version>/<type>.json.

    Args:
        schema_path: Sti til skjemafila (*.yaml)
        validation_type: Type validering (bronze/examples/data/<policy>)
        result_json: JSON-streng frå flatten-and-validate.bash
        output_dir: Rotmappe for loggar (standard: src/linkml)
    """
    domain, model = get_domain_model(schema_path)
    schema_name = get_schema_name(schema_path)
    version = get_version(schema_path, fallback="0.0.0-dev")

    # Parse result-JSON
    try:
        result = json.loads(result_json)
    except json.JSONDecodeError as e:
        print(f"FEIL: Ugyldig JSON i --result: {e}", file=sys.stderr)
        sys.exit(1)

    # Bygg opp logg-objektet (delt struktur — sjå utils/validation_log.py, BUG-12)
    log_entry = build_validation_log_entry(schema_name, domain, version, validation_type, result)

    # Skriv til src/linkml/<domain>/<model>/validation/<version>/<type>.json
    # Filnamn basert på validation_type (t.d. bronze.json, examples.json, data.json)
    log_file = output_dir / domain / model / "validation" / version / f"{validation_type}.json"
    write_validation_log(log_file, log_entry)

    print(f"✓ Lagra {log_file}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Lagrar valideringsresultat frå validate.yml til src/linkml/<domain>/<model>/validation/"
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
        default=Path("src/linkml"),
        help="Rotmappe for loggar (standard: src/linkml)",
    )

    args = parser.parse_args()
    save_log(args.schema, args.type, args.result, args.output_dir)


if __name__ == "__main__":
    main()
