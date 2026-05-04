

# Slot: vare 



URI: [https://schema.fintlabs.no/okonomi/:vare](https://schema.fintlabs.no/okonomi/:vare)
Alias: vare

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturautsteder](Fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |
| [Fakturalinje](Fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fakturautsteder](Fakturautsteder.md), [Fakturalinje](Fakturalinje.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:vare |
| native | https://schema.fintlabs.no/okonomi/:vare |




## LinkML Source

<details>
```yaml
name: vare
alias: vare
domain_of:
- Fakturautsteder
- Fakturalinje
range: string

```
</details>