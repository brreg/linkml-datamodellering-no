

# Slot: stillingskode 


_Firesifra stillingskode frå KS, eventuelt utvida med to siffer._





URI: [adm:stillingskode](https://schema.fintlabs.no/administrasjon/stillingskode)
Alias: stillingskode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Stillingskode](stillingskode.md) |
| Domain Of | [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:stillingskode](https://schema.fintlabs.no/administrasjon/stillingskode) |

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
| self | adm:stillingskode |
| native | https://schema.fintlabs.no/administrasjon/:stillingskode |




## LinkML Source

<details>
```yaml
name: stillingskode
description: Firesifra stillingskode frå KS, eventuelt utvida med to siffer.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:stillingskode
alias: stillingskode
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: Stillingskode

```
</details>