

# Slot: faggrupper 


_Alle faggrupper i containeren._





URI: [utd:faggrupper](https://schema.fintlabs.no/utdanning/faggrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Faggruppe](faggruppe.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:faggrupper](https://schema.fintlabs.no/utdanning/faggrupper) |

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
| self | utd:faggrupper |
| native | https://schema.fintlabs.no/utdanning/:faggrupper |




## LinkML Source

<details>
```yaml
name: faggrupper
description: Alle faggrupper i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:faggrupper
domain_of:
- UtdanningContainer
range: Faggruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>