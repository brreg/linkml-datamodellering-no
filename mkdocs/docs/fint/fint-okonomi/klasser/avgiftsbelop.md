

# Slot: avgiftsbelop 


_Del av totalbeløp som er avgifter, i øre._





URI: [okn:avgiftsbelop](https://schema.fintlabs.no/okonomi/avgiftsbelop)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md) |
| Slot URI | [okn:avgiftsbelop](https://schema.fintlabs.no/okonomi/avgiftsbelop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:avgiftsbelop |
| native | https://schema.fintlabs.no/okonomi/:avgiftsbelop |




## LinkML Source

<details>
```yaml
name: avgiftsbelop
description: Del av totalbeløp som er avgifter, i øre.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:avgiftsbelop
domain_of:
- Fakturagrunnlag
range: integer

```
</details>