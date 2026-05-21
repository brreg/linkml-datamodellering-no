

# Slot: elevkategoriar 


_Alle elevkategoriar i containeren._





URI: [utd:elevkategoriar](https://schema.fintlabs.no/utdanning/elevkategoriar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevkategori](elevkategori.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:elevkategoriar](https://schema.fintlabs.no/utdanning/elevkategoriar) |

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
| self | utd:elevkategoriar |
| native | https://schema.fintlabs.no/utdanning/:elevkategoriar |




## LinkML Source

<details>
```yaml
name: elevkategoriar
description: Alle elevkategoriar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:elevkategoriar
domain_of:
- UtdanningContainer
range: Elevkategori
multivalued: true
inlined: true
inlined_as_list: true

```
</details>