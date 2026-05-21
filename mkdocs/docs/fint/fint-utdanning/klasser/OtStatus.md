

# Slot: otStatus 


_Alle OT-statuser i containeren._





URI: [utd:otStatus](https://schema.fintlabs.no/utdanning/otStatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OtStatus](otstatus.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:otStatus](https://schema.fintlabs.no/utdanning/otStatus) |

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
| self | utd:otStatus |
| native | https://schema.fintlabs.no/utdanning/:otStatus |




## LinkML Source

<details>
```yaml
name: otStatus
description: Alle OT-statuser i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:otStatus
domain_of:
- UtdanningContainer
range: OtStatus
multivalued: true
inlined: true
inlined_as_list: true

```
</details>