#!/usr/bin/env python3
"""Standardisert error-handtering for Python-script i repoet.

Dette er den obligatoriske konvensjonen for uventa unntak i script under
src/assets/scripts/ og mkdocs/lib/scripts/ — ikkje ei valfri hjelpefunksjon.
Ein bar `except:`/`except Exception:` utan anten log_error() herifrå eller
eksplisitt print(..., file=sys.stderr) er ikkje tillate. Sjå
specs/done/ingen-stille-feil.md for grunngjeving.
"""

import sys
import traceback
from pathlib import Path
from typing import Dict, Optional


def log_error(context: Optional[Dict[str, str]] = None, exit_code: int = 1) -> None:
    """
    Logg feil med strukturert kontekst og stack trace.

    Args:
        context: Dict med kontekstuell info (t.d. schema, domain, step)
        exit_code: Exit-kode (default 1)

    Eksempel:
        try:
            # ... arbeid ...
        except Exception:
            log_error({
                "schema": schema_path,
                "domain": domain,
                "step": "generate_validation_md",
            })
    """
    # Finn kallande script-fil (hopp over denne error_handler.py-fila)
    stack = traceback.extract_stack()
    caller_frame = stack[-2] if len(stack) >= 2 else stack[0]
    caller_file = Path(caller_frame.filename)

    # Prøv å finne relativ sti frå repo-rot
    try:
        repo_root = Path.cwd()
        relative_path = caller_file.relative_to(repo_root)
    except ValueError:
        relative_path = caller_file

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"ERROR in {relative_path}:{caller_frame.lineno}", file=sys.stderr)

    if context:
        print(f"Context:", file=sys.stderr)
        for key, value in context.items():
            print(f"  {key}: {value}", file=sys.stderr)

    print(f"{'='*60}\n", file=sys.stderr)

    # Print full stack trace
    traceback.print_exc()

    sys.exit(exit_code)


def format_error_message(script: str, line: int, context: Optional[Dict[str, str]] = None) -> str:
    """
    Formater feilmelding for GitHub Actions annotation.

    Args:
        script: Script-fil som feila (relativ sti)
        line: Linjenummer
        context: Kontekstuell info

    Returns:
        Formatert feilmelding for GitHub Actions ::error::
    """
    msg = f"Error in {script}:{line}"

    if context:
        ctx_str = ", ".join(f"{k}={v}" for k, v in context.items())
        msg += f" ({ctx_str})"

    return msg
