#!/usr/bin/env python3
"""
Genererer ein ## Valideringsresultat-seksjon frå latest.json til stdout.

Bruk: python3 generate-validation-md.py <validation/domain/model/latest.json>
"""

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) < 2:
        print("Bruk: generate-validation-md.py <latest.json>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FEIL: kunne ikkje lese {path}: {e}", file=sys.stderr)
        sys.exit(1)

    version = data.get("version", "")
    validated_at = data.get("validated_at", "")
    policy = data.get("data_policy", "bronze")
    result = data.get("result", {})
    valid = result.get("valid", False)
    error_count = result.get("error_count", 0)
    warning_count = result.get("warning_count", 0)
    issues = result.get("issues", [])
    errors = [i for i in issues if i.get("severity") == "error"]

    status = "✅ Godkjent" if valid else "❌ Ikkje godkjent"

    lines = [
        "",
        "## Valideringsresultat",
        "",
        f"*Siste validering: {validated_at} — v{version} — policy: {policy}*",
        "",
        "| Status | Feil | Åtvaringar |",
        "|---|---|---|",
        f"| {status} | {error_count} | {warning_count} |",
    ]

    if errors:
        lines += [
            "",
            "<details>",
            f"<summary>Feil ({error_count})</summary>",
            "",
            "```",
        ]
        for issue in errors:
            code = issue.get("code", "")
            target = issue.get("target", "")
            message = issue.get("message", "")
            lines.append(f"{code}: {target} — {message}")
        lines += [
            "```",
            "",
            "</details>",
        ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
