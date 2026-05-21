

# Slot: kontaktlaerergrupper 


_Alle kontaktlærargrupper i containeren._





URI: [utd:kontaktlaerergrupper](https://schema.fintlabs.no/utdanning/kontaktlaerergrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktlaerergruppe](kontaktlaerergruppe.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:kontaktlaerergrupper](https://schema.fintlabs.no/utdanning/kontaktlaerergrupper) |

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
| self | utd:kontaktlaerergrupper |
| native | https://schema.fintlabs.no/utdanning/:kontaktlaerergrupper |




## LinkML Source

<details>
```yaml
name: kontaktlaerergrupper
description: Alle kontaktlærargrupper i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:kontaktlaerergrupper
domain_of:
- UtdanningContainer
range: Kontaktlaerergruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>