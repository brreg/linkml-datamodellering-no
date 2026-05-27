

# Slot: utsteder 


_Skoleressurs som sende varselet._





URI: [utd:utsteder](https://schema.fintlabs.no/utdanning/utsteder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:utsteder
domain_of:
- Varsel
range: Skoleressurs

```
</details>