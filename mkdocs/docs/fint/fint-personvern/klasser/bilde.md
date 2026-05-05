

# Slot: bilde 


_HTTP(S)-lenkje til eit bilete av personen._





URI: [fint:bilde](https://schema.fintlabs.no/bilde)
Alias: bilde

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:bilde](https://schema.fintlabs.no/bilde) |

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


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:bilde |
| native | https://schema.fintlabs.no/personvern/:bilde |




## LinkML Source

<details>
```yaml
name: bilde
description: HTTP(S)-lenkje til eit bilete av personen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:bilde
alias: bilde
owner: Person
domain_of:
- Person
range: string

```
</details>