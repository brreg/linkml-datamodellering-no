

# Slot: skjermingshjemmel 


_Skjermingsheimelen._





URI: [ark:skjermingshjemmel](https://schema.fintlabs.no/arkiv/skjermingshjemmel)
Alias: skjermingshjemmel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skjerming](Skjerming.md) | Skjerming av mappe, registrering eller dokument etter offentleglova |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skjermingshjemmel](Skjermingshjemmel.md) |
| Domain Of | [Skjerming](Skjerming.md) |
| Slot URI | [ark:skjermingshjemmel](https://schema.fintlabs.no/arkiv/skjermingshjemmel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Skjerming](Skjerming.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:skjermingshjemmel |
| native | https://schema.fintlabs.no/arkiv/:skjermingshjemmel |




## LinkML Source

<details>
```yaml
name: skjermingshjemmel
description: Skjermingsheimelen.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:skjermingshjemmel
alias: skjermingshjemmel
owner: Skjerming
domain_of:
- Skjerming
range: Skjermingshjemmel
required: true

```
</details>