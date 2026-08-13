#!/usr/bin/env python3
"""Delte hjelpefunksjonar for å lese CODEOWNERS.md og finne eigar-organisasjon via path-matching."""

import fnmatch
import re
from pathlib import Path
from typing import Dict, List, Optional

import yaml


def load_codeowners(repo_root: Path) -> List[Dict]:
    """
    Les YAML-frontmatter frå CODEOWNERS.md og returner liste av organisasjonar.
    """
    codeowners_path = repo_root / "CODEOWNERS.md"
    if not codeowners_path.exists():
        return []

    with open(codeowners_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Ekstraher YAML-frontmatter (mellom ```yaml og ```)
    yaml_match = re.search(r"```yaml\n(.*?)\n```", content, re.DOTALL)
    if not yaml_match:
        return []

    yaml_content = yaml_match.group(1)
    data = yaml.safe_load(yaml_content)
    return data.get("organizations", [])


def find_owner_org(path: Path, orgs: List[Dict]) -> Optional[Dict]:
    """
    Finn eigar-organisasjon basert på path-matching mot CODEOWNERS.md sine path_patterns.

    Args:
        path: Relativ sti til ressursen (t.d. src/linkml/oreg/begrepssamling-foretaksregisteret)
        orgs: Liste av organisasjonar frå CODEOWNERS.md

    Returns:
        Matchande organisasjon-dict eller None
    """
    path_str = str(path)

    for org in orgs:
        for pattern in org.get("path_patterns", []):
            # Konverter glob-pattern til fnmatch og match
            if fnmatch.fnmatch(path_str, pattern):
                return org

    return None
