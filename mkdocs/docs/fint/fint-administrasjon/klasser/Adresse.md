

# Slot: adresse 


_Adresse til matrikkeleining._





URI: [fint:adresse](https://schema.fintlabs.no/adresse)
Alias: adresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Matrikkelnummer](matrikkelnummer.md) |
| Slot URI | [fint:adresse](https://schema.fintlabs.no/adresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Matrikkelnummer](matrikkelnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:adresse |
| native | https://schema.fintlabs.no/administrasjon/:adresse |




## LinkML Source

<details>
```yaml
name: adresse
description: Adresse til matrikkeleining.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:adresse
alias: adresse
owner: Matrikkelnummer
domain_of:
- Matrikkelnummer
range: Adresse
inlined: true

```
</details>