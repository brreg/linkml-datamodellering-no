#!/usr/bin/env python3
"""Delte hjelpefunksjonar for å utleie metadata frå ein skjema-sti."""

import re
import sys
from pathlib import Path

from .yaml_io import load_yaml


def get_domain_model(schema_path: Path) -> tuple[str, str]:
    """Utlei domain og modellnavn frå skjemastien."""
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


def detect_policy(schema_path: Path) -> str:
    """Les validation_policy frå build.yaml i same katalog som skjemaet.

    Returnerer 'bronze' som default dersom build.yaml ikkje finst eller
    manglar feltet.
    """
    manifest_path = schema_path.parent / "build.yaml"
    if not manifest_path.exists():
        return "bronze"
    try:
        manifest = load_yaml(manifest_path)
        return manifest.get("validation_policy", "bronze")
    except Exception as e:
        print(
            f"ÅTVARING: klarte ikkje lese validation_policy frå {manifest_path} ({e}) — brukar bronze",
            file=sys.stderr,
        )
        return "bronze"
