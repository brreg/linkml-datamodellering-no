

# Slot: otUngdom 


_Alle OT-ungdom i containeren._





URI: [utd:otUngdom](https://schema.fintlabs.no/utdanning/otUngdom)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OtUngdom](otungdom.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:otUngdom](https://schema.fintlabs.no/utdanning/otUngdom) |

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
| self | utd:otUngdom |
| native | https://schema.fintlabs.no/utdanning/:otUngdom |




## LinkML Source

<details>
```yaml
name: otUngdom
description: Alle OT-ungdom i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:otUngdom
domain_of:
- UtdanningContainer
range: OtUngdom
multivalued: true
inlined: true
inlined_as_list: true

```
</details>