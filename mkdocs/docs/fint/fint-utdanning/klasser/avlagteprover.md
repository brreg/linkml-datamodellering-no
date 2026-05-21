

# Slot: avlagteprover 


_Alle avlagde prøver i containeren._





URI: [utd:avlagteprover](https://schema.fintlabs.no/utdanning/avlagteprover)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AvlagtProve](avlagtprove.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:avlagteprover](https://schema.fintlabs.no/utdanning/avlagteprover) |

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
| self | utd:avlagteprover |
| native | https://schema.fintlabs.no/utdanning/:avlagteprover |




## LinkML Source

<details>
```yaml
name: avlagteprover
description: Alle avlagde prøver i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:avlagteprover
domain_of:
- UtdanningContainer
range: AvlagtProve
multivalued: true
inlined: true
inlined_as_list: true

```
</details>