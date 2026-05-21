

# Slot: skoleeijartypar 


_Alle skuleeigarstypar i containeren._





URI: [utd:skoleeijartypar](https://schema.fintlabs.no/utdanning/skoleeijartypar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleeiertype](skoleeiertype.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:skoleeijartypar](https://schema.fintlabs.no/utdanning/skoleeijartypar) |

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
| self | utd:skoleeijartypar |
| native | https://schema.fintlabs.no/utdanning/:skoleeijartypar |




## LinkML Source

<details>
```yaml
name: skoleeijartypar
description: Alle skuleeigarstypar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skoleeijartypar
domain_of:
- UtdanningContainer
range: Skoleeiertype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>