

# Slot: laerlingar 


_Alle lærlingar i containeren._





URI: [utd:laerlingar](https://schema.fintlabs.no/utdanning/laerlingar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Laerling](laerling.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:laerlingar](https://schema.fintlabs.no/utdanning/laerlingar) |

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
| self | utd:laerlingar |
| native | https://schema.fintlabs.no/utdanning/:laerlingar |




## LinkML Source

<details>
```yaml
name: laerlingar
description: Alle lærlingar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:laerlingar
domain_of:
- UtdanningContainer
range: Laerling
multivalued: true
inlined: true
inlined_as_list: true

```
</details>