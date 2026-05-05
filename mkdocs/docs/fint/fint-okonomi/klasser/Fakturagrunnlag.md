

# Slot: fakturagrunnlag 



URI: [https://schema.fintlabs.no/okonomi/:fakturagrunnlag](https://schema.fintlabs.no/okonomi/:fakturagrunnlag)
Alias: fakturagrunnlag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md), [Faktura](faktura.md), [Fakturautsteder](fakturautsteder.md) |

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