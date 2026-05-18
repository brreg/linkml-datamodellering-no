

# Slot: underveisordensvurdering 


_Underveisordensvurderingar._





URI: [utd:underveisordensvurdering](https://schema.fintlabs.no/utdanning/underveisordensvurdering)
Alias: underveisordensvurdering

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
| Range | [Underveisordensvurdering](underveisordensvurdering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevvurdering](elevvurdering.md) |
| Slot URI | [utd:underveisordensvurdering](https://schema.fintlabs.no/utdanning/underveisordensvurdering) |

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
| self | utd:underveisordensvurdering |
| native | https://schema.fintlabs.no/utdanning/:underveisordensvurdering |




## LinkML Source

<details>
```yaml
name: underveisordensvurdering
description: Underveisordensvurderingar.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:underveisordensvurdering
alias: underveisordensvurdering
domain_of:
- UtdanningContainer
- Elevvurdering
range: Underveisordensvurdering
multivalued: true

```
</details>