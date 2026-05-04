

# Slot: halvaar 


_Fråværsprosent for halvåret._





URI: [utd:halvaar](https://schema.fintlabs.no/utdanning/halvaar)
Alias: halvaar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravarsoversikt](Fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravarsprosent](Fravarsprosent.md) |
| Domain Of | [Fravarsoversikt](Fravarsoversikt.md) |
| Slot URI | [utd:halvaar](https://schema.fintlabs.no/utdanning/halvaar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fravarsoversikt](Fravarsoversikt.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:halvaar |
| native | https://schema.fintlabs.no/utdanning/:halvaar |




## LinkML Source

<details>
```yaml
name: halvaar
description: Fråværsprosent for halvåret.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:halvaar
alias: halvaar
owner: Fravarsoversikt
domain_of:
- Fravarsoversikt
range: Fravarsprosent
required: true
inlined: true

```
</details>