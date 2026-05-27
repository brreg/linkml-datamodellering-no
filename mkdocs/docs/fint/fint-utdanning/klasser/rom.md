

# Slot: rom 


_Rom._





URI: [utd:rom](https://schema.fintlabs.no/utdanning/rom)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  yes  |
| [Time](time.md) | Ein time i timeplanen |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rom](rom.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Eksamen](eksamen.md), [Time](time.md) |
| Slot URI | [utd:rom](https://schema.fintlabs.no/utdanning/rom) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:rom |
| native | https://schema.fintlabs.no/utdanning/:rom |




## LinkML Source

<details>
```yaml
name: rom
description: Rom.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:rom
domain_of:
- UtdanningContainer
- Eksamen
- Time
range: Rom

```
</details>