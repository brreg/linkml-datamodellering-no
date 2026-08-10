#!/usr/bin/env python3
"""
Køyrer valideringssteget for kvart releasja skjema og lagrar resultata som JSON.

- Hentar policy frå build.yaml sitt validation_policy-felt (utils.schema_meta.detect_policy)
- Fleire skjema (alle releasja pakkar) vert batcha til éin mcp-linkml-
  validator-kontainar via batch-flatten-and-validate.py — same mekanisme
  som validate-bronze/validate-data alt brukar
- Eitt skjema (--schema) validerast direkte via flatten-and-validate.bash —
  ingen kontainar-amortisering å hente ved N=1
- Lagrar via same delte format som validate-bronze/validate-data
  (utils.validation_log.build_validation_log_entry/write_validation_log)
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src" / "assets" / "scripts"))
from utils.release_helpers import find_released_packages  # noqa: E402
from utils.schema_meta import detect_policy, get_domain_model, get_version  # noqa: E402
from utils.validation_log import build_validation_log_entry, write_validation_log  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR_DIR = REPO_ROOT / "src" / "mcp-linkml-validator"


def save_result(schema_path: Path, policy: str, result: dict, dry_run: bool = False) -> None:
    domain, model = get_domain_model(schema_path)
    version = get_version(schema_path)
    schema_name = schema_path.stem.removesuffix("-schema")
    log_file = (
        REPO_ROOT / "src" / "linkml" / domain / model / "validation" / version / f"{policy}.json"
    )

    if dry_run:
        print(f"  [dry-run] ville skrive {log_file}")
        return

    entry = build_validation_log_entry(schema_name, domain, version, policy, result)
    write_validation_log(log_file, entry)

    status = "✅" if result.get("valid", False) else "❌"
    print(
        f"  {status} {log_file} "
        f"({result.get('errorCount', 0)} feil, {result.get('warningCount', 0)} åtv.)"
    )


def process_schema(schema_path: Path, dry_run: bool) -> dict:
    """Valider eitt enkelt skjema direkte (ingen batching — brukt for --schema)."""
    policy = detect_policy(schema_path)
    print(f"\n{schema_path} (policy: {policy}):")

    if dry_run:
        print(f"  [dry-run] ville validert {schema_path} med policy {policy}")
        save_result(schema_path, policy, {}, dry_run=True)
        return {"schema": str(schema_path), "valid": False, "error_count": 0, "warning_count": 0}

    proc = subprocess.run(
        ["bash", str(VALIDATOR_DIR / "flatten-and-validate.bash"), str(schema_path), policy],
        capture_output=True,
        text=True,
    )
    if not proc.stdout.strip():
        print(f"  FEIL: ingen output frå validator:\n{proc.stderr[:300]}", file=sys.stderr)
        result = {
            "valid": False, "errorCount": 1, "warningCount": 0,
            "issues": [{"severity": "error", "code": "no_validator_output", "target": "schema",
                        "message": "Ingen output frå flatten-and-validate.bash"}],
        }
    else:
        try:
            result = json.loads(proc.stdout)
        except json.JSONDecodeError as e:
            print(f"  FEIL: ugyldig JSON frå validator: {e}", file=sys.stderr)
            result = {
                "valid": False, "errorCount": 1, "warningCount": 0,
                "issues": [{"severity": "error", "code": "invalid_validator_output", "target": "schema",
                            "message": str(e)}],
            }

    save_result(schema_path, policy, result)
    return {
        "schema": str(schema_path),
        "valid": result.get("valid", False),
        "error_count": result.get("errorCount", 0),
        "warning_count": result.get("warningCount", 0),
    }


def process_schemas_batch(schemas: list[Path], dry_run: bool) -> None:
    """Valider fleire skjema i éin delt mcp-linkml-validator-kontainar."""
    jobs = [(schema, detect_policy(schema)) for schema in schemas]

    if dry_run:
        print(f"\nKøyrer batcha validering av {len(jobs)} skjema ...")
        for schema, policy in jobs:
            print(f"  [dry-run] ville validert {schema} med policy {policy}")
            save_result(schema, policy, {}, dry_run=True)
        return

    print(f"\nKøyrer batcha validering av {len(jobs)} skjema i éin kontainar ...")
    with tempfile.TemporaryDirectory() as tmpdir_str:
        tmpdir = Path(tmpdir_str)
        jobs_tsv = tmpdir / "jobs.tsv"
        jobs_tsv.write_text(
            "".join(f"{schema}\t{policy}\t\n" for schema, policy in jobs),
            encoding="utf-8",
        )
        output_dir = tmpdir / "results"
        subprocess.run(
            ["python3", str(VALIDATOR_DIR / "batch-flatten-and-validate.py"),
             "--jobs-tsv", str(jobs_tsv),
             "--output-dir", str(output_dir),
             "--repo-root", str(REPO_ROOT)],
            check=False,
        )

        results = []
        for idx, (schema, policy) in enumerate(jobs):
            result_file = output_dir / f"{idx}.json"
            if result_file.exists():
                result = json.loads(result_file.read_text(encoding="utf-8"))
            else:
                print(f"  ÅTVARING: manglar batch-resultat for {schema}", file=sys.stderr)
                result = {
                    "valid": False, "errorCount": 1, "warningCount": 0,
                    "issues": [{"severity": "error", "code": "missing_batch_result", "target": "schema",
                                "message": "Batch-resultat manglar"}],
                }
            save_result(schema, policy, result)
            results.append({
                "schema": str(schema),
                "valid": result.get("valid", False),
                "error_count": result.get("errorCount", 0),
                "warning_count": result.get("warningCount", 0),
            })

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

    if args.schema:
        schema_path = Path(args.schema)
        if not schema_path.exists():
            print(f"FEIL: {schema_path} finst ikkje", file=sys.stderr)
            sys.exit(1)
        process_schema(schema_path, args.dry_run)
        return

    config_path = Path(args.config)
    try:
        config = json.loads(config_path.read_text())
    except Exception as e:
        print(f"FEIL: kunne ikkje lese {config_path}: {e}", file=sys.stderr)
        sys.exit(1)

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

    process_schemas_batch(schemas, args.dry_run)


if __name__ == "__main__":
    main()
