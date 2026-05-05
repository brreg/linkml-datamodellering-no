

# Slot: tekst 


_Innhald i varselet._





URI: [utd:tekst](https://schema.fintlabs.no/utdanning/tekst)
Alias: tekst

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Varsel](varsel.md) |
| Slot URI | [utd:tekst](https://schema.fintlabs.no/utdanning/tekst) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Varsel](varsel.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:tekst |
| native | https://schema.fintlabs.no/utdanning/:tekst |




## LinkML Source

<details>
```yaml
name: tekst
description: Innhald i varselet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:tekst
alias: tekst
owner: Varsel
domain_of:
- Varsel
range: string

```
</details>