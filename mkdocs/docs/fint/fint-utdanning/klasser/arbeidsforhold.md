

# Slot: arbeidsforhold 


_Referanse til Arbeidsforhold i Administrasjon-domenet._





URI: [utd:arbeidsforhold](https://schema.fintlabs.no/utdanning/arbeidsforhold)
Alias: arbeidsforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Undervisningsforhold](Undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Undervisningsforhold](Undervisningsforhold.md) |
| Slot URI | [utd:arbeidsforhold](https://schema.fintlabs.no/utdanning/arbeidsforhold) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Undervisningsforhold](Undervisningsforhold.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:arbeidsforhold |
| native | https://schema.fintlabs.no/utdanning/:arbeidsforhold |




## LinkML Source

<details>
```yaml
name: arbeidsforhold
description: Referanse til Arbeidsforhold i Administrasjon-domenet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:arbeidsforhold
alias: arbeidsforhold
owner: Undervisningsforhold
domain_of:
- Undervisningsforhold
range: uriorcurie
required: true

```
</details>