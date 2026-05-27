

# Slot: faktura 


_Utferdigde fakturaer for fakturagrunnlaget._





URI: [okn:faktura](https://schema.fintlabs.no/okonomi/faktura)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Faktura](faktura.md) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md) |
| Slot URI | [okn:faktura](https://schema.fintlabs.no/okonomi/faktura) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




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
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:faktura
domain_of:
- Fakturagrunnlag
range: Faktura
multivalued: true

```
</details>