#!/usr/bin/env python3
"""
Validerer eit LinkML-skjema og skriv strukturert JSON-logg til fil.

Bruk:
  python3 validate-and-log.py --schema <schema.yaml> --policy <policy> --log-file <output.json>
  python3 validate-and-log.py --schema <schema.yaml> --policy <policy> --instance <instance.yaml> --log-file <output.json>
"""

import argparse
import json
import sys
import yaml
from datetime import datetime, timezone
from pathlib import Path

# Importer validate_schema frå server.py
sys.path.insert(0, str(Path(__file__).parent))
from server import validate_schema, validate_instance


def extract_metadata(schema_text: str, schema_path: str) -> dict:
    """Ekstraher metadata frå skjema (domain, modell, version)."""
    try:
        schema_dict = yaml.safe_load(schema_text)
        schema_name = schema_dict.get("name", "")
        version = schema_dict.get("version", "")

        # Ekstraher domain og modell frå sti: src/linkml/<domain>/<modell>/<modell>-schema.yaml
        path_parts = Path(schema_path).parts
        if len(path_parts) >= 4 and path_parts[0] == "src" and path_parts[1] == "linkml":
            domain = path_parts[2]
            model = path_parts[3]
        else:
            domain = ""
            model = schema_name

        return {
            "schema": schema_name,
            "domain": domain,
            "version": version,
        }
    except Exception as e:
        print(f"Åtvaring: kunne ikkje ekstrahere metadata: {e}", file=sys.stderr)
        return {
            "schema": "",
            "domain": "",
            "version": "",
        }


def main():
    parser = argparse.ArgumentParser(description="Validerer LinkML-skjema og skriv JSON-logg")
    parser.add_argument("--schema", required=True, help="Sti til schema YAML-fil")
    parser.add_argument("--policy", required=True, help="Valideringspolicy (bronze/silver/gold/...)")
    parser.add_argument("--instance", help="Sti til instans YAML-fil (valfri)")
    parser.add_argument("--log-file", required=True, help="Sti til output JSON-logg")

    args = parser.parse_args()

    # Les skjema
    try:
        schema_text = Path(args.schema).read_text(encoding="utf-8")
    except Exception as e:
        print(f"Feil: kunne ikkje lese skjema {args.schema}: {e}", file=sys.stderr)
        sys.exit(1)

    # Les instans (valfri)
    instance_text = None
    if args.instance:
        try:
            instance_text = Path(args.instance).read_text(encoding="utf-8")
        except Exception as e:
            print(f"Feil: kunne ikkje lese instans {args.instance}: {e}", file=sys.stderr)
            sys.exit(1)

    # Ekstraher metadata
    metadata = extract_metadata(schema_text, args.schema)

    # Køyr validering
    result = validate_schema(schema_text, args.policy, instance_text)

    # Bygg logg-objekt
    log_data = {
        "schema": metadata["schema"],
        "domain": metadata["domain"],
        "version": metadata["version"],
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "validation_type": args.policy,
        "result": result,
    }

    # Skriv til fil med konsistent formatering (sort_keys=True)
    try:
        Path(args.log_file).parent.mkdir(parents=True, exist_ok=True)
        with open(args.log_file, "w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False, sort_keys=True)
        print(f"Valideringslogg skriven til: {args.log_file}", file=sys.stderr)
    except Exception as e:
        print(f"Feil: kunne ikkje skrive logg til {args.log_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Exit med feilkode dersom validering feila
    if not result.get("valid", False):
        sys.exit(1)


if __name__ == "__main__":
    main()
