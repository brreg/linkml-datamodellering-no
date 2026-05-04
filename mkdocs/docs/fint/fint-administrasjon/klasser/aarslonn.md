

# Slot: aarslonn 


_Årslønn/grunnlønn i 100 % stilling._





URI: [adm:aarslonn](https://schema.fintlabs.no/administrasjon/aarslonn)
Alias: aarslonn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Arbeidsforhold](Arbeidsforhold.md) |
| Slot URI | [adm:aarslonn](https://schema.fintlabs.no/administrasjon/aarslonn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Arbeidsforhold](Arbeidsforhold.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:aarslonn |
| native | https://schema.fintlabs.no/administrasjon/:aarslonn |




## LinkML Source

<details>
```yaml
name: aarslonn
description: Årslønn/grunnlønn i 100 % stilling.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:aarslonn
alias: aarslonn
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: integer
required: true

```
</details>