

# Slot: kontonummer 


_Kontonummer til leverandøren._





URI: [okn:kontonummer](https://schema.fintlabs.no/okonomi/kontonummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Leverandor](leverandor.md) |
| Slot URI | [okn:kontonummer](https://schema.fintlabs.no/okonomi/kontonummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:kontonummer |
| native | https://schema.fintlabs.no/okonomi/:kontonummer |




## LinkML Source

<details>
```yaml
name: kontonummer
description: Kontonummer til leverandøren.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:kontonummer
domain_of:
- Leverandor
range: string

```
</details>