

# Slot: fakturalinjer 


_Linjer av varer eller tenester som skal fakturerast._





URI: [okn:fakturalinjer](https://schema.fintlabs.no/okonomi/fakturalinjer)
Alias: fakturalinjer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturagrunnlag](Fakturagrunnlag.md) | Grunnlag for fakturering |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fakturalinje](Fakturalinje.md) |
| Domain Of | [Fakturagrunnlag](Fakturagrunnlag.md) |
| Slot URI | [okn:fakturalinjer](https://schema.fintlabs.no/okonomi/fakturalinjer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fakturagrunnlag](Fakturagrunnlag.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




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
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:fakturalinjer
alias: fakturalinjer
owner: Fakturagrunnlag
domain_of:
- Fakturagrunnlag
range: Fakturalinje
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>