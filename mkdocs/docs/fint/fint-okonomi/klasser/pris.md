

# Slot: pris 



URI: [https://schema.fintlabs.no/okonomi/:pris](https://schema.fintlabs.no/okonomi/:pris)
Alias: pris

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vare](Vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Fakturalinje](Fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fakturalinje](Fakturalinje.md), [Vare](Vare.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:pris |
| native | https://schema.fintlabs.no/okonomi/:pris |




## LinkML Source

<details>
```yaml
name: pris
alias: pris
domain_of:
- Fakturalinje
- Vare
range: string

```
</details>