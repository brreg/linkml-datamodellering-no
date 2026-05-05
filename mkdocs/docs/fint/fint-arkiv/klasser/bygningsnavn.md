

# Slot: bygningsnavn 


_Bygningens namn._





URI: [ark:bygningsnavn](https://schema.fintlabs.no/arkiv/bygningsnavn)
Alias: bygningsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) |
| Slot URI | [ark:bygningsnavn](https://schema.fintlabs.no/arkiv/bygningsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:bygningsnavn |
| native | https://schema.fintlabs.no/arkiv/:bygningsnavn |




## LinkML Source

<details>
```yaml
name: bygningsnavn
description: Bygningens namn.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:bygningsnavn
alias: bygningsnavn
owner: TilskuddFredaBygningPrivatEie
domain_of:
- TilskuddFredaBygningPrivatEie
range: string

```
</details>