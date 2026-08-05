#!/usr/bin/env python3
"""Generate an AsyncAPI 3.0 spec from a LinkML-generated JSON Schema and YAML schema metadata.

Usage:
  gen-asyncapi.py <schema.json> <schema.yaml> [--out <output.yaml>]

All classes from $defs in the JSON Schema are placed under components/schemas.
$ref paths are rewritten: #/$defs/X  →  #/components/schemas/X
Metadata (title, version, description, id) is read from the YAML schema file.
channels: {} and operations: {} — schema library only, no channel stubs.
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from api_spec_common import load_yaml_meta, rewrite_refs  # noqa: E402


def build_asyncapi(json_path, yaml_path):
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
        "asyncapi": "3.0.0",
        "info": info,
        "channels": {},
        "operations": {},
        "components": {"schemas": schemas},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_schema", help="Path to generated JSON Schema (.json)")
    parser.add_argument("yaml_schema", help="Path to LinkML YAML schema (.yaml)")
    parser.add_argument("--out", help="Output file path (default: stdout)")
    args = parser.parse_args()

    doc = build_asyncapi(args.json_schema, args.yaml_schema)
    output = yaml.dump(doc, allow_unicode=True, default_flow_style=False, sort_keys=False)

    if args.out:
        with open(args.out, "w") as f:
            f.write(output)
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
