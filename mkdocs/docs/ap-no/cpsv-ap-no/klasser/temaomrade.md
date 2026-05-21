

# Slot: temaomrade 


_Tematisk område for tenesta._





URI: [cv:thematicArea](http://data.europa.eu/m8g/thematicArea)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [cv:thematicArea](http://data.europa.eu/m8g/thematicArea) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:thematicArea |
| native | https://data.norge.no/linkml/cpsv-ap-no/temaomrade |




## LinkML Source

<details>
```yaml
name: temaomrade
description: Tematisk område for tenesta.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:thematicArea
domain_of:
- OffentligTjeneste
- Tjeneste
range: Konsept
multivalued: true

```
</details>