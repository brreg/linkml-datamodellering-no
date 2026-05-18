

# Slot: elevvurdering 


_Elevvurderingsobjekt._





URI: [utd:elevvurdering](https://schema.fintlabs.no/utdanning/elevvurdering)
Alias: elevvurdering

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  yes  |
| [Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  yes  |
| [Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  yes  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  yes  |
| [Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  yes  |
| [Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevvurdering](elevvurdering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Eksamensvurdering](eksamensvurdering.md), [Halvaarsfagvurdering](halvaarsfagvurdering.md), [Halvaarsordensvurdering](halvaarsordensvurdering.md), [Sluttfagvurdering](sluttfagvurdering.md), [Sluttordensvurdering](sluttordensvurdering.md), [Underveisfagvurdering](underveisfagvurdering.md), [Underveisordensvurdering](underveisordensvurdering.md) |
| Slot URI | [utd:elevvurdering](https://schema.fintlabs.no/utdanning/elevvurdering) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:elevvurdering |
| native | https://schema.fintlabs.no/utdanning/:elevvurdering |




## LinkML Source

<details>
```yaml
name: elevvurdering
description: Elevvurderingsobjekt.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:elevvurdering
alias: elevvurdering
domain_of:
- UtdanningContainer
- Elevforhold
- Eksamensvurdering
- Halvaarsfagvurdering
- Halvaarsordensvurdering
- Sluttfagvurdering
- Sluttordensvurdering
- Underveisfagvurdering
- Underveisordensvurdering
range: Elevvurdering

```
</details>