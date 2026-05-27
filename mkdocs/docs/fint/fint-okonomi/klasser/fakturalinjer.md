

# Slot: fakturalinjer 


_Linjer av varer eller tenester som skal fakturerast._





URI: [okn:fakturalinjer](https://schema.fintlabs.no/okonomi/fakturalinjer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fakturalinje](fakturalinje.md) |
| Domain Of | [Fakturagrunnlag](fakturagrunnlag.md) |
| Slot URI | [okn:fakturalinjer](https://schema.fintlabs.no/okonomi/fakturalinjer) |

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
| self | okn:fakturalinjer |
| native | https://schema.fintlabs.no/okonomi/:fakturalinjer |




## LinkML Source

<details>
```yaml
name: fakturalinjer
description: Linjer av varer eller tenester som skal fakturerast.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:fakturalinjer
domain_of:
- Fakturagrunnlag
range: Fakturalinje
multivalued: true
inlined: true
inlined_as_list: true

```
</details>