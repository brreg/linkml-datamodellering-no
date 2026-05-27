

# Slot: fritekst 


_Fritekst som skildrar varen slik han er levert._





URI: [okn:fritekst](https://schema.fintlabs.no/okonomi/fritekst)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturalinje](fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Fakturalinje](fakturalinje.md) |
| Slot URI | [okn:fritekst](https://schema.fintlabs.no/okonomi/fritekst) |

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
| self | okn:fritekst |
| native | https://schema.fintlabs.no/okonomi/:fritekst |




## LinkML Source

<details>
```yaml
name: fritekst
description: Fritekst som skildrar varen slik han er levert.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:fritekst
domain_of:
- Fakturalinje
range: string
multivalued: true

```
</details>