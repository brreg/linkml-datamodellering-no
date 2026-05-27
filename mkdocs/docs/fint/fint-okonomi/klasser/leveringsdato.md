

# Slot: leveringsdato 


_Dato varer eller tenester vart leverte._





URI: [okn:leveringsdato](https://schema.fintlabs.no/okonomi/leveringsdato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md) |
| Slot URI | [okn:leveringsdato](https://schema.fintlabs.no/okonomi/leveringsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:leveringsdato |
| native | https://schema.fintlabs.no/okonomi/:leveringsdato |




## LinkML Source

<details>
```yaml
name: leveringsdato
description: Dato varer eller tenester vart leverte.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:leveringsdato
domain_of:
- Fakturagrunnlag
range: date

```
</details>