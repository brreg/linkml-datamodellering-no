

# Slot: sendt 


_Dato varselet vart sendt._





URI: [utd:sendt](https://schema.fintlabs.no/utdanning/sendt)
Alias: sendt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](Varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Varsel](Varsel.md) |
| Slot URI | [utd:sendt](https://schema.fintlabs.no/utdanning/sendt) |

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
| self | utd:sendt |
| native | https://schema.fintlabs.no/utdanning/:sendt |




## LinkML Source

<details>
```yaml
name: sendt
description: Dato varselet vart sendt.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:sendt
alias: sendt
owner: Varsel
domain_of:
- Varsel
range: date

```
</details>