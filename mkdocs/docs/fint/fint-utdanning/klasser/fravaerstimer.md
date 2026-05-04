

# Slot: fravaerstimer 


_Antal fråværstimar._





URI: [utd:fravaerstimer](https://schema.fintlabs.no/utdanning/fravaerstimer)
Alias: fravaerstimer

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
| Slot URI | [utd:fravaerstimer](https://schema.fintlabs.no/utdanning/fravaerstimer) |

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
| self | utd:fravaerstimer |
| native | https://schema.fintlabs.no/utdanning/:fravaerstimer |




## LinkML Source

<details>
```yaml
name: fravaerstimer
description: Antal fråværstimar.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fravaerstimer
alias: fravaerstimer
owner: Fravarsprosent
domain_of:
- Fravarsprosent
range: integer
required: true

```
</details>