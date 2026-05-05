

# Slot: lonnsprosent 


_Prosent av årslønn den tilsette skal ha utbetalt._





URI: [adm:lonnsprosent](https://schema.fintlabs.no/administrasjon/lonnsprosent)
Alias: lonnsprosent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:lonnsprosent](https://schema.fintlabs.no/administrasjon/lonnsprosent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Arbeidsforhold](arbeidsforhold.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:lonnsprosent |
| native | https://schema.fintlabs.no/administrasjon/:lonnsprosent |




## LinkML Source

<details>
```yaml
name: lonnsprosent
description: Prosent av årslønn den tilsette skal ha utbetalt.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:lonnsprosent
alias: lonnsprosent
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: integer
required: true

```
</details>