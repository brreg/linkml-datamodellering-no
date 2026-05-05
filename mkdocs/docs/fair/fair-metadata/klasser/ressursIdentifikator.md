

# Slot: ressursIdentifikator 


_Global og persistent identifikator for ressursen (FAIR F1). Skal vere ein PID (t.d. DOI, Handle, eller stabil URI)._

__





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
Alias: ressursIdentifikator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FAIRMetadata](fairmetadata.md) | Maskin-aksjonerbar metadata som beskriver ein digital ressurs i tråd med FAIR... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [FAIRMetadata](fairmetadata.md) |
| Slot URI | [dct:identifier](http://purl.org/dc/terms/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fair-metadata




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
from_schema: https://data.norge.no/linkml/fair-metadata
rank: 1000
slot_uri: dct:identifier
alias: ressursIdentifikator
domain_of:
- FAIRMetadata
range: uriorcurie

```
</details>