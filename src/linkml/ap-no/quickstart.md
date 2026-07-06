## Kom i gang

### Importer i LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/src/linkml/ap-no/{{SCHEMA}}/{{SCHEMA}}-schema
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from {{SCHEMA_UNDERSCORE}}_model import Katalog

katalog = yaml_loader.load('eksempel.yaml', target_class=Katalog)
print(katalog.tittel)
```

### Valider data mot SHACL

```bash
pyshacl --shacl {{SCHEMA}}-shapes.ttl --data-format turtle mine-data.ttl
```
