

# Slot: halvaarsfagvurdering 


_Halvårsfagvurderingar._





URI: [utd:halvaarsfagvurdering](https://schema.fintlabs.no/utdanning/halvaarsfagvurdering)
Alias: halvaarsfagvurdering

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
| Range | [Halvaarsfagvurdering](halvaarsfagvurdering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevvurdering](elevvurdering.md) |
| Slot URI | [utd:halvaarsfagvurdering](https://schema.fintlabs.no/utdanning/halvaarsfagvurdering) |

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
| self | utd:halvaarsfagvurdering |
| native | https://schema.fintlabs.no/utdanning/:halvaarsfagvurdering |




## LinkML Source

<details>
```yaml
name: halvaarsfagvurdering
description: Halvårsfagvurderingar.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:halvaarsfagvurdering
alias: halvaarsfagvurdering
domain_of:
- UtdanningContainer
- Elevvurdering
range: Halvaarsfagvurdering
multivalued: true

```
</details>