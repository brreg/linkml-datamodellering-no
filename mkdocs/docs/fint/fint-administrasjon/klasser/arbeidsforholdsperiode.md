

# Slot: arbeidsforholdsperiode 


_Periode for ei gjeven stilling._





URI: [adm:arbeidsforholdsperiode](https://schema.fintlabs.no/administrasjon/arbeidsforholdsperiode)
Alias: arbeidsforholdsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](Periode.md) |
| Domain Of | [Arbeidsforhold](Arbeidsforhold.md) |
| Slot URI | [adm:arbeidsforholdsperiode](https://schema.fintlabs.no/administrasjon/arbeidsforholdsperiode) |

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
| self | adm:arbeidsforholdsperiode |
| native | https://schema.fintlabs.no/administrasjon/:arbeidsforholdsperiode |




## LinkML Source

<details>
```yaml
name: arbeidsforholdsperiode
description: Periode for ei gjeven stilling.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:arbeidsforholdsperiode
alias: arbeidsforholdsperiode
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: Periode
inlined: true

```
</details>