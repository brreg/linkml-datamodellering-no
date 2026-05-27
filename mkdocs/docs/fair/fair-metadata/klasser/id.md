

# Slot: id 


_Persistent URI-identifikator for metadata-posten (FAIR F1)._





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FAIRMetadata](fairmetadata.md) | Maskin-aksjonerbar metadata som beskriver ein digital ressurs i tråd med FAIR... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [FAIRMetadata](fairmetadata.md) |
| Slot URI | [dct:identifier](http://purl.org/dc/terms/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fair/fair-metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:identifier |
| native | https://data.norge.no/fair#:id |




## LinkML Source

<details>
```yaml
name: id
description: Persistent URI-identifikator for metadata-posten (FAIR F1).
from_schema: https://data.norge.no/fair/fair-metadata
rank: 1000
slot_uri: dct:identifier
identifier: true
domain_of:
- FAIRMetadata
range: uriorcurie
required: true

```
</details>