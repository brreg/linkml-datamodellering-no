

# Slot: leveringsdato 


_Dato varer eller tenester vart leverte._





URI: [okn:leveringsdato](https://schema.fintlabs.no/okonomi/leveringsdato)
Alias: leveringsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](Fakturagrunnlag.md) | Grunnlag for fakturering |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Fakturagrunnlag](Fakturagrunnlag.md) |
| Slot URI | [okn:leveringsdato](https://schema.fintlabs.no/okonomi/leveringsdato) |

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
| self | okn:leveringsdato |
| native | https://schema.fintlabs.no/okonomi/:leveringsdato |




## LinkML Source

<details>
```yaml
name: leveringsdato
description: Dato varer eller tenester vart leverte.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:leveringsdato
alias: leveringsdato
owner: Fakturagrunnlag
domain_of:
- Fakturagrunnlag
range: date

```
</details>