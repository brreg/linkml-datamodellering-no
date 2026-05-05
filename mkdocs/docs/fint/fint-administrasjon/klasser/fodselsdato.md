

# Slot: fodselsdato 


_Dato for fødsel._





URI: [fint:fodselsdato](https://schema.fintlabs.no/fodselsdato)
Alias: fodselsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](date.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:fodselsdato](https://schema.fintlabs.no/fodselsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Person](person.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:fodselsdato |
| native | https://schema.fintlabs.no/administrasjon/:fodselsdato |




## LinkML Source

<details>
```yaml
name: fodselsdato
description: Dato for fødsel.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:fodselsdato
alias: fodselsdato
owner: Person
domain_of:
- Person
range: date

```
</details>