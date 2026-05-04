

# Slot: inneholder_modellelement 


_Modellelement som er del av informasjonsmodellen (modelldcatno:containsModelElement)._





URI: [modelldcatno:containsModelElement](https://data.norge.no/vocabulary/modelldcatno#containsModelElement)
Alias: inneholder_modellelement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Informasjonsmodell](Informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modellelement](Modellelement.md) |
| Domain Of | [Informasjonsmodell](Informasjonsmodell.md) |
| Slot URI | [modelldcatno:containsModelElement](https://data.norge.no/vocabulary/modelldcatno#containsModelElement) |

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
| self | modelldcatno:containsModelElement |
| native | https://data.norge.no/linkml/modelldcat-ap-no/inneholder_modellelement |




## LinkML Source

<details>
```yaml
name: inneholder_modellelement
description: Modellelement som er del av informasjonsmodellen (modelldcatno:containsModelElement).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:containsModelElement
alias: inneholder_modellelement
domain_of:
- Informasjonsmodell
range: Modellelement
multivalued: true

```
</details>