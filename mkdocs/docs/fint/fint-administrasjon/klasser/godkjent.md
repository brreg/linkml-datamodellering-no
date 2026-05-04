

# Slot: godkjent 


_Tidspunkt då fråværet vart godkjent._





URI: [adm:godkjent](https://schema.fintlabs.no/administrasjon/godkjent)
Alias: godkjent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravaer](Fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Fravaer](Fravaer.md) |
| Slot URI | [adm:godkjent](https://schema.fintlabs.no/administrasjon/godkjent) |

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
| self | adm:godkjent |
| native | https://schema.fintlabs.no/administrasjon/:godkjent |




## LinkML Source

<details>
```yaml
name: godkjent
description: Tidspunkt då fråværet vart godkjent.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:godkjent
alias: godkjent
owner: Fravaer
domain_of:
- Fravaer
range: datetime

```
</details>