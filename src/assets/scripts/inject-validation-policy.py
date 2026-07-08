#!/usr/bin/env python3
"""
Injiser validation_policy frå build.yaml i Metadata-tabellen i index.md.

Usage:
    inject-validation-policy.py <index.md> <build.yaml>
"""
import sys
from pathlib import Path
import yaml

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <index.md> <build.yaml>", file=sys.stderr)
        sys.exit(1)

    index_path = Path(sys.argv[1])
    manifest_path = Path(sys.argv[2])

    # Les build.yaml
    if not manifest_path.exists():
        # Ingen manifest, bruk bronze som default
        policy = "bronze"
    else:
        with open(manifest_path, encoding="utf-8") as f:
            manifest = yaml.safe_load(f)
        policy = manifest.get("validation_policy", "bronze")

    # Les index.md
    content = index_path.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Finn Metadata-tabellen og legg til validation_policy rett før Imports (eller etter siste felt)
    new_lines = []
    in_metadata_table = False
    policy_injected = False

    for i, line in enumerate(lines):
        # Sjekk om me er i Metadata-tabellen
        if line.startswith("## Metadata"):
            in_metadata_table = True
        elif in_metadata_table and line.startswith("##"):
            # Slutt på Metadata-seksjon
            in_metadata_table = False

        # Injiser validation_policy rett før Imports-linja eller rett før slutten av tabellen
        if in_metadata_table and not policy_injected:
            if line.startswith("| Imports |") or (line == "" and i > 0 and lines[i-1].startswith("|")):
                # Injiser før Imports eller etter siste tabellinje
                new_lines.append(f"| Validation policy | {policy} |")
                policy_injected = True

        new_lines.append(line)

    # Skriv tilbake
    index_path.write_text("\n".join(new_lines), encoding="utf-8")

if __name__ == "__main__":
    main()
