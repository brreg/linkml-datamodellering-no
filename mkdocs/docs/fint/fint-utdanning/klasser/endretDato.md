

# Slot: endretDato 


_Dato og tidspunkt for endringa._





URI: [utd:endretDato](https://schema.fintlabs.no/utdanning/endretDato)
Alias: endretDato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterhistorie](Karakterhistorie.md) | Historikk over endringar i ein karakter |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Karakterhistorie](Karakterhistorie.md) |
| Slot URI | [utd:endretDato](https://schema.fintlabs.no/utdanning/endretDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Karakterhistorie](Karakterhistorie.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:endretDato |
| native | https://schema.fintlabs.no/utdanning/:endretDato |




## LinkML Source

<details>
```yaml
name: endretDato
description: Dato og tidspunkt for endringa.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:endretDato
alias: endretDato
owner: Karakterhistorie
domain_of:
- Karakterhistorie
range: datetime
required: true

```
</details>