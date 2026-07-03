#!/usr/bin/env python3
"""
Filtrer ut valideringsloggar som er identiske med eksisterande loggar i git.
Ignorer validated_at-feltet i samanlikning.

Bruk:
  python3 filter-unchanged-logs.py

Køyrer frå repo-root og filtrerer alle valideringsloggar under src/linkml/*/validation/
"""

import json
import sys
from pathlib import Path
import subprocess


def load_json_without_timestamp(file_path):
    """Last JSON og fjern validated_at-feltet."""
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        data.pop("validated_at", None)
        return data
    except Exception as e:
        print(f"Åtvaring: kunne ikkje lese {file_path}: {e}", file=sys.stderr)
        return None


def main():
    """Finn og filtrer alle valideringsloggar under src/linkml/"""
    src_path = Path("src/linkml")

    if not src_path.exists():
        print("Feil: src/linkml/ finst ikkje — køyr frå repo-root", file=sys.stderr)
        sys.exit(1)

    unchanged_count = 0
    changed_count = 0
    new_count = 0

    for log_file in src_path.rglob("validation/**/*.json"):
        # Les ny logg (utan validated_at)
        new_log = load_json_without_timestamp(log_file)
        if new_log is None:
            continue

        # Hent eksisterande logg frå git HEAD (dersom den finst)
        try:
            result = subprocess.run(
                ["git", "show", f"HEAD:{log_file}"],
                capture_output=True,
                text=True,
                check=True
            )
            old_log = json.loads(result.stdout)
            old_log.pop("validated_at", None)

            # Samanlikn JSON (utan validated_at)
            if new_log == old_log:
                print(f"Identisk logg (fjernar): {log_file}")
                # Tilbakestill til HEAD-versjon (fjernar endring)
                subprocess.run(["git", "checkout", "HEAD", str(log_file)], check=True)
                unchanged_count += 1
            else:
                print(f"Endra logg (beheld): {log_file}")
                changed_count += 1

        except subprocess.CalledProcessError:
            # Fila finst ikkje i git HEAD — det er ein ny logg
            print(f"Ny logg (beheld): {log_file}")
            new_count += 1

    # Samandrag
    total = unchanged_count + changed_count + new_count
    print(f"\nSamandrag: {total} loggar prosesserte", file=sys.stderr)
    print(f"  - {unchanged_count} identiske (fjerna)", file=sys.stderr)
    print(f"  - {changed_count} endra (behelde)", file=sys.stderr)
    print(f"  - {new_count} nye (behelde)", file=sys.stderr)


if __name__ == "__main__":
    main()
