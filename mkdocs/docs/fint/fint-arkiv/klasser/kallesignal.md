

# Slot: kallesignal 


_Fartøyets kallesignal._





URI: [ark:kallesignal](https://schema.fintlabs.no/arkiv/kallesignal)
Alias: kallesignal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [TilskuddFartoy](tilskuddfartoy.md) |
| Slot URI | [ark:kallesignal](https://schema.fintlabs.no/arkiv/kallesignal) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TilskuddFartoy](tilskuddfartoy.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:kallesignal |
| native | https://schema.fintlabs.no/arkiv/:kallesignal |




## LinkML Source

<details>
```yaml
name: kallesignal
description: Fartøyets kallesignal.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:kallesignal
alias: kallesignal
owner: TilskuddFartoy
domain_of:
- TilskuddFartoy
range: string
required: true

```
</details>