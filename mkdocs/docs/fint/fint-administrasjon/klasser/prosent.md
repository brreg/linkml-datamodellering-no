

# Slot: prosent 


_Prosent._





URI: [adm:prosent](https://schema.fintlabs.no/administrasjon/prosent)
Alias: prosent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  yes  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Fastlonn](fastlonn.md), [Fravaer](fravaer.md) |
| Slot URI | [adm:prosent](https://schema.fintlabs.no/administrasjon/prosent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:prosent |
| native | https://schema.fintlabs.no/administrasjon/:prosent |




## LinkML Source

<details>
```yaml
name: prosent
description: Prosent.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:prosent
alias: prosent
domain_of:
- Fastlonn
- Fravaer
range: integer

```
</details>