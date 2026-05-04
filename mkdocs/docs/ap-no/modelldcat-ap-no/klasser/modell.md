

# Slot: modell 


_Informasjonsmodellar i modelkatalogen (modelldcatno:model)._





URI: [modelldcatno:model](https://data.norge.no/vocabulary/modelldcatno#model)
Alias: modell

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modelkatalog](Modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Informasjonsmodell](Informasjonsmodell.md) |
| Domain Of | [Modelkatalog](Modelkatalog.md) |
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
rank: 1000
slot_uri: modelldcatno:model
alias: modell
domain_of:
- Modelkatalog
range: Informasjonsmodell
multivalued: true

```
</details>