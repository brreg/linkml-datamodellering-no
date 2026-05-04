

# Slot: stillingstittel 


_Arbeidstakarens stillingstittel i gjeldande stilling._





URI: [adm:stillingstittel](https://schema.fintlabs.no/administrasjon/stillingstittel)
Alias: stillingstittel

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
| Slot URI | [adm:stillingstittel](https://schema.fintlabs.no/administrasjon/stillingstittel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Arbeidsforhold](Arbeidsforhold.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:stillingstittel |
| native | https://schema.fintlabs.no/administrasjon/:stillingstittel |




## LinkML Source

<details>
```yaml
name: stillingstittel
description: Arbeidstakarens stillingstittel i gjeldande stilling.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:stillingstittel
alias: stillingstittel
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: string

```
</details>