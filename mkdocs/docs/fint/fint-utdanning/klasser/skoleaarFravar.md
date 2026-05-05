

# Slot: skoleaarFravar 


_Fråværsprosent for heile skoleåret._





URI: [utd:skoleaarFravar](https://schema.fintlabs.no/utdanning/skoleaarFravar)
Alias: skoleaarFravar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravarsoversikt](fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravarsprosent](fravarsprosent.md) |
| Domain Of | [Fravarsoversikt](fravarsoversikt.md) |
| Slot URI | [utd:skoleaarFravar](https://schema.fintlabs.no/utdanning/skoleaarFravar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fravarsoversikt](fravarsoversikt.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skoleaarFravar |
| native | https://schema.fintlabs.no/utdanning/:skoleaarFravar |




## LinkML Source

<details>
```yaml
name: skoleaarFravar
description: Fråværsprosent for heile skoleåret.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skoleaarFravar
alias: skoleaarFravar
owner: Fravarsoversikt
domain_of:
- Fravarsoversikt
range: Fravarsprosent
required: true
inlined: true

```
</details>