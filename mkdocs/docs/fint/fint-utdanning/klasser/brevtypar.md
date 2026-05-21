

# Slot: brevtypar 


_Alle brevtypar i containeren._





URI: [utd:brevtypar](https://schema.fintlabs.no/utdanning/brevtypar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Brevtype](brevtype.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:brevtypar](https://schema.fintlabs.no/utdanning/brevtypar) |

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
| self | utd:brevtypar |
| native | https://schema.fintlabs.no/utdanning/:brevtypar |




## LinkML Source

<details>
```yaml
name: brevtypar
description: Alle brevtypar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:brevtypar
domain_of:
- UtdanningContainer
range: Brevtype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>