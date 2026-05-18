

# Slot: sluttordensvurdering 


_Sluttordensvurderingar._





URI: [utd:sluttordensvurdering](https://schema.fintlabs.no/utdanning/sluttordensvurdering)
Alias: sluttordensvurdering

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
| Range | [Sluttordensvurdering](sluttordensvurdering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevvurdering](elevvurdering.md) |
| Slot URI | [utd:sluttordensvurdering](https://schema.fintlabs.no/utdanning/sluttordensvurdering) |

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
| self | utd:sluttordensvurdering |
| native | https://schema.fintlabs.no/utdanning/:sluttordensvurdering |




## LinkML Source

<details>
```yaml
name: sluttordensvurdering
description: Sluttordensvurderingar.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:sluttordensvurdering
alias: sluttordensvurdering
domain_of:
- UtdanningContainer
- Elevvurdering
range: Sluttordensvurdering
multivalued: true

```
</details>