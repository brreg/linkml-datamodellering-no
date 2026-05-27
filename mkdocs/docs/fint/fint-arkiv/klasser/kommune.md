

# Slot: kommune 


_Kommune._





URI: [fint:kommune](https://schema.fintlabs.no/kommune)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fylke](fylke.md) | Liste over Norges fylker |  yes  |
| [Person](person.md) | Fysiske private personar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](kommune.md) |
| Domain Of | [Fylke](fylke.md), [Person](person.md) |
| Slot URI | [fint:kommune](https://schema.fintlabs.no/kommune) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kommune |
| native | https://schema.fintlabs.no/:kommune |




## LinkML Source

<details>
```yaml
name: kommune
description: Kommune.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:kommune
domain_of:
- Fylke
- Person
range: Kommune

```
</details>