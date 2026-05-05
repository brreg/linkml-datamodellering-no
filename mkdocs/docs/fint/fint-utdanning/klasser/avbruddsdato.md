

# Slot: avbruddsdato 


_Dato for avbrot frå opplæring._





URI: [utd:avbruddsdato](https://schema.fintlabs.no/utdanning/avbruddsdato)
Alias: avbruddsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](date.md) |
| Domain Of | [Elevforhold](elevforhold.md) |
| Slot URI | [utd:avbruddsdato](https://schema.fintlabs.no/utdanning/avbruddsdato) |

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
| self | utd:avbruddsdato |
| native | https://schema.fintlabs.no/utdanning/:avbruddsdato |




## LinkML Source

<details>
```yaml
name: avbruddsdato
description: Dato for avbrot frå opplæring.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:avbruddsdato
alias: avbruddsdato
owner: Elevforhold
domain_of:
- Elevforhold
range: date

```
</details>