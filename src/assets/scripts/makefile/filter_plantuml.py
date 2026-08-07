# filter_plantuml.py
"""Filtrer eit PlantUML-diagram til "filtered" (berre lokale klasser) eller
"full" (alle klasser utanom tree_root) modus.

Bruk (CLI): python3 filter_plantuml.py <schema.yaml> <raw.puml> [filtered|full]
Bruk (import): process_file(schema_path, puml_path, mode) -> str
"""

import re
import sys
from pathlib import Path

import yaml

CLASS_DEF_RE = re.compile(r'^\s*(abstract\s+|class\s+)"([^"]+)"')
# Fangar relasjonar: "A" --> "B" eller "A" --> "0..1" "B" eller "A" ^-- "B" (arv),
# inkl. kardinalitet som "0..1", "1..*" osv.
REL_RE = re.compile(r'^\s*"([^"]+)"\s+([\-*o<>.|^]+)\s+(?:"[^"]*"\s+)?"([^"]+)"')


def process_file(schema_path: Path, puml_path: Path, mode: str = "filtered") -> str:
    """Filtrer puml_path sitt innhald basert på schema_path sine klasser.

    mode="filtered": berre lokale klasser (ingen importerte).
    mode="full": alle klasser minus tree_root (inkluderer importerte).
    """
    schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
    classes_dict = schema.get("classes") or {}

    tree_root_classes = {
        cls_name for cls_name, cls_def in classes_dict.items() if (cls_def or {}).get("tree_root", False)
    }
    local_classes = {
        cls_name for cls_name, cls_def in classes_dict.items() if not (cls_def or {}).get("tree_root", False)
    }
    allowed_classes = local_classes if mode == "filtered" else None  # None => alle utanom tree_root

    def should_include_class(cls_name: str) -> bool:
        if cls_name in tree_root_classes:
            return False
        if allowed_classes is None:
            return True
        return cls_name in allowed_classes

    text = puml_path.read_text(encoding="utf-8").splitlines()

    out: list[str] = []
    in_class_block = False
    current_class = None
    class_buf: list[str] = []

    def flush_class():
        nonlocal class_buf, current_class
        if current_class and should_include_class(current_class):
            out.extend(class_buf)
        class_buf = []
        current_class = None

    for line in text:
        if line.strip() in ["@startuml", "@enduml"] or line.startswith("skinparam") or line.startswith("hide"):
            out.append(line)
            continue

        m = CLASS_DEF_RE.match(line)
        if m:
            flush_class()
            in_class_block = True
            current_class = m.group(2)
            class_buf = [line]
            continue

        if in_class_block:
            class_buf.append(line)
            if line.strip() == "}":
                in_class_block = False
                flush_class()
            continue

        m = REL_RE.match(line)
        if m:
            a, b = m.group(1), m.group(3)
            if mode == "filtered":
                if a in local_classes and b in local_classes:
                    out.append(line)
            else:
                if a not in tree_root_classes and b not in tree_root_classes:
                    out.append(line)
            continue

        if line.strip() == "":
            out.append(line)

    return "\n".join(out)


def main():
    schema_path = Path(sys.argv[1])
    puml_path = Path(sys.argv[2])
    mode = sys.argv[3] if len(sys.argv) > 3 else "filtered"
    print(process_file(schema_path, puml_path, mode))


if __name__ == "__main__":
    main()
