

# Slot: tilgangs_url 


_URL for tilgang til distribusjonen._





URI: [dcat:accessURL](http://www.w3.org/ns/dcat#accessURL)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Distribusjon](distribusjon.md) |
| Slot URI | [dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:accessURL |
| native | https://data.norge.no/ap-no/dcat-ap-no/tilgangs_url |




## LinkML Source

<details>
```yaml
name: tilgangs_url
description: URL for tilgang til distribusjonen.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dcat:accessURL
domain_of:
- Distribusjon
range: uri
multivalued: true

```
</details>