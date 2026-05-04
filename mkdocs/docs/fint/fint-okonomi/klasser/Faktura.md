

# Slot: faktura 


_Utferdigde fakturaer for fakturagrunnlaget._





URI: [okn:faktura](https://schema.fintlabs.no/okonomi/faktura)
Alias: faktura

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](Fakturagrunnlag.md) | Grunnlag for fakturering |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Faktura](Faktura.md) |
| Domain Of | [Fakturagrunnlag](Fakturagrunnlag.md) |
| Slot URI | [okn:faktura](https://schema.fintlabs.no/okonomi/faktura) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | okn:faktura |
| native | https://schema.fintlabs.no/okonomi/:faktura |




## LinkML Source

<details>
```yaml
name: faktura
description: Utferdigde fakturaer for fakturagrunnlaget.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:faktura
alias: faktura
owner: Fakturagrunnlag
domain_of:
- Fakturagrunnlag
range: Faktura
multivalued: true

```
</details>