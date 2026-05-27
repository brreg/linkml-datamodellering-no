

# Slot: undervisningstimer 


_Totalt antal undervisningstimar._





URI: [utd:undervisningstimer](https://schema.fintlabs.no/utdanning/undervisningstimer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravarsprosent](fravarsprosent.md) | Kompleks type som representerer fråværsprosent for ein periode |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Fravarsprosent](fravarsprosent.md) |
| Slot URI | [utd:undervisningstimer](https://schema.fintlabs.no/utdanning/undervisningstimer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:undervisningstimer |
| native | https://schema.fintlabs.no/utdanning/:undervisningstimer |




## LinkML Source

<details>
```yaml
name: undervisningstimer
description: Totalt antal undervisningstimar.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:undervisningstimer
domain_of:
- Fravarsprosent
range: integer

```
</details>