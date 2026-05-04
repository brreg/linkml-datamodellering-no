

# Slot: fullmektig 


_Personalressurs som har fått fullmakt til ei gjeven rolle._





URI: [adm:fullmektig](https://schema.fintlabs.no/administrasjon/fullmektig)
Alias: fullmektig

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fullmakt](Fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](Personalressurs.md) |
| Domain Of | [Fullmakt](Fullmakt.md) |
| Slot URI | [adm:fullmektig](https://schema.fintlabs.no/administrasjon/fullmektig) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fullmakt](Fullmakt.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:fullmektig |
| native | https://schema.fintlabs.no/administrasjon/:fullmektig |




## LinkML Source

<details>
```yaml
name: fullmektig
description: Personalressurs som har fått fullmakt til ei gjeven rolle.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:fullmektig
alias: fullmektig
owner: Fullmakt
domain_of:
- Fullmakt
range: Personalressurs

```
</details>