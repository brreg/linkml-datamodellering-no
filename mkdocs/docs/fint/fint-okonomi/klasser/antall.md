

# Slot: antall 


_Mengd av varen levert._





URI: [okn:antall](https://schema.fintlabs.no/okonomi/antall)
Alias: antall

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturalinje](fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](float.md) |
| Domain Of | [Fakturalinje](fakturalinje.md) |
| Slot URI | [okn:antall](https://schema.fintlabs.no/okonomi/antall) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fakturalinje](fakturalinje.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:antall |
| native | https://schema.fintlabs.no/okonomi/:antall |




## LinkML Source

<details>
```yaml
name: antall
description: Mengd av varen levert.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:antall
alias: antall
owner: Fakturalinje
domain_of:
- Fakturalinje
range: float
required: true

```
</details>