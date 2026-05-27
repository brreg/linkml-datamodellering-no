

# Slot: totalbelop 


_Totalt beløp på faktura inkl. avgifter, i øre._





URI: [okn:totalbelop](https://schema.fintlabs.no/okonomi/totalbelop)
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
| Slot URI | [okn:totalbelop](https://schema.fintlabs.no/okonomi/totalbelop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:totalbelop |
| native | https://schema.fintlabs.no/okonomi/:totalbelop |




## LinkML Source

<details>
```yaml
name: totalbelop
description: Totalt beløp på faktura inkl. avgifter, i øre.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:totalbelop
domain_of:
- Fakturagrunnlag
range: integer

```
</details>