

# Slot: elevtilrettelegging 


_Alle elevtilretteleggingar i containeren._





URI: [utd:elevtilrettelegging](https://schema.fintlabs.no/utdanning/elevtilrettelegging)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevtilrettelegging](elevtilrettelegging.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:elevtilrettelegging](https://schema.fintlabs.no/utdanning/elevtilrettelegging) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:elevtilrettelegging |
| native | https://schema.fintlabs.no/utdanning/:elevtilrettelegging |




## LinkML Source

<details>
```yaml
name: elevtilrettelegging
description: Alle elevtilretteleggingar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:elevtilrettelegging
domain_of:
- UtdanningContainer
range: Elevtilrettelegging
multivalued: true
inlined: true
inlined_as_list: true

```
</details>