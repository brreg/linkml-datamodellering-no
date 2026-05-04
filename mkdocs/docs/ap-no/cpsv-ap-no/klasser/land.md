

# Slot: land 


_Land (ISO 3166-1 alpha-2 kode)._





URI: [locn:adminUnitL1](http://www.w3.org/ns/locn#adminUnitL1)
Alias: land

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adresse](Adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Adresse](Adresse.md) |
| Slot URI | [locn:adminUnitL1](http://www.w3.org/ns/locn#adminUnitL1) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:adminUnitL1 |
| native | https://data.norge.no/linkml/cpsv-ap-no/land |




## LinkML Source

<details>
```yaml
name: land
description: Land (ISO 3166-1 alpha-2 kode).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: locn:adminUnitL1
alias: land
domain_of:
- Adresse
range: string

```
</details>