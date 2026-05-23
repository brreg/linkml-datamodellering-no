#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import yaml

REPO = Path(".")
ARTIFACT_FIELD = {
    "linkml":       None,            # alltid aktiv (lint/validering)
    "context":      "jsonld_context",
    "shapes":       "shacl",
    "python":       "python",
    "json-schema":  "json_schema",
    "owl":          "owl",
    "rdf":          "rdf",
    "erdiagram":    "erdiagram",
    "doc":          "docs",
    "proto":        "protobuf",
    "plantuml":     "plantuml",
    "examples":     "example_rdf",
}

def local_imports(schema_path: Path) -> list[Path]:
    schema_dir = schema_path.parent
    try:
        data = yaml.safe_load(schema_path.read_text())
    except Exception:
        return []
    result = []
    for imp in (data or {}).get("imports", []):
        if imp.startswith("linkml:"):
            continue
        candidate = (schema_dir / (imp + ".yaml")).resolve()
        if candidate.exists():
            result.append(candidate)
    return result

def all_deps(schema_path: Path, visited: set | None = None) -> set[Path]:
    if visited is None:
        visited = set()
    p = schema_path.resolve()
    if p in visited:
        return set()
    visited.add(p)
    deps = {p}
    for imp in local_imports(p):
        deps |= all_deps(imp, visited)
    return deps

def deps_hash(schema_path: Path) -> str:
    h = hashlib.sha256()
    for dep in sorted(all_deps(schema_path)):
        h.update(dep.read_bytes())
    return h.hexdigest()[:16]

entries = []
for yaml_file in sorted(REPO.glob("src/linkml/*/*/generate.yaml")):
    if "/common/" in str(yaml_file):
        continue
    domain = yaml_file.parts[2]
    model  = yaml_file.parts[3]
    schema = REPO / f"src/linkml/{domain}/{model}/{model}-schema.yaml"
    if not schema.exists():
        continue

    cfg = yaml.safe_load(yaml_file.read_text()).get("generators", {})
    dhash = deps_hash(schema)

    for artifact, field in ARTIFACT_FIELD.items():
        if field is not None:
            val = cfg.get(field, True)
            if val is False:
                continue
        if artifact == "examples":
            example_file = REPO / f"examples/{domain}/{model}-eksempel.yaml"
            if not example_file.exists():
                continue
        entries.append({
            "domain":    domain,
            "model":     model,
            "schema":    str(schema),
            "artifact":  artifact,
            "deps_hash": dhash,
        })

print(json.dumps({"include": entries}))
