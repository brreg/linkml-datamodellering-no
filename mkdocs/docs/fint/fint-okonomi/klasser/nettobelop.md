

# Slot: nettobelop 


_Del av totalbeløp som utgjer summen av fakturalinjene, i øre._





URI: [okn:nettobelop](https://schema.fintlabs.no/okonomi/nettobelop)
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
| Slot URI | [okn:nettobelop](https://schema.fintlabs.no/okonomi/nettobelop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:nettobelop |
| native | https://schema.fintlabs.no/okonomi/:nettobelop |




## LinkML Source

<details>
```yaml
name: nettobelop
description: Del av totalbeløp som utgjer summen av fakturalinjene, i øre.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:nettobelop
domain_of:
- Fakturagrunnlag
range: integer

```
</details>