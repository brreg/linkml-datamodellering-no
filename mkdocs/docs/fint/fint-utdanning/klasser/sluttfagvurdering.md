

# Slot: sluttfagvurdering 


_Sluttfagvurderingar._





URI: [utd:sluttfagvurdering](https://schema.fintlabs.no/utdanning/sluttfagvurdering)
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
| Range | [Sluttfagvurdering](sluttfagvurdering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevvurdering](elevvurdering.md) |
| Slot URI | [utd:sluttfagvurdering](https://schema.fintlabs.no/utdanning/sluttfagvurdering) |

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
| self | utd:sluttfagvurdering |
| native | https://schema.fintlabs.no/utdanning/:sluttfagvurdering |




## LinkML Source

<details>
```yaml
name: sluttfagvurdering
description: Sluttfagvurderingar.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:sluttfagvurdering
domain_of:
- UtdanningContainer
- Elevvurdering
range: Sluttfagvurdering
multivalued: true

```
</details>