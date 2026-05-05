

# Slot: tilstedeprosent 


_Det personalressursen faktisk jobbar._





URI: [adm:tilstedeprosent](https://schema.fintlabs.no/administrasjon/tilstedeprosent)
Alias: tilstedeprosent

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
| Slot URI | [adm:tilstedeprosent](https://schema.fintlabs.no/administrasjon/tilstedeprosent) |

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
| self | adm:tilstedeprosent |
| native | https://schema.fintlabs.no/administrasjon/:tilstedeprosent |




## LinkML Source

<details>
```yaml
name: tilstedeprosent
description: Det personalressursen faktisk jobbar.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:tilstedeprosent
alias: tilstedeprosent
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: integer
required: true

```
</details>