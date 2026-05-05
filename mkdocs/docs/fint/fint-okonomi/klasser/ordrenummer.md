

# Slot: ordrenummer 


_Unik identifikator for ordren det skal utferdigast faktura på._





URI: [okn:ordrenummer](https://schema.fintlabs.no/okonomi/ordrenummer)
Alias: ordrenummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md) |
| Slot URI | [okn:ordrenummer](https://schema.fintlabs.no/okonomi/ordrenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fakturagrunnlag](fakturagrunnlag.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:ordrenummer |
| native | https://schema.fintlabs.no/okonomi/:ordrenummer |




## LinkML Source

<details>
```yaml
name: ordrenummer
description: Unik identifikator for ordren det skal utferdigast faktura på.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:ordrenummer
alias: ordrenummer
owner: Fakturagrunnlag
domain_of:
- Fakturagrunnlag
range: Identifikator
required: true
inlined: true

```
</details>