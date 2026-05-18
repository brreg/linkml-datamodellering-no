

# Slot: tilrettelegging 


_Tilretteleggingstype._





URI: [utd:tilrettelegging](https://schema.fintlabs.no/utdanning/tilrettelegging)
Alias: tilrettelegging

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Elevtilrettelegging](elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tilrettelegging](tilrettelegging.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Elevtilrettelegging](elevtilrettelegging.md), [Fag](fag.md) |
| Slot URI | [utd:tilrettelegging](https://schema.fintlabs.no/utdanning/tilrettelegging) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:tilrettelegging |
| native | https://schema.fintlabs.no/utdanning/:tilrettelegging |




## LinkML Source

<details>
```yaml
name: tilrettelegging
description: Tilretteleggingstype.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:tilrettelegging
alias: tilrettelegging
domain_of:
- UtdanningContainer
- Elevforhold
- Elevtilrettelegging
- Fag
range: Tilrettelegging

```
</details>