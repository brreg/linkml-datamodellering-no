

# Slot: tilgangs_url 


_URL for tilgang til distribusjonen._





URI: [dcat:accessURL](http://www.w3.org/ns/dcat#accessURL)
Alias: tilgangs_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Distribusjon](Distribusjon.md) |
| Slot URI | [dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) |

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
| self | dcat:accessURL |
| native | https://data.norge.no/linkml/dcat-ap-no/tilgangs_url |




## LinkML Source

<details>
```yaml
name: tilgangs_url
description: URL for tilgang til distribusjonen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:accessURL
alias: tilgangs_url
domain_of:
- Distribusjon
range: uri
multivalued: true

```
</details>