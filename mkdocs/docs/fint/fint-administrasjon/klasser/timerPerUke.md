

# Slot: timerPerUke 


_Timer per veke i 100 % stilling._





URI: [adm:timerPerUke](https://schema.fintlabs.no/administrasjon/timerPerUke)
Alias: timerPerUke

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uketimetall](Uketimetall.md) |
| Domain Of | [Arbeidsforhold](Arbeidsforhold.md) |
| Slot URI | [adm:timerPerUke](https://schema.fintlabs.no/administrasjon/timerPerUke) |

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
| self | adm:timerPerUke |
| native | https://schema.fintlabs.no/administrasjon/:timerPerUke |




## LinkML Source

<details>
```yaml
name: timerPerUke
description: Timer per veke i 100 % stilling.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:timerPerUke
alias: timerPerUke
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: Uketimetall

```
</details>