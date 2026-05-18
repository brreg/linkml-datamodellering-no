

# Slot: pris 


_Pris per eining, i øre._





URI: [okn:pris](https://schema.fintlabs.no/okonomi/pris)
Alias: pris

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturalinje](fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  yes  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Fakturalinje](fakturalinje.md), [Vare](vare.md) |
| Slot URI | [okn:pris](https://schema.fintlabs.no/okonomi/pris) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:pris |
| native | https://schema.fintlabs.no/okonomi/:pris |




## LinkML Source

<details>
```yaml
name: pris
description: Pris per eining, i øre.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:pris
alias: pris
domain_of:
- Fakturalinje
- Vare
range: integer

```
</details>