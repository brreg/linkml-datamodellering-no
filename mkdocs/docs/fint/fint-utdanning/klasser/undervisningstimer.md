

# Slot: undervisningstimer 


_Totalt antal undervisningstimar._





URI: [utd:undervisningstimer](https://schema.fintlabs.no/utdanning/undervisningstimer)
Alias: undervisningstimer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravarsprosent](fravarsprosent.md) | Kompleks type som representerer fråværsprosent for ein periode |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Fravarsprosent](fravarsprosent.md) |
| Slot URI | [utd:undervisningstimer](https://schema.fintlabs.no/utdanning/undervisningstimer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fravarsprosent](fravarsprosent.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:undervisningstimer |
| native | https://schema.fintlabs.no/utdanning/:undervisningstimer |




## LinkML Source

<details>
```yaml
name: undervisningstimer
description: Totalt antal undervisningstimar.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:undervisningstimer
alias: undervisningstimer
owner: Fravarsprosent
domain_of:
- Fravarsprosent
range: integer
required: true

```
</details>