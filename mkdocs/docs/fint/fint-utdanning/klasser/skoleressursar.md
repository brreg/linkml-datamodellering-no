

# Slot: skoleressursar 


_Alle skoleressursar i containeren._





URI: [utd:skoleressursar](https://schema.fintlabs.no/utdanning/skoleressursar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleressurs](skoleressurs.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:skoleressursar](https://schema.fintlabs.no/utdanning/skoleressursar) |

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
| self | utd:skoleressursar |
| native | https://schema.fintlabs.no/utdanning/:skoleressursar |




## LinkML Source

<details>
```yaml
name: skoleressursar
description: Alle skoleressursar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skoleressursar
domain_of:
- UtdanningContainer
range: Skoleressurs
multivalued: true
inlined: true
inlined_as_list: true

```
</details>