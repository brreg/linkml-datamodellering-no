

# Slot: tosprakligFagopplaering 


_Indikerer om eleven har tospråkleg fagopplæring._





URI: [utd:tosprakligFagopplaering](https://schema.fintlabs.no/utdanning/tosprakligFagopplaering)
Alias: tosprakligFagopplaering

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](boolean.md) |
| Domain Of | [Elevforhold](elevforhold.md) |
| Slot URI | [utd:tosprakligFagopplaering](https://schema.fintlabs.no/utdanning/tosprakligFagopplaering) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Elevforhold](elevforhold.md) |








## In Subsets


* [Valgfri](valgfri.md)






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