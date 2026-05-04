

# Slot: elevvurdering 



URI: [https://schema.fintlabs.no/utdanning/:elevvurdering](https://schema.fintlabs.no/utdanning/:elevvurdering)
Alias: elevvurdering

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttordensvurdering](Sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Underveisfagvurdering](Underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Underveisordensvurdering](Underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Halvaarsordensvurdering](Halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [Eksamensvurdering](Eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Sluttfagvurdering](Sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [Halvaarsfagvurdering](Halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Elevforhold](Elevforhold.md), [Eksamensvurdering](Eksamensvurdering.md), [Halvaarsfagvurdering](Halvaarsfagvurdering.md), [Halvaarsordensvurdering](Halvaarsordensvurdering.md), [Sluttfagvurdering](Sluttfagvurdering.md), [Sluttordensvurdering](Sluttordensvurdering.md), [Underveisfagvurdering](Underveisfagvurdering.md), [Underveisordensvurdering](Underveisordensvurdering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:elevvurdering |
| native | https://schema.fintlabs.no/utdanning/:elevvurdering |




## LinkML Source

<details>
```yaml
name: elevvurdering
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
range: string

```
</details>