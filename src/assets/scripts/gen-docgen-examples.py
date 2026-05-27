"""
Split a container-structured example YAML into per-class files for gen-doc --example-directory.

Usage:
    python3 gen-docgen-examples.py <schema.yaml> <eksempel.yaml> <output-dir>

Reads the tree_root class attributes from schema.yaml to find {attribute_name: ClassName}
mappings, then splits the example file into <ClassName>-<slug>.yaml per instance.

Exits 0 silently if:
  - docgen_examples: false is set in manifest.yaml (sibling of schema.yaml)
  - example file does not exist
  - schema has no tree_root class with attributes
"""
import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not available", file=sys.stderr)
    sys.exit(1)


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def slug_from_obj(obj, index):
    """Derive a short slug from the object's id field, or use zero-padded index."""
    id_val = obj.get("id") or obj.get("identifier") or obj.get("identifikator")
    if id_val and isinstance(id_val, str):
        # URL: take last path segment; CURIE (prefix:local): take local part
        if "/" in id_val:
            segment = id_val.rstrip("/").rsplit("/", 1)[-1]
        elif ":" in id_val:
            segment = id_val.rsplit(":", 1)[-1]
        else:
            segment = id_val
        segment = re.sub(r"[^A-Za-z0-9_-]", "-", segment)
        if segment and len(segment) <= 60:
            return segment
    return f"{index:03d}"


def find_attr_class_map(schema):
    """Return {attr_name: ClassName} from the tree_root class attributes."""
    classes = schema.get("classes") or {}
    for cls_name, cls in classes.items():
        if not isinstance(cls, dict):
            continue
        if not cls.get("tree_root"):
            continue
        attrs = cls.get("attributes") or {}
        result = {}
        for attr_name, attr in attrs.items():
            if isinstance(attr, dict) and attr.get("range"):
                result[attr_name] = attr["range"]
        return result
    return {}


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <schema.yaml> <eksempel.yaml> <output-dir>", file=sys.stderr)
        sys.exit(1)

    schema_path = Path(sys.argv[1])
    example_path = Path(sys.argv[2])
    out_dir = Path(sys.argv[3])

    # Check opt-out in manifest.yaml (sibling of schema file)
    generate_yaml = schema_path.parent / "manifest.yaml"
    if generate_yaml.exists():
        with open(generate_yaml, encoding="utf-8") as f:
            for line in f:
                if re.match(r"^docgen_examples\s*:\s*false\s*$", line.strip()):
                    sys.exit(0)

    if not example_path.exists():
        sys.exit(0)

    if not schema_path.exists():
        print(f"Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)

    schema = load_yaml(schema_path)
    attr_class_map = find_attr_class_map(schema)
    if not attr_class_map:
        sys.exit(0)

    example = load_yaml(example_path)
    if not isinstance(example, dict):
        sys.exit(0)

    out_dir.mkdir(parents=True, exist_ok=True)

    for attr_name, class_name in attr_class_map.items():
        instances = example.get(attr_name)
        if not instances or not isinstance(instances, list):
            continue

        # Track used slugs to avoid collisions
        used = {}
        for i, obj in enumerate(instances, start=1):
            base_slug = slug_from_obj(obj, i)
            if base_slug in used:
                # Append suffix to make unique
                suffix_chars = "bcdefghijklmnopqrstuvwxyz"
                for ch in suffix_chars:
                    candidate = f"{base_slug}-{ch}"
                    if candidate not in used:
                        base_slug = candidate
                        break
                else:
                    base_slug = f"{base_slug}-{i}"
            used[base_slug] = True

            filename = out_dir / f"{class_name}-{base_slug}.yaml"
            with open(filename, "w", encoding="utf-8") as f:
                yaml.dump(obj, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    main()
