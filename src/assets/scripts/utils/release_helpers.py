#!/usr/bin/env python3
"""Delte hjelpefunksjonar for release-please-relaterte script."""

import json
import subprocess
import sys
from pathlib import Path


def find_released_packages(config: dict) -> list[str]:
    """Finn pakkar som endra versjon mellom HEAD~1 og HEAD ved å samanlikne manifest."""
    try:
        old_json = subprocess.check_output(
            ["git", "show", "HEAD~1:.release-please-manifest.json"],
            stderr=subprocess.DEVNULL,
        ).decode()
        old = json.loads(old_json)
    except Exception as e:
        print(f"INFO: fann ikkje HEAD~1:.release-please-manifest.json ({e}) — behandlar alle pakkar som nye", file=sys.stderr)
        old = {}

    try:
        new = json.loads(Path(".release-please-manifest.json").read_text())
    except Exception as e:
        print(f"FEIL: kunne ikkje lese .release-please-manifest.json: {e}", file=sys.stderr)
        return []

    return [p for p in new if old.get(p) != new[p] and p in config.get("packages", {})]
