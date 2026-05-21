

# Slot: terminar 


_Alle terminar i containeren._





URI: [utd:terminar](https://schema.fintlabs.no/utdanning/terminar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Termin](termin.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:terminar](https://schema.fintlabs.no/utdanning/terminar) |

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
| self | utd:terminar |
| native | https://schema.fintlabs.no/utdanning/:terminar |




## LinkML Source

<details>
```yaml
name: terminar
description: Alle terminar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:terminar
domain_of:
- UtdanningContainer
range: Termin
multivalued: true
inlined: true
inlined_as_list: true

```
</details>