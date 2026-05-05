

# Slot: kjonn 


_Kjønn for personen._





URI: [fint:kjonn](https://schema.fintlabs.no/kjonn)
Alias: kjonn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kjonn](kjonn.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:kjonn](https://schema.fintlabs.no/kjonn) |

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


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kjonn |
| native | https://schema.fintlabs.no/utdanning/:kjonn |




## LinkML Source

<details>
```yaml
name: kjonn
description: Kjønn for personen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:kjonn
alias: kjonn
owner: Person
domain_of:
- Person
range: Kjonn

```
</details>