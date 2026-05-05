

# Slot: foreldre 


_Den/dei som har foreldreansvar til personen._





URI: [fint:foreldre](https://schema.fintlabs.no/foreldre)
Alias: foreldre

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:foreldre](https://schema.fintlabs.no/foreldre) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Person](person.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:foreldre |
| native | https://schema.fintlabs.no/arkiv/:foreldre |




## LinkML Source

<details>
```yaml
name: foreldre
description: Den/dei som har foreldreansvar til personen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: fint:foreldre
alias: foreldre
owner: Person
domain_of:
- Person
range: Person
multivalued: true

```
</details>