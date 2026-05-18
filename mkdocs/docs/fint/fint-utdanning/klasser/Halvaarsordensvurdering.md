

# Slot: halvaarsordensvurdering 


_Halvårsordensvurderingar._





URI: [utd:halvaarsordensvurdering](https://schema.fintlabs.no/utdanning/halvaarsordensvurdering)
Alias: halvaarsordensvurdering

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
| Range | [Halvaarsordensvurdering](halvaarsordensvurdering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevvurdering](elevvurdering.md) |
| Slot URI | [utd:halvaarsordensvurdering](https://schema.fintlabs.no/utdanning/halvaarsordensvurdering) |

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
| self | utd:halvaarsordensvurdering |
| native | https://schema.fintlabs.no/utdanning/:halvaarsordensvurdering |




## LinkML Source

<details>
```yaml
name: halvaarsordensvurdering
description: Halvårsordensvurderingar.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:halvaarsordensvurdering
alias: halvaarsordensvurdering
domain_of:
- UtdanningContainer
- Elevvurdering
range: Halvaarsordensvurdering
multivalued: true

```
</details>