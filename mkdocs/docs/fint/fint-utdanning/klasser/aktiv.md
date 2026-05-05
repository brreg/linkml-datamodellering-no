

# Slot: aktiv 


_Angir om sensoren er aktiv._





URI: [utd:aktiv](https://schema.fintlabs.no/utdanning/aktiv)
Alias: aktiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](boolean.md) |
| Domain Of | [Sensor](sensor.md) |
| Slot URI | [utd:aktiv](https://schema.fintlabs.no/utdanning/aktiv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Sensor](sensor.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:aktiv |
| native | https://schema.fintlabs.no/utdanning/:aktiv |




## LinkML Source

<details>
```yaml
name: aktiv
description: Angir om sensoren er aktiv.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:aktiv
alias: aktiv
owner: Sensor
domain_of:
- Sensor
range: boolean
required: true

```
</details>