

# Slot: hovedstilling 


_Angir kva arbeidsforhold som er hovudarbeidsforhold._





URI: [adm:hovedstilling](https://schema.fintlabs.no/administrasjon/hovedstilling)
Alias: hovedstilling

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Arbeidsforhold](Arbeidsforhold.md) |
| Slot URI | [adm:hovedstilling](https://schema.fintlabs.no/administrasjon/hovedstilling) |

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
| self | adm:hovedstilling |
| native | https://schema.fintlabs.no/administrasjon/:hovedstilling |




## LinkML Source

<details>
```yaml
name: hovedstilling
description: Angir kva arbeidsforhold som er hovudarbeidsforhold.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:hovedstilling
alias: hovedstilling
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: boolean
required: true

```
</details>