

# Slot: klasser 


_Alle klassar i containeren._





URI: [utd:klasser](https://schema.fintlabs.no/utdanning/klasser)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Klasse](klasse.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:klasser](https://schema.fintlabs.no/utdanning/klasser) |

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
| self | utd:klasser |
| native | https://schema.fintlabs.no/utdanning/:klasser |




## LinkML Source

<details>
```yaml
name: klasser
description: Alle klassar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:klasser
domain_of:
- UtdanningContainer
range: Klasse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>