#!/usr/bin/env python3
"""
Oppdaterer version og datoannotasjonar i skjema-YAML-filer etter ein release.

- version: sett til verdien frå release-please-manifest.json, men berre
  dersom han er endra (unngår unødvendige diff-ar)
- annotations.endringsdato: sett til dagens dato når version endrar seg
- annotations.utgivelsesdato: sett berre viss feltet manglar (første publisering)

Skjemastien for kvar pakke vert utleia direkte frå pakke-stien i manifestet:
<pkg_path>/<basename(pkg_path)>-schema.yaml — same mønster som CONVENTIONS.md
§ "Fil- og mappenavn" krev for alle modellkatalogar. Krev difor ingen
`extra-files`-konfigurasjon i release-please-config.json.

Ingen eksterne avhengigheiter — berre Python stdlib.
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


def resolve_schema_path(pkg_path: str) -> Path:
    """<pkg_path>/<basename(pkg_path)>-schema.yaml — konvensjonen for alle modellkatalogar."""
    name = Path(pkg_path).name
    return Path(pkg_path) / f"{name}-schema.yaml"


def read_version(schema_path: Path) -> str | None:
    match = re.search(r'^version:\s*"?([^"\n]+?)"?\s*$', schema_path.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1) if match else None


def update_version(content: str, new_version: str) -> str:
    return re.sub(r'^version:.*$', f'version: "{new_version}"', content, count=1, flags=re.MULTILINE)


def update_dates(content: str, today: str) -> str:
    if not re.search(r"^annotations:", content, re.MULTILINE):
        return content

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

    return content


def sync_package(pkg_path: str, manifest_version: str, today: str, dry_run: bool) -> bool:
    schema_path = resolve_schema_path(pkg_path)
    if not schema_path.exists():
        print(f"  ÅTVARING: {schema_path} finst ikkje ({pkg_path})", file=sys.stderr)
        return False

    current_version = read_version(schema_path)
    if current_version == manifest_version:
        return False

    content = schema_path.read_text(encoding="utf-8")
    content = update_version(content, manifest_version)
    content = update_dates(content, today)

    prefix = "[dry-run] " if dry_run else ""
    print(f"  {prefix}OPPDATERT: {schema_path} (version {current_version} → {manifest_version})")

    if not dry_run:
        schema_path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Synkroniser version/endringsdato/utgivelsesdato frå release-please-manifest")
    parser.add_argument(
        "--manifest",
        default=".github/release-please-manifest.json",
        help="Sti til release-please-manifest.json",
    )
    parser.add_argument(
        "--print-schema-path",
        metavar="PKG_PATH",
        help="Skriv ut skjemastien for éin pakke og avslutt (brukt av artefakt-/tag-steg i release-please.yml)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Vis endringar utan å skrive")
    args = parser.parse_args()

    if args.print_schema_path:
        schema_path = resolve_schema_path(args.print_schema_path)
        if not schema_path.exists():
            print(f"FEIL: {schema_path} finst ikkje", file=sys.stderr)
            sys.exit(1)
        print(schema_path)
        return

    manifest_path = Path(args.manifest)
    try:
        manifest = json.loads(manifest_path.read_text())
    except Exception as e:
        print(f"FEIL: kunne ikkje lese {manifest_path}: {e}", file=sys.stderr)
        sys.exit(1)

    today = date.today().isoformat()
    changed = 0
    for pkg_path, version in manifest.items():
        if sync_package(pkg_path, version, today, args.dry_run):
            changed += 1

    print(f"\n{changed} fil(ar) oppdatert.")


if __name__ == "__main__":
    main()
