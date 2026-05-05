

# Slot: personalleder 


_Personalleiar til arbeidsforholdet._





URI: [adm:personalleder](https://schema.fintlabs.no/administrasjon/personalleder)
Alias: personalleder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](personalressurs.md) |
| Domain Of | [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:personalleder](https://schema.fintlabs.no/administrasjon/personalleder) |

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
| self | adm:personalleder |
| native | https://schema.fintlabs.no/administrasjon/:personalleder |




## LinkML Source

<details>
```yaml
name: personalleder
description: Personalleiar til arbeidsforholdet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:personalleder
alias: personalleder
owner: Arbeidsforhold
domain_of:
- Arbeidsforhold
range: Personalressurs

```
</details>