

# Slot: adresse 


_Adresse til matrikkeleining._





URI: [fint:adresse](https://schema.fintlabs.no/adresse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Matrikkelnummer](matrikkelnummer.md), [Faktura](faktura.md) |
| Slot URI | [fint:adresse](https://schema.fintlabs.no/adresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:adresse |
| native | https://schema.fintlabs.no/:adresse |




## LinkML Source

<details>
```yaml
name: adresse
description: Adresse til matrikkeleining.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:adresse
domain_of:
- Matrikkelnummer
- Faktura
range: Adresse
inlined: true

```
</details>