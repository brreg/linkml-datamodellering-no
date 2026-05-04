

# Slot: sensornummer 


_Sensornummer._





URI: [utd:sensornummer](https://schema.fintlabs.no/utdanning/sensornummer)
Alias: sensornummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sensor](Sensor.md) | Ein sensor for ein eksamen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Sensor](Sensor.md) |
| Slot URI | [utd:sensornummer](https://schema.fintlabs.no/utdanning/sensornummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Sensor](Sensor.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:sensornummer |
| native | https://schema.fintlabs.no/utdanning/:sensornummer |




## LinkML Source

<details>
```yaml
name: sensornummer
description: Sensornummer.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:sensornummer
alias: sensornummer
owner: Sensor
domain_of:
- Sensor
range: integer

```
</details>