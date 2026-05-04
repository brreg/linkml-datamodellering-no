

# Slot: mottaker 



URI: [https://schema.fintlabs.no/okonomi/:mottaker](https://schema.fintlabs.no/okonomi/:mottaker)
Alias: mottaker

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](Fakturagrunnlag.md) | Grunnlag for fakturering |  no  |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Faktura](Faktura.md), [Fakturagrunnlag](Fakturagrunnlag.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:mottaker |
| native | https://schema.fintlabs.no/okonomi/:mottaker |




## LinkML Source

<details>
```yaml
name: mottaker
alias: mottaker
domain_of:
- Faktura
- Fakturagrunnlag
range: string

```
</details>