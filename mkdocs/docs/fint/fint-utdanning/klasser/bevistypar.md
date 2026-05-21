

# Slot: bevistypar 


_Alle bevistypar i containeren._





URI: [utd:bevistypar](https://schema.fintlabs.no/utdanning/bevistypar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bevistype](bevistype.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:bevistypar](https://schema.fintlabs.no/utdanning/bevistypar) |

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
| self | utd:bevistypar |
| native | https://schema.fintlabs.no/utdanning/:bevistypar |




## LinkML Source

<details>
```yaml
name: bevistypar
description: Alle bevistypar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:bevistypar
domain_of:
- UtdanningContainer
range: Bevistype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>