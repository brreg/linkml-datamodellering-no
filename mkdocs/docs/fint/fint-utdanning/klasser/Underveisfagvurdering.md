

# Slot: underveisfagvurdering 


_Underveisfagvurderingar._





URI: [utd:underveisfagvurdering](https://schema.fintlabs.no/utdanning/underveisfagvurdering)
Alias: underveisfagvurdering

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
| Range | [Underveisfagvurdering](underveisfagvurdering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevvurdering](elevvurdering.md) |
| Slot URI | [utd:underveisfagvurdering](https://schema.fintlabs.no/utdanning/underveisfagvurdering) |

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
| self | utd:underveisfagvurdering |
| native | https://schema.fintlabs.no/utdanning/:underveisfagvurdering |




## LinkML Source

<details>
```yaml
name: underveisfagvurdering
description: Underveisfagvurderingar.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:underveisfagvurdering
alias: underveisfagvurdering
domain_of:
- UtdanningContainer
- Elevvurdering
range: Underveisfagvurdering
multivalued: true

```
</details>