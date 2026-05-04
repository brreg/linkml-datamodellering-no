

# Slot: data 


_Dokumentfilens data, koda som Base64._





URI: [ark:data](https://schema.fintlabs.no/arkiv/data)
Alias: data

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentfil](Dokumentfil.md) | Sjølve dokumentfila med data og metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Dokumentfil](Dokumentfil.md) |
| Slot URI | [ark:data](https://schema.fintlabs.no/arkiv/data) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentfil](Dokumentfil.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:data |
| native | https://schema.fintlabs.no/arkiv/:data |




## LinkML Source

<details>
```yaml
name: data
description: Dokumentfilens data, koda som Base64.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:data
alias: data
owner: Dokumentfil
domain_of:
- Dokumentfil
range: string
required: true

```
</details>