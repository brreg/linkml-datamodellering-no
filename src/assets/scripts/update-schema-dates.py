#!/usr/bin/env python3
"""
Oppdaterer datoannotasjonar i skjema-YAML-filer etter ein release.

- annotations.endringsdato: sett alltid til dagens dato
- annotations.utgivelsesdato: sett berre viss feltet manglar (første publisering)

Ingen eksterne avhengigheiter — berre Python stdlib.
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


def update_dates(schema_path: Path, today: str, dry_run: bool = False) -> bool:
    content = schema_path.read_text(encoding="utf-8")
    original = content

    if not re.search(r"^annotations:", content, re.MULTILINE):
        print(f"  HOPP OVER: ingen annotations-seksjon på toppnivå — {schema_path}", file=sys.stderr)
        return False

    if re.search(r"^  endringsdato:", content, re.MULTILINE):
        content = re.sub(
            r'^(  endringsdato:\s*")[^"]*(")',
            rf"\g<1>{today}\2",
            content,
            flags=re.MULTILINE,
        )
    else:
        content = re.sub(
            r"^(annotations:\n)",
            rf'\1  endringsdato: "{today}"\n',
            content,
            flags=re.MULTILINE,
        )

    if not re.search(r"^  utgivelsesdato:", content, re.MULTILINE):
        content = re.sub(
            r'^(  endringsdato: "[^"]*"\n)',
            rf'\1  utgivelsesdato: "{today}"\n',
            content,
            flags=re.MULTILINE,
        )

    if content == original:
        print(f"  UENDRA: {schema_path}")
        return False

    if not dry_run:
        schema_path.write_text(content, encoding="utf-8")

    changed_fields = []
    old_date = re.search(r'endringsdato:\s*"([^"]*)"', original)
    if old_date and old_date.group(1) != today:
        changed_fields.append(f"endringsdato {old_date.group(1)} → {today}")
    elif not old_date:
        changed_fields.append(f"endringsdato (ny) → {today}")
    if not re.search(r"^  utgivelsesdato:", original, re.MULTILINE):
        changed_fields.append(f"utgivelsesdato (ny) → {today}")

    prefix = "[dry-run] " if dry_run else ""
    print(f"  {prefix}OPPDATERT: {schema_path} ({', '.join(changed_fields)})")
    return True


def find_released_packages(config: dict) -> list[str]:
    """Finn pakkar som endra versjon mellom HEAD~1 og HEAD ved å samanlikne manifest."""
    import subprocess

    try:
        old_json = subprocess.check_output(
            ["git", "show", "HEAD~1:.release-please-manifest.json"],
            stderr=subprocess.DEVNULL,
        ).decode()
        old = json.loads(old_json)
    except Exception:
        old = {}

    try:
        new = json.loads(Path(".release-please-manifest.json").read_text())
    except Exception as e:
        print(f"FEIL: kunne ikkje lese .release-please-manifest.json: {e}", file=sys.stderr)
        return []

    return [p for p in new if old.get(p) != new[p] and p in config.get("packages", {})]


def main() -> None:
    parser = argparse.ArgumentParser(description="Oppdater datoannotasjonar etter release")
    parser.add_argument(
        "--released-paths",
        help="JSON-array med pakke-stiar frå release-please (valfri — les manifest-diff viss utelaten)",
    )
    parser.add_argument(
        "--config",
        default="release-please-config.json",
        help="Sti til release-please-config.json",
    )
    parser.add_argument("--dry-run", action="store_true", help="Vis endringar utan å skrive")
    args = parser.parse_args()

    today = date.today().isoformat()
    config_path = Path(args.config)

    try:
        config = json.loads(config_path.read_text())
    except Exception as e:
        print(f"FEIL: kunne ikkje lese {config_path}: {e}", file=sys.stderr)
        sys.exit(1)

    if args.released_paths:
        try:
            released_paths = json.loads(args.released_paths)
        except Exception as e:
            print(f"FEIL: ugyldig JSON i --released-paths: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        released_paths = find_released_packages(config)

    if not released_paths:
        print("Ingen pakkar releasja — ingenting å gjere.")
        return

    print(f"Dato: {today}")
    print(f"Releasja pakkar: {released_paths}")

    changed = 0
    for pkg_path in released_paths:
        pkg_config = config.get("packages", {}).get(pkg_path)
        if not pkg_config:
            print(f"  ÅTVARING: {pkg_path} ikkje funne i {config_path}", file=sys.stderr)
            continue

        extra_files = pkg_config.get("extra-files", [])
        if not extra_files:
            print(f"  ÅTVARING: ingen extra-files for {pkg_path}", file=sys.stderr)
            continue

        schema_rel = extra_files[0].get("path")
        if not schema_rel:
            continue

        schema_path = Path(schema_rel)
        if not schema_path.exists():
            print(f"  ÅTVARING: fila finst ikkje: {schema_path}", file=sys.stderr)
            continue

        print(f"\n{pkg_path}:")
        if update_dates(schema_path, today, dry_run=args.dry_run):
            changed += 1

    print(f"\n{changed} fil(ar) oppdatert.")


if __name__ == "__main__":
    main()
