

# Slot: fartoyNavn 


_Fartøyets namn._





URI: [ark:fartoyNavn](https://schema.fintlabs.no/arkiv/fartoyNavn)
Alias: fartoyNavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFartoy](TilskuddFartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TilskuddFartoy](TilskuddFartoy.md) |
| Slot URI | [ark:fartoyNavn](https://schema.fintlabs.no/arkiv/fartoyNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TilskuddFartoy](TilskuddFartoy.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:fartoyNavn |
| native | https://schema.fintlabs.no/arkiv/:fartoyNavn |




## LinkML Source

<details>
```yaml
name: fartoyNavn
description: Fartøyets namn.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:fartoyNavn
alias: fartoyNavn
owner: TilskuddFartoy
domain_of:
- TilskuddFartoy
range: string
required: true

```
</details>