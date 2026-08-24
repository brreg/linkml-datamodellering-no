import sys, yaml
sys.path.insert(0, "/app/utils")
import linkml_relative_import_patch
linkml_relative_import_patch.apply()
from linkml_runtime.utils.schemaview import SchemaView
from linkml.validator import validate

schema_path = sys.argv[1]
data_path = sys.argv[2]
sv = SchemaView(schema_path)
container = next((n for n, c in sv.all_classes().items() if c.tree_root), None)
data = yaml.safe_load(open(data_path))
report = validate(data, schema_path, target_class=container)
errors = [str(r.message) for r in report.results if str(r.severity).endswith("ERROR")]
warnings = [str(r.message) for r in report.results if str(r.severity).endswith("WARNING")]
print(f"container={container} errors={len(errors)} warnings={len(warnings)}")
for e in errors:
    print("ERROR:", e)
for w in warnings[:10]:
    print("WARN:", w)
