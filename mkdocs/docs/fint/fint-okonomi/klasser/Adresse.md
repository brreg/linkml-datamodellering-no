

# Slot: adresse 



URI: [https://schema.fintlabs.no/okonomi/:adresse](https://schema.fintlabs.no/okonomi/:adresse)
Alias: adresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Faktura](faktura.md), [Matrikkelnummer](matrikkelnummer.md) |

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