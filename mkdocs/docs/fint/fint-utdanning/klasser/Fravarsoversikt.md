

# Slot: fravarsoversikt 


_Alle fråværsoversikter i containeren._





URI: [utd:fravarsoversikt](https://schema.fintlabs.no/utdanning/fravarsoversikt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravarsoversikt](fravarsoversikt.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:fravarsoversikt](https://schema.fintlabs.no/utdanning/fravarsoversikt) |

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
| self | utd:fravarsoversikt |
| native | https://schema.fintlabs.no/utdanning/:fravarsoversikt |




## LinkML Source

<details>
```yaml
name: fravarsoversikt
description: Alle fråværsoversikter i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fravarsoversikt
domain_of:
- UtdanningContainer
range: Fravarsoversikt
multivalued: true
inlined: true
inlined_as_list: true

```
</details>