

# Slot: pris 



URI: [https://schema.fintlabs.no/okonomi/:pris](https://schema.fintlabs.no/okonomi/:pris)
Alias: pris

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturalinje](fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  no  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Fakturalinje](fakturalinje.md), [Vare](vare.md) |

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