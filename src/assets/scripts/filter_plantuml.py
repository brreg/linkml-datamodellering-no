# filter_plantuml.py
import re, sys, yaml
from pathlib import Path

schema_path = Path(sys.argv[1])
puml_path = Path(sys.argv[2])
mode = sys.argv[3] if len(sys.argv) > 3 else "filtered"  # "filtered" eller "full"

schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
classes_dict = schema.get("classes") or {}

# Hent tree_root-klasser (containerklasser) — skal alltid filtrerast vekk
tree_root_classes = set()
for cls_name, cls_def in classes_dict.items():
    if (cls_def or {}).get("tree_root", False):
        tree_root_classes.add(cls_name)

# Hent lokale klasser (ekskl. tree_root)
local_classes = set()
for cls_name, cls_def in classes_dict.items():
    if not (cls_def or {}).get("tree_root", False):
        local_classes.add(cls_name)

# Bestem kva klasser som skal inkluderast basert på mode
if mode == "filtered":
    # Berre lokale klasser (ingen importerte)
    allowed_classes = local_classes
else:  # mode == "full"
    # Alle klasser minus tree_root (inkluderer importerte)
    allowed_classes = None  # None betyr "alle utanom tree_root"

text = puml_path.read_text(encoding="utf-8").splitlines()

out = []
in_class_block = False
current_class = None
class_buf = []

# Regex for klassedefinisjoner: class "Klassenamn" eller abstract "Klassenamn"
class_def_re = re.compile(r'^\s*(abstract\s+|class\s+)"([^"]+)"')

# Regex for relasjonar: "A" --> "B" eller "A" --> "0..1" "B" eller "A" ^-- "B" (arv)
# Fangar også kardinalitet som "0..1", "1..*" osv.
rel_re = re.compile(r'^\s*"([^"]+)"\s+([\-*o<>.|^]+)\s+(?:"[^"]*"\s+)?"([^"]+)"')

def should_include_class(cls_name):
    """Sjekk om ein klasse skal inkluderast basert på mode."""
    if cls_name in tree_root_classes:
        return False  # tree_root-klasser skal alltid filtrerast vekk
    if allowed_classes is None:
        return True  # "full" mode — alle utanom tree_root
    return cls_name in allowed_classes  # "filtered" mode — berre lokale

def flush_class():
    global class_buf, current_class
    if current_class and should_include_class(current_class):
        out.extend(class_buf)
    class_buf = []
    current_class = None

for line in text:
    # Bevare header-linjer
    if line.strip() in ["@startuml", "@enduml"] or line.startswith("skinparam") or line.startswith("hide"):
        out.append(line)
        continue

    # Klassedefinisjonsstart: class "Klassenamn" { eller abstract "Klassenamn" {
    m = class_def_re.match(line)
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

    # Relasjonslinje: "A" --> "B" : "label"
    m = rel_re.match(line)
    if m:
        a = m.group(1)
        b = m.group(3)
        # I "filtered" mode: berre relasjonar mellom lokale klasser
        # I "full" mode: alle relasjonar utanom dei som involverer tree_root
        if mode == "filtered":
            if a in local_classes and b in local_classes:
                out.append(line)
        else:  # mode == "full"
            if a not in tree_root_classes and b not in tree_root_classes:
                out.append(line)
        continue

    # Tomme linjer
    if line.strip() == "":
        out.append(line)

print("\n".join(out))
