

# Slot: utsteder 


_Skoleressurs som sende varselet._





URI: [utd:utsteder](https://schema.fintlabs.no/utdanning/utsteder)
Alias: utsteder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](Varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleressurs](Skoleressurs.md) |
| Domain Of | [Varsel](Varsel.md) |
| Slot URI | [utd:utsteder](https://schema.fintlabs.no/utdanning/utsteder) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Varsel](Varsel.md) |








## In Subsets


* [Valgfri](Valgfri.md)






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