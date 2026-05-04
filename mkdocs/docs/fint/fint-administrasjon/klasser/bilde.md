

# Slot: bilde 


_HTTP(S)-lenkje til eit bilete av personen._





URI: [fint:bilde](https://schema.fintlabs.no/bilde)
Alias: bilde

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [fint:bilde](https://schema.fintlabs.no/bilde) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Person](Person.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:bilde |
| native | https://schema.fintlabs.no/administrasjon/:bilde |




## LinkML Source

<details>
```yaml
name: bilde
description: HTTP(S)-lenkje til eit bilete av personen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:bilde
alias: bilde
owner: Person
domain_of:
- Person
range: string

```
</details>