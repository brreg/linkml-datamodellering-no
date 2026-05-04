

# Slot: oppdatertAv 


_Skoleressurs som oppdaterte karakteren._





URI: [utd:oppdatertAv](https://schema.fintlabs.no/utdanning/oppdatertAv)
Alias: oppdatertAv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterhistorie](Karakterhistorie.md) | Historikk over endringar i ein karakter |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleressurs](Skoleressurs.md) |
| Domain Of | [Karakterhistorie](Karakterhistorie.md) |
| Slot URI | [utd:oppdatertAv](https://schema.fintlabs.no/utdanning/oppdatertAv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Karakterhistorie](Karakterhistorie.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:oppdatertAv |
| native | https://schema.fintlabs.no/utdanning/:oppdatertAv |




## LinkML Source

<details>
```yaml
name: oppdatertAv
description: Skoleressurs som oppdaterte karakteren.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:oppdatertAv
alias: oppdatertAv
owner: Karakterhistorie
domain_of:
- Karakterhistorie
range: Skoleressurs

```
</details>