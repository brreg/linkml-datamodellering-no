

# Slot: utsteder 


_Skoleressurs som sende varselet._





URI: [utd:utsteder](https://schema.fintlabs.no/utdanning/utsteder)
Alias: utsteder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleressurs](skoleressurs.md) |
| Domain Of | [Varsel](varsel.md) |
| Slot URI | [utd:utsteder](https://schema.fintlabs.no/utdanning/utsteder) |

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
| self | utd:utsteder |
| native | https://schema.fintlabs.no/utdanning/:utsteder |




## LinkML Source

<details>
```yaml
name: utsteder
description: Skoleressurs som sende varselet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:utsteder
alias: utsteder
owner: Varsel
domain_of:
- Varsel
range: Skoleressurs

```
</details>