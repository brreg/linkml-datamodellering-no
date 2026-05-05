

# Slot: rolle 


_Kva type fullmakt._





URI: [adm:rolle](https://schema.fintlabs.no/administrasjon/rolle)
Alias: rolle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rolle](rolle.md) |
| Domain Of | [Fullmakt](fullmakt.md) |
| Slot URI | [adm:rolle](https://schema.fintlabs.no/administrasjon/rolle) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fullmakt](fullmakt.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:rolle |
| native | https://schema.fintlabs.no/administrasjon/:rolle |




## LinkML Source

<details>
```yaml
name: rolle
description: Kva type fullmakt.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:rolle
alias: rolle
owner: Fullmakt
domain_of:
- Fullmakt
range: Rolle
required: true

```
</details>