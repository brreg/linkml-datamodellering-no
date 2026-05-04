

# Slot: partNavn 


_Namn på verksemd eller person som er part._





URI: [ark:partNavn](https://schema.fintlabs.no/arkiv/partNavn)
Alias: partNavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Part](Part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Part](Part.md) |
| Slot URI | [ark:partNavn](https://schema.fintlabs.no/arkiv/partNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Part](Part.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:partNavn |
| native | https://schema.fintlabs.no/arkiv/:partNavn |




## LinkML Source

<details>
```yaml
name: partNavn
description: Namn på verksemd eller person som er part.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:partNavn
alias: partNavn
owner: Part
domain_of:
- Part
range: string
required: true

```
</details>