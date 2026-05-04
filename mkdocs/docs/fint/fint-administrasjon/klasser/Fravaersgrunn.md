

# Slot: fravaersgrunn 


_Grunn til fråværet._





URI: [adm:fravaersgrunn](https://schema.fintlabs.no/administrasjon/fravaersgrunn)
Alias: fravaersgrunn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravaer](Fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravaersgrunn](Fravaersgrunn.md) |
| Domain Of | [Fravaer](Fravaer.md) |
| Slot URI | [adm:fravaersgrunn](https://schema.fintlabs.no/administrasjon/fravaersgrunn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fravaer](Fravaer.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:fravaersgrunn |
| native | https://schema.fintlabs.no/administrasjon/:fravaersgrunn |




## LinkML Source

<details>
```yaml
name: fravaersgrunn
description: Grunn til fråværet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:fravaersgrunn
alias: fravaersgrunn
owner: Fravaer
domain_of:
- Fravaer
range: Fravaersgrunn

```
</details>