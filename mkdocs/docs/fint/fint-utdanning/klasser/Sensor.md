

# Slot: sensor 


_Sensor._





URI: [utd:sensor](https://schema.fintlabs.no/utdanning/sensor)
Alias: sensor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sensor](sensor.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Skoleressurs](skoleressurs.md), [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:sensor](https://schema.fintlabs.no/utdanning/sensor) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:sensor |
| native | https://schema.fintlabs.no/utdanning/:sensor |




## LinkML Source

<details>
```yaml
name: sensor
description: Sensor.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:sensor
alias: sensor
domain_of:
- UtdanningContainer
- Skoleressurs
- Eksamensgruppe
range: Sensor
multivalued: true

```
</details>