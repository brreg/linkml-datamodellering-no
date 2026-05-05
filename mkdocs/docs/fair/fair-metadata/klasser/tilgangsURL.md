

# Slot: tilgangsURL 


_URL for maskinell tilgang til ressurs eller metadata (FAIR A1)._





URI: [dcat:accessURL](http://www.w3.org/ns/dcat#accessURL)
Alias: tilgangsURL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tilgangsmetadata](tilgangsmetadata.md) | Metadata for tilgang, autentisering og tilgjengelegheit (FAIR A1/A2) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Tilgangsmetadata](tilgangsmetadata.md) |
| Slot URI | [dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fair-metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:accessURL |
| native | https://data.norge.no/fair#:tilgangsURL |




## LinkML Source

<details>
```yaml
name: tilgangsURL
description: URL for maskinell tilgang til ressurs eller metadata (FAIR A1).
from_schema: https://data.norge.no/linkml/fair-metadata
rank: 1000
slot_uri: dcat:accessURL
alias: tilgangsURL
domain_of:
- Tilgangsmetadata
range: uriorcurie

```
</details>