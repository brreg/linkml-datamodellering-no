

# Slot: nedlastningslenke 


_Direkte nedlastingslenke for distribusjonsfila._





URI: [dcat:downloadURL](http://www.w3.org/ns/dcat#downloadURL)
Alias: nedlastningslenke

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Distribusjon](Distribusjon.md) |
| Slot URI | [dcat:downloadURL](http://www.w3.org/ns/dcat#downloadURL) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:downloadURL |
| native | https://data.norge.no/linkml/dcat-ap-no/nedlastningslenke |




## LinkML Source

<details>
```yaml
name: nedlastningslenke
description: Direkte nedlastingslenke for distribusjonsfila.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:downloadURL
alias: nedlastningslenke
domain_of:
- Distribusjon
range: uri
multivalued: true

```
</details>