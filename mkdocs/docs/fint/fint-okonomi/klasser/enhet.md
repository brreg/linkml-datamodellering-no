

# Slot: enhet 


_Namn på mengdeeininga varen leverast i._





URI: [okn:enhet](https://schema.fintlabs.no/okonomi/enhet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Vare](vare.md) |
| Slot URI | [okn:enhet](https://schema.fintlabs.no/okonomi/enhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




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
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:enhet
domain_of:
- Vare
range: string

```
</details>