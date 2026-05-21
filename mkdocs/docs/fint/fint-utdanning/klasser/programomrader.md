

# Slot: programomrader 


_Alle programområde i containeren._





URI: [utd:programomrader](https://schema.fintlabs.no/utdanning/programomrader)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Programomrade](programomrade.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:programomrader](https://schema.fintlabs.no/utdanning/programomrader) |

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
| self | utd:programomrader |
| native | https://schema.fintlabs.no/utdanning/:programomrader |




## LinkML Source

<details>
```yaml
name: programomrader
description: Alle programområde i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:programomrader
domain_of:
- UtdanningContainer
range: Programomrade
multivalued: true
inlined: true
inlined_as_list: true

```
</details>