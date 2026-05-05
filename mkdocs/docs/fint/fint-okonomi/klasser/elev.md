

# Slot: elev 


_Referanse til Elev (Utdanning)._





URI: [fint:elev](https://schema.fintlabs.no/elev)
Alias: elev

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:elev](https://schema.fintlabs.no/elev) |

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


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:elev |
| native | https://schema.fintlabs.no/okonomi/:elev |




## LinkML Source

<details>
```yaml
name: elev
description: Referanse til Elev (Utdanning).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:elev
alias: elev
owner: Person
domain_of:
- Person
range: uriorcurie

```
</details>