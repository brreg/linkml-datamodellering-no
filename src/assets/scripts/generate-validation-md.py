#!/usr/bin/env python3
"""
Genererer ein ## Valideringsresultat-seksjon frå validation JSON til stdout.

Bruk: python3 generate-validation-md.py <src/linkml/domain/model/validation/version/policy.json>
"""

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) < 2:
        print("Bruk: generate-validation-md.py <validation-json>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FEIL: kunne ikkje lese {path}: {e}", file=sys.stderr)
        sys.exit(1)

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
    # Bronze/silver/gold: anchor er "{policy}-sjekkliste"
    # felles-begrepskatalog: anchor er "felles-begrepskatalog-felles-begrepskatalog"
    # felles-datakatalog: anchor er "felles-datakatalog-felles-datakatalog"
    if policy in ("bronze", "silver", "gold"):
        anchor = f"{policy}-sjekkliste"
    elif policy == "felles-begrepskatalog":
        anchor = "felles-begrepskatalog-felles-begrepskatalog"
    elif policy == "felles-datakatalog":
        anchor = "felles-datakatalog-felles-datakatalog"
    else:
        # Fallback — bruk policy som anchor
        anchor = policy
    policy_link = f"[policy: {policy}](/valideringsregler/#{anchor})"

    lines = [
        "",
        "## Valideringsresultat",
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
