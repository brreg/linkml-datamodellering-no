

# Slot: opprettet 


_Dato då samtykket vart oppretta._





URI: [pvn:opprettet](https://schema.fintlabs.no/personvern/opprettet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Samtykke](samtykke.md) |
| Slot URI | [pvn:opprettet](https://schema.fintlabs.no/personvern/opprettet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




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
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
slot_uri: pvn:opprettet
domain_of:
- Samtykke
range: datetime

```
</details>