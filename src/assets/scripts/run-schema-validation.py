#!/usr/bin/env python3
"""
Køyrer mcp-validate for kvart releasja skjema og lagrar resultata som JSON.

- Hentar policy frå manifest.yaml sitt data_policy-felt (fallback: bronze)
- Lagrar validation/<domain>/<model>/<version>.json og latest.json

Ingen eksterne avhengigheiter — berre Python stdlib.
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path


def get_policy(schema_path: Path) -> str:
    manifest = schema_path.parent / "manifest.yaml"
    if manifest.exists():
        content = manifest.read_text(encoding="utf-8")
        m = re.search(r"^data_policy:\s*(\S+)", content, re.MULTILINE)
        return m.group(1) if m else "bronze"
    return "bronze"


def get_version(schema_path: Path) -> str:
    content = schema_path.read_text(encoding="utf-8")
    m = re.search(r'^version:\s*"([^"]+)"', content, re.MULTILINE)
    return m.group(1) if m else "0.0.0"


def get_domain_model(schema_path: Path) -> tuple[str, str]:
    """Utlei domain og modellnamn frå skjemastien."""
    model = schema_path.parent.name
    domain = schema_path.parent.parent.name
    if domain == "linkml":
        domain = model
    return domain, model


def run_validation(schema_path: Path, policy: str, dry_run: bool = False) -> dict | None:
    if dry_run:
        print(f"  [dry-run] ville validert {schema_path} med policy {policy}")
        return None

    print(f"  Validerer {schema_path} (policy: {policy}) ...")
    result = subprocess.run(
        ["bash", "src/mcp-linkml-validator/flatten-and-validate.bash",
         str(schema_path), policy],
        capture_output=True,
        text=True,
    )
    if not result.stdout.strip():
        print(f"  FEIL: ingen output frå validator:\n{result.stderr[:300]}", file=sys.stderr)
        return None

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"  FEIL: ugyldig JSON frå validator: {e}", file=sys.stderr)
        return None

    errors = [i for i in data.get("issues", []) if i.get("severity") == "error"]
    warnings = [i for i in data.get("issues", []) if i.get("severity") == "warning"]
    return {
        "valid": data.get("valid", False),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "issues": data.get("issues", []),
    }


def save_report(
    domain: str,
    model: str,
    version: str,
    policy: str,
    result: dict,
    dry_run: bool = False,
) -> None:
    report = {
        "schema": model,
        "domain": domain,
        "version": version,
        "validated_at": date.today().isoformat(),
        "data_policy": policy,
        "result": result,
    }

    out_dir = Path("validation") / domain / model
    versioned = out_dir / f"{version}.json"
    latest = out_dir / "latest.json"

    if dry_run:
        print(f"  [dry-run] ville skrive {versioned} og {latest}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    versioned.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")

    status = "✅" if result.get("valid") else "❌"
    print(
        f"  {status} {versioned} "
        f"({result.get('error_count', 0)} feil, {result.get('warning_count', 0)} åtv.)"
    )


def find_released_packages(config: dict) -> list[str]:
    """Same logikk som i update-schema-dates.py — manifest-diff mellom HEAD~1 og HEAD."""
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


def process_schema(schema_path: Path, dry_run: bool) -> None:
    domain, model = get_domain_model(schema_path)
    version = get_version(schema_path)
    policy = get_policy(schema_path)

    print(f"\n{schema_path} (v{version}, policy: {policy}):")
    result = run_validation(schema_path, policy, dry_run)
    if result is not None or dry_run:
        save_report(domain, model, version, policy, result or {}, dry_run)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fang valideringsresultat per skjema")
    parser.add_argument(
        "--config",
        default="release-please-config.json",
        help="Sti til release-please-config.json",
    )
    parser.add_argument(
        "--schema",
        help="Sti til enkelt skjemafil (køyr berre for denne)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Vis kva som ville skjedd utan å skrive")
    args = parser.parse_args()

    config_path = Path(args.config)
    try:
        config = json.loads(config_path.read_text())
    except Exception as e:
        print(f"FEIL: kunne ikkje lese {config_path}: {e}", file=sys.stderr)
        sys.exit(1)

    if args.schema:
        schema_path = Path(args.schema)
        if not schema_path.exists():
            print(f"FEIL: {schema_path} finst ikkje", file=sys.stderr)
            sys.exit(1)
        process_schema(schema_path, args.dry_run)
        return

    released = find_released_packages(config)
    if not released:
        print("Ingen pakkar releasja — ingenting å gjere.")
        return

    print(f"Releasja pakkar: {released}")
    for pkg_path in released:
        pkg_config = config.get("packages", {}).get(pkg_path, {})
        extra_files = pkg_config.get("extra-files", [])
        if not extra_files:
            continue
        schema_rel = extra_files[0].get("path")
        if not schema_rel:
            continue
        schema_path = Path(schema_rel)
        if not schema_path.exists():
            print(f"  ÅTVARING: {schema_path} finst ikkje", file=sys.stderr)
            continue
        process_schema(schema_path, args.dry_run)


if __name__ == "__main__":
    main()
