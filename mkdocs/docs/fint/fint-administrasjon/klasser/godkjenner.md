

# Slot: godkjenner 


_Personalressurs som har godkjent fråværsmeldinga._





URI: [adm:godkjenner](https://schema.fintlabs.no/administrasjon/godkjenner)
Alias: godkjenner

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravaer](Fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](Personalressurs.md) |
| Domain Of | [Fravaer](Fravaer.md) |
| Slot URI | [adm:godkjenner](https://schema.fintlabs.no/administrasjon/godkjenner) |

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
| self | adm:godkjenner |
| native | https://schema.fintlabs.no/administrasjon/:godkjenner |




## LinkML Source

<details>
```yaml
name: godkjenner
description: Personalressurs som har godkjent fråværsmeldinga.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:godkjenner
alias: godkjenner
owner: Fravaer
domain_of:
- Fravaer
range: Personalressurs

```
</details>