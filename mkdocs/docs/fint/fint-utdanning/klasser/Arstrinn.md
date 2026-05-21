

# Slot: arstrinn 


_Alle årstrinns-objekt i containeren._





URI: [utd:arstrinn](https://schema.fintlabs.no/utdanning/arstrinn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arstrinn](arstrinn.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:arstrinn](https://schema.fintlabs.no/utdanning/arstrinn) |

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
| self | utd:arstrinn |
| native | https://schema.fintlabs.no/utdanning/:arstrinn |




## LinkML Source

<details>
```yaml
name: arstrinn
description: Alle årstrinns-objekt i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:arstrinn
domain_of:
- UtdanningContainer
range: Arstrinn
multivalued: true
inlined: true
inlined_as_list: true

```
</details>