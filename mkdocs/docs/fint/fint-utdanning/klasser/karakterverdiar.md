

# Slot: karakterverdiar 


_Alle karakterverdiar i containeren._





URI: [utd:karakterverdiar](https://schema.fintlabs.no/utdanning/karakterverdiar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterverdi](karakterverdi.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:karakterverdiar](https://schema.fintlabs.no/utdanning/karakterverdiar) |

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
| self | utd:karakterverdiar |
| native | https://schema.fintlabs.no/utdanning/:karakterverdiar |




## LinkML Source

<details>
```yaml
name: karakterverdiar
description: Alle karakterverdiar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:karakterverdiar
domain_of:
- UtdanningContainer
range: Karakterverdi
multivalued: true
inlined: true
inlined_as_list: true

```
</details>