

# Slot: fravaerstype 


_Type fråvær._





URI: [adm:fravaerstype](https://schema.fintlabs.no/administrasjon/fravaerstype)
Alias: fravaerstype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravaerstype](fravaerstype.md) |
| Domain Of | [Fravaer](fravaer.md) |
| Slot URI | [adm:fravaerstype](https://schema.fintlabs.no/administrasjon/fravaerstype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fravaer](fravaer.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:fravaerstype |
| native | https://schema.fintlabs.no/administrasjon/:fravaerstype |




## LinkML Source

<details>
```yaml
name: fravaerstype
description: Type fråvær.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:fravaerstype
alias: fravaerstype
owner: Fravaer
domain_of:
- Fravaer
range: Fravaerstype
required: true

```
</details>