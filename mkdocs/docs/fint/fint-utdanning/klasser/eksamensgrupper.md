

# Slot: eksamensgrupper 


_Alle eksamensgrupper i containeren._





URI: [utd:eksamensgrupper](https://schema.fintlabs.no/utdanning/eksamensgrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eksamensgruppe](eksamensgruppe.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:eksamensgrupper](https://schema.fintlabs.no/utdanning/eksamensgrupper) |

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
| self | utd:eksamensgrupper |
| native | https://schema.fintlabs.no/utdanning/:eksamensgrupper |




## LinkML Source

<details>
```yaml
name: eksamensgrupper
description: Alle eksamensgrupper i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:eksamensgrupper
domain_of:
- UtdanningContainer
range: Eksamensgruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>