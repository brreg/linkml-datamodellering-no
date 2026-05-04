

# Slot: prosent 


_Fråværsprosent (heiltal)._





URI: [utd:prosent](https://schema.fintlabs.no/utdanning/prosent)
Alias: prosent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravarsprosent](Fravarsprosent.md) | Kompleks type som representerer fråværsprosent for ein periode |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Fravarsprosent](Fravarsprosent.md) |
| Slot URI | [utd:prosent](https://schema.fintlabs.no/utdanning/prosent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fravarsprosent](Fravarsprosent.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:prosent |
| native | https://schema.fintlabs.no/utdanning/:prosent |




## LinkML Source

<details>
```yaml
name: prosent
description: Fråværsprosent (heiltal).
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:prosent
alias: prosent
owner: Fravarsprosent
domain_of:
- Fravarsprosent
range: integer
required: true

```
</details>