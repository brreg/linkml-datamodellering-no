#!/usr/bin/env python3
"""
Genererer ein ## Valideringsresultat-seksjon frå validation JSON til stdout.

Bruk: python3 generate-validation-md.py <validation-json-path> <domain> <schema>
"""

import json
import sys
from pathlib import Path

# Legg til repo-root i sys.path for å importere error_handler
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src" / "assets" / "scripts"))
from utils.error_handler import log_error


def main() -> None:
    if len(sys.argv) < 4:
        print("Bruk: generate-validation-md.py <validation-json> <domain> <schema>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    domain = sys.argv[2]
    schema = sys.argv[3]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        log_error({
            "validation_json": str(path),
            "domain": domain,
            "schema": schema,
            "step": "read_validation_json",
        })

    version = data.get("version", "")
    validated_at = data.get("validated_at", "")

    # Støtt både validation_policy (ny) og data_policy (gamal) for bakoverkompatibilitet
    policy = data.get("validation_policy") or data.get("data_policy", "bronze")

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
    # Bruk relativ path frå <domain>/<schema>/index.md til valideringsregler.md
    # (to nivå opp: ../../valideringsregler/)
    anchor = policy
    policy_link = f"[policy: {policy}](../../valideringsregler/#{anchor})"

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
            lines.append(f"   {message}")
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
            lines.append(f"   {message}")
            lines.append("")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
