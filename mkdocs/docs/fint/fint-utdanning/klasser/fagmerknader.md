

# Slot: fagmerknader 


_Alle fagmerknadar i containeren._





URI: [utd:fagmerknader](https://schema.fintlabs.no/utdanning/fagmerknader)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fagmerknad](fagmerknad.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:fagmerknader](https://schema.fintlabs.no/utdanning/fagmerknader) |

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
| self | utd:fagmerknader |
| native | https://schema.fintlabs.no/utdanning/:fagmerknader |




## LinkML Source

<details>
```yaml
name: fagmerknader
description: Alle fagmerknadar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fagmerknader
domain_of:
- UtdanningContainer
range: Fagmerknad
multivalued: true
inlined: true
inlined_as_list: true

```
</details>