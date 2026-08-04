#!/usr/bin/env python3
"""Delte hjelpefunksjonar for å utleie metadata frå ein skjema-sti."""

import re
from pathlib import Path


def get_domain_model(schema_path: Path) -> tuple[str, str]:
    """Utlei domain og modellnamn frå skjemastien."""
    model = schema_path.parent.name
    domain = schema_path.parent.parent.name
    if domain == "linkml":
        # src/linkml/referanse/referanse-schema.yaml → domain=referanse
        domain = model
    return domain, model


def get_version(schema_path: Path, fallback: str = "0.0.0") -> str:
    """Hent versjonsnummer frå version:-feltet i skjemaet."""
    if not schema_path.exists():
        return fallback
    content = schema_path.read_text(encoding="utf-8")
    m = re.search(r'^version:\s*"([^"]+)"', content, re.MULTILINE)
    return m.group(1) if m else fallback
