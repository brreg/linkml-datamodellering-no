## Kom i gang

### Importer i LinkML-skjema

```yaml
imports:
  - https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/{{VERSION_PATH}}/src/linkml/samt/{{SCHEMA}}/{{SCHEMA}}-schema.yaml
```

### Valider datafil

Valider datafil mot LinkML-skjemaet:

```bash
make validate-instance SCHEMA=src/linkml/samt/{{SCHEMA}}/{{SCHEMA}}-schema.yaml INSTANCE=mine-data.yaml
```

Valider skjemaet mot {{POLICY}}-policy:

```bash
make mcp-validate SCHEMA=src/linkml/samt/{{SCHEMA}}/{{SCHEMA}}-schema.yaml
```

### Python-bruk

```bash
pip install linkml-runtime pyyaml
```

```python
from linkml_runtime.loaders import yaml_loader
from {{SCHEMA_UNDERSCORE}}_model import {{EXAMPLE_CLASS}}

{{EXAMPLE_VAR}} = yaml_loader.load('mine-data.yaml', target_class={{EXAMPLE_CLASS}})
```
