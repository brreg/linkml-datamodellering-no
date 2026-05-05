

# Slot: fylke 


_Fylket kommunen høyrer til._





URI: [fint:fylke](https://schema.fintlabs.no/fylke)
Alias: fylke

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fylke](fylke.md) |
| Domain Of | [Kommune](kommune.md) |
| Slot URI | [fint:fylke](https://schema.fintlabs.no/fylke) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kommune](kommune.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:fylke |
| native | https://schema.fintlabs.no/arkiv/:fylke |




## LinkML Source

<details>
```yaml
name: fylke
description: Fylket kommunen høyrer til.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
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