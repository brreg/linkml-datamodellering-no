

# Slot: merverdiavgift 


_Varens avgiftsklasse og -sats._





URI: [okn:merverdiavgift](https://schema.fintlabs.no/okonomi/merverdiavgift)
Alias: merverdiavgift

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vare](Vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Merverdiavgift](Merverdiavgift.md) |
| Domain Of | [Vare](Vare.md) |
| Slot URI | [okn:merverdiavgift](https://schema.fintlabs.no/okonomi/merverdiavgift) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Vare](Vare.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:merverdiavgift |
| native | https://schema.fintlabs.no/okonomi/:merverdiavgift |




## LinkML Source

<details>
```yaml
name: merverdiavgift
description: Varens avgiftsklasse og -sats.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:merverdiavgift
alias: merverdiavgift
owner: Vare
domain_of:
- Vare
range: Merverdiavgift
required: true

```
</details>