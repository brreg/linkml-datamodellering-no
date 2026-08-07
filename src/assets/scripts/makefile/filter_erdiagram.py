# filter_erdiagram.py
"""Filtrer eit Mermaid ER-diagram til berre lokale klasser i schema_path.

Bruk (CLI): python3 filter_erdiagram.py <schema.yaml> <unfiltered.md>
Bruk (import): process_file(schema_path, mmd_path) -> str  (inkl. ```mermaid-fence)
"""

import re
import sys
from pathlib import Path

import yaml

REL_RE = re.compile(r'^\s*([A-Za-z0-9_]+)\s+([|}o. -]+)\s+([A-Za-z0-9_]+)\s*:')


def process_file(schema_path: Path, mmd_path: Path) -> str:
    schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
    local_classes = set((schema.get("classes") or {}).keys())

    text = mmd_path.read_text(encoding="utf-8").splitlines()

    out: list[str] = []
    in_entity_block = False
    current_entity = None
    entity_buf: list[str] = []

    def flush_entity():
        nonlocal entity_buf, current_entity
        if current_entity and current_entity in local_classes:
            out.extend(entity_buf)
        entity_buf = []
        current_entity = None

    for line in text:
        if line.strip() == "erDiagram":
            out.append(line)
            continue

        m = re.match(r'^\s*([A-Za-z0-9_]+)\s*\{\s*$', line)
        if m:
            flush_entity()
            in_entity_block = True
            current_entity = m.group(1)
            entity_buf = [line]
            continue

        if in_entity_block:
            entity_buf.append(line)
            if line.strip() == "}":
                in_entity_block = False
                flush_entity()
            continue

        m = REL_RE.match(line)
        if m:
            a, b = m.group(1), m.group(3)
            if a in local_classes and b in local_classes:
                out.append(line)
            continue

        if line.strip() == "":
            out.append(line)

    return "```mermaid\n" + "\n".join(out) + "\n```\n"


def main():
    schema_path = Path(sys.argv[1])
    mmd_path = Path(sys.argv[2])
    sys.stdout.write(process_file(schema_path, mmd_path))


if __name__ == "__main__":
    main()
