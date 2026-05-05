

# Slot: mottaker 



URI: [https://schema.fintlabs.no/okonomi/:mottaker](https://schema.fintlabs.no/okonomi/:mottaker)
Alias: mottaker

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Faktura](faktura.md), [Fakturagrunnlag](fakturagrunnlag.md) |

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