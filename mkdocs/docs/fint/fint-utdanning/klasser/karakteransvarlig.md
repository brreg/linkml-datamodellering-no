

# Slot: karakteransvarlig 


_Skoleressurs som er ansvarleg for karakteren._





URI: [utd:karakteransvarlig](https://schema.fintlabs.no/utdanning/karakteransvarlig)
Alias: karakteransvarlig

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
| Slot URI | [utd:karakteransvarlig](https://schema.fintlabs.no/utdanning/karakteransvarlig) |

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