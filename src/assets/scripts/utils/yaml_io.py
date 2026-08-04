#!/usr/bin/env python3
"""Delte hjelpefunksjonar for å lese og skrive YAML-filer."""

from pathlib import Path
from typing import Dict

import yaml


def load_yaml(path) -> Dict:
    """Last YAML-fil. Returnerer {} (ikkje None) for tom fil."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def write_yaml(file_path: Path, data: Dict, generated_by: str, note: str = "") -> None:
    """
    Skriv YAML-fil med "generert av"-header.

    Args:
        file_path: Sti til fila som skal skrivast
        data: Data som skal serialiserast
        generated_by: Kallande script sitt filnamn (t.d. Path(__file__).name)
        note: Valfri ekstra forklaringslinje i header-kommentaren
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# Generert av CI frå {generated_by} — ikkje rediger manuelt\n")
        if note:
            f.write(f"# {note}\n")
        f.write("\n")
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
