# filter_erdiagram.py
import re, sys, yaml
from pathlib import Path

schema_path = Path(sys.argv[1])
mmd_path = Path(sys.argv[2])

schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
local_classes = set((schema.get("classes") or {}).keys())

text = mmd_path.read_text(encoding="utf-8").splitlines()

out = []
in_entity_block = False
current_entity = None
entity_buf = []

rel_re = re.compile(r'^\s*([A-Za-z0-9_]+)\s+([|}o. -]+)\s+([A-Za-z0-9_]+)\s*:')

def flush_entity():
    global entity_buf, current_entity
    if current_entity and current_entity in local_classes:
        out.extend(entity_buf)
    entity_buf = []
    current_entity = None

for line in text:
    if line.strip() == "erDiagram":
        out.append(line)
        continue

    # Entity block start: NAME {
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

    # Relationship line: A }|--|| B : "label"
    m = rel_re.match(line)
    if m:
        a = m.group(1)
        b = m.group(3)
        if a in local_classes and b in local_classes:
            out.append(line)
        continue

    # ellers: ignorer tomme linjer etc
    if line.strip() == "":
        out.append(line)

print("```mermaid")
print("\n".join(out))
print("```")