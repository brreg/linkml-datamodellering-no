

# Slot: tidsrom 


_Tidsrom._





URI: [utd:tidsrom](https://schema.fintlabs.no/utdanning/tidsrom)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  yes  |
| [Time](time.md) | Ein time i timeplanen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Eksamen](eksamen.md), [Time](time.md) |
| Slot URI | [utd:tidsrom](https://schema.fintlabs.no/utdanning/tidsrom) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:tidsrom |
| native | https://schema.fintlabs.no/utdanning/:tidsrom |




## LinkML Source

<details>
```yaml
name: tidsrom
description: Tidsrom.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:tidsrom
domain_of:
- Eksamen
- Time
range: Periode
inlined: true

```
</details>