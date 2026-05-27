

# Slot: inneholder_modellelement 


_Modellelement som er del av informasjonsmodellen (modelldcatno:containsModelElement)._





URI: [modelldcatno:containsModelElement](https://data.norge.no/vocabulary/modelldcatno#containsModelElement)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modellkatalog (modelldcatno:... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Modellelement](modellelement.md) |
| Domain Of | [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [modelldcatno:containsModelElement](https://data.norge.no/vocabulary/modelldcatno#containsModelElement) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | modelldcatno:containsModelElement |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/inneholder_modellelement |




## LinkML Source

<details>
```yaml
name: inneholder_modellelement
description: Modellelement som er del av informasjonsmodellen (modelldcatno:containsModelElement).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: modelldcatno:containsModelElement
domain_of:
- Informasjonsmodell
range: Modellelement
multivalued: true

```
</details>