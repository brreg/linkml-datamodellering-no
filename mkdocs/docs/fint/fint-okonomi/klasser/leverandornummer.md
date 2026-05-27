

# Slot: leverandornummer 


_Nummer som identifiserer ein leverandør._





URI: [okn:leverandornummer](https://schema.fintlabs.no/okonomi/leverandornummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Leverandor](leverandor.md) |
| Slot URI | [okn:leverandornummer](https://schema.fintlabs.no/okonomi/leverandornummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:leverandornummer |
| native | https://schema.fintlabs.no/okonomi/:leverandornummer |




## LinkML Source

<details>
```yaml
name: leverandornummer
description: Nummer som identifiserer ein leverandør.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:leverandornummer
domain_of:
- Leverandor
range: Identifikator
inlined: true

```
</details>