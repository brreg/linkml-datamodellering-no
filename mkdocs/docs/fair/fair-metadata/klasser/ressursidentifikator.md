

# Slot: ressursIdentifikator 


_Global og persistent identifikator for ressursen (FAIR F1). Skal vere ein PID (t.d. DOI, Handle, eller stabil URI)._

__





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
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
| Slot URI | [dct:identifier](http://purl.org/dc/terms/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fair/fair-metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:identifier |
| native | https://data.norge.no/fair#:ressursIdentifikator |




## LinkML Source

<details>
```yaml
name: ressursIdentifikator
description: 'Global og persistent identifikator for ressursen (FAIR F1). Skal vere
  ein PID (t.d. DOI, Handle, eller stabil URI).

  '
from_schema: https://data.norge.no/fair/fair-metadata
rank: 1000
slot_uri: dct:identifier
domain_of:
- FAIRMetadata
range: uriorcurie

```
</details>