

# Slot: fakturamottaker 


_Mottakar som skal betale faktura._





URI: [okn:fakturamottaker](https://schema.fintlabs.no/okonomi/fakturamottaker)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fakturamottaker](fakturamottaker.md) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md) |
| Slot URI | [okn:fakturamottaker](https://schema.fintlabs.no/okonomi/fakturamottaker) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:fakturamottaker |
| native | https://schema.fintlabs.no/okonomi/:fakturamottaker |




## LinkML Source

<details>
```yaml
name: fakturamottaker
description: Mottakar som skal betale faktura.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:fakturamottaker
domain_of:
- Fakturagrunnlag
range: Fakturamottaker
inlined: true

```
</details>