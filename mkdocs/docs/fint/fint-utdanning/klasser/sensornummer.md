

# Slot: sensornummer 


_Sensornummer._





URI: [utd:sensornummer](https://schema.fintlabs.no/utdanning/sensornummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Sensor](sensor.md) |
| Slot URI | [utd:sensornummer](https://schema.fintlabs.no/utdanning/sensornummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:sensornummer
domain_of:
- Sensor
range: integer

```
</details>