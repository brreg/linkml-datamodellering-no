

# Slot: modell 


_Informasjonsmodellar i modelkatalogen (modelldcatno:model)._





URI: [modelldcatno:model](https://data.norge.no/vocabulary/modelldcatno#model)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modelkatalog](modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Informasjonsmodell](informasjonsmodell.md) |
| Domain Of | [Modelkatalog](modelkatalog.md) |
| Slot URI | [modelldcatno:model](https://data.norge.no/vocabulary/modelldcatno#model) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:model |
| native | https://data.norge.no/linkml/modelldcat-ap-no/modell |




## LinkML Source

<details>
```yaml
name: modell
description: Informasjonsmodellar i modelkatalogen (modelldcatno:model).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
slot_uri: modelldcatno:model
domain_of:
- Modelkatalog
range: Informasjonsmodell
multivalued: true

```
</details>