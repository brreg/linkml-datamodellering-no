

# Slot: arbeidslokasjon 


_Fysisk lokasjon der den tilsette har sitt arbeidsstad._





URI: [adm:arbeidslokasjon](https://schema.fintlabs.no/administrasjon/arbeidslokasjon)
Alias: arbeidslokasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arbeidslokasjon](Arbeidslokasjon.md) |
| Domain Of | [Arbeidsforhold](Arbeidsforhold.md) |
| Slot URI | [adm:arbeidslokasjon](https://schema.fintlabs.no/administrasjon/arbeidslokasjon) |

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
| self | adm:arbeidslokasjon |
| native | https://schema.fintlabs.no/administrasjon/:arbeidslokasjon |




## LinkML Source

<details>
```yaml
name: arbeidslokasjon
description: Fysisk lokasjon der den tilsette har sitt arbeidsstad.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:arbeidslokasjon
alias: arbeidslokasjon
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: Arbeidslokasjon

```
</details>