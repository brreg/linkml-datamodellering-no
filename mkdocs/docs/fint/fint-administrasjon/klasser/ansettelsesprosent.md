

# Slot: ansettelsesprosent 


_Prosenten personalressursen eig i høve til arbeidsavtalen._





URI: [adm:ansettelsesprosent](https://schema.fintlabs.no/administrasjon/ansettelsesprosent)
Alias: ansettelsesprosent

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
| Slot URI | [adm:ansettelsesprosent](https://schema.fintlabs.no/administrasjon/ansettelsesprosent) |

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
| self | adm:ansettelsesprosent |
| native | https://schema.fintlabs.no/administrasjon/:ansettelsesprosent |




## LinkML Source

<details>
```yaml
name: ansettelsesprosent
description: Prosenten personalressursen eig i høve til arbeidsavtalen.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:ansettelsesprosent
alias: ansettelsesprosent
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: integer
required: true

```
</details>