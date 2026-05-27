

# Slot: aktiv 


_Angir om sensoren er aktiv._





URI: [utd:aktiv](https://schema.fintlabs.no/utdanning/aktiv)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [Sensor](sensor.md) |
| Slot URI | [utd:aktiv](https://schema.fintlabs.no/utdanning/aktiv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:aktiv
domain_of:
- Sensor
range: boolean

```
</details>