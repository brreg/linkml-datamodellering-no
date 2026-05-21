

# Slot: elevar 


_Alle elevar i containeren._





URI: [utd:elevar](https://schema.fintlabs.no/utdanning/elevar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elev](elev.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:elevar](https://schema.fintlabs.no/utdanning/elevar) |

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
| self | utd:elevar |
| native | https://schema.fintlabs.no/utdanning/:elevar |




## LinkML Source

<details>
```yaml
name: elevar
description: Alle elevar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:elevar
domain_of:
- UtdanningContainer
range: Elev
multivalued: true
inlined: true
inlined_as_list: true

```
</details>