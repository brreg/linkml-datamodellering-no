

# Slot: endringsdato 


_Sist endra dato (FAIR R1.2)._





URI: [dct:modified](http://purl.org/dc/terms/modified)
Alias: endringsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Proveniensmetadata](Proveniensmetadata.md) | Metadata om opphav og endringshistorie (FAIR R1 |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Proveniensmetadata](Proveniensmetadata.md) |
| Slot URI | [dct:modified](http://purl.org/dc/terms/modified) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fair-metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:modified |
| native | https://data.norge.no/fair#:endringsdato |




## LinkML Source

<details>
```yaml
name: endringsdato
description: Sist endra dato (FAIR R1.2).
from_schema: https://data.norge.no/linkml/fair-metadata
rank: 1000
slot_uri: dct:modified
alias: endringsdato
domain_of:
- Proveniensmetadata
range: date

```
</details>