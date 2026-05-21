

# Slot: provestatuser 


_Alle prøvestatuser i containeren._





URI: [utd:provestatuser](https://schema.fintlabs.no/utdanning/provestatuser)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Provestatus](provestatus.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:provestatuser](https://schema.fintlabs.no/utdanning/provestatuser) |

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
| self | utd:provestatuser |
| native | https://schema.fintlabs.no/utdanning/:provestatuser |




## LinkML Source

<details>
```yaml
name: provestatuser
description: Alle prøvestatuser i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:provestatuser
domain_of:
- UtdanningContainer
range: Provestatus
multivalued: true
inlined: true
inlined_as_list: true

```
</details>