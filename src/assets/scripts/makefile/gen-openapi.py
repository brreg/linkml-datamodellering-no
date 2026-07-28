#!/usr/bin/env python3
"""Generate an OpenAPI 3.1 spec from a LinkML-generated JSON Schema and YAML schema metadata.

Usage:
  gen-openapi.py <schema.json> <schema.yaml> [--out <output.yaml>]

All classes from $defs in the JSON Schema are placed under components/schemas.
$ref paths are rewritten: #/$defs/X  →  #/components/schemas/X
Metadata (title, version, description, id) is read from the YAML schema file.
paths: {} — schema library only, no endpoint stubs.
"""

import argparse
import json
import sys

import yaml


def rewrite_refs(obj):
    if isinstance(obj, dict):
        return {
            k: v.replace("#/$defs/", "#/components/schemas/") if k == "$ref" else rewrite_refs(v)
            for k, v in obj.items()
        }
    if isinstance(obj, list):
        return [rewrite_refs(item) for item in obj]
    return obj


def load_yaml_meta(yaml_path):
    with open(yaml_path) as f:
        schema = yaml.safe_load(f)
    return {
        "title":       schema.get("title") or schema.get("name", ""),
        "version":     str(schema.get("version") or "0.0.0"),
        "description": schema.get("description") or "",
        "id":          schema.get("id") or "",
    }


def build_openapi(json_path, yaml_path):
    with open(json_path) as f:
        json_schema = json.load(f)

    meta = load_yaml_meta(yaml_path)
    schemas = rewrite_refs(json_schema.get("$defs", {}))

    info = {"title": meta["title"], "version": meta["version"]}
    if meta["description"]:
        info["description"] = meta["description"]
    if meta["id"]:
        info["contact"] = {"url": meta["id"]}

    return {
        "openapi": "3.1.0",
        "info": info,
        "paths": {},
        "components": {"schemas": schemas},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_schema", help="Path to generated JSON Schema (.json)")
    parser.add_argument("yaml_schema", help="Path to LinkML YAML schema (.yaml)")
    parser.add_argument("--out", help="Output file path (default: stdout)")
    args = parser.parse_args()

    doc = build_openapi(args.json_schema, args.yaml_schema)
    output = yaml.dump(doc, allow_unicode=True, default_flow_style=False, sort_keys=False)

    if args.out:
        with open(args.out, "w") as f:
            f.write(output)
        print(f"gen-openapi: skriven til {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
