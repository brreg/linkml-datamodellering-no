

# Slot: rettighet 


_Rettigheiter knytt til identiteten._





URI: [res:rettighet](https://schema.fintlabs.no/ressurs/rettighet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Identitet](identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rettighet](rettighet.md) |
| Domain Of | [Identitet](identitet.md) |
| Slot URI | [res:rettighet](https://schema.fintlabs.no/ressurs/rettighet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:rettighet |
| native | https://schema.fintlabs.no/ressurs/:rettighet |




## LinkML Source

<details>
```yaml
name: rettighet
description: Rettigheiter knytt til identiteten.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slot_uri: res:rettighet
domain_of:
- Identitet
range: Rettighet
multivalued: true

```
</details>