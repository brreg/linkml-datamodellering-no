

# Slot: avgiftsbelop 


_Del av totalbeløp som er avgifter, i øre (avgiftsbeløp)._





URI: [okn:avgiftsbelop](https://schema.fintlabs.no/okonomi/avgiftsbelop)
Alias: avgiftsbelop

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md) |
| Slot URI | [okn:avgiftsbelop](https://schema.fintlabs.no/okonomi/avgiftsbelop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fakturagrunnlag](fakturagrunnlag.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:avgiftsbelop |
| native | https://schema.fintlabs.no/okonomi/:avgiftsbelop |




## LinkML Source

<details>
```yaml
name: avgiftsbelop
description: Del av totalbeløp som er avgifter, i øre (avgiftsbeløp).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:avgiftsbelop
alias: avgiftsbelop
owner: Fakturagrunnlag
domain_of:
- Fakturagrunnlag
range: integer

```
</details>