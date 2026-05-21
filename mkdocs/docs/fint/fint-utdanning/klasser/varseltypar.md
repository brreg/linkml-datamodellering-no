

# Slot: varseltypar 


_Alle varseltypar i containeren._





URI: [utd:varseltypar](https://schema.fintlabs.no/utdanning/varseltypar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Varseltype](varseltype.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:varseltypar](https://schema.fintlabs.no/utdanning/varseltypar) |

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
| self | utd:varseltypar |
| native | https://schema.fintlabs.no/utdanning/:varseltypar |




## LinkML Source

<details>
```yaml
name: varseltypar
description: Alle varseltypar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:varseltypar
domain_of:
- UtdanningContainer
range: Varseltype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>