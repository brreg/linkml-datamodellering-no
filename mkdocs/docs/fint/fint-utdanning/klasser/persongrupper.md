

# Slot: persongrupper 


_Alle persongrupper i containeren._





URI: [utd:persongrupper](https://schema.fintlabs.no/utdanning/persongrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Persongruppe](persongruppe.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:persongrupper](https://schema.fintlabs.no/utdanning/persongrupper) |

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
| self | utd:persongrupper |
| native | https://schema.fintlabs.no/utdanning/:persongrupper |




## LinkML Source

<details>
```yaml
name: persongrupper
description: Alle persongrupper i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:persongrupper
domain_of:
- UtdanningContainer
range: Persongruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>