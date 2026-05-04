

# Slot: totalbelop 


_Totalt beløp på faktura inkl. avgifter, i øre (totalbeløp)._





URI: [okn:totalbelop](https://schema.fintlabs.no/okonomi/totalbelop)
Alias: totalbelop

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](Fakturagrunnlag.md) | Grunnlag for fakturering |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Fakturagrunnlag](Fakturagrunnlag.md) |
| Slot URI | [okn:totalbelop](https://schema.fintlabs.no/okonomi/totalbelop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fakturagrunnlag](Fakturagrunnlag.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:totalbelop |
| native | https://schema.fintlabs.no/okonomi/:totalbelop |




## LinkML Source

<details>
```yaml
name: totalbelop
description: Totalt beløp på faktura inkl. avgifter, i øre (totalbeløp).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:totalbelop
alias: totalbelop
owner: Fakturagrunnlag
domain_of:
- Fakturagrunnlag
range: integer

```
</details>