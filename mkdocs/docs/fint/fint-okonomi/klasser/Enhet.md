

# Slot: enhet 


_Namn på mengdeeininga varen leverast i._





URI: [okn:enhet](https://schema.fintlabs.no/okonomi/enhet)
Alias: enhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Vare](vare.md) |
| Slot URI | [okn:enhet](https://schema.fintlabs.no/okonomi/enhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Vare](vare.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:enhet |
| native | https://schema.fintlabs.no/okonomi/:enhet |




## LinkML Source

<details>
```yaml
name: enhet
description: Namn på mengdeeininga varen leverast i.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:enhet
alias: enhet
owner: Vare
domain_of:
- Vare
range: string
required: true

```
</details>