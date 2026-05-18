

# Slot: karakterhistorie 


_Karakterhistorikk._





URI: [utd:karakterhistorie](https://schema.fintlabs.no/utdanning/karakterhistorie)
Alias: karakterhistorie

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterhistorie](karakterhistorie.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Eksamensvurdering](eksamensvurdering.md), [Sluttfagvurdering](sluttfagvurdering.md) |
| Slot URI | [utd:karakterhistorie](https://schema.fintlabs.no/utdanning/karakterhistorie) |

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
| self | utd:karakterhistorie |
| native | https://schema.fintlabs.no/utdanning/:karakterhistorie |




## LinkML Source

<details>
```yaml
name: karakterhistorie
description: Karakterhistorikk.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:karakterhistorie
alias: karakterhistorie
domain_of:
- UtdanningContainer
- Eksamensvurdering
- Sluttfagvurdering
range: Karakterhistorie
multivalued: true

```
</details>