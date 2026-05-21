

# Slot: skolar 


_Alle skular i containeren._





URI: [utd:skolar](https://schema.fintlabs.no/utdanning/skolar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skole](skole.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:skolar](https://schema.fintlabs.no/utdanning/skolar) |

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
| self | utd:skolar |
| native | https://schema.fintlabs.no/utdanning/:skolar |




## LinkML Source

<details>
```yaml
name: skolar
description: Alle skular i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skolar
domain_of:
- UtdanningContainer
range: Skole
multivalued: true
inlined: true
inlined_as_list: true

```
</details>