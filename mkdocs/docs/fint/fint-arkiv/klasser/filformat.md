

# Slot: filformat 


_Dokumentets format._





URI: [ark:filformat](https://schema.fintlabs.no/arkiv/filformat)
Alias: filformat

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentobjekt](Dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Format](Format.md) |
| Domain Of | [Dokumentobjekt](Dokumentobjekt.md) |
| Slot URI | [ark:filformat](https://schema.fintlabs.no/arkiv/filformat) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentobjekt](Dokumentobjekt.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:filformat |
| native | https://schema.fintlabs.no/arkiv/:filformat |




## LinkML Source

<details>
```yaml
name: filformat
description: Dokumentets format.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:filformat
alias: filformat
owner: Dokumentobjekt
domain_of:
- Dokumentobjekt
range: Format

```
</details>