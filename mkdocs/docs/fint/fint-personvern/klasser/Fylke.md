

# Slot: fylke 


_Fylket kommunen høyrer til._





URI: [fint:fylke](https://schema.fintlabs.no/fylke)
Alias: fylke

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fylke](Fylke.md) |
| Domain Of | [Kommune](Kommune.md) |
| Slot URI | [fint:fylke](https://schema.fintlabs.no/fylke) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kommune](Kommune.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:fylke |
| native | https://schema.fintlabs.no/personvern/:fylke |




## LinkML Source

<details>
```yaml
name: fylke
description: Fylket kommunen høyrer til.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:fylke
alias: fylke
owner: Kommune
domain_of:
- Kommune
range: Fylke
required: true

```
</details>