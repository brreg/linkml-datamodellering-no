

# Slot: filstorrelse 


_Storleiken på fila i antal bytes._





URI: [ark:filstorrelse](https://schema.fintlabs.no/arkiv/filstorrelse)
Alias: filstorrelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Dokumentobjekt](dokumentobjekt.md) |
| Slot URI | [ark:filstorrelse](https://schema.fintlabs.no/arkiv/filstorrelse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentobjekt](dokumentobjekt.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:filstorrelse |
| native | https://schema.fintlabs.no/arkiv/:filstorrelse |




## LinkML Source

<details>
```yaml
name: filstorrelse
description: Storleiken på fila i antal bytes.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:filstorrelse
alias: filstorrelse
owner: Dokumentobjekt
domain_of:
- Dokumentobjekt
range: string

```
</details>