

# Slot: personalressurs 


_Referanse til Personalressurs (Administrasjon)._





URI: [fint:personalressurs](https://schema.fintlabs.no/personalressurs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:personalressurs](https://schema.fintlabs.no/personalressurs) |

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


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:personalressurs |
| native | https://schema.fintlabs.no/:personalressurs |




## LinkML Source

<details>
```yaml
name: personalressurs
description: Referanse til Personalressurs (Administrasjon).
in_subset:
- Valgfri
from_schema: https://data.norge.no/fint/fint-common
rank: 1000
slot_uri: fint:personalressurs
owner: Person
domain_of:
- Person
range: uriorcurie

```
</details>