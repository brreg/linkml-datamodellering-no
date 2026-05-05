

# Slot: nettobelop 


_Del av totalbeløp som utgjer summen av fakturalinjene, i øre (nettobeløp)._





URI: [okn:nettobelop](https://schema.fintlabs.no/okonomi/nettobelop)
Alias: nettobelop

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
| Slot URI | [okn:nettobelop](https://schema.fintlabs.no/okonomi/nettobelop) |

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
| self | okn:nettobelop |
| native | https://schema.fintlabs.no/okonomi/:nettobelop |




## LinkML Source

<details>
```yaml
name: nettobelop
description: Del av totalbeløp som utgjer summen av fakturalinjene, i øre (nettobeløp).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:nettobelop
alias: nettobelop
owner: Fakturagrunnlag
domain_of:
- Fakturagrunnlag
range: integer

```
</details>