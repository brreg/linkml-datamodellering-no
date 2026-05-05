

# Slot: fodselsnummer 


_Fødselsnummer eller ein av dei fiktive variantane._





URI: [fint:fodselsnummer](https://schema.fintlabs.no/fodselsnummer)
Alias: fodselsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:fodselsnummer](https://schema.fintlabs.no/fodselsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Person](person.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:fodselsnummer |
| native | https://schema.fintlabs.no/arkiv/:fodselsnummer |




## LinkML Source

<details>
```yaml
name: fodselsnummer
description: Fødselsnummer eller ein av dei fiktive variantane.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: fint:fodselsnummer
alias: fodselsnummer
owner: Person
domain_of:
- Person
range: Identifikator
required: true
inlined: true

```
</details>