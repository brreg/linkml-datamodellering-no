

# Slot: fakturautsteder 



URI: [https://schema.fintlabs.no/okonomi/:fakturautsteder](https://schema.fintlabs.no/okonomi/:fakturautsteder)
Alias: fakturautsteder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md), [Vare](vare.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:fakturautsteder |
| native | https://schema.fintlabs.no/okonomi/:fakturautsteder |




## LinkML Source

<details>
```yaml
name: fakturautsteder
alias: fakturautsteder
domain_of:
- Fakturagrunnlag
- Vare
range: string

```
</details>