

# Slot: antall 


_Mengd av varen levert._





URI: [okn:antall](https://schema.fintlabs.no/okonomi/antall)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturalinje](fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:float](http://www.w3.org/2001/XMLSchema#float) |
| Domain Of | [Fakturalinje](fakturalinje.md) |
| Slot URI | [okn:antall](https://schema.fintlabs.no/okonomi/antall) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




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
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:antall
domain_of:
- Fakturalinje
range: float

```
</details>