

# Slot: adresse 



URI: [https://schema.fintlabs.no/okonomi/:adresse](https://schema.fintlabs.no/okonomi/:adresse)
Alias: adresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](Matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Faktura](Faktura.md), [Matrikkelnummer](Matrikkelnummer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:adresse |
| native | https://schema.fintlabs.no/okonomi/:adresse |




## LinkML Source

<details>
```yaml
name: adresse
alias: adresse
domain_of:
- Faktura
- Matrikkelnummer
range: string

```
</details>