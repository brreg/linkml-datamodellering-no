

# Slot: personalressurs 


_Referanse til Personalressurs (Administrasjon)._





URI: [fint:personalressurs](https://schema.fintlabs.no/personalressurs)
Alias: personalressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [fint:personalressurs](https://schema.fintlabs.no/personalressurs) |

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


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:personalressurs |
| native | https://schema.fintlabs.no/okonomi/:personalressurs |




## LinkML Source

<details>
```yaml
name: personalressurs
description: Referanse til Personalressurs (Administrasjon).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:personalressurs
alias: personalressurs
owner: Person
domain_of:
- Person
range: uriorcurie

```
</details>