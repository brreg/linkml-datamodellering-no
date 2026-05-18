

# Slot: fakturautsteder 


_Utstedar av faktura og mottakar av betaling._





URI: [okn:fakturautsteder](https://schema.fintlabs.no/okonomi/fakturautsteder)
Alias: fakturautsteder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  yes  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fakturautsteder](fakturautsteder.md) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md), [Vare](vare.md) |
| Slot URI | [okn:fakturautsteder](https://schema.fintlabs.no/okonomi/fakturautsteder) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:fakturautsteder |
| native | https://schema.fintlabs.no/okonomi/:fakturautsteder |




## LinkML Source

<details>
```yaml
name: fakturautsteder
description: Utstedar av faktura og mottakar av betaling.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:fakturautsteder
alias: fakturautsteder
domain_of:
- Fakturagrunnlag
- Vare
range: Fakturautsteder

```
</details>