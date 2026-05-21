

# Slot: avbruddsaarsaker 


_Alle avbruddsårsakar i containeren._





URI: [utd:avbruddsaarsaker](https://schema.fintlabs.no/utdanning/avbruddsaarsaker)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Avbruddsaarsak](avbruddsaarsak.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:avbruddsaarsaker](https://schema.fintlabs.no/utdanning/avbruddsaarsaker) |

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
| self | utd:avbruddsaarsaker |
| native | https://schema.fintlabs.no/utdanning/:avbruddsaarsaker |




## LinkML Source

<details>
```yaml
name: avbruddsaarsaker
description: Alle avbruddsårsakar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:avbruddsaarsaker
domain_of:
- UtdanningContainer
range: Avbruddsaarsak
multivalued: true
inlined: true
inlined_as_list: true

```
</details>