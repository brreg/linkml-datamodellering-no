

# Slot: tosprakligFagopplaering 


_Indikerer om eleven har tospråkleg fagopplæring._





URI: [utd:tosprakligFagopplaering](https://schema.fintlabs.no/utdanning/tosprakligFagopplaering)
Alias: tosprakligFagopplaering

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Elevforhold](Elevforhold.md) |
| Slot URI | [utd:tosprakligFagopplaering](https://schema.fintlabs.no/utdanning/tosprakligFagopplaering) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Elevforhold](Elevforhold.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:tosprakligFagopplaering |
| native | https://schema.fintlabs.no/utdanning/:tosprakligFagopplaering |




## LinkML Source

<details>
```yaml
name: tosprakligFagopplaering
description: Indikerer om eleven har tospråkleg fagopplæring.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:tosprakligFagopplaering
alias: tosprakligFagopplaering
owner: Elevforhold
domain_of:
- Elevforhold
range: boolean

```
</details>