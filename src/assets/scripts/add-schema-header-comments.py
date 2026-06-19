#!/usr/bin/env python3
"""
Legg til 2-linja filhovud-kommentar i alle release-please-forvalta skjema.

Kommentaren informerer bidragsytarar om at version/endringsdato/utgivelsesdato
vert forvalta automatisk av CI, og peikar til CONTRIBUTING.md for detaljar.

Køyr éin gong etter at felta er på plass. Idempotent — hoppar over filer
som allereie har kommentaren.
"""
import argparse
import json
import sys
from pathlib import Path

COMMENT_1 = "# version, endringsdato og utgivelsesdato vert automatisk oppdatert av CI."
COMMENT_2 = "# Sjå CONTRIBUTING.md for detaljar om kva som er manuelt vs. automatisk."
MARKER = "version, endringsdato og utgivelsesdato vert automatisk oppdatert av CI"

COMMENT_1_HASH = "## version, endringsdato og utgivelsesdato vert automatisk oppdatert av CI."
COMMENT_2_HASH = "## Sjå CONTRIBUTING.md for detaljar om kva som er manuelt vs. automatisk."


def add_header(schema_path: Path, dry_run: bool = False) -> bool:
    content = schema_path.read_text(encoding="utf-8")

    if MARKER in content:
        print(f"  ALLEREIE LAGT TIL: {schema_path}")
        return False

    if content.startswith("##"):
        # Skjema har eksisterande ##-blokk — sett inn to ## liner rett før avsluttande ##
        lines = content.split("\n")
        # Finn siste ## i opningsblokka (sett inn to nye liner rett foran den)
        closing_hash = -1
        for i, line in enumerate(lines):
            if not line.startswith("##") and line.strip() != "":
                break
            if line.startswith("##"):
                closing_hash = i
        if closing_hash < 0:
            print(f"  ÅTVARING: fann ikkje avsluttande ## i {schema_path}", file=sys.stderr)
            return False
        lines.insert(closing_hash, COMMENT_2_HASH)
        lines.insert(closing_hash, COMMENT_1_HASH)
        new_content = "\n".join(lines)
    else:
        new_content = f"{COMMENT_1}\n{COMMENT_2}\n\n{content}"

    if not dry_run:
        schema_path.write_text(new_content, encoding="utf-8")

    prefix = "[dry-run] " if dry_run else ""
    print(f"  {prefix}LAGT TIL: {schema_path}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Legg til filhovud-kommentar i skjema")
    parser.add_argument(
        "--config",
        default="release-please-config.json",
        help="Sti til release-please-config.json",
    )
    parser.add_argument("--dry-run", action="store_true", help="Vis endringar utan å skrive")
    args = parser.parse_args()

    config_path = Path(args.config)
    try:
        config = json.loads(config_path.read_text())
    except Exception as e:
        print(f"FEIL: kunne ikkje lese {config_path}: {e}", file=sys.stderr)
        sys.exit(1)

    changed = 0
    skipped = 0
    for pkg_path, pkg_config in config.get("packages", {}).items():
        extra_files = pkg_config.get("extra-files", [])
        if not extra_files:
            continue
        schema_rel = extra_files[0].get("path")
        if not schema_rel:
            continue
        schema_path = Path(schema_rel)
        if not schema_path.exists():
            print(f"  ÅTVARING: fila finst ikkje: {schema_path}", file=sys.stderr)
            skipped += 1
            continue
        if add_header(schema_path, dry_run=args.dry_run):
            changed += 1
        else:
            skipped += 1

    print(f"\n{changed} fil(ar) oppdatert, {skipped} hoppa over.")


if __name__ == "__main__":
    main()
