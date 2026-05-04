

# Slot: stillingsnummer 


_Løpenummer for stillinga._





URI: [adm:stillingsnummer](https://schema.fintlabs.no/administrasjon/stillingsnummer)
Alias: stillingsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Arbeidsforhold](Arbeidsforhold.md) |
| Slot URI | [adm:stillingsnummer](https://schema.fintlabs.no/administrasjon/stillingsnummer) |

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
| self | adm:stillingsnummer |
| native | https://schema.fintlabs.no/administrasjon/:stillingsnummer |




## LinkML Source

<details>
```yaml
name: stillingsnummer
description: Løpenummer for stillinga.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:stillingsnummer
alias: stillingsnummer
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: string
required: true

```
</details>