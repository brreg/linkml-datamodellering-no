

# Slot: arbeidsforholdstype 


_Beskriven kode som kategoriserer kva funksjon stillinga er gruppert til._





URI: [adm:arbeidsforholdstype](https://schema.fintlabs.no/administrasjon/arbeidsforholdstype)
Alias: arbeidsforholdstype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arbeidsforholdstype](arbeidsforholdstype.md) |
| Domain Of | [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:arbeidsforholdstype](https://schema.fintlabs.no/administrasjon/arbeidsforholdstype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Arbeidsforhold](arbeidsforhold.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:arbeidsforholdstype |
| native | https://schema.fintlabs.no/administrasjon/:arbeidsforholdstype |




## LinkML Source

<details>
```yaml
name: arbeidsforholdstype
description: Beskriven kode som kategoriserer kva funksjon stillinga er gruppert til.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:arbeidsforholdstype
alias: arbeidsforholdstype
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: Arbeidsforholdstype

```
</details>