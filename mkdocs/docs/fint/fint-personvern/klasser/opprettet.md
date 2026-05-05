

# Slot: opprettet 


_Dato då samtykket vart oppretta._





URI: [pvn:opprettet](https://schema.fintlabs.no/personvern/opprettet)
Alias: opprettet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Samtykke](samtykke.md) |
| Slot URI | [pvn:opprettet](https://schema.fintlabs.no/personvern/opprettet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Samtykke](samtykke.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:opprettet |
| native | https://schema.fintlabs.no/personvern/:opprettet |




## LinkML Source

<details>
```yaml
name: opprettet
description: Dato då samtykket vart oppretta.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:opprettet
alias: opprettet
owner: Samtykke
domain_of:
- Samtykke
range: datetime
required: true

```
</details>