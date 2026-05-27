

# Slot: ressurstype 


_Type digital ressurs, t.d. dcat:Dataset, dcat:DataService eller ein URI frå eit kontrollert vokabular (FAIR F2)._

__





URI: [dct:type](http://purl.org/dc/terms/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FAIRMetadata](fairmetadata.md) | Maskin-aksjonerbar metadata som beskriver ein digital ressurs i tråd med FAIR... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [FAIRMetadata](fairmetadata.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fair/fair-metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:type |
| native | https://data.norge.no/fair#:ressurstype |




## LinkML Source

<details>
```yaml
name: ressurstype
description: 'Type digital ressurs, t.d. dcat:Dataset, dcat:DataService eller ein
  URI frå eit kontrollert vokabular (FAIR F2).

  '
from_schema: https://data.norge.no/fair/fair-metadata
rank: 1000
slot_uri: dct:type
domain_of:
- FAIRMetadata
range: uriorcurie

```
</details>