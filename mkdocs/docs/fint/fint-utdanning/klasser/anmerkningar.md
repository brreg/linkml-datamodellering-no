

# Slot: anmerkningar 


_Alle anmerkningar i containeren._





URI: [utd:anmerkningar](https://schema.fintlabs.no/utdanning/anmerkningar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Anmerkninger](anmerkninger.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:anmerkningar](https://schema.fintlabs.no/utdanning/anmerkningar) |

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
| self | utd:anmerkningar |
| native | https://schema.fintlabs.no/utdanning/:anmerkningar |




## LinkML Source

<details>
```yaml
name: anmerkningar
description: Alle anmerkningar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:anmerkningar
domain_of:
- UtdanningContainer
range: Anmerkninger
multivalued: true
inlined: true
inlined_as_list: true

```
</details>