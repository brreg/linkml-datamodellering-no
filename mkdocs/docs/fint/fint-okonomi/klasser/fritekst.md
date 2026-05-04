

# Slot: fritekst 


_Fritekst som skildrar varen slik han er levert._





URI: [okn:fritekst](https://schema.fintlabs.no/okonomi/fritekst)
Alias: fritekst

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturalinje](Fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fakturalinje](Fakturalinje.md) |
| Slot URI | [okn:fritekst](https://schema.fintlabs.no/okonomi/fritekst) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fakturalinje](Fakturalinje.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:fritekst |
| native | https://schema.fintlabs.no/okonomi/:fritekst |




## LinkML Source

<details>
```yaml
name: fritekst
description: Fritekst som skildrar varen slik han er levert.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:fritekst
alias: fritekst
owner: Fakturalinje
domain_of:
- Fakturalinje
range: string
multivalued: true

```
</details>