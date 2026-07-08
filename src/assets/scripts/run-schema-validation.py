#!/usr/bin/env python3
"""
Køyrer mcp-validate for kvart releasja skjema og lagrar resultata som JSON.

- Hentar policy frå build.yaml sitt validation_policy-felt (fallback: bronze)
- Lagrar src/linkml/<domain>/<model>/validation/<version>/<policy>.json

Ingen eksterne avhengigheiter — berre Python stdlib.
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path


def get_policy(schema_path: Path) -> str:
    manifest = schema_path.parent / "build.yaml"
    if manifest.exists():
        content = manifest.read_text(encoding="utf-8")
        m = re.search(r"^validation_policy:\s*(\S+)", content, re.MULTILINE)
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
        "validation_policy": policy,
        "result": result,
    }

    # Co-location: lagrar ved sidan av skjemafila
    out_dir = Path("src/linkml") / domain / model / "validation" / version
    policy_json = out_dir / f"{policy}.json"

    if dry_run:
        print(f"  [dry-run] ville skrive {policy_json}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    policy_json.write_text(text, encoding="utf-8")

    status = "✅" if result.get("valid") else "❌"
    print(
        f"  {status} {policy_json} "
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


def process_schema(schema_path: Path, dry_run: bool) -> dict:
    """Prosesser eitt skjema og returner resultat."""
    domain, model = get_domain_model(schema_path)
    version = get_version(schema_path)
    policy = get_policy(schema_path)

    print(f"\n{schema_path} (v{version}, policy: {policy}):")
    result = run_validation(schema_path, policy, dry_run)
    if result is not None or dry_run:
        save_report(domain, model, version, policy, result or {}, dry_run)

    return {
        "schema": str(schema_path),
        "valid": result.get("valid", False) if result else False,
        "error_count": result.get("error_count", 0) if result else 0,
        "warning_count": result.get("warning_count", 0) if result else 0,
    }


def process_schemas_parallel(schemas: list[Path], dry_run: bool, max_workers: int) -> None:
    """Prosesser fleire skjema parallelt ved å køyre separate Python-prosessar."""
    print(f"\nKøyrer validering av {len(schemas)} skjema med {max_workers} workers...")

    # Skriv skjemaliste til midlertidig fil
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        schema_list_file = f.name
        for schema in schemas:
            f.write(f"{schema}\n")

    try:
        # Køyr xargs for å parallellisere (fungerer både på Linux og WSL)
        # -P N: køyr N jobbar parallelt
        # -I {}: erstatt {} med input-linja
        script_path = Path(__file__).resolve()
        cmd = [
            "xargs",
            "-P", str(max_workers),
            "-I", "{}",
            "python3", str(script_path),
            "--schema", "{}"
        ]
        if dry_run:
            cmd.append("--dry-run")

        with open(schema_list_file, 'r') as input_file:
            result = subprocess.run(
                cmd,
                stdin=input_file,
                capture_output=False,  # La output gå direkte til terminalen
                text=True,
            )

        if result.returncode != 0:
            print(f"\n⚠️  Nokre valideringar feila (exit code: {result.returncode})", file=sys.stderr)

        # Samla statistikk frå genererte JSON-filer
        results = []
        for schema in schemas:
            domain, model = get_domain_model(schema)
            version = get_version(schema)
            policy = get_policy(schema)
            policy_json = Path("src/linkml") / domain / model / "validation" / version / f"{policy}.json"

            if policy_json.exists():
                try:
                    data = json.loads(policy_json.read_text())
                    result_data = data.get("result", {})
                    results.append({
                        "schema": str(schema),
                        "valid": result_data.get("valid", False),
                        "error_count": result_data.get("error_count", 0),
                        "warning_count": result_data.get("warning_count", 0),
                    })
                except Exception as e:
                    print(f"  ÅTVARING: kunne ikkje lese {policy_json}: {e}", file=sys.stderr)

        # Vis samla statistikk
        if results:
            total = len(results)
            valid = sum(1 for r in results if r["valid"])
            total_errors = sum(r["error_count"] for r in results)
            total_warnings = sum(r["warning_count"] for r in results)

            print(f"\n{'='*60}")
            print(f"Totalt: {total} skjema validerte")
            print(f"  ✅ Gyldige: {valid}")
            print(f"  ❌ Ugyldige: {total - valid}")
            print(f"  🐛 Totalt feil: {total_errors}")
            print(f"  ⚠️  Totalt åtvaringar: {total_warnings}")
            print(f"{'='*60}")
    finally:
        # Rydd opp midlertidig fil
        Path(schema_list_file).unlink(missing_ok=True)


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
    parser.add_argument(
        "--parallel",
        type=int,
        default=1,
        help="Tal på parallelle workers (default: 1 for sekvensiell køyring)",
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
    schemas = []
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
        schemas.append(schema_path)

    if not schemas:
        print("Ingen skjema å validere.")
        return

    if args.parallel > 1:
        process_schemas_parallel(schemas, args.dry_run, args.parallel)
    else:
        for schema_path in schemas:
            process_schema(schema_path, args.dry_run)


if __name__ == "__main__":
    main()
