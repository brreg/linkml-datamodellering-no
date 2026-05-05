

# Slot: fravarsprosent 


_Fråværsprosent ved utsending av varselet._





URI: [utd:fravarsprosent](https://schema.fintlabs.no/utdanning/fravarsprosent)
Alias: fravarsprosent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Varsel](varsel.md) |
| Slot URI | [utd:fravarsprosent](https://schema.fintlabs.no/utdanning/fravarsprosent) |

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
| self | utd:fravarsprosent |
| native | https://schema.fintlabs.no/utdanning/:fravarsprosent |




## LinkML Source

<details>
```yaml
name: fravarsprosent
description: Fråværsprosent ved utsending av varselet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fravarsprosent
alias: fravarsprosent
owner: Varsel
domain_of:
- Varsel
range: integer

```
</details>