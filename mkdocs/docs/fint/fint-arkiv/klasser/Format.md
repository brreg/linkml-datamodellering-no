

# Slot: format 


_Format på dokumentfil, som IANA Media Type._





URI: [ark:format](https://schema.fintlabs.no/arkiv/format)
Alias: format

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
| Slot URI | [ark:format](https://schema.fintlabs.no/arkiv/format) |

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
| self | ark:format |
| native | https://schema.fintlabs.no/arkiv/:format |




## LinkML Source

<details>
```yaml
name: format
description: Format på dokumentfil, som IANA Media Type.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:format
alias: format
owner: Dokumentfil
domain_of:
- Dokumentfil
range: string
required: true

```
</details>