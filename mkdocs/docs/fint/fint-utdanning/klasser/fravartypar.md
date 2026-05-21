

# Slot: fravartypar 


_Alle fråværstypar i containeren._





URI: [utd:fravartypar](https://schema.fintlabs.no/utdanning/fravartypar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravartype](fravartype.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:fravartypar](https://schema.fintlabs.no/utdanning/fravartypar) |

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
| self | utd:fravartypar |
| native | https://schema.fintlabs.no/utdanning/:fravartypar |




## LinkML Source

<details>
```yaml
name: fravartypar
description: Alle fråværstypar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fravartypar
domain_of:
- UtdanningContainer
range: Fravartype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>