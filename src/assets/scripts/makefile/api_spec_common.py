#!/usr/bin/env python3
"""Delte hjelpefunksjonar for gen-asyncapi.py og gen-openapi.py."""

import yaml


def rewrite_refs(obj):
    """Reskriv $ref-stiar frå JSON Schema-format ($defs) til komponent-schema-format."""
    if isinstance(obj, dict):
        return {
            k: v.replace("#/$defs/", "#/components/schemas/") if k == "$ref" else rewrite_refs(v)
            for k, v in obj.items()
        }
    if isinstance(obj, list):
        return [rewrite_refs(item) for item in obj]
    return obj


def load_yaml_meta(yaml_path):
    """Hent title/version/description/id frå eit LinkML YAML-skjema."""
    with open(yaml_path) as f:
        schema = yaml.safe_load(f)
    return {
        "title":       schema.get("title") or schema.get("name", ""),
        "version":     str(schema.get("version") or "0.0.0"),
        "description": schema.get("description") or "",
        "id":          schema.get("id") or "",
    }
