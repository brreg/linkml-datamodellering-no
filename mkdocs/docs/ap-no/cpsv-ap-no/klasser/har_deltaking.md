

# Slot: har_deltaking 


_Deltakarar med spesifikke roller i levering av tenesta._





URI: [cv:hasParticipation](http://data.europa.eu/m8g/hasParticipation)
Alias: har_deltaking

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Deltagelse](deltagelse.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [cv:hasParticipation](http://data.europa.eu/m8g/hasParticipation) |

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
| self | cv:hasParticipation |
| native | https://data.norge.no/linkml/cpsv-ap-no/har_deltaking |




## LinkML Source

<details>
```yaml
name: har_deltaking
description: Deltakarar med spesifikke roller i levering av tenesta.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:hasParticipation
alias: har_deltaking
domain_of:
- OffentligTjeneste
- Tjeneste
range: Deltagelse
multivalued: true

```
</details>