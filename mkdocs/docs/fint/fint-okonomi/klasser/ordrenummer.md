

# Slot: ordrenummer 


_Unik identifikator for ordren det skal utferdigast faktura på._





URI: [okn:ordrenummer](https://schema.fintlabs.no/okonomi/ordrenummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




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
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:ordrenummer
domain_of:
- Fakturagrunnlag
range: Identifikator
inlined: true

```
</details>