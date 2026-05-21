

# Slot: undervisningsgrupper 


_Alle undervisningsgrupper i containeren._





URI: [utd:undervisningsgrupper](https://schema.fintlabs.no/utdanning/undervisningsgrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Undervisningsgruppe](undervisningsgruppe.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:undervisningsgrupper](https://schema.fintlabs.no/utdanning/undervisningsgrupper) |

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
| self | utd:undervisningsgrupper |
| native | https://schema.fintlabs.no/utdanning/:undervisningsgrupper |




## LinkML Source

<details>
```yaml
name: undervisningsgrupper
description: Alle undervisningsgrupper i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:undervisningsgrupper
domain_of:
- UtdanningContainer
range: Undervisningsgruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>