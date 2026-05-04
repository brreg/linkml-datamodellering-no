

# Slot: verdi 


_Verdien av gebyret._





URI: [cv:value](http://data.europa.eu/m8g/value)
Alias: verdi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gebyr](Gebyr.md) | Eit gebyr knytt til ei teneste |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Gebyr](Gebyr.md) |
| Slot URI | [cv:value](http://data.europa.eu/m8g/value) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:value |
| native | https://data.norge.no/linkml/cpsv-ap-no/verdi |




## LinkML Source

<details>
```yaml
name: verdi
description: Verdien av gebyret.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:value
alias: verdi
domain_of:
- Gebyr
range: float

```
</details>