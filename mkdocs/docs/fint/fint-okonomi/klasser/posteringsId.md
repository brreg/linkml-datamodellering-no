

# Slot: posteringsId 


_Intern unik identifikator i økonomisystemet._





URI: [okn:posteringsId](https://schema.fintlabs.no/okonomi/posteringsId)
Alias: posteringsId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Postering](postering.md) |
| Slot URI | [okn:posteringsId](https://schema.fintlabs.no/okonomi/posteringsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Postering](postering.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:posteringsId |
| native | https://schema.fintlabs.no/okonomi/:posteringsId |




## LinkML Source

<details>
```yaml
name: posteringsId
description: Intern unik identifikator i økonomisystemet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:posteringsId
alias: posteringsId
owner: Postering
domain_of:
- Postering
range: Identifikator
required: true
inlined: true

```
</details>