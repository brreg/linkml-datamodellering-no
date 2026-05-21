

# Slot: fullfortkoder 


_Alle fullfortkoder i containeren._





URI: [utd:fullfortkoder](https://schema.fintlabs.no/utdanning/fullfortkoder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fullfortkode](fullfortkode.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:fullfortkoder](https://schema.fintlabs.no/utdanning/fullfortkoder) |

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
| self | utd:fullfortkoder |
| native | https://schema.fintlabs.no/utdanning/:fullfortkoder |




## LinkML Source

<details>
```yaml
name: fullfortkoder
description: Alle fullfortkoder i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fullfortkoder
domain_of:
- UtdanningContainer
range: Fullfortkode
multivalued: true
inlined: true
inlined_as_list: true

```
</details>