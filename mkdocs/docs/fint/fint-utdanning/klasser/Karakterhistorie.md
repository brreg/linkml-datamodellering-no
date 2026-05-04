

# Slot: karakterhistorie 



URI: [https://schema.fintlabs.no/utdanning/:karakterhistorie](https://schema.fintlabs.no/utdanning/:karakterhistorie)
Alias: karakterhistorie

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Eksamensvurdering](Eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Sluttfagvurdering](Sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Eksamensvurdering](Eksamensvurdering.md), [Sluttfagvurdering](Sluttfagvurdering.md) |

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