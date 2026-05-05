

# Slot: elevvurdering 



URI: [https://schema.fintlabs.no/utdanning/:elevvurdering](https://schema.fintlabs.no/utdanning/:elevvurdering)
Alias: elevvurdering

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |  no  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |  no  |
| [Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Eksamensvurdering](eksamensvurdering.md), [Halvaarsfagvurdering](halvaarsfagvurdering.md), [Halvaarsordensvurdering](halvaarsordensvurdering.md), [Sluttfagvurdering](sluttfagvurdering.md), [Sluttordensvurdering](sluttordensvurdering.md), [Underveisfagvurdering](underveisfagvurdering.md), [Underveisordensvurdering](underveisordensvurdering.md) |

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