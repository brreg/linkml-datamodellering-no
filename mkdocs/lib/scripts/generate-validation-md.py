#!/usr/bin/env python3
"""
Genererer ein ## Valideringsresultat-seksjon frå validation JSON til stdout.

Bruk: python3 generate-validation-md.py <validation-json-path> <domain> <schema>
"""

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FEIL: pyyaml er ikkje installert. Køyr: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def get_validation_policy_from_manifest(domain: str, schema: str) -> str:
    """Les validation_policy frå build.yaml (autoritativ kjelde)."""
    repo_root = Path(__file__).resolve().parents[3]
    manifest = repo_root / "src" / "linkml" / domain / schema / "build.yaml"

    if not manifest.exists():
        return "bronze"  # Fallback dersom build.yaml ikkje finst

    try:
        with manifest.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data.get("validation_policy", "bronze")
    except Exception as e:
        print(f"ÅTVARING: klarte ikkje lese validation_policy frå {manifest} ({e}) — brukar bronze", file=sys.stderr)
        return "bronze"


def main() -> None:
    if len(sys.argv) < 4:
        print("Bruk: generate-validation-md.py <validation-json> <domain> <schema>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    domain = sys.argv[2]
    schema = sys.argv[3]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        # Dersom JSON-fila er ugyldig, skriv ein fallback-seksjon
        print("\n## Valideringsresultat\n")
        print("> Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte.\n")
        print(f"*Valideringsfila er ugyldig eller manglar nødvendige felt: {path}*\n")
        print(f"*Feil: {e}*")
        sys.exit(0)  # Exit utan feil for å ikkje stoppe publish-prosessen

    version = data.get("version", "")
    validated_at = data.get("validated_at", "")

    # Les validation_policy frå build.yaml (autoritativ kjelde)
    # i staden for frå validation JSON (kan mangle eller vere feil)
    policy = get_validation_policy_from_manifest(domain, schema)

    result = data.get("result", {})
    valid = result.get("valid", False)

    # Støtt både errorCount (ny camelCase) og error_count (gamal snake_case)
    error_count = result.get("errorCount") or result.get("error_count", 0)
    warning_count = result.get("warningCount") or result.get("warning_count", 0)

    issues = result.get("issues", [])
    errors = [i for i in issues if i.get("severity") == "error"]
    warnings = [i for i in issues if i.get("severity") == "warning"]

    status = "✅ Godkjent" if valid else "❌ Ikkje godkjent"

    # Generer lenke til valideringspolicy
    # MkDocs genererer anker frå fullstendig overskriftstekst
    # bronze/silver/gold/felles-*: ### <policy> → #<policy>
    # Anchor-namnet er identisk med policy-namnet
    # Bruk relativ path frå <domain>/<schema>/index.md til arkitektur/valideringsregler.md
    # (to nivå opp, so inn i arkitektur/: ../../arkitektur/valideringsregler.md)
    anchor = policy
    policy_link = f"[policy: {policy}](../../arkitektur/valideringsregler.md#{anchor})"

    lines = [
        "",
        "## Valideringsresultat",
        "",
        "> Valideringsrapporten viser i kva grad modellen etterlever definerte modelleringsreglar og kvalitetskrav. Resultata kan omfatte både lokale og importerte element avhengig av kva reglar som er evaluerte.",
        "",
        f"*Siste validering: {validated_at} — v{version} — {policy_link}*",
        "",
        "| Status | Feil | Åtvaringar |",
        "|---|---|---|",
        f"| {status} | {error_count} | {warning_count} |",
    ]

    if errors:
        lines += [
            "",
            f"### Feil ({error_count})",
            "",
        ]
        for idx, issue in enumerate(errors, start=1):
            code = issue.get("code", "")
            target = issue.get("target", "")
            message = issue.get("message", "")
            lines.append(f"{idx}. **`{code}`** — `{target}`")
            lines.append(f"   `{message}`")
            lines.append("")

    if warnings:
        lines += [
            "",
            f"### Åtvaringar ({warning_count})",
            "",
        ]
        for idx, issue in enumerate(warnings, start=1):
            code = issue.get("code", "")
            target = issue.get("target", "")
            message = issue.get("message", "")
            lines.append(f"{idx}. **`{code}`** — `{target}`")
            lines.append(f"   `{message}`")
            lines.append("")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
