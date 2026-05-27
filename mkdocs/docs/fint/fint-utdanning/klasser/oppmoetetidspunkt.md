

# Slot: oppmoetetidspunkt 


_Tidspunkt for oppmøte._





URI: [utd:oppmoetetidspunkt](https://schema.fintlabs.no/utdanning/oppmoetetidspunkt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Eksamen](eksamen.md) |
| Slot URI | [utd:oppmoetetidspunkt](https://schema.fintlabs.no/utdanning/oppmoetetidspunkt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:oppmoetetidspunkt |
| native | https://schema.fintlabs.no/utdanning/:oppmoetetidspunkt |




## LinkML Source

<details>
```yaml
name: oppmoetetidspunkt
description: Tidspunkt for oppmøte.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:oppmoetetidspunkt
domain_of:
- Eksamen
range: datetime

```
</details>