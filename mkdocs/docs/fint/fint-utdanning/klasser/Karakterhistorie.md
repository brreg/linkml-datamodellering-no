

# Slot: karakterhistorie 



URI: [https://schema.fintlabs.no/utdanning/:karakterhistorie](https://schema.fintlabs.no/utdanning/:karakterhistorie)
Alias: karakterhistorie

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Eksamensvurdering](eksamensvurdering.md), [Sluttfagvurdering](sluttfagvurdering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:karakterhistorie |
| native | https://schema.fintlabs.no/utdanning/:karakterhistorie |




## LinkML Source

<details>
```yaml
name: karakterhistorie
alias: karakterhistorie
domain_of:
- UtdanningContainer
- Eksamensvurdering
- Sluttfagvurdering
range: string

```
</details>