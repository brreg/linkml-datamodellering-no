

# Slot: karakterskalaer 


_Alle karakterskalaer i containeren._





URI: [utd:karakterskalaer](https://schema.fintlabs.no/utdanning/karakterskalaer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterskala](karakterskala.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:karakterskalaer](https://schema.fintlabs.no/utdanning/karakterskalaer) |

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
| self | utd:karakterskalaer |
| native | https://schema.fintlabs.no/utdanning/:karakterskalaer |




## LinkML Source

<details>
```yaml
name: karakterskalaer
description: Alle karakterskalaer i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:karakterskalaer
domain_of:
- UtdanningContainer
range: Karakterskala
multivalued: true
inlined: true
inlined_as_list: true

```
</details>