

# Slot: timar 


_Alle timar i containeren._





URI: [utd:timar](https://schema.fintlabs.no/utdanning/timar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Time](time.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:timar](https://schema.fintlabs.no/utdanning/timar) |

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
| self | utd:timar |
| native | https://schema.fintlabs.no/utdanning/:timar |




## LinkML Source

<details>
```yaml
name: timar
description: Alle timar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:timar
domain_of:
- UtdanningContainer
range: Time
multivalued: true
inlined: true
inlined_as_list: true

```
</details>