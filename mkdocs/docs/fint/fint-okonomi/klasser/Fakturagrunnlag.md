

# Slot: fakturagrunnlag 



URI: [https://schema.fintlabs.no/okonomi/:fakturagrunnlag](https://schema.fintlabs.no/okonomi/:fakturagrunnlag)
Alias: fakturagrunnlag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](OkonomiContainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |
| [Fakturautsteder](Fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OkonomiContainer](OkonomiContainer.md), [Faktura](Faktura.md), [Fakturautsteder](Fakturautsteder.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:fakturagrunnlag |
| native | https://schema.fintlabs.no/okonomi/:fakturagrunnlag |




## LinkML Source

<details>
```yaml
name: fakturagrunnlag
alias: fakturagrunnlag
domain_of:
- OkonomiContainer
- Faktura
- Fakturautsteder
range: string

```
</details>