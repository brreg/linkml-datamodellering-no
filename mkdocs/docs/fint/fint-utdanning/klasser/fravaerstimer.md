

# Slot: fravaerstimer 


_Antal fråværstimar._





URI: [utd:fravaerstimer](https://schema.fintlabs.no/utdanning/fravaerstimer)
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
| Slot URI | [utd:fravaerstimer](https://schema.fintlabs.no/utdanning/fravaerstimer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:fravaerstimer |
| native | https://schema.fintlabs.no/utdanning/:fravaerstimer |




## LinkML Source

<details>
```yaml
name: fravaerstimer
description: Antal fråværstimar.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:fravaerstimer
domain_of:
- Fravarsprosent
range: integer

```
</details>