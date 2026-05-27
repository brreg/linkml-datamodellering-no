

# Slot: eksamensvurdering 


_Eksamensvurderingar._





URI: [utd:eksamensvurdering](https://schema.fintlabs.no/utdanning/eksamensvurdering)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevvurdering](elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eksamensvurdering](eksamensvurdering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevvurdering](elevvurdering.md) |
| Slot URI | [utd:eksamensvurdering](https://schema.fintlabs.no/utdanning/eksamensvurdering) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:eksamensvurdering |
| native | https://schema.fintlabs.no/utdanning/:eksamensvurdering |




## LinkML Source

<details>
```yaml
name: eksamensvurdering
description: Eksamensvurderingar.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:eksamensvurdering
domain_of:
- UtdanningContainer
- Elevvurdering
range: Eksamensvurdering
multivalued: true

```
</details>