

# Slot: filnavn 


_Dokumentfilens namn._





URI: [ark:filnavn](https://schema.fintlabs.no/arkiv/filnavn)
Alias: filnavn

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
| Slot URI | [ark:filnavn](https://schema.fintlabs.no/arkiv/filnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentfil](Dokumentfil.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:filnavn |
| native | https://schema.fintlabs.no/arkiv/:filnavn |




## LinkML Source

<details>
```yaml
name: filnavn
description: Dokumentfilens namn.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:filnavn
alias: filnavn
owner: Dokumentfil
domain_of:
- Dokumentfil
range: string

```
</details>