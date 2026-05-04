

# Slot: karakteransvarlig 


_Skoleressurs som er ansvarleg for karakteren._





URI: [utd:karakteransvarlig](https://schema.fintlabs.no/utdanning/karakteransvarlig)
Alias: karakteransvarlig

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
| Slot URI | [utd:karakteransvarlig](https://schema.fintlabs.no/utdanning/karakteransvarlig) |

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
| self | utd:karakteransvarlig |
| native | https://schema.fintlabs.no/utdanning/:karakteransvarlig |




## LinkML Source

<details>
```yaml
name: karakteransvarlig
description: Skoleressurs som er ansvarleg for karakteren.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:karakteransvarlig
alias: karakteransvarlig
owner: Varsel
domain_of:
- Varsel
range: Skoleressurs

```
</details>